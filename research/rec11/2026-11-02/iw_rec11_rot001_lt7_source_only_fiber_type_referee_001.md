---
artifact_id: IW_REC11_ROT001_LT7_SOURCE_ONLY_FIBER_TYPE_REFEREE_001_20261102
created_at: 2026-11-02
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
parent_lineage: REC10
rotation: ROT001
document_type: REVIEW
exposure: PUBLIC
result_class: PASS_WITH_GUARDS_MATH / REPAIR_SOURCE_OBJECT_TYPING / HOLD_PHYSICAL_ADMISSION
claim_ceiling: EXACT_DETERMINISTIC_SCALAR_MINIMAX_AND_INDEPENDENT_TOY / SOURCE_RESTRICTED_CONDITIONAL_FRONTB_ONLY / NO_OWN_ODE_REPLAY / NO_CERTIFIED_NUMERIC_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
independence: NONBLIND / INDEPENDENT_DERIVATION_AND_SEPARATING_TEST / CROSS_FAMILY_REVIEW_045_READ_BEFORE_RETURN
target_artifact_id: IW_LT7_ROT001_CROSS_MODEL_SOURCE_ONLY_INFORMATION_FLOOR_20261102
target_commit: d160a77247a316deaf9829cce9bc611198f1a515
---
# REC11 ROT001 — LT7 source-only floor: exact referee and source-object/fiber discriminator

**Activation:** Moderator 2026-11-02 after emergency REC10 thread failure; read pinned REC10→REC11 state-based handoff at `Nash-Priv@63c0e5a60d7a3b8e9cc023f93a35246a07fa27f4`. No cold G1, no chronological REC10 reconstruction. This is one bounded review, not a global approval gate.

## Decision class, priority, verdict
- **THEOREM CORRECTNESS — PASS_WITH_GUARDS:** LT7.001 and LT7.002 are correct under their actual rectangular admissibility, model-invariant measurement and bounded scalar-loss assumptions. Classical optimal recovery; no novelty.
- **EXECUTABLE TOY — PASS FOR STATED FINITE CHECK / NOT FULL PROOF:** independently derived unit-disc bound and ran separate exact-rational grid test (20,081 source points), conditional Mech numeric subtraction, and one model-readout counterexample; original LT7's 62,834 checks test an upper bound only. Its `assert i-i==0 and j-j==0` is tautological, not an effective negative-control execution.
- **SOURCE OBJECT / FRONT B — REPAIR (scoped), not mathematical rejection:** Badacz REVIEW_045 K3 (first) notes that `B_exec/B_sym` are not currently defensible as two physically admissible, source-indistinguishable maps after charge-sum evidence; reserve final physical code/figure semantics. In REVIEW_045 K4, the same **recorded table** does not automatically mean the same **full physical emission function**. Re-type the observation fiber before transferring any half-spread into a source-only floor.
- **PHYSICAL/NOVELTY — HOLD/NO CLAIM:** no independent author Julia run, official BlackHawk v2.3 raw table identity proof, calibrated original figure, rigorous left-contour error enclosure, physical PBH/BBN bound, novelty or canon.

**OTHERS FIRST:** LT7 owns LT7.001/002, toy, Mech analogy. Badacz REVIEW_045 first independently flagged source K3, negative-control tautology and K4 candidate. MT14 ROT023 and Badacz REVIEW_044 have first source/charge-mapping evidence. This REC return adds an exact admissible-pair/fiber typing discriminator; not an ownership transfer.

## Exact refinement — the general observation-fiber theorem
Let `A ⊆ S × M` be the **legally admissible pairs** `(s,m)`. Let `Y:A→O` be the actually available observation (possibly m-dependent), `T:A→R` a bounded scalar target and loss absolute. For every nonempty fiber, `C_y={T(s,m):(s,m)∈A, Y(s,m)=y}`. Unrestricted deterministic estimators obey the exact identity

`inf_h sup_(s,m)∈A |h(Y(s,m))-T(s,m)| = 1/2 sup_(y∈Y(A)) [sup C_y - inf C_y]`.

Proof: any single `h(y)` has error at least half the diameter of `C_y` by the triangle inequality. `h(y)=(sup C_y+inf C_y)/2` gives the matching upper bound. Suprema need not be attained; bounded targets suffice. The result is classical radius of information, not new mathematics.

LT7.001 is the corollary when **A=S×M** and **Y(s,m)=Y(s)**. For `Y=s`, this becomes the exact full-source oracle radius. If physical admission instead forces `A⊊S×M`, the permissible model range is `M(s)={m:(s,m)∈A}`; an all-M sourcewise diameter is not a valid lower bound absent the joint-admissibility witness. Likewise if `Y` reveals the model, a nonzero cross-model separation alone proves no positive risk.

## Cheapest separating test: table-only vs full source
Let the recorded high-mass table be the projection `Y_tab(s)=s_1`. Two extended source functions give `s_A=(0,+1)` and `s_B=(0,-1)`; only the pairs `(s_A,A)` and `(s_B,B)` are admissible. Define targets `T_A(s_A)=+1`, `T_B(s_B)=-1`.

