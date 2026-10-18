import numpy as np

# SWIADEK DLA par.7.2 MONOGRAFII, czlon "nie wynika stad jej CIAGLOSC"
#
# W 007 par.2 zapisalem: "konstruowalne mechanizmem z par.2.3 (faktoryzacja przez redukcje,
# ktora jest ciagla bijekcja, lecz nie jest odwzorowaniem ilorazowym), ale NIE SKONSTRUOWALEM
# go. Potrzeba ciaglego U_t i takiej redukcji jednoczesnie, a przyklad [0,2pi) -> S^1 z par.2.3
# dotyczy tau-bar, nie V_t, wiec nie przenosi sie wprost."
#
# Blokada byla pozorna. Szukalem polgrupy OBROTU na [0,2pi), ktora faktycznie nie jest ciagla
# (zawija sie). Ale zadna reguła nie wymaga obrotu. Kontrakcja wystarcza.
#
# KONSTRUKCJA
#   X  = [0, 2pi) z topologia zwykla
#   U_t(theta) = theta * e^{-t}            polgrupa kontrakcji, ciagla LACZNIE w (t, theta)
#   r(theta) = e^{i theta},  Y0 = r(X) = S^1    ciagla BIJEKCJA, nie homeomorfizm
#   V_t := r U_t r^{-1},  czyli  V_t(e^{i theta}) = e^{i theta e^{-t}}
#
# Wtedy V_t r = r U_t z definicji, a V_t jest NIECIAGLE w punkcie 1 = r(0) dla kazdego t > 0:
#   V_t(1) = 1,  natomiast  lim_{theta -> 2pi^-} V_t(e^{i theta}) = e^{2 pi i e^{-t}} != 1.
# Skok na S^1:  |e^{2 pi i e^{-t}} - 1| = 2 |sin(pi e^{-t})|.

def U(t, th):  return th*np.exp(-t)
def r(th):     return np.exp(1j*th)
def V(t, th):  return np.exp(1j*U(t, th))      # V_t dziala na r(theta)

print("TABELA S1  U_t jest poprawna polgrupa na [0, 2pi)")
rng = np.random.default_rng(201)
th = rng.uniform(0, 2*np.pi, 20000); s = rng.uniform(0, 5, 20000); t = rng.uniform(0, 5, 20000)
print(f"  U_s U_t = U_(s+t):  max blad = {np.max(np.abs(U(s, U(t, th)) - U(s+t, th))):.3e}")
print(f"  U_0 = id:           max blad = {np.max(np.abs(U(0.0, th) - th)):.3e}")
print(f"  U_t([0,2pi)) c [0,2pi):  max = {np.max(U(t, th)):.9f} < {2*np.pi:.9f}  -> {np.max(U(t,th)) < 2*np.pi}")
print(f"  U_t ciagla lacznie: |U(t,a) - U(t',a')| <= |a-a'| + 2pi|t-t'| (Lipschitz) — sprawdzenie:")
a1 = rng.uniform(0,2*np.pi,20000); a2 = rng.uniform(0,2*np.pi,20000)
t1 = rng.uniform(0,5,20000); t2 = rng.uniform(0,5,20000)
lhs = np.abs(U(t1,a1) - U(t2,a2)); rhs = np.abs(a1-a2) + 2*np.pi*np.abs(t1-t2)
print(f"    naruszen: {int(np.sum(lhs > rhs + 1e-12))} na 20000")

print()
print("TABELA S2  r jest ciagla bijekcja [0,2pi) -> S^1, ale r^{-1} jest nieciagla")
print("  theta           r(theta)                  |r(theta) - r(0)|")
for x in [0.0, 1e-3, np.pi, 2*np.pi-1e-3, 2*np.pi-1e-9]:
    print(f"  {x:<15.9f} {r(x).real:+.9f}{r(x).imag:+.9f}j   {abs(r(x)-r(0.0)):.3e}")
print("  r(theta) -> r(0) = 1 gdy theta -> 2pi^-, ale theta -> 2pi != 0.")
print("  Zatem r^{-1} skacze z 2pi^- do 0: nieciagla w punkcie 1. Bijekcja: tak (theta <-> e^{i theta}).")

