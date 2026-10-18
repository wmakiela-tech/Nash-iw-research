import numpy as np
from scipy.linalg import expm

def shiftgen(N):
    h=1.0/N; S=np.zeros((N,N))
    for i in range(N-1): S[i,i+1]=1.0
    return (S-np.eye(N))/h, h
def bump(N,lo,hi):
    h=1.0/N; x=(np.arange(N)+0.5)*h; w=np.zeros(N)
    m=(x>lo)&(x<hi); s=(x[m]-lo)/(hi-lo); w[m]=np.exp(-1.0/(s*(1-s)))
    return w/np.sqrt(np.sum(w**2)*h)

def system(N,eps):
    A,h=shiftgen(N); D=A.copy()
    g=bump(N,0,eps); beta=bump(N,1-eps,1.0); u=bump(N,0,eps)
    gam=bump(N,1-eps,1.0); v=bump(N,0,eps)
    G=(h*g).reshape(1,N); B=np.outer(beta,h*u); C=np.outer(gam,h*v)
    L=np.block([[A,B],[C,D]])
    P=np.hstack([np.eye(N),np.zeros((N,N))]); JY=np.vstack([np.zeros((N,N)),np.eye(N)])
    return dict(A=A,D=D,B=B,C=C,G=G,L=L,P=P,JY=JY,N=N,h=h)

# PROPOZYCJA NAPRAWY: kryterium na rezolwencie celu Sigma_G(lam)=GP(lam-L)^{-1}J_Y,
# nie na momentach. Predykcja: |Sigma_G(lam)| ~ exp(-lam*t_0), t_0=1-2eps.
print("TABELA 10  rezolwenta celu Sigma_G(lam) = G P (lam-L)^{-1} J_Y, eps=0.25 => t_0=0.5")
print("N     lam     |Sigma_G|        -ln|Sigma_G|/lam")
for N in [200,400]:
    s=system(N,0.25); I=np.eye(2*N)
    for lam in [20.0,40.0,80.0,160.0,320.0]:
        R=np.linalg.solve(lam*I-s['L'], s['JY'])
        val=np.linalg.norm(s['G']@s['P']@R,2)
        print(f"{N:<5} {lam:<7.0f} {val:<16.6e} {-np.log(val)/lam:.6f}")

print()
print("TABELA 11  to samo dla rezolwenty Schura pamieci Sigma(z)=B(z-D)^{-1}C")
print("N     lam     |Sigma|          -ln|Sigma|/lam")
for N in [200,400]:
    s=system(N,0.25); I=np.eye(N)
    for lam in [20.0,40.0,80.0,160.0,320.0]:
        R=np.linalg.solve(lam*I-s['D'], s['C'])
        val=np.linalg.norm(s['B']@R,2)
        print(f"{N:<5} {lam:<7.0f} {val:<16.6e} {-np.log(val)/lam:.6f}")

print()
print("TABELA 12  zaleznosc nachylenia od eps (przewidywane t_0 = 1-2eps), N=400, lam=160")
print("eps    t_0_przew   -ln|Sigma_G|/lam   -ln|Sigma|/lam")
for eps in [0.10,0.15,0.20,0.25,0.30,0.40]:
    s=system(400,eps); I2=np.eye(800); I1=np.eye(400); lam=160.0
    R2=np.linalg.solve(lam*I2-s['L'], s['JY'])
    v2=np.linalg.norm(s['G']@s['P']@R2,2)
    R1=np.linalg.solve(lam*I1-s['D'], s['C'])
    v1=np.linalg.norm(s['B']@R1,2)
    print(f"{eps:<6.2f} {1-2*eps:<11.2f} {-np.log(v2)/lam:<18.6f} {-np.log(v1)/lam:.6f}")

print()
print("TABELA 13  kontrola odwrotna: generator OGRANICZONY (A,D losowe), brak opoznienia")
print("n    lam     |Sigma_G|        -ln|Sigma_G|/lam")
rng=np.random.default_rng(11)
n=6
A=rng.normal(size=(n,n)); D=rng.normal(size=(n,n)); B=rng.normal(size=(n,n))
C=rng.normal(size=(n,n)); G=rng.normal(size=(1,n))
L=np.block([[A,B],[C,D]]); P=np.hstack([np.eye(n),np.zeros((n,n))])
JY=np.vstack([np.zeros((n,n)),np.eye(n)])
for lam in [20.0,40.0,80.0,160.0,320.0]:
    R=np.linalg.solve(lam*np.eye(2*n)-L, JY)
    val=np.linalg.norm(G@P@R,2)
    print(f"{n:<4} {lam:<7.0f} {val:<16.6e} {-np.log(val)/lam:.6f}")
