import numpy as np

# WERYFIKACJA: czy przy KAZDYM phi != 0 sufit znika, czy tylko przy phi = pi/2
# poprzedza: l2c.py sha256 c677751a318fb2ed409991172cc56ffc53b0b9522102344ea07912e065a2b43a
#
# Predykcja A3 z PREREG_ALIGN byla: sufit rosnie do 1/|cos phi| i pozostaje SKONCZONY.
# Tabela A3 jej przeczy. Wyprowadzenie po fakcie:
#   jesli v _|_ d w chwili pomiaru, to ubytek amplitudy = 0, a sygnal = A |sin phi|,
#   wiec protokol zerokosztowy daje gamma||c||_2 = sqrt(k) |sin phi| sigma(s) -> inf
#   dla KAZDEGO phi != 0. Ponizej test tego wzoru na duzych k.

def rot(v, dt):
    x, y = v
    return np.array([x*np.cos(dt) + y*np.sin(dt), -x*np.sin(dt) + y*np.cos(dt)])

def run(times, strengths, th, phi, gam=1.0):
    e = np.array([np.sin(th), np.cos(th)])
    d = np.array([np.sin(th+phi), np.cos(th+phi)])
    v = np.array([0.0, 1.0]); t = 0.0; c = []; dA2 = []
    for tj, s in zip(times, strengths):
        v = rot(v, tj - t); t = tj
        u = np.exp(-gam*s)
        c.append((v @ e)*(1.0-u)/gam)
        p = v @ d; A2o = v @ v
        v = v - p*d + p*u*d
        dA2.append(A2o - v @ v)
    return np.array(c), np.array(dA2)

# chwile, w ktorych v _|_ d : v startuje wzdluz (0,1) i obraca sie z okresem 2pi.
# v(t) = (sin t, cos t).  v.d = sin t sin(th+phi) + cos t cos(th+phi) = cos(t - (th+phi)).
# zeruje sie dla t = th+phi +- pi/2 + j*pi.
def zero_cost_times(k, th, phi):
    t0 = th + phi + np.pi/2
    return np.array([t0 + j*np.pi for j in range(k)])

print("TABELA D1  protokol zerokosztowy: gamma||c||_2 wobec sqrt(k)|sin phi|sigma(s), s=1")
print("  phi/pi    k=64       k=256      k=1024     k=4096     wzor przy k=4096   suma ubytkow A^2")
s = 1.0; sg = 1-np.exp(-1.0)
for fr in [0.01, 0.05, 0.125, 0.25, 0.5]:
    phi = fr*np.pi; row = []
    for k in [64,256,1024,4096]:
        ts = zero_cost_times(k, 0.0, phi)
        c, dA = run(ts, np.full(k, s), 0.0, phi)
        row.append((np.sqrt(np.sum(c*c)), np.sum(np.abs(dA))))
    pred = np.sqrt(4096)*abs(np.sin(phi))*sg
    print("  %-9.3f " % fr + " ".join(f"{v:<10.4f}" for v,_ in row) + f" {pred:<18.4f} {row[-1][1]:.2e}")

print()
print("TABELA D2  czy przy phi=0 ten sam protokol zerokosztowy istnieje? (kontrola negatywna)")
print("  phi = 0 : v _|_ d oznacza v _|_ e, czyli sygnal rowniez zerowy")
print("  k      gamma||c||_2   suma ubytkow A^2   max |c_j|")
for k in [64, 1024, 4096]:
    ts = zero_cost_times(k, 0.0, 0.0)
    c, dA = run(ts, np.full(k, s), 0.0, 0.0)
    print(f"  {k:<6} {np.sqrt(np.sum(c*c)):<14.3e} {np.sum(np.abs(dA)):<18.3e} {np.max(np.abs(c)):.3e}")

print()
print("TABELA D3  nadmiar na pomiar: max_[stan,u] [(gamma c)^2 - dA^2] wobec |sin phi|")
print("  skan po kacie stanu psi i po u")
print("  phi/pi    zmierzony nadmiar   |sin phi|          roznica")
for fr in [0.0,0.01,0.05,0.125,0.25,0.375,0.45,0.5]:
    phi = fr*np.pi; best = -1e9
    for psi in np.linspace(0, np.pi, 4001):
        for u in [0.0,1e-6,1e-3,0.01,0.1,0.3,0.6,0.9]:
            val = (np.cos(psi)**2)*(1-u)**2 - (np.cos(psi-phi)**2)*(1-u*u)
            best = max(best, val)
    print(f"  {fr:<9.3f} {best:<19.9f} {abs(np.sin(phi)):<18.9f} {best-abs(np.sin(phi)):.2e}")

print()
print("TABELA D4  jak maly musi byc phi, zeby sufit byl zlamany przy realistycznym k")
print("  najmniejsze k, dla ktorego protokol zerokosztowy daje gamma||c||_2 > 1; s=1")
print("  phi/pi      phi [stopnie]   k potrzebne   gamma||c||_2 przy tym k")
for fr in [0.5,0.25,0.1,0.03,0.01,0.003,0.001]:
    phi = fr*np.pi
    kneed = int(np.ceil((1.0/(abs(np.sin(phi))*sg))**2))
    ts = zero_cost_times(kneed, 0.0, phi)
    c,_ = run(ts, np.full(kneed, s), 0.0, phi)
    print(f"  {fr:<11.4f} {np.degrees(phi):<15.3f} {kneed:<13} {np.sqrt(np.sum(c*c)):.6f}")
