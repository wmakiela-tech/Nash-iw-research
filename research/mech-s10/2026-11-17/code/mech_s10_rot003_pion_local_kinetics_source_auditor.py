#!/usr/bin/env python3
"""Mech-S10 ROT003: exact frozen-background charged-pion kinetics from original Wu-Xu code.

Input: author main-scan.jl and tool_script-parameters.jl at frozen d395183...
Output: source-typed finite-time and stationary formulas, dimensionless controls.
No Julia, BlackHawk, PBH mass evolution, 10D solution, physical Yp or beta.

python3 -I mech_s10_rot003_pion_local_kinetics.py /path/main-scan.jl /path/tool_script-parameters.jl
"""
import hashlib
import json
import math
from pathlib import Path
import sys

ORIGINAL_COMMIT = "d395183674cace6c9906a8911bdeb7234ba4040d"
MAIN_BLOB = "b368ba55d5a493f7bc185909730f7fe5691f10d6"
PARAM_BLOB = "0d7198ff3557bdbd5753000bb07a7a7405cc24f5"
C_SI = 299792458.0
HBAR_SI = 1.054571817e-34
E_CHARGE_SI = 1.602176634e-19
MEV_J = E_CHARGE_SI * 1e6
ZETA3 = 1.2020569031595942854

# Original author values, all checked verbatim against hash-gated original source.
ALPHA_EM = 1.0 / 137.035999084
M_PI = 139.57039              # MeV
M_P = 938.27208816           # MeV
M_N = 939.5654205            # MeV
Q = M_N - M_P
TAU_PI = 2.6033e-8          # s
ETA_B = 6.1e-10
A0_MBARN = 1.5
B0_MBARN = 1.7
T_NUC = 0.078185270688319950  # MeV
GAMMA_PI = 1.0/TAU_PI

MAIN_REQUIRED = (
    "dXₙ_dt_π = (1 - Xₙ) * n_π⁻ * σv_π⁻_pTOn(T_SM) - Xₙ * n_π⁺ * σv_π⁺_nTOp(T_SM)",
    "d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH",
    "d_n_π⁻_dt = d_n_π_dt_from_PBH - Γ_π⁻ * n_π⁻ -",
    "d_n_π⁺_dt = d_n_π_dt_from_PBH - Γ_π⁺ * n_π⁺ -",
    "σv_π⁻_pTOn(T_SM) * (1 - Xₙ) * n_B * n_π⁻",
    "σv_π⁺_nTOp(T_SM) * Xₙ * n_B * n_π⁺",
    "n_B = η_B * n_γ",
)
PARAM_REQUIRED = (
    "m_π = MeV(139.57039)",
    "m_p = MeV(938.27208816)",
    "m_n = MeV(939.5654205)",
    "τ_π = 2.6033e-8 * NU.s",
    "Γ_π⁻ = Γ_π⁺ = inv(τ_π)",
    "η_B = 6.1e-10",
    "α_EM = inv(137.035999084)",
    "σv_π⁺_nTOp(T) = 1.7mbarn",
    "σv_π⁻_pTOn(T) = 1.5mbarn * Fc_π⁻(T)",
    "T_nuc = MeV(0.078185270688319950)",
    "vₑ = sqrt(T / mₕ) + sqrt(T / m_p)",
    "x = 2 * π * α_EM / vₑ",
    "return x / (1 - exp(-x))",
)

def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def attest(path, sha, substrings):
    raw = Path(path).read_bytes()
    got = gitblob(raw)
    if got != sha:
        raise ValueError(f"ORIGINAL_SOURCE_SHA_MISMATCH expected={sha} got={got}")
    text = raw.decode("utf-8")
    missing = [line for line in substrings if text.count(line) != 1]
    if missing:
        raise ValueError("SOURCE_CONTRACT_MISMATCH: " + repr(missing))
    return got

def fc(T):
    v = math.sqrt(T/M_PI) + math.sqrt(T/M_P)
    x = 2 * math.pi * ALPHA_EM / v
    return x / (-math.expm1(-x))

