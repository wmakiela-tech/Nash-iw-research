# MECH-S7 ROT017 — source-native precision gate at Wu–Xu PBH evaporation cutoff (2026-10-24)

**LINEAGE:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`  
**PROBLEM:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**RETURN_ID:** `MECH-S7-FRONTB-SOURCE-NATIVE-PRECISION-AND-CUTOFF-INSTRUMENTATION-017_20261024`  
**CLASS:** Executed independent exact numerical representation analysis; source-code audit; corrected static Julia diagnostic patch. **NOT** an original Julia run; no physical PBH/BBN claim.

## 1. Scope, prior work and source evidence

**OTHERS FIRST / own lineage:** MECH ROT004 derives mass-cube law for the source's constant high-energy degrees-of-freedom plateau; ROT013 repairs mis-transplanted hadron state at 10^9g; ROT014 separates clock-origin gauge and altered evaporation coefficient; ROT015 measures deviations of archived 1600-sample mass curves from the cube invariant; ROT016 proves that accepted-integrator errors cannot be inferred from sparse dense-output samples, provides a counterexample, and prepares a Julia instrumenter. REC10: source-off does NOT remove existing hadrons; MT13/LT5: fixed-temperature event target; DAX/PRF11: separate thermal/EOS and source-vs-observable typing.

**Pinned primary source:** Wu–Xu `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl`, `main-scan-parameters.jl`, `tool_script-parameters.jl`.

Source-local contract, checked against GitHub fetch on ROT017:
* `BITS=100`, initial scan mass and beta explicitly constructed with `ArbFloat(...;bits=BITS)` (`main-scan-parameters.jl`); `a_f=ArbFloat(1;bits=BITS)` (`main-scan.jl`). These are **declared input precision**, not independent certificate of a solver trajectory's effective accuracy.
* cutoff: `log_m_PBH_evaporated_in_EU = max(log(m_PBH)-20, log(m_Pl))`; for `M_i=6e9g`, first branch sets **M_cut=M_i exp(-20)=12.366921734631...g**.
* discontinuous RHS switch `PBH_evaporated_flag = log_m_PBH_in_EU ≤ log_m_PBH_evaporated_in_EU`; sets `n_PBH=0`, `d_m_PBH_dt=0`, and turns off fresh hadron emission, **not** surviving hadron populations.
* original `solve(evolution_problem, AutoTsit5(Rosenbrock23()))` call has no explicitly supplied `callback`, `tstops`, `reltol`, or `abstol` in inspected main file. This is a code observation, **not** proof that SciML never detects or resolves the switch.
* archived outputs are generated from `results_list=(evolution_solution ∘ log).(a_list)` and converted to Float64 in dump. Thus the archived grid is NOT equivalent to accepted-step trace at native precision.

**Important audit of our own work:** ROT016 monitor computed `current_t`, `current_m`, the cube invariant and event diagnostics **after casting to Float64** and also pinned a displayed ~16-digit `Γ=4.207579833788249e27g³/s`. That instrument is insufficient to test the last ~10^-25s of a 100-bit source trajectory. This finding **supersedes ROT016's instrumentation adequacy at cutoff**, not ROT016's independently executed interpolation counterexample.

## 2. Exact precision bound: subtraction at t ≈ 51.3359 seconds

For the source plateau,

\[
\frac{dM^3}{dt}=-\Gamma,\qquad
\Gamma_{\mathrm{display}}=4.207579833788249\times10^{27}\ \mathrm{g^3/s},\qquad
\tau(M)=M^3/\Gamma.
\]

The cutoff remaining lifetime is **4.4952357399230644×10^-25 s** (conditional displayed Gamma; the 16-digit gamma input suffices for this representation-scale estimate, NOT for a native 100-bit exact residual).

At t in `[32,64)` seconds, a binary `p`-bit significand has temporal spacing **ULP=2^(6-p) s**. For `M_cut` to remain distinguishable from the formal zero-mass epoch, **ULP ≲ M_cut³/Γ** is required. This is *necessary* for explicit time representation; it does not imply local/global ODE accuracy, event rootfinding success or physical source validity.

| p (bits) | ULP at 51s (s) | mass with τ=1 ULP (g) | cutoff lifetime in ULPs |
|---:|---:|---:|---:|
| 53 | 7.105427357601e-15 | 31036.60361 | 6.32648e-11 |
| 64 | 3.469446951954e-18 | 2443.97939 | 1.29566e-7 |
| 80 | 5.293955920339e-23 | 60.61837 | 8.49126e-3 |
| 87 | 4.135903062765e-25 | 12.02821 | 1.08688 |
| 90 | 5.169878828456e-26 | 6.01410 | 8.69505 |
| 94 | 3.231174267785e-27 | 2.38670 | 139.121 |
| **100** | **5.048709793414e-29** | **0.59667** | **8903.73** |
| 113 | 6.162975822039e-33 | 0.02960 | 7.29394e7 |

The exact mathematical representation test with `mpmath` reproduces that `t_cut - τ_cut` rounds to `t_cut` at p=53,64,80; it remains distinct for p≥87. **Do not claim p=87 is sufficient for numerical ODE precision**: one represented ULP allows no error budget.

Another source-type issue: a Float64 `Γ` rounded to 16 digits creates a relative coefficient error at ~1e-16; accumulated over a 51s lifetime it can create absolute cube-law residual ~5e-15s, far **larger** than the cutoff lifetime. The appropriate high-precision invariant must derive its `Γ_native = 3*N_BH(T_BH(m_i))*NU.m_Pl^4` from exactly the same native source code and numerical types as the ODE, inside the true PDG high-temperature plateau. Matching a source-native invariant is not equivalent to validating its physical coefficients.

## 3. Independent source fluence negative control

The precision hole in a Float64 time trace is NOT automatically a large physical endpoint error. Under the **declared conditional paper law** `Q(M)∝M^-1.3`, with `dt/dM∝M²`, the number emitted in a mass interval scales as `∫M^0.7dM`.

The mass scale corresponding to one Float64 time ULP is ~31,036.6g. The fraction of emitted hadrons from `M_cut` up to 31,036.6g, relative to emission from `M_cut` to `10^9g`, is **2.16862969588×10^-8**. This is a simple conditional power-law **unweighted emitted number** estimate, not a bound on the neutron endpoint; nontrivial survival kernels, signed cancellation and dynamical feedback can modify relative endpoint sensitivity. It prevents falsely reading numerical cutoff-time invisibility as proof of a large source-fluence error or invalid 10D result.

## 4. Audit of original saved 2x2 archives

Both original GitHub Actions artifacts were re-read as ZIPs. All four runs have 1600 archived rows, exactly 1470 source-active rows, and zero source-active rows below 10^9g. Last active masses: `1.8366330858522944e9g` (`exec`) and `1.835347299766672e9g` (`sym`), identical across public/paper before the table edge. These archive facts establish inadequate **output sampling**, not absence of internal accepted steps, nor native arithmetic type.

## 5. Corrected observational Julia monitor, prepared NOT executed

Artifact: `instrument_wuxu_native_precision_017.py`. It replaces precisely one pinned two-line output anchor, preserves the original solve call and 10D equations, and writes two distinct CSVs: `solver_saved` (`sol.t` and `sol.u`) and `dense_sampled` (the author's `results_list` on 1600-point-like `a_list`). The corrected `t`, `M`, `remaining_time`, `Γ` and invariant are computed and serialized **without Float64 downcasting**. A floating cast occurs only in the optional *target-selection predicate* for matching `(M_i,β)`; it is not used for monitoring. For points after `source_off`, cubic invariant comparison is suppressed, since source intentionally freezes M.

Native coefficient: `Γ_cube_native = 3*N_BH(T_BH(m_PBH))*NU.m_Pl^4`; source code's actual dimensional wrappers are retained. This construction is valid as a constant cubic law only on the verified high-T plateau; never extend it to lower temperatures uncritically.

**STILL OPEN:** The actual patched Julia code has NOT been parsed, compiled or executed under Julia or SciML. The original source was checked via GitHub connector, and the patcher exercised on a mock extraction of pinned Julia statements. Exact branch checks, double-patch rejection, preserved solver statement, native arithmetic checks, and negative tests: **11/11 static PASS**. Native-print precision and `precision(::ArbFloat)` applicability require actual runtime verification; fallback `-1` is logged where applicable. Patching original source and running the Python structure test does not constitute solving the 10D model.

**Scientific acceptance gate for a Julia follow-up:** pin repository SHA and Julia/ArbNumerics/SciML environment; capture complete `sol.t`/`sol.u` and `sol(log(a_list))` with native precision and `retcode`/integrator `destats`; observe the cutoff mass event with exact source flag, record pre/post states including nPBH and all hadrons; recompute `Γ_native` and the source-supported cube invariant strictly **before** cutoff; run a tolerance ladder with a physically matched terminal `T_nuc` event. Only then compare accepted-step residuals, dense-output residuals and endpoint difference. Consider an **explicit continuous cutoff callback as a separate counterfactual run**, never silently reinterpreting it as what the unmodified code originally did.

## 6. Reproduction, provenance and stop status

Executed in Python: `reproduce_precision_event_gate_017.py`, `validate_native_precision_patch_017.py`; source ZIP check and output CSV/JSON. `precision_ladder_017.csv`, `archive_source_event_017.csv`, `precision_gate_017.json`, `static_native_patch_tests_017.json`. Standalone `instrument_wuxu_native_precision_017.py` static patcher.

Source-native reference: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl and corresponding `main-scan-parameters.jl`, `tool_script-parameters.jl`.

Reference numerical solver documentation: https://docs.sciml.ai/DiffEqDocs/stable/features/callback_functions/ (continuous rootfinding and cutoff event handling); https://docs.sciml.ai/OrdinaryDiffEq/dev/api/common_interface/ (step storage, dense output, and discontinuity concerns). Documentation describes supported facilities, **not** a diagnosis of how the pinned original run behaved.

**NEW DECISION:** amend ROT016 instrument's cutoff certification requirement immediately: neither `Float64` time nor Float64 `Γ` can establish native-precision invariant validity at 12.37g. The artifact is a revised, syntactically unvalidated monitor plus an executed *exact representation* gate. Do not claim a proved original Julia solver defect, a bound on final X or an astrophysical PBH exclusion.

**STOP:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_MODERN_Yp_DH / NO_PBH_BOUND / BW_INGEST_UNVERIFIED / ORIGINAL_JULIA_10D_NOT_EXECUTED`.



