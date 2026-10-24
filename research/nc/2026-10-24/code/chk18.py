import numpy as np
# Czy NC-NUM-004 (18 X) to to samo prawo co dzisiejsze T1?
# G=0, m pomiarow, e _|_ d (phi=pi/2), sila s. Predykcja: gamma||c||_2 = sqrt(m)(1-u).
def gram(m,u,phi):
    e=np.array([1.,0.]); d=np.array([np.cos(phi),np.sin(phi)])
    # d jest pod katem phi do e; phi=pi/2 => d=(0,1)
    L=np.eye(2); W=np.zeros((2,2))
    for _ in range(m):
        w=(1-u)*(L.T@e); W=W+np.outer(w,w)
        L=(np.eye(2)-(1-u)*np.outer(d,d))@L
    return float(max(np.linalg.eigvalsh((W+W.T)/2)))
u=np.exp(-1.0)
for m in (1,16,256,4096):
    v=np.sqrt(gram(m,u,np.pi/2))
    print(f"  m={m:<6} gamma||c||_2={v:<12.6f} sqrt(m)(1-u)={np.sqrt(m)*(1-u):<12.6f} "
          f"rel={abs(v-np.sqrt(m)*(1-u))/v:.2e}")
print(f"\n  NC-NUM-004 raportuje 40.46 przy k=4096;  sqrt(4096)*(1-e^-1) = {64*(1-np.exp(-1)):.6f}")
print(f"  dzisiejsze T1 mowi gamma||c||_2 <= sqrt(m) = {np.sqrt(4096):.1f}; wartosc 40.46 to {40.456/64:.6f} tego kresu = (1-u)")
print("\n  kontrola e=d (phi=0), granica m->inf: ma byc sqrt(tanh(gamma s/2)) = NC-ALG-003")
for m in (1,8,10**4):
    v=np.sqrt(gram(m,u,0.0))
    print(f"  m={m:<7} {v:.12f}   sqrt(tanh(0.5))={np.sqrt(np.tanh(0.5)):.12f}")
print(f"\n  NC-ALG-004: zysk z nieskonczonego powtarzania 1/sqrt(1-e^-2gs) = {1/np.sqrt(1-np.exp(-2.0)):.12f}")
print(f"  zmierzony iloraz m=inf / m=1 przy e=d: {np.sqrt(gram(10**4,u,0.0))/np.sqrt(gram(1,u,0.0)):.12f}")
