# MECH-S7 ROT016 — Archival event aliasing and exact-knot interpolation non-identifiability

**Date:** 2026-10-24. **Lineage:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`.
**Return ID:** `MECH-S7-FRONTB-SAVED_EVENT_ALIASING_AND_EXACT_KNOT_INTERPOLATION_NEGATIVE_CONTROL-016`.
**Problem:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`.
**Result class:** `EXECUTED_SOURCE_ARCHIVE_EVENT_WINDOW_ANALYSIS / EXECUTED_EXACT_KNOT_INTERPOLATION_COUNTEREXAMPLE / ORIGINAL_JULIA_ACCEPTED_VS_DENSE_PATCH_STATIC_READY_ONLY`.
**Ceiling:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_MODERN_Yp_DH / NO_PBH_BOUND`.

## 1. Original evidence and host subtraction

Pinned source: Wu–Xu `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl` (Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`), `tool_script-N_relativistic_species.jl`, `tool_script-parameters.jl`. The source computes a ten-component log-state in `η=ln a`, solves via `solve(evolution_problem,AutoTsit5(Rosenbrock23()))` **without explicitly specified tolerances**, then samples `evolution_solution(log(a))` on an external `a_list`. The source tests source-on status at `log_M > log_M_cut` inside the RHS rather than installing a `ContinuousCallback` at `M=10^9g` or at the cutoff. This is a **source code statement**, not evidence that an actual solver accepted a bad step.

Original *separately SHA256-validated* Mech-S6 GitHub Actions archives: `mech_s6_public_2x2_raw.zip` `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`, `mech_s6_paper_2x2_raw.zip` `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`. Four independent trajectories, 1600 archived rows each, last source-active row `iloc 1469` (CSV field `i=1470`) and first source-off row `iloc 1470` (CSV field `i=1471`). Last source-on mass ~1.8366e9g and first off ~8–11g. **No sampled source-active states below M=1e9g.** Data are post-solve samples, not accepted internal solver mesh.

MECH ROT004 source plateau mass-cube: `Γ=4.207579833788249e27 g³/s`, `M_i=6e9g`, `M_cut = M_i exp(-20) = 12.366921733...g`, applicable only to the code-defined source-on plateau. ROT015 audited the saved 1470 source-active rows and found nonconstant secant deviations up to −5.9624% then +3.4692% for B_exec, but **did not observe** accepted steps. This ROT016 is a genuinely different **negative attribution control** and an archive-sampling information gate; source interpolation/dense theory is a mature numerical-analysis host, not new theorem novelty. NC/MT13 event-weighted source sufficiency and LT5 exact event target distinguish target from emitted particle fluence; PRF11/DAX two-temperature EOS and source mass spectrum validation remain upstream.

## 2. Exact source event and recorded sampling gap

Conditional exact source equations:

```
M(t)^3=M_i^3−Γ(t−t_i),
t(M*)=t_i+(M_i^3−M*^3)/Γ.
```

Exact event values within this host:

- `t(M=1e9g) = 51.09825802317032 s`.
- `t(M=M_cut) = 51.33592433955715 s`.
- **Actual model-defined subtable interval** = `0.23766631638683577 s`.
- Last archived on row `public_exec`: `t=49.96189862690079 s`; first archived off row `t=52.25910204802943 s`. Gap `2.2972034211286427 s`, or **9.665666789 times** the entire subtable lifetime. Ratios for `public_sym/paper_exec/paper_sym` respectively `9.6654923/9.6656913/9.6654667`.
- In public_exec, the source-table edge lies **49.4671%** into this recorded gap and source cutoff **59.8130%** into it; the 10.35%-of-gap source-on subtable interval is completely unseen by saved samples. These percentages use **exact source-law event clock**, not source-missing interpolation.
- Reanchoring exact cubic mass law to the last saved source-on mass instead of the initial mass shifts the edge to `51.19666294957113 s`, **+0.09840492640081 s** for exec, or +0.0926952755s sym. That is the archived mass-clock defect from ROT014/015, not clock-origin gauge: changing the initial-value specification changes inferred event placement and must not be silently reconciled.

