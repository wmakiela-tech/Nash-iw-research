import numpy as np
from pathlib import Path
import importlib.util

# Requires the adjacent XH-S4 ROT019 reproducer and its XH018 dependency.
S=importlib.util.spec_from_file_location(
    "x19",
    Path(__file__).parents[2]/"xh-s4"/"2026-10-23"/"xh_s4_dtc0a_derivative_crosscheck_019.py"
)
m=importlib.util.module_from_spec(S); S.loader.exec_module(m)

def rms(A,s=None):
    return m.m.rms(A,s)

def one(N=31,alpha=.05):
    dx=2*np.pi/N
    s=slice(3,N-3)
    C1,C2,h,_,_,_=m.m.smooth(N)

    T1=lambda u:m.lie(C1,u,dx,"spectral")
    T2=lambda u:m.lie(C2,u,dx,"spectral")
    b=m.bracket(C1,C2,dx,"spectral")
    Tb=lambda u:m.lie(b,u,dx,"spectral")
    E=lambda u:m.m.E_lin(u,dx,alpha)

    KC=T1(E(T2(E(h))))-T2(E(T1(E(h))))-Tb(E(h))

    def comm_E_T1(u): return E(T1(u))-T1(E(u))
    def comm_E_T2(u): return E(T2(u))-T2(E(u))

    term0=Tb(E(E(h))-E(h))
    term1=T1(comm_E_T2(E(h)))
    term2=-T2(comm_E_T1(E(h)))
    rhs=term0+term1+term2

    return dict(
        N=N,
        alpha=alpha,
        KC_mask_RMS=rms(KC,s),
        RHS_mask_RMS=rms(rhs,s),
        identity_error_RMS=rms(KC-rhs,s),
        term_E2_minus_E_RMS=rms(term0,s),
        term_T1_comm_E_T2_RMS=rms(term1,s),
        term_minus_T2_comm_E_T1_RMS=rms(term2,s),
    )

if __name__=="__main__":
    rows=[one(31,a) for a in (0.,.05,.2)]
    for row in rows: print(row)
    assert rows[0]["KC_mask_RMS"] < 1e-15
    assert max(r["identity_error_RMS"] for r in rows) < 1e-14
    print("PASS")
