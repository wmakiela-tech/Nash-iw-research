import numpy as np
import math
from scipy.linalg import expm
from scipy.integrate import quad

def opn(M): return np.linalg.norm(np.atleast_2d(M),2)

# ===== P4: niezalezna kontrola Twierdzenia A LT4 (wzor B) =====
# q(t,x0) = GP S(t) J_X x0 - G S_A(t) x0  ==  int_0^t M(t-s) C S_A(s) x0 ds
print("TABELA 5  Tw. A LT4, wzor (B): defekt tozsamosci, uklady losowe")
print("nx ny  t      |lewa|          |prawa|         |lewa-prawa|    rel")
rng = np.random.default_rng(7)
for (nx,ny) in [(3,2),(4,4),(5,3),(6,6)]:
    A = rng.normal(size=(nx,nx)); D = rng.normal(size=(ny,ny))
    B = rng.normal(size=(nx,ny)); C = rng.normal(size=(ny,nx))
    G = rng.normal(size=(1,nx));  x0 = rng.normal(size=nx)
    L = np.block([[A,B],[C,D]])
    P = np.hstack([np.eye(nx), np.zeros((nx,ny))])
    JX = np.vstack([np.eye(nx), np.zeros((ny,nx))])
    JY = np.vstack([np.zeros((nx,ny)), np.eye(ny)])
    GP = G@P
    for t in [0.3, 1.0]:
        lhs = float((GP@expm(t*L)@JX@x0)[0] - (G@expm(t*A)@x0)[0])
        def integ(s):
            M = GP@expm((t-s)*L)@JY          # M(t-s) : Y -> R
            return float((M@(C@(expm(s*A)@x0)))[0])
        rhs,_ = quad(integ, 0.0, t, limit=400, epsabs=1e-13, epsrel=1e-13)
        d = abs(lhs-rhs); rel = d/max(abs(lhs),1e-300)
        print(f"{nx}  {ny}  {t:<6.2f} {lhs:<15.8e} {rhs:<15.8e} {d:<15.3e} {rel:.3e}")

# ===== P4b: ta sama kontrola w ukladzie opoznieniowym (nieograniczony A w granicy) =====
def shiftgen(N):
    h=1.0/N; S=np.zeros((N,N))
    for i in range(N-1): S[i,i+1]=1.0
    return (S-np.eye(N))/h, h
def bump(N,lo,hi):
    h=1.0/N; x=(np.arange(N)+0.5)*h; w=np.zeros(N)
    m=(x>lo)&(x<hi); s=(x[m]-lo)/(hi-lo); w[m]=np.exp(-1.0/(s*(1-s)))
    return w/np.sqrt(np.sum(w**2)*h)
print()
print("TABELA 6  Tw. A LT4 w ukladzie opoznieniowym, eps=0.25")
print("N    t     |lewa|          |prawa|         |lewa-prawa|    rel")
for N in [40, 80]:
    A,h = shiftgen(N); D = A.copy()
    g=bump(N,0,0.25); beta=bump(N,0.75,1.0); u=bump(N,0,0.25)
    gam=bump(N,0.75,1.0); v=bump(N,0,0.25)
    G=(h*g).reshape(1,N); B=np.outer(beta,h*u); C=np.outer(gam,h*v)
    L=np.block([[A,B],[C,D]])
    P=np.hstack([np.eye(N),np.zeros((N,N))])
    JX=np.vstack([np.eye(N),np.zeros((N,N))]); JY=np.vstack([np.zeros((N,N)),np.eye(N)])
    GP=G@P; x0=bump(N,0.0,0.3)
    for t in [0.8, 1.6]:
        lhs=float((GP@expm(t*L)@JX@x0)[0]-(G@expm(t*A)@x0)[0])
        def integ(s):
            M=GP@expm((t-s)*L)@JY
            return float((M@(C@(expm(s*A)@x0)))[0])
        rhs,_=quad(integ,0.0,t,limit=300,epsabs=1e-14,epsrel=1e-12)
        d=abs(lhs-rhs); print(f"{N:<4} {t:<5.2f} {lhs:<15.8e} {rhs:<15.8e} {d:<15.3e} {d/max(abs(lhs),1e-300):.3e}")

