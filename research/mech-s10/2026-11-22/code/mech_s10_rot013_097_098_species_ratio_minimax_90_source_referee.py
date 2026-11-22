#!/usr/bin/env python3
"""Mech-S10 ROT013: independently recompute 90 fingerprint residuals of Badacz 097,
then form energy-by-energy species COMPOSITION odds-ratios and Chebyshev minimax
scalar-normalization NO-GO. Source-only Python standard library.

Strict provenance: three ACTUAL Herwig 097 event-mean MC JSONs are owner raw
source. The six-energy five-species BH counts are only AUTHOR-DERIVED aggregates
in owner analysis097.json; original full BlackHawk raw tabular 100x100 files are
NOT bundled in this GitHub checkout, and this is NOT an independent extraction
of BlackHawk table bins. Owner analysis097 'ratios' are used ONLY as a
post-computation numeric oracle, never to construct residuals.
No Herwig/PYTHIA/BlackHawk/Wu-Xu/PRyMordial physics jobs executed.

Firstness Badacz PREREG097 REVIEW098, archived BlackHawk original script.
Prior science LT9 ROT016 already showed old vs modern table multipliers
not globally scalar (145 mass-group entries). ROT013 different: same-energy
historical BH versus 7.2/7.3 generator MC species-composition and conditional
per-energy scalar rescaling, with explicit prior firstness.

From Nash-iw-research root:
python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot013_097_098_species_ratio_minimax_90_source_referee.py result.json
"""
import json
import math
from pathlib import Path
import subprocess
import sys

B=Path("research/badacz/2026-11-22/data")
SOURCES={
    B/"analysis097.json":"f6043967d386e6e7a46f8cb2c66b5529ec7bd6a9",
    B/"mc097/H72_f1.json":"1958acb99fe345f83649399220709eb879385426",
    B/"mc097/H73_f1.json":"5b0f8ef94042159b477856d17b64649f74d83748",
    B/"mc097/H73_f2.json":"505707fed0184acc5d987ca336a5ccca9af48049",
}
S={"pipm":"211","Kpm":"321","K0L":"130","proton":"2212","neutron":"2112"}
ARMS=("H72_f1","H73_f1","H73_f2")
EXPECTED_SQRTS={"H72_f1":1.0,"H73_f1":1.0,"H73_f2":2.0}

def verified_source(path,sha):
    assert path.is_file(),("MISSING",str(path))
    got=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
    assert got==sha,("GIT_BLOB_CHANGED",str(path),got,sha)
    return json.loads(path.read_text(encoding="utf8"))

def rms(x):
    return math.sqrt(sum(v*v for v in x)/len(x))

