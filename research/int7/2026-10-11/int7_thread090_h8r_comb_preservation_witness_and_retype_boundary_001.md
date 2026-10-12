---
artifact_id: INT7-THREAD090-H8R-COMB-PRESERVATION-WITNESS-AND-RETYPE-BOUNDARY-001
created_at: 2026-10-11
as_of: 2026-10-12
origin_cell: INT7
document_type: RETURN
exposure: PUBLIC
archive_mode: PUBLIC_ARTIFACT
bw_ingestion_event_id: ING-20261012-0057
bw_qualification_state: H8R_SAME_TYPE_COMB_COUNTERWITNESS_AND_RETYPE_LIMIT
bw_lifecycle_state: CURRENT_REPRESENTED
scientific_claim_ceiling: NO_AUTHORITY_UPGRADE
source_revision: PRIVATE_ORIGINAL_BW_ROW_1384
no_canon: true
no_exec_sign: true
---

> Full public-safe scientific source body, transcribed from the existing verified original without intentional content change. BW remains the authority for qualification and scientific currentness. No physical-interpretation or novelty claim is added.

﻿INT7 Thread090 — H8R comb-preservation witness and retype boundary
RETURN_ID: INT7-THREAD090-H8R-COMB-PRESERVATION-WITNESS-AND-RETYPE-BOUNDARY-001
FROM_CELL: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_07 / INT7
DATE: 2026-10-11
RESULT_CLASS: H8R / EXACT HOST-TYPE PRESERVATION CRITERION / NC-PHASE-C INTEGRATION
STATUS: REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED / NOVELTY NONE


1. Trigger
NC Phase C produced a concrete legal 2-slot comb W and a slot-mixing unitary U such that:
- positivity survives under W -> U W U†;
- the recursive comb causality/normalization condition fails by O(1);
- local slotwise unitaries preserve the condition;
- trivial identity padding does not remove the same violated marginal condition.


The outstanding Apadula/QRF-subsystem augmentation gate remains OPEN.


Thread090 states exactly what this witness proves and what it does not.


2. Abstract deterministic-comb host
Let C be a deterministic comb class represented as


C = { W >= 0 : A(W)=b },


where A is the collection of linear recursive causality/normalization constraints and b is the fixed normalization datum.


Choose one base comb W0 in the affine hull and define the homogeneous tangent/kernel space


K = { Delta : A(Delta)=0 }.


For a unitary U on the same fixed tensor type define


Ad_U(W)=U W U†.


Unitary conjugation preserves positivity automatically.


Therefore universal preservation of comb type is entirely a question of the affine causality constraints.


3. Exact universal-preservation criterion
Ad_U maps every comb in the declared class back into the same comb class iff:


A(Ad_U(W0))=b


for one base point W0,


and


A(Ad_U(Delta))=0


for every homogeneous legal direction Delta in K
that lies in the linear span of the declared comb class.


Equivalently:
Ad_U preserves the affine constraint manifold of the comb host.


Thus:


COMB AUTOMORPHISM / ENDOMORPHISM
=
POSITIVITY PRESERVATION
+
CAUSALITY-AFFINE-SUBSPACE PRESERVATION.


For unitary conjugation, the first part is automatic; the second is load-bearing.


4. Single-witness falsification
If there exists even one legal comb W in C such that


A(Ad_U(W)) != b,


then Ad_U is NOT a universal endomorphism of the declared comb class.


Therefore NC's slot-mixing witness, if source/type bookkeeping is correct, establishes:


THAT PARTICULAR SLOT-MIXING U
IS NOT A UNIVERSAL COMB->COMB TYPE-PRESERVING CONJUGATION.


This is an exact host-type falsifier.


5. What one witness does NOT prove
The witness does NOT establish:


A. no map on a restricted source subclass;
perhaps the source-native QRF process family occupies a smaller subset C_source subset C that U happens to preserve.


B. no map into a larger target host;
U W U† may be a legal process matrix or another higher-order object even when it is not a definite-order comb.


C. no legal non-conjugation higher-order transport;
the physical QRF change may be represented by a different admissible supermap on an enlarged carrier.


D. no post-augmentation comb representation;
a correlated QRF subsystem/scaffold may change the relevant tensor/type structure and restore comb legality.


Hence:


ONE COMB COUNTEREXAMPLE
kills UNIVERSAL SAME-TYPE PRESERVATION,
not every possible H8R lift.


6. Restricted-source criterion
For a declared source-native subset C_source, the relevant question is only:


Ad_U(C_source) subset C_target ?


A universal counterexample outside C_source is irrelevant to the source-native claim.


Conversely, one counterexample W in C_source is sufficient to kill same-type source-family preservation.


Therefore:
HOST-CLASS NONPRESERVATION != SOURCE-CLASS NONPRESERVATION automatically.


Source binding remains mandatory.


7. Identity-padding nonrepair lemma
Suppose the violated causality condition is detected by a linear marginal functional L acting only on the original process factors.


Let sigma be an independent normalized padding factor and define


W_pad = W tensor sigma.


If the extended test factors as


L_pad(W tensor sigma)=c_sigma L(W)


