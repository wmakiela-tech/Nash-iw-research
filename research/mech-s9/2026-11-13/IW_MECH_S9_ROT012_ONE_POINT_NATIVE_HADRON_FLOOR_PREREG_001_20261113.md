---
artifact_id: IW_MECH_S9_ROT012_SINGLE_WUXU_NATIVE_HADRON_RAW_VS_EFFECTIVE_FLOOR_DIAGNOSTIC_PREREG_001_20261113
created_at: 2026-11-13
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: PREDECLARED_BOUNDED_ORIGINAL_SOURCE_DIAGNOSTIC
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ONE_FROZEN_MODEL_SOURCE_NATIVE_TRACE / NO_PBH_BOUND / NO_NOVELTY / NO_JCAP_FIG5_BUILD_ID / NO_E4_UNBLOCK / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# ROT012 prereg — one pinned Wu–Xu native Julia six-hadron dual RAW/RHS floor history

## Original scientific lineage / status BEFORE execution

Wu/Xu FIRST wrote the original scientific PBH/BBN model and its 10D source `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, original `arXiv-2509.05618/main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. The authors are not contacted; this frozen old v2 repo is NOT authenticated final journal Fig5 build. Badacz (Claude) FIRST authored REVIEW053 and self-corrected j22 V2 coarse fit in prereg064/REVIEW065; Mech-S9 GPT L1 53/53 full source native equality and 57-call independent native L2 later original owner correction observed. EKS1 (Claude) FIRST recovered working remote Julia via Mech-S6. The **log-population numerical floor and dual raw-vs-used contract** was FIRST identified in LT8 ROT014–015, whose source-first finding is explicitly acknowledged here; INT9 ROT021/022 floor-forcing inequality and physical units, AUD2 ROT003 certified terminal no-floor conditional and independent bounded referee, are prior claims; Mech-S9 will NOT claim these proofs as new.

Original direct source:
- lines53–58: for six hadrons RHS *effective* `n_eff,h=EU(exp(max(log_n_raw,h,-100)),3)`;
- lines87–99: these effective species enter `dX_n/dt`;
- lines145–149: `magic(m,beta;hadrons_output_flag=true,dump_flag=false)`;
- lines182–192: return raw `exp(log_n_raw,h)` per species;
- lines232–237: `hadrons_output_flag=true` adds six raw arrays and returns **13** slots, original helium channel remains **slot 7**. Never use `last(magic)` under this flag.

## One preregistered original source input and budget

Single mass **j=22 (zero-based)** from ORIGINAL 100-point author mass grid `m_PBH_f_list[23]` corresponding m≈1.121174e9 g. `x=log10 beta=-16.9974609375`, original independently generated GPT L2 V2 adaptive root center `43310359194`, NOT an inferred physical PBH exclusion boundary. `beta=ArbFloat(10.0^x;bits=BITS)`, same mass, same source, same numeric-beta construction as original L1/L2. ONE call only to original author `magic(m,beta;hadrons_output_flag=true)`, at original default `num_points=10000`, default original ODE solver tolerances; no 100×100 and no second sample until independently reviewed. Julia 1.12.3 and frozen Mech-S6 dependencies as already validated, original author source commit + blob pin identical, write-only diagnostics in separate `research/mech-s9/2026-11-13` + new Actions artifact; no original equations modified, no bot `git push`.

## Frozen test observables, decisions and uncertainties

For all 10,000 original output indices construct from native returned arrays:
1. `t_seconds=t_list[i]/NU.s`, `T_MeV=EUval(MeV,from_rho_to_T(rho_SM_list[i]))`, `X_n`, `n_PBH` positive/zero and mass; original scalar `Yp_author=res[7]`, `Yp_corrected_2X_T0` only if target temperature in original trajectory, no new bound.
2. Six **RAW** `ell_h=log(EUval(EU,raw_h[i]))` in *original* dimensionless energy-unit convention EU=GeV; no early Float64 conversion before `log`, so very tiny populations remain visible. Define `floor_h[i]=(ell_h<-100)`, and used log `max(ell_h,-100)`. The originally used RHS contribution differs by `Δn_h=(exp(max(ell_h,-100))-exp(ell_h))*EU(1,3)`; compute in original units.
3. PBH evaporation event sample bracket: first `nPBH[i]==0`, preceding last source-active sample, time and temperature; if no event in returned trajectory, report not observed, no fabricated event. For T1=0.099688851247... MeV and T0=original T_nuc=0.07818527068831994 MeV, locate nearest source output sample; publish `ΔT` discrepancy rather than call it exact at T*. Also publish first/postev/final floor flags and extrema separately.
4. Per hadron summary: first whole-history floor index, first POSTEV floor index, postev sample fraction floor-active, terminal raw log, min/max postev raw log, first onset bracket and T/T0 relation; distinguish SOURCE-active phase from postev.
5. On-solution instantaneous signed floor forcing in neutron equation from the SIX original source channel coefficients at SOURCE-SAMPLED T1, T0 and final snapshot: `Δ(dX/dt)_floor=Σ_h C_h(X,T)*(n_eff,h - n_raw,h)`, using exact original source `σv` functions with original units, expressed in `s^-1` by `NU.s`. This compares RHS on the SAME original trajectory; it is **not** the integrated difference between distinct clamped-vs-unclamped trajectories and not physical helium error.
6. Publish full source-raw diagnostic trace CSV (temperature/time, six `ell_h`, floor flags), concise JSON/summary, original source/package identities, stdlib SHA256 and artifact checksum. Output each sampled scientific quantity in `Float64` after high-precision calculation; initial source results `ArbFloat`. Do not silently classify tiny underflow as exactly zero before log.

Predeclared reporting gates:
- `SOURCE_PIN_PASS`: author main blob `b368ba55...`, julia env and script SHA locked.
- `NATIVE_SINGLE_CALL_PASS`: source function returns exactly 13 fields and 10k points, finite temperatures / times, no numeric error.
- `RAW_FLOOR_MEASURED`: for each species, explicitly report `TRUE/FALSE/NO_EVENT` at near-T1, near-T0, postev segment and terminal; do not assume prior LT8 synthetic examples imply native occurrence.
- `NO_FLOOR_ENDPOINT_SUFF`: if all six RAW terminal `ell_h>=-100`, **and only conditional on** postev nonnegative original decay/annihilation, infer LT8/AUD2's existing conditional no-floor terminal certificate; otherwise HOLD and report floor-active raw values.
- `PHYSICAL_IMPORTANCE_HOLD`: even if source raw floor is active, without a source-validated counterfactual solution and E4 spectra, no PBH/BBN physical bound or claim that source impact is significant.

Stopping conditions: only one native source solve; failures preserved as scientific engineering negatives, do not rerun until fixed wrapper bug is diagnosed (no iterative tuning toward desired result), no root search, no new external reviewer task.
