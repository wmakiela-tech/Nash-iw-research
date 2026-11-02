---
artifact_id: IW_REC11_ROT002_LT7_MODEL_READOUT_FULL_SOURCE_SEPARATOR_001_20261102
created_at: 2026-11-02
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
rotation: ROT002
document_type: REVIEW
exposure: PUBLIC
result_class: PASS_WITH_GUARDS_EXACT_MATH / NEW_ASSUMPTION_SEPARATING_TEST / NO_PHYSICAL_ADMISSION
claim_ceiling: EXACT_CLASSICAL_TWO_MODEL_UNIT_DISC_ONLY / KNOWN_SOURCE_THEOREM_PASS / UNKNOWN_SOURCE_COUNTERCONTROL / NO_AUTHOR_FULL_REPORT_REPLAY / NO_FRONTB_TRANSFER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
independence: NONBLIND / INDEPENDENT_DERIVATION / SOURCE_SCRIPT_READ_NOT_EXECUTED
target_artifact_id: IW_LT7_ROT002_TARGET_ALIGNED_MODEL_DISCRIMINATION_20261102
target_code_commit: 896ded5425542171f93f9ed7ea8f87eff62ae51f
responds_to: IW_LT7_ROT002_TARGET_ALIGNED_MODEL_DISCRIMINATION_20261102
---

# REC11 ROT002 — LT7 ROT002 referee: model-sensitive readout and the full-source assumption

**Decision class:** theorem correctness, exact separating test, instrumentation/claim ceiling. **Owner:** LT7. **Referee:** REC11, nonblind. **Date:** 2 November 2026. This is one bounded scientific review, not AUD1 orchestration or an approval gate.

## 1. Direct currentness and evidence

Current LT7 ROT002 reached #iw-dispatch at 2026-11-02 13:28:17 CET under `IWTO_REC10`, inherited by activated REC11 after the REC10 technical failure. The posted message contains theorem, conditions, values, and source-code pointer. Pinned public source `lt7_rot002_reproduce.py`, Git blob `de30d84fda4949ad691cdb6bf9c63853648ef545`, commit `896ded5425542171f93f9ed7ea8f87eff62ae51f`, was fetched and inspected. The LT7 full detailed manuscript and local ZIP were reported as local to the Moderator; **their complete contents were not accessible for this review**. Thus the verdict attaches to the precise theorem and code *observed*, not to uninspected supplementary materials. No latest BW/adoption inferred from transport.

Original current LT7: two targets `T_A(s)=s_1`, `T_B(s)=s_2`, `s=(s_1,s_2)` in closed Euclidean unit disk, full **exact source s known to the estimator**, model unknown. A fixed instrument `w` (norm <=1) yields a model-sensitive reading `z_A(s)=(w.s)/2 + eta`, `z_B(s)=-(w.s)/2 + eta`, with adversarial deterministic `|eta|<=epsilon`.

## 2. Independent exact check: PASS_WITH_GUARDS

For fixed `s`, the two compatible-reading intervals intersect iff `|w.s|<=2epsilon`. In their intersection, observation cannot distinguish model labels, hence minimal worst scalar absolute error is `|T_A(s)-T_B(s)|/2 = |s_1-s_2|/2`; elsewhere the disjoint intervals identify the model and the known `s` identifies the target exactly. Consequently:

`R(w,epsilon)=(1/2) max_{||s||<=1, |w.s|<=2epsilon}|s_1-s_2|`.

For `||w||=1`, set `g=(1,-1)/sqrt(2)`, `c=|w.g|`, `q=sqrt(1-c^2)`, `d=min(1,2epsilon)`. Maximizing a linear functional over unit disk intersected with the slab yields

- `R=1/sqrt(2)` if `d>=c`;
- `R=(c*d+q*sqrt(1-d^2))/sqrt(2)` if `d<c`.

A nonunit `w` with `r=||w||>0` uses `d=min(1,2epsilon/r)`; `w=0` leaves all readings overlapping and has risk `1/sqrt(2)`. For any `||w||<=1`, every `||s||<=min(1,2epsilon)` is in the overlap slab. This forces `R>=min(1,2epsilon)/sqrt(2)`. The target-aligned unit instrument `w=g` achieves equality:

`inf_{||w||<=1} R(w,epsilon) = min(sqrt(2)*epsilon,1/sqrt(2))`.

This theorem is a **PASS** as stated. It is an elementary classical minimax/optimal-recovery calculation, no novelty priority. In particular for `epsilon=0.1`, aligned risk is `sqrt(2)/10` and orthogonal risk `1/sqrt(2)`. The original source script provides angle/noise numerical controls and a rational *subset* check; the proof is analytical, not certified by a grid.

## 3. New independent separating test: remove knowledge of full source

Maintain **exactly the same** two targets, unit disk, model-sensitive instrument and even the best noiseless (`epsilon=0`) measurement, but no longer furnish the estimator with the exact `s`. It sees **only z**, with `w` preselected. Denote the minimax risk by `R_no_source(w,0)`.

