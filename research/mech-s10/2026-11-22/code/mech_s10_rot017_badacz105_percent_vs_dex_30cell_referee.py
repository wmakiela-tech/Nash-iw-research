#!/usr/bin/env python3
"""ROT017 Mech-S10: independently re-evaluate actual 30 Herwig7.1.5
native owner MC multiplicities versus processed BlackHawk source aggregates
from original Badacz 097, distinguish dex-vs-percent accuracy.

- Gate exact original SHA-1 Git blob of each of five sources before parsing.
- 30 signed ratios recomputed from actual 10000-event MC source+OWNER DERIVED
  BH six-node aggregate. analysis105.ratios is used as oracle AFTER new
  computation, not to derive ratios; the original BH 100x100 table contents
  were NOT independently extracted.
- True asymmetrical percent: 100*(BH/MC−1), NOT 100*abs(log10).
  Also includes symmetric percent relative to BH for denominator sensitivity.
- No independent MC replicates or true coverage; MC SE is an approximation
  about event-mean sampling, not a p-value or proof of a population-level
  mismatch. Distinguish 'observed event means within 1%' from statistical
  compatibility with a 1% population-level rule.
- Strictly preserve owner frozen MATCH_7.1 at original 0.04 dex criterion.
- Distinct from prior Mech ROT013 Herwig7.2/7.3 vintage composition test.
No new Herwig, Julia, PRyMordial, PYTHIA or BlackHawk physics runs.
"""
import json
import math
from pathlib import Path
import subprocess
import sys

B=Path("research/badacz/2026-11-22")
SOURCES={
    B/"IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_PREREG_105_20261122.md":"94afa813a73ba5d4fb46738f4d2bc0ffb50ca46f",
    B/"IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_REVIEW_106_20261122.md":"196ff9dfd5437694d2dee4ab3edadeecd7228c80",
    B/"data/analysis097.json":"f6043967d386e6e7a46f8cb2c66b5529ec7bd6a9",
    B/"data/analysis105.json":"f4ec04e475b27d09cc2b1b7f02f895bfaba28692",
    B/"data/mc105/H71_f1.json":"5211432914ea6be5f7cca6334bf8f1f798e8a7e4",
}
SPECIES={"pipm":"211","Kpm":"321","K0L":"130","proton":"2212","neutron":"2112"}

def read_locked(path):
    assert path.exists(),("SOURCE_MISSING",str(path))
    sha=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
    assert sha==SOURCES[path],("GIT_SHA_MISMATCH",str(path),sha,SOURCES[path])
    return path.read_text(encoding="utf8")

