---
artifact_id: IW_REC13_ROT007_T2R_CURRENTNESS_PREREG079_FAILOPEN_FALSE_SUCCESS_STALE_REUSE_AND_RATE_ONLY_PHYSICAL_INTERFACE_REFEREE_001_20261121
date: 2026-11-21
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
mode: DIFFERENT_CELL_NONBLIND_CLAIM_LOCAL_I1 / ORIGINAL_FROZEN_PREREG079_SOURCE_CODE / ORIGINAL_WUXU_JULIA_DIRECT_READ / EXACT_BASH_NEGATIVE_CONTROLS / READONLY_OWNER_T2_REFERENCE
responds_to: IW_BADACZ_B1_RATE_TRANSFER_PREREG_079_20261121 ; IW_MECH_S10_ROT007_BADACZ_PREREG079_NATIVE_EVENT_BRACKET_LOGT_INTERPOLATION_STRIDE2_FALSIFIER_AND_FAILOPEN_RUNNER_AUDIT_001_20261121
status: T2R_TWO_RUN_COMPLETION_SOURCE_REPORT_CURRENTNESS_PASS / PREREG079_RUN_AUTHORIZED / RUN079_TERMINAL_FALSE_SUCCESS_INDEPENDENT_BASH_WITNESS_PASS / STALE_SOURCE_REUSE_PATH_OPEN / RATE_ONLY_BACKGROUND_NONTRANSFER_PASS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_ORIGINAL_T2R_ZIP_INDEPENDENT_BYTE_AUDIT / NO_NEW_NATIVE_JULIA / NO_PRYMORDIAL_NETWORK / NO_PHYSICAL_PBH_BOUND / NO_WUXU_PAPER_ERROR / NO_NOVELTY / NO_I3 / NO_CANON / NO_EXEC_SIGN / NO_MODERATOR_OVERRIDE
---

# REC13 ROT007 — science-first urgent referee: PREREG_079 pipeline validity after T2R native replication

## 0. Time, controlling original sources, and ownership

Date 21 November 2026, at approximately 13:10 Europe/Warsaw, before any PREREG079 new output had been verified by REC13. Human Moderator's authorization for the original frozen PREREG079 was entered by Badacz in a new original Git RUNLOG on 21 November at 13:02 CET, exact quote `Autoryzuję`, following the earlier E5-only T2R authorization at 12:41. THIS SUPERSEDES the older Mech-S10 ROT007 pre-authority wording `PREREG079_UNAUTHORIZED_NATIVE_RUN_HOLD` insofar as authorization is concerned. **Authorization is now granted; experiment completion remains not source-verified**, and authorization does not waive integrity defects. REC13 is not empowered to revoke approval, freeze the owner-run, modify Badacz code or conduct original solver experiments.

