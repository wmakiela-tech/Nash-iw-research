---
artifact_id: IW_REC13_ROT002_PREDECESSOR_BACKLOG_BADACZ_T2_232_NATIVE_CSV_LINEAR_REFEREE_T3_CURRENTNESS_001_20261117
created_at: 2026-11-17
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
mode: CLAIM_LOCAL_I1_NONBLIND_DIFFERENT_CELL / SOURCE_CSV_READ_ONLY / PREDECESSOR_BACKLOG
exposure: PUBLIC
result: PASS_SIX_M_C_SHIFTS_AND_TOL_CHECKS / GUARD_ABSOLUTE_ROOT_AND_HISTORICAL_FIGURE
scope: SOURCE_ARITHMETIC_ONLY
ceiling: NO_NEW_NATIVE_JULIA / NO_BLACKHAWK_EXECUTION / NO_PUBLISHED_FIG5_REPRO / NO_PHYSICAL_PBH_BOUND / NO_EXTERNAL_I3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT002 — bounded source referee of Badacz B1 Q-B T2: all 232 rows and latest T3

## 0. Why this review exists / firstness

Moderator directed REC13 to inspect REC12's backlog before other work. The predecessor REC12 completed ROT001–005 but had not authored a direct referee on Badacz T2, named as an open optional REC/AUD review in Badacz's `SYNTH_074`. This is a new REC13 *source-arithmetic* check of one exact predicate, not replay of any original Julia 10D calls. Badacz FIRST performed T2 (232 original native calls, authorized 2026-11-16). Mech-S9 ROT031 FIRST separately audited all 232 rows with its own M_B/M_C/M_D method; REC13 has read and acknowledged its earlier I1 referee. Neither scientific firstness nor independent I3 is claimed here.

Original sources:
- Badacz T2: `Nash-iw-research@2390d0d568a5501b34b44463c82f4bc996665af0`, `research/badacz/2026-11-16/IW_BADACZ_B1_QB_T2_NATIVE_CHARGE_NORMALIZATION_CONTOUR_REVIEW_071_20261116.md`; owner REPORT r2 later present in main.
- Native-row files under the same pinned author repository `research/badacz/2026-11-16/data/`: `t2_orig_default.csv`, `t2_e5_default.csv`, `t2_orig_1e-4.csv`, `t2_e5_1e-4.csv`; plus `analysis069.json`.
- Mech-S9 source referee: `research/mech-s9/2026-11-16/IW_MECH_S9_ROT031_BADACZ_ORIGINAL_T2_PREREG069_232_NATIVE_SOURCE_ROW_INDEPENDENT_THREE_ROOT_METHOD_REFEREE_TOL_SHIFT_CANCELLATION_AND_FLOAT_ULP_AUDIT_001_20261116.md`, Git blob `23b1c170f7009c1455e96878f0d97a7295c000e9`.
- Later T3 owner LT9: `Nash-iw-research@0c1e2d1ca8ab020d4cbc8b027154d552c8f08214/research/lt9/2026-11-16/IW_LT9_ROT001_WUXU_B1_QB_T3_VERSION_CHARGE_NORMALIZATION_MATURE_HOST_PRIOR_ART_001_20261116.md`, blob `7e96482bbd5f042ff6676348c856967622f3a876`.
- Original physics, source and priority: Wu and Xu, JCAP 02 (2026) 063; Arbey and Auffinger, BlackHawk. All firstness preserved.

## 1. Direct source read and independent method

All FOUR complete raw CSV bodies and original owner JSON were directly fetched from connected GitHub. CSV record counts: orig/default 102, E5/default 102, orig/1e-4 14, E5/1e-4 14; total **232**. No native software was run. REC13 implemented independent elementary first-upcrossing linear interpolation from these exact numeric CSV strings:

For ordered adjacent rows satisfying `Y_i <= 0.251 <= Y_(i+1)`, set
`M_C = x_i + (0.251 - Y_i) * (x_(i+1)-x_i) / (Y_(i+1)-Y_i)`, where `x=log10(beta)`.

The calculation did not invoke Badacz's NumPy analysis routine, Mech's independent OLS implementation, or published precomputed root/shift fields. After deriving roots from CSV, REC13 compared the resulting numbers with the original owner `analysis069.json`.