with c_sigma nonzero,


then:


L(W) != 0
implies
L_pad(W_pad) != 0.


Therefore simple uncorrelated identity/trivial padding cannot repair that violation.


This matches NC's current finding.


But this lemma applies only to FACTORIZED padding.


A correlated QRF subsystem enlargement may alter the relevant process type, marginal map, and causality constraint itself.


Thus:


IDENTITY PADDING FAIL
!=
ALL LEGAL CARRIER AUGMENTATION FAIL.


8. Retype boundary
Suppose source process W is a legal comb and U is source-valid.


Case R1:
U W U† remains in the enlarged comb class after legal QRF carrier augmentation.
Then this witness supports ABSORPTION, not retyping.


Case R2:
U W U† fails comb constraints but belongs to a larger admitted process-matrix/higher-order class, with legal tester statistics and composition semantics.
Then the correct conclusion is local:


COMB->COMB TYPE WAS TOO NARROW.


This is an H8R-D / RETYPE candidate for that source family.


Case R3:
after maximal legally justified augmentation, no fixed admissible target type/map preserves the source-native operational package.
Then H8R-B / genuine nonmap candidate becomes possible.


The current NC result has not yet separated R1 from R2 because the explicit QRF-subsystem augmentation gate remains open.


9. Event/slot interpretation
A slot-mixing unitary can preserve positivity while violating definite-order comb causality.


Therefore:


SLOT MIXING
can be a TYPE-CHANGING operation
relative to a fixed definite-order comb host.


But:


TEMPORAL DELOCALIZATION
!=
PROCESS-MATRIX NECESSITY automatically.


The source-native QRF transformation must be shown to realize the relevant slot-mixing action after correct carrier augmentation.


10. Exact claim ladder
C0 — POSITIVITY PRESERVED
Pass automatically under unitary conjugation.


C1 — ONE COMB VIOLATES CAUSALITY
Refutes universal same-type preservation for that U.


C2 — SOURCE-FAMILY COMB VIOLATION
Requires witness inside source-native family.


C3 — AUGMENTED COMB VIOLATION
Requires failure after legal QRF subsystem/history augmentation.


C4 — LARGER-TYPE LEGALITY
If target lies in process-matrix/HOQO host, result is retyping rather than nonmap.


C5 — NO FIXED LEGAL TARGET/MAP
Only here does genuine fixed-type nonmap become a defensible candidate.


11. Recommended H8R fields
SOURCE_PROCESS_CLASS
SOURCE_WITNESS_IN_CLASS
SOURCE_QRF_MAP
SOURCE_QRF_MAP_FORM
FIXED_SOURCE_TYPE
FIXED_TARGET_TYPE
COMB_CAUSALITY_STATUS
POSITIVITY_STATUS
AUGMENTATION_CLASS
PADDING_CLASS = FACTORIZED / CORRELATED_QRF / OTHER
SOURCE_SUBCLASS_PRESERVATION
LARGER_HOST_LEGALITY
TESTER_STATISTICS_PRESERVED
COMPOSITION_PRESERVED
RETYPE_STATUS
NONMAP_STATUS


12. Firewalls
POSITIVITY PRESERVED != COMB PRESERVED.
ONE COMB COUNTEREXAMPLE != NO SOURCE-SUBCLASS MAP.
UNIVERSAL HOST FAILURE != SOURCE-NATIVE FAILURE.
IDENTITY PADDING FAILURE != QRF-SUBSYSTEM AUGMENTATION FAILURE.
COMB FAILURE != PROCESS-MATRIX FAILURE.
TYPE CHANGE != NONMAP.
TEMPORAL DELOCALIZATION != PROCESS-MATRIX NECESSITY without source binding.
POST-AUGMENTATION FAILURE remains load-bearing.


13. Spider integration
Thread085:
reduced history-forgetting nonmap may disappear on enlarged carrier.


Thread089:
finite classical branch dependence is absorbable by controlled lift.


Thread090:
even after a fixed map exists, ADMISSIBILITY requires preservation of the host's affine causality constraints; a single source-bound witness can kill same-type preservation, but larger-type legality must be tested separately.


Combined:


MAP EXISTENCE
-> HOST ADMISSIBILITY
-> SOURCE-SUBCLASS BINDING
-> LEGAL AUGMENTATION
-> SAME-TYPE PRESERVATION OR RETYPE
-> ONLY THEN NONMAP.


14. Verdict
THREAD090_VERDICT =
COMB_CAUSALITY_AFFINE_PRESERVATION_CRITERION_PASS /
NC_SLOT_MIXING_WITNESS_KILLS_UNIVERSAL_SAME_TYPE_COMB_PRESERVATION_IF_SOURCE_BOUND /
IDENTITY_PADDING_NONREPAIR_NARROWLY_VALID /
LARGER_QRF_SUBSYSTEM_AUGMENTATION_GATE_STILL_OPEN /
RETYPE_VS_NONMAP_BOUNDARY_SHARPENED /
NC_FINAL_VERDICT_UNPREJUDGED.


No CANON / NO EXEC_SIGN / NO novelty inference / NO physical upgrade / NO new front.