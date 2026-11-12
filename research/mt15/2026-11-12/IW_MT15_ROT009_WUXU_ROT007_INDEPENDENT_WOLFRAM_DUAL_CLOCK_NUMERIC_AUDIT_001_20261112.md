---
artifact_id: IW_MT15_ROT009_WUXU_ROT007_INDEPENDENT_WOLFRAM_DUAL_CLOCK_NUMERIC_AUDIT_001_20261112
created_at: 2026-11-12
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: ACTUALLY_EXECUTED_ORIGINAL_SOURCE_NUMERIC_CROSS_LANGUAGE_AUDIT
status: 100x5_AUTHOR_SOURCE_TWO_NATIVE_CLOCKS_WOLFRAM_PASS_8_CASES / PYTHON_LOCAL_SYNTHETIC_PASS / PYTHON_ORIGINAL_SOURCE_CLI_NOT_EXECUTED
claim_ceiling: MONOTONE_INTERGRID_SOURCE_CLASS_AND_FROZEN_NUMBER_CLOCK_ONLY / NO_PHYSICAL_BBN_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT009 — independent Wolfram execution confirms all ROT007 sharp monotone-integral bounds

## Original source and firstness

Original AUTHOR: Wu–Xu, JCAP 02 (2026) 063; frozen original public repository Fenyutanchan/Primordial-Black-Hole, immutable commit d395183674cace6c9906a8911bdeb7234ba4040d. Author 100×5 original mass/number-rate table arXiv-2509.05618/data/out/hadrons_from_PBH.dat Git blob SHA1 06d0883a27b108692720422294ba2baacd381a64, mass converted original GeV to grams using 5.609588603804452e23 GeV/g. No code-v2 vs published-paper-v3 build identity asserted.

BADACZ original native Julia OWNER: REVIEW057 r1 eight-row default event clock Git blob 357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e and r2 six-row posthoc 1e-4 event clock Git blob e0759b4a22c3282d3f11c58412c4b6543e6dc4c7. Original precommit P2/P4 FAIL remains. Mech-S8 historical original physical source E4 firstness; new current owner Mech-S9 HUMAN ACTIVATED on Nov12. Mech-S8 ROT020 actual JLD2 and code/paper Yp source discrepancy OWNER ACK, but historical final JCAP build and physical bound HOLD. Badacz original PREREG062 4 variants C1–C4 failed driver parsing at S1 before magic/ODE; REC11 ROT020, INT9 ROT015, KN13 ROT016 independent parser controls, not a physical model FAIL. No native Julia execution by MT15.

MT14 ROT029 first original five-channel loglog source quadrature; MT15 ROT001 number partial ID, ROT004 conditional UNSOURCED slope band, ROT006 default/posthoc mass clock sensitivity. MT15 ROT007 FIRST sharp post-event mass-weighted number fraction inf/sup in hypothetical POSITIVE MONOTONE INTERGRID completions; AUD1 ROT038 first original strictly decreasing node transitions and C-infinity inter-node nonidentification, Mech-S8 ROT017 first full-table 490 LOO and flat edge falsifier, ROT018 first masked long-horizon known-data source test. MT15 ROT008 FIRST target-integrated C-infinity positive bump proof that WITHOUT intergrid monotonicity same 100 node values and all nodal jets permit ANY late fraction in (0,1). Firstness preserved.

## Executed independent mathematics runtime

This turn DIRECTLY fetched all three ORIGINAL immutable Git source blobs via GitHub connector. The actual NATIVE WOLFRAM LANGUAGE EVALUATOR was then invoked on original 100×6 numerical author data and eight source j98/j99 owner event records converted to Wolfram numeric matrix literals (no manually invented source values). Independently implemented via Wolfram Module, Do, Total and weighted source-cell arithmetic, NOT earlier JS or Python execution. Original author mass values were serialized as machine numbers, so this is independent arithmetic but NOT a high-precision author-spectra certificate or source-generator reexecution.

With normalized x=M/(1e9 g), frozen dt ∝ M²dM, 1<t=M_Tnuc/(1e9g)<m=M_init/(1e9g), source original left/right rate sums U,V, positive monotone between-node assumption, W(a,b)=(b³-a³)/3:
- Wholly late cell Llo sums V*W and Lhi sums U*W;
- Wholly early cell Elo sums V*W and Ehi sums U*W;
- Single crossing cell weights Wl=W(a,t), We=W(t,b);
- exact sharp inf F = min[(Llo+V Wl)/(Llo+V Wl+Ehi+V We), (Llo+U Wl)/(Llo+U Wl+Ehi+U We)];
- exact sharp sup F = (Lhi+U Wl)/(Lhi+U Wl+Elo+V We).

