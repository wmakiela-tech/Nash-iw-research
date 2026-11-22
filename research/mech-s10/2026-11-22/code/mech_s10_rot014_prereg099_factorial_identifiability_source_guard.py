#!/usr/bin/env python3
"""Mech-S10 ROT014 independent pre-execution PROTOCOL/SOURCE-ALGEBRA gate.

Read the actual frozen BADACZ PREREG099+builder+analyser and original fold_090
from source authentic Git checkout; do NOT modify prereg or perform physics.
Certify:
 (1) Only L(00),Sa(10),Ua(11) (plus Sb different high-E continuation), and
     NO old-label bin-only V(01) are present, so causal factorial interaction
     and path-independent label/bin Shapley allocation are NOT identified.
 (2) Source-mass folded yields from the actual implementation obey for
     nonnegative primary weights/multiplicities:
     1 <= Ua/Sa <= BIN_HW/BIN_PY = 1.110889..., independent of mass.
     This is a TABLE INPUT bound, NOT a bound on Yp or root beta.
 (3) Changing split 25->12.5 has seven grid nodes in a declared 100-node
     5...100000 GeV logarithmic source grid; 'd_label' also changes the
     PY-vs-HER routing between these cutoffs and the unmeasured >5e4 tail.
 (4) Elementary *constructive* nonzero table-stage factorial interaction
     even with positive spectra; and two MONOTONE synthetic completions
     of missing factorial root arm that reverse Shapley dominance.
All examples are algebraic/synthetic countermodels, NOT actual Wu-Xu results.
Source table R2 used only for positive-yield evidence in its original 100x5
entries, NOT as if new L/Sa/Ua physical tables had been computed.

Run from public Nash-iw-research repo root:
python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot014_prereg099_factorial_identifiability_source_guard.py rot014.json
"""
import csv
import json
import math
from pathlib import Path
import subprocess
import sys

D=Path("research/badacz")
B=D/"2026-11-22"
SOURCES={
    B/"IW_BADACZ_B1_HERWIG_TABLE_LABEL_THRESHOLD_DECOMPOSITION_PREREG_099_20261122.md":"62deee1e54b9803e351bdfacff4ec5cd90561c7e",
    B/"code/build_tables_099.py":"16b28f58af1ca545c16ba70582760e565e8d19b6",
    B/"code/analysis_099.py":"06d6d8058d923fda1e15ec932b12441eba96f297",
    B/"code/run099.sh":"e24d763b9b49fc6d1880d8ae03a7de7e84f43be7",
    D/"2026-11-21/code/fold_090.py":"3392d1d088a4bdae869ecdc70bcd2081861ecf37",
    D/"2026-11-21/data/hadrons_085_R2.dat":"000d22b6e173ea1f913eaf6cc75511f254301d63",
}
def read_locked():
    contents={}
    for p,sha in SOURCES.items():
        assert p.is_file(),("MISSING",str(p))
        a=subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
        assert a==sha,("WRONG_SOURCE_BLOB",str(p),a,sha)
        contents[str(p)]=p.read_text(encoding="utf8")
    return contents

def trapezoid(values,energies):
    return sum((energies[i+1]-energies[i])*(values[i]+values[i+1])*0.5
               for i in range(len(values)-1))

