import numpy as np
import itertools

# SWIADEK DLA NON-MAPA par.2.8 MONOGRAFII:
# "Losowa redukcja informacji i fizyczna eliminacja sektora Hilberta nie sa tym samym
#  dzialaniem."
#
# Definicje przyjete (musza byc podane, bo caly non-map jest o roznicy typow):
#   GARBLING (Blackwell): ustalony pomiar M; wynik przepuszczony przez macierz
#     stochastyczna L (kolumny sumuja sie do 1). Dziala na ROZKLADZIE WYNIKOW.
#     Zbior osiagalny: { L p_M(rho) : L stochastyczna }.
#   ELIMINACJA SEKTORA: rzut P na podprzestrzen, rho -> P rho P, potem pomiar M.
#     Dziala na STANIE. Nie zachowuje sladu.
#
# KIERUNEK 1 (wlasciwy swiadek): istnieja stany o IDENTYCZNYCH statystykach M, wiec
#   nierozroznialne przez KAZDY garbling, ktore eliminacja sektora rozroznia.
#   To jest o koherencji niewidocznej dla M, NIE o utracie sladu.
# KIERUNEK 2: eliminacja traci slad, garbling nie. To jest w istocie obserwacja
#   z rozdz. 1 par.8 monografii (V rho V* zmniejsza slad) i NIE zglaszam tego jako nowego.

def dm(v):
    v = np.array(v, dtype=complex); v = v/np.linalg.norm(v)
    return np.outer(v, v.conj())

ket0 = [1,0]; ket1 = [0,1]
plus  = [1,1]; minus = [1,-1]
P0 = dm(ket0); Pp = dm(plus); Pm = dm(minus)

rho1 = dm(plus)                      # stan czysty, koherentny w bazie obliczeniowej
rho2 = 0.5*np.eye(2, dtype=complex)  # mieszanina maksymalna

M = [dm(ket0), dm(ket1)]             # pomiar referencyjny: baza obliczeniowa

def stats(rho, M):
    return np.array([np.real(np.trace(E @ rho)) for E in M])

print("TABELA Q1  oba stany sa NIEROZROZNIALNE przez pomiar referencyjny M")
print("  stan            p(0)        p(1)")
for nm, r in [("|+><+|", rho1), ("I/2   ", rho2)]:
    s = stats(r, M); print(f"  {nm}        {s[0]:.9f}  {s[1]:.9f}")
print(f"  roznica statystyk: {np.max(np.abs(stats(rho1,M)-stats(rho2,M))):.3e}")

print()
print("TABELA Q2  wiec ZADEN garbling ich nie rozrozni — skan po macierzach stochastycznych")
print("  2x2 stochastyczne L: wiersz [[1-a, b],[a, 1-b]] dla a,b w [0,1]")
rng = np.random.default_rng(101)
worst = 0.0
for _ in range(200000):
    a, b = rng.random(2)
    L = np.array([[1-a, b],[a, 1-b]])
    d = np.max(np.abs(L @ stats(rho1,M) - L @ stats(rho2,M)))
    worst = max(worst, d)
print(f"  200000 losowych L; najwieksza roznica wyjsc: {worst:.3e}")
print("  (musi byc 0 z definicji: L dziala na rozkladzie, a rozklady sa rowne)")

print()
print("TABELA Q3  eliminacja sektora JE ROZROZNIA — obserwabla: prawdopodobienstwo przezycia")
print("  rzut P        tr(P rho1 P)     tr(P rho2 P)     roznica")
for nm, P in [("P_0 (|0>)", P0), ("P_+ (|+>)", Pp), ("P_- (|->)", Pm)]:
    t1 = np.real(np.trace(P @ rho1 @ P)); t2 = np.real(np.trace(P @ rho2 @ P))
    print(f"  {nm}     {t1:.9f}      {t2:.9f}      {abs(t1-t2):.9f}")

print()
print("TABELA Q4  rozroznienie przezywa normalizacje — nie jest artefaktem utraty sladu")
print("  (to odroznia swiadka od uwagi rozdz.1 par.8, ktora JEST o sladzie)")
print("  po rzucie P_+ i RENORMALIZACJI mierzymy w bazie obliczeniowej:")
for nm, r in [("|+><+|", rho1), ("I/2   ", rho2)]:
    s = Pp @ r @ Pp; tr = np.real(np.trace(s))
    sn = s/tr
    print(f"  {nm}  tr = {tr:.6f}   po normalizacji p = {stats(sn,M)[0]:.6f}, {stats(sn,M)[1]:.6f}")
print("  Obie renormalizuja sie do tego samego stanu |+><+|. Czyli samo p po renormalizacji")
print("  NIE rozroznia — rozroznia prawdopodobienstwo przezycia, ktore jest obserwabla")
print("  operacyjna (czestosc zdarzen niezawetowanych), nie artefaktem rachunkowym.")

print()
print("TABELA Q5  kontrola czulosci: swiadek musi ZAWODZIC, gdy sektor jest wspolosiowy z M")
print("  jesli rzut komutuje z pomiarem, eliminacja da sie odtworzyc garblingiem")
print("  rzut        [tr(P rho1 P), tr(P rho2 P)]   czy rozne?   [P,M_0] = 0 ?")
for nm, P in [("P_0", P0), ("P_+", Pp)]:
    t1 = np.real(np.trace(P @ rho1 @ P)); t2 = np.real(np.trace(P @ rho2 @ P))
    comm = np.max(np.abs(P @ M[0] - M[0] @ P))
    print(f"  {nm}         [{t1:.6f}, {t2:.6f}]           {'TAK' if abs(t1-t2)>1e-9 else 'nie'}          {comm:.3e}")
print("  P_0 komutuje z M i NIE rozroznia; P_+ nie komutuje i rozroznia.")
print("  Swiadek dziala dokladnie wtedy, gdy sektor jest niewspolosiowy z pomiarem.")

print()
print("TABELA Q6  kierunek odwrotny: czy eliminacja odtwarza dowolny garbling?")
print("  garbling BSC(eps) na stanie |0><0| daje (1-eps, eps) przy sladzie 1.")
print("  eliminacja: szukamy rzutu P dajacego te statystyki PO renormalizacji i slad 1")
print("  eps      cel (1-eps, eps)    najlepszy rzut: stat po renorm.   slad   slad=1 ?")
for eps in [0.0, 0.1, 0.25, 0.5]:
    best = (1e9, None)
    for th in np.linspace(0, np.pi, 4001):
        P = dm([np.cos(th), np.sin(th)])
        s = P @ dm(ket0) @ P; tr = np.real(np.trace(s))
        if tr < 1e-12: continue
        st = stats(s/tr, M)
        err = abs(st[0]-(1-eps))
        if err < best[0]: best = (err, (st, tr))
    st, tr = best[1]
    print(f"  {eps:<8} ({1-eps:.3f}, {eps:.3f})       ({st[0]:.6f}, {st[1]:.6f})            {tr:.6f}  {'TAK' if abs(tr-1)<1e-9 else 'NIE'}")
