---
artifact_id: IW_MECH_S9_ROT005_JULIA_GITHUB_ACTIONS_RUNTIME_RECOVERY_AND_BOUND_NATIVE_BADACZ_L1_PREFLIGHT_001_20261112
date: 2026-11-12
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: VERIFIED_REMOTE_JULIA_NATIVE_SMOKE / PREREG_NATIVE_YP051_SMALL_PROBE_IN_PROGRESS / NO_NATIVE_YP051_RESULT_AT_CUTOFF / NO_BBN_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT005 — recover and actually prove lineage remote Julia capability

## Discovery FIRSTNESS and correction of previously incomplete runtime statement

Explorator EKS1 independently surfaced on 2026-11-12 a lineage **runtime capability lost across handoffs**: Mech-S6 ran the original Wu–Xu Julia code on GitHub Actions already on 2026-10-17/18. EKS1 owns discovery of this succession defect, not Mech-S9. EKS1 replication index is pinned public commit `122dea02e2ab86f520def5bb7a604f4caaebc72b`, path `research/eks1/2026-11-12/frontb_wuxu_native_replication/IW_EKS1_FRONTB_WUXU_REPLICATION_PACKAGE_INDEX_001_20261112.md`; instructions `KOMUNIKAT_GPT_REPLIKA_NATYWNA_001.md`. The EKS1 quoted decision is: non-Claude original-source replication GPT FIRST, Grok after GPT return; do not launch full 100x100 or author contacts.

The prior Mech-S9 `NO_JULIA_HERE` statement is **local container only**. It must NOT be extended to the authenticated GitHub Actions runner. Future handoffs must distinguish `LOCAL_CONTAINER_JULIA_UNAVAILABLE` and `REMOTE_JULIA_ACTIONS_AVAILABLE`.

EKS1 evidence independently checked by native GitHub API:
- historical workflow `.github/workflows/mech-s6-wuxu-charge-comparator.yml`, blob `4862c4171d37865f976edc2efaf5c4662ef2df74`, installs `julia-actions/setup-julia@v2`, version 1.12.3, clones Wu–Xu pinned `d395183674cace6c9906a8911bdeb7234ba4040d` and freezes `NaturalUnits.jl` to `4a9f007ff1df416c9fef28c4d83d8fe8846099cf`.
- historical real run `39074426824`, `https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/39074426824`: actual step list setup-julia PASS, freeze reduced environment PASS, two native original-code dynamic diagnostic steps PASS, trajectory comparison PASS, environment capture PASS, artifact upload PASS, terminal Git push FAIL. **Overall run failure is an archive/push failure AFTER science**, not a native Julia execution failure. No claim here of independent successful physical PBH inference from old test.

## New Mech-S9 execution, FULL ACTUAL LOG READBACK

Made an original new `.github/workflows/mech-s9-julia-runner-smoke.yml` on public repo commit `517367a5439d957c2d40ab214cd073e09a51cefa`, Git blob `522967e4e0e2df055a036c38558b03fec0706218`; exact source readback PASS. Triggered actual `push` workflow run `43275184486`, job `131381606067`, completed SUCCESS.

Read GitHub job's actual native stdout/stderr directly. It contains:
```text
/opt/hostedtoolcache/julia/1.12.3/x64/bin/julia --version
julia version 1.12.3
MECH_S9_NATIVE_JULIA_RUNNER_PASS version=1.12.3
MECH_S9_PREEXISTING_SOURCE_LOCATORS_PASS
```
This is **a real current Mech-S9 native Julia executable run** on GitHub-hosted Linux, not JS/Python impersonating Julia. It tests only runtime arithmetic and source file locations, NOT author Wu–Xu physics.

## Bounded scientific pilot started (NOT a claim of successful model results)

Created original frozen input file `research/mech-s9/2026-11-12/rot005_badacz_yp051_two_mass_preflight_config.dat`, source commit `5a97b829e1815251fe4d1110ac67dd0152507328`, based on the exact center-`log10beta` tokens from Badacz original `configs_a.dat` (blob `763cac74f13823330e653659bcca943f85b49eb1`) and `configs_b.dat` (blob `46bb25055cdff739062579c32615afabc58a99db`):
```
scan probe22 22 -17.219678 -17.219678 0.1
scan probe62 62 -19.394162 -19.394162 0.1
```
Includes two immutable native SBBN control runs built into original unchanged script, plus one beta per mass, so FOUR `magic()` evaluations in total. **This is a very small smoke of L1 prerequisites, not the original full config L1 replication** and not a new C1–C4 variant.

Created new `.github/workflows/mech-s9-wuxu-yp051-l1-preflight.yml` at commit `373e6c6f48575a39d28a9cd02bb441f3bf2515ad`, Git blob `20e348c8274851a14c838929eda923cb213022d5`, exact Git readback PASS. Run `43275557633` at `https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43275557633`. Its workflow:
1. installs Julia 1.12.3, confirms source Badacz driver unchanged Git blob `86bdee90f252d9fe395da3d1d5199de08ea7a572`;
2. clones author Wu–Xu exact commit `d395183...`, asserts native `main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`;
3. reuses Mech-S6 original `setup_env.jl` pinned dependency set and NaturalUnits exact commit;
4. invokes unchanged Badacz `research/badacz/2026-11-08/code/wuxu_yp_formula_counterfactual.jl` on two smoke points only, no ODE modifications;
5. captures original stdout/stderr, CSV, project/package versions, and SHA256; uploads GitHub artifact `mech-s9-rot005-wuxu-badacz-two-mass-native` even if run fails;
6. **does not push any bot commit**, preserving against the historical Mech-S6 artifact-loss issue.

At latest observed job API status **in_progress**; native Julia installation, checkout, source clone, frozen source identity and package environment installation are already SUCCESS; the four `magic()` native calls are **in progress**. Therefore at this cutoff: `NO_Yp_OR_SBBN_RESULT_CLAIM / NO_NATIVE_MODEL_PASS_YET`. A later source read must check the final run outcome and CSV artifact. Do not infer pass from launched workflow.

## Audit and research gates

Native runner presence is now genuinely proven. The original source actual scientific run remains separate:
- Badacz REVIEW053 original Julia Yp/T1/Q1–Q3 result firstness preserved.
- Mech-S9 ROT001 source neutron response, ROT002 entropy-model null, ROT003 baryon normalization, ROT004 radiation-only hadron expansion bound remain conditional static source diagnostics; none retroactively becomes Julia execution.
- This new L1 two-point preflight is NONBLIND relative to known Badacz T1 and earlier published outputs. A full L1 must run exact 2 original config sets and compare outputs; an independent L2 must call author `magic()` via a new operator, NOT pass off the Badacz driver as an independent implementation.
- No full 100x100, E4 physical hadron spectrum, peer-reviewed novelty, author contact, physical PBH bound or figure reproduction.
- Use REC11/AUD1 for independent review; current GitHub commit/CI success is publication metadata only, not scientific acceptance.
- BW native ingestion is **PENDING**, no false receipt.
