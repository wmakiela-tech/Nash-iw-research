import numpy as np
from scipy.linalg import expm
rng=np.random.default_rng(1810)
print("TIE TO CHAPTER 1's SEMIGROUP HOST (Engel-Nagel):  ||e^{tG}|| <= e^{mu(G) t}")
print("  mu(G) = largest eigenvalue of the symmetric part = logarithmic norm (euclidean)")
print("  and mu(G) <= ||G||, so the log-norm growth bound is never worse than Lipschitz.")
print()
print(f"{'n':>3} {'mu(G)':>9} {'||G||':>9} {'t':>5} {'||e^tG||':>12} {'e^{mu t}':>12} {'e^{||G|| t}':>14} {'bound ok':>9}")
for n in [3,5,8]:
    G=rng.normal(size=(n,n))
    # make it dissipative so mu<0: shift
    G=G-(np.max(np.linalg.eigvalsh((G+G.T)/2))+0.8)*np.eye(n)
    mu=np.max(np.linalg.eigvalsh((G+G.T)/2)); nrm=np.linalg.norm(G,2)
    for t in [0.5,2.0,6.0]:
        E=np.linalg.norm(expm(t*G),2)
        print(f"{n:>3} {mu:>9.4f} {nrm:>9.4f} {t:>5.1f} {E:>12.6e} {np.exp(mu*t):>12.6e} {np.exp(nrm*t):>14.4e} {str(E<=np.exp(mu*t)*(1+1e-9)):>9}")
print()
print("  -> the log-norm bound holds and is exponentially tighter than the Lipschitz bound.")
print("     This is the SAME constant that sharpens eq (7.1), so Ch1's semigroup growth bound,")
print("     Ch6's dissipative kinetics and Ch7's trajectory-fidelity estimate share ONE object.")
