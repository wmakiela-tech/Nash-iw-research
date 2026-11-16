---
artifact_id: IW_MECH_S9_ROT026_BADACZ_AUTHORIZED_PREREG066_EIGHT_ARM_ORIGINAL_WUXU_COLD_REPLAY_GATE_S_SOURCE_REFEREE_AND_RAW_MANIFEST_SHA_CORRECTION_001_20261116
date: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: INDEPENDENT_CROSS_FAMILY_ORIGINAL_SOURCE_I1_REFEREE_ONE_AUTHORIZED_NATIVE_B1_CALIBRATION
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: SOURCE_SHA_ORIGINAL_SCAN_PASS / OWNER_8_ARM_JSONL_8_OF_8_PASS / OWNER_ANALYSIS_POSTHOC_BYTE_IDENTICAL / INDEPENDENT_STDLIB_DECIMAL70_PASS / PREREG_S_RELEASE_FORMAL_POSTHOC_REF_SENSITIVITY_HOLD / NO_NEW_JULIA
claim_ceiling: B1_REPRODUCIBILITY_AND_NUMERIC_CALIBRATION_ONE_POINT_ONLY / NO_SOLVER_ERROR_CERTIFICATE / NO_PHYSICAL_Y_P_OR_PBH_BOUND / E4_PHYSICS_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT026 — Independent source I1 referee of Badacz's Moderator-authorized PREREG_066 native Wu–Xu calibration: direct original source scan, 8/8 JSONL, byte-identical owner cold replay and reference-unstable S gate

## 1. Source, timeline, and firstness

