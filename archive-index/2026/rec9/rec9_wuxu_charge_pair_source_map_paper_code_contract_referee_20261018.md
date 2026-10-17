# REC9 — Wu–Xu charge-pair source-map and paper↔code contract referee

RETURN_ID: REC9-WUXU-CHARGE-PAIR-SOURCE-MAP-AND-PAPER-CODE-CONTRACT-REFEREE-001_20261018
CELL: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_08 / Rec9
CLASS: CLAIM-LOCAL STRESS / TYPE / HARDEN
VERDICT: PASS_HIGH_OBJECT_MAP_MISMATCH / PASS_COMMON_BACKGROUND_TRANSFORM / REPAIR_BSYM_EVIDENCE_LABEL / HOLD_PUBLISHED_ENDPOINT
SEVERITY: HIGH
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PBH_BOUND / NO_NEW_TASK

## Objects reviewed

1. XH-S3-FRONTB-WU-XU-PAPER-CODE-SOURCE-MAP-CURRENTNESS-HARVEST-026
   Drive: 1UX9zEyq008k0xrKtyBun-kcIivKWVFUNmzuvHWRh2Kk

2. MECH-S6-FRONTB-CHARGE-PAIR-SOURCE-MAP-AND-COMMON-BACKGROUND-RESPONSE-THEOREM-001
   controlling public revision reviewed:
   commit 47b5282f468072cc5dcb13eaf2c3f57aca65b618
   blob 6fd7f9d1a1096637502868ee69647ccd61426e43

3. Public Wu–Xu repository at commit:
   d395183674cace6c9906a8911bdeb7234ba4040d

   Directly checked:
   - arXiv-2509.05618/main-scan.jl
   - arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
   - arXiv-2509.05618/data/out/hadrons_from_PBH.dat

4. Wu & Xu, JCAP 02 (2026) 063 / arXiv:2509.05618, current arXiv text.

## 1. Source-native facts that pass

### 1.1 Paper-declared subedge source rule

The paper states:
- BlackHawk is used for m_BH >= 1e9 g;
- below 1e9 g, an analytical hadron source is used and rescaled to match BlackHawk at 1e9 g;
- the analytical rate scales as T_BH^1.3, hence as M^-1.3 for Schwarzschild PBHs.

Therefore:

PAPER_DECLARED_SUBEDGE_SOURCE = CALIBRATED ANALYTIC M^-1.3.

### 1.2 Current public helper

The public helper constructs log(rate) vs log(mass) LinearInterpolation objects with linear extrapolation and contains no explicit 1e9 g branch or explicit M^-1.3 formula.

The first table edge has slopes around -1.20.

Therefore:

CURRENT_PUBLIC_HELPER_SUBEDGE_SOURCE = LOG-LOG EDGE EXTRAPOLATION.

Hence:

PAPER_DECLARED_SUBEDGE_METHOD != CURRENT_PUBLIC_HELPER_SUBEDGE_SEMANTICS.

This mismatch is exact at the source-contract level.

It does NOT establish which source rule generated the published numerical scan. The committed scanning.jld2 and current code being colocated in repository history increases relevance but is not a provenance proof.

## 2. Aggregate source semantics

The paper labels hadronic yields as pi±, K±, K0_L, p, n and explicitly states that the quoted multiplicities include contributions from both particles and antiparticles.

For nucleons the paper further states explicitly that PBH hadronization generates the same amount of nucleons and antinucleons.

The public source table columns are:

charged_pion_dN_over_dt
charged_kaon_dN_over_dt
kaon_zero_long_dN_over_dt
proton_dN_over_dt
neutron_dN_over_dt.

Thus the charged-pion, charged-kaon and nucleon columns are not legally identical to one selected charge-conjugate reaction population without a charge-resolution map.

Controlling firewall:

PAIR-AGGREGATED SOURCE != SINGLE-CHARGE SOURCE.

## 3. Exact public executor map

Direct code inspection of main-scan.jl shows:

d_n_pi_from_PBH = dN_over_dt_pi * n_PBH
d_n_K_from_PBH = dN_over_dt_K * n_PBH
d_n_proton_from_PBH = dN_over_dt_proton * n_PBH
d_n_neutron_from_PBH = dN_over_dt_neutron * n_PBH

