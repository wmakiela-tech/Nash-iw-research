#!/usr/bin/env python3
"""Mech-S10 ROT004 source-only shutdown memory discriminator.

Original Wu-Xu source commit d395183; frozen constant-background pion
subsystem ONLY. Verifies two upstream Julia Git blobs before deriving numbers.
No Julia, BlackHawk, 10D evolution, physical PBH bound or Yp calculation.

Usage:
  python3 -I mech_s10_rot004_pion_postsource_memory.py --selftest
  python3 -I mech_s10_rot004_pion_postsource_memory.py MAIN.jl PARAMETERS.jl
"""
import hashlib
import json
import math
import sys
from pathlib import Path

COMMIT="d395183674cace6c9906a8911bdeb7234ba4040d"
MAIN="b368ba55d5a493f7bc185909730f7fe5691f10d6"
PARAMS="0d7198ff3557bdbd5753000bb07a7a7405cc24f5"
TAU=2.6033e-8
GAMMA=1/TAU
C=299792458.0
HBAR=1.054571817e-34
E=1.602176634e-19
MBARN=1e-31
ETA=6.1e-10
ZETA3=1.2020569031595942854
ALPHA=1/137.035999084
M_PI=139.57039
M_P=938.27208816

SOURCE_LITERALS_MAIN=(
  "PBH_evaporated_flag = log_m_PBH_in_EU ≤ log_m_PBH_evaporated_in_EU",
  "n_PBH = PBH_evaporated_flag ? zero(n_PBH_ini) : n_PBH_ini * (a_ini / a)^3",
  "d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH",
  "d_n_π⁻_dt = d_n_π_dt_from_PBH - Γ_π⁻ * n_π⁻ -",
  "d_n_π⁺_dt = d_n_π_dt_from_PBH - Γ_π⁺ * n_π⁺ -",
  "dXₙ_dt_π = (1 - Xₙ) * n_π⁻ * σv_π⁻_pTOn(T_SM) - Xₙ * n_π⁺ * σv_π⁺_nTOp(T_SM)",
)
SOURCE_LITERALS_PAR=(
  "τ_π = 2.6033e-8 * NU.s",
  "Γ_π⁻ = Γ_π⁺ = inv(τ_π)",
  "σv_π⁺_nTOp(T) = 1.7mbarn",
  "σv_π⁻_pTOn(T) = 1.5mbarn * Fc_π⁻(T)",
  "η_B = 6.1e-10",
  "α_EM = inv(137.035999084)",
  "m_π = MeV(139.57039)",
  "m_p = MeV(938.27208816)",
)