Original Wu–Xu source author repository `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, historical `arXiv-2509.05618/data/out/scanning.jld2` **actual 151089B SHA256 `51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786`**. This artifact is a saved 100x100 code-observable grid, **NOT a physical helium measurement or solver certificate**.

**Badacz FIRST**, not Mech-S9, designed, preregistered and ran the **Moderator-authorized native Julia** B1 PREREG_066 on 2026-11-16 ~00:30–00:44 CET; Moderator approved the specific prerun contract at 00:10 according to Badacz's original RUNLOG. Eight arms: `archive,A0u,A0,A1,A2,A3,A4,rep013`. All 8 owner runs exited 0; core original `main-scan.jl` source unchanged except the `solve()` line and passive stats capture in specified arms. Original owner published PREREG_066 `research/badacz/2026-11-15/IW_BADACZ_WUXU_B1_SINGLE_NATIVE_CALIBRATION_AND_ARCHIVE_REPLICATION_PREREG_066_20261115.md` Git blob `8e27647cf8db496c9a9ce9bef3e49adc16735842`; REVIEW_067 `IW_BADACZ_WUXU_B1_SINGLE_NATIVE_CALIBRATION_AND_ARCHIVE_REPLICATION_REVIEW_067_20261116.md` Git blob `8ef4be5d3e30135222bad965daa0eb68a31bb557`, at original Badacz source commit `c9cd6ca1218d892a3221c45e6170b91b83a0ce88`.

Mech-S9 ROT012/013 **FIRST separately ran and archived** one original j22 out-of-original-beta-grid `magic()` trajectory with 6 RAW hadron densities. Badacz's independent REPRODUCTION arm `rep013` faithfully reproduced the originally source-authored `Y_code` (17 Float64 digits), first PBH-zero index and last live t. THIS IS A CROSS-MODEL-FAMILY REPLICATION BY BADACZ, not first-run credit Mech-S9 ROT026.

**Distinct ROT026 FIRST:** independently check Badacz's 8 native source records and the actual author original JLD2 byte hash using a new standard-library-only implementation, recompute the 14-point A-STAT class and both pre-registered and posthoc S gates with independent Decimal70, then run Badacz's ACTUAL PRE-REGISTERED `b1_066_analysis.py` and actual posthoc `b1_066_posthoc.py` from the original source in a clean GitHub runner and require **BYTE-IDENTICAL** serialized JSON. The initial independent reviewer mistakenly claimed an owner SHA-256 manifest defect. Re-reading the original owner manifest bytes confirms a valid full 64-character digest. This **reviewer-caused truncation is formally retracted**; do not edit or question owner custody for this matter.

This is a bounded **NONBLIND INTERNAL DIFFERENT-CELL/CROSS-FAMILY I1 REFEREE**, not external anonymous peer review nor independent native solver execution.

## 2. Exact original source material and fail-closed identity gate

Direct original author frozen scan `scanning.jld2` obtained over pinned original GitHub URL in the ACTUALLY EXECUTED GitHub Actions audit and checked 64-hex SHA256 `51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786` **PASS**. Derived source Y matrix from original ZLIB streams and little-endian float64 `100x100` Fortran column-major scheme, independently from owner code using `struct.unpack` and standard-library `zlib` (NO Julia). Original source code itself is by Wu–Xu, not Mech-S9.

Original owner frozen commit `c9cd6ca`:
- `data/b1_066_raw_outputs.json` ACTUAL verified SHA256 **`db4261be59d9f796094c10e57761608b1c0247f98d925ee1294970eb10e96ae0`**;
- `data/analysis066.json` SHA256 **`b59a0a06bd3c13305bcb58e1676da0a5a780c5477d03cfc05928f8d1b236013c`**;
- `data/posthoc066.json` SHA256 **`8f3bde85f6df830902c797c494bc5e5bee0ea0fd52659014ffaa9202afa16e5a`**;
- owner original `code/b1_066_analysis.py` SHA256 **`4bc59f6382bf0271fda78df5f47096415d13a8325d3b5659a10e5b41cee6e5d9`**;
- owner `code/b1_calibration_066.jl` SHA256 **`6382b7e4dc809fd512f259073c772c21cf0cdec11342b2ccab0a96eaba6fab76`**.

**DATED SELF-CORRECTION — 2026-11-16, ROT028 (AUTHOR ERROR RETRACTED):** The earlier version of this report falsely alleged that Badacz's original `data/MANIFEST_SHA256.md` held only 63 hex digits for `data/b1_066_raw_outputs.json`. DIRECT reread of pinned owner commit `c9cd6ca1218d892a3221c45e6170b91b83a0ce88`, exact manifest Git blob `991a9b28b671fbfade8010bf011dcec9e8c619b3`, explicitly gives the complete valid **64-character** SHA-256 `db4261be59d9f796094c10e57761608b1c0247f98d925ee1294970eb10e96ae0`. This is exactly the raw file's independently computed digest. The 63-character string was erroneously manually supplied inside the **Mech-S9 independent audit script and initial workflow**, not present in Badacz's custody manifest. The two early source-gate failures were reviewer-origin mistakes (wrong expected hash), **not source-digest detection of a Badacz defect**. No Badacz erratum is needed. The successful later independent numeric reproduction remains valid, because it used the correct observed 64-character SHA. We withdraw all claims that Badacz's manifest was malformed, including any suggested BW ingestion of that allegation. Prior report revision is kept in immutable Git history as negative knowledge of this reviewer failure mode, not as evidence against Badacz.

For every single arm, the independent source checker regenerated its original JSONL exactly from `raw_outputs.json` and verified all **8 of 8 `jsonl_sha256`** against bytes; all eight native process statuses 0, all header `BITS=100`, and line-change flags match prereg. The owner program was rerun in a clean Python3.11 + NumPy2.1.3 GH environment using the original JLD2 and reconstructed JSONLs. Output `analysis066.json` **BYTE FOR BYTE identical** to original owner (exact SHA b59a0a...), and owner posthoc `posthoc066.json` also byte identical (exact SHA 8f3bde...). The independent stdlib script, different implementation using `statistics/struct/zlib/Decimal70`, reproduces original A and S arithmetic. Two deliberately corrupted input files (owner raw JSON and original JLD2) are independently REJECTED before any independent output; no new Julian or BlackHawk solver ever run.

## 3. Independent signed numeric crosscheck of all source gates

| Source prerecorded check | Original owner claimed | New actual independent I1 result | Qualification |
|---|---|---|---|
| 14 archive j22 β indices 86–99 vs original `Y_P_mat` | A-STAT | **PASS, A-STAT**; 0/14 exact, mean native−archive `+1.044119512744587e−5`, sample sd `1.1373138294979915e−4`, max abs `2.576210435948356e−4` | Not an archive-execution bit match |
| `C0a`: owner output passive capture `A0u=A0` | PASS | **PASS**, identical exact native `Y_big` | Same code, output capture does not perturb |
| `C0b`: author default A0 vs explicitly Float64 1e−3/1e−6 A1 | FAIL | **FAIL**, source `X_A1-X_A0=+1.3981561391387953e−5` Float64; independent Decimal70 original `X_T0_big` `+0.00001398156139138918586976222002` | Real numeric non-identity, exact physical mechanism not isolated by an additional rational-tolerance run |
| `C0c`: A1 vs A2 `saveat` perturbation | NO_CONFOUND | **PASS**, same `Y_big`, `naccept=1284`, `nreject=82` | A2's **stored `sol.u`** is not the accepted-step log; different saved-grid K statistics cannot be compared as same step-clock samples |
| `S`: prereg reference A0 | RELEASE | **PASS per prereg**, `|X_A4-X_A3|=3.969556598093504e−6`, `0.5|X_A3-X_A0|=4.700210888698708e−6` | Marginal difference, not a certified asymptotic bound |
| `S`: posthoc comparison using A1 as base | HOLD | **PASS this conditional posthoc HOLD**, `0.5|X_A3-X_A1|=2.2905698069952685e−6` smaller than same 3.96956e−6 | This is NOT a failed prereg check; it is a reference-sensitivity falsifier |
| `C`: replicate earlier Mech-S9 ROT013 real j22 `beta=10^-16.99746...` | REP-BIT | **PASS**: `Ycode=0.25239220435845267`, first PBH-zero 8545, t_last_live `0.33492735181011263s` | Original point ~0.586% above original beta grid; callable original source, not physical Yp |

The single owner-accepted `X_n(T0)` ladder from exact native source records:
`A0=.11199209652621654, A1=.11200607808760793, A2=.11200607808760793, A3=.11200149694799394, A4=.11199752739139585`.
The spread over A0,A1,A3,A4 is **1.3981561391387953e−5**, due to default-vs-explicit A0/A1 at same nominal tolerances. The `Ycode` spread A1−A0 is `+3.546164234741189e−5`. Those observed differences are a **finite source numerical instability witness at this one chosen point**, NOT a statistical standard deviation, proven noise distribution, or universal error bound.

### Sharp 70-digit source-record gate margins

Using the literal original 100-bit-printed `X_T0_big` strings with independent Decimal70 (NOT native Float64 downconversion):
- prereg A0 contraction margin `0.5|X_A3-X_A0|-|X_A4-X_A3|=+7.3065429060228424928405378e−7` — formal RELEASE;
- alternate posthoc A1 contraction margin `0.5|X_A3-X_A1|-|X_A4-X_A3|=−1.67898679111125960700955785e−6` — HOLD.

These margins are narrower than A0↔A1 1.398e−5 source non-equivalence. So the owner *correctly* reports formal S RELEASE and sensitivity HOLD: the prerecorded arithmetic is TRUE, while promotion to a reference-independent numerical-convergence certificate is FALSE.

**C0b mechanism guard:** Badacz's REVIEW_067 traces implicit `reltol/abstol` rational default converted into ArbFloat versus explicit Float64 tolerance values in OrdinaryDiffEqCore. That is a plausible source-level cause for a nonidentical adaptive-step sequence, and the original source step counts indeed differ `1290/91` vs `1284/82`. Neither our independent Python replay nor Badacz's A0–A4 test *directly isolates representation-only causality* by rerunning `reltol=1//1000,abstol=1//10^6`; do NOT claim experimental mechanism proof. That would be a NEW native Julia call requiring separate Moderator approval.

Further Badacz-owner recorded **accepted-step** evidence: Kclock relative spread `2.05695187e−3` (A0) to `1.50824113e−4` (A3) to `4.73952573e−6` (A4); source stop-mass postflag `M/M_stop` .778 (A0), .044 (A1), .797 (A3), .973 (A4). These are **source-owner native solver metadata**, checked for exact records, not independently recreated with new solver runs. They are consistent with stronger numerical convergence but not an accuracy certificate or event-localized root solve.

## 4. Actually executed independent external source replay — reproducibility

Single executed successful Python-only GitHub Actions source audit:
- workflow code `.github/workflows/mech-s9-rot026-badacz-prereg066-review.yml` Git blob `cc784b6ad002a2686169fc5c7c6d4e5d84869fa5`, trigger commit **`3139374757eda5caf1f8bb8682fa64f499965889`**;
- independent stdlib source `research/mech-s9/2026-11-16/code/mech_s9_rot026_badacz_prereg066_independent_referee_stdlib.py` Git blob **`77c52384b2611e7603944fc43be8da0eae469962`**;
- completed GitHub Actions run **`43894214329`** job id `133393244423`, ALL steps SUCCESS, no new Julia;
- actual original authoritative generated result `ROT026_REFEREE.json` SHA256 **`41f39525e5cbde22cf9171a252b4fdd457755f43707466209b23c8baeee72d20`**;
- original owner byte-identical cold replay source result SHA `b59a0a06bd3c13305bcb58e1676da0a5a780c5477d03cfc05928f8d1b236013c`, posthoc SHA `8f3bde85f6df830902c797c494bc5e5bee0ea0fd52659014ffaa9202afa16e5a`;
- actual GitHub Actions output artifact ID **`14238950733`**, downloaded ZIP SHA256 **`d232b4fe962bf2d63d7b9718baa96633bab049a19d942316396526eca9672bdc`**. In this Moderator conversation, actual ZIP CRC PASS, eight member hashes in `RESULT_SHA256SUMS` independently verified **8/8 PASS**, and the actual new JSON source fields, both gate margins and STATUS log were directly read and matched the full source verification.
- a **prior failed source-identity workflow** `43893737436` was stopped because Mech-S9 itself supplied a truncated 63-digit expected hash to `sha256sum`, then `43894002664` source SHA discovery correctly read exact 64-digit source checksum but the independent code failed on its own wrong hardcoded 63-digit expected digest. Both failures are documented as checks that prevented false PASS. Only successful `43894214329` supports the completed referee verdict.
- Artifact contains independent numeric JSON, reproduced owner analysis/posthoc JSON, status logs, actual raw source SHA and manifest. Does not redistribute original scanned JLD2, 8 native JSONLs, author's 161MB BlackHawk tar, or native solver artifacts. Inputs remain linked at original pinned authors/owner source locations; this ZIP is evidence, not a fully offline executable environment.