---

## APPENDIX: Complete executed Python code and prepared Julia source instrumenter


### `reproduce_precision_event_gate_017.py`

```python
#!/usr/bin/env python3
"""Mech-S7 ROT017: exact source-cutoff representation and native-precision logging gate.
This is a mathematical precision experiment, NOT the original Wu-Xu Julia 10D run.
Inputs: source commit d395183, ROT004 cube-law Gamma and the author's BITS=100 and exp(-20) cutoff.
"""
from pathlib import Path
import csv, json, hashlib
import mpmath as mp
import numpy as np
from zipfile import ZipFile

HERE=Path(__file__).resolve().parent
MI=mp.mpf('6000000000')
GAMMA=mp.mpf('4.207579833788249e27')
TCUT_DISPLAY='51.33592433955715' # decimal display of ROT016 exact source mass-cube event
FIELDS=[53,64,80,87,90,94,100,106,113,128]
mp.mp.dps=90
MCUT=MI*mp.exp(-20)
DELTACUT=MCUT**3/GAMMA
TCUT=mp.mpf(TCUT_DISPLAY)
ln_mass_range=mp.log(MI/MCUT,2)
records=[]
for p in FIELDS:
    with mp.workprec(p):
        t0=mp.mpf(TCUT_DISPLAY)
        tau=mp.mpf(str(DELTACUT))
        tpre=t0-tau
        delta=t0-tpre
        resolved=bool(tpre!=t0)
    ulp=mp.power(2,6-p) # time t around 51 sec is in binary [32,64) bin
    m_ulp=mp.root(GAMMA*ulp,3)
    ratio=DELTACUT/ulp
    records.append(dict(bits=p,ulp_at_51_sec=mp.nstr(ulp,18),mass_cuberoot_of_one_ulp_g=mp.nstr(m_ulp,18),
                        cutoff_remaining_time_sec=mp.nstr(DELTACUT,18),ulps_in_cutoff_lifetime=mp.nstr(ratio,17),
                        can_resolve_cutoff_lifetime_from_event_time=resolved,
                        stored_interval_sec=mp.nstr(delta,17)))

with (HERE/'precision_ladder_017.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)

# Provable non-implication control: cutoff is not an integrated-fluence catastrophe.
# For dN/dt ~ M^-1.3 and -dM/dt=C/M^2, dN ~ M^0.7 dM.
paper_index=mp.mpf('1.3')
mu53=mp.root(GAMMA * mp.power(2,6-53),3)
frac_deep=(mu53**(3-paper_index)-MCUT**(3-paper_index))/(mp.mpf('1e9')**(3-paper_index)-MCUT**(3-paper_index))

# Correct source threshold taken from default log_m_PBH_evaporated_ratio=20:
assert abs(float(MCUT)-12.366921734631347)<1e-11
assert records[0]['can_resolve_cutoff_lifetime_from_event_time']==False
assert records[6]['can_resolve_cutoff_lifetime_from_event_time']==True

# Data source check, no unknown paths or claims.
archive_rows=[]
for fname in ['mech_s6_public_2x2_raw.zip','mech_s6_paper_2x2_raw.zip']:
    zip_path=Path('/mnt/data')/fname
    with ZipFile(zip_path) as z:
        for item in z.namelist():
            if not item.endswith('.csv'): continue
            import io
            import pandas as pd
            df=pd.read_csv(io.BytesIO(z.read(item)))
            active=df[df['source_active'].astype(bool)]
            archive_rows.append({'archive':fname,'trajectory':item,'n_total':len(df),'n_active':len(active),'n_active_below_edge':int((active['m_PBH_g']<1e9).sum()),'last_active_mass_g':float(active['m_PBH_g'].iloc[-1])})
with (HERE/'archive_source_event_017.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(archive_rows[0]));w.writeheader();w.writerows(archive_rows)

result={
 'source':'Wu-Xu primary pinned d395183674cace6c9906a8911bdeb7234ba4040d and original Mech-S6 Actions 2x2 archives',
 'status':'EXECUTED_MATHEMATICAL_PRECISION_GATE; original Julia 10D NOT_EXECUTED',
 'B_native_source_bits':100,
 'M_initial_g':int(MI),
 'M_cut_g':mp.nstr(MCUT,40),
 'Gamma_g3_per_s_input_round_16digits':mp.nstr(GAMMA,20),
 'cutoff_remaining_time_s':mp.nstr(DELTACUT,36),
 'binary_log2_mass_ratio':mp.nstr(ln_mass_range,20),
 'event_time_printed_anchor_s':TCUT_DISPLAY,
 'precision_ladder':records,
 'mass_floor_53bit_g':mp.nstr(mu53,30),
 'emitted_fluence_fraction_Mcut_to_floor53_within_Mcut_to_1e9_paper_powerlaw':mp.nstr(frac_deep,22),
 'negative_knowledge': ['100-bit configured, effective precision of solver NOT certified','cutoff temporal representability is necessary not sufficient for solver convergence','53-bit output time fails event-scale logging, not automatically physical endpoint','mass-law Gamma from earlier 16-digit numeric pin cannot certify 100-bit invariant by itself','emitted-fluence fraction computed only for conditional power-law extrapolation'],
 'archive':archive_rows
}
(HERE/'precision_gate_017.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
for row in records: print(f"bits={row['bits']:3d} ulp={row['ulp_at_51_sec']} sec, M_ulp={row['mass_cuberoot_of_one_ulp_g']}g, cutoff_ulps={row['ulps_in_cutoff_lifetime']}, resolve={row['can_resolve_cutoff_lifetime_from_event_time']}")
print('cutoff remaining',mp.nstr(DELTACUT,30))
print('deep unresolved fraction if 53b',mp.nstr(frac_deep,23))
print(json.dumps(archive_rows,indent=2))

```