## 3. Three mutually incompatible 2-point archive reconstructions

Use only archived mass/time endpoints flanking both physical thresholds; linearly interpolate in raw mass `M`, mass cube `M³`, or log mass `ln M`. This is an **information-content stress**, NOT a reconstruction of SciML's dense-output algorithm. Compared to original-initial-mass exact clock for `public_exec`:

| Two-point linear variable | Edge time `t(1e9g)` [s] | Edge time bias [s] | Inferred subtable interval [s] | Relative to exact |
|---|---:|---:|---:|---:|
| M | 51.008333220 | −0.089924803 | 1.250768823 | 5.26271× |
| M³ | 51.888308436 | +0.790050413 | 0.370793612 | 1.56014× |
| ln M | 50.034644929 | −1.063613094 | 2.178825435 | 9.16758× |
| **Exact source cube law** | **51.098258023** | **0** | **0.237666316** | **1×** |

All four branches were independently checked and show qualitatively the same severe disagreement; see `source_archive_event_estimates_016.csv` (12 records) and `event_gap_archived_summary_016.csv` (4 records). **The terminal sample cannot resolve both internal thresholds by itself.** None of the three chosen two-point formulas should be called "the SciML error"; they illustrate missing information.

## 4. Exact accepted-knot / inexact dense sample counterexample

Create an **independent synthetic counterexample** on the same source cubic-law host, but not on the unknown original solver mesh. Two accepted knots `(t_a,M_a)` and `(t_b,M_b)` with `M_a=3e9g`, `M_b=2.9e9g`, `t_a=0`, `t_b=(M_a³−M_b³)/Γ=0.6205467520860s` satisfy cubic mass law **exactly**. Define between knots:

```
θ = (t−t_a)/(t_b−t_a),
M_exact(θ)^3 = (1−θ) M_a^3 + θ M_b^3,
ln M_interp(θ) = (1−θ) ln M_a + θ ln M_b.
```

The interpolant passes **exactly through both accepted knots**. Nonetheless on 101 equidistant synthetic samples:

- Maximum `|M_interp/M_exact−1|` = `0.000430834447` = **0.04308%**.
- Adjacent sampled **effective cube-law rate** `−ΔM_interp³/(Γ Δt)` ranges **0.9504927761 ... 1.0511795255**, i.e. local secant defects **−4.9507% ... +5.1180%** with **zero knot errors**.
- The source-defined mass-cube residual at the knot endpoints is zero, but between knots reaches **0.007887362 s** in this intentionally generic interpolant.

This quantitatively falsifies the inference `up to ~5% saved-point secant deviation ⇒ accepted ODE steps had ~5% rate error`. Dense interpolation alone **can** do so in principle. It **does not demonstrate** that SciML's actual specific `AutoTsit5(Rosenbrock23())` interpolant generated the observed ROT015 anomaly: that requires genuine original accepted-step capture, method identification and direct comparison. Conversely a well-behaved dense interpolant would not certify accepted-step correctness. The two mechanisms are not identified from archived samples.

## 5. Independent numeric and static code controls

`reproduce_event_interpolation_gate_016.py` checks original ZIP SHA, all four 1600-row branch inputs, first-source-off and table bounds, calculates exact event fractions, three competing 2-point inversion laws, and produces three CSV plus `result_016.json`. **Independent** `independent_decimal_controls_016.py` evaluates original *serialized* `trajectory_current.csv` mass/time cells at Decimal precision 65, reproduces event times and all three two-point inversions to within `2e-13 s` of source CSV Float64 calculations. Both scripts **executed**. A corrected checksum typo in the development script was caught by the mandatory original archive SHA assertion before a successful replay; no data mutation.

`instrument_wuxu_accepted_and_dense_016.py` is a **prepared/static-tested only** patcher for the pinned `main-scan.jl`: unique original two-line anchor verified against GitHub source; adds environmental gated dual output files `saved_steps` (`evolution_solution.t`+`.u`) and `dense_samples` (`results_list`). The patcher passes a Python fixture test and rejects double patches. **Original Julia source was not executed**, the exact engine's Julia compile, result `retcode`, saved-node semantics and numerical properties remain **OPEN**. This instrumenter only observes existing saved solver states, does not itself enforce a callback and must not be mistaken for an accepted-stage profiler.

