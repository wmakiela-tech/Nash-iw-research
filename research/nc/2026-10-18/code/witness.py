import numpy as np
from scipy.integrate import quad

# Weryfikacja SWIADKOW non-mapow monografii. Kazdy blok liczy swiadka niezaleznie
# od tekstu i porownuje z wartoscia, ktora tekst podaje.
# Tabele, bez tekstu interpretacyjnego w print.

print("TABELA W1  [R1 #3] defekt kompresji: C(ST) vs C(S)C(T)")
# X=Y=C, H=C^2, P=(1,0), J=(1,0)^T  => C(T)=T_11
T=np.array([[1.,0.],[1.,1.]]); S=np.array([[1.,1.],[0.,1.]])
c=lambda M: M[0,0]
print(f"  c(T)={c(T):.0f}  c(S)={c(S):.0f}  c(S)c(T)={c(S)*c(T):.0f}")
print(f"  c(ST)={c(S@T):.0f}   tekst podaje 2")
print(f"  c(TS)={c(T@S):.0f}   tekst podaje 1")
Q=np.eye(2)-np.outer([1,0],[1,0])
print(f"  tozsamosc PSQTJ = {(np.array([[1.,0.]])@S@Q@T@np.array([[1.],[0.]]))[0,0]:.0f}  vs c(ST)-c(S)c(T) = {c(S@T)-c(S)*c(T):.0f}")

print()
print("TABELA W2  [R1 Kontrprz.1] BC=0 ale BDC=1, K(t)=t")
B=np.array([[1.,0.]]); C=np.array([[0.],[1.]]); D=np.array([[0.,1.],[0.,0.]])
from scipy.linalg import expm
print(f"  BC   = {float((B@C).item()):.0f}   tekst: 0")
print(f"  BDC  = {float((B@D@C).item()):.0f}   tekst: 1")
for t in [0.5,1.0,2.0]:
    print(f"  K({t}) = {float((B@expm(t*D)@C).item()):.6f}   tekst: t = {t}")

print()
print("TABELA W3  [R1 Kontrprz.3] wszystkie tau B D^k C = 0, ale tau A B C != 0")
A=np.array([[0.,1.],[0.,0.]]); B3=np.array([[0.],[1.]]); C3=np.array([[1.,0.]]); tau=np.array([[1.,0.]])
D3=np.zeros((1,1))
print("  k   tau B D^k C")
M=np.eye(1)
for k in range(4):
    print(f"  {k}   {float((tau@B3@M@C3@np.array([[1.],[0.]])).item()):.6e}")
    M=M@D3
print(f"  tau A B C (na x0=(1,0)) = {float((tau@A@B3@C3@np.array([[1.],[0.]])).item()):.0f}   tekst: 1")
# tau x(t) = 1 + t^3/6 + O(t^6)
L=np.block([[A,B3],[C3,D3]])
for t in [0.1,0.3]:
    x=expm(t*L)@np.array([1.,0.,0.]); pred=1+t**3/6
    print(f"  t={t}  tau x(t)={x[0]:.9f}  1+t^3/6={pred:.9f}  roznica={abs(x[0]-pred):.2e}")

print()
print("TABELA W4  [R2 Przykl.2.4] dokladny modul Holdera dla r(x)=x^3, tau(x)=x")
print("  delta   omega(delta) zmierzone   (4 delta)^(1/3)")
for d in [0.05,0.2,0.5,1.0,2.0]:
    best=0.0
    xs=np.linspace(-1,1,20001)
    for x in xs[::7]:
        lo,hi=-1,1
        # znajdz x' z |x^3 - x'^3| <= d maksymalizujace |x-x'|
        xp=np.linspace(-1,1,4001)
        ok=np.abs(x**3-xp**3)<=d+1e-15
        if ok.any(): best=max(best,np.max(np.abs(x-xp[ok])))
    print(f"  {d:<7.2f} {best:<22.6f} {(4*d)**(1/3):.6f}")

print()
print("TABELA W5  [R2 #17] ciagla bijekcja [0,2pi)->S^1 nie zachowuje topologii")
print("  n      tau_bar(y_n)      tau_bar(1)=0")
for n in [10,100,10000]:
    print(f"  {n:<6} {2*np.pi-1/n:<17.9f} 0")