### `validate_native_precision_patch_017.py`

```python
#!/usr/bin/env python3
"""ROT017 static integrity and native-precision monitor smoke tests (no Julia runtime)."""
from pathlib import Path
import inspect, sys, json
sys.path.insert(0,str(Path(__file__).resolve().parent))
from instrument_wuxu_native_precision_017 import patch, ANCHOR, SOLVE, CHECKS, SNIPPET

def expect_fail(s):
    try:patch(s)
    except ValueError:return True
    return False
src='\n'.join(CHECKS[:-1])+'\n'+SOLVE+'\n'+ANCHOR+'\n'
new=patch(src)
checks={
  'unique_pinned_anchor':src.count(ANCHOR)==1,
  'source_original_solver_preserved':new.count(SOLVE)==1,
  'original_solver_return_and_grid_preserved':ANCHOR in new,
  'native_time_and_mass_no_downcast':('Float64(t_now)' not in SNIPPET and 'Float64(m_now)' not in SNIPPET),
  'native_cube_residual_no_float_gamma':('Γ_cube_native = 3 * N_BH(T_BH(m_PBH)) * NU.m_Pl^4' in SNIPPET and '4.207579' not in SNIPPET),
  'both_saved_and_dense_observed':'solver_saved' in SNIPPET and 'dense_sampled' in SNIPPET,
  'source_on_only_cubic_invariant':'is_active ?' in SNIPPET and 'cube_residual_sec_native' in SNIPPET,
  'no_callback_or_rerun':('ContinuousCallback' not in SNIPPET and 'solve(' not in SNIPPET),
  'rejects_double_patch':expect_fail(new),
  'rejects_ambiguous_anchor':expect_fail(src+ANCHOR),
  'rejects_mismatched_source':expect_fail('hello'),
}
assert all(checks.values()),checks
out=Path(__file__).resolve().parent/'static_native_patch_tests_017.json'
out.write_text(json.dumps({'checks':checks,'status':'PASS; not Julia parser/runtime compilation'},indent=2)+'\n')
print(json.dumps(checks,indent=2))

```