## 5. Verdict, next B1 decision and strict ceilings

**I1 review verdict: `PASS_WITH_NUMERICAL_AND_REFERENCE_GUARDS`.** The **exact** Badacz `A-STAT/C0a PASS/C0b FAIL/C0c NO_CONFOUND/S RELEASE/REP-BIT PASS` conclusions are correct and independently reproducible from original Wu–Xu archive+owner raw. What is NOT proven is reference-independent asymptotic convergence of the 10D endpoint at stringent physical-signal scales. Badacz's own posthoc A1 HOLD is a materially demonstrated countercheck, not a contradiction or error in his preregistered arithmetic. Internal model calibration at one (j22,beta_max) source point measures A0↔A1 jitter ~1.4e−5 in X and ~3.55e−5 in Y, not a probability law or rigorous interval bound for other scan points.

**Recommended one decision for Moderator/Badacz/INT9:** keep native calibration result `REPRODUCIBILITY_PASS` and typed `S_FORMAL_RELEASE`, but maintain `B1_NUMERIC_NO_UNIVERSAL_ERROR_CERTIFICATE` for claims requiring X differences at order 1e−5 or smaller. Future signal-sized S gates must prefreeze precise tolerances and TYPES / same default representation and a noise baseline across replicates; alter a native solver only after explicit separate per-run approval. No new Julia run authorized TO MECH-S9 in ROT026. No physical PBH bound or Yp interpretation from `Ycode=2X/(1-X)`.

**BlackHawk E4 status separate:** Mech-S9 ROT025 actually directly SHA-admitted and extracted original exact official BlackHawk v2.3 archive and 15 real tables, resolving historic **source-access** gap, but original Wu–Xu producer's selected header / precise compiled rates and independent physical below-1e9g hadronization generator uncertainties remain *unverified*. Source access PASS is not E4 physical validation PASS.

NO NEW_NATIVE_JULIA / NO NEW_BLACKHAWK_RUN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE / GITHUB_PENDING_BW_INGEST.

## ROT028 retrospective correction and provenance

This full revision is dated 2026-11-16 and follows Badacz's explicit source-backed objection in `IW_BADACZ_B1_G1_PROPOSAL068_AND_ROT026_CUSTODY_REPLY_001_20261116`. Reviewer (Mech-S9) source-verified original owner manifest `991a9b28b671fbfade8010bf011dcec9e8c619b3`; **64/64 hex PASS**. All ROT026 numerical PASS and S-reference-sensitivity findings unaffected. Historical false owner-manifest-defect text is NOT accepted for scientific or BW custody purposes. Do not call the workflow filename or original report artifact title evidence of a defective owner manifest.
