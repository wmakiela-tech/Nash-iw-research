#!/usr/bin/env python3
"""Mech-S10 ROT018: exact-source protocol pre-native custody audit of Badacz
PREREG109 DEV2 incomplete Herwig 7.1.5 top high-energy endpoint.

Independent source-only Python3 stdlib, no Herwig, Julia, PRyMordial, physics.
Read exact Git blobs of the original PREREG109, owner DEV2 analysis/builder
and runner, fold_090 source, original script and latest REVIEW106. Formal
identification and synthetic in-memory counterexample, not actual 109 data.

An exact gate-level synthetic witness:
  10 primary channels x 3 requested 2000-event MC energy nodes, with ONLY
  (top,100000 GeV) failed. The original G_MC loop EXCLUDES that row and
  therefore accepts 29/30; the original builder drops the row and
  n_hc top uses last-good 70710.678 GeV constant clip across E>70710.
  The seam at E=50000 checks 10x5 hadron multiplicities but does NOT
  validate the missing top endpoint. All 29 "good" values identical
  across arbitrary positive physically synthetic endpoint completions.
This does not prove original 109 actual result label or magnitude.

The missing-source segment has nontrivial support on 4 of the declared
100 source energy nodes (5 GeV ..100000 GeV), so the top contribution
to the folded source cannot be inferred from the measurement. If top
primary flux is zero there, effect is zero; otherwise positive differences
can occur, but no unconditional numerical PBH-root bound is available.

Run from repo root:
 python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot018_prereg109_dev2_top_missing_endpoint_and_gate_nonidentification_referee.py OUT.json
"""
import ast
import json
import math
from pathlib import Path
import subprocess
import sys

B=Path("research/badacz/2026-11-22")
F=Path("research/badacz/2026-11-21/code/fold_090.py")
SOURCES={
 B/"IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_PREREG_109_20261122.md":"4cb85ea4b112780d588884361c4d076952d58dfa",
 B/"code/analysis_109.py":"c84d3a32603d96f08c4be4c3e8198772c9bf2e92",
 B/"code/build_tables_109.py":"fd231901b01602909974f77cdffd2af5053f8de6",
 B/"code/run109_dev2.sh":"38c2b8ba2d21826893eff5198adb6353a6eb5a57",
 B/"IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_REVIEW_106_20261122.md":"196ff9dfd5437694d2dee4ab3edadeecd7228c80",
 F:"3392d1d088a4bdae869ecdc70bcd2081861ecf37",
}
CHANNELS=("up","down","strange","charm","bottom","top","gluon","Wpm","Z0","tau")
ENERGIES=(50000.0,70710.67811865475,100000.0)

def read_locked(path):
    assert path.is_file(),("SOURCE_ABSENT",str(path))
    sh=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
    assert sh==SOURCES[path],("SOURCE_CHANGED",str(path),sh,SOURCES[path])
    return path.read_text(encoding="utf8")

def trapz(x,y):
    return sum((x[i+1]-x[i])*(y[i]+y[i+1])/2 for i in range(len(x)-1))

def emu_owner_g_mc(doc):
    """Same predicate as original source loop; uses AST-literal EXCL."""
    excl={("top",100000.)}
    ok=True
    for c,rows in doc.items():
        for e in rows:
            if (c,round(e["E"],6)) in excl:
                continue
            ok &= (e.get("rc_read")==0 and e.get("rc_run")==0
                and e.get("events")==2000 and abs(e["Efinal_over_sqrts"]-1)<=1e-3)
    return bool(ok)