### `instrument_wuxu_native_precision_017.py`

```python
#!/usr/bin/env python3
"""ROT017 pin-sensitive STATIC source modifier: preserves author Julia scalar precision.

Usage: python instrument_wuxu_native_precision_017.py PINNED/main-scan.jl new.jl
EXPECTED SOURCE: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d.

DOES NOT execute or syntax-compile Julia. The patched source observes the original solver
and stores saved-step versus dense-sampled states at native precision in separate CSVs.

Environment variables:
  MECH_S7_NATIVE_MONITOR=1     enable one target run
  MECH_S7_TARGET_M_G=6e9       targeted initial mass [grams]
  MECH_S7_TARGET_BETA=1e-16    targeted initial beta
  MECH_S7_BRANCH=public_exec   output label, sanitized
"""
from pathlib import Path
import sys

ANCHOR='''    a_list = geomspace(a_f, a_end, num_points)
    results_list = (evolution_solution ∘ log).(a_list)'''
SOLVE='''    evolution_solution = solve(evolution_problem, AutoTsit5(Rosenbrock23()))'''
CHECKS=(
  'PBH_evaporated_flag = log_m_PBH_in_EU ≤ log_m_PBH_evaporated_in_EU',
  'PBH_evaporated_flag && (d_m_PBH_dt = zero(d_m_PBH_dt))',
  'log_m_PBH_evaporated_in_EU = max(',
  'n_PBH = PBH_evaporated_flag ? zero(n_PBH_ini)',
  'BITS = 100', # parameter file separate, not main source; do not insist in main-scan
)
SNIPPET=r'''
    # MECH-S7 ROT017 native-precision observational monitor. Same original ODE solve.
    # No callback, no artificial mass/time forcing. The original solver saves sol.t/u.
    # Observe the exact pre-cutoff invariant only where mass is source-active.
    if get(ENV, "MECH_S7_NATIVE_MONITOR", "0") == "1"
        target_m_g = parse(Float64, get(ENV, "MECH_S7_TARGET_M_G", "6e9"))
        target_beta = parse(Float64, get(ENV, "MECH_S7_TARGET_BETA", "1e-16"))
        if isapprox(Float64(m_PBH / NU.g), target_m_g; rtol=1e-10) &&
           isapprox(Float64(β_PBH), target_beta; rtol=1e-10)
            label = replace(get(ENV,"MECH_S7_BRANCH","unknown"),r"[^A-Za-z0-9_-]" => "_")
            mkpath(output_data_directory)
            # Cubic coefficient computed using source's native-typed formula, not a
            # 16-significant-digit Float64 literature/display constant.
            Γ_cube_native = 3 * N_BH(T_BH(m_PBH)) * NU.m_Pl^4
            mcut_native = EU(exp(log_m_PBH_evaporated_in_EU), 1)
            for (kind, etas, us) in (("solver_saved", evolution_solution.t, evolution_solution.u),
                                      ("dense_sampled", log.(a_list), results_list))
                outfile=joinpath(output_data_directory,"MECH_S7_ROT017_$(label)_$(kind).csv")
                open(outfile,"w") do io
                    println(io,"idx,eta_native,time_sec_native,mass_g_native,source_on,remaining_to_cut_sec_native,cube_residual_sec_native,event_time_from_state_sec_native,precision_bits_time,precision_bits_mass")
                    for (j,(η_now,state)) in enumerate(zip(etas,us))
                        t_now = EU(exp(state[1]), -1)
                        m_now = EU(exp(state[3]), 1)
                        is_active = state[3] > log_m_PBH_evaporated_in_EU
                        remaining = is_active ? ((m_now^3 - mcut_native^3)/Γ_cube_native) / NU.s : NaN
                        residual = is_active ? ((m_now^3 + Γ_cube_native*(t_now-t_f) - m_PBH^3)/Γ_cube_native) / NU.s : NaN
                        t_event_by_now = is_active ? (t_now + (m_now^3 - mcut_native^3)/Γ_cube_native) / NU.s : NaN
                        p_t = try precision(state[1]) catch; -1 end
                        p_m = try precision(state[3]) catch; -1 end
                        # NEVER cast time/mass/residual to Float64 on this path.
                        println(io, join((string(j), string(η_now), string(t_now/NU.s),
                             string(m_now/NU.g), is_active ? "1" : "0", string(remaining),
                             string(residual), string(t_event_by_now), string(p_t), string(p_m)), ","))
                    end
                end
            end
        end
    end
    # END MECH-S7 ROT017 monitor
'''

def patch(s):
    if s.count(ANCHOR)!=1: raise ValueError('Pinned source anchor count != 1')
    if s.count(SOLVE)!=1: raise ValueError('Pinned solver statement count != 1')
    for line in CHECKS[:-1]:
        if line not in s: raise ValueError('Source branch contract missing: '+line)
    if 'MECH-S7 ROT017' in s:raise ValueError('Cannot patch twice')
    return s.replace(ANCHOR,ANCHOR+SNIPPET)

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit(__doc__)
    src,dst=map(Path,sys.argv[1:])
    if src.resolve()==dst.resolve():raise ValueError('Refusing in-place modification')
    s=patch(src.read_text(encoding='utf-8'))
    dst.write_text(s,encoding='utf-8')
    print('Wrote original solver + native precision observer:',dst,'bytes:',len(s.encode()))
    print('Static-only patch. Julia compilation and 10D execution NOT performed.')

```