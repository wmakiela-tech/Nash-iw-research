---
artifact_id: IW_REC11_ROT026_MECHS9_ROT007_L2_PATH_FAILURE_SOURCE_REFEREE_001_20261112
cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-12
visibility: PUBLIC
source_type: NONBLIND_INDEPENDENT_ACTUAL_GITHUB_ACTIONS_FAILURE_ARTIFACT_REFEREE
source_firstness: MECH_S9_ROT007_FIRST_L2_OPERATOR; MECH_S9_ROT008_FIRST_OWNER_INCIDENT_DIAGNOSIS_AND_FIXED_RETRY
classification: PASS_ORIGINAL_ARCHIVE_PROVENANCE / FAIL_SOURCE_INCLUDE_PATH_LINE26 / NO_L2_SCIENCE_OUTPUT / NO_PHYSICS_INFERENCE
owner_ack: PENDING
bw_ingest: UNVERIFIED
claim_ceiling: NO_L2_PASS / NO_L2_NUMERICAL_COMPARISON / NO_JCAP_FIG5_ID / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC11 ROT026 — Source-authenticated failure of Mech-S9 native L2: Julia relative `include` path at line 26

## 1. Original source, firstness and currentness

Mech-S9 ROT007 **FIRST** authored the independent GPT observation/root Julia L2 driver and triggered its original 10D Wu–Xu source-native run. Its Slack dispatch at 2026-11-12 22:18:58 CET reported L2 **RUNNING**, with no result yet. REC11 independently checked the current direct GitHub Actions REST run 43308493869 and job 131497974547; the job finished **FAILURE** at `2026-11-12T21:26:01Z` (22:26 CET). This supersedes the owner's earlier ROT007 running status; it does **not** invalidate Mech-S9 ROT006 and REC11 ROT025 **FULL53 L1 PASS**. **Currentness reconciliation:** Mech-S9 independently diagnosed the SAME loader issue in its own ROT008 report at **22:28:37 CET**, before this REC11 report, and already committed and triggered its one-line repair. REC11 independently verifies the original failure, with firstness of diagnosis/repair retained by Mech-S9 ROT008. The new repaired run was still RUNNING at REC11 source readback; the failed original run remains FAILED.

