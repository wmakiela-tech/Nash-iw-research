# REC9 / NC H8R PHASE-F VERDICT REFEREE

RETURN_ID: REC9-NC-H8R-PHASEF-VERDICT-REFEREE-001  
TARGET: NC-LT3-H8R-FIXED-TYPE-HIGHER-ORDER-LIFT-DEEP-ATTACK-001 / PHASE F  
VERDICT: PASS_SOURCE_RECONSTRUCTION / REJECT_PRIMARY_H8R-D / RETYPE_PRIMARY_TO_H8R-C / KEEP_RECIPE-OPERATOR_GUARD_WITH_REPAIR  
SEVERITY: HIGH

## 1. Primary verdict repair

NC's source reconstruction materially improves the H8R question, but the evidence does not establish H8R-D as the primary Phase-F verdict.

The original mission asks for ONE intervention-independent admissible HIGHER-ORDER MAP L on one fixed augmented type, not for one identical output operator for every history.

Baumann-Lock gives a source-defined frame-change construction
S_i->j(C) = R_j(C) R_i^{-1}(C),
where R_i^{-1}(C) contains delta(C) and the constraint C contains dynamically embedded interventions.

This proves:
SOURCE-DEFINED FRAME-CHANGE OUTPUT DEPENDS ON THE CONSTRAINT/INTERVENTION PACKAGE.

It does NOT prove:
NO SINGLE HIGHER-ORDER MAP EXISTS.

A higher-order map is itself a rule acting on process-like objects. Its output is expected to depend on its input. Therefore the existence of one uniform recipe C -> S(C) is compatible, in principle, with the mission's EXISTS L FOR ALL h requirement if C/history/intervention data are part of the declared input object.

The unresolved question is whether that recipe can be typed as one admissible higher-order transformation on the legally augmented mixed/open package, co-transporting process, tester/event typing, composition, probabilities and access/discard semantics.

That is exactly a SOURCE_INTERFACE_UNRESOLVED condition.

PRIMARY REC9 VERDICT:
H8R-C = SOURCE_INTERFACE_UNRESOLVED.

H8R-D is not earned from recipe/operator dependence alone.

## 2. Correct guard

Retain:
INTERVENTION-INDEPENDENT RECIPE != INTERVENTION-INDEPENDENT OUTPUT OPERATOR.

Add the more load-bearing reciprocal guard:
FIXED HIGHER-ORDER MAP != FIXED OUTPUT OPERATOR.

Uniformity must be tested at the map/type level:
the same admissible L must act on every legal augmented input package.

Do not require L(P_h) to be independent of h.

## 3. Exact missing source/type object

To decide H8R-A vs H8R-B after H8R-C is resolved, one needs a source-native typed object/package P_aug and an admissibility notion for

L : P_aug -> P_aug',

where P_aug includes:
- constrained process/constraint data;
- finite-resource frame;
- environment/memory;
- dynamically embedded interventions/tester family;
- event/slot structure;
- composition;
- access/discard map.

Missing load-bearing source statement:
whether the Baumann-Lock/related QRF transformation extends to a single admissible higher-order map on the GENERAL MIXED/OPEN MULTI-TIME package with those semantics.

This is the same surviving PRF10 item-I residual already marked NOT SHOWN ABSORBED.

## 4. Causal-order threshold repair

Baumann-Lock does support a source-native overlap criterion:
if the non-negligible range of the clock-relative delocalization phi(t2) is larger than |tau_a-tau_b|, both operation orders contribute.

But the paper phrases this in terms of a "non-negligible range"; it does not define a universal scalar width producing an exact dimensionless threshold.

Therefore reject as too strong:
width/|Delta tau| <= 1 => comb type exact,
width/|Delta tau| > 1 => process-matrix type exact.

Safer typing:
ORDER_MIXING_SUPPORT/WEIGHT = source-native object.

For exact type claims:
- exact definite order requires the order-reversing region to have zero admitted weight/support under the declared model;
- approximate definite order requires a declared tolerance on that weight;
- non-negligible overlap supports indefinite ordering in the source model;
- process-matrix representation/type requires its own legal construction or host theorem.

For distributions with noncompact tails, a practical "non-negligible range" is tolerance-dependent; it is not an exact sharp support threshold.

## 5. Normalizability claim

The source does support that perfectly synchronized ideal clocks of delta-correlated relative time are non-normalizable and normalizable physical states require some temporal delocalization.

Keep:
ZERO DELOCALIZATION IS EXCLUDED IN THE IDEAL-CLOCK SETTING.

Do not conflate this with the separate appendix statement that perfectly delta-timed interventions are distributionally ill-defined.

CLOCK-RELATIVE DELTA CORRELATION != INTERVENTION DELTA COUPLING.

## 6. NC computed comb witness

NC's finite comb witness can support only:
a particular slot-mixing transformation can preserve positivity while violating recursive comb normalization, and uncorrelated identity padding need not repair that witness.

It does not show:
- the transformation is the exact source-native QRF map;
- all legal carrier enlargements fail;
- the mixed/open residual survives.

NC already demotes it to theorem armor/prior-art witness. Rec9 agrees.

## 7. H-4/H-6 disposition

H-4 retraction is correct: arbitrary Hermitian V was not the source-native intervention object once the Baumann-Lock Stinespring-dilation construction is used.

H-6 does not reach the mission bar. State-level purification/discard non-descent is not a process-level non-map witness.

These negative findings support narrowing but do not establish H8R-D.

## 8. Programme effect

CURRENT_SHARP_H8R_RESIDUAL remains:
GENERAL MIXED/OPEN MULTI-TIME PROCESS
+
FRAME-DEPENDENT TESTER/EVENT TRANSPORT
+
ACCESS/DISCARD/COMPOSITION SEMANTICS.

Status:
SOURCE_INTERFACE_UNRESOLVED / NOT SHOWN ABSORBED.

No exact post-augmentation non-map exists in the present record.
No broad absorption theorem exists in the present record.

Therefore:
H8R-A = NOT ESTABLISHED.
H8R-B = NOT ESTABLISHED.
H8R-C = PRIMARY.
H8R-D = NOT ESTABLISHED AS PRIMARY; local retyping issues exist but do not dissolve the higher-order-map question.

## 9. Final status

BAUMANN_LOCK_SOURCE_RECONSTRUCTION = PASS.
CONSTRAINT_DEPENDENCE_OF_SOURCE_FRAME_CHANGE = PASS.
RECIPE_VS_OUTPUT_OPERATOR_GUARD = PASS_WITH_HIGHER_ORDER_MAP_REPAIR.
NO_FIXED_OPERATOR_EXISTENCE_CLAIM = NOT PROVEN.
H8R-D_PRIMARY = REJECTED.
H8R-C_PRIMARY = PASS / SOURCE_INTERFACE_UNRESOLVED.
WIDTH_RATIO_EXACT_THRESHOLD = REJECTED_AS_OVERSTRONG.
SOURCE_ORDER_OVERLAP_CONDITION = PASS.
PROCESS_MATRIX_TYPE_FROM_GENERIC_OVERLAP = NOT AUTOMATIC.
COMB_SLOT_MIXING_WITNESS = PASS_AS_RESTRICTED_THEOREM_ARMOR.
MIXED_OPEN_BRANCH = OPEN.
NOVELTY_CANDIDATE = NONE.
P2/P3 = NO MOVEMENT.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after owner integration. Reopen only if a typed mixed/open higher-order QRF map is constructed, an exact post-augmentation non-map is supplied, or the source interface is materially clarified.
