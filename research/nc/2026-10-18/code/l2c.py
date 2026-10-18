import numpy as np
from scipy.optimize import minimize

# CZY SUFIT 1/gamma JEST O REAKCJI ZWROTNEJ, CZY O JEJ WSPOLOSIOWOSCI Z ODCZYTEM
# prerejestracja: PREREG_ALIGN.md sha256 1c075b7afe970e4b3e246b63f655608c4a522348761359b72ad4cc3a755491ad
#
# v = (x,y); ewolucja swobodna = obrot.  Czujnik ma DWA kierunki:
#   odczyt        e = (sin th,        cos th)         sygnal = (v.e) sigma(s)
#   reakcja zwr.  d = (sin(th+phi),   cos(th+phi))    skladowa wzdluz d *= u = e^{-gamma s}
# ART008/009 to wylacznie phi = 0, th = 0.

def rot(v, dt):
    x, y = v
    return np.array([x*np.cos(dt) + y*np.sin(dt), -x*np.sin(dt) + y*np.cos(dt)])

def run(times, strengths, th, phi, gam):
    """zwraca (c, dA2) : wzmocnienia znakowane oraz ubytki kwadratu amplitudy"""
    e = np.array([np.sin(th),       np.cos(th)])
    d = np.array([np.sin(th+phi),   np.cos(th+phi)])
    v = np.array([0.0, 1.0]); t = 0.0
    c, dA2 = [], []
    for tj, s in zip(times, strengths):
        v = rot(v, tj - t); t = tj
        u = np.exp(-gam*s)
        c.append((v @ e)*(1.0-u)/gam)
        p = v @ d
        A2o = v @ v
        v = v - p*d + p*u*d
        dA2.append(A2o - v @ v)
    return np.array(c), np.array(dA2)

def n2(times, strengths, th, phi, gam=1.0):
    c, _ = run(times, strengths, th, phi, gam); return np.sqrt(np.sum(c*c))

print("TABELA A1  phi = pi/2 : czy ||c||_2 rosnie bez kresu?")
print("  protokol: pomiary co pi, czyli dokladnie tam gdzie v.d = 0 (zerowy ubytek amplitudy)")
print("  s = 1.0, gamma = 1, th = 0")
print("  k      gamma||c||_2    sqrt(k)*sigma(1)   suma ubytkow A^2")
s = 1.0; sg = (1-np.exp(-1.0))/1.0
for k in [1,2,4,8,16,64,256,1024]:
    ts = np.array([j*np.pi for j in range(k)])
    c, dA = run(ts, np.full(k, s), 0.0, np.pi/2, 1.0)
    print(f"  {k:<6} {np.sqrt(np.sum(c*c)):<15.6f} {np.sqrt(k)*sg:<18.6f} {np.sum(dA):.3e}")

print()
print("TABELA A2  phi = 0 : czy sufit zachodzi dla KAZDEJ kwadratury odczytu th?")
print("  skan losowy po czasach i silach, 20000 prob na kazde th")
print("  th          max gamma||c||_2    naruszen (>1+1e-9)")
rng = np.random.default_rng(31)
for th in [0.0, 0.3, 0.7853981633974483, 1.2, 1.5707963267948966, 2.5]:
    b = 0.0; viol = 0
    for _ in range(20000):
        k = int(rng.integers(1,7))
        ts = np.sort(rng.uniform(0,20.0,k))
        ss = np.exp(rng.uniform(np.log(1e-3), np.log(60.0), k))
        v = n2(ts, ss, th, 0.0)
        b = max(b, v)
        if v > 1+1e-9: viol += 1
    print(f"  {th:<11.6f} {b:<19.9f} {viol}")

print()
print("TABELA A3  posrednie phi : jak rosnie supremum. k ustalone, optymalizacja po czasach")
print("  s = 1.0, gamma = 1, th = 0; wielostart Nelder-Mead; 'zgadniete' = 1/|cos phi| x (k=1)")
print("  phi/pi    k=1        k=2        k=4        k=8        k=16       1/|cos phi|")
rng = np.random.default_rng(32)
for fr in [0.0, 0.125, 0.25, 0.375, 0.45, 0.49, 0.5]:
    phi = fr*np.pi; row = []
    for k in [1,2,4,8,16]:
        best = 0.0
        for _ in range(12):
            t0 = np.sort(rng.uniform(0, 6.0*k, k))
            f = lambda p: -n2(np.sort(np.abs(p)), np.full(k, 1.0), 0.0, phi)
            r = minimize(f, t0, method='Nelder-Mead', options={'maxiter':4000,'xatol':1e-9,'fatol':1e-12})
            best = max(best, -r.fun)
        row.append(best)
    cp = abs(np.cos(phi)); guess = (1.0/cp if cp > 1e-12 else np.inf)
    print("  %-9.3f " % fr + " ".join(f"{v:<10.6f}" for v in row) + f" {guess:.4f}")

print()
print("TABELA A4  czy przy phi=pi/2 optymalne k przestaje byc 1? ustalony budzet S = suma sil")
print("  gamma = 1, th = 0, pomiary co pi")
print("  S        k=1        k=2        k=4        k=8        k=32       argmax")
for S in [0.1, 0.5, 1.0, 2.0, 5.0, 20.0]:
    row = []
    for k in [1,2,4,8,32]:
        ts = np.array([j*np.pi for j in range(k)])
        row.append(n2(ts, np.full(k, S/k), 0.0, np.pi/2))
    am = [1,2,4,8,32][int(np.argmax(row))]
    print("  %-8s " % S + " ".join(f"{v:<10.6f}" for v in row) + f" k={am}")

print()
print("TABELA A5  tozsamosc (gamma c)^2 = dA2 * tanh(gamma s/2) : przy ktorych phi zachodzi")
print("  mierzone: max po pomiarach |(gamma c)^2 - dA2*tanh(gamma s/2)|, 4000 losowych protokolow")
print("  phi/pi    max odchylenie     max (gamma c)^2 - dA2  (dodatnie = sufit zlamany)")
rng = np.random.default_rng(33)
for fr in [0.0, 0.05, 0.125, 0.25, 0.375, 0.5]:
    phi = fr*np.pi; dev = 0.0; exc = -1e9
    for _ in range(4000):
        k = int(rng.integers(1,7))
        ts = np.sort(rng.uniform(0,20.0,k))
        ss = np.exp(rng.uniform(np.log(1e-3), np.log(60.0), k))
        c, dA = run(ts, ss, 0.0, phi, 1.0)
        dev = max(dev, np.max(np.abs(c*c - dA*np.tanh(ss/2.0))))
        exc = max(exc, np.max(c*c - dA))
    print(f"  {fr:<9.3f} {dev:<18.3e} {exc:.3e}")
