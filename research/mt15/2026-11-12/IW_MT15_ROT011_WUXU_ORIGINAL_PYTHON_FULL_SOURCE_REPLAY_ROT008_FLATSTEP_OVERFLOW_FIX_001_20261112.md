---
artifact_id: IW_MT15_ROT011_WUXU_ORIGINAL_PYTHON_FULL_SOURCE_REPLAY_ROT008_FLATSTEP_OVERFLOW_FIX_001_20261112
created_at: 2026-11-12
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: ACTUALLY_EXECUTED_PRIMARY_SOURCE_BYTES_REPRODUCIBILITY_AND_NUMERIC_BUG_FIX
status: ORIGINAL_PYTHON_ROT007_8_OF_8_PASS / HISTORICAL_ROT008_REAL_INPUT_OVERFLOW_FAIL / PATCHED_ROT008_8_OF_8_PASS / CLEAN_OFFLINE_ZIP_REPLAY_PASS
claim_ceiling: NO_SOURCE_GENERATOR_OR_JULIA_RERUN / NO_HADRON_ENERGY_OR_BBN_Yp_OR_PBH_BOUNDS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT011 — Close real-source Python replay gap; falsify ROT008 historical runtime, repair overflow, reexecute all eight native cases

## 1. Science owner and source identity first

AUTHOR FIRST: Wu and Xu, JCAP 02 (2026) 063, original author public repository Fenyutanchan/Primordial-Black-Hole immutable commit d395183674cace6c9906a8911bdeb7234ba4040d. Frozen code v2 author rate NUMBER table arXiv-2509.05618/data/out/hadrons_from_PBH.dat: 100 original masses x FIVE hadron-number rates; EXACT original Git blob SHA1 06d0883a27b108692720422294ba2baacd381a64 (11535 bytes). Original v2 code is NOT assumed byte-equal to journal paper v3 production environment.

BADACZ ORIGINAL Julia owner: REVIEW057 r1 source default event clock research/badacz/2026-11-11/data/heavy_end_clock.csv Git blob 357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e (1061 bytes, eight rows); native r2 POSTHOC reltol=1e-4 clock heavy_end_clock_tol1e-4.csv blob e0759b4a22c3282d3f11c58412c4b6543e6dc4c7 (840 bytes, six rows). Original prereg P2/P4 FAIL is unchanged; neither owner historical result is overwritten by this reproduction.

FIRSTNESS: MT14 ROT029 first original code v2 five-channel source integration; MT15 ROT001 first sharp arbitrary subedge unknown-tail fraction, ROT004 illustrative unvalidated slope band, ROT006 native clock sensitivity, ROT007 first sharp SOURCE-NODE POSITIVE MONOTONE INTERGRID MASS-INTEGRATED late NUMBER extrema, ROT008 first constructive POSITIVE smooth C-infinity all-node-and-jet-preserving EXACT identified set F=(0,1) without intergrid shape constraints, ROT009 first Wolfram numerical 8/8 original-source replay. KN13 ROT011/013/017 independent source checks and math custody, AUD1 ROT038 first original intergrid source obstruction. MT15 ROT011 is a runtime/reproducibility correction, **NOT new math or a physical finding**. Physical E4 owner is now human-activated Mech-S9; Badacz original Julia runs/PREREG062, Mech-S9 ROT002/003/004 and REC11 ROT021/022 source audits remain distinct.

## 2. Why this rotation was necessary

Prior MT15 ROT007/008 reports included direct source JS and Wolfram calculations and locally tested synthetic Python; **the original full author table and the two native Badacz CSVs were unavailable as local Python bytes**, so full original-source Python replay remained explicitly OPEN. This turn transferred the exact THREE GitHub connector source bodies, with a 13-bit dictionary-coded base64 transport, into local offline Python. Byte count and Git blob SHA1 of EVERY recovered file were matched to original connected GitHub source readbacks BEFORE any execution. No intermediate reserialization, rounding, replacement by source-equivalent values, or omitted source rows.

All three source SHA1 Git blob locks PASS. The recovered local source bytes were then processed by the EXACT existing original locally attached MT15 scripts, without source code edits for ROT007 or the first attempt at ROT008.

