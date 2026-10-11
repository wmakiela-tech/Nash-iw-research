# REC9 / XH-S3 WU-XU WATERFALL MAP REFEREE

RETURN_ID: REC9-XH-S3-WU-XU-WATERFALL-MAP-REFEREE-001  
TARGET: XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019 + LT DRAFT018 integration  
VERDICT: PASS_DIRECTIONAL_PROJECTION / PASS_CANDIDATE_DE_FORMULATION / REPAIR_FEEDBACK_AND_B2_CLAIM_CEILING  
SEVERITY: MEDIUM

## 1. Primary directional projection — PASS EXACT

For the source-native hadronic contribution
X'|had = (1-X) A - X B,
with A = Lambda_{p->n} and B = Lambda_{n->p}, define R=A+B and, on R>0, q=A/R.

Then exactly:
X'|had = R(q-X).

Therefore (A,B) are the correct primary source-native directional-rate object. The chart (R,q) is exactly replay-sufficient for the hadronic RHS wherever R>0. At R=0, q is undefined/ill-conditioned while A=B=0 remains well typed.

This repairs the previous NC/XH object mismatch because no identification with hadron-population depletion D_h is required.

## 2. Replay sufficiency — PASS WITH SEMANTIC CEILING

If A_FULL(t), B_FULL(t) are extracted from one full Wu-Xu trajectory, then the same initial X and the same non-hadronic RHS reproduce that X trajectory exactly.

This is on-trajectory compression/replay.

It does NOT establish:
- a constitutive state law (A,B)=F(X,state);
- predictive sufficiency under changed source/background;
- DE closure validity;
- Yp or D/H target sufficiency.

XH states this firewall correctly.

## 3. Source-native DE formulation — PASS AS CANDIDATE

Where the stated public hadron equation has scalar source-sink form
n_h' = S_h - D_h(X,T,n_B,...) n_h,
the algebraic population n_h*=S_h/D_h is a legitimate source-native dynamical-equilibrium candidate.

Substitution into the directional-rate formulas A and B therefore yields a legitimate reduced candidate model.

This proves FORMULABILITY only.

It does NOT prove:
- existence or uniqueness of a coupled instantaneous fixed point;
- convergence of an iteration used to find one;
- dynamic tracking of the full hadron ODE;
- target-relative accuracy.

FROZEN ALGEBRAIC ROOT != DYNAMIC TRAJECTORY ACCURACY.

## 4. Feedback typing repair

Harvest 019 says the multi-species gate is source-native. The Wu-Xu equations indeed contain source-native state dependence, but species count is not the fundamental gate.

Even a single species can yield a state-dependent total directional strength R(X,state) through its state-dependent population. Conversely, several species with externally prescribed population/composition histories can still produce prescribed A(t),B(t).

Safe typing:
DIRECTIONAL_RATES_PRESCRIBED_IN_TIME
vs
DIRECTIONAL_RATES_STATE_DEPENDENT.

For the ratio chart separately:
q_PRESCRIBED
vs
q_STATE_DEPENDENT.

MULTI_SPECIES != FEEDBACK AUTOMATICALLY.
SINGLE_SPECIES != NO_FEEDBACK AUTOMATICALLY.

The source-native Wu-Xu system is on the state-dependent side, so the scientific conclusion survives; only the reason should be typed more sharply.

## 5. Fixed-point claim ceiling

The equation X = q_DE(X;state) is only the hadron-dominated instantaneous equilibrium condition.

With standard weak/decay terms retained, the relevant reduced scientific object is the dynamic X equation, as XH also writes.

Therefore:
INSTANTANEOUS HADRON-DOMINATED FIXED POINT != FULL REDUCED DYNAMICS.

Existence, uniqueness, conditioning, numerical iteration convergence, and dynamic tracking remain separate.

The earlier NC elasticity overreach remains rejected:
LOCAL NONCONTRACTION != NONEXISTENCE.

## 6. Validation contract repair

Comparing A_DE vs A_FULL, B_DE vs B_FULL, species fractions and replayed X is a good staged diagnostic, but raw visual or pointwise closeness is not itself a target certificate.

Before a claim-bearing validation, freeze:
- source/background history;
- initial state;
- comparison interval;
- norms/weights for A and B;
- completion/timeout semantics;
- tolerance for X trajectory error;
- target family and target tolerance.

A,B should be validated before using the derived q=A/(A+B), because q is poorly conditioned near R=A+B=0.

For dynamic X validation, the existing monotone/stability error propagation can translate directional-rate error into trajectory error when its assumptions hold.

Only after that should Yp/D-H target weighting be used.

DESCRIPTOR AGREEMENT != TARGET AGREEMENT AUTOMATICALLY.

## 7. B2 extension — FORMAL STRUCTURAL COMPATIBILITY ONLY

Replacing each additive monochromatic injection source by an aggregate population source Q_h is mathematically compatible with the same source-sink architecture if:
- individual PBH emissions add linearly at the injection level;
- all injected hadrons feed one common ambient BBN state;
- the background/source carrier is defined consistently;
- no source component is double counted;
- the PBH population evolution and background feedback are included in the frozen B2 contract.

The downstream closure is still nonlinear through the shared state even though the injection source is additive.

Therefore:
LINEAR SOURCE AGGREGATION != LINEAR SOLUTION SUPERPOSITION.
MONOCHROMATIC SOURCE-MATCHED CLOSURE != B2 SOURCE-VALIDATED CLOSURE.

XH correctly labels B2 as structural/not validated.

The sentence "the remaining gap is not formulation but validation" is safe only for the monochromatic Wu-Xu candidate. For B2, source/carrier admission and background coupling remain formulation/source-binding work as well.

## 8. DRAFT018 integration

DRAFT018 has already made the key Rec9 repair:
- (A,B) directional rates are primary;
- (R,q) is a derived chart;
- D_h population depletion is distinct from R;
- replay sufficiency != predictive closure sufficiency;
- independent population-error control is required.

Retain those.

Recommended minor tightening:
- replace "multi-species feedback gate" by "state-dependent directional-rate/composition gate";
- type the mono-vs-B2 claim separately;
- attach explicit validation metric/tolerance before calling descriptor comparison PASS.

## 9. Final status

WU_XU_DIRECTIONAL_RATE_PROJECTION = PASS_EXACT.  
AB_PRIMARY_TYPED_OBJECT = PASS.  
RQ_REPLAY_CHART = PASS_ON_R_GT_0.  
TRAJECTORY_REPLAY_SUFFICIENCY = PASS_EXACT / ON-TRAJECTORY ONLY.  
SOURCE_NATIVE_DE_FORMULATION = PASS_CANDIDATE.  
DE_DYNAMIC_VALIDATION = NOT_RUN.  
FEEDBACK_GATE = RETYPE_TO_STATE_DEPENDENT_DIRECTIONAL_RATES.  
MULTI_SPECIES_AS_NECESSARY_GATE = REJECTED.  
B2_SOURCE_AGGREGATION = FORMALLY_COMPATIBLE / SOURCE-CARRIER_VALIDATION_OPEN.  
PBH_B2_WATERFALL_TRANSFER = OPEN.  
REDUCED_WATERFALL_DESCRIPTOR = CANDIDATE / NOT VALIDATED FOR PREDICTION.  
SOURCE_MATCHED_K_PBH = UNDEFINED.  
NOVELTY_CANDIDATE = NONE.  
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.  
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration. Reopen only for source-matched DE-vs-full execution, B2 source/carrier validation, or a stronger sufficiency claim.