Independent executed Wolfram output:

| clock | j | log10 beta | Wolfram inf | Wolfram sup |
| --- | ---: | ---: | ---: | ---: |
| DEFAULT | 98 | -30 | .07222391761949262 | .08825020889783333 |
| DEFAULT | 98 | -19.2 | .07449636815991842 | .09091835714696904 |
| DEFAULT | 99 | -30 | .23225058693607800 | .27305319613862095 |
| DEFAULT | 99 | -19.2 | .23559900229534267 | .27649142307639790 |
| POSTHOC | 98 | -30 | .06630529157881941 | .08107111610413599 |
| POSTHOC | 98 | -19.2 | .06597953333073808 | .08067567025003687 |
| POSTHOC | 99 | -30 | .23136945985774476 | .27214801531166016 |
| POSTHOC | 99 | -19.2 | .23133966771645326 | .27211740681913670 |

A SEPARATE JS comparator executed AFTER Wolfram returned, fetching the original MT15 ROT007 SOURCE result JSON exact original Git blob bd8af5686fe18709a2e3c60a4efac7d07943c01a, produced max absolute difference across ALL 16 endpoint numbers = 5.551115123125783e-17, 8/8 scenarios PASS. Immutable audit result JSON companion: mt15_rot009_wolfram_independent_100x5_eight_case_comparison.json, all source metadata and per-case residuals, direct GitHub readback PASS. This confirms ROT007 numerical arithmetic, not its physical interpolation premise.

## Two user-attached local Python scripts tested

Actual uploaded code on working system:
- mt15_rot007_monotone_table_integral_bounds.py local SHA256 1bfc185e6426faefe3a63106411ad4a08e5b8c6ccc74e528bd27184fc024ab8c
- mt15_rot008_cinfty_integrated_fraction_nonidentification.py local SHA256 49dc14550e2b9fe7cca770d33541a50d7ae3fbcd45c688945ba1ac2b46a9871f

EXECUTED python -m py_compile on BOTH: PASS. EXECUTED Python3 ROT007 --selftest: 250 of 250 synthetic monotone finite-step test controls PASS; source-independent synthetic fraction inf .10606872729438392 / sup .5243941140117919 and original-style source loglog value .2746866599926128 inside. EXECUTED Python3 ROT008 --selftest: synthetic positive smooth bump 4-node fraction baseline .2637018208306332, target one percent and ninety-nine percent PASS. Both tests do not use author source bytes.

Despite attempts, original author Git source file and Badacz original clocks were NOT available as local file system fixtures in the offline Python runtime; original Python source-CLI replay NOT executed. Original source was, however, used directly in separate native Wolfram Language executable and earlier MT15 JS. DO NOT silently upgrade Python fixture status.

## Science ceiling and scope correction

ROT007 intervals are sharp only given the stipulated MONOTONE INTERGRID source-rate functions plus frozen mass-only model clock; 495 strictly decreasing source adjacent NODE transitions do NOT establish hidden inter-node monotonicity. Under positive C-infinity rates without monotonicity/derivative/amplitude bounds, ROT008 proves the identified fraction set exactly (0,1), even preserving all 100 node values and every nodal derivative of a chosen baseline. Adding an unrestricted nonnegative below-1e9g source number tail also destroys the apparently finite total late-fraction sup.

This is five-channel HADRON NUMBER ONLY. No real BlackHawk/PYTHIA full hadron spectrum, E4 source validation, neutron ODE, Yp helium contour, final JCAP Fig5 build, physical BBN response or PBH beta bound. No mathematical novelty, no source I3 independent referee, no canonical change, no executive signature. Native C1–C4 parser S1 bug belongs Badacz/Mech-S9, not MT15.

STOP: SOURCE_WOLFRAM_INDEPENDENT_8_CASE_PASS / MAX_ABS_DIFFERENCE_5.55e-17 / LOCAL_PYTHON_TWO_SYNTHETIC_PASS / PYTHON_SOURCE_FIXTURES_NOT_EXECUTED / E4_SOURCE_HOLD / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
