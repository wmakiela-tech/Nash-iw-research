import numpy as np

# PROBLEM OTWARTY §7.5b.5 monografii: minimaks dla FIZYCZNIE OGRANICZONEJ rodziny
# obserwacji, gdy czujnik oddzialuje zwrotnie na uklad.
#
# MODEL. Oscylator z rozdz. 7 monografii, ale czujnik o wzmocnieniu a mierzy predkosc
# i przez to JA TLUMI (uczciwa reakcja zwrotna: pomiar pedu odbiera ped):
#     x' = y,   y' = -x - a*gamma*y
# Ukryte przygotowanie y0, |y0| <= R; x0 = 0 znane. Cel: x(T).
# Pomiar w chwili t_s:  b = a*y(t_s) + eta,  |eta| <= delta.
#
# beta = a*gamma/2,  omega = sqrt(1-beta^2) (albo urojona przy beta>1)
#   x(t) = y0 * h_a(t),   h_a(t) = e^{-beta t} sin(omega t)/omega
#   y(t) = y0 * g_a(t),   g_a(t) = e^{-beta t} (cos(omega t) - (beta/omega) sin(omega t))
#
# RYZYKO z Tw. 7.9 (skalarne y, jeden pomiar):
#   E(a) = max{ |h_a(T) v| : |v|<=R, |a g_a(t_s) v| <= delta }
#        = |h_a(T)| * min(R, delta/(a|g_a(t_s)|))      dla a*g_a != 0
#        = |h_a(T)| * R                                 dla a*g_a == 0

def resp(t, beta):
    """zwraca (h, g) dla tlumionego oscylatora; obsluguje beta<1, =1, >1"""
    t = np.asarray(t, dtype=float)
    if abs(beta-1.0) < 1e-12:
        h = np.exp(-t)*t
        g = np.exp(-t)*(1.0-t)
    elif beta < 1.0:
        w = np.sqrt(1.0-beta**2)
        h = np.exp(-beta*t)*np.sin(w*t)/w
        g = np.exp(-beta*t)*(np.cos(w*t)-(beta/w)*np.sin(w*t))
    else:
        s = np.sqrt(beta**2-1.0)
        h = np.exp(-beta*t)*np.sinh(s*t)/s
        g = np.exp(-beta*t)*(np.cosh(s*t)-(beta/s)*np.sinh(s*t))
    return h, g

def risk(a, gamma, T, ts, R, delta):
    beta = a*gamma/2.0
    hT,_ = resp(T, beta)
    _,gs = resp(ts, beta)
    sig = abs(a*gs)                      # czulosc pomiaru na y0
    prior = R*abs(hT)                    # niepewnosc celu BEZ pomiaru
    if sig < 1e-300:
        return prior, prior, 1.0
    E = abs(hT)*min(R, delta/sig)
    return E, prior, (E/prior if prior>0 else np.nan)

G, T, TS, R, D = 1.0, 2.0, 0.5, 1.0, 0.05

print("TABELA B1  blad minimaksowy a wzmocnienie czujnika, gamma=1, T=2, t_s=0.5, R=1, delta=0.05")
print("   a        E(a) surowy        prior R|h_a(T)|     E/prior (ulamek)   a|g_a(t_s)|")
for a in [0.0,0.1,0.5,1.0,2.0,4.0,8.0,16.0,32.0,64.0,128.0]:
    E,pr,fr = risk(a,G,T,TS,R,D)
    beta=a*G/2; _,gs=resp(TS,beta)
    print(f"  {a:<8.1f} {E:<18.9e} {pr:<19.9e} {fr:<18.6f} {abs(a*gs):.6f}")

print()
print("TABELA B2  czulosc a|g_a(t_s)| — gdzie maksimum, czyli gdzie najwiecej informacji")
print("   a        a|g_a(t_s)|       przewidywane a* = 2/(gamma t_s) = %.3f" % (2/(G*TS)))
best=(0,None)
for a in np.linspace(0.05,20,400):
    beta=a*G/2; _,gs=resp(TS,beta); v=abs(a*gs)
    if v>best[0]: best=(v,a)
for a in [1,2,3,4,5,6,8,12,20]:
    beta=a*G/2; _,gs=resp(TS,beta)
    print(f"  {a:<8} {abs(a*gs):.6f}")
print(f"  MAKSIMUM: a = {best[1]:.4f}, wartosc {best[0]:.6f}")

print()
print("TABELA B3  ulamek niepewnosci, ktory zostaje — czy ma WNETRZNE minimum?")
print("   a        E/prior")
grid=np.concatenate([np.linspace(0.02,2,100),np.linspace(2,60,200)])
vals=[risk(a,G,T,TS,R,D)[2] for a in grid]
i=int(np.argmin(vals))
for a in [0.05,0.2,0.5,1,2,3,4,6,10,20,40,60]:
    print(f"  {a:<8} {risk(a,G,T,TS,R,D)[2]:.6f}")
print(f"  MINIMUM: a = {grid[i]:.4f}, ulamek {vals[i]:.6f}   (1.0 = pomiar bezuzyteczny)")

print()
print("TABELA B4  skalowanie optimum: a* wobec 2/(gamma t_s)")
print("  gamma   t_s     a* zmierzone   2/(gamma t_s)   iloraz")
for gam in [0.5,1.0,2.0]:
    for ts in [0.25,0.5,1.0]:
        b=(0,None)
        for a in np.linspace(0.02,200,8000):
            beta=a*gam/2; _,gs=resp(ts,beta); v=abs(a*gs)
            if v>b[0]: b=(v,a)
        pred=2/(gam*ts)
        print(f"  {gam:<7} {ts:<7} {b[1]:<14.4f} {pred:<15.4f} {b[1]/pred:.4f}")

print()
print("TABELA B5  NON-MAP: surowy blad -> 0, a pomiar NIC nie mowi")
print("   a        E(a) surowy        E/prior        interpretacja liczbowa")
for a in [1.0,10.0,50.0,200.0,1000.0]:
    E,pr,fr=risk(a,G,T,TS,R,D)
    print(f"  {a:<8.1f} {E:<18.9e} {fr:<14.6f} prior={pr:.3e}")

print()
print("TABELA B6  podloga bledu wzgledem delta (czy floor skaluje sie liniowo?)")
print("  delta     min_a E/prior    a* optymalne")
for d in [0.5,0.2,0.1,0.05,0.02,0.01,0.005]:
    v=[risk(a,G,T,TS,R,d)[2] for a in grid]
    j=int(np.argmin(v))
    print(f"  {d:<9} {v[j]:<16.6f} {grid[j]:.4f}")