def main(dst):
    source={str(p):read_locked(p) for p in SOURCES}
    ana=source[str(B/"code/analysis_109.py")]
    build=source[str(B/"code/build_tables_109.py")]
    run=source[str(B/"code/run109_dev2.sh")]
    base=source[str(F)]
    pre=source[str(B/"IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_PREREG_109_20261122.md")]
    assert "10 kanałów" in pre and "2000" in pre and "SEAM_PASS" in pre
    assert "EXCL = {(\"top\", 100000.0)}" in ana
    assert 'if (c, round(e["E"], 6)) in EXCL:' in ana
    assert 'out.setdefault("excluded_DEV2"' in ana
    assert "if gated and not ok:" in ana and 'out["labels"]["SEAM"]' in ana
    assert 'okmc &= e.get("rc_read") == 0 and e.get("rc_run") == 0' in ana
    assert 'good = [e for e in d["energies"] if e.get("rc_run") == 0' in build
    assert 'F.interp_loglog(Em, nm, E)' in build
    assert "def n_hc(s, c):" in build
    assert "def interp_loglog(Ei, n, E):" in base
    assert "E = np.clip(E, Ei[0], Ei[-1])" in base
    assert "run109c" in run and "top E=1e5 failed and is excluded" in run
    assert 'for c in top Wpm' in run
    assert 'mc 9709 gluon' in run

    # Actual AST top-level constant and exclusion existence; avoid executing
    # the owner script which imports unavailable physics/numpy dependencies.
    tree=ast.parse(ana)
    exc=[]
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="EXCL" for t in node.targets):
            exc=list(ast.literal_eval(node.value))
    assert exc==[("top",100000.0)]
    # 30 requested records; one top E100000 truly failed.
    records={}
    for c in CHANNELS:
        records[c]=[]
        for E in ENERGIES:
            failure=(c=="top" and E==100000.)
            records[c].append({"E":E, "rc_read":0,
                         "rc_run":1 if failure else 0,
                         "events":568 if failure else 2000,
                         "Efinal_over_sqrts":1.0})
    owner_gmc=emu_owner_g_mc(records)
    assert owner_gmc
    unfiltered=all(e["rc_run"]==0 and e["events"]==2000
                   for v in records.values() for e in v)
    assert not unfiltered
    good={c:[e for e in records[c] if e.get("rc_run")==0 and (e.get("events") or 0)>0]
          for c in CHANNELS}
    assert len(good["top"])==2 and all(len(good[c])==3 for c in CHANNELS if c!="top")
    requested=sum(len(v) for v in records.values())
    passed=sum(len(v) for v in good.values())
    assert (requested,passed)==(30,29)

    grid=[5*(100000/5)**(i/99) for i in range(100)]
    assert grid[0]==5 and abs(grid[-1]-100000)<1e-9
    top_cut=ENERGIES[1]
    miss=[(i,E) for i,E in enumerate(grid) if E>top_cut]
    assert len(miss)==4 and miss[-1][0]==99
    hi=[(i,E) for i,E in enumerate(grid) if E>50000]
    assert len(hi)==7

    # Exact behavior of fold_090 interp_loglog when E is clipped to the
    # last positive source MC energy, demonstrated analytically below.
    # If two measured top values n(50000)=10, n(70710)=10, the extrapolated
    # top component is 10 at 100000, but any positive third value is
    # compatible with those same input observations, e.g. 5 or 20.
    low,high=ENERGIES[1],ENERGIES[-1]
    def interp_missing_endpoint(E,n_last,n_end):
        if E<=low:return n_last
        return n_last*(n_end/n_last)**(math.log(E/low)/math.log(high/low))
    witnesses=[]
    # Isolate missing high-energy source component using synthetic Phi=1
    # for the entire segment E>low: deliberately NOT a true PBH Phi_top.
    actual_grid=grid[95:]
    # grid[95] < low, but positive Phi throughout [grid95, grid99] is a
    # synthetic positive integration weight only.
    clip=[10.]*len(actual_grid)
    for M in (0.5,2.0,5.0):
        truth=[interp_missing_endpoint(E,10,10*M) for E in actual_grid]
        A=trapz(actual_grid,clip)
        V=trapz(actual_grid,truth)
        assert A>0 and V>0
        witnesses.append({"synthetic_missing_endpoint_ratio_to_last_good":M,
            "source_clip_n_at_100000":10,
            "conditional_truth_n_at_100000":10*M,
            "source_missing_segment_integral_ratio_truth_over_clip_uniform_phi":V/A,
            "source_missing_segment_abs_difference_uniform_phi":V-A,
            "all_29_good_generated_measurements_identical":True})
    assert witnesses[0]["source_missing_segment_integral_ratio_truth_over_clip_uniform_phi"]<1.
    assert witnesses[1]["source_missing_segment_integral_ratio_truth_over_clip_uniform_phi"]>1.
    assert witnesses[2]["source_missing_segment_integral_ratio_truth_over_clip_uniform_phi"]>witnesses[1]["source_missing_segment_integral_ratio_truth_over_clip_uniform_phi"]

    # Oracles: seam uses e5 from each channel, where top is still GOOD;
    # 10x5 nominal seam is not invalidated by top 100000 failure, unlike
    # "complete top high-energy 3-node measurement" statement.
    result={
      "artifact":"IW_MECH_S10_ROT018_BADACZ109_DEV2_TOP_100TEV_INCOMPLETE_INPUT_AND_GATE_COVERAGE",
      "status":"PRE_NATIVE_SOURCE_ONLY_EXACT_OWNER_DEV2_RACE_SAFE_GUARD",
      "source_git_blobs":{str(p):s for p,s in SOURCES.items()},
      "actual_owner_NATIVE_REVIEW109_present":False,
      "actual_owner_MC109_binaries_or_results_read":False,
      "synthetic_MC_30_record_one_failure":True,
      "original_G_MC_logic_accepts_29_good_plus_one_excluded_failure":owner_gmc,
      "complete_original_three_energy_per_ten_channel_mc_coverage":unfiltered,
      "planned_source_energy_cells":requested,
      "actually_clean_source_cells_in_witness":passed,
      "missing_top_at_Eprime_GeV":100000.,
      "missing_top_sqrts_GeV":200000.,
      "last_good_top_Eprime_GeV":top_cut,
      "four_declared_primary_grid_nodes_above_last_good_top":miss,
      "seven_declared_primary_grid_nodes_above_50000":hi,
      "source_only_top_n_hc_operation":"F.interp_loglog uses np.clip(E, minGoodE, maxGoodE), so top E>70710 is EXACTLY a flat continuation if maxGoodE is 70710; independent of unobserved physical top multiplicity",
      "original_10x5_seam_at_Eprime50000_can_be_valid_with_top_high_endpoint_missing":True,
      "synthetic_in_memory_positive_missing_endpoint_witnesses_NOT_PHYSICS":witnesses,
      "scientific_negative_knowledge":[
        "G_MC PASS under DEV2 is a gated-valid subset verdict for 29 of 30 planned MC energy-channel records; it does NOT certify all 10 channels measured across 3 high-energy nodes.",
        "Pr1 SEAM_PASS for 10x5 hadronic cells at 50000 remains perfectly meaningful; top at 50000 had good data. Do not reject seam by conflating it with upper tail.",
        "Top primaries in omitted E>70710 range are coded as frozen last-good multiplicities. Actual quantitative source impact depends on original PBH primary top spectrum, not independently re-read here. No root beta effect or bound can be assigned.",
        "Even with positive primary source and n, arbitrary positive missing endpoint choices share all available 29 measurements yet imply distinct folded top contributions. This is source identifiability no-go; physical constraints and missing MC could restrict endpoints.",
        "DEV2 is explicitly logged pre-native, not an undeclared change; owner must label the eventual 109 table and threshold as conditional on top-high extrapolation or run prospective sensitivity.",
        "No actual native analysis109.json or owner physical run inferred."
      ],
      "no_physics_simulation_executed":True,"NO_CANON":True,"NO_EXEC_SIGN":True
    }
    Path(dst).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf8")
    print(json.dumps({"sources_sha":len(SOURCES),"source_10channels_x3":requested,"source_accepted":passed,"one_failed_excluded":owner_gmc,"G_MC_full_completion":unfiltered,
       "source_grid_top_unmeasured_nodes":miss,
       "synthetic_witness_ratios":[w["source_missing_segment_integral_ratio_truth_over_clip_uniform_phi"] for w in witnesses]},indent=2))

if __name__=="__main__":
    assert len(sys.argv)==2,"Usage python3 rot018.py results.json"
    main(sys.argv[1])