- [Run 43308493869](https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43308493869), commit `03e5906775ee08f76dadf200703d5580f1fe1bf5`.
- [Independent L2 driver, pinned](https://github.com/wmakiela-tech/Nash-iw-research/blob/2d1adbbe33925190e203931412fb238adc98a1ff/research/mech-s9/2026-11-12/mech_s9_rot007_independent_native_L2.jl), original Git blob `f44cb0babdb931e936e04883d3a1e75f7e1e273b`; directly read by GitHub connector.
- Original Wu–Xu author `Fenyutanchan/Primordial-Black-Hole` source commit `d395183674cace6c9906a8911bdeb7234ba4040d`; `main-scan.jl` original blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`; **original** `main-scan-parameters.jl` exists and was directly read, blob `53faee65beda383348580c28d0424188da69b660`. This is a relative-include resolution error **not** a missing parameter file in author Git.
- Author's historic Badacz REVIEW053 Julia driver original Git blob `86bdee90f252d9fe395da3d1d5199de08ea7a572` correctly uses `include(joinpath(src_dir, "main-scan-parameters.jl"))` and was actually used for successful L1. This comparison is a prior-work recognition, **not** a claim that REC invented the fix.

GitHub run API itself reports status `completed`, conclusion `failure`. Run steps freezing operator and source pins, source cloning, Julia1.12.3 installation and pinned dependency setup all **SUCCESS**; `Independent GPT observation operator and native adaptive root searches` **FAILURE**, post-run numeric comparator **SKIPPED**, artifact hashing/upload **SUCCESS**.

## 2. Actual immutable failed archive — forensics

REC11 used the GitHub connector to **download the actual source-native Actions artifact ZIP**, ID **13985551662** (10 members, 14,810 bytes). ZIP SHA-256 exactly equals the **provider's registered artifact digest**:

`e997107d25b49556242f3bc63335fa9e1228ee251ccc8372ac4055ce02f047c6`

[Original immutable artifact](https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43308493869/artifacts/13985551662).

CRC **PASS**, interior `ARTIFACT_SHA256SUMS` contains 9 entries, verified **9/9 PASS**, no self-entry. `AUTHOR_COMMIT` equals frozen Wu–Xu commit; `REPO_COMMIT` equals run head. Julia version file states **1.12.3**. Exact file status:
- `NATIVE_L2_STDOUT`: 0 bytes.
- `NATIVE_L2_STDERR`: 17,349 bytes, containing package precompilation then **exact fatal**:
  `ERROR: LoadError: SystemError: opening file "/home/runner/work/Nash-iw-research/Nash-iw-research/research/mech-s9/2026-11-12/main-scan-parameters.jl": No such file or directory`
- Stack trace: `mech_s9_rot007_independent_native_L2.jl:26`, within `cd` block at line 24.
- `independent_L2_raw_calls.csv`: **ABSENT**.
- `independent_L2_roots.csv`: **ABSENT**.
- `independent_L2_summary.txt`: **ABSENT**.

Therefore **no SBBN calibration was completed and not one of the planned PBH `magic()` calls or six adaptive L2 roots was executed**. Success of dependency compilation and archive upload does not count as L2. Evidence is native exception plus zero stdout/absent outputs, not a guessed interpretation of GitHub's green upload.

## 3. P0 deterministic loader defect and minimal repair

The original ROT007 driver at lines 23–27:

```julia
try
    cd(author_dir) do
        include(prefix_path)
        include("main-scan-parameters.jl")  # FAIL: source-script-relative resolution
    end
finally
    isfile(prefix_path) && rm(prefix_path)
end
```

Julia's `include` in this source context resolves a relative path against the **including script's path**, not the temporary process `pwd` selected via `cd`. The original author parameter file is under `author_dir`, but the loader tries to open it alongside Mech-S9's script. It failed at exactly that path and line in the **original actual Julia stdout/stderr**.

**Minimal source patch, independently verified and already IMPLEMENTED by owner Mech-S9 ROT008 (NOT applied by REC11):**

```julia
include(joinpath(author_dir, "main-scan-parameters.jl"))
```

Mech-S9 ROT008 independently filed this same one-line correction in its **separate** new Julia file `mech_s9_rot008_independent_native_L2_FIXED_INCLUDE.jl`, pinned commit `3d69cfc72fb31fe03e6719f2ea835830ffbb880c`, Git blob `5ca59bd911bbd12e4bb2b3deca9fbd3fa4ed0506`. REC11 fetched **BOTH** old and new original scripts and independently compared nonempty noncomment lines: **153/153 unchanged apart from precisely the one `include` replacement**, no other executable-line change. New owner workflow commit `9e2ee03c342a56b6f57efb2e69292a829a0be2d4`, run [43310359194](https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43310359194) was **IN PROGRESS** when checked, with frozen source and package installation PASS, scientific root step IN PROGRESS. This currentness does **not** give L2 numerical PASS.

Optional fail-closed guard before the `try`: `isfile(joinpath(author_dir, "main-scan-parameters.jl")) || error("FROZEN_AUTHOR_PARAMETERS_MISSING")`. The existing `include(prefix_path)` is already absolute. This is a source-layout repair, not a physical-model modification. The owner has already made that versioned change and initiated one bounded rerun. Preserve original failed artifact and owner immutable report; REC11 makes **no** bot changes or runtime requests.

## 4. Secondary numerical science guards for owner fixed retry (not executed by REC11)

Even after the owner's loader repair, the L2 claim still requires six **actually completed independent** native roots with negative/positive residual brackets, record of all beta calls and the claimed independent interpolation geometry. ROT007 uses the same **original Wu–Xu `magic()` ODE**, and changes the observation/interpolation and search algorithm relative to Badacz; it is an **independent observation/root operator**, *not* an independent implementation of the physical ODE model. Source code uses manual Float64 linear interpolation in `q=Q/T`, fixed coarse anchors and 8 bisection steps per root. `native_observation` checks reconstructed `Ycode` only to tolerance `1e-8`, distinct from the stricter 53-point decimal-source agreement achieved in ROT025.

At j62, historical Badacz/REC11 ROT025 V2 **linear-data root** was around `−19.303610678`, just `0.00361` dex below the upper coarse anchor `−19.30`. This is a *pre-run design fragility observation*, not proof of an L2 bracketing failure: the source original ODE may shift the actual root relative to 53-point interpolation. Require actual sign bracket after the repaired owner run completes; do not silently widen admissible physics intervals to force a result.

The original SBBN comparison remains logically separate: `X0s(j22)=0.109037947009` and `X0s(j62)=0.109032060693`, discrepancy **5.886316e−6** exceeding the original `1e−6` equality gate. L1 replicated both; no independent L2 prelaunch attempt can erase that. Corrected physical helium `Yp=2X(T1)` vs author `Ycode=2X(T0)/(1-X(T0))`, historic JCAP model producer ID, E4 hadron and actual PBH exclusions remain held.

AUD1 ROT044 separately FIRST discovered fail-open comparison logic (`exact=false` can still exit zero). Treat numeric comparison and science pass as **explicitly fail-closed** once an actual successful rerun produces source values. REC11 does not reassign AUD1 firstness.

## 5. Independent executable verifier and reproducibility

REC11 **actually executed** the standalone Python3-stdlib postmortem 
`verify_rec11_rot026_l2_failure.py` on the exact original downloaded 14,810-byte ZIP. It tests provider SHA-256; zip member identity and CRC; *all* 9 manifest hashes; original author/run commits; exact source exception string and script line; zero stdout; absence of both numeric CSVs. **PASS**.

Independent negative-control code `verify_rec11_rot026_negative_controls.py` **actually executed**: (1) one-byte corrupted provider archive => REJECT; (2) valid ZIP with altered stderr and stale manifest => REJECT; (3) valid ZIP missing stderr => REJECT. All three rejected, not fail-open.

Scientific type: genuine original executed Julia *failure* artifact independently inspected; **the L2 operator was NOT successfully run** in REC11 or the owner Actions run. The Python verifier replays the forensic proof, NOT a scientific new 10D Julia trajectory. The original author `main-scan-parameters.jl` was separately authenticated by direct GitHub source read and was not smuggled into the archived original failed ZIP.

Final: **`REC11_ROT026_COMPLETE / FAIL_MECH_S9_ROT007_INDEPENDENT_L2_SOURCE_LOADER / PASS_FAILURE_CUSTODY_9_OF_9 / OWNER_ROT008_INCLUDE_PATH_REPAIR_VERIFIED_STATIC / OWNER_FIXED_RETRY_RUNNING / HOLD_L2_SCIENCE / KEEP_L1_53_PASS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`**.

RETURN_ID: `IW_REC11_ROT026_MECHS9_ROT007_L2_PATH_FAILURE_SOURCE_REFEREE_001_20261112`.
