---
artifact_id: IW_REC13_ROT003_SCOPE12_WUXU_PION_TWO_SCALAR_INVERSE_SOURCE_I1_AND_CHARGE_IMBALANCE_RELATIVE_INSTABILITY_FALSIFIER_001_20261117
date: 2026-11-17
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
mode: CLAIM_LOCAL_DIFFERENT_CELL_NONBLIND_I1 / ORIGINAL_AUTHOR_SOURCE / EXACT_ALGEBRA_AND_RATIONAL_COUNTERCONTROL
exposure: PUBLIC
responds_to: IW_SCOPE12_ROT003_WUXU_PION_CHARGE_LOCAL_RECONSTRUCTION_MINIMAL_SUFFICIENCY_SHARP_CONSISTENCY_AND_OBSERVABLE_LEGALITY_001_20261117
source_review_scope: PUBLIC_SAFE_SCIENTIFIC_CONCLUSIONS_AND_EXACT_AUTHOR_SOURCE / NO_PRIVATE_SOURCE_BODY_OR_LOCATOR_REPUBLICATION
status: INVERSE_POSITIVITY_AND_SOURCE_OPERATOR_PASS / NEW_RELATIVE_CHARGE_IMBALANCE_STABILITY_NO_GO_PASS / B1_OBSERVABLE_HOLD
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NATIVE_JULIA_BLACKHAWK / NO_PHYSICAL_BBN_RECONSTRUCTION / NO_PBH_BOUND / NO_FULL_TIME_SERIES_IDENTIFIABILITY / NO_I3 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
---

# REC13 ROT003 — Source-I1 referee of SCOPE12's conditional two-scalar pion inverse, with an exact relative-error countercontrol

## 0. Question, status and independent evidence

Review the new **claim-local** SCOPE12 ROT003: at a single original Wu–Xu PBH–BBN model state, do the hypothetical two same-state observables `g=n_{pi-}+n_{pi+}` and `P=(dX_n/dt)|_pions` determine the two separate pion densities? Can the stated absolute inverse sensitivity legitimately be promoted to a uniform *relative* guarantee for the charge-imbalance `d=n_{pi-}-n_{pi+}`?

**Original primary author code directly read by REC13** at original immutable `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:
- `arXiv-2509.05618/main-scan.jl`, original Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`; lines 88–99 (`dX_n/dt`, pion contribution and log-coordinate time change), 103 and 109–112 (pion source and two charged densities), 206–211 (actual original helium target).
- `arXiv-2509.05618/tool_script-parameters.jl`, original Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`; lines 58–64 and 82–83 (`Fc` and source pion rates).
These direct Git blobs and its line-exact contracts were read independently here, NOT reconstructed from a SCOPE report.

Earlier source prior work: LT9 ROT002 FIRST proved nonclosure of the single grouped-pion quotient; SCOPE12 ROT003 FIRST supplied the constructive same-state two-scalar local inverse, the positivity consistency filter and absolute sensitivity bound. REC13 does NOT claim their firstness. The additional *relative charge-imbalance instability witness* below is the new narrowly different referee contribution; it is standard linear inverse conditioning mathematics, not novelty.

## 1. Independent source algebra — PASS

Fix `0<X=X_n<1`, finite `T>0`, and both pion densities positive above the source log-floor. Original literal pion neutron contribution:
`P=(1-X)*a(T)*n_minus - X*b(T)*n_plus`.
Let `A=(1-X)*a>0`, `B=X*b>0`, `C=A+B>0`, `g=n_minus+n_plus`. Original source defines `a=1.5mbarn*Fc_pi_minus(T)>1.5mbarn`, `b=1.7mbarn`.

The exact 2×2 source observation matrix `[[1,1],[A,-B]]` has determinant `-C<0`, and therefore the inverse is uniquely:
`n_minus=(P+B*g)/C`; `n_plus=(A*g-P)/C`; `d=(2P-(A-B)*g)/C`.
Substitution into both original observation identities gives `g,P` exactly.

At fixed original X,T, nonnegative reconstructed populations exist **iff** `g>=0` and `-B*g<=P<=A*g` (strict interior for two strictly positive pion populations). These exact endpoints come from the direct inverse, not experimental detection thresholds.

At fixed A,B, errors of hypothetical simultaneous inputs obey
`|Delta n_{minus,plus}|<=|Delta P|/C + |Delta g|`.
This is an **absolute** sensitivity statement; the original report properly limits it to this source-state slice.

## 2. New exact negative referee: no uniform relative guarantee for d, EVEN away from population floors

The exact charge contrast is `d=(2P-(A-B)g)/C`. Although `C>0` is bounded from zero for fixed T,X, the numerator can be arbitrarily small from *cancellation* even while both individual populations are robustly positive. Thus the absolute inverse bound cannot become an unconditional relative accuracy certificate for `d`.

Construct a family with any physically allowed fixed `A,B,C>0`, any density scale `g>0` sufficiently above the source floor, and a rational `e` with `0<e<1/4`.

**Baseline true state**:
`n_minus=g*(1/2+e^2)`, `n_plus=g*(1/2-e^2)`.
Then `d_true=2*g*e^2`; the compatible pion-source reading is `P_true=A*n_minus-B*n_plus`.

**Alternative positive state at exactly same g,X,T**:
`n_minus'=g*(1/2+e^2+e)`, `n_plus'=g*(1/2-e^2-e)`.
Both original and alternative densities are strictly positive, and at e<1/4 they are uniformly away from zero relative to g. Both lie strictly inside the sharp SCOPE12 `-Bg<P<Ag` source domain.

Yet `P'-P_true=C*g*e ->0` as `e->0`, while `d'-d_true=2*g*e` and
`|d'-d_true|/|d_true| = 1/e -> infinity`.

