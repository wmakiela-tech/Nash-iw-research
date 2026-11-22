#!/usr/bin/env python3
"""Mech-S10 ROT022. Reproduce post-hoc owner REVIEW110/POSTHOC109b
actual Herwig7.1.5 TOP excluded endpoint 5 scenario table-level effects
from original Badacz 100x100x14 primary spectra gzip, native Herwig71 TOP
two successful MC energy nodes, true Sc data and original Wu-Xu log-log
two-row below-grid extrapolation. SOURCE-ONLY; NO new MC, Julia or BBN.

The top-high-segment k∈{0,.5,2,3} scenarios are owner-defined POST HOC,
not prereg physical uncertainty bounds. "slope" uses owner last 2 measured
top MC energies 50000 and 70710.678.

Reconstruct exactly owner posthoc109b max |log10(Sc_alt/Sc)| for rows
0..28 all five hadrons with no BlackHawk hadron multiplicity tables:
Delta Sc(M_j) = HBAR/BIN_HW * trapz(E, Phi_top(M_j,E)*
  [n_alt_top(E)-n_clip_top(E)] 1_{E>E_last}).
The other original channels cancel in the difference, so it suffices
to use the original owner Sc source table. Validate all five owner
posthoc checks at <5e-12 dex absolute. This is actual reanalysis from
independent raw owner primary 10000 source nodes, not invented synthetic
physics.

Then apply public official Wu-Xu original source code operator:
R_h(M)=R_h(M0)*(M/M0)^slope,
slope=[ln R_h(M1)-ln R_h(M0)]/[ln M1-ln M0].
The code extrapolates R_h below M0=1e9g with linear extrapolation
in log(rate)-log(mass), until PBH evaporated flag. For each actual
table variant compute exact extrapolated log ratios to baseline Sc at
declared mass positions [1e9g, 1e8, 1e6,1e4, 13g,371g].
The 13g and 371g limits are owner original magic() DEFAULT end mass
M_init*exp(-20), not claims that native ODE reaches them.

Since k=0/3 and k=.5/2 were named post hoc and change only one
segment, this highlights domain mismatch of owner's <=.0111dex
in-table 0..28 test vs unknown extrapolation; it DOES NOT prove
j22/j62 native Yp or beta roots change.

Keep original source custody checks immutable. No raw MC unlogged reuse.
"""
from pathlib import Path
import runpy
import json
import math
import hashlib
import subprocess
import sys
import urllib.request

B=Path("research/badacz/2026-11-22")
D=Path("research/badacz/2026-11-21")
READER=Path("research/mech-s10/2026-11-22/code/mech_s10_rot019_actual_blackhawk_primary_top_tail_energy_conservation_sharp_discrete_bound.py")
PIN_READER="5d12bfe84eb95a5fdd2f91011e2211a284c178ea"
SOURCES={
 B/"data/mc109/herwig71_top.json":"58e48b22ad58bb50d4b4729efc5f30696c3d865b",
 B/"data/hadrons_109_Sc.dat":"2cc859a1a44a1b8fafa479f6c844a76bd2db5afe",
 B/"data/hadrons_099_Sa.dat":"3aac28554204e6b6951a7472773535ad3c8613ea",
 B/"data/posthoc109b.json":"d47a8bfee70ed7d1ad0b2b606330f41fe0433b9c",
 B/"code/posthoc_109b.py":"3545fdb65510f95bef6980b2970f9a4f5417f2e1",
 B/"IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_REVIEW_110_20261122.md":"c818f071d7473ab0752d2e6329aa8388cba8f745",
 D/"code/fold_090.py":"3392d1d088a4bdae869ecdc70bcd2081861ecf37",
}
NAMES=("pipm","Kpm","K0L","proton","neutron")
PDG={"pipm":"211","Kpm":"321","K0L":"130","proton":"2212","neutron":"2112"}
MS_PER_GEV=5.609588603804452e23
HBAR=6.582119569e-25
MODES=("0","0.5","2","3","slope")
NUMERIC={"0":0.0,"0.5":.5,"2":2.0,"3":3.0}
AUTHOR_URL="https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl"
AUTHOR_BLOB="cc73432910f872d526113ce59b6204f38d0766a9"

