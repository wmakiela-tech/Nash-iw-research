#!/usr/bin/env python3
"""Mech-S7 Wu-Xu 2x2 raw artifact audit. Python 3, numpy/pandas/scipy.
Usage: python reproduce_mech_s7_wuxu_postevap_gate_001.py PUBLIC.zip PAPER.zip
No source-native Julia re-execution; diagnostic only / no physical endpoint.
"""
import hashlib, io, json, sys
from zipfile import ZipFile
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator
from scipy.integrate import cumulative_trapezoid

PUBLIC_SHA = "75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5"
PAPER_SHA = "3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e"
Q = 939.5654205 - 938.27208816
TAU = 878.4
TNUC = .078185270688319950

def open_source(path, sha, names):
    assert hashlib.sha256(open(path, "rb").read()).hexdigest() == sha, "raw ZIP provenance mismatch"
    with ZipFile(path) as z:
        return {label: pd.read_csv(io.BytesIO(z.read("trajectory_"+filename+".csv")))
                for label,filename in names}

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Pass ORIGINAL public and paper GitHub Actions ZIP archives")
    ds = {}
    ds.update(open_source(sys.argv[1], PUBLIC_SHA,
        [("public_exec","current"),("public_sym","repaired")]))
    ds.update(open_source(sys.argv[2], PAPER_SHA,
        [("paper_exec","paper_exec"),("paper_sym","paper_sym")]))
    ref = ds["public_exec"]
    for label,d in ds.items():
        assert len(d) == 1600 and np.array_equal(d.a.to_numpy(), ref.a.to_numpy())
        assert d.source_active.iloc[:1470].eq(1).all()
        assert d.source_active.iloc[1470:].eq(0).all()
    E = (ds["paper_exec"].Xn-ds["public_exec"].Xn).to_numpy()
    S = (ds["paper_sym"].Xn-ds["public_sym"].Xn).to_numpy()
    assert E[1469] == S[1469] == 0.
    assert E[1470] < 0 < S[1470]
    def fixedT(d):
        x = Q / (1000*d.T_GeV.to_numpy())
        return float(np.interp(Q/TNUC, x, d.Xn.to_numpy()))
    x_ref = Q/(1000*ref.T_GeV.to_numpy())
    lna_ref = float(np.interp(Q/TNUC, x_ref, np.log(ref.a.to_numpy())))
    def fixedA(d):
        return float(np.interp(lna_ref, np.log(d.a.to_numpy()), d.Xn.to_numpy()))
    target_T = {k:fixedT(d) for k,d in ds.items()}
    target_a = {k:fixedA(d) for k,d in ds.items()}

    # Positive sign-preserving source-free conditional propagator on one shared background
    t = ref.t_sec.to_numpy()[1470:]
    T = ref.T_GeV.to_numpy()[1470:]*1000
    fine = np.linspace(t[0],t[-1],80001)
    x = Q/PchipInterpolator(t,T)(fine)
    Gamma = (255/TAU)*(12+6*x+x*x)/(x**5)
    k = Gamma*(1+np.exp(-x))+1/TAU
    integral = cumulative_trapezoid(k, fine, initial=0)
    damp = np.exp(-np.interp(t,fine,integral))
    i = 1502
    out = {
      "source_provenance": {"public_zip_SHA256":PUBLIC_SHA,"paper_zip_SHA256":PAPER_SHA},
      "first_off_index":1470,
      "last_on_delta": [float(E[1469]),float(S[1469])],
      "first_off_delta": [float(E[1470]),float(S[1470])],
      "first_off_interaction": float(S[1470]-E[1470]),
      "first_post_off_sign_crossing": [
        int(1471+np.flatnonzero(np.sign(E[1471:]) != np.sign(E[1470]))[0]),
        int(1471+np.flatnonzero(np.sign(S[1471:]) != np.sign(S[1470]))[0])],
      "at_index_1502": {
        "observed_delta_exec":float(E[i]), "observed_delta_sym":float(S[i]),
        "sourcefree_common_bg_exec":float(E[1470]*damp[i-1470]),
        "sourcefree_common_bg_sym":float(S[1470]*damp[i-1470]),
        "positive_multiplier":float(damp[i-1470])},
      "target_Xn_fixed_T":target_T,
      "target_Xn_fixed_same_a":target_a,
      "contrast_fixed_T": [
          target_T["paper_exec"]-target_T["public_exec"],
          target_T["paper_sym"]-target_T["public_sym"]],
      "contrast_fixed_a":[
          target_a["paper_exec"]-target_a["public_exec"],
          target_a["paper_sym"]-target_a["public_sym"]],
      "floor_flags_caveat":"run_one_point floor_active() returns false when nPBH zero",
      "ceiling":"RAW_NUMERICAL_DIAGNOSTIC_NOT_SOLVER_CONVERGENCE_NOT_SOURCE_VALID_E2B_NOT_PHYSICAL"
    }
    print(json.dumps(out,indent=2))
if __name__ == "__main__":
    main()