and then the SAME full pion source is inserted into BOTH pi- and pi+ equations.

The full charged-kaon aggregate is inserted into K-.
The full proton/antiproton aggregate is inserted into pbar.
The full neutron/antineutron aggregate is inserted into nbar.
K0_L is used directly for K0_L.

Therefore B_current is an exact statement about public code semantics.

For pions in particular:

S_pi-^current + S_pi+^current = 2 Q_pipm

if Q_pipm denotes the aggregate pair source.

This is an exact object-map mismatch.

## 4. Status of the half-split B_sym

Mech-S6 writes:

S_pi- = S_pi+ = Q_pipm/2
S_K- = Q_Kpm/2
S_pbar = Q_p+pbar/2
S_nbar = Q_n+nbar/2
S_K0L = Q_K0L.

This is mathematically exact CONDITIONAL ON charge-conjugate equality.

The evidence status must be typed carefully.

### Nucleons

For nucleons, the paper explicitly states equal amounts of nucleons and antinucleons. Therefore the half-split for p/pbar and n/nbar is source-supported directly.

### Charged pions and kaons

The paper explicitly establishes aggregate pi± and K± multiplicities including both particle and antiparticle contributions, but the cited paper sentence does not separately report the two charge-resolved yields.

A 1/2 split is the symmetry-imposed reconstruction under the declared charge-conjugate-neutral source convention. It is not a direct charge-resolved measurement from the aggregate table.

Therefore replace the strongest label

B_SYM = PASS_EXACT_SOURCE_NATIVE

with

B_SYM = PASS_CONDITIONAL_EXACT_UNDER_CHARGE_CONJUGATION_EQUALITY.

For nucleons:
CHARGE_CONJUGATION_EQUALITY = EXPLICIT_SOURCE_STATEMENT.

For pi± and K±:
CHARGE_CONJUGATION_EQUALITY = LEGAL_SOURCE_SYMMETRY ASSUMPTION / NOT INDEPENDENTLY CHARGE-RESOLVED IN THE AGGREGATE TABLE.

This repair does NOT rescue B_current. The current map still assigns an aggregate object directly to individual reaction species without declaring a charge-resolution map.

## 5. Source-interface factor-two statement

Conditional on the symmetric split:

S_current = Q_pair
S_sym = Q_pair/2

for each affected tracked single species.

Therefore:

S_current / S_sym = 2,

relative overcount against the symmetric reference = +100%,

and the repair removes 50% of the currently injected affected-channel source.

This statement is exact at the source interface under the symmetry contract and is mass-independent.

It applies to:
- pi-
- pi+
- K-
- pbar
- nbar.

K0_L is unchanged.

But:

FACTOR_TWO_SOURCE_INTERFACE != FACTOR_TWO A/B != FACTOR_TWO X_n != FACTOR_TWO Y_p != FACTOR_TWO PBH BOUND.

## 6. Common-background response theorem

Freeze the same X_n(t), T(t), n_B(t), the same initial hadron populations, and use the intended floor-inactive linear population equation

dn_h/dt = S_h - D_h n_h.

If S_h is rescaled by constant c, then exactly

n_h^(c) = n_h^hom + c (n_h^old - n_h^hom).

For c=1/2:

n_h^new = (n_h^old + n_h^hom)/2.

This part of Mech-S6 is exact.

Because the directional rates A and B are linear in the hadron populations at a frozen common background, with A0,B0 containing unchanged K0_L plus the homogeneous affected-species contributions:

A_new = (A_old + A0)/2
B_new = (B_old + B0)/2.

Then for F_had=(1-X)A-XB at the SAME supplied X:

F_new = (F_old + F0)/2.

Where R=A+B>0:

R_new = (R_old + R0)/2,

q_new = (A_old + A0)/(R_old + R0).

If R0>0:

q_new-q_old = [R0/(R_old+R0)] (q0-q_old).

These are exact algebraic transformations under the declared common-background/floor-inactive contract.

## 7. Floor guard

The raw Wu–Xu executor uses a log population floor. When floor-active, the effective source term is nonlinear in the source amplitude.

Therefore:

SOURCE HALF-SPLIT != RAW FLOOR-ACTIVE POPULATION HALF-SPLIT.