print()
print("TABELA W6  [R3 #39] stany Bella: te same marginesy, rozne wyjscia po CNOT")
k0=np.array([1,0]); k1=np.array([0,1])
phip=(np.kron(k0,k0)+np.kron(k1,k1))/np.sqrt(2)
phim=(np.kron(k0,k0)-np.kron(k1,k1))/np.sqrt(2)
def marg_A(v):
    R=np.outer(v,v.conj()).reshape(2,2,2,2)
    return np.trace(R,axis1=1,axis2=3)
CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=float)
print(f"  marginesy A: Phi+ {np.round(marg_A(phip),6).tolist()}   Phi- {np.round(marg_A(phim),6).tolist()}")
for nm,v in [("Phi+",phip),("Phi-",phim)]:
    out=CNOT@v; rB=np.trace(np.outer(out,out.conj()).reshape(2,2,2,2),axis1=0,axis2=2)
    plus=np.array([1,1])/np.sqrt(2); minus=np.array([1,-1])/np.sqrt(2)
    print(f"  {nm}: po CNOT stan B = {np.round(rB,6).tolist()}  <+|rB|+>={float(plus@rB@plus):.6f}  <-|rB|->={float(minus@rB@minus):.6f}")

print()
print("TABELA W7  [R5 Tw.5.2] brak polgrupowosci: Phi_2=id, Phi_1 o Phi_1 = Phi_1 != id")
# U = CNOT z kontrola na srodowisku; sigma_E = I/2
I2=np.eye(2); X=np.array([[0.,1.],[1.,0.]])
P0=np.diag([1.,0.]); P1=np.diag([0.,1.])
U=np.kron(I2,P0)+np.kron(X,P1)       # S tensor E
sE=I2/2
def Phi(rho,n):
    Un=np.linalg.matrix_power(U,n)
    full=Un@np.kron(rho,sE)@Un.conj().T
    return np.trace(full.reshape(2,2,2,2),axis1=1,axis2=3)
r0=np.outer(k0,k0).astype(float)
print(f"  rho0        = {np.round(r0,6).tolist()}")
print(f"  Phi_1(rho0) = {np.round(Phi(r0,1),6).tolist()}   tekst: I/2")
print(f"  Phi_2(rho0) = {np.round(Phi(r0,2),6).tolist()}   tekst: rho0 (Phi_2=id)")
print(f"  Phi_1(Phi_1(rho0)) = {np.round(Phi(Phi(r0,1),1),6).tolist()}")

print()
print("TABELA W8  [R5 Tw.5.6] transpozycja: dodatnia, nie CP; wartosc wlasna -1/2")
J=np.zeros((4,4))
for i in range(2):
    for j in range(2):
        E=np.zeros((2,2)); E[i,j]=1
        J+=np.kron(E,E.T)
print(f"  wartosci wlasne operatora Choi transpozycji / 2: {np.round(np.linalg.eigvalsh(J/2),6).tolist()}   tekst: -1/2 obecne")

print()
print("TABELA W9  [R6 Tw.6.5] ta sama dawka, rozna obserwabla koncowa")
r,a,h,T=1.0,0.2,1.0,5.0
def xT(early):
    if early:
        xh=(a/r)*(1-np.exp(-r*h));  return xh*np.exp(-r*(T-h))
    else:
        return (a/r)*(1-np.exp(-r*h))
print(f"  x_early(T) = {xT(True):.9f}")
print(f"  x_late(T)  = {xT(False):.9f}")
print(f"  iloraz     = {xT(False)/xT(True):.6f}   wzor e^{{r(T-h)}} = {np.exp(r*(T-h)):.6f}   tekst: >54")

print()
print("TABELA W10  [R7 Przykl.7.3] oscylator: M(pi)=0 ale q(pi,1)=-2")
Mt=lambda t: np.sin(t)
q=lambda t: quad(lambda s: -np.sin(t-s),0,t)[0]
for t in [np.pi/2,np.pi]:
    print(f"  t={t:.6f}  M(t)={Mt(t):.3e}  q(t,1)={q(t):.9f}  cos(t)-1={np.cos(t)-1:.9f}")
