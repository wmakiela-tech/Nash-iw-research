import numpy as np
from scipy.linalg import expm

# nilpotentna polgrupa lewych przesuniec na L^2(0,1), dyskretyzacja N komorek
# A_N = (1/h)(S - I), S = dokladne przesuniecie o jedna komorke, brzeg absorbujacy
def shiftgen(N):
    h = 1.0/N
    S = np.zeros((N,N))
    for i in range(N-1):
        S[i,i+1] = 1.0
    return (S-np.eye(N))/h, h

def bump(N, lo, hi):
    # nieujemny gladki bump na (lo,hi), znormalizowany w L^2 z waga h
    h = 1.0/N
    x = (np.arange(N)+0.5)*h
    w = np.zeros(N)
    m = (x>lo)&(x<hi)
    s = (x[m]-lo)/(hi-lo)
    w[m] = np.exp(-1.0/(s*(1-s)))
    nrm = np.sqrt(np.sum(w**2)*h)
    return w/nrm

def build(N, eps):
    A,h = shiftgen(N)
    D = A.copy()
    g    = bump(N, 0.0, eps)          # G f = <f,g>
    beta = bump(N, 1-eps, 1.0)        # ran B
    u    = bump(N, 0.0, eps)          # B y = <y,u> beta
    gam  = bump(N, 1-eps, 1.0)        # C x = <x,v> gam
    v    = bump(N, 0.0, eps)
    G = (h*g).reshape(1,N)
    B = np.outer(beta, h*u)
    C = np.outer(gam,  h*v)
    L = np.block([[A,B],[C,D]])
    return dict(A=A,D=D,B=B,C=C,G=G,L=L,h=h,N=N,
                g=g,beta=beta,u=u,gam=gam,v=v)

def opnorm(M):
    return np.linalg.norm(M,2)

# ---------- P1: momenty ----------
print("TABELA 1  pierwszy niezerowy moment pamieci B D^k C, eps=0.25, t_0=0.5")
print("N      h        m_K(pierwszy k z B D^k C != 0)   N*t_0   prog")
for N in [20,40,80,160]:
    s = build(N,0.25)
    D,B,C = s['D'],s['B'],s['C']
    M = C.copy()
    mk = None
    tol = 1e-10*opnorm(B)*opnorm(C)
    for k in range(0, 3*N):
        val = opnorm(B@M)
        if val > tol:
            mk = k; break
        M = D@M
        if not np.all(np.isfinite(M)): break
    print(f"{N:<6} {s['h']:<8.5f} {str(mk):<32} {N*0.5:<7.1f} {tol:.3e}")

print()
print("TABELA 2  pierwszy niezerowy moment widzialnosci M_k = G P L^k J_Y, eps=0.25")
print("N      m_M     |M_m|          N*t_0")
for N in [20,40,80,160]:
    s = build(N,0.25); N_=s['N']; L=s['L']; G=s['G']
    P = np.hstack([np.eye(N_), np.zeros((N_,N_))])
    JY = np.vstack([np.zeros((N_,N_)), np.eye(N_)])
    GP = G@P
    T = JY.copy(); mk=None; val=None
    tol = 1e-10*opnorm(GP)*opnorm(JY)
    for k in range(0,3*N_):
        val = opnorm(GP@T)
        if val > tol:
            mk=k; break
        T = L@T
        if not np.all(np.isfinite(T)): break
    print(f"{N:<6} {str(mk):<7} {val:<14.6e} {N*0.5:.1f}")

# ---------- P2,P3: K(t), M(t), saturacja ----------
print()
print("TABELA 3  ||K(t)|| i ||M(t)|| wzgledem t, N=400, eps=0.25, t_0=0.5")
s = build(400,0.25); N=400; L=s['L']; G=s['G']; B=s['B']; C=s['C']; D=s['D']
P = np.hstack([np.eye(N), np.zeros((N,N))])
JY = np.vstack([np.zeros((N,N)), np.eye(N)])
GP = G@P
nB, nC = opnorm(B), opnorm(C)
print("t       ||K(t)||       ||K||/(||B||||C||)   ||M(t)||")
for t in [0.0,0.1,0.2,0.3,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.9,1.0]:
    K = B@expm(t*D)@C
    M = GP@expm(t*L)@JY
    print(f"{t:<7.2f} {opnorm(K):<13.6e} {opnorm(K)/(nB*nC):<20.6f} {opnorm(M):.6e}")

print()
print("TABELA 4  saturacja max_t ||K(t)||/(||B|| ||C||), eps=0.25")
print("N      max_t ratio    argmax t")
for N in [50,100,200,400,800]:
    s2 = build(N,0.25); B2,C2,D2 = s2['B'],s2['C'],s2['D']
    nb, nc = opnorm(B2), opnorm(C2)
    best=(0.0,None)
    for t in np.linspace(0.3,1.0,71):
        r = opnorm(B2@expm(t*D2)@C2)/(nb*nc)
        if r>best[0]: best=(r,t)
    print(f"{N:<6} {best[0]:<14.6f} {best[1]:.3f}")