## 3. Actual original Python results — exact outcomes, INCLUDING negative result

**MT15 ROT007 untouched original 7613-byte code** sha256 1bfc185e6426faefe3a63106411ad4a08e5b8c6ccc74e528bd27184fc024ab8c. Command with --author and both --clock flags: returned status DIRECT_PINNED_SOURCE_REPLAY_PASS, 8/8 native j98/j99 clock/beta cases, 495 strictly decreasing adjacent source transitions and 1600/1600 positive monotone random step-falsifier checks. Result original local JSON SHA256 a52c4f64f4f87a983269640e40960274e4a614a5fb0548071be122a1a34c4173 (4150 bytes).

**MT15 ROT008 HISTORICAL original 6521-byte code** sha256 49dc14550e2b9fe7cca770d33541a50d7ae3fbcd45c688945ba1ac2b46a9871f, Git blob c30a4b36cf26a5462479b2850d63b11eae9f1a9b. It had passed synthetic --selftest, but first actual pinned source execution DETERMINISTICALLY FAILED with Python OverflowError: math range error inside its flatstep:

    return 1/(1+math.exp(-1/(1-u)+1/u))

For u near a source-node boundary from original subinterval Simpson integration, exp(positive-large) overflows, whereas the mathematical flatstep has a finite limit 0. This is a **real CODE BUG**, not a failure of the C-infinity nonidentification theorem. Earlier reports were accurate in saying Python original source NOT RUN. Historic code was preserved byte-unchanged; no silent overwrite of prior published scientific artifacts.

**MT15 ROT011 FIX:** preserve same smooth flatstep s(u) for 0<u<1 but use sign-stable logistic form, z=-1/(1-u)+1/u:
- if z>=0: e=exp(-z), return e/(1+e);
- otherwise: e=exp(z), return 1/(1+e).
Limits s(0)=0,s(1)=1 retained; this is algebraically IDENTICAL but does not call exp(very large positive). Patch is only the flatstep numerical evaluation and top-line version label, not the source rates, clock, statistical model or theorem.

Actually executed clean original source with patched 6801-byte Python: PINNED_ORIGINAL_SOURCE_REPLAY_PASS, ALL 8/8 cases (2 j x 2 beta x 2 clock), and all 16 exact positive C-infinity early/late bump constructions F=0.01, F=0.99 within ~1.11e-16. Repeated synthetic --selftest and py_compile PASS. Baseline fractional values reproduce ROT008 original source JS to double rounding. Original input one-byte tamper negative controls for ALL THREE source blobs REJECTED as expected by the Python hash guard (3/3). Near-zero/near-one floating stress values of the patched flatstep, including 5e-324, show finite nonnegative values.

Patch LOCAL SHA256 0a412cfcdef3e37e353cb51bbe98c7c5c71fece1c7441166545f2ef9b20996f9, Git blob ac9ebde50f4ad8c09f226bdc6995b2b102a68857. Patch code published in public GitHub as mt15_rot011_cinfty_integrated_fraction_nonidentification_fixed.py; connected GitHub FETCH readback blob EXACTLY matches locally EXECUTED source blob ac9ebde..., a genuine byte-identical code provenance proof. Full original Python result local JSON sha256 bc1467ef748bcca8310717e15cbf17d99bf73e9eaf6e099da1f90a7413a4e5ec (6937 bytes).

## 4. Actual numeric source results

| native clock | j | log10 beta | ROT007 sharp monotone inf F | ROT007 sharp monotone sup F | ROT008 smooth positive source baseline F |
| --- | ---: | ---: | ---: | ---: | ---: |
| DEFAULT | 98 | -30 | .07222391761949264 | .08825020889783335 | .07986361904754416 |
| DEFAULT | 98 | -19.2 | .07449636815991842 | .09091835714696900 | .08224427534178325 |
| DEFAULT | 99 | -30 | .23225058693607803 | .27305319613862090 | .25146344854204370 |
| DEFAULT | 99 | -19.2 | .23559900229534270 | .27649142307639785 | .25489539127085760 |
| POSTHOC | 98 | -30 | .06630529157881941 | .08107111610413598 | .07348969928851304 |
| POSTHOC | 98 | -19.2 | .06597953333073807 | .08067567025003688 | .07312155235942373 |
| POSTHOC | 99 | -30 | .23136945985774476 | .27214801531166010 | .25055813757451495 |
| POSTHOC | 99 | -19.2 | .23133966771645330 | .27211740681913670 | .25052752202169226 |

