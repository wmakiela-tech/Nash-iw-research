"""INT8 ROT011 — NumPy-only synthetic CP-instrument and two-time coupling checks.

Source class: Z-basis measure-and-prepare qubit instrument, with informative POVM.
Not a source-valid hardware model. Analytic diamond proof is in the paired report.
"""
import numpy as np

ID = np.eye(2, dtype=complex)
Z = np.diag([1, -1]).astype(complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGNS = (-1, 1)

def joint_conditional(s, C, y, w, z):
    return (1 + y*s*z + w*(1-s)*z + y*w*C)/4

def kraus(s, C):
    assert 0<s<1 and 0<=C<=2*min(s,1-s)+1e-14
    out = {}
    for y in SIGNS:
        out[y] = []
        for z in SIGNS:
            for w in SIGNS:
                p = joint_conditional(s,C,y,w,z)
                assert p >= -1e-14
                vz=ID[:,0 if z==1 else 1]
                vw=ID[:,0 if w==1 else 1]
                out[y].append(np.sqrt(max(0.,p))*np.outer(vw,vz.conj()))
    return out

def operation(ks, rho):
    return sum((k@rho@k.conj().T for k in ks), np.zeros((2,2),complex))

def trace_norm(h):
    return float(np.linalg.svd(h,compute_uv=False).sum())

def check(s):
    cap=2*min(s,1-s)
    all_maps={c:kraus(s,c) for c in (0, .37*cap, cap)}
    for C, inst in all_maps.items():
        TP=sum((k.conj().T@k for ks in inst.values() for k in ks),
               np.zeros((2,2),complex))
        assert np.allclose(TP,ID,atol=1e-13)
        for y in SIGNS:
            effect=sum((k.conj().T@k for k in inst[y]),
                       np.zeros((2,2),complex))
            assert np.allclose(effect,(ID+y*s*Z)/2,atol=1e-13)

        for vec in ((0.,0.,.7),(.2,.3,.4),(-.3,.15,-.2)):
            rx,ry,rz=vec
            rho=(ID+rx*X+ry*Y+rz*Z)/2
            branches={y:operation(inst[y],rho) for y in SIGNS}
            out=sum(branches.values())
            assert np.allclose(out,(ID+(1-s)*rz*Z)/2,atol=1e-13)
            assert np.allclose([np.trace(branches[y]).real for y in SIGNS],
                               [(1+y*s*rz)/2 for y in SIGNS],atol=1e-13)
            # Read y first, optionally apply X if y=-1:
            final=branches[1]+X@branches[-1]@X
            assert np.isclose(np.trace(Z@final).real,C,atol=1e-13)

        for theta in (-.8,0.,.5):
            rho=(ID+theta*Z)/2
            b1={y:operation(inst[y],rho) for y in SIGNS}
            joint={}
            for y1 in SIGNS:
                for y2 in SIGNS:
                    joint[y1,y2]=np.trace(operation(inst[y2],b1[y1])).real
                    target=(1+y1*s*theta+y2*s*(1-s)*theta+y1*y2*s*C)/4
                    assert np.isclose(joint[y1,y2],target,atol=1e-13)
            moment=sum(y1*y2*v for (y1,y2),v in joint.items())
            assert np.isclose(moment,s*C,atol=1e-13)

    A=all_maps[0]; B=all_maps[cap]
    theta=.3
    rho=(ID+theta*Z)/2
    def Ptwo(K):
        first={y:operation(K[y],rho) for y in SIGNS}
        return np.array([np.trace(operation(K[y2],first[y1])).real
                         for y1 in SIGNS for y2 in SIGNS])
    tv=.5*np.abs(Ptwo(A)-Ptwo(B)).sum()
    assert np.isclose(tv,s*cap/2,atol=1e-13)
    # Explicit flagged channel difference on any ordinary state saturates
    # the analytic diamond upper bound (trace-and-prepare factorization).
    flagged_trace=sum(trace_norm(operation(B[y],rho)-operation(A[y],rho))
                      for y in SIGNS)
    assert np.isclose(flagged_trace,cap,atol=1e-13)
    return cap,tv,flagged_trace

if __name__=="__main__":
    for s in (.2,.4,.5,.8):
        cap,tv,dia=check(s)
        print(f"s={s:.2f}, Cmax={cap:.6f}, max_crossmoment={s*cap:.6f}, "
              f"two_shot_TV={tv:.6f}, flagged_diamond={dia:.6f}: PASS")
    print("ALL_PASS / SYNTHETIC_QUANTUM_MATH_ONLY / NO_HARDWARE_CLAIM")
