import numpy as np
# Czy "redukcja rangi 1" jest ogolna, czy TYLKO n=2?
# Pi = I - d d^T ma range n-1. Dla n=2 to 1, wiec rho(P)=tr(P). Dla n>2 NIE.
rng=np.random.default_rng(7)
for n in (2,3,4,6):
    G=rng.normal(0,1,(n,n)); G=G-1.5*np.eye(n)*0  # dowolna
    d=rng.normal(0,1,n); d/=np.linalg.norm(d)
    Pi=np.eye(n)-np.outer(d,d)
    P=np.linalg.matrix_power(np.eye(n),1)@(__import__('scipy.linalg',fromlist=['expm']).expm(0.7*G))@Pi
    rho=max(abs(np.linalg.eigvals(P))); tr=abs(np.trace(P))
    w=d  # d_perp nieokreslone jednoznacznie dla n>2
    print(f"n={n}: rank(Pi)={np.linalg.matrix_rank(Pi)}  rank(P)={np.linalg.matrix_rank(P)}  "
          f"rho={rho:.6f}  |tr|={tr:.6f}  rho==tr? {abs(rho-tr)<1e-9}")
print()
print("Wniosek: formula rho = tr = w^T e^{G*Delta} w opiera sie na rank(P)=1,")
print("co zachodzi WYLACZNIE przy n=2. Dla n>2 d_perp nie jest nawet kierunkiem, lecz podprzestrzenia.")
