import numpy as np

# WERYFIKACJA LICZB MT13 — mt13_nc_active_research_weighted_yield_sufficiency_001
# TRYB: NONBLIND. Przeczytalem dowod MT13 przed wlasnym podejsciem (patrz zwrot NC 018).
# Dwie drogi: (a) ich wzory zamkniete, (b) niezalezna calkowanie ODE. Jesli sie rozejda,
# to jest wynik.

T, GAMMA, LAM, KAP = 2.0, 2.0, 1.0, 0.1
n0, X0 = 0.0, 0.1
D = 0.1
A = [0.0, 0.7, 1.4]          # starty impulsow

def Q(r, a, d=D, Tt=T):
    return np.exp(-r*(Tt-a))*(np.exp(r*d)-1.0)/(r*d)

q = np.array([Q(GAMMA, a) for a in A])
w = np.array([KAP*GAMMA/(GAMMA-LAM)*(Q(LAM, a) - Q(GAMMA, a)) for a in A])

print("TABELA T1  wspolczynniki q_i i w_i ze wzorow MT13")
for i,(qq,ww) in enumerate(zip(q,w)):
    print(f"  impuls {i+1} (start {A[i]:.1f}):  q = {qq:.15f}   w = {ww:.15f}")

c = np.array([q[1]-q[2], q[2]-q[0], q[0]-q[1]])
c = c/np.max(np.abs(c))
Sp = 1.0 + c/2.0
Sm = 1.0 - c/2.0
print()
print("TABELA T2  wagi zrodel wobec wartosci podanych przez MT13")
print(f"  S+ policzone  = {np.round(Sp,9).tolist()}")
print(f"  S+ MT13       = [0.598908056, 1.5, 0.901091944]")
print(f"  S- policzone  = {np.round(Sm,9).tolist()}")
print(f"  S- MT13       = [1.401091944, 0.5, 1.098908056]")
print(f"  wszystkie dodatnie: {bool(np.all(Sp>0) and np.all(Sm>0))}")
print(f"  sumy wag: S+ = {Sp.sum():.12f}   S- = {Sm.sum():.12f}")

print()
print("TABELA T3  rownosc emisji i ocalalych — warunki konstrukcji")
print(f"  int S+ = {Sp.sum():.15f}   int S- = {Sm.sum():.15f}   roznica = {abs(Sp.sum()-Sm.sum()):.2e}")
nTp = n0*np.exp(-GAMMA*T) + float(Sp @ q)
nTm = n0*np.exp(-GAMMA*T) + float(Sm @ q)
print(f"  n(T) dla S+ = {nTp:.15f}")
print(f"  n(T) dla S- = {nTm:.15f}")
print(f"  roznica n(T) = {abs(nTp-nTm):.2e}   MT13 podaje n(T) = 0.435923686508751")
print(f"  zgodnosc z MT13: {abs(nTp-0.435923686508751):.2e}")

print()
print("TABELA T4  cel X(T) — czy rozny, jak twierdzi MT13")
XTp = X0*np.exp(-LAM*T) + float(Sp @ w)
XTm = X0*np.exp(-LAM*T) + float(Sm @ w)
print(f"  X+(T) policzone = {XTp:.15f}   MT13 = 0.133405261248882   roznica = {abs(XTp-0.133405261248882):.2e}")
print(f"  X-(T) policzone = {XTm:.15f}   MT13 = 0.121751434726216   roznica = {abs(XTm-0.121751434726216):.2e}")
print(f"  DELTA X policzone = {abs(XTp-XTm):.15f}   MT13 = 0.0116538265226661")
print(f"  roznica = {abs(abs(XTp-XTm)-0.0116538265226661):.2e}")

print()
print("TABELA T5  NIEZALEZNA kontrola przez calkowanie ODE (Runge-Kutta 4, bez wzorow MT13)")
def integruj(wagi, N=4000000):
    h = T/N
    n, X = n0, X0
    def Sfun(t):
        s = 0.0
        for a, wg in zip(A, wagi):
            if a <= t < a+D: s += wg/D
        return s
    def f(t, n, X):
        return (Sfun(t) - GAMMA*n, -LAM*X + KAP*GAMMA*n)
    intgn = 0.0
    for i in range(N):
        t = i*h
        k1 = f(t, n, X); k2 = f(t+h/2, n+h/2*k1[0], X+h/2*k1[1])
        k3 = f(t+h/2, n+h/2*k2[0], X+h/2*k2[1]); k4 = f(t+h, n+h*k3[0], X+h*k3[1])
        intgn += GAMMA*n*h
        n += h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        X += h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
    return n, X, intgn
np_, Xp_, gp = integruj(Sp)
nm_, Xm_, gm = integruj(Sm)
print(f"  n(T):  ODE S+ = {np_:.12f}   ODE S- = {nm_:.12f}   wzor = {nTp:.12f}")
print(f"  X(T):  ODE S+ = {Xp_:.12f}   wzor = {XTp:.12f}   roznica = {abs(Xp_-XTp):.2e}")
print(f"  X(T):  ODE S- = {Xm_:.12f}   wzor = {XTm:.12f}   roznica = {abs(Xm_-XTm):.2e}")
print(f"  int gamma n: S+ = {gp:.12f}   S- = {gm:.12f}   MT13 = 2.564076313491249")

print()
print("TABELA T6  wyznacznik [1, q, w] — czy trzeci moment jest niezalezny")
M = np.column_stack([np.ones(3), q, w])
det = np.linalg.det(M)
print(f"  det policzony = {det:.15f}   MT13 = -0.00364940138641307   roznica = {abs(det-(-0.00364940138641307)):.2e}")
print(f"  w w span{{1,q}}? (det = 0 oznaczaloby TAK): {'NIE' if abs(det)>1e-12 else 'TAK'}")

print()
print("TABELA T7  kontrola czulosci twierdzenia: przypadek, w ktorym w LEZY w span{1,q}")
print("  MT13: dla lambda = 0 i stalego kappa mamy w = kappa(1 - q), czyli w span{1,q}.")
w0 = np.array([KAP*(1.0 - Q(GAMMA, a)) for a in A])
M0 = np.column_stack([np.ones(3), q, w0])
print(f"  w (lambda=0) = {np.round(w0,12).tolist()}")
print(f"  det [1,q,w] = {np.linalg.det(M0):.3e}   -> {'w span (twierdzenie: cele ROWNE)' if abs(np.linalg.det(M0))<1e-12 else 'NIE w span'}")
XTp0 = X0 + float(Sp @ w0); XTm0 = X0 + float(Sm @ w0)
print(f"  X+(T) = {XTp0:.15f}   X-(T) = {XTm0:.15f}   roznica = {abs(XTp0-XTm0):.2e}")
print("  Jesli roznica ~ 0, kierunek 'if' twierdzenia MT13 jest potwierdzony na tym przykladzie.")
