import math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp, quad

# PREREG_MT13_EVENT.md sha256 6c11af49e6f36fac3afee652eb947f606c829c9131ebd4311ed8e4f00d63a163
# Uklad i stale z mt13_nc_lt5_event_weighted_source_sufficiency_check_001.py (MT13, commit bd749bb);
# pomocnicze H i P sa ich. Jedyna zmiana badawcza: lambda jako parametr, w szczegolnosci lambda = 0.
# Pytanie: czy ART018 par.4 (bilans masy) przezywa odczyt w chwili zdarzenia.

G, MU, K, BETA, C = 2., .7, .12, .4, 1.37
A = (.05, .30, .57); WIDTH = .08; BASE = 2.; X0 = .1; TFIX = 1.0

def H(r, t): return -math.expm1(-r*t)/r
def P(r, t, a):
    hi = min(t, a+WIDTH)
    if hi <= a: return 0.
    return (math.exp(-r*(t-hi))-math.exp(-r*(t-a)))/(r*WIDTH)

q = np.array([P(G, TFIX, a) for a in A])
v = np.array([q[1]-q[2], q[2]-q[0], q[0]-q[1]]); v = v/max(abs(v))

def E(t, z): return BASE*t + sum(z[i]*max(0., min(1., (t-a)/WIDTH)) for i, a in enumerate(A))
def n(r, t, z): return BASE*H(r, t) + sum(z[i]*P(r, t, a) for i, a in enumerate(A))
def S(t, z): return BASE + sum(z[i]/WIDTH for i, a in enumerate(A) if a <= t < a+WIDTH)
def TH(t, z): return 2 - C*t + BETA/MU*(E(t, z) - n(MU, t, z))
def event(z): return brentq(lambda t: TH(t, z)-1, .7, 1.1, xtol=1e-14)

def X(t, z, lam):
    """plon w chwili t; przy lam = 0 to X0 + kappa*G*int_0^t n"""
    if lam == 0.0:
        # kappa*G*int_0^t n: z bilansu masy G*int P = cumfrac - P oraz G*int H(G,.) = t - H(G,t),
        # wiec czynnik G sie SKRACA. Wczesniejsza wersja miala K*G*(...) i byla G razy za duza;
        # blad byl NIEWIDOCZNY w ustalonym t=1 (oba zrodla maja tam rowne intGamma, wiec roznica
        # zerowa niezaleznie od prefaktora) i wyszedl dopiero w kontroli DOP853.
        return X0 + K*(BASE*(t-H(G, t)) +
                       sum(z[i]*(max(0., min(1., (t-A[i])/WIDTH)) - P(G, t, A[i])) for i in range(3)))
    return (math.exp(-lam*t)*X0 + K*G/(G-lam) *
            (BASE*(H(lam, t)-H(G, t)) + sum(z[i]*(P(lam, t, A[i])-P(G, t, A[i])) for i in range(3))))

def indep(z, lam):
    """niezalezne DOP853 z lamaniem na krawedziach impulsow; zwraca (t_zdarzenia, X, intGamma)"""
    br = sorted(set([0., 1.2] + [x for a in A for x in (a, a+WIDTH)]))
    y = np.array([0., 0., X0, 2., 0.])
    for lo, hi in zip(br[:-1], br[1:]):
        s = S((lo+hi)/2, z)
        f = lambda t, y: [s-G*y[0], s-MU*y[1], -lam*y[2]+K*G*y[0], -C+BETA*y[1], G*y[0]]
        sol = solve_ivp(f, (lo, hi), y, method='DOP853', rtol=1e-13, atol=1e-15, dense_output=True)
        assert sol.success
        if (sol.sol(lo)[3]-1)*(sol.sol(hi)[3]-1) <= 0:
            t = brentq(lambda u: sol.sol(u)[3]-1, lo, hi, xtol=1e-14)
            return t, sol.sol(t)[2], sol.sol(t)[4]
        y = sol.y[:, -1]
    raise AssertionError('brak zdarzenia')

zp, zm = .1*v, -.1*v
print("TABELA E0  wiezy konstrukcji MT13 (niezalezne od lambda)")
print(f"  kierunek v = {np.round(v,9).tolist()}   suma v = {abs(sum(v)):.2e}   q.v = {abs(q@v):.2e}")
print(f"  int S do t=1 :  z+ = {E(TFIX,zp):.15f}   z- = {E(TFIX,zm):.15f}   roznica = {abs(E(TFIX,zp)-E(TFIX,zm)):.2e}")
print(f"  ocalali n(T) :  z+ = {n(G,TFIX,zp):.15f}   z- = {n(G,TFIX,zm):.15f}   roznica = {abs(n(G,TFIX,zp)-n(G,TFIX,zm)):.2e}")
print(f"  masa reakcji :  z+ = {E(TFIX,zp)-n(G,TFIX,zp):.15f}   z- = {E(TFIX,zm)-n(G,TFIX,zm):.15f}   "
      f"roznica = {abs((E(TFIX,zp)-n(G,TFIX,zp))-(E(TFIX,zm)-n(G,TFIX,zm))):.2e}")
print(f"  dodatniosc S :  min = {min(S(t,z) for z in (zp,zm) for t in np.linspace(0,1.2,20001)):.6f}")

for lam in (1.0, 0.0):
    tp, tm = event(zp), event(zm)
    print()
    print(f"TABELA E{1 if lam else 2}  lambda = {lam}")
    print(f"  plon w USTALONEJ chwili t = 1 :  z+ = {X(TFIX,zp,lam):.15f}   z- = {X(TFIX,zm,lam):.15f}")
    print(f"     roznica = {abs(X(TFIX,zp,lam)-X(TFIX,zm,lam)):.3e}")
    print(f"  czasy zdarzenia : t+ = {tp:.15f}   t- = {tm:.15f}   rozsuniecie = {abs(tp-tm):.3e}")
    yp, ym = X(tp, zp, lam), X(tm, zm, lam)
    print(f"  plon w CHWILI ZDARZENIA :  z+ = {yp:.15f}   z- = {ym:.15f}")
    print(f"     roznica = {yp-ym:+.15f}")
    cp, xp_, ip = indep(zp, lam); cm, xm_, im = indep(zm, lam)
    print(f"  kontrola DOP853 : |dt+| = {abs(cp-tp):.2e}  |dX+| = {abs(xp_-yp):.2e}  "
          f"|dt-| = {abs(cm-tm):.2e}  |dX-| = {abs(xm_-ym):.2e}")
    if lam == 0.0:
        pred = K*quad(lambda t: G*n(G, t, zp), tm, tp, epsabs=1e-14, epsrel=1e-14)[0]
        print(f"  PROGNOZA E3  kappa * int_{{t-}}^{{t+}} Gamma  = {pred:+.15f}")
        print(f"     roznica prognozy wobec pomiaru = {abs(pred-(yp-ym)):.3e}")
        print(f"  kontrola: kappa*(intGamma+ - intGamma-) z DOP853 = {K*(ip-im):+.15f}   "
              f"roznica = {abs(K*(ip-im)-(yp-ym)):.2e}")
