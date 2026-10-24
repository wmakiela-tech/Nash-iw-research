import numpy as np

# NC-OPN-002, RUNDA 3: SWIADEK ZAMIAST PRZESZUKIWANIA (guard NC-FAL-018).
# Mechanizm zidentyfikowany analitycznie, nie przez optymalizator:
#   przy u -> 0 back-action staje sie rzutem ortogonalnym Pi = I - d d^T,
#   cykl okresowy P = exp(G*Delta) * Pi ma RANG 1, wiec
#       rho(P) = tr(P) = w^T exp(G*Delta) w,   w = d_perp,
#   czyli tempo wzrostu na pomiar to maksymalna czesc rzeczywista
#   ZAKRESU NUMERYCZNEGO propagatora.
# HIPOTEZY DO ZABICIA:
#   W1  rho(exp(G*D) Pi) = w^T exp(G*D) w dokladnie (rank-1 => rho = trace)
#   W2  dla separatora INT7, Delta=1, w=(1,1)/sqrt2:  rho = 51/e = 18.7696...
#       i to odtwarza zmierzony w K3 iloraz ~18.8 na pomiar
#   W3  PROG: sup_{t>0} max_{||w||=1} w^T exp(tG) w > 1  <=>  mu_2(G) > 0
#       (jesli znajde G z mu_2 > 0 i sup <= 1, albo mu_2 <= 0 i sup > 1, W3 pada)
#   W4  SWIADEK JAWNY: dla mu_2 > 0 jawna konfiguracja okresowa daje
#       ||c||_2 rosnace geometrycznie w m z ilorazem rho > 1 -> brak skonczonego sufitu.
#       Liczone z definicji Gramianu W, bez zadnej optymalizacji.
#   W5  KONTROLA: ta sama jawna konstrukcja przy mu_2 <= 0 NIE MOZE przekroczyc sqrt(m)
#       (twierdzenie: lam_max(W) <= m). Przekroczenie = kod zly.

GAM = 1.0

def E(G, t):
    a = 0.5*(G[0, 0] + G[1, 1]); N = G - a*np.eye(2)
    b2 = -(N[0, 0]*N[1, 1] - N[0, 1]*N[1, 0]); I = np.eye(2)
    if abs(b2) < 1e-14:
        return np.exp(a*t)*(I + t*N)
    if b2 > 0:
        b = np.sqrt(b2); return np.exp(a*t)*(np.cosh(b*t)*I + (np.sinh(b*t)/b)*N)
    b = np.sqrt(-b2); return np.exp(a*t)*(np.cos(b*t)*I + (np.sin(b*t)/b)*N)

def mu2(G):
    return float(max(np.linalg.eigvalsh((G + G.T)/2)))

def numrange_max(G, t):
    """max_{||w||=1} w^T exp(tG) w = lam_max( sym(exp(tG)) ); zwraca tez argmax w"""
    S = E(G, t); S = (S + S.T)/2
    ev, V = np.linalg.eigh(S)
    return float(ev[-1]), V[:, -1]

def gram_lam(G, e, d, ts, ss, gam=GAM):
    o = np.argsort(ts); ts = np.asarray(ts)[o]; ss = np.asarray(ss)[o]
    L = np.eye(2); t = 0.0; W = np.zeros((2, 2))
    for tj, s in zip(ts, ss):
        if tj > t:
            L = E(G, tj-t) @ L
        t = tj
        u = np.exp(-gam*s); w = (1.0-u)*(L.T @ e)
        W = W + np.outer(w, w)
        L = (np.eye(2) - (1.0-u)*np.outer(d, d)) @ L
    return float(max(np.linalg.eigvalsh((W + W.T)/2)))/gam**2

SEP = np.array([[-1., 100.], [0., -1.]])
MET = np.array([[-1.1, 4.], [1., -4.1]])
HUR = np.array([[-1., 4.], [0., -1.]])

print("W1/W2  rank-1 => rho = trace = w^T exp(G*Delta) w; swiadek dla separatora INT7")
Pi = np.eye(2) - np.outer([1., -1.]/np.sqrt(2), [1., -1.]/np.sqrt(2))
P = E(SEP, 1.0) @ Pi
rho = float(max(abs(np.linalg.eigvals(P))))
w = np.array([1., 1.])/np.sqrt(2)
print(f"  rank(Pi)                      = {np.linalg.matrix_rank(Pi)}")
print(f"  rho(exp(G)Pi)                 = {rho:.10f}")
print(f"  tr(exp(G)Pi)                  = {float(np.trace(P)):.10f}")
print(f"  w^T exp(G) w,  w=(1,1)/sqrt2  = {float(w @ E(SEP, 1.0) @ w):.10f}")
print(f"  51/e                          = {51/np.e:.10f}")
print(f"  zmierzony iloraz z K3         = 18.8 (691.39/36.79, 12974.5/691.39)")
print(f"  W1 {'OK' if abs(rho-float(np.trace(P))) < 1e-12 else 'ZALAMANE'}   "
      f"W2 {'OK' if abs(rho-51/np.e) < 1e-10 else 'ZALAMANE'}")

