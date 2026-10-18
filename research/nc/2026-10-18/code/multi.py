import numpy as np

# WIELOKROTNY POMIAR Z KUMULUJACA SIE REAKCJA ZWROTNA
#
# Model z ART008, ale pomiar ma CZAS TRWANIA i tlumi PODCZAS odczytu
# (pomiar impulsowy tlumiacy PO odczycie bylby niefizyczny — przywraca
#  nieograniczone wzmocnienie, bo sygnal czytamy zanim zaburzenie zadziala).
#
# Pomiar o sile s = a*tau w okienku [t_j, t_j+tau], tau -> 0 przy s ustalonym:
#   sygnal   = y(t_j) * sigma(s),   sigma(s) = (1 - e^{-gamma s})/gamma   <- NASYCA SIE
#   przezyca = y(t_j) * e^{-gamma s}                                      <- TLUMI
# Zatem jeden pomiar wyciaga NAJWYZEJ 1/gamma sygnalu i zostawia e^{-gamma s} stanu.
# To jest budzet informacja-zaburzenie z zachowana suma.
#
# Z Tw. 7.10 monografii (adwersarialny szum |eta_j|<=delta osobno na kazdy pomiar)
# wiaze tylko NAJOSTRZEJSZE ograniczenie, wiec figura zaslugi to
#   M = max_j |G_j| sigma(s_j),      blad znormalizowany = min(1, delta/(R M)).

GAM = 1.0
sig = lambda s: (1-np.exp(-GAM*s))/GAM
sur = lambda s: np.exp(-GAM*s)

def run(times, strengths):
    """swobodna ewolucja oscylatora miedzy pomiarami; zwraca |G_j| dla kazdego pomiaru"""
    x, y = 0.0, 1.0            # y0 = 1 (wszystko proporcjonalne do y0)
    t = 0.0; G = []
    for tj, s in zip(times, strengths):
        dt = tj - t
        xn = x*np.cos(dt) + y*np.sin(dt)
        yn = -x*np.sin(dt) + y*np.cos(dt)
        x, y, t = xn, yn, tj
        G.append(abs(y))        # czulosc TEGO pomiaru na y0
        y = y*sur(s)            # reakcja zwrotna: tlumi predkosc
    return np.array(G)

def merit(times, strengths):
    G = run(times, strengths)
    return max(G[j]*sig(strengths[j]) for j in range(len(G)))

print("TABELA M1  CZASY SWOBODNE: czy wiecej niz jeden pomiar kiedykolwiek pomaga?")
print("  kres gorny z modelu: |G| <= 1 oraz sigma <= 1/gamma = %.4f" % (1/GAM))
print("  k   najlepsze M (skan)    gdzie")
rng = np.random.default_rng(3)
for k in [1,2,3]:
    best=(0,None)
    for _ in range(40000):
        ts = np.sort(rng.uniform(0, 6.0, k))
        ss = rng.uniform(0.01, 8.0, k)
        m = merit(ts, ss)
        if m>best[0]: best=(m,(np.round(ts,3).tolist(), np.round(ss,2).tolist()))
    print(f"  {k}   {best[0]:<20.6f} t={best[1][0]}  s={best[1][1]}")

print()
print("TABELA M2  CZASY OGRANICZONE do okienka wokol czasu slepego pi/2 = 1.5708")
print("  okienko [1.40, 1.75]; w nim |cos t| jest male, wiec jeden pomiar widzi malo")
W0, W1 = 1.40, 1.75
print(f"  |cos(1.40)| = {abs(np.cos(1.40)):.6f}   |cos(1.5708)| = {abs(np.cos(1.5708)):.6f}   |cos(1.75)| = {abs(np.cos(1.75)):.6f}")
best1=(0,None)
for t in np.linspace(W0,W1,2000):
    for s in [0.5,1,2,4,8,20]:
        m=merit([t],[s])
        if m>best1[0]: best1=(m,(t,s))
print(f"  JEDEN pomiar : M = {best1[0]:.6f}  przy t={best1[1][0]:.4f}, s={best1[1][1]}")

best2=(0,None)
for t1 in np.linspace(W0,W1-0.01,120):
    for t2 in np.linspace(t1+0.01,W1,120):
        for s1 in [0.5,1,2,4,8,20,50]:
            for s2 in [0.5,1,2,4,8,20,50]:
                m=merit([t1,t2],[s1,s2])
                if m>best2[0]: best2=(m,(t1,t2,s1,s2))
t1,t2,s1,s2 = best2[1]
print(f"  DWA pomiary  : M = {best2[0]:.6f}  przy t1={t1:.4f}, t2={t2:.4f}, s1={s1}, s2={s2}")
print(f"  ZYSK = {best2[0]/best1[0]:.4f} x")

print()
print("TABELA M3  rozklad zaslugi: ktory pomiar niesie informacje?")
G = run([t1,t2],[s1,s2])
print(f"  |G_1| = {G[0]:.6f}   wklad pomiaru 1 = {G[0]*sig(s1):.6f}")
print(f"  |G_2| = {G[1]:.6f}   wklad pomiaru 2 = {G[1]*sig(s2):.6f}")
print(f"  gdyby pomiar 1 NIE tlumil (s1 -> 0 w reakcji, ale czyta): ", end="")
x,y=0.0,1.0
xn=x*np.cos(t1)+y*np.sin(t1); yn=-x*np.sin(t1)+y*np.cos(t1)
d=t2-t1
G2_nodamp=abs(-xn*np.sin(d)+yn*np.cos(d))
print(f"|G_2| = {G2_nodamp:.6f}")
print(f"  czyli reakcja zwrotna pomiaru 1 zmienia |G_2| z {G2_nodamp:.6f} na {G[1]:.6f}  ({G[1]/max(G2_nodamp,1e-12):.2f} x)")

print()
print("TABELA M4  czy pierwszy pomiar jest OFIARNY? sila s1 wobec zysku")
print("  s1      |G_2|      wklad 1    wklad 2    M = max")
for s1v in [0.0,0.25,0.5,1,2,4,8,20,50]:
    G=run([t1,t2],[max(s1v,1e-12),s2])
    c1=G[0]*sig(max(s1v,1e-12)); c2=G[1]*sig(s2)
    print(f"  {s1v:<7} {G[1]:<10.6f} {c1:<10.6f} {c2:<10.6f} {max(c1,c2):.6f}")

print()
print("TABELA M5  jak zysk zalezy od szerokosci okienka wokol czasu slepego")
print("  okienko             M(1 pomiar)   M(2 pomiary)   zysk")
for lo,hi in [(1.50,1.65),(1.45,1.70),(1.40,1.75),(1.30,1.85),(1.10,2.05),(0.80,2.35)]:
    b1=max(merit([t],[20]) for t in np.linspace(lo,hi,1500))
    b2=0
    for a in np.linspace(lo,hi-0.01,70):
        for b in np.linspace(a+0.01,hi,70):
            m=merit([a,b],[50,20])
            if m>b2: b2=m
    print(f"  [{lo:.2f}, {hi:.2f}]        {b1:<13.6f} {b2:<14.6f} {b2/b1:.4f}")
