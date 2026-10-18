import numpy as np
from scipy.optimize import minimize

# UZUPELNIENIE DO l2.py (sha256 205d51c30e47ae036f30290b374202f62fb94443e9f8b21b7309b7585a051464)
#
# WZOR WYPROWADZONY PO ZOBACZENIU TABELI L3, NIE PRZED. Dlatego test jest na punktach
# (gamma, s) NIE wystepujacych w L3, i obejmuje wartosci gamma != 1.
#
# Pomiary w antywezlach predkosci (t_j = j*pi), rowna sila s, u = e^{-gamma s}:
#   A_j = u^{j-1},  gamma c_j = u^{j-1}(1-u)
#   sum_j (gamma c_j)^2 = (1-u)^2 / (1-u^2) = (1-u)/(1+u) = tanh(gamma s / 2)
# PREDYKCJA: gamma ||c||_2 -> sqrt(tanh(gamma s/2)) przy k -> inf, i to jest SUP przy
# ustalonej sile s na pomiar (nie tylko granica protokolu antywezlowego).
#
# ZYSK Z POWTARZANIA wzgledem jednego pomiaru tej samej sily:
#   sqrt(tanh(gamma s/2)) / (1-u) = 1/sqrt(1-u^2) = 1/sqrt(1-e^{-2 gamma s})

def trace(times, strengths, gam):
    x, y, t = 0.0, 1.0, 0.0
    c = []
    for tj, s in zip(times, strengths):
        dt = tj - t
        xn = x*np.cos(dt) + y*np.sin(dt)
        yn = -x*np.sin(dt) + y*np.cos(dt)
        x, y, t = xn, yn, tj
        u = np.exp(-gam*s)
        c.append(y*(1.0-u)/gam)
        y = y*u
    return np.array(c)

def l2(times, strengths, gam):
    c = trace(times, strengths, gam); return np.sqrt(np.sum(c*c))

print("TABELA N1  wzor zamkniety sqrt(tanh(gamma s/2)) na punktach SPOZA tabeli L3")
print("  gamma   s       k=200 antywezly   sqrt(tanh(gs/2))   roznica")
for gam in [0.25, 0.5, 1.0, 2.0, 4.0]:
    for s in [0.13, 0.37, 1.7, 3.3]:
        K = 200
        ts = np.array([j*np.pi for j in range(K)])
        v = gam*l2(ts, np.full(K, s), gam)
        pred = np.sqrt(np.tanh(gam*s/2.0))
        print(f"  {gam:<7} {s:<7} {v:<17.12f} {pred:<18.12f} {v-pred:.3e}")

print()
print("TABELA N2  czy antywezly sa OPTYMALNE przy ustalonej sile s? optymalizacja po czasach")
print("  gamma=1, k=6, sily rowne s; wielostart Nelder-Mead po czasach")
print("  s       antywezly k=6      optimum po czasach   sqrt(tanh(s/2)) (kres k->inf)")
rng = np.random.default_rng(21)
for s in [0.1, 0.3, 1.0, 2.0, 5.0]:
    k = 6
    base = l2(np.array([j*np.pi for j in range(k)]), np.full(k, s), 1.0)
    best = 0.0
    for _ in range(40):
        t0 = np.sort(rng.uniform(0, 25.0, k))
        f = lambda p: -l2(np.sort(np.abs(p)), np.full(k, s), 1.0)
        r = minimize(f, t0, method='Nelder-Mead', options={'maxiter':6000,'xatol':1e-10,'fatol':1e-13})
        best = max(best, -r.fun)
    print(f"  {s:<7} {base:<18.12f} {best:<20.12f} {np.sqrt(np.tanh(s/2)):.12f}")

print()
print("TABELA N3  zysk z POWTARZANIA wzgledem jednego pomiaru tej samej sily")
print("  gamma=1; kolumna 'zmierzony' = (k=200 antywezly)/(k=1), 'wzor' = 1/sqrt(1-e^{-2s})")
print("  s        1 pomiar        k=200           zmierzony   wzor        roznica")
for s in [0.02, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0]:
    one = l2([0.0], [s], 1.0)
    K = 200
    many = l2(np.array([j*np.pi for j in range(K)]), np.full(K, s), 1.0)
    meas = many/one; pred = 1.0/np.sqrt(1.0-np.exp(-2*s))
    print(f"  {s:<8} {one:<15.9f} {many:<15.9f} {meas:<11.6f} {pred:<11.6f} {meas-pred:.2e}")

print()
print("TABELA N4  czy ART009 Tw.1 'optymalne k=1' przezywa zmiane modelu szumu?")
print("  gamma=1; przy USTALONYM budzecie calkowitym S = suma sil, najlepsze k")
print("  S        k=1         k=2         k=4         k=8         k=32        argmax")
for S in [0.1, 0.5, 1.0, 2.0, 5.0, 20.0]:
    row = []
    for k in [1,2,4,8,32]:
        ts = np.array([j*np.pi for j in range(k)])
        row.append(l2(ts, np.full(k, S/k), 1.0))
    am = [1,2,4,8,32][int(np.argmax(row))]
    print("  %-8s " % S + " ".join(f"{v:<11.7f}" for v in row) + f" k={am}")

print()
print("TABELA N5  to samo w normie inf (figura z ART009) — kontrola, ze tam k=1 wygrywa")
print("  S        k=1         k=2         k=4         k=8         k=32        argmax")
for S in [0.1, 0.5, 1.0, 2.0, 5.0, 20.0]:
    row = []
    for k in [1,2,4,8,32]:
        ts = np.array([j*np.pi for j in range(k)])
        row.append(np.max(np.abs(trace(ts, np.full(k, S/k), 1.0))))
    am = [1,2,4,8,32][int(np.argmax(row))]
    print("  %-8s " % S + " ".join(f"{v:<11.7f}" for v in row) + f" k={am}")