def synthetic_four_arms(Bp,Bh):
    # The exact code structure in build_tables_099.py, but synthetic
    # strictly positive input functions and a generic nonnegative primary Phi.
    E=[5*20000**(i/99) for i in range(100)]
    phi=[math.exp(-e/3000.0)/(e+10) for e in E]
    py=[0.9+0.03*math.log1p(e) for e in E]
    oldh=[1.15+0.025*math.log1p(e) for e in E]
    newh=[1.48+0.019*math.log1p(e) for e in E]
    def v(split,h,Bher):
        return trapezoid([w*( (p/Bp if e<split else hh/Bher))
                           for w,e,p,hh in zip(phi,E,py,h)],E)
    L=v(25.,oldh,Bh)
    S=v(12.5,newh,Bh)
    U=v(12.5,newh,Bp)
    V=v(25.,oldh,Bp) # missing from owner prereg 099
    interaction=U-S-V+L
    H_old=trapezoid([w*hh*(e>=25) for w,e,hh in zip(phi,E,oldh)],E)
    H_new=trapezoid([w*hh*(e>=12.5) for w,e,hh in zip(phi,E,newh)],E)
    exact=(1/Bp-1/Bh)*(H_new-H_old)
    assert abs(interaction-exact)<1e-12*(1+abs(exact))
    assert interaction!=0
    assert 1<U/S<Bh/Bp
    return {"label":"SYNTHETIC_NOT_PHYSICAL",
            "L_original_label_old_bin":L,
            "S_corrected_label_old_bin":S,
            "U_corrected_label_new_bin":U,
            "V_old_label_new_bin_MISSING_IN_OWNER_DESIGN":V,
            "tabular_factorial_interaction_U_minus_S_minus_V_plus_L":interaction,
            "exact_formula":exact,
            "Hnew":H_new,"Hold":H_old,
            "source_U_over_S":U/S,
            "n_source_grid_nodes_12p5_to_25":sum(12.5<=e<25 for e in E),
            "n_source_grid_nodes_above_5e4":sum(e>5e4 for e in E),
            "cutoff_band_nodes":[e for e in E if 12.5<=e<25],
            "high_tail_nodes":[e for e in E if e>5e4]}

def synthetic_root_completion():
    """Two distinct monotonic, positive-label/bin threshold-shift worlds
    have identical observed L,S,Ua roots but opposite Shapley dominance."""
    observed={"r_L":0.0,"r_S":-0.06,"r_U":-0.10}
    worlds=[]
    for rV in (-0.01,-0.07):
        l0=observed["r_S"]-observed["r_L"]
        b1=observed["r_U"]-observed["r_S"]
        b0=rV-observed["r_L"]
        l1=observed["r_U"]-rV
        inter=observed["r_U"]-observed["r_S"]-rV+observed["r_L"]
        sL=(l0+l1)/2
        sB=(b0+b1)/2
        assert abs(sL+sB-(observed["r_U"]-observed["r_L"]))<1e-14
        assert observed["r_U"]<=min(observed["r_S"],rV)
        assert max(observed["r_S"],rV)<=observed["r_L"]
        worlds.append({"rV_MISSING_bin_only":rV,
                       "d_label_first":l0,"d_bin_after_label":b1,
                       "d_bin_first":b0,"d_label_after_bin":l1,
                       "factorial_interaction":inter,
                       "Shapley_label":sL,"Shapley_bin":sB,
                       "dominant_absolute":"label" if abs(sL)>abs(sB) else "bin"})
    assert worlds[0]["dominant_absolute"]=="label"
    assert worlds[1]["dominant_absolute"]=="bin"
    return {"observed_same_in_both":observed,
            "monotone_synthetic_completions":worlds,
            "negative_result":"No unique factorial/causal label-vs-bin attribution from 3 arms even assuming individually threshold-decreasing interventions."}