def gh(p):
    return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()

def load_table(p):
    with p.open(encoding="utf8") as f:lines=f.read().splitlines()
    assert lines[0].startswith("m_PBH [GeV]")
    rows=[[float(x) for x in ln.split()] for ln in lines[1:] if ln.strip()]
    assert len(rows)==100 and all(len(r)==6 and min(r)>0 for r in rows)
    return rows

def main(outpath):
    for p,want in [(READER,PIN_READER),*SOURCES.items()]:
        assert p.exists() and gh(p)==want,("ORIGINAL_GIT_SHA_MISMATCH",str(p),gh(p) if p.exists() else None,want)
    old=runpy.run_path(str(READER))
    old["check_sources"]() # 7 owner original input SHA and actual source gzip
    A=old["primary_read"]() # ACTUAL 100x100x14 original spectra
    Sc=load_table(B/"data/hadrons_109_Sc.dat")
    Sa=load_table(B/"data/hadrons_099_Sa.dat")
    owner=json.loads((B/"data/posthoc109b.json").read_text(encoding="utf8"))
    mc=json.loads((B/"data/mc109/herwig71_top.json").read_text(encoding="utf8"))
    assert mc["version"]=="7.1.5" and mc["primary"]=="top" and mc["sqrt_s_factor"]==2
    good=[e for e in mc["energies"] if e.get("rc_run")==0 and (e.get("events") or 0)>0]
    fail=[e for e in mc["energies"] if e.get("rc_run")!=0]
    assert len(good)==2 and len(fail)==1 and fail[0]["E"]==100000 and all(e["events"]==2000 for e in good)
    lastE=good[-1]["E"];firstE=good[-2]["E"]
    assert abs(lastE-70710.67811865475)<1e-10
    assert owner["E_last_top"]==lastE
    assert "E = np.clip(E, Ei[0], Ei[-1])" in (D/"code/fold_090.py").read_text(encoding="utf8")
    assert 'K = slice(0, 29)' in (B/"code/posthoc_109b.py").read_text(encoding="utf8")

    # Verify original author's intended extrapolation source directly.
    req=urllib.request.Request(AUTHOR_URL,headers={"User-Agent":"IW-NASH-ROT022-Falsification-Audit"})
    with urllib.request.urlopen(req,timeout=30) as resp:
        assert resp.status==200
        raw=resp.read()
    original_content=raw.decode("utf-8")
    # SHA of original Git BLOB = sha1(b'blob {len}\0'+raw)
    blob=hashlib.sha1(b"blob "+str(len(raw)).encode("ascii")+b"\0"+raw).hexdigest()
    assert blob==AUTHOR_BLOB
    assert original_content.count("LinearInterpolation(log.(hadrons_from_PBH[:,")==5
    assert original_content.count("extrapolation=ExtrapolationType.Linear")==5

    assert all(abs(Sc[j][0]/(A[j]["mass_g"]*MS_PER_GEV)-1)<1e-10 for j in range(100))
    assert all(Sc[j][0]==Sa[j][0] for j in range(100))
    m0=A[0]["mass_g"];m1=A[1]["mass_g"]
    assert m0==1e9 and m1>m0
    bins=old["BIN_HW"]
    scenarios={mode:[[0.0]*5 for _ in range(100)] for mode in MODES}
    shares=[[0.0]*5 for _ in range(100)]
    # physical original scale: source table [GeV] = rate [1/s] * HBAR
    for j in range(100):
        E=A[j]["energy"]
        f=A[j]["phi"]["top"]
        for h,s in enumerate(NAMES):
            # raw MC counts are for a pair, divide by 2 per PRIMARY top
            lastN=.5*good[-1][PDG[s]]
            firstN=.5*good[-2][PDG[s]]
            assert lastN>0 and firstN>0
            slope=math.log(lastN/firstN)/math.log(lastE/firstE)
            source_clip=[f[i]*lastN if E[i]>lastE else 0.0 for i in range(100)]
            T=HBAR/bins*old["trapezoid"](E,source_clip)
            shares[j][h]=T/Sc[j][h+1]
            assert 0<=shares[j][h]<1.
            for mode in MODES:
                if mode=="slope":
                    ys=[f[i]*lastN*(E[i]/lastE)**slope if E[i]>lastE else 0.0 for i in range(100)]
                    new=HBAR/bins*old["trapezoid"](E,ys)
                else:
                    new=NUMERIC[mode]*T
                actual_new=Sc[j][h+1]+new-T
                assert actual_new>0
                scenarios[mode][j][h]=actual_new
    replay={}
    for mode in MODES:
        mx=max(abs(math.log10(scenarios[mode][j][h]/Sc[j][h+1])) for j in range(29) for h in range(5))
        want=owner["scenarios"][mode]
        replay[mode]={"original_owner_max_abs_log10_rows0_to28":want,
            "independent_source_replay_max_abs_log10_rows0_to28":mx,
            "oracle_absolute_difference":abs(mx-want)}
        assert abs(mx-want)<2e-11,("ORIGINAL_OWNER_POSTHOC_ORACLE_MISMATCH",mode,mx,want)
    shareMax=max(shares[j][h] for j in range(29) for h in range(5))
    assert abs(shareMax-owner["top_segment_share_max_rows0_28"])<2e-11,("ORIGINAL_SHARE_ORACLE_DIFF",shareMax)
    assert abs(owner["reproduce_Sc_max_rel"])<3e-16

    def ratio_log_at_M(new0,new1,base0,base1,mass):
        lam=math.log(mass/m0)/math.log(m1/m0)
        return (1-lam)*math.log10(new0/base0)+lam*math.log10(new1/base1)
    mass_targets={
      "grid_lower_mass_1e9g":m0,
      "below_grid_1e8g":1e8,
      "below_grid_1e6g":1e6,
      "below_grid_1e4g":1e4,
      "j22_hypothetical_default_mass_floor_g":Sc[22][0]/MS_PER_GEV*math.exp(-20),
      "j62_hypothetical_default_mass_floor_g":Sc[62][0]/MS_PER_GEV*math.exp(-20)
    }
    # At each mass and mode all 5 true data-driven scenario source ratios.
    extrap={}
    for mode in MODES:
        extrap[mode]={}
        for tag,mass in mass_targets.items():
            vals={s:ratio_log_at_M(scenarios[mode][0][h],scenarios[mode][1][h],Sc[0][h+1],Sc[1][h+1],mass)
                  for h,s in enumerate(NAMES)}
            extrap[mode][tag]={
              "source_rate_ratio_log10_each_hadron_vs_original_Sc":vals,
              "max_abs_log10_source_rate_ratio_hadron":max(abs(v) for v in vals.values()),
              "max_ratio_alt_over_Sc":max(10**v for v in vals.values()),
              "min_ratio_alt_over_Sc":min(10**v for v in vals.values())
            }

    # Raw owner Sc versus Sa under same publicly verified Wu-Xu extrapolation.
    sc_sa={}
    for tag,mass in mass_targets.items():
        sc_sa[tag]={s:ratio_log_at_M(Sc[0][h+1],Sc[1][h+1],Sa[0][h+1],Sa[1][h+1],mass) for h,s in enumerate(NAMES)}
    max_onsource=max(max(x["independent_source_replay_max_abs_log10_rows0_to28"] for x in replay.values()),0)
    max_end=max(extrap[mode]["j22_hypothetical_default_mass_floor_g"]["max_abs_log10_source_rate_ratio_hadron"] for mode in MODES)
    assert max_end>max_onsource,("NO_AMPLIFICATION_WITNESS",max_end,max_onsource)
    result={
      "artifact":"IW_MECH_S10_ROT022_BADACZ110_REAL_TOP_SEGMENT_REPLAY_AND_WUXU_OUT_OF_GRID_EXTRAPOLATION_CUSTODY",
      "claim_class":"REAL_ORIGINAL_SOURCE_ONLY_POSTHOC_OWNER_109B_REPLICATION_AND_SOURCE_EXTRAPOLATION",
      "badacz_review110_r2_firstness":True,
      "badacz_actual_native_review110_results_consumed_only_as_context_not_reexecuted":True,
      "source_sha_verified":{str(k):v for k,v in SOURCES.items()},
      "pinned_prior_original_primary_reader_git_sha":PIN_READER,
      "pinned_prior_original_primary_7_git_sha_pass":True,
      "real_original_100x100_primary_gzip_re_read":True,
      "actual_top_MC_succeeded":2,"actual_top_MC_failed":1,
      "actual_Herwig71_top_missing_highest_E_GeV":100000.,
      "real_original_author_Julia_extrapolation_blob":blob,
      "real_original_author_Julia_extrapolation_type":"LinearInterpolation(log(rate),log(mass);ExtrapolationType.Linear)",
      "owner_posthoc109b_five_max_0_to28_exact_replay":replay,
      "owner_posthoc109b_original_top_share_max_0_to28":owner["top_segment_share_max_rows0_28"],
      "own_independent_share_max_0_to28":shareMax,
      "posthoc_named_five_modes_NOT_STATISTICAL_CONFIDENCE_SET":list(MODES),
      "original_Sc_original_Sa_two_lowest_mass_grid_nodes":masses if False else [m0,m1],
      "actual_two_first_source_grid_rows_top_segment_share_each_species":{str(j):{NAMES[h]:shares[j][h] for h in range(5)} for j in (0,1)},
      "actual_five_owner_source_variants_source_log_ratios_in_and_below_grid":extrap,
      "actual_Sc_vs_Sa_boundary_extrapolation_log_ratios_for_context":sc_sa,
      "largest_owner_original_table_log_variation_0_to28":max_onsource,
      "largest_hypothetical_j22_end_floor_log_variation_five_scenarios":max_end,
      "scientific_guard":[
        "Actual Badacz posthoc109b measures <=0.011102 dex on rows 0..28, NOT across m<1e9g; exact upstream Wu-Xu rate interpolation extrapolates loglog below 1e9g, potentially magnifying small differences in first 2 mass rows.",
        "This replay reproduces ORIGINAL 109b source-only scenario numbers, does not invent another physics run or an uncertainty distribution.",
        "Five top-tail multiplier alternatives k=0,.5,2,3 and slope are post hoc exploration, not calibrated confidence interval or physically guaranteed envelope.",
        "Extrapolated endpoint (13g,371g) assumes author default exp(-20) PBH mass floor is reached; actual mass trajectories and time-integrated BBN Yp response are NOT estimated.",
        "A large relative source rate at 13g does not imply large integrated energy, hadron counts, BBN helium abundance or root beta change. Without M(t) weighting, no physical threshold claim.",
        "This test operates on original source tables and raw primary in author hadronization units only. Local owner source code checkout not independently hashed, public original author method verified."
      ],
      "no_native_physics_executed":True,"no_new_Herwig_MC_executed":True,
      "no_pbh_bound":True,"no_novelty":True,"no_canon":True,"no_exec_sign":True
    }
    outpath=Path(outpath)
    outpath.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf8")
    print(json.dumps({"oracles":replay,"share":shareMax,"j22_sources":{k:v["j22_hypothetical_default_mass_floor_g"] for k,v in extrap.items()},"j62_sources":{k:v["j62_hypothetical_default_mass_floor_g"] for k,v in extrap.items()}},ensure_ascii=False,indent=2))
if __name__=="__main__":
    assert len(sys.argv)==2
    main(sys.argv[1])
