import numpy as np
from scipy.integrate import dblquad, quad

# OBIEKT CIAGLY, bez dyskretyzacji:
# Sigma(lam) = int_0^1 int_0^1 g(xi) beta(s) e^{-lam (s-xi)} ds dxi   (rezolwenta nilpotentnego przesuniecia)
# M(t)       = int_0^t phi(u) du,  phi(u) = int g(xi) beta(xi+u) dxi
# g na (0,eps), beta na (1-eps,1), oba bumpy C_c^inf, nieujemne.
EPS = 0.25
def bmp(x, lo, hi):
    s = (x-lo)/(hi-lo)
    return np.where((s>0)&(s<1), np.exp(-1.0/np.clip(s*(1-s),1e-300,None)), 0.0)
NG = quad(lambda x: bmp(x,0,EPS)**2, 0, EPS, limit=400)[0]**0.5
NB = quad(lambda x: bmp(x,1-EPS,1)**2, 1-EPS, 1, limit=400)[0]**0.5
g    = lambda x: bmp(x,0,EPS)/NG
beta = lambda x: bmp(x,1-EPS,1)/NB
T0 = (1-EPS) - EPS   # odleglosc nosnikow

print("TABELA 14  Sigma(lam) obiektu ciaglego, calka podwojna, eps=0.25, t_0=0.50")
print("lam    Sigma(lam)        -ln Sigma/lam   granica gorna e^{-lam t_0}*||g||_1||beta||_inf")
g1 = quad(g,0,EPS,limit=400)[0]
binf = max(beta(x) for x in np.linspace(1-EPS,1,20001))
for lam in [10,20,40,80,160,320,640]:
    val = dblquad(lambda s,xi: g(xi)*beta(s)*np.exp(-lam*(s-xi)),
                  0, EPS, 1-EPS, 1, epsabs=1e-300, epsrel=1e-11)[0]
    ub = g1*binf*np.exp(-lam*T0)
    print(f"{lam:<6} {val:<17.9e} {-np.log(val)/lam:<15.6f} {ub:.9e}")

print()
print("TABELA 15  momenty ciagle  int g beta^{(k)}  (przewidywane dokladnie 0)")
import scipy.misc
def dk(f, x, k, h=1e-3):
    # roznica centralna rzedu k
    c = np.array([(-1)**j*__import__("math").comb(k,j) for j in range(k+1)])
    xs = np.array([x+(k/2-j)*h for j in range(k+1)])
    return np.sum(c*f(xs))/h**k
for k in [0,1,2,3,4,5]:
    val = quad(lambda x: g(x)*dk(beta,x,k), 0, EPS, limit=400)[0]
    print(f"k={k}   int g beta^(k) = {val:.6e}")

print()
print("TABELA 16  M(t) i phi(t) obiektu ciaglego")
print("t      phi(t)=int g beta(.+t)   M(t)=int_0^t phi")
def phi(u):
    return quad(lambda xi: g(xi)*beta(xi+u), 0, EPS, limit=400)[0]
for t in [0.1,0.3,0.45,0.49,0.5,0.55,0.6,0.7,0.75,0.8,0.9,1.0]:
    p = phi(t)
    M = quad(phi, 0, t, limit=400)[0]
    print(f"{t:<6.2f} {p:<24.9e} {M:.9e}")

print()
print("TABELA 17  saturacja ciagla: max_u <S_D(u)gamma, u_vec> / (||gamma|| ||u_vec||)")
print("   (gamma i u_vec sa przesunieciami tego samego bumpa o 1-eps)")
best=(0,None)
for u in np.linspace(0.6,0.9,301):
    v = quad(lambda x: g(x)*beta(x+u), 0, EPS, limit=400)[0]
    if v>best[0]: best=(v,u)
print(f"max = {best[0]:.12f} przy u = {best[1]:.4f}   (||g||=||beta||=1, wiec kres = 1)")