def git_blob_sha(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def authenticate(path, expected, literals):
    raw=Path(path).read_bytes()
    found=git_blob_sha(raw)
    if found!=expected:
        raise ValueError("ORIGINAL_BLOB_SHA_MISMATCH: "+found)
    text=raw.decode("utf-8")
    for line in literals:
        if text.count(line)!=1:
            raise ValueError("SOURCE_LITERAL_NOT_UNIQUE: "+line)
    return found

def charge_coefficients(T, X):
    assert T>0 and 0<X<1
    vv=math.sqrt(T/M_PI)+math.sqrt(T/M_P)
    xx=2*math.pi*ALPHA/vv
    fc=xx/(-math.expm1(-xx))
    n_gamma=2*ZETA3/math.pi**2*(T*1e6*E/(HBAR*C))**3
    n_b=ETA*n_gamma
    A=(1-X)*n_b*1.5*fc*MBARN*C
    B=X*n_b*1.7*MBARN*C
    return A,B,fc,n_b

def postshutdown(A,B,pre_source_duration_gamma=None):
    """S and n_B cancel from ratios. gamma from the original pion lifetime.

    pre_source_duration_gamma=None: source S>0 for infinitely long before
    shutdown, so the initial pion densities are exactly steady.
    Otherwise finite S-pulse with ZERO initial pion densities, duration L
    in units of 1/gamma.
    """
    if not A>0 or not B>0 or A==B:
        raise ValueError("EXPECTED_STRICTLY_POSITIVE_AND_DISTINCT")
    if pre_source_duration_gamma is None:
        um=up=1.0
    else:
        if pre_source_duration_gamma<=0:
            raise ValueError("L_MUST_BE_POSITIVE")
        L=pre_source_duration_gamma/GAMMA
        um=-math.expm1(-(GAMMA+A)*L)
        up=-math.expm1(-(GAMMA+B)*L)
    c_minus=A*um/(GAMMA+A)
    c_plus=B*up/(GAMMA+B)
    if (c_minus-c_plus)*(A-B)<=0:
        raise AssertionError("PRESTOP_SIGN")
    tc=math.log(c_minus/c_plus)/(A-B)
    area_direct=(A*um/(GAMMA+A)**2-B*up/(GAMMA+B)**2)
    if pre_source_duration_gamma is None:
        factor=(A-B)*(GAMMA**2-A*B)/((GAMMA+A)**2*(GAMMA+B)**2)
        if not math.isclose(area_direct,factor,rel_tol=5e-12,abs_tol=1e-25):
            raise AssertionError("SHARP_INTEGRAL_FACTOR_IDENTITY")
    if tc<=0:
        raise AssertionError("NO_POSITIVE_SWITCH_TIME")
    p_at=lambda dt:c_minus*math.exp(-(GAMMA+A)*dt)-c_plus*math.exp(-(GAMMA+B)*dt)
    if (A-B)*p_at(0)<=0 or (A-B)*p_at(tc*1.01)>=0:
        raise AssertionError("SIGN_SWITCH_NEGATIVE_CONTROL_FAILED")
    return {"A_over_gamma":A/GAMMA,"B_over_gamma":B/GAMMA,
            "P_at_shutdown_over_S_over_nB":c_minus-c_plus,
            "post_sign_flip_seconds":tc,
            "post_sign_flip_over_tau":tc/TAU,
            "integrated_post_P_over_S_over_nB_times_tau":GAMMA*area_direct,
            "integrated_post_P_sign":("positive" if area_direct>0 else "negative"),
            "pre_source_duration_over_tau":pre_source_duration_gamma}

def selftest():
    ideal=postshutdown(2*GAMMA,GAMMA)
    assert math.isclose(ideal["post_sign_flip_over_tau"],math.log(4/3),rel_tol=1e-14)
    assert math.isclose(ideal["integrated_post_P_over_S_over_nB_times_tau"],-1/36,rel_tol=1e-14)
    assert math.isclose(ideal["P_at_shutdown_over_S_over_nB"],1/6,rel_tol=1e-14)
    critical=-math.log((1+math.sqrt(33))/16)
    below=postshutdown(2*GAMMA,GAMMA,critical*.5)
    above=postshutdown(2*GAMMA,GAMMA,critical*2)
    assert below["integrated_post_P_sign"]=="positive"
    assert above["integrated_post_P_sign"]=="negative"
    assert math.isclose(critical,0.8638520758182877,rel_tol=1e-13)
    A,B,fc,nb=charge_coefficients(5.,.3)
    physical=postshutdown(A,B)
    assert math.isclose(physical["post_sign_flip_seconds"],7.22128558684478e-9,rel_tol=5e-13)
    return {"synthetic_ideal":ideal,"finite_source_duration_sign_gate_tau":critical,
            "frozen_original_constants_T5_X0p3":physical,
            "T5_Fc":fc,"T5_baryon_number_density_SI":nb,
            "original_source_authenticated":False}

def main():
    if len(sys.argv)==2 and sys.argv[1]=="--selftest":
        print(json.dumps(selftest(),indent=2,sort_keys=True));return
    if len(sys.argv)!=3:
        raise SystemExit("Need MAIN.jl PARAMETERS.jl, or --selftest")
    main_sha=authenticate(sys.argv[1],MAIN,SOURCE_LITERALS_MAIN)
    par_sha=authenticate(sys.argv[2],PARAMS,SOURCE_LITERALS_PAR)
    o=selftest()
    o["original_source_authenticated"]=True
    o["upstream_commit"]=COMMIT
    o["upstream_blobs"]={"main":main_sha,"parameters":par_sha}
    o["NO_NATIVE_JULIA_BLACKHAWK_OR_10D"]=True
    print(json.dumps(o,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
