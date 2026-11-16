---
artifact_id: IW_MECH_S9_ROT029_APPROVED_T1_ORIGINAL_BLACKHAWK_V23_FIRST_MASS_SOURCE_EXECUTION_PARSER_GRID_PREREG_MISMATCH_AND_FAIL_CLOSED_001_20261116
date: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: APPROVED_ORIGINAL_BLACKHAWK_T1_EXPERIMENT_EXECUTION_FAIL_CLOSED_AND_SELF_CORRECTION
authorization: Moderator 2026-11-16 16:47 CET T1 via BADACZ relay
prereg: c896351e537d79c401eee9a36a80cfac3a47f19d
scientific_status: T1-NOREPRO_PARSER_GRID_ASSUMPTION_ERROR / NATIVE_SOURCE_ARCHIVE_BUILD_FIRST_RUN_PASS / NO_RATES_COMPARED / NO_VALID_PHYSICS_VERDICT
claim_ceiling: NOT_T1_GROUPED / NOT_T1_PERSTATE / NO_PHYSICAL_SOURCE_REPRODUCTION / NO_NEW_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT029 — preregistered BlackHawk T1 first execution fails closed because the reviewer conflated 100 primary energy nodes with 500 secondary emission-energy nodes

## 1. Owner and firstness

Original physics and software: BlackHawk authors **Arbey/Auffinger**, PBH–BBN model/source producer **Wu–Xu**. **Badacz FIRST** completed explicitly Moderator-authorized T2 native E5 vs original contour PREREG_069 and REVIEW_071 on 2026-11-16, with six conditional Δlog10β values 0.2723/0.2756/0.2758/0.2926/0.2981/0.3007 dex, W-PASS / ORD-PASS / TOL-STABLE, subject to T1/T3/E4; Mech-S9 mirrored Badacz's ACK and T2 results into issue #16. Mech ROT025 FIRST successfully extracted original BlackHawk v2.3 TAR previously first SHA-admitted by MT14; ROT027 FIRST compared actual original source PYTHIA current/old numerical data (179379/625005 numeric-different records).

On Nov16 Moderator approved source T1 and Badacz T2 separately, direct relay:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794844111499439

This T1 was prepared by Mech-S9 with GitHub prereg **COMMIT BEFORE EXECUTION** `c896351e537d79c401eee9a36a80cfac3a47f19d`, Git blob `720320a3f24b63a3fa8482dcfb8413a28db5598e`, explicitly fixing five Wu–Xu source hadron-table mass indices **0,22,49,74,99**, original PYTHIA BBN choice0, five channels `pipm,Kpm,K0L,proton,neutron`, ratio thresholds <=1e-5 for `T1-GROUPED` vs `T1-PERSTATE`, else `T1-NOREPRO`; original source versions and SHA. No changes to hypotheses or indices after seeing output.

## 2. Actual authorized BlackHawk execution and proof

Original official BlackHawk v2.3 `blackhawk_v2.3.tar.bz2` **161495983B** was freshly fetched during REAL GitHub Actions run **`43911170672`** and validated whole archive SHA256 **`dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`** exact Wu–Xu `Artifacts.toml`. Decompression PASS. Author frozen `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d` 3 original overlays separately checked exact Git blob:
- `BlackHawk_inst.c` `f517b0a71a3c994e396600ce73cb9658e440d646`;
- `BlackHawk_tot.c` `76758e05a71688b94979b326723d02dbdf630dc5`;
- `src/include.h` `3a1eaefd6d884c864056ea45233513493794ee7e`.

Original exact BlackHawk v2.3 `src/hadro_pythia.c` SHA256 `64bdaa88564f15a615b385a10c17ca5294fe19343e51593a8345951e5e34c62a` PASS, original author's patch line `//#define HARDTABLES` still COMMENTED (no source-enabled compiled precomputed-header branch), current PYTHIA BBN `pipm.txt` SHA256 `603f8b1a53efe316b4378da9a6242c1a1b3be026c17fbdaa917cb07f13850ac4`, old `pipm.txt` SHA256 `39306be56e4feeeb361c23983e64b7c4f193c60be4ffa7211b745275cad679fa`; original source distinct. Original `hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64` PASS, SHA256 `25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df`.

Original author source overlays were COMPILED with `make BlackHawk_inst.c BlackHawk_tot.c`, build SUCCESS. Executable sha256 `17da5c5bd9d2958c18ee2c31e1f8236b12be69902795c23e947d8da70eded221`. The first mass (original table j=0 / M=1e9 g) was **actually executed once** through original `BlackHawk_inst.x` with author notebook original wrapper's parameters, `hadronization_choice=0`, `E_number=100` **PRIMARY** energy count 5..1e5GeV, full source pythia tables. Native generator process returned exit code0, 2353B stdout SHA256 `2b40a8a0b7364bb84097171c62cf2490858dbd2131f2ed0d4ec59207a8e0fd01`, exact input .in SHA256 `22efd2bd5cfe40c1b09be16feb657054165870cea7b4efecd92e10a1fb6337a6`.

No further four masses were executed: the independent Python output parser HIT a STRICT SOURCE-ASSUMPTION ASSERTION after first actual `instantaneous_secondary_spectra.txt` output. Run counts: **ONE** BlackHawk source execution, **ZERO** original Julia executions; 0 of 25 final rate comparisons. The GitHub Actions infrastructure job reports `SUCCESS` because the numeric audit deliberately turns a source incompatibility into a source-typed JSON FAIL-CLOSED outcome, NOT because T1 source reproduction passed. A reader must inspect the JSON `verdict`, not merely workflow run conclusion.