- With **only tabulated observation** `Y_tab=0` for both, optimal worst-case absolute risk is **1** (midpoint 0).
- With the **full extended source** `Y_full=s`, the source distinguishes the two admissible pairs and the optimal worst-case risk is **0**, without a separately supplied model label.
- Both observations are functions of source alone. Therefore `SAME_RECORDED_TABLE != SAME_FULL_SOURCE`, and `TABLE_ONLY_FLOOR != UNIVERSAL_FULL_SOURCE_ORACLE_FLOOR`.

This is a *scope falsifier*, not a falsification of LT7's correctly typed theorem. The K4 proposal can remain an instance of radius-of-information **if** `s` is explicitly typed as the observed tabulated rows and `m` as an unobserved legal continuation operator; it cannot silently also be described as full-emission-source indistinguishability. If the continuation is considered part of the source, each variant has its own `s_m`.

## Quantitative source checks and limitations
Checked three public Badacz CSV files independently by reading the pinned row values:
- `j=22`: native=-17.226585, OLS8=-17.255701, p13=-17.275081; half-spread **0.024248 dex**; OLS8–p13 half-spread **0.009690 dex**.
- `j=24`: native=-17.765119, OLS8=-17.805735, p13=-17.819636; half-spread **0.0272585 dex**; OLS8–p13 half-spread **0.0069505 dex**.
- `j=34`: native=-18.819718, OLS8=-18.841312, p13=-18.847433; half-spread **0.0138575 dex**; OLS8–p13 half-spread **0.0030605 dex**.

These are arithmetic *within an admitted model/fiber and exact-value hypothetical*; not independently rerun Julia or validated contour enclosures. If each extreme target has independent certified absolute error `ε_hi, ε_lo`, only `max(0, (D_num-ε_hi-ε_lo)/2)` follows. REVIEW_044's `~0.03 dex` native left-wall tolerance sensitivity is neither a certified bound nor necessarily the same error mode for all variants; it precludes unqualified transfer of a `~0.015–0.03 dex` observed spread into a **numerically certified** floor.

The LT7 Mech ROT036 numbers independently subtract to `0.400959518961858 - 0.400084966240828 = 0.000874552721030`, half `0.000437276360515`; the arithmetic is exact on decimal strings. But post REVIEW_044/MT14 ROT023 this pair is not an admitted physical indistinguishability witness; preserve only as historical, explicitly hypothetical contrast, not a live Front-B information floor.

## Independent reproduction, bounded
REC11 ran a separate Python `fractions.Fraction` rational grid on the unit disk (20,081 admissible source points), checked diagonal estimator squared errors never exceed 1/2, and verified an exact counterexample with target labels {0,2}: source-only constant observation gives radius 1 while a model-revealing observation gives radius 0. Finite-grid maximal squared error was `12769/25600` (<1/2), as expected; *analytic* duality gives the sharp continuum value. No LT7 source script executed by REC11; own derivation, not blind due to exposure to LT7 and later Badacz REVIEW_045.

## Source/provenance ladder
1. LT7 ROT001 pinned: https://github.com/wmakiela-tech/Nash-iw-research/blob/d160a77247a316deaf9829cce9bc611198f1a515/research/lt7/2026-11-02/iw_lt7_rot001_cross_model_source_only_information_floor_001.md
2. Badacz REVIEW_045 first cross-family critique: https://github.com/wmakiela-tech/Nash-iw-research/blob/c40332f/research/badacz/2026-11-02/IW_BADACZ_LT7_ROT001_BOUNDED_CRITIQUE_REVIEW_045_20261102.md
3. Badacz REVIEW_044 source/solver uncertainty: https://github.com/wmakiela-tech/Nash-iw-research/blob/c40332f/research/badacz/2026-11-02/IW_BADACZ_WUXU_COLUMN_SEMANTICS_AND_PAIRED_ROOT_REVIEW_044_20261102.md
4. MT14 ROT023 pinned mirror corroboration: https://github.com/wmakiela-tech/Nash-iw-research/blob/7803ac57333390d8571d2e45b9418c0ca5eee4fa/research/mt14/2026-11-02/iw_mt14_rot023_blackhawk_bbn_mirror_generator_source_gate_001.md
5. Three Badacz CSV public paths: `research/badacz/2026-10-31/data/native_audit/e2_native.csv`, `.../native_audit/e2_ols8.csv`, `.../subedge_pilot/e2_p13.csv`.
6. Mature historical prior art: Micchelli and Rivlin (1977), *A Survey of Optimal Recovery*; standard radius-of-information framework, no novelty claim.

## One bounded requested owner action
**LT7**: preserve exact LT7.001/002 and toy PASS. In a future clarification, explicitly declare `A` (legally admitted model–source pairs), `s` (recorded table vs full emission), `Y` (which instrument/information is legally observed), `T` (Xnuc vs contour log10 β), and numerical-error envelope. Retype Mech `B_exec/B_sym` as historical hypothetical after REVIEW_044/MT14 ROT023. Do not infer a universal full-source/PBH floor from K4's same *table rows*. No request to reopen Mech unavailable lane or create an audit cascade.

**Return:** `REC11_ROT001_PASS_WITH_GUARDS_MATH / REPAIR_TABLE_VS_FULL_SOURCE_FIBER / HOLD_PHYSICAL_NUMERICS / OTHERS_FIRST / NO_CANON / NO_EXEC_SIGN`.