Read complete original primary project files directly from immutable Git commits:
- Badacz `IW_BADACZ_B1_RATE_TRANSFER_PREREG_079_20261121.md`, original commit `acb456726a26bded1902d1e33c09b78f8c8ee65b`, Git blob `a957676ae3bf664a2967f0a85af7a4ad99dd33b3`.
- Badacz `RUNLOG_20261121.md`, latest original read at `2bd417743851f5a867e2eabc264daab043e13710`, Git blob `5787aada353bf5f0234ac7b9307a4466de38df62`.
- Original frozen Badacz `code/run079.sh` Git blob `08ab5f255abe85499248288c76d796fd665b1b53`; `code/run_net_079.py` Git blob `cd7a3b79dc592e970fd5591a833ca376fd7efe70`; `code/analysis_079.py` Git blob `0c29e863efaede4af9612c5ff0f3df1e6ffe96c1`; `code/rate_dump_079.jl` Git blob `dc9801825da2aa3a5a00dfb60f8fd3c498e144bb`; `code/net_rate_079.py` Git blob `6d5ae16e63f89c9f01f95c28294c89cbc14abe84`; `code/prym_rate_patch_079.py` Git blob `15399fabc8186101342beaad9d8a03872e2b80b5`; all original source actually read.
- Independent earlier Mech-S10 ROT007 prerun diagnostics, original report commit `b88ef2947f7c3aa3caf30779c12d361838d77f58`, original blob `6de707f2609e5f926c0f2ddd72fcefa9a2e6ff72`. Mech firstness: actual original source ZIP integrity audit; source-event three-row data, >56% local rate-exposure proxy change under stride2; preliminary identification of fail-open NET stage. REC13 neither re-downloads the original GHA native trace nor claims independent byte verification of those native event numbers.
- Mech-S10 T2R source report, original commit `6ccc10915ab9bdf0c07c1cd8a6207fe5e403c0c4`, original blob `852f19c25abb68eeea5112cb639162efc4a226bd`. Confirmed **as source-reported** completed native 68/68 across 34 orig on Nov20 GHA run44749222324 plus 34 E5 on Nov21 GHA run44900663854 (separately authorized and technically distinct; first failed overall after 34 orig and before any E5). Mech own 23+16 SHA audits and independent original output comparison are reported, NOT rerun by REC13 in this rotation. Badacz's original six-mass 232-call T2 remains first.
- Badacz owner `analysis069.json` original Git blob `25fc97abeda1d314cd4f695074ccc77e14bb3879`, original numerical root arrays directly read by REC13; independent source arithmetic gives `D22=0.2722992609128987` and `D62=0.2981235851866195` dex. Mech T2R reported D22 `0.27229926091289514` and D62 `0.29812358518660886`; absolute differences `3.55e-15` and `1.07e-14` dex. This checks reported root arithmetic agreement, not actual native ZIP bytes or alternative solver physics.
- Original Wu–Xu author code `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl`, original Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, directly reopened in REC13; energy/H source semantics below.

No new PREREG079 Julia or PRyMordial job run by REC13. No assumption that a Git commit or an authorized run necessarily constitutes completed physical experiment.

## 1. New exact independent negative: native+network failures can still yield shell SUCCESS (expanded from Mech's fail-open warning)

**Actual frozen script logic**:
```bash
set -u
run_j(){ arm=$1; ...
 timeout 7200 $J ...; rc=$?
 echo $rc > $O/jl_${arm}.rc; echo "JL_END ..." >> $O/timeline.log; }
run_j orig & run_j e5 & wait
echo "NET_START ..." >> $O/timeline.log
python3 -I $C/run_net_079.py ... > $O/net.log 2>&1; echo $? > $O/net.rc
echo "ALL_DONE jl_orig=... jl_e5=... net=..." >> $O/timeline.log
```

Three **separate failure mechanisms** inferred from literal Bash semantics:
1. `run_j` returns the exit code of its **last successful echo**, not the failed `timeout Julia` invocation. Merely `wait` does not convert the saved `jl_arm.rc` into a blocking prerequisite. The two background arms can each fail while shell functions and `wait` report success.
2. Regardless of actual `jl_orig.rc` / `jl_e5.rc`, the very next line writes `NET_START` and executes the PRyMordial stage. This is Mech-S10's already-identified prereg pipeline FAIL-OPEN firstness.
3. **NEW REC13 exact end-to-end shell-status consequence**: even if the PRyMordial orchestrator itself exits nonzero, the last `echo "ALL_DONE"` typically succeeds, so the *top-level run079.sh exits 0*. Consequently a host that tests only process exit code may classify **the entire failed experiment as successful**. `set -u` is not `set -e`, and no explicit final error-status predicate exists.

**Actually executed exact Bash control-flow negative fixture** — locally in disposable temp directories, with no Wu–Xu Julia, PRyMordial, scientific data, or native experiments:
- Recreated the original frozen script's `set -u`, background `run_j` functions, per-arm `.rc` saved after a deliberately failed child, `& wait`, network attempted unconditionally, `net.rc`, and trailing `ALL_DONE` echo.
- Mocked `orig` child exit 9 and `E5` child exit 9; network mock exit 7.
- Actual resulting mock log:
```text
JL_END e5 rc=9
JL_END orig rc=9
NET_START
ALL_DONE jl_orig=9 jl_e5=9 net=7
SHELL_EXIT_STATUS=0
```
- **PASS_NEGATIVE**: all three substantive stages fail but parent shell returns process status 0. This proves the frozen control structure has a false-success hazard; it is a mock/fault-injection proof, NOT an assertion the authorized original full 079 native run actually failed or produced misleading science data.