**Lower bound for every w:** for any nonzero `w`, choose a unit vector `u` orthogonal to `w`. The two sources `s=+u` and `s=-u` yield the **same reading z=0 for either model**. Select either target coordinate with larger `|u_i|`; its two values are `+|u_i|` and `-|u_i|` up to sign. Any estimator at z=0 errs by at least `max(|u_1|,|u_2|)>=1/sqrt(2)`. If `w=0` the same conclusion is immediate. Hence

`inf_{||w||<=1} R_no_source(w,0)>=1/sqrt(2)`.

**Matching upper bound:** choose `w=g=(1,-1)/sqrt(2)` and estimator `hatT(z)=sqrt(2)*z`. In model A, `z=(s_1-s_2)/(2sqrt(2))` and `s_1-hatT(z)=(s_1+s_2)/2`. In model B, `z=-(s_1-s_2)/(2sqrt(2))` and `s_2-hatT(z)=(s_1+s_2)/2`. By Cauchy-Schwarz `sup_{||s||<=1}|s_1+s_2|/2=1/sqrt(2)`. Therefore

**`inf_{||w||<=1} R_no_source(w,0) = 1/sqrt(2)`**,

while LT7's **known-full-source** optimum at `epsilon=0` is **zero**. The two opposite witnesses `s=+/- (1,1)/sqrt(2)` both have `z=0`, with source-coordinate target values `+/- 1/sqrt(2)`.

**Material implication:** A nominally model-sensitive instrument, even with *zero measurement noise*, need not reduce the original target risk if exact source coordinates are not separately observed. The exact-source side information is load-bearing. This does **not** falsify the correctly stated LT7 ROT002 theorem; it falsifies any unqualified transfer of its `epsilon->0` improvement to source-unknown physical observation.

## 4. Independent executable control and status

A distinct Python 3 standard-library `fractions.Fraction` script tested 25,445 rational unit-disk points (`N=90`) and both model errors for `w=g`, `epsilon=0`. At every source the two model errors equal `(s_1+s_2)/2`, and their squares do not exceed `1/2`. Maximal *grid* squared error was `16129/32400`, below the sharp continuum `1/2`; lower bound is supplied by the exact irrational antipodal witnesses, not the finite grid. Additional simple controls verified the known-source formula at `epsilon=0` and `.1`. The program was executed locally and printed the matching JSON. Neither this grid nor LT7's own grid is a substitute for an analytic sharpness proof.

Source: `verify_rec11_rot002_assumption_switch.py`, SHA-256 `925cab3f88536d80d08c5507dfaf1a8c9b52f4cd6dfb69129cb57fec7f05477b`; output: `rec11_rot002_result.json`, SHA-256 `4531ef54a41c024be17d261bdd0c86e6805a46698fbab914ce1117cbf9b33b62`.

## 5. Claim ceiling, attribution and one action

- **PASS_WITH_GUARDS:** exact theorem for known `s`, bounded deterministic measurement noise, model-index sensitive toy; source code inspected and independently checked by alternative proof and tests. **Not** a review of unavailable full LT7 local report/ZIP.
- **NEW NEGATIVE CONTROL:** without exact source knowledge, model-sensitive noiseless instrumentation cannot beat `1/sqrt(2)` in this unit-disc example, even after optimizing w.
- **HOLD:** physical implementability of `z_m`, real-world full-source oracle, unknown-source noisy minimax, specific Wu–Xu/Front-B mapping, source-native ODE/risk calibration and certified PBH/BBN bounds.
- **OTHERS FIRST:** LT7 owns all of ROT002, and REC11 does not claim novelty for classical radius-of-information, convex geometry or standard active discrimination. No re-opening of Mech-S7/S8 and no audit cascade.

**Single bounded owner action for LT7:** When restating ROT002 or importing it into the monograph, explicitly name the observation `Y=(s,z)` and mark that its risk reduction requires exact `s`. Keep `(z)`-only as a distinct model class (proved countercontrol above) and do not imply that a physical model-sensitive readout alone achieves the ROT002 optimum. If LT7 already did this consistently, no correction of the theorem is needed.

**Disposition:** `REC11_ROT002_PASS_WITH_GUARDS_KNOWN_SOURCE / SEPARATING_TEST_SOURCE_UNKNOWN / HOLD_PHYSICAL_TRANSFER / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.

## Sources
- LT7 ROT002 Slack source/owner: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793622497448899
- Pinned LT7 code: https://github.com/wmakiela-tech/Nash-iw-research/blob/896ded5425542171f93f9ed7ea8f87eff62ae51f/research/lt7/2026-11-02/lt7_rot002_reproduce.py
- REC11 previous scoped LT7 ROT001 referee: https://github.com/wmakiela-tech/Nash-iw-research/blob/aedd86b0e4877752c557634b268b80e35815b5a0/research/rec11/2026-11-02/iw_rec11_rot001_lt7_source_only_fiber_type_referee_001.md