## 3. Identified and owned scientific-method error

The FIRST original `instantaneous_secondary_spectra.txt` output contained **500 numerical secondary-energy rows**, whereas the Mech-authored Python parser incorrectly checked `len(data)==ENERGY_COUNT==100`, raising
`AssertionError: ('unexpected source E_number', 500)`.
This is NOT Wu–Xu's error. The original Wu–Xu notebook `valid_hadrons_from_BlackHawk.ipynb` Git blob `8a10396ae771b17059808fc2b91235dd194cba8d`, code cell12, calls `set_BlackHawk_energy_spectrum!(params, GeV(5), GeV(1e5), 100)` to set 100 **PRIMARY** input Hawking energy knots, then reads `inst_secondary_spectra["energy"]` and integrates its **ACTUAL OUTPUT grid length** through `mean(diff(log(E)))` with no `100`-row check. Original BlackHawk PYTHIA BBN hadronization table specifies **500 SECONDARY output knots**. Those two sizes are independent.

My ROT028 prereg §2 incorrectly said *read 100 secondary energies*, silently conflating input and output. Because the test contract was frozen, the code rejected 500; it correctly did NOT truncate to 100, pretend that 100 is original output, change prereg after inspecting output or output unearned GROUPED/PERSTATE. This is a **reviewer-origin prereg design mistake / incomplete source inspection**, not paper physics, no actual discrepancy of reconstructed rate yet.

**Declared source-valid verdict**: `T1-NOREPRO / PARSER_GRID_ASSUMPTION_ERROR`. This is neither `T1-GROUPED` nor `T1-PERSTATE`; it does NOT falsify BlackHawk source or determine the meaning of charge grouping.

The generated original raw secondary 500-point file was **not preserved** in the evidence ZIP because the Python parser raises prior to the copy instruction; thus no legitimate posthoc 500-point integral can be reconstructed from the delivered artifact without **a new generator execution**, which was NOT silently initiated. The source stdout and original config plus failure JSON and checksums are preserved. The missing raw file is an additional reviewer-custody limitation to fix, not a source author fault.

## 4. Evidence, controls, and scientific stop

Actual source-only GH Actions workflow at commit `45a1ea1647a857e53d667cf4536f1a2e23fb5603`, executable analysis script Git blob `d763a21589ea4e61061592d7474d7c907400989e` @commit `e64aaf2c32e0d5f73609037ab05a7e415ed0c2c4`; actual run link:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43911170672

Actual original GitHub Actions artifact ID **`14247857006`**, 10563B ZIP SHA256 **`e08930dd72f855a8d9bbc1d1b036d97a80f397ef35ab7bc384dea1c8cac620f1`**, downloaded into Moderator conversation and independently checked ZIP CRC PASS, **12/12** member SHA256 manifest checks PASS. Exact result JSON `T1_SOURCE_COMPARE_RESULT.json` SHA256 **`25ba0634beece6d08e64c02075d41d12d60f6d66f6100cf571a461c372198729`**, readback actual `verdict=T1-NOREPRO`, `generator_original_author_BBN_PYTHIA_runs=1`, `native_julia_runs=0`, `results=[]`, `error.type=AssertionError`, `error.message=('unexpected source E_number', 500)`. Build log 84682B SHA256 `012ef5742189edcbeaad9525db53f25b83f70fd208708d515678b4338f743574` and one input config full source SHA recorded. No original 161MB source TAR redistributed in this result.

Source chain authentic PASS, original build PASS, original j0 invocation PASS, original table comparison NOT PERFORMED, scientific T1 source semantic gate `HOLD_REPAIR`.

## 5. Proposal only, no unauthorized second experiment

**Single bounded repair proposal, NOT ACTIVE**: versioned T1 prereg `v002` should correct §2 from 100 SECONDARY to exactly **500 SECONDARY energy knots**, while retaining original **100 PRIMARY** knots, the five fixed mass indices [0,22,49,74,99], 25 rates, original notebook operator and original relative 1e-5 criterion, original source/BH SHA+3 overlay blobs and grouped/perstate/no-repro outcomes unchanged. Parser must copy the raw secondary file and its SHA **before** checking output shape, then refuse any other number/format. A separate, explicitly dated source/approver acknowledgment of this *post-observation technical prereg amendment* is required before another real BlackHawk execution, because the first run already consumed a j0 generator invocation. Do NOT relabel v001 retrospectively as accepting 500. No Julia or source physical equation changes proposed.

Mech and Badacz cross-bridge issue: https://github.com/wmakiela-tech/Nash-iw-research/issues/16
Badacz owner T2 already done PREREG_069 / REVIEW_071; its conditional native contour shift remains **HOLD** for physical interpretation until a future actually successful T1 and separate T3/E4 source validation.

FINAL: `ROT029_T1-NOREPRO_PARSER_GRID_ASSUMPTION_ERROR / BLACKHAWK_161MB_SHA_PASS / ORIGINAL_OVERLAY3_PASS / ORIGINAL_COMPILE_PASS / J000_AUTHOR_EXEC_PASS / 0_OF_25_RATE_CHECKS / EXACT_RESULT_JSON_SOURCE_PASS / 12_OF_12_MANIFEST_PASS / CORRECTED_PREREG_V002_REQUIRES_NEW_AUTH / NO_NEW_JULIA / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