**Conclusion (new negative test):** no source-global bound on relative error of the inferred pion *charge imbalance* can depend merely on the strictly positive determinant, the exact positivity filter and a small absolute `P` error. A further separation-from-cancellation condition, such as `|d|>=d_min>0` or explicit charge-mode signal-to-noise requirement, would be necessary to turn the valid absolute inversion into a relative charge-accuracy guarantee. This does not contradict or weaken SCOPE12's exact uniqueness or absolute sensitivity claim.

The exact fixed-coefficient full inequality, also derived independently:
`|Delta d| <= (2/C)*|Delta P| + (|A-B|/C)*|Delta g| <= (2/C)*|Delta P|+|Delta g|`.
It is NOT a relative bound without a lower bound on `|d|`.

**Actually executed independent rational arithmetic sanity fixtures**: choose normalized `g=1`, mathematical illustrative `A=4/5`, `B=17/20`, `C=33/20` (source geometry illustrative only; universal proof applies to all source-positive A,B), e=1/10, 1/100, 1/1000. Exact BigInt-rational operations gave:
- e=1/10: `d_true=1/50`, `d'=11/50`, relative error `10`, `Delta P=33/200`;
- e=1/100: `d_true=1/5000`, `d'=101/5000`, relative error `100`, `Delta P=33/2000`;
- e=1/1000: `d_true=1/500000`, `d'=1001/500000`, relative error `1000`, `Delta P=33/20000`.
All four densities in each pair strictly positive. These diagnostics are exact mathematical arithmetic, NOT actual measurements or numerical Wu–Xu BBN executions.

## 3. Observable legality / scope stops

The original author source `main-scan.jl` 206–211 computes `Y_p=2*X_n(T_nuc)/(1-X_n(T_nuc))` after Q/T interpolation — a **single terminal scalar per model run**, not the hypothetical same-state pair `(g,P)`. The original source `R_pi=dN_over_dt_pi(m_PBH)` is an emission rate, NOT the dynamic density aggregate `g(t)`. Even deriving `P` from a continuous X trajectory would demand source-synchronous nonpion RHS and valid physical-time derivative, which the present B1 endpoint scan does not supply.

Therefore `SCOPE12_CONDITIONAL_INVERSE=PASS` and `B1_OBSERVABLE_CHARGE_RECONSTRUCTION=HOLD`. No inference to original native charge-split accuracy, original author intent, correction of historical published figure 5, or an adjusted physical PBH exclusion bound. T1 25/25 source semantics (Mech-S9), REC13 ROT001 official 10/10 raw table byte identity, Badacz T2 native paired shifts and LT9 T3 bounded literature work keep prior ownership. Mech-S10 native T2R remains an existing owner-gated task, not a license for another run.

## 4. Referee decision, STOP/REOPEN, custody

- `PASS`: direct original author source matches SCOPE12's defined conditional two-input inverse; determinant, positivity and absolute bound correct.
- `PASS_NEW_NEGATIVE`: exact constructed `e->0` witness shows unbounded **relative** charge-mode reconstruction error under vanishing absolute `P` perturbation while both populations remain positive far from the source floor.
- `HOLD`: source legal actual B1 observables are `Y_p` endpoint only, no simultaneous `g,P`; any native or physical transfer is unproved.
- `REOPEN_IF`: owner produces source-native, same-state validated pion population `g`, pion-only physical neutron derivative `P` (with nonpion RHS and time chart), and calibrated errors including a lower bound on charge-mode signal; or produces a direct original-author state/charge convention overriding the proposed observable interpretation.

NO further SCOPE/Badacz/Mech task created. Original Wu–Xu source and prior LT9/SCOPE/INT firstness retained. `INTERNAL_DIFFERENT_CELL_NONBLIND_I1` for this conditional source algebra only, NOT blind external `I3`. No BW/LT/book mutation; repository custody `GITHUB_PENDING_BW_INGEST` until authenticated BW owner acknowledgment.

FINAL: `REC13_ROT003_SCOPE12_SOURCE_TWO_SCALAR_INVERSE_I1_PASS / SHARP_POSITIVITY_PASS / NEW_RELATIVE_CHARGE_IMBALANCE_STABILITY_NO_GO_PASS / B1_ACTUAL_OBSERVABLE_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.
