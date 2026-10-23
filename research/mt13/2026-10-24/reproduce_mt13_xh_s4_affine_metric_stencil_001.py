#!/usr/bin/env python3
"""MT13/XH-S4 Q43: exact metric-local affine stencil; source-helper check when provided.
No physical NASH/GR claim; executes finite periodic grids. NumPy required.
Set DTC0A_HELPER to original retained deepseek_python_20260627_a87249.py path.
"""
import os, importlib.util, hashlib, json
import numpy as np
EXPECTED="23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801"
HELPER=os.environ.get("DTC0A_HELPER",os.path.join(os.path.dirname(__file__),"deepseek_python_20260627_a87249.py"))
def E0(h,alpha):
    if os.path.isfile(HELPER):
        sha=hashlib.sha256(open(HELPER,"rb").read()).hexdigest()
        assert sha==EXPECTED,("source_sha_mismatch",sha)
        if not hasattr(E0,"helper"):
            sp=importlib.util.spec_from_file_location("dtc_original",HELPER)
            mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
            E0.helper=mod
        return E0.helper.apply_E(h,"E_lin",2*np.pi/h.shape[0],order=2,alpha=alpha)
    print("SOURCE_HELPER_ABSENT / using equivalent independent 6-shift reference")
    out=h.copy()
    for axis in range(3):
        out+=alpha*(np.roll(h,1,axis)+np.roll(h,-1,axis)-2*h)
    return out
def shift(h,v): return np.roll(h,tuple(-int(s) for s in v),(0,1,2))
def invert_int(A):
    inv=np.rint(np.linalg.inv(A)).astype(int)
    assert np.array_equal(A@inv,np.eye(3,dtype=int))
    return inv
def adapted(h,A,alpha):
    out=h.copy();inv=invert_int(A)
    for j in range(3):
        v=inv[:,j]
        out+=alpha*(shift(h,v)+shift(h,-v)-2*h)
    return out
def pull(h,A):
    N=h.shape[0]
    idx=np.einsum("ij,jabc->iabc",A,np.indices((N,N,N)),optimize=True)%N
    shifted=h[idx[0],idx[1],idx[2]]
    return np.einsum("ai,...ab,bj->...ij",A,shifted,A,optimize=True)
def norm(h,g):
    gi=np.linalg.inv(g)
    return np.sqrt(np.mean(np.einsum("...ij,ia,jb,...ab->...",h,gi,gi,h,optimize=True)))
def TT(H,k,g):
    gi=np.linalg.inv(g);k=np.asarray(k,dtype=float);r=k@gi@k
    P=np.eye(3)-np.outer(k,gi@k)/r
    Hp=P@H@P.T
    return Hp-.5*np.sum(gi*Hp)*(g-np.outer(k,k)/r)
A=np.array([[1,1,0],[0,1,0],[0,0,1]],dtype=int)
B=np.array([[1,0,0],[0,1,1],[0,0,1]],dtype=int)
g=A.T@A; H=np.diag([0.,1.,-1.]); alpha=.05
assert np.array_equal(A.T@H@A,H)
data=[]
for N in (9,15,31,41):
    X=np.arange(N)[:,None,None]
    for m in (1,(N-1)//2):
        h=np.broadcast_to(np.cos(2*np.pi*m*X/N),(N,N,N))[...,None,None]*H
        moved=pull(h,A)
        ref=pull(E0(h,alpha),A)
        fixed=E0(moved,alpha)
        repaired=adapted(moved,A,alpha)
        frozen=float(norm(fixed-ref,g)/norm(moved,g))
        residual=float(norm(repaired-ref,g)/norm(moved,g))
        expected=4*abs(alpha)*np.sin(np.pi*m/N)**2
        assert abs(frozen-expected)<2e-13
        assert residual<1e-14
        assert np.linalg.norm(TT(H,[m,m,0],g)-H)<1e-13
        data.append(dict(N=N,m=m,frozen=frozen,metric_adapted=residual))
        print("TT",N,m,"frozen",frozen,"metric_adapted",residual)
rng=np.random.default_rng(20261024)
N=11;h=rng.normal(size=(N,N,N,3,3));h=.5*(h+np.swapaxes(h,-1,-2))
moved=pull(h,A)
err=norm(adapted(moved,A,alpha)-pull(E0(h,alpha),A),g)/norm(pull(E0(h,alpha),A),g)
assert err<5e-14
assert norm(pull(pull(h,A),B)-pull(h,A@B),np.eye(3))<5e-13
assert norm(adapted(pull(h,A@B),A@B,alpha)-pull(E0(h,alpha),A@B),np.eye(3))<5e-13
print("FULL_TENSOR_PASS",err,"TWO_SHEARS_PASS")
print("SOURCE_VALIDATED" if os.path.isfile(HELPER) else "SOURCE_HELPER_ABSENT_NOT_SOURCE_RUN")
print("PASS")