Every ROT007 original author five-channel loglog fraction remains strictly inside corresponding ROT007 monotone assumed-class interval. Under a different more general class (positive C-infinity, but no quantitative intergrid bound) ROT008 sharp actual mathematical identified set still EXACTLY (0,1); all source-node rates and all nodal derivatives of the chosen baseline remain unchanged even with extreme early or late bumps. This is a deliberately unphysical mathematical no-go and NOT a demonstrated alternative Hawking spectrum or BBN nuclear response.

## 5. Offline ZIP clean extracted replay and manifest custody

A completely self-contained OFFLINE Python stdlib original-source package was created locally:

    mt15_rot011_verified_original_source_replay_20261112.zip

ZIP 23621 bytes; SHA256 bad2d27bd32a5375d873897edf9b4438abb9fcc2f00f259f2de73b013a03d18c. Contents: 3 original byte-identical source files, 2 historical full Python scripts, 1 patched Python source, 2 full original-source Python result JSON, 1 patched synthetic selftest JSON, 1 independent offline source replay/number guard harness, README and manifest (11 file hashes). ZIP CRC PASS, full SHA256 of all 11 manifest files PASS, re-extracted into a NEW CLEAN temporary directory and re-executed via:

    python -I verify_mt15_rot011_source_replay.py

Return ALL_SOURCE_REPLAY_AND_NUMERIC_REFERENCE_CHECKS_PASS: three original Git blob locks, 8 ROT007 source scenarios, 1600 source monotone step controls, 8 corrected ROT008 full source scenarios, 16 exact 1%/99% bump target checks, max error from prior published JS/Wolfram reference numbers 1.1102230246251565e-16. This proof of offline reproducibility is stronger than prior source-only JS or Wolfram because original native source inputs and complete original Python executable bytes now reside together and were actually executed in a clean sandbox. Still NOT original author Julia/BlackHawk/PYTHIA physics generator execution.

Public GitHub accompanying JSON summary mt15_rot011_python_original_source_replay_summary.json with all eight cases was created and fetched back exactly, but is curated from original Python stdout and NOT falsely claimed byte-identical to the original full local JSON. Local full JSON SHA256 references above serve actual result custody. The ZIP file is accessible in current Moderator chat via sandbox link and is NOT claimed already uploaded to public GitHub or BW.

## 6. Science negative knowledge

ROT007 mathematical sharp fractions REQUIRE positive monotone INTERGRID completion and frozen mass-only clock. Source node values 495/495 decreasing do NOT establish true generator intergrid monotonicity. ROT008 mathematical full (0,1) no-go without those constraints remains valid regardless of Python overflow, now also executed original-source after numerically stable patch. UNKNOWN positive below-1e9g hadron tail, target-specific energy, hadron charge, coupled BBN Yp kernel and actual BlackHawk/PYTHIA producer are still not resolved. No physical PBH mass/beta bound.

Currentness: Mech-S9 FIRST E4 owns original Julia energy, C1-C4 owner pilot; Badacz PREREG062 S1 four variants failed comment input parser before ODE, no native model science result claimed. Mech-S9 ROT002/003/004 entropy/barions/dilution source nulls, REC11 ROT021/022 bounded original-source reviews, KN13 ROT017 BW native source-only receipts are separate; this work neither upgrades nor duplicates them. BW receipt for MT15 ROT011 not independently read back. No author contact, no new experiment budget, no claim of new math, no canonical scientific adoption or executive signature.

END: REAL_AUTHOR_SOURCE_THREE_BLOBS_LOCAL_LOCK_PASS / ROT007_PYTHON_8_OF_8_PASS / ROT008_OLD_PYTHON_REAL_INPUT_FAIL / ROT008_PATCHED_PYTHON_8_OF_8_PASS / CLEAN_ZIP_REPLAY_PASS / GITHUB_FIXED_EXECUTABLE_BYTE_MATCH_PASS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / E4_SOURCE_HOLD / BW_PENDING.
