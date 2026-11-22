#!/usr/bin/env python3
"""ROT021 Mech-S10: original Wu-Xu log-log EXTRAPOLATION below hadron mass grid,
and exact two-endpoint extrapolation conditioning at author magic() cutoff.

Actual ORIGINAL PUBLIC AUTHOR SOURCE at pinned Git commit d395183...:
- tool_script-hadrons_from_PBH.jl exact Git blob cc734329...
- main-scan.jl blob b368ba55...
- data/out/hadrons_from_PBH.dat blob 06d0883...
- tool_script-parameters.jl blob 0d7198...
- Project.toml blob 6297eb...
Fetch original author SOURCE as immutable bytes via HTTPS raw GitHub, check
actual Git blob SHA, store each byte in output evidence directory.

Actual ORIGINAL Badacz source:
- Sa 099 table blob 3aac285...
- original owner rate_dump_081.jl blob 4b415...
- source-mapping patch MechS6 blob 4d1f2be...
- prereg109 blob 4cb85...
- owner 109 runner blob 38c2...
Check exact git hash-object for all before parsing.

Compute exact log-log linear extrapolation slopes using first two mass rows
for each of five species (H=source original and Sa=original owner table).
Compute potential rate magnification at the symbolic magic() default
'log_m_PBH_evaporated_ratio=20' conditional on the trajectory reaching
that threshold; note actual ODE may stop before this point.

Prove an exact expression for sensitivity to UNKNOWN future Sc first-two
rates under SAME mass grid:
log(R_Sc/R_Sa)(M) = (1-lambda)log(Sc0/Sa0)
                     +lambda log(Sc1/Sa1);
lambda=log(M/M0)/log(M1/M0).
Construct purely synthetic 0.1% rate perturbation of ONE boundary row
to show amplification far below table, not actual physical error.
The sensitivity is deterministic algebra, not solver noise and NOT BBN Yp.
No original Julia, PRyMordial, MC, BlackHawk or Herwig run.
"""
import csv
import json
import math
from pathlib import Path
import subprocess
import sys
import urllib.request

REPO=Path("research")
OWNER=REPO/"badacz"
OUT_BASE=Path("research/mech-s10/2026-11-22")
OFFICIAL_REPO="Fenyutanchan/Primordial-Black-Hole"
OFFICIAL_COMMIT="d395183674cace6c9906a8911bdeb7234ba4040d"
OFFICIAL_PATH="arXiv-2509.05618"
UPSTREAM={
  "tool_script-hadrons_from_PBH.jl":"cc73432910f872d526113ce59b6204f38d0766a9",
  "main-scan.jl":"b368ba55d5a493f7bc185909730f7fe5691f10d6",
  "data/out/hadrons_from_PBH.dat":"06d0883a27b108692720422294ba2baacd381a64",
  "tool_script-parameters.jl":"0d7198ff3557bdbd5753000bb07a7a7405cc24f5",
  "Project.toml":"6297eb1682da77bbbfa87307795b655c677f98c4"
}
OWNER_SOURCE={
 OWNER/"2026-11-22/data/hadrons_099_Sa.dat":"3aac28554204e6b6951a7472773535ad3c8613ea",
 OWNER/"2026-11-21/code/rate_dump_081.jl":"4b415a6ddd7d102ad03194af75aa1fb9203c11fb",
 REPO/"mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py":"4d1f2be94510c576e4f48752911f88ede8b50474",
 OWNER/"2026-11-22/IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_PREREG_109_20261122.md":"4cb85ea4b112780d588884361c4d076952d58dfa",
 OWNER/"2026-11-22/code/run109_dev2.sh":"38c2b8ba2d21826893eff5198adb6353a6eb5a57"
}
MASS_CONVERSION_GEV_PER_G=5.609588603804452e23
PERCENT_SYNTHETIC=.001

def blob_sha(path):
    return subprocess.check_output(["git","hash-object",str(path)],text=True).strip()