# ===== kontrola przykladow LT4 =====
print()
print("TABELA 7  przyklady LT4, wartosci dokladne vs podane")
# Przyklad A: u''' = 0, M_t = t^2/2, R=1, T=0.4
T=0.4; eA = T**2/2; eH = np.sqrt(quad(lambda t:(t*t/2)**2,0,T)[0])
print(f"PrzykladA E_end(0.4)   wyliczone {eA:.16f}   podane 0.08")
print(f"PrzykladA E_hist(0.4)  wyliczone {eH:.16f}   podane 0.0226274169979695")
print(f"PrzykladA T^(5/2)/sqrt20 {T**2.5/np.sqrt(20):.16f}")
# Przyklad B: oscylator, M_t=sin t, T=pi
eB = abs(np.sin(np.pi)); hB = np.sqrt(quad(lambda t:np.sin(t)**2,0,np.pi)[0])
print(f"PrzykladB E_end(pi)    wyliczone {eB:.3e}       podane 0")
print(f"PrzykladB E_hist(pi)   wyliczone {hB:.16f}   sqrt(pi/2)={np.sqrt(np.pi/2):.16f}")

print()
print("TABELA 8  asymptotyka (5) LT4: E_hist(T)/T^(m+1/2) -> R||M_m||/(m! sqrt(2m+1))")
# uklad lancuchowy: m-krotne opoznienie, M_t = t^m/m!
for m in [1,2,3]:
    pred = 1.0/(math.factorial(m)*np.sqrt(2*m+1))
    print(f"m={m}  predykcja {pred:.12f}")
    for T in [0.4,0.1,0.02]:
        val = np.sqrt(quad(lambda t:(t**m/math.factorial(m))**2,0,T)[0])/T**(m+0.5)
        print(f"       T={T:<6.3f} iloraz {val:.12f}  rel.blad {abs(val-pred)/pred:.3e}")

# ===== P5: dwustronny most E_end <-> E_hist =====
print()
print("TABELA 9  cel skalarny: lambda_max(W_T) <= tr(W_T) <= r*lambda_max(W_T)")
print("uklad              r   E_hist^2=lmax   int E_end^2=tr   tr/lmax   sqrt(tr/lmax)")
def gram(Mfun, ny, T, n=4001):
    ts=np.linspace(0,T,n); W=np.zeros((ny,ny))
    Ws=np.array([np.outer(Mfun(t),Mfun(t)) for t in ts])
    for i in range(ny):
        for j in range(ny):
            W[i,j]=np.trapezoid(Ws[:,i,j],ts)
    return W
# (a) oscylator 1D: rank 1 -> rownosc
W=gram(lambda t: np.array([np.sin(t)]),1,np.pi)
lm=np.linalg.eigvalsh(W)[-1]; tr=np.trace(W)
print(f"oscylator 1D       1   {lm:<15.9f} {tr:<16.9f} {tr/lm:<9.6f} {np.sqrt(tr/lm):.6f}")
# (b) r oscylatorow o bliskich, niewspolmiernych czestosciach
for r in [2,3,5]:
    om = 1.0 + 0.011*np.arange(1,r+1)*np.array([1,np.sqrt(2),np.sqrt(3),np.sqrt(5),np.sqrt(7)])[:r]
    T = 900.0
    W=gram(lambda t: np.sin(om*t)/(om*np.sqrt(r)), r, T, n=200001)
    ev=np.linalg.eigvalsh(W); lm=ev[-1]; tr=np.trace(W)
    print(f"{r} oscylatorow (T=900) {r}   {lm:<15.9f} {tr:<16.9f} {tr/lm:<9.6f} {np.sqrt(tr/lm):.6f}")
# (c) przypadek wspolmierny: wszystkie te same czestosci -> rank 1 pomimo r wymiarow
r=5; om=np.ones(r)
W=gram(lambda t: np.sin(om*t)/(om*np.sqrt(r)), r, 10.0, n=40001)
ev=np.linalg.eigvalsh(W); lm=ev[-1]; tr=np.trace(W)
print(f"5 osc. wspolmiernych 5   {lm:<15.9f} {tr:<16.9f} {tr/lm:<9.6f} {np.sqrt(tr/lm):.6f}")
print(f"   rank numeryczny W_T = {np.linalg.matrix_rank(W,tol=1e-12*lm)}")