SciML documentation to use for exact accepted-step/dense interpretation:
- https://docs.sciml.ai/DiffEqDocs/stable/solvers/ode_solve/index.html
- https://docs.sciml.ai/DiffEqDocs/dev/api/ordinarydiffeq/api/common_interface/

## 6. Consequential P1 experiment / falsifier

Within the **existing Front B** source 10D experiment, preserve on identical branch and tolerances:

1. Observed saved **solver mesh** `solution.t/u` AND reconstructed dense queries `solution(log(a))`, *and* check solver `retcode`, algorithm identity, accepted-step stats and whether every logged saved state is actually a post-accept node.
2. Compute mass cube monitor on both data layers while source ON, not only at final saved frame, and independently log the crossing of `M=1e9g`, `M=M_cut`, `T=T_nuc`, using exact source-native event times as external controls.
3. Compare `M³(t)` numerical error on the same physical coordinate, not just `ln a`. At cutoff, distinguish a **pure observation callback** from a **state-changing callback** and do not infer equivalence of runs.
4. Explicit tolerance ladder with cross-cell identical background, species source rates and hadron storage through source OFF; target Xn at **fixed T**, and global accuracy budget `ε_X<6.3335656e-6` for previous archived sign certification, per MT13 (not yet achieved).
5. Triage: if accepted-step mass cube invariant PASS and dense FAIL, source-localize to interpolation; if accepted-step FAIL, analyze integrator, event transition or numerical scaling; if both PASS on new rerun, classify **historical** archive mismatch as unreproduced, not automatically disproved.

**Negative knowledge:** no Julia runtime here; no fully sourced subtable antinucleon emission; no BBN abundance calculations; no validated physical signal; no novel theorem, no Moderator EXEC sign. `GITHUB_WRITE != BW_INGEST != REFEREE_PASS != PHYSICAL_UPGRADE`.


---

## 7. Complete executed and prepared source files (verbatim)

### `reproduce_event_interpolation_gate_016.py`