def main(output):
    f=read_locked()
    build=f[str(B/"code/build_tables_099.py")]
    an=f[str(B/"code/analysis_099.py")]
    pre=f[str(B/"IW_BADACZ_B1_HERWIG_TABLE_LABEL_THRESHOLD_DECOMPOSITION_PREREG_099_20261122.md")]
    original=f[str(D/"2026-11-21/code/fold_090.py")]
    assert all(q in build for q in ("np.trapezoid",'"L": fold_parts(n_py, n_hl, 25.0, BIN_PY, BIN_HW)', '"Sa": fold_parts(n_py, lambda s, c: n_hs(s, c, "a"), 12.5, BIN_PY, BIN_HW)', '"Ua": fold_parts(n_py, lambda s, c: n_hs(s, c, "a"), 12.5, BIN_PY, BIN_PY)'))
    assert "for a in ARMS" in an and 'ARMS = "lsbu"' in an
    assert '"d_label"' in an and '"d_bin"' in an and '"d_resid"' in an
    assert "G_LINK" in an and "Pr4_G_LINK" in an
    assert "table" in pre.lower() and "Sa" in pre and "Sb" in pre
    assert "100 energies 5-1e5 GeV" in original
    dlPY=math.log(1e11)/499
    dlHER=math.log(1e11)/99
    BP=math.expm1(dlPY)/dlPY
    BH=math.expm1(dlHER)/dlHER
    factor=BH/BP
    assert 1.1108<factor<1.111
    assert 0.0456<math.log10(factor)<0.0458
    rows=[]
    src=f[str(D/"2026-11-21/data/hadrons_085_R2.dat")]
    with (D/"2026-11-21/data/hadrons_085_R2.dat").open(encoding="utf8") as fh:
        hdr=next(fh)
        assert "charged_pion" in hdr
        for line in fh:
            if line.strip():
                t=[float(x) for x in line.split()]
                assert len(t)==6 and all(math.isfinite(v) for v in t)
                rows.append(t)
    assert len(rows)==100 and all(all(y>0 for y in row) for row in rows)
    synth=synthetic_four_arms(BP,BH)
    completions=synthetic_root_completion()
    # Restriction is sharp as PY contribution tends to zero:
    test_eps=[1.0,0.1,0.001,1e-8]
    sharp=[]
    for p in test_eps:
        h=1.
        ratio=(p+h)/(p+(BP/BH)*h)
        assert 1<ratio<factor
        sharp.append({"positive_py_to_H_ratio":p,"Ua_over_Sa":ratio})
    cert={
      "artifact":"IW_MECH_S10_ROT014_PREREG099_MISSING_FACTORIAL_ARM_AND_SHARP_TABULAR_BIN_BOUND",
      "type":"PREEXEC_SOURCE_PROTOCOL_ALGEBRA_AND_SYNTHETIC_COUNTERMODEL",
      "scientific_owner":"Badacz PREREG_099 firstness",
      "original_source_git_blobs":{str(p):sha for p,sha in SOURCES.items()},
      "provenance":"Original prereg builder/analysis/runner/090 folding source read and git-blob-verified; original real 085 R2 table 100 rows×5 positive yields only; NO real 099 table construction or solver run.",
      "three_of_four_factorial_cells":["L (label old, bin old)",
                                      "Sa (label corrected, bin old)",
                                      "Ua (label corrected, bin corrected)"],
      "missing_fourth_factorial_cell":"V (label old, bin corrected)",
      "binning_source_constants":{"BIN_PY":BP,"BIN_HER":BH,
         "bin_only_herwig_component_Ua_over_Sa_upper":factor,
         "log10_max_yield_bin_factor_dex":math.log10(factor),
         "sharp_for_nonnegative_primary_Phi_and_multiplicities":True,
         "not_bound_on_helium_Yp_or_logbeta_root":True,
         "sharp_limit_examples":sharp},
      "real_085_R2_source_table_rows_positive":len(rows),
      "real_085_R2_source_table_species_per_row":5,
      "source_cutoff_routing":"L PY for E<25 / HER labelled above; Sa PY for E<12.5 / HER relabelled above; change in [12.5,25) affects PY-vs-HER source selection as well as label and high-energy extrapolation",
      "independent_positive_source_stage_factorial_witness":synth,
      "independent_monotone_root_nonidentification_witness":completions,
      "scope_warning":"SYNTHETIC countermodels are not actual original 099 physical predictions; path-specific telescoping decomposition is exact and legitimate, but NOT uniquely identifiable path-independent/causal label/bin effects without missing V arm.",
      "next_prospective_action_only":"Add old-label/new-bin 2x2 fourth arm or explicitly limit claims to chosen label-first path; do not revise prereg after results silently.",
      "NO_NEW_JULIA":True,"NO_CANON":True,"NO_EXEC_SIGN":True
    }
    Path(output).write_text(json.dumps(cert,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf8")
    print(json.dumps({"bin_upper_ratio":factor,
         "bin_upper_dex":math.log10(factor),
         "real_r2_rows_positive":len(rows),
         "cutoff_grid_nodes":synth["n_source_grid_nodes_12p5_to_25"],
         "missing_factorial_arm":"V",
         "synthetic_table_interaction":synth["tabular_factorial_interaction_U_minus_S_minus_V_plus_L"],
         "completions":completions["monotone_synthetic_completions"]},indent=2))
if __name__=="__main__":
    assert len(sys.argv)==2,"usage: python3 script.py out.json"
    main(sys.argv[1])