def main(dst):
    src={str(p):verified_source(p,sha) for p,sha in SOURCES.items()}
    base=src[str(B/"analysis097.json")]
    armdata={a:src[str(B/f"mc097/{a}.json")] for a in ARMS}
    assert base["gates"]["G_MC"]["pass"] and base["gates"]["G_NODES"]["pass"]
    Ekeys=sorted(base["bh"],key=float)
    assert len(Ekeys)==6
    out={}
    errors=[]
    allrows=[]
    for arm in ARMS:
        d=armdata[arm]
        assert d["sqrt_s_factor"]==EXPECTED_SQRTS[arm]
        assert d["primary"]=="up"
        assert len(d["energies"])==6
        records=[]
        for k,r in zip(Ekeys,d["energies"]):
            E=float(k)
            assert abs(r["E"]/E-1)<1e-5,("ENERGY_NOT_MATCHED",arm,k,r["E"])
            assert r["rc_read"]==r["rc_run"]==0
            assert r["events"]==2000
            assert abs(r["Efinal_over_sqrts"]-1)<1e-3
            BH=base["bh"][k]
            L={}
            se={}
            for sp,pdg in S.items():
                assert BH[sp]>0 and r[pdg]>0
                L[sp]=math.log10(BH[sp]/r[pdg])
                se[sp]=r[f"se_{pdg}"]/(r[pdg]*math.log(10.0))
                delta=abs(L[sp]-base["ratios"][arm][k][sp])
                errors.append(delta)
                assert delta<=1e-14,("ORIGINAL_RATIO_ORACLE_DISAGREE",arm,k,sp,delta)
            v=list(L.values())
            a=min(v); b=max(v)
            c=(a+b)/2
            eps=(b-a)/2
            assert all(abs(vv-c)<=eps+1e-14 for vv in v)
            # proof of exact minimax: any c outside [min,max] is worse,
            # midpoint minimizes max(abs(min-c),abs(max-c)).
            assert abs((b-c)-eps)<1e-14 and abs((c-a)-eps)<1e-14
            comp={s:L[s]-L["pipm"] for s in S if s!="pipm"}
            # normalized K/pi odds-ratio is invariant under ANY positive
            # common species-blind c(E); also BlackHawk forward-bin constant
            # cancels exactly if it is shared by species at this E.
            logKpi=math.log10((BH["Kpm"]/BH["pipm"])/(r["321"]/r["211"]))
            assert abs(comp["Kpm"]-logKpi)<1e-14
            logsigK=math.hypot(se["Kpm"],se["pipm"])
            records.append({
                "Eprime_GeV":E,
                "sqrt_s_over_Eprime":d["sqrt_s_factor"],
                "original_BH_5_author_processed_aggregate":BH,
                "raw_MC_means":{s:r[pdg] for s,pdg in S.items()},
                "L_log10_BH_over_MC_5_species":L,
                "MC_one_sigma_log10_approx":se,
                "species_composition_relative_to_pions":comp,
                "Kpm_over_pi_source_log_ratio":logKpi,
                "Kpm_over_pi_MC_SE_log10_delta_method":logsigK,
                "per_energy_best_scalar_log10_offset":c,
                "per_energy_optimal_chebyshev_residual_dex":eps,
                "rms_unshifted_five_species":rms(v),
                "rms_after_midrange_shift":rms([t-c for t in v])
            })
            allrows.append(records[-1])
        out[arm]=records
    assert len(allrows)==90//5
    assert len(errors)==90
    assert max(errors)<=1e-14
    summary={}
    for arm,records in out.items():
        summary[arm]={
            "n_E":6,"n_source_species_entries":30,
            "max_abs_original_L":max(abs(v) for r in records for v in r["L_log10_BH_over_MC_5_species"].values()),
            "global_per_energy_minimax_floor_max":max(r["per_energy_optimal_chebyshev_residual_dex"] for r in records),
            "mean_per_energy_minimax_floor":sum(r["per_energy_optimal_chebyshev_residual_dex"] for r in records)/6,
            "max_abs_Kpm_pi_composition":max(abs(r["Kpm_over_pi_source_log_ratio"]) for r in records),
            "Kpm_pi_low":records[0]["Kpm_over_pi_source_log_ratio"],
            "Kpm_pi_high":records[-1]["Kpm_over_pi_source_log_ratio"],
        }
    composition_version_preference=[]
    energy_version_preference=[]
    convention_composition_preferences=[]
    for i,k in enumerate(Ekeys):
        a=out["H72_f1"][i]
        b=out["H73_f1"][i]
        c=out["H73_f2"][i]
        composition_version_preference.append({
          "Eprime":float(k),
          "per_energy_minimax_winner":"H72_f1" if a["per_energy_optimal_chebyshev_residual_dex"]<b["per_energy_optimal_chebyshev_residual_dex"] else "H73_f1",
          "floor72":a["per_energy_optimal_chebyshev_residual_dex"],
          "floor73":b["per_energy_optimal_chebyshev_residual_dex"]})
        convention_composition_preferences.append({
          "Eprime":float(k),
          "winner":"H73_f1" if b["per_energy_optimal_chebyshev_residual_dex"]<c["per_energy_optimal_chebyshev_residual_dex"] else "H73_f2",
          "floor_f1":b["per_energy_optimal_chebyshev_residual_dex"],
          "floor_f2":c["per_energy_optimal_chebyshev_residual_dex"]})
        energy_version_preference.append({
          "Eprime":float(k),"H72_pion_L":a["L_log10_BH_over_MC_5_species"]["pipm"],
          "H73_f1_pion_L":b["L_log10_BH_over_MC_5_species"]["pipm"],
          "H73_f2_pion_L":c["L_log10_BH_over_MC_5_species"]["pipm"]})
    n72=sum(z["per_energy_minimax_winner"]=="H72_f1" for z in composition_version_preference)
    nf1=sum(z["winner"]=="H73_f1" for z in convention_composition_preferences)
    assert n72==4 and nf1==4,("CHANGED_VERSION_OR_E_REPLAY",n72,nf1)
    high=out["H73_f1"][-1]
    assert -0.24<high["Kpm_over_pi_source_log_ratio"]<-0.22
    assert high["per_energy_optimal_chebyshev_residual_dex"]>0.12
    answer={
      "artifact":"IW_MECH_S10_ROT013_BADACZ097_098_SOURCE_90_L_REPLAY_KPI_NORMALIZATION_INVARIANCE_VERSION_IDENTIFIABILITY",
      "status":"SOURCE_ONLY_POSTHOC_CONDITIONAL_THIRD_PARTY_AUTHOR_BH_AGGREGATES",
      "source_Git_blobs":{str(p):sha for p,sha in SOURCES.items()},
      "BH_data_level":"AUTHOR_DERIVED_6x5_BH_COUNTS_IN_analysis097, NOT_RAW_100x100_HERWIG_TABLES",
      "MC_data_level":"ORIGINAL_MC_3_ARMS_6_ENERGIES_2000_EVENTS_EACH",
      "original_BH_script_source_examined_separately":{
        "repo":"cewasiuk/Spin-and-Charge-BH-Evolution",
        "file":"scripts/herwig_scripts/up/main.cpp",
        "git_blob":"5a133a13630b67afbacc123ef903d31fdab2321e",
        "file2":"scripts/herwig_scripts/up/LEP.in",
        "git_blob2":"eafce728a4fb071f3f6681eb17dac21d6cd401c3",
        "scope":"CODE_SNAPSHOT_REPRODUCES_ENERGY_ASSIGNMENT, DOES_NOT_PROVE_THIS_VERSION_GENERATED_ARCHIVED_TABLES"
      },
      "n_independent_L_recalculations":len(errors),
      "max_abs_L_vs_owner_oracle":max(errors),
      "n_species_per_energy":5,
      "summary":summary,
      "direct_original_data_per_arm":out,
      "conditional_version_label_after_row_scalar":{
        "H72_better_minimax_energy_count":n72,
        "H73_better_minimax_energy_count":6-n72,
        "comparison":composition_version_preference},
      "conditional_energy_convention_label_after_row_scalar":{
        "H73_sqrts_E_better_minimax_energy_count":nf1,
        "H73_sqrts_2E_better_minimax_energy_count":6-nf1,
        "comparison":convention_composition_preferences},
      "pion_only_absolute_comparison":energy_version_preference,
      "interpretation":"Species-level K/pi residual cannot be corrected by any common energy-bin scalar. BUT free per-energy scalar destroys universal winner of physical generator version; 7.2 wins 4 of 6 scalar-free composition contests, while raw pion absolute normalization prefers 7.3. No statistical CI, historical Herwig version or physical beta bound.",
      "firstness":"Badacz REVIEW098 owner original mc and sqrt-s convention; LT9 ROT016 earlier global vintage-table scalar no-go; here alternative per-energy five-species fingerprints",
      "no_native_physics_executed":True,
      "no_canon":True,"no_exec_sign":True,"no_novelty_claim":True
    }
    Path(dst).write_text(json.dumps(answer,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf8")
    print(json.dumps({"n_independent_L":len(errors),"max_owner_L_abs_error":max(errors),
         "Kpm_pi_H73f1_high":high["Kpm_over_pi_source_log_ratio"],
         "H73f1_max_row_scalar_minimax":summary["H73_f1"]["global_per_energy_minimax_floor_max"],
         "version_H72_wins_nodes":n72,
         "energy_H73f1_wins_composition_nodes":nf1},indent=2))
if __name__=="__main__":
    assert len(sys.argv)==2, "usage python3 program.py result.json"
    main(sys.argv[1])