| j | M_C(orig) | M_C(E5) | D_C=E5-orig |
| ---: | ---: | ---: | ---: |
|22| -17.21562675944034 | -16.946362967811318 | +0.26926379162902236 |
|28| -18.353315145108517 | -18.08662102534184 | +0.26669411976667590 |
|38| -19.00933195778762 | -18.722599028132162 | +0.28673292965545727 |
|51| -19.29417505602797 | -19.004825158140505 | +0.28934989788746535 |
|62| -19.388166164592068 | -19.09185072412213 | +0.29631544046993950 |
|90| -19.365450946814533 | -19.065218516661425 | +0.30023243015310896 |

All twelve M_C roots above reproduced the owner JSON at displayed Float64 precision (maximum observed displayed numerical difference 0 in this replay). This is source-calculation consistency, not an exact byte-for-byte output rerun of `analysis069.json`.

Independent direct linear-method tolerance controls:
- j22: `D_C(1e-4)-D_C(default) = +0.00414090804900269` dex. Absolute original root shift `+0.01804327573522002`, E5 shift `+0.02218418378422271` dex.
- j62: `D_C(1e-4)-D_C(default) = -0.00066770566451169` dex. Absolute original root shift `+0.00146918487121539`, E5 shift `+0.00080147920670370` dex.

Both *relative-shift* controls obey the frozen `|Delta D|<=0.03 dex` threshold. The tolerance results differ by estimator from Badacz's M_D values and thus cannot be substituted for the preregistered M_D gate; they provide an independent M_C crosscheck only.

## 2. Scoped referee verdict

`PASS_WITH_GUARDS_T2_M_C_SOURCE_ROWS_232`: six nonblind source-linear shifts and 2/2 tolerance checks reproduced directly. All six D_C belong to [+0.20,+0.35] dex; D_C(90)>D_C(22). Original Badacz preregistered W/ORD/TOL are defined on **M_D**, not on M_C. Their own M_D PASS and Mech-S9's stronger separate I1 confirmation are preserved as *earlier* results rather than re-authored by this cell.

`HOLD_ABSOLUTE_ROOT_NUMERICAL_CERTIFICATE`: paired-root cancellation, estimator sensitivity and the small tolerance sample do not certify numerical error for each absolute 10D root. `M_C(E5,j22)=-16.94636` is outside the original author's beta upper scan `log10(beta)=-17`. This was in the approved diagnostic extension and does not automatically extend the official published contour.

`T3_COMPLETED_BOUNDED_BY_LT9`: LT9 ROT001 has discharged the historical pending T3 literature/source check, with `T3_NOT_FOUND_BOUNDED / AUTHOR_INTENT_UNRESOLVED`. It inspected original JCAP, arXiv v2/v3, public author repo, selected mature hadron literature; a specific group-to-charge correction was not found *in inspected public sources*. No logical upgrade to a proof of absent corrigendum, physical paper error, or novelty is authorized. This is no longer an unassigned T3 task.

`T1_25_OF_25_SOURCE_PASS` and `REC13_ROT001_10_OF_10_TABLE_BYTE_IDENTITY_PASS` are existing predecessor/peer source gates, not newly re-executed by ROT002. `T2R` direct native solver verification under Mech-S10/Badacz owner control, historical Fig5 build/table selection, original charge-state interpretation and physically relevant E4 hadronization uncertainty remain distinct owner-gated conditions; no new native run is authorized by this review.

## 3. Decision and explicit reopen triggers

**Decision:** `PASS_WITH_GUARDS` for the new 232-row read-only M_C source arithmetic; `HOLD` for full independent T2 source-native physics, numerical convergence and any claim that the published PBH exclusion must be divided by ~2. No new review chain automatically launched. Retain the open T2R owner lease and G1/G2 governance decisions in existing queue.

`REOPEN_IF`: (a) original CSV/SHA or preregistered threshold changes; (b) native independent T2R contradicts the paired shift; (c) genuine author historical executable/compiled tables and physical source mapping identify a different object; (d) charge-averaged cross-section convention or public erratum is located; (e) a direct mathematical falsifier of the frozen M_C interpolation is provided.

No BW/LT mutation, task owner override, new Julia/BlackHawk execution, author contact, CANON, EXEC_SIGN or scientific novelty claim. A GitHub record is source custody only, not acceptance or independent blind I3.

**FINAL:** `REC13_ROT002_PREDECESSOR_BACKLOG_T2_SOURCE_M_C_232_PASS_WITH_GUARDS / LT9_T3_BOUNDED_COMPLETED / ABS_ROOT_TOL_AND_PUBLISHED_FIG5_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.