```python
#!/usr/bin/env python3
"""MECH-S7 ROT016. Archive-only event reconstruction and analytic interpolation counterexample.
NO Julia accepted-step capture. Synthetic log-linear example is NOT SciML dense output.
"""
import csv, hashlib, json, math, zipfile
from pathlib import Path
import numpy as np
import pandas as pd

OUT=Path(__file__).resolve().parent
G=4.207579833788249e27 # g^3/s, Wu-Xu N_rho plateau, ROT004 audit
Mi=6e9
Medge=1e9
Mcut=Mi*math.exp(-20)
ARCHIVES={
    'public':('mech_s6_public_2x2_raw.zip','75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5'),
    'paper':('mech_s6_paper_2x2_raw.zip','3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e'),
}
files={'public':{'exec':'trajectory_current.csv','sym':'trajectory_repaired.csv'},
       'paper':{'exec':'trajectory_paper_exec.csv','sym':'trajectory_paper_sym.csv'}}

def shasum(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def event_from_two_rows(t0,t1,m0,m1,target,form):
    assert m0>target>m1
    if form=='mass': frac=(m0-target)/(m0-m1)
    elif form=='mass_cube':frac=(m0**3-target**3)/(m0**3-m1**3)
    elif form=='log_mass':frac=(math.log(m0)-math.log(target))/(math.log(m0)-math.log(m1))
    else:raise ValueError(form)
    return t0+(t1-t0)*frac

def write_csv(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

allres=[]; summaries=[]
for source,(zipname,expected) in ARCHIVES.items():
    zp=OUT/zipname
    if not zp.exists():zp=Path('/mnt/data')/zipname
    if shasum(zp)!=expected:raise RuntimeError('Original SHA mismatch '+str(zp))
    with zipfile.ZipFile(zp) as z:
        for mapping,file in files[source].items():
            df=pd.read_csv(z.open(file))
            assert len(df)==1600
            mask=df.source_active.astype(bool).to_numpy()
            active=np.flatnonzero(mask);k=int(active[-1]);assert k==1469
            assert df.iloc[k]['m_PBH_g']>Medge>df.iloc[k+1]['m_PBH_g']
            t0=float(df.iloc[0]['t_sec']);tfirst=float(df.iloc[k]['t_sec']);tlast=float(df.iloc[k+1]['t_sec']);mfirst=float(df.iloc[k]['m_PBH_g']);mlast=float(df.iloc[k+1]['m_PBH_g']);
            texact_edge=t0+(Mi**3-Medge**3)/G
            texact_cut=t0+(Mi**3-Mcut**3)/G
            tbridge_edge=tfirst+(mfirst**3-Medge**3)/G
            tbridge_cut=tfirst+(mfirst**3-Mcut**3)/G
            duration=tlast-tfirst
            summary={'branch':source+'_'+mapping,'t_first_active_sec':tfirst,'t_first_off_sec':tlast,'archive_gap_sec':duration,'m_last_active_g':mfirst,'m_first_off_g':mlast,'exact_edge_t_sec':texact_edge,'exact_cut_t_sec':texact_cut,'exact_subedge_sec':texact_cut-texact_edge,'archive_gap_over_true_subedge':duration/(texact_cut-texact_edge),'edge_gap_fraction_exact':(texact_edge-tfirst)/duration,'cut_gap_fraction_exact':(texact_cut-tfirst)/duration,'edge_t_reanchored_last_sec':tbridge_edge,'edge_t_reanchoring_shift_sec':tbridge_edge-texact_edge}
            assert tfirst<texact_edge<texact_cut<tlast
            for form in ('mass','mass_cube','log_mass'):
                edge=event_from_two_rows(tfirst,tlast,mfirst,mlast,Medge,form)
                cutoff=event_from_two_rows(tfirst,tlast,mfirst,mlast,Mcut,form)
                row={'branch':source+'_'+mapping,'method':'2-point_'+form,'edge_t_sec':edge,'cut_t_sec':cutoff,'edge_minus_exact_sec':edge-texact_edge,'cut_minus_exact_sec':cutoff-texact_cut,'inferred_subedge_sec':cutoff-edge,'subedge_over_true':(cutoff-edge)/(texact_cut-texact_edge),'sample_gap_sec':duration,'source_active_sample_count_below_edge':int(sum(mask&(df.m_PBH_g.to_numpy()<Medge)))}
                allres.append(row)
            summaries.append(summary)

# Synthetic counterexample: both knot endpoints are EXACT cube-law states in physical t,
# but the plausible generic componentwise dense interpolation linear in ln M
# has a nonconstant cube-law secant and large local secant residual.
# This is NOT the SciML interpolation formula, not the real accepted mesh.
Ma,Mb=3.0e9,2.9e9
Ta=0.0;Tb=(Ma**3-Mb**3)/G
p=np.linspace(0,1,101)
tsynthetic=Ta+(Tb-Ta)*p
mlog=np.exp((1-p)*math.log(Ma)+p*math.log(Mb))
mcube=((1-p)*Ma**3+p*Mb**3)**(1/3)
clock=(mlog**3+G*tsynthetic-Ma**3)/G
local=-(mlog[1:]**3-mlog[:-1]**3)/(G*(tsynthetic[1:]-tsynthetic[:-1]))
resmass=mlog/mcube-1
syn_rows=[{'fraction':p[i],'t_sec':tsynthetic[i],'m_loglinear_g':mlog[i],'m_exact_cube_g':mcube[i],'relative_mass_error':resmass[i],'cube_clock_defect_sec':clock[i],'local_step_gamma_over_exact':(local[i-1] if i>0 else '')} for i in range(len(p))]
write_csv(OUT/'source_archive_event_estimates_016.csv',allres)
write_csv(OUT/'event_gap_archived_summary_016.csv',summaries)
write_csv(OUT/'synthetic_exact_knot_logmass_dense_counterexample_016.csv',syn_rows)
result={'source':'Wu-Xu d395183674cace6c9906a8911bdeb7234ba4040d; original Actions two 2x2 archives','gamma_g3_per_s':G,'M_edge_g':Medge,'M_cut_g':Mcut,'archive_gap_4branch':summaries,'event_2pt_estimates':allres,'synthetic_exact_accepted_endpoints':{'m_a_g':Ma,'m_b_g':Mb,'t_a_sec':Ta,'t_b_sec':Tb,'M3_error_at_both_knot_endpoints':0,'max_abs_synthetic_mass_relative_error':float(np.max(abs(resmass))),'min_local_gamma_ratio':float(np.min(local)),'max_local_gamma_ratio':float(np.max(local)),'max_clock_error_seconds':float(np.max(abs(clock))),'interpolant':'linear in log mass vs physical time; illustrative, NOT SciML'} ,'warnings':['Original Julia runtime is not invoked','Two-point archive interpolation is not the author SciML dense interpolant','Synthetic internal knots not observed accepted steps','Cubic mass law exact only inside source defined plateau and before evaporation','No physical source or BBN bound']}
(OUT/'result_016.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for x in summaries:print(x['branch'],'saved gap sec',x['archive_gap_sec'],'true subedge sec',x['exact_subedge_sec'],'gap ratio',x['archive_gap_over_true_subedge'])
for row in allres:
  if row['branch']=='public_exec':print(row['method'],'edge error',row['edge_minus_exact_sec'],'subedge ratio',row['subedge_over_true'])
print('synthetic max mass error',np.max(abs(resmass)),'local gamma ratio',min(local),max(local))

```