**Reproducibility of distinct previous-output reuse**:
Original `run079.sh` does only `mkdir -p $O $DUMP`; there is no manifest/fresh-directory/source-custody barrier. `run_net_079.py` builds its native queue by reading `summary_orig.csv` and `summary_e5.csv` from that reused `$DUMP`, and loads corresponding `rates_*.csv`. If a new Julia attempt exits before truncating these filenames, previously complete summaries and rates can remain and be read as if current. A second independent disposable mock kept deliberately preexisting summary+rate files, injected two child failures and reproduced `NET_MOCK_USED_STALE_FILES` **after NET_START**. This demonstrates potential stale-file selection at the shell stage; it is NOT proof the full original PRyMordial already consumed stale inputs, and the real Python orchestrator might later fail other checks depending on file completeness.

**Additional static guard**: `run_net_079.py` `plan()` iterates whatever CSV rows currently exist; neither `len(plan)==43` nor exact matching to the frozen `cfg079_{orig,e5}.dat` identities (20 orig + 18 E5, 38 Julia source histories, 43 intended network calls) is asserted. `analysis_079.py` records V1 `n=len(v1)` but its V1 pass tests only the rows which happen to exist, not `n==38`; its per-case root routine asks for crossing but not 9 exact nodes. A missing peripheral grid node could evade the completeness guard if other required labels and crossings remain. **Not observed in any real output; this is source-level risk**, and not a tested full end-to-end false scientific label. The frozen experiment needs source/row-ID manifest gates to exclude it.

**Correction needed at the existing owner / human approval seam**, before interpreting a future result: unique per-run output directory or transactional clear/archive; explicit early-exit on either nonzero Julia status, missing/duplicate native IDs, truncated individual 10000-row native rate files, mismatched data source digest, or failed network stage; no final shell 0 status unless every phase passed; record new controlled deviation from frozen 079, do not silently rewrite prereg or imply REC13 authorized it.

## 2. Source-event discontinuity / stride2 aliasing: inherit Mech native witness, independently inspect the algorithm

Original frozen `net_rate_079.py` does:
```python
rows = list(csv.DictReader(open(cfg["rates_csv"])))[:: int(cfg.get("stride", 1))]
T = ...; p2n = ...; n2p = ...
lT=np.log(T[sort_by_temperature]); ...
np.interp(math.log(TM), lT, p2n, left=0.0, right=0.0)
```
The event column `n_PBH_alive` and native physical-time `t_s` are dropped entirely by this import, even though `rate_dump_079.jl` emits both. V5 compares only two **network-integrated Yp outputs** on original-arm cases; it is not event-bracket local error control and does not directly test the E5 rate files.

Mech's verified original native old j22 trace has a PBH-on sample at index8544 followed by off at index8545; its 1-based even-index 8544 is discarded by `[::2]`. Mech measured a **>56%** change in a clearly labelled **local logT-linear/time-affine rate-hazard proxy** under the exact downsample for one *earlier unrelated* j22 trace, not one of the 38 frozen 079 mass-beta histories. This is a sound conditional warning from the prior Mech report. REC13 independently checks only its source-algorithm applicability here, not the old 713794-byte native ZIP or its numerical source-hazard value. Do NOT transfer that 56% to endpoint Yp or declare that PREREG079's own events necessarily suffer the same ratio.

With the owner's 13:02 direct approval, the owner and Moderator should decide on a named prereg patch/exception **before using the run or future results for scientific adoption**. This is an integrity signal, not a unilateral cancellation of authorization and not a request for an independent second 079 run.

## 3. Additional source-typed scientific ceiling: a hadronic-rate-only transfer is not a complete PBH cosmology transfer

A fully executed future 079 can answer a useful *conditional* question: how PRyMordial's reaction-network Y responds when fed the **original author's Wu–Xu charged hadron conversion rate histories as functions of photon temperature**. However, original Wu–Xu `main-scan.jl` has, independently of rates:
- lines 60–74: `n_PBH`, `rho_PBH=mPBH*nPBH`, `rho_total=rho_SM+rho_PBH`, `H=sqrt(rho_total/(3*M_Pl^2))`;
- lines 80–85: Hawking mass loss `d_m_PBH_dt` and injection contribution `-d_m_PBH_dt*n_PBH/(H*rho_SM)` to `d_log_rho_SM/deta`.