def snapshot(T, X):
    """Fixed-temperature, fixed-X, fixed-n_B local kinetic coefficients."""
    if T <= 0 or not (0 < X < 1):
        raise ValueError("DOMAIN")
    a_mb = A0_MBARN * fc(T)
    b_mb = B0_MBARN
    n_gamma = 2 * ZETA3 / math.pi**2 * (T*MEV_J/(HBAR_SI*C_SI))**3
    n_b = ETA_B * n_gamma
    # sigma*v is written as an area with c=1 by original Wu-Xu.
    A = (1-X)*n_b*a_mb*1e-31*C_SI
    B = X*n_b*b_mb*1e-31*C_SI
    gamma = GAMMA_PI
    threshold = a_mb/(a_mb+b_mb)
    n_minus_per_S = 1/(gamma+A)
    n_plus_per_S = 1/(gamma+B)
    # dX/dt pion rate per equal *one-state* injection source S.
    Psteady_per_S = (A*n_minus_per_S - B*n_plus_per_S)/n_b
    Pblind_per_S = ((A-B)*(n_minus_per_S+n_plus_per_S)/2)/n_b
    ratio = 2*gamma/(2*gamma+A+B)
    if abs(A-B) > 1e-9*max(A,B):
        if not math.isclose(Psteady_per_S/Pblind_per_S, ratio, rel_tol=3e-11):
            raise ValueError("QUASI_STEADY_RATIO_IDENTITY")
    def finite(t):
        minus = -math.expm1(-(gamma+A)*t)/(gamma+A)
        plus = -math.expm1(-(gamma+B)*t)/(gamma+B)
        return (A*minus-B*plus)/n_b  # per source S, starts at zero pion densities
    t = 10*TAU_PI
    value = finite(t)
    if abs(A-B) > 1e-9*max(A,B) and (value > 0) != (A>B):
        raise ValueError("FINITE_TIME_SIGN")
    return {"T_MeV": T, "X": X, "Fc": fc(T), "Xstar": threshold,
            "n_B_mminus3": n_b, "gamma_per_s": gamma,
            "A_capture_per_s": A, "B_capture_per_s": B,
            "nminus_over_nplus_steady_equal_source": (gamma+B)/(gamma+A),
            "net_over_equal_density_approx_steady": ratio,
            "pion_dXdt_per_S_steady": Psteady_per_S,
            "pion_dXdt_per_S_time_10tau": value}

def x_weak_eq(T):
    return 1.0/(1.0+math.exp(Q/T))

def cross_residual(T):
    return A0_MBARN*fc(T)*math.exp(Q/T)-B0_MBARN

def weak_eq_cross_T():
    lo, hi = 1.0, 100.0
    assert cross_residual(lo) > 0 > cross_residual(hi)
    for _ in range(100):
        mid = (lo+hi)/2
        if cross_residual(mid)>0:
            lo=mid
        else:
            hi=mid
    t = (lo+hi)/2
    if not math.isclose(x_weak_eq(t), snapshot(t,x_weak_eq(t))["Xstar"], rel_tol=1e-12):
        raise ValueError("WEAK_EQUILIBRIUM_CROSS_FAILURE")
    return t

def main():
    if len(sys.argv)!=3:
        raise SystemExit("Need two original files: main-scan.jl tool_script-parameters.jl")
    main_sha=attest(sys.argv[1], MAIN_BLOB, MAIN_REQUIRED)
    p_sha=attest(sys.argv[2], PARAM_BLOB, PARAM_REQUIRED)
    tstar=weak_eq_cross_T()
    result={"source_commit": ORIGINAL_COMMIT,"main_blob":main_sha,
            "parameter_blob":p_sha, "status": "SOURCE_EXACT_LOCAL_CONSTANT_BACKGROUND_ONLY",
            "inference": "NO_NATIVE_JULIA_NO_BBN_NO_PHYSICAL_BETA",
            "weak_eq_sign_change_temperature_MeV": tstar,
            "samples_fixed_X_0p15": [snapshot(t,.15) for t in (T_NUC,.1,1.,5.,10.)],
            "samples_weak_eq_X": [snapshot(t,x_weak_eq(t)) for t in (1.,10.,tstar,20.)]}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