print()
print("TABELA S3  V_t jest NIECIAGLA w punkcie 1 dla kazdego t > 0")
print("  t          V_t(1)        lim_{theta->2pi^-} V_t        skok |.|      2|sin(pi e^{-t})|")
for tv in [0.0, 0.1, 0.25, np.log(2), 1.0, 2.0, 5.0]:
    v0 = V(tv, 0.0)
    vlim = np.exp(1j*2*np.pi*np.exp(-tv))
    jump = abs(vlim - v0)
    pred = 2*abs(np.sin(np.pi*np.exp(-tv)))
    print(f"  {tv:<10.6f} {v0.real:+.6f}      {vlim.real:+.6f}{vlim.imag:+.6f}j      {jump:<13.9f} {pred:.9f}")

print()
print("TABELA S4  skok jest MAKSYMALNY przy t = ln 2 (punkty antypodyczne na S^1)")
grid = np.linspace(1e-6, 4.0, 400001)
j = 2*np.abs(np.sin(np.pi*np.exp(-grid)))
i = int(np.argmax(j))
print(f"  maksimum skoku: {j[i]:.12f} przy t = {grid[i]:.9f}")
print(f"  ln 2 = {np.log(2):.9f}   (e^{{-ln2}} = 1/2, wiec e^{{2 pi i /2}} = -1, srednica okregu)")
print(f"  roznica: {abs(grid[i]-np.log(2)):.3e};  srednica S^1 = 2")

print()
print("TABELA S5  ktora ciaglosc zawodzi — rozdzielenie przestrzennej od czasowej")
print("  (a) kazde V_t jako ODWZOROWANIE Y0 -> Y0, t > 0: NIECIAGLE (tabela S3)")
print("  (b) orbity t -> V_t(y) przy ustalonym y: CIAGLE. Sprawdzenie modulu ciaglosci:")
for y_th in [0.0, 1.0, 3.0, 2*np.pi-1e-6]:
    ts = np.linspace(0, 3, 20001)
    vals = np.exp(1j*y_th*np.exp(-ts))
    print(f"    theta = {y_th:<12.6f} max |V_(t+dt) y - V_t y| po siatce = {np.max(np.abs(np.diff(vals))):.3e}")
print("  Zawodzi zatem ciaglosc PRZESTRZENNA kazdego V_t, nie ciaglosc orbit.")
print("  To jest dokladnie to rozroznienie, ktorego zdanie par.7.2 nie precyzuje.")

print()
print("TABELA S6  KONTROLA CZULOSCI: gdy r JEST homeomorfizmem, V_t jest ciagla")
print("  X' = [0, pi], r'(theta) = e^{i theta} na polokrag gorny — r' homeomorfizm na obraz")
print("  t          max |V_t(e^{i a}) - V_t(e^{i b})| / |e^{i a} - e^{i b}|  po 200000 parach")
rng2 = np.random.default_rng(202)
for tv in [0.1, np.log(2), 1.0, 2.0]:
    a = rng2.uniform(0, np.pi, 200000); b = rng2.uniform(0, np.pi, 200000)
    m = np.abs(np.exp(1j*a) - np.exp(1j*b)) > 1e-9
    ratio = np.abs(np.exp(1j*U(tv,a[m])) - np.exp(1j*U(tv,b[m])))/np.abs(np.exp(1j*a[m]) - np.exp(1j*b[m]))
    print(f"  {tv:<10.6f} {ratio.max():.9f}   (ograniczone -> V_t Lipschitz, wiec ciagla)")
print("  Na [0, pi] nie ma punktu sklejenia, r' jest homeomorfizmem i nieciaglosc znika.")
print("  Swiadek musi tu zawodzic i zawodzi: odpowiada za niego REDUKCJA, nie polgrupa.")

print()
print("TABELA S7  KONTROLA: ta sama wielkosc na [0,2pi) MUSI byc nieograniczona")
for tv in [0.1, np.log(2), 1.0]:
    a = rng2.uniform(0, 2*np.pi, 200000); b = rng2.uniform(0, 2*np.pi, 200000)
    m = np.abs(np.exp(1j*a) - np.exp(1j*b)) > 1e-9
    ratio = np.abs(np.exp(1j*U(tv,a[m])) - np.exp(1j*U(tv,b[m])))/np.abs(np.exp(1j*a[m]) - np.exp(1j*b[m]))
    print(f"  t = {tv:<10.6f} max iloraz = {ratio.max():.6e}   (rosnie bez ograniczenia przy a->0, b->2pi)")
