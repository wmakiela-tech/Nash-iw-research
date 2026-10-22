"""INT8 ROT009: synthetic finite-matrix instrument + pathwise NONMAP checks.
No real hardware or NASH physical interpretation. Requires numpy.
"""
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.diag([1,-1]).astype(complex)

def instrument(s):
    assert 0 < s < 1
    out = {}
    for y in [-1, 1]:
        effect = (I + y*s*Z)/2
        root = np.diag(np.sqrt(np.diag(effect).real))
        out[y] = [np.sqrt(1-s/2)*root, np.sqrt(s/2)*X@root]
    return out

def cp_map(kraus, rho):
    return sum((K@rho@K.conj().T for K in kraus), np.zeros_like(rho))

def run():
    for s in (.10, .55, .95):
        K = instrument(s)
        total = sum((A.conj().T@A for ks in K.values() for A in ks),
                    np.zeros((2,2),complex))
        assert np.allclose(total,I,atol=1e-13)
        for theta in (-.90, 0., .37, .83):
            rho = (I+theta*Z)/2
            first = {y:cp_map(K[y],rho) for y in K}
            p={y:np.trace(first[y]).real for y in K}
            output=sum(first.values())
            assert all(np.linalg.eigvalsh(x).min()>=-1e-13 for x in first.values())
            assert all(np.isclose(p[y],(1+y*s*theta)/2) for y in K)
            assert np.isclose(sum(y*p[y] for y in K),s*theta)
            assert np.isclose(np.trace(Z@output).real,(1-s)*theta)
            assert np.isclose(np.trace(X@output).real,0.)
            assert np.isclose(np.trace(Y@output).real,0.)
            for y in K:
                posterior = (1-s)*(theta+y*s)/(1+y*s*theta)
                assert np.isclose(np.trace(Z@first[y]).real/p[y],posterior)
            joint={(a,b):np.trace(cp_map(K[b],first[a])).real
                   for a in K for b in K}
            ey2=sum(b*pr for (a,b),pr in joint.items())
            ey1y2=sum(a*b*pr for (a,b),pr in joint.items())
            assert np.isclose(sum(joint.values()),1.)
            assert np.isclose(ey2,s*(1-s)*theta)
            assert np.isclose(ey1y2,s*s*(1-s))
            cov = ey1y2-(s*theta)*ey2
            assert np.isclose(cov,s*s*(1-s)*(1-theta*theta))
            FI=s*s/(1-s*s*theta*theta)
            assert FI<=1/(1-theta*theta)+1e-12
        for P,expected in ((X,np.sqrt(1-s*s)),
                           (Y,(1-s)*np.sqrt(1-s*s)),
                           (Z,1-s)):
            image=sum((cp_map(K[y],P) for y in K),np.zeros((2,2),complex))
            assert np.allclose(image,expected*P,atol=1e-12)

        # channel F_p has Choi support vec(I),vec(X);
        # hence each refinement effect is in span(I,X), orthogonal to Z.
        for a,b in ((1.+.3j,.5-1j),(-.2+1.2j,.7+.4j)):
            W=a*I+b*X
            eff=W.conj().T@W
            assert abs(np.trace(eff@Z))<1e-12
        print(f"s={s:.2f}: kraus TP, restricted reset, posteriors, 2-shot covariance PASS")
    print("ALL_PASS; mathematical qubit instrument only; no device realization")

if __name__=="__main__":
    run()