def verify_own_sources():
    result={}
    for f,expected in OWNER_SOURCE.items():
        assert f.is_file(),("SOURCE_NOT_FOUND",str(f))
        observed=blob_sha(f)
        assert observed==expected,("SOURCE_SHA_CHANGED",str(f),observed,expected)
        result[str(f)]=observed
    return result

def download_upstream(output):
    dst=output/"official_wuxu_pinned"
    dst.mkdir(parents=True,exist_ok=True)
    seen={}
    for name,sha in UPSTREAM.items():
        url=f"https://raw.githubusercontent.com/{OFFICIAL_REPO}/{OFFICIAL_COMMIT}/{OFFICIAL_PATH}/{name}"
        req=urllib.request.Request(url,headers={"User-Agent":"IW-NASH-Scientific-Source-Referee/1.0"})
        with urllib.request.urlopen(req,timeout=30) as r:
            assert r.status==200,("HTTP_SOURCE",url,r.status)
            raw=r.read()
        p=dst/name
        p.parent.mkdir(exist_ok=True,parents=True)
        p.write_bytes(raw)
        got=blob_sha(p)
        assert got==sha,("UPSTREAM_SOURCE_GIT_SHA_MISMATCH",name,got,sha)
        seen[name]={"path":str(p),"git_blob":sha,"source_url":url,"bytes":len(raw)}
    return seen

def read_table(path):
    with open(path,encoding="utf8") as f:
        lines=f.read().splitlines()
    assert lines[0].startswith("m_PBH [GeV]")
    vals=[[float(v) for v in s.strip().split()] for s in lines[1:] if s.strip()]
    assert len(vals)==100 and all(len(x)==6 for x in vals)
    assert all(x[0]>0 and all(z>0 for z in x[1:]) for x in vals)
    return vals

def table_metrics(vals,kind,Mstop_by_j):
    m0=vals[0][0]/MASS_CONVERSION_GEV_PER_G
    m1=vals[1][0]/MASS_CONVERSION_GEV_PER_G
    assert abs(m0/1e9-1)<1e-12
    lnratio=math.log(m1/m0)
    assert 0<lnratio<.2
    S=[]
    for k in range(5):
        R0,R1=vals[0][k+1],vals[1][k+1]
        exponent=math.log(R1/R0)/lnratio
        point={}
        for j,m in Mstop_by_j.items():
            lam=math.log(m/m0)/lnratio
            power=R0*math.exp(exponent*math.log(m/m0))
            point[str(j)]={"conditional_mass_g":m,
                            "lambda_logmass_extension_from_first_interval":lam,
                            "source_rate_at_conditional_mass_in_original_table_Units_GeV":power,
                            "rate_over_at_M1e9":power/R0,
                            "condition_number_abs_to_log_second_row":abs(lam),
                            "condition_number_abs_to_log_first_row":abs(1-lam),
                            "if_second_row_only_plus0p1pct_output_ratio":
                                math.exp(lam*math.log1p(PERCENT_SYNTHETIC)),
                            "if_first_row_only_plus0p1pct_output_ratio":
                                math.exp((1-lam)*math.log1p(PERCENT_SYNTHETIC)),
                            "only_hypothetical_single_row_change_not_Sc":True}
        S.append({"species":("pipm","Kpm","K0L","proton","neutron")[k],
                  "first_tabulated_rate_source_GeV":R0,
                  "second_tabulated_rate_source_GeV":R1,
                  "low_mass_loglog_exponent":exponent,
                  "conditional_mass_endpoints":point})
    return {"table":kind,"m0_g":m0,"m1_g":m1,"n_rows":len(vals),
            "units_are_original_file_source_rate_GeV_not_seconds":True,
            "species":S}