### `independent_decimal_controls_016.py`

```python
#!/usr/bin/env python3
"""Independent Decimal high-precision check, not SciML / Julia replay."""
from decimal import Decimal, localcontext
import zipfile, csv, io, json
from pathlib import Path
P=Path(__file__).resolve().parent
with localcontext() as ctx:
 ctx.prec=65
 D=Decimal
 gam=D('4.207579833788249e27'); initial=D('6e9'); edge=D('1e9'); cutoff=initial * (-D(20)).exp()
 with zipfile.ZipFile(P/'mech_s6_public_2x2_raw.zip') as z:
  rows=list(csv.DictReader(io.TextIOWrapper(z.open('trajectory_current.csv'),encoding='utf-8')))
 active=[r for r in rows if Decimal(r['source_active'])==1]
 assert len(active)==1470, len(active)
 r0=rows[0];a=rows[1469];b=rows[1470]
 t0=D(r0['t_sec']); ta=D(a['t_sec']);tb=D(b['t_sec']); ma=D(a['m_PBH_g']);mb=D(b['m_PBH_g']);
 true_edge=t0+(initial**3-edge**3)/gam
 true_cut=t0+(initial**3-cutoff**3)/gam
 inverse={}
 for form in ('mass','mass_cube','log_mass'):
  if form=='mass':weight=(ma-edge)/(ma-mb)
  elif form=='mass_cube':weight=(ma**3-edge**3)/(ma**3-mb**3)
  else:weight=(ma.ln()-edge.ln())/(ma.ln()-mb.ln())
  inverse[form]=float(ta+(tb-ta)*weight)
 out={'control':'65-digit Decimal read directly from original CSV strings','edge_time':str(true_edge),'cut_time':str(true_cut),'inverse_t':inverse,'cut_duration':str(true_cut-true_edge)}
 saved=json.loads((P/'result_016.json').read_text())
 assert abs(float(true_edge)-saved['archive_gap_4branch'][0]['exact_edge_t_sec'])<2e-13
 assert abs(float(true_cut)-saved['archive_gap_4branch'][0]['exact_cut_t_sec'])<2e-13
 for row in saved['event_2pt_estimates']:
  if row['branch']=='public_exec':
   f=row['method'].replace('2-point_','')
   assert abs(inverse[f]-row['edge_t_sec'])<2e-13, (f,inverse[f],row['edge_t_sec'])
 (P/'decimal_controls_016.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DECIMAL_65_SOURCE_CSV_EVENT_CONTROLS_PASS')

```