print()
print("W3  PROG: sup_t max_w w^T exp(tG) w > 1  <=>  mu_2(G) > 0 ?")
print("  macierz                      mu_2        sup_t numrange   arg t      werdykt")
TST = [("G=0", np.zeros((2, 2))), ("oscylator", np.array([[0., 1.], [-1., 0.]])),
       ("diag(-1,-2)", np.diag([-1., -2.])), ("Metzler M13", MET),
       ("Hurwitz [[-1,4],[0,-1]]", HUR), ("separator INT7", SEP),
       ("[[-1,2],[0,-1]] (mu_2=0)", np.array([[-1., 2.], [0., -1.]])),
       ("[[-1,1.9],[0,-1]] (mu_2<0)", np.array([[-1., 1.9], [0., -1.]])),
       ("[[-1,2.1],[0,-1]] (mu_2>0)", np.array([[-1., 2.1], [0., -1.]]))]
w3 = True
for nm, G in TST:
    ts = np.concatenate([np.linspace(1e-6, 0.05, 4000), np.linspace(0.05, 30, 6000)])
    vals = np.array([numrange_max(G, t)[0] for t in ts])
    i = int(np.argmax(vals)); sup = float(vals[i])
    pos_mu = mu2(G) > 1e-12; pos_sup = sup > 1 + 1e-12
    ok = (pos_mu == pos_sup)
    w3 = w3 and ok
    print(f"  {nm:<28} {mu2(G):+.6f}  {sup:<16.9f} {ts[i]:<10.5f} "
          f"{'zgodne' if ok else 'ROZBIEZNE -> W3 PADA'}")
print(f"  W3 {'POTWIERDZONE na tej probce' if w3 else 'ZALAMANE'}")

print()
print("W4  SWIADEK JAWNY (bez optymalizacji): okresowa konfiguracja, u->0, d=w_perp")
print("  macierz            Delta   rho      m    ||c||_2        ||c||/rho^(m-1)   M(G)")
for nm, G in [("separator INT7", SEP), ("Hurwitz", HUR), ("Metzler M13", MET)]:
    ts_ = np.linspace(1e-4, 8, 20000)
    vv = np.array([numrange_max(G, t)[0] for t in ts_])
    i = int(np.argmax(vv)); D = float(ts_[i]); r, wst = numrange_max(G, D)
    d = np.array([-wst[1], wst[0]]); e = wst/np.linalg.norm(wst)
    Mg = max(float(np.sqrt(max(np.linalg.eigvalsh(E(G, t).T @ E(G, t))))) for t in np.linspace(0, 40, 8000))
    for m in [1, 2, 4, 8]:
        tt = D*np.arange(1, m+1); ss = np.full(m, 60.0)
        c = np.sqrt(gram_lam(G, e, d, tt, ss))
        print(f"  {nm:<18} {D:<7.4f} {r:<8.4f} {m:<4} {c:<14.6g} {c/r**(m-1):<17.6g} {Mg:.6g}")

print()
print("W5  KONTROLA: ta sama konstrukcja przy mu_2 <= 0 nie moze przekroczyc sqrt(m)")
for nm, G in [("G=0", np.zeros((2, 2))), ("oscylator", np.array([[0., 1.], [-1., 0.]])),
              ("diag(-1,-2)", np.diag([-1., -2.])),
              ("[[-1,1.9],[0,-1]]", np.array([[-1., 1.9], [0., -1.]]))]:
    bad = []
    for m in [1, 2, 4, 8, 16]:
        best = 0.0
        for D in np.linspace(1e-3, 5, 60):
            r, wst = numrange_max(G, D)
            d = np.array([-wst[1], wst[0]])
            for ee in (wst, d, np.array([1., 0.]), np.array([1., 1.])/np.sqrt(2)):
                for dd in (d, wst, np.array([0., 1.])):
                    v = np.sqrt(gram_lam(G, ee/np.linalg.norm(ee), dd/np.linalg.norm(dd),
                                         D*np.arange(1, m+1), np.full(m, 60.0)))
                    best = max(best, v)
        ok = best <= np.sqrt(m) + 1e-9
        bad.append(not ok)
        print(f"  {nm:<18} m={m:<3} max={best:<12.8f} sqrt(m)={np.sqrt(m):<11.8f} {'OK' if ok else 'TWIERDZENIE NARUSZONE'}")
    if any(bad):
        print("  >>> W5 ZALAMANE: twierdzenie lam_max(W) <= m jest FALSZYWE albo kod zly")
