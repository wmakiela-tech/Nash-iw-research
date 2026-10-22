"""PRF11 R18: exact qubit noisy-error-flag controls (NumPy)."""
import numpy as np

ID = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
rho_plus = (ID + X)/2
rho_minus = (ID - X)/2

def joint_error_flag(p, q):
    """P(error e, displayed bit b); e is row, b column."""
    return np.array([[(1-p)*(1-q), (1-p)*q],
                     [p*q, p*(1-q)]])

def instrument(p, q, rho):
    a = joint_error_flag(p, q)
    return tuple(a[0,b]*rho + a[1,b]*(Z@rho@Z) for b in (0,1))

def trace_norm(a):
    return float(np.sum(np.linalg.svd(a, compute_uv=False)))

def binary_entropy(x):
    if x in (0., 1.):
        return 0.
    return -x*np.log(x)-(1-x)*np.log(1-x)

for p in [0., .2, .5, .8, 1.]:
    for q in [0., .1, .25, .3, .5]:
        a = joint_error_flag(p,q)
        risk = float(np.minimum(a[0],a[1]).sum())
        assert np.isclose(risk, min(p,1-p,q))
        for rho in [rho_plus, rho_minus, ID/2, (ID+.2*X)/2]:
            f = instrument(p,q,rho)
            assert np.allclose(sum(f), (1-p)*rho+p*Z@rho@Z)
            assert np.isclose(sum(np.trace(x) for x in f), 1.)
            # Both recorded outcomes are independent of input state.
            assert np.allclose([np.trace(x).real for x in f],
                               a.sum(axis=0))
        f_plus = instrument(p,q,rho_plus)
        f_minus = instrument(p,q,rho_minus)
        before_D = .5 * sum(trace_norm(u-v)
                             for u,v in zip(f_plus,f_minus))
        assert np.isclose(before_D,1-2*risk)
        # Explicit MAP correction attains the universal diamond lower bound.
        result = np.zeros((2,2),complex)
        for b in (0,1):
            tmp=f_plus[b]
            if a[1,b]>a[0,b]:
                tmp=Z@tmp@Z
            result+=tmp
        assert np.allclose(result,(1-risk)*rho_plus+risk*rho_minus)
print("R18: 25 SOURCE-TYPED INSTRUMENT / MAP / TRACE-DISTANCE CHECKS PASS")

def mutual_information(p,q):
    pb=q+p*(1-2*q)
    return binary_entropy(pb)-binary_entropy(q)

print("p q posterior_MAP_error min_channel_diamond binary_target_success MI_error_record_nats")
for p,q in [(0.5,0.),(0.5,0.1),(0.5,0.25),(0.5,0.5),
            (0.2,0.1),(0.2,0.3),(0.2,0.5)]:
    r=min(p,1-p,q)
    print(f"{p:.2f} {q:.2f} {r:.6f} {2*r:.6f} {1-r:.6f} {mutual_information(p,q):.9f}")

# SAME nonselective CPTP and SAME POVM for every q when p=.5;
# verified on both orthogonal test states, plus arbitrary mixed input.
for q in np.linspace(0,.5,11):
    for rho in (rho_plus,rho_minus,ID/2,(ID+.3*X)/2):
        pair=instrument(.5,float(q),rho)
        assert np.allclose(sum(pair), (rho+Z@rho@Z)/2)
        assert np.allclose([np.trace(x).real for x in pair],[.5,.5])
print("R18: SAME CPTP + SAME POVM ACROSS NOISY SYNDROME FAMILY PASS")