def main(outpath):
    s={str(p):read_locked(p) for p in SOURCES}
    doc=s[str(B/"IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_REVIEW_106_20261122.md")]
    pre=s[str(B/"IW_BADACZ_B1_DIR009_HERWIG71_VINTAGE_FINGERPRINT_PREREG_105_20261122.md")]
    assert "≤ 1%" in doc and "0.01 dex" in doc
    assert "max(0.04, 4" in pre and "MATCH_7.1" in pre
    BH=json.loads(s[str(B/"data/analysis097.json")])
    MC=json.loads(s[str(B/"data/mc105/H71_f1.json")])
    own=json.loads(s[str(B/"data/analysis105.json")])
    assert own["labels"]["L_VER"]=="MATCH_7.1"
    assert all(x["pass"] for x in own["gates"].values())
    keys=sorted(BH["bh"],key=float)
    assert len(keys)==len(MC["energies"])==6
    assert MC["version"]=="7.1.5" and MC["primary"]=="up"
    assert MC["sqrt_s_factor"]==1.0
    assert all(abs(float(k)/node["E"]-1)<1e-5
               for k,node in zip(keys,MC["energies"]))
    arr=[]
    for k,node in zip(keys,MC["energies"]):
        assert node["events"]==10000 and node["rc_run"]==node["rc_read"]==0
        for name,pdg in SPECIES.items():
            b=float(BH["bh"][k][name])
            m=float(node[pdg])
            assert b>0 and m>0
            L=math.log10(b/m)
            rel=100.0*(b/m-1)
            inv=100.0*(m/b-1)
            se_pct=100.*node["se_"+pdg]/m
            sL=se_pct/100./math.log(10)
            a=own["ratios"][k][name]
            assert abs(L-a)<1e-14,("CUSTODY_ORACLE_MISMATCH",k,name,L,a)
            owner_tol=own["tol"][k][name]
            assert abs(owner_tol-max(.04,4*sL))<=1e-12
            arr.append({
              "Eprime_GeV_source_label":k,
              "species":name,"PDG":pdg,
              "owner_mc_actual_10000_event_mean":m,
              "owner_mc_se_actual":node["se_"+pdg],
              "blackhawk_owner_097_processed_BH_mean":b,
              "independently_recomputed_L_dex":L,
              "blackhawk_vs_herwig_percent_of_Herwig":rel,
              "herwig_vs_blackhawk_percent_of_BlackHawk":inv,
              "relative_MC_standard_error_percent":se_pct,
              "MC_only_standard_error_log10_approx":sL,
              "deviation_over_MC_only_SE_dimensionless_abs":
                abs(rel)/se_pct,
              "above_one_percent_of_MC":abs(rel)>1.0,
              "above_one_percent_of_BH":abs(inv)>1.0,
              "within_original_preregistered_dex_gate":abs(L)<=owner_tol,
              "owner_original_tolerance_dex":owner_tol
            })
    assert len(arr)==30
    assert all(t["within_original_preregistered_dex_gate"] for t in arr)
    count1=sum(t["above_one_percent_of_MC"] for t in arr)
    count1bh=sum(t["above_one_percent_of_BH"] for t in arr)
    count2=sum(abs(t["blackhawk_vs_herwig_percent_of_Herwig"])>2 for t in arr)
    biggest=max(arr,key=lambda x:abs(x["blackhawk_vs_herwig_percent_of_Herwig"]))
    maxL=max(arr,key=lambda x:abs(x["independently_recomputed_L_dex"]))
    assert count1==6 and count1bh==6 and count2==1
    assert biggest["species"]=="proton" and biggest["Eprime_GeV_source_label"]=="25"
    assert biggest is maxL
    assert abs(biggest["blackhawk_vs_herwig_percent_of_Herwig"]-2.256008739985438)<1e-12
    assert biggest["deviation_over_MC_only_SE_dimensionless_abs"]<2.0
    upper100=100*(10**.04-1)
    lower100=100*(1-10**(-.04))
    summary={
      "source_30_cell_recomputed_exact":len(arr),
      "original_source_BH_is_owner_derived_6x5_aggregates_not_raw_100x100_table":True,
      "max_absolute_L_dex":abs(maxL["independently_recomputed_L_dex"]),
      "max_absolute_relative_percent_to_MC":abs(biggest["blackhawk_vs_herwig_percent_of_Herwig"]),
      "max_absolute_relative_percent_to_BH":max(abs(x["herwig_vs_blackhawk_percent_of_BlackHawk"]) for x in arr),
      "count_cells_observed_relative_deviation_above_1pct_MC":count1,
      "count_cells_observed_relative_deviation_above_1pct_BH":count1bh,
      "count_cells_observed_relative_deviation_above_2pct_MC":count2,
      "most_deviant_cell":biggest,
      "one_percent_positive_log10_threshold_dex":math.log10(1.01),
      "one_percent_negative_log10_threshold_dex":math.log10(.99),
      "one_hundredth_dex_as_positive_relative_percent":100*(10**.01-1),
      "frozen_0p04_dex_gate_upper_percent":upper100,
      "frozen_0p04_dex_gate_lower_magnitude_percent":lower100,
      "original_preregistered_MATCH_7p1_pass_preserved":True,
      "sample_MCS_exceed_1pct_does_NOT_certify_underlying_model_mismatch_above_1pct":True
    }
    assert 2.2<summary["max_absolute_relative_percent_to_MC"]<2.3
    assert summary["one_hundredth_dex_as_positive_relative_percent"]>2.3
    assert 9.5<upper100<9.7
    result={
      "artifact":"IW_MECH_S10_ROT017_BADACZ105_REVIEW106_DEX_PERCENT_EXACT_30_CELL_REFEREE",
      "lineage":"IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10",
      "claim_class":"SOURCE_ONLY_UNIT_ACCURACY_CONSISTENCY_GUARD",
      "original_owner_firstness":"BADACZ_PREREG105_REVIEW106 actual Herwig7.1.5 source built and 6x10000 MC events",
      "original_github_git_blob_sources":{str(p):sha for p,sha in SOURCES.items()},
      "summary":summary,
      "all_30_actual_owner_BH_processed_and_MC_original_cells":arr,
      "interpretation":"Observed 30 source means meet frozen absolute 0.04dex matching rule, but 6 measured relative deviations exceed 1pct; therefore REVIEW106 sentence 'within <=1pct in all 30' is quantitatively false for the realized means; replace with <=0.009689dex = <=2.256pct relative to MC. The largest outlier is 1.39 MC-only standard errors, so no statistical rejection of potential latent 1pct accuracy is claimed. The original BH full table was not re-extracted; no ability to identify historical version uniquely.",
      "new_original_physics_executed":False,
      "NO_PBH_BOUND":True,"NO_NOVELTY":True,"NO_CANON":True,"NO_EXEC_SIGN":True
    }
    Path(outpath).write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf8")
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=="__main__":
    assert len(sys.argv)==2,"usage: python3 rot017.py output.json"
    main(sys.argv[1])