def main(out):
    out=Path(out);out.parent.mkdir(exist_ok=True,parents=True)
    own=verify_own_sources()
    verified=download_upstream(out.parent)
    inter=(out.parent/verified["tool_script-hadrons_from_PBH.jl"]["path"]).read_text() if False else (Path(verified["tool_script-hadrons_from_PBH.jl"]["path"])).read_text(encoding="utf8")
    main=(Path(verified["main-scan.jl"]["path"])).read_text(encoding="utf8")
    params=(Path(verified["tool_script-parameters.jl"]["path"])).read_text(encoding="utf8")
    project=(Path(verified["Project.toml"]["path"])).read_text(encoding="utf8")
    dump=(OWNER/"2026-11-21/code/rate_dump_081.jl").read_text(encoding="utf8")
    patch=(REPO/"mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py").read_text(encoding="utf8")
    runner=(OWNER/"2026-11-22/code/run109_dev2.sh").read_text(encoding="utf8")

    # author source implements rates as exp(linear extrapolation in logM)
    assert inter.count("LinearInterpolation(log.(hadrons_from_PBH[:,") == 5
    assert inter.count("extrapolation=ExtrapolationType.Linear") == 5
    assert all(f"dN_over_dt_{s}(m_PBH)" in main for s in ("π","K","K⁰ᴸ","proton","neutron"))
    assert 'include("tool_script-hadrons_from_PBH.jl")' in main
    assert 'PBH_evaporated_flag = log_m_PBH_in_EU ≤ log_m_PBH_evaporated_in_EU' in main
    assert "n_PBH = PBH_evaporated_flag ? zero(n_PBH_ini)" in main
    assert "d_n_π_dt_from_PBH = dN_over_dt_π(m_PBH) * n_PBH" in main
    assert 'log_m_PBH_evaporated_ratio::Number=20' in main
    assert "log_m_PBH_evaporated_in_EU = max(" in main
    assert "DataInterpolations" in project
    assert 'm_π = MeV(139.57039)' in params
    # actual Badacz native wrapper uses magic() default: it supplies NO override
    assert "res = magic(m, β; hadrons_output_flag=true)" in dump
    assert 'include(joinpath(src_dir, "main-scan-parameters.jl"))' in dump
    assert 'include(prefix_file)' in dump
    assert '"pi": "    d_n_π_dt_from_PBH = 0.5 * ' in patch
    assert 'for x in k c; do cp -a $SRC $W/src_$x' in runner
    assert "hadrons_from_PBH.dat" in runner

    Sa=read_table(OWNER/"2026-11-22/data/hadrons_099_Sa.dat")
    Wu=read_table(out.parent/"official_wuxu_pinned/data/out/hadrons_from_PBH.dat")
    Mstop={}
    initial={}
    for j in (22,62):
        Minit=Sa[j][0]/MASS_CONVERSION_GEV_PER_G
        # terminal Planck floor in original magic; here initial*e^-20
        # > ~10 grams and >> 2e-5g, so explicit max selects exp(-20).
        stop=Minit*math.exp(-20)
        assert stop>1
        initial[str(j)]=Minit
        Mstop[j]=stop
    own_metrics=table_metrics(Sa,"ORIGINAL_BADACZ_099_Sa",Mstop)
    orig_metrics=table_metrics(Wu,"PUBLIC_ORIGINAL_WU_XU_TABLE",Mstop)
    assert abs(own_metrics["m0_g"]-orig_metrics["m0_g"])<1e-6
    assert all(abs(own_metrics["species"][k]["low_mass_loglog_exponent"]+1)<.2 for k in range(5))
    assert all(own_metrics["species"][k]["conditional_mass_endpoints"]["22"]["condition_number_abs_to_log_second_row"]>200 for k in range(5))
    assert all(own_metrics["species"][k]["conditional_mass_endpoints"]["62"]["condition_number_abs_to_log_second_row"]>175 for k in range(5))
    assert all(0<own_metrics["species"][k]["conditional_mass_endpoints"]["22"]["if_second_row_only_plus0p1pct_output_ratio"]<.81 for k in range(5))
    assert all(0<own_metrics["species"][k]["conditional_mass_endpoints"]["62"]["if_second_row_only_plus0p1pct_output_ratio"]<.85 for k in range(5))
    assert all(x["conditional_mass_endpoints"]["22"]["rate_over_at_M1e9"]>1e8 for x in own_metrics["species"])
    assert all(x["conditional_mass_endpoints"]["62"]["rate_over_at_M1e9"]>1e7 for x in own_metrics["species"])
    output={
        "artifact":"IW_MECH_S10_ROT021_SOURCE_AUTHORED_WU_XU_ACTUAL_LOGLOG_LINEAR_EXTRAP_WITH_MASS_CONDITIONING",
        "official_author_original_repo":OFFICIAL_REPO,
        "official_author_original_commit":OFFICIAL_COMMIT,
        "original_author_verified_bytes_and_SHA":verified,
        "actual_owner_original_5_git_sha_pins":own,
        "source_exact_five_author_hadron_species_loglog_extrapolation":True,
        "original_AUTHOR_evolution_includes_r_h(M)_times_n_PBH":True,
        "original_AUTHOR_mass_evaporation_flag_sets_n_PBH_zero_at_mass_floor":True,
        "owner_wrapper_original_magic_keyword_default_20_unoverridden":True,
        "owner_charge_pair_source_map_patch_changes_four_species_SOURCE_ASSIGNMENT_multipliers_but_NOT_loglog_interpolation_method":True,
        "initial_mass_grams":initial,
        "conditional_ODE_stop_Minit_exp_minus20_grams_if_reached":{str(k):v for k,v in Mstop.items()},
        "owner_actual_Sa_rates_source_subgrid_power":own_metrics,
        "published_original_author_table_rates_source_subgrid_power":orig_metrics,
        "exact_two_boundary_log_sensitivity_identity":
          "lambda=ln(M/M0)/ln(M1/M0); log(Rnew/Rold)(M)=(1-lambda)*ln(Rnew0/Rold0)+lambda*ln(Rnew1/Rold1), valid for positive rates and same first two mass nodes; no true Sc table presently available",
        "synthetic_perturbation_log_boundary_second_node_only":PERCENT_SYNTHETIC,
        "synthetic_witness_is_not_Sc_and_not_new_physics":True,
        "do_not_promote_rate_endpoint_enhancement_to_integrated_BBN":True,
        "scientific_limits":[
          "Original author GitHub source has exact LinearInterpolation(log rate, log mass) with ExtrapolationType.Linear. It gives a determinate numerical continuation, not a physically calibrated subgrid source.",
          "Published original author commit is pinned, but local /home/claude checkout not directly available to Mech; owner wrapper verified only by source text; the owner source clone commit itself has not been SHA checked here.",
          "Original magic default mass floor log ratio20, or Planck scale if larger; to claim physical times or whether stop actually reached requires native trajectory.",
          "Synthetic 0.1% perturbation of only second source rate node quantifies formal ill-conditioning at hypothetical stop; not actual Sc mismatch, not actual noise and no actual Yp effect.",
          "Native PBH mass loss and BBN network may suppress or amplify the integrated effect; no bound on beta root or BBN Yp follows."
        ],
        "no_native_physics_executed":True,
        "no_physical_pbh_bound":True,"no_novelty":True,"no_canon":True,"no_exec_sign":True
    }
    out.write_text(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf8")
    print(json.dumps({"source_author_pinned":len(verified),"original_owner_locked":len(own),
                     "initial_grams":initial,"conditional_stop_grams":output["conditional_ODE_stop_Minit_exp_minus20_grams_if_reached"],
                     "Sa_species":own_metrics["species"]},indent=2,ensure_ascii=False))
if __name__=="__main__":
    assert len(sys.argv)==2
    main(sys.argv[1])