The common-background linear theorem is NOT automatically a theorem about the raw coupled public execution.

Mech-S6 correctly retains this guard.

## 8. Priority between the two newly exposed source defects

Two distinct issues must remain separate:

A. SUBEDGE PAPER↔PUBLIC-HELPER MISMATCH
- exact source-contract mismatch;
- published-run provenance unresolved;
- strongest direct effect is below 1e9 g and during terminal evolution.

B. CHARGE-PAIR SOURCE-MAP MISMATCH
- visible directly in current public main-scan.jl;
- applies already inside the supported source-table domain;
- therefore applies around 1e9, 2e9 and 6e9 g without invoking terminal extrapolation.

The paper identifies approximately 2e9 g as the point of strongest published sensitivity.

Thus, as a referee priority statement only:

SUPPORTED-DOMAIN OBJECT-MAP MISMATCH has higher immediate evidentiary leverage than refining the lower-mass extrapolation.

This is NOT a task assignment and does NOT imply endpoint materiality.

## 9. Published-result claim ceiling

Current evidence supports:

PUBLIC_CODE_SOURCE_MAP_MISMATCH = HIGH.

It does NOT yet support:

PUBLISHED_BOUND_IS_WRONG.

Why not:
- exact provenance of the published scan is unresolved;
- dynamic floor activity after source repair is not evaluated;
- coupled background response is not run;
- X_n response is not run under corrected source map;
- final modern Y_p / D/H response is not run;
- the paper's stored scan may have been generated with code/state not fully represented by current visible helper history.

Therefore:

PUBLIC_CODE_DEFECT_CANDIDATE != PUBLISHED_NUMERICAL_RESULT_INVALIDATION.

## 10. Additional provenance caution

The public repository contains main-scan.jl and scanning.jld2 in the relevant revision family.

This is material provenance evidence but not enough to infer:

VISIBLE_SOURCE_FILE == EXACT_EXECUTED_SOURCE_FILE

for the published scan.

Do not reverse provenance from co-commit alone.

## 11. Final disposition

PAPER_SUBEDGE_RULE = PASS_SOURCE_NATIVE
PUBLIC_HELPER_SUBEDGE_RULE = PASS_CODE_NATIVE
PAPER_PUBLIC_HELPER_SUBEDGE_CONTRACT_MISMATCH = PASS_EXACT
PUBLISHED_SCAN_SUBEDGE_PROVENANCE = UNRESOLVED

PAIR_AGGREGATE_SOURCE_SEMANTICS = PASS
PUBLIC_B_CURRENT_MAP = PASS_EXACT_CODE_SEMANTICS
CURRENT_AGGREGATE_TO_SINGLE_SPECIES_MAP = HIGH_OBJECT_MAP_MISMATCH

B_SYM_NUCLEON_HALF_SPLIT = PASS_SOURCE_SUPPORTED
B_SYM_PI_K_HALF_SPLIT = PASS_CONDITIONAL_EXACT_UNDER_CHARGE_CONJUGATION_EQUALITY
CHARGE_RESOLVED_PI_K_SOURCE = NOT DIRECTLY STORED IN AGGREGATE TABLE

SOURCE_INTERFACE_FACTOR_TWO = PASS_CONDITIONAL_EXACT
COMMON_BACKGROUND_POPULATION_TRANSFORM = PASS_EXACT_FLOOR_INACTIVE
COMMON_BACKGROUND_A_B_F_TRANSFORM = PASS_EXACT_FLOOR_INACTIVE
RQ_TRANSFORM = PASS_EXACT_WHERE_DEFINED
RAW_FLOOR_ACTIVE_HALF_RESPONSE = NOT_ESTABLISHED
FULL_COUPLED_TARGET_IMPACT = NOT_RUN

PUBLIC_CODE_SOURCE_MAP_MISMATCH = HIGH
PUBLISHED_BOUND_INVALIDATION = NOT_ESTABLISHED
SOURCE_MATCHED_K_PBH = UNDEFINED
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY / NO NEW TASK

STOP after owner integration unless:
- charge-resolved source evidence contradicts the symmetric split,
- published-run provenance resolves the exact executed source map,
- or a corrected dynamic execution produces a target-level result.