### `instrument_wuxu_accepted_and_dense_016.py`

```python
#!/usr/bin/env python3
"""Static Julia source patcher for ORIGINAL Wu-Xu main-scan.jl pinned d395183... .
Copies input to a new file. DOES NOT execute Julia or claim syntax-tested with Julia.
Usage: python instrument_wuxu_accepted_and_dense_016.py /path/main-scan.jl /path/main-scan-instrumented.jl
Environment when running Julia: MECH_S7_ACCEPTED_MONITOR=1,
MECH_S7_TARGET_M_G=6e9, MECH_S7_TARGET_BETA=1e-16,
MECH_S7_SOURCE_BRANCH=public_exec (or other label).
Author's source must have the exact two-line anchor; checked from pinned GitHub file.
"""
import sys
from pathlib import Path

ANCHOR='''    a_list = geomspace(a_f, a_end, num_points)
    results_list = (evolution_solution ∘ log).(a_list)'''
SNIPPET=r'''

    # MECH-S7 ROT016: observational probe. Captures separately the solver-saved
    # step points sol.t/sol.u and the later dense samples sol(log(a_list)).
    # IMPORTANT: sol.t/sol.u are saved step states when save_everystep=true;
    # the user must verify solver retcode and stage/accepted-step semantics.
    if get(ENV, "MECH_S7_ACCEPTED_MONITOR", "0") == "1"
        target_m = parse(Float64, get(ENV, "MECH_S7_TARGET_M_G", "6e9"))
        target_beta = parse(Float64, get(ENV, "MECH_S7_TARGET_BETA", "1e-16"))
        if isapprox(Float64(m_PBH / NU.g), target_m; rtol=1e-10) &&
           isapprox(Float64(β_PBH), target_beta; rtol=1e-10)
            branch = replace(get(ENV, "MECH_S7_SOURCE_BRANCH", "unknown"), r"[^A-Za-z0-9_-]" => "_")
            mkpath(output_data_directory)
            # Recorded metric here follows the PINNED PDG high-T plateau;
            # do not treat Gamma as physics outside the plateau.
            Gamma_g3s = 4.207579833788249e27
            formation_mass_g = Float64(m_PBH / NU.g)
            formation_time_s = Float64(t_f / NU.s)
            for (label, etas, states) in (("saved_steps", evolution_solution.t, evolution_solution.u),
                                          ("dense_samples", log.(a_list), results_list))
                outpath = joinpath(output_data_directory, "MECH_S7_$(branch)_$(label)_016.csv")
                open(outpath, "w") do io
                    println(io, "row,eta,log_t_EU,log_M_EU,t_sec,m_g,source_on,cube_residual_sec")
                    for (ii, (eta_now, state)) in enumerate(zip(etas, states))
                        current_t = Float64(EU(exp(state[1]), -1) / NU.s)
                        current_m = Float64(EU(exp(state[3]), 1) / NU.g)
                        residual = (current_m^3 + Gamma_g3s*(current_t-formation_time_s)-formation_mass_g^3) / Gamma_g3s
                        source_on = state[3] > log_m_PBH_evaporated_in_EU ? 1 : 0
                        println(io, string(ii, ",", Float64(eta_now), ",", state[1], ",", state[3], ",",
                            current_t, ",", current_m, ",", source_on, ",", residual))
                    end
                end
            end
        end
    end
    # END MECH-S7 ROT016 observational probe
'''

def patch(text):
    if text.count(ANCHOR)!=1:raise ValueError(f'Expected unique original source anchor; got {text.count(ANCHOR)}')
    if 'MECH-S7 ROT016' in text:raise ValueError('Already instrumented')
    return text.replace(ANCHOR,ANCHOR+SNIPPET)

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    orig,dest=map(Path,sys.argv[1:]); assert orig.resolve()!=dest.resolve()
    dest.write_text(patch(orig.read_text(encoding='utf-8')),encoding='utf-8')
    print(f'Static patch output: {dest}, bytes={dest.stat().st_size}. Julia syntax NOT runtime verified')

```