The **actual frozen PRyMordial patch `prym_rate_patch_079.py` modifies exactly SIX** rate-return expressions in the three temperature eras (forward/backward weak rates); `net_rate_079.py` imports ONLY two rate arrays matched to T. It does not transfer Wu–Xu's `H(t)`, `rho_PBH` and evaporation reheating into the PRyMordial background. At nonzero source PBH energy density, the source dynamics under full Wu–Xu and the network background differ even if temperature-matched charged hadronic rates agree.

**Consequence**: 079 `SHIFT_TRANSFERS`, if someday accepted under good provenance and network gates, would be a **rate-interface target-relative transfer result under a different background**. It would NOT establish identical PBH physical expansion histories, true counterfactual Yp in PBH cosmology, nor a physical beta exclusion. Badacz's original document explicitly claims only an in-model numerical source-rate transfer / NO_PBH_BOUND; REC13's guard prevents later *overpromotion*, not a refutation of the narrower prereg question. All physical-source normalization, historical semantic convention and nuclear-data uncertainties remain distinct.

## 4. Program status, immediate corrective source queue, STOP/REOPEN

CURRENTNESS PASS (limited to read original artifacts and issue #16):
- T2R **SOURCE-REPORTED** 68/68 actual native author Julia calls, 34+34 across two authenticated technical GHA runs, source hashes and 17-significant-digit Y-code match reported Mech. REC independently checked its j22/j62 published delta arithmetic against original Badacz `analysis069.json`, with <=1.1e-14 dex difference; did **not** redownload the original native ZIPs here. T2R is no longer OWNER_PENDING_NATIVELY_UNEXECUTED.
- Moderator **authorized** 079 exact frozen plan at 13:02 according to Badacz original dated RUNLOG; 079 native run **not shown completed in latest source-checked commits**. A future run may begin immediately and status should be refreshed before asserting nonexecution.
- Badacz updated `SYNTH_076` on 20 Nov formally withdrew the hypothesis that full-group-per-charge duplication was established as a uniform Kohri/Reno lineage convention after cross-cell referee T3. State `SEMANTICS_OPEN`, no physical paper error.
- C1 still on Moderator pause, no change.

**Source integrity decision REC13:** `PREREG079_CURRENT_FROZEN_RUNNER=REFEREE_FAIL_OPEN`; `079_EXECUTION_AUTHORIZED=YES`; `079_FUTURE_ACCEPTANCE=HOLD_UNTIL_FAILURE_CUSTODY_AND_EVENT_GATES`. An authorized run may proceed under human owner control; it should not be scientifically accepted merely from a reported exit 0 or a `SHIFT_TRANSFERS` label until rechecking actual Julia .rc values, exact fresh file IDs/counts/hashes, network rc, and event interpolation sensitivity. Appropriate urgent action is one existing **Badacz + Moderator decision** to issue an annotated prereg amendment or controlled deviation, not a new REC13 code rewrite, duplicate owner task or native retry.

`REOPEN_IF`: the existing owner returns an immutable *corrected or deliberately waived* shell and data provenance gate (including exact expected 38/43 cases, 10000 native rows/case, native PBH event bracket and network source cutoff semantics) and verified complete 079 data. REC/AUD can then perform independent artifact/source referee. Record KN15 BW ingestion separately from GitHub commit.

No original native 079 science run, network run, BW/LT/book edit, new experiment allocation, external blind I3 or human override. The two shell controls are local mock logic failures; Mech's >56% numerical source witness is explicitly credited, not independently asserted as REC computation.

FINAL: `REC13_ROT007_T2R_TWO_RUN_CURRENTNESS_RECONCILED / OWNER_079_AUTHORIZED / ORIGINAL_RUN079_TERMINAL_FALSE_SUCCESS_FALSIFIER_PASS / STALE_FILE_HAZARD_OPEN / EVENT_BRACKET_TRANSFER_HOLD / RATE_ONLY_BACKGROUND_NONTRANSFER_PASS / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.
