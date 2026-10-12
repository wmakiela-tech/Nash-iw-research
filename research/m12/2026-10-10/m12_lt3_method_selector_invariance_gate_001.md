---
artifact_id: M12-LT3-METHOD-SELECTOR-INVARIANCE-GATE-001
bw_ingestion_event_id: ING-20261010-0071
bw_qualification_state: METHOD_SELECTOR_INVARIANCE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-LT3-METHOD-SELECTOR-INVARIANCE-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - LT3 method-selector invariance gate
RESULT_CLASS
EXACT LOCAL CONTROL / DRAFT011 IDENTIFICATION HARDENING / NO NOVELTY CLAIM
SETUP
Let data y induce scientific identified set:
I(y) subset X.
Let tau:X->T be the declared target.
Let R be a frozen family of admissible METHOD-ONLY procedures/regularizers.
Each r in R selects one point:
s_r(y) in I(y).
The selector may be unique for every r.
CERTIFICATE A - UNIQUE SELECTOR != IDENTIFICATION
Data point-identify tau iff tau is constant on I(y).
A unique selected point s_r(y) says only that one method chose one representative.
It does not change I(y).
Therefore:
UNIQUE OPTIMIZER
!=
DATA POINT IDENTIFICATION.
CERTIFICATE B - METHOD-SELECTION ORBIT
Define method-selection image:
S_R(y)={s_r(y): r in R} subset I(y).
Define method-induced target spread:
D_R^tau(y)
=
sup_{r,r' in R} d_T(tau(s_r(y)),tau(s_r'(y))).
If:
D_R^tau(y)>0,
then the reported target depends on method choice inside the same data fiber.
Therefore a point claim that does not type the method choice is not invariant under the frozen admissible procedure class.
CERTIFICATE C - METHOD ROBUSTNESS IS WEAKER THAN IDENTIFICATION
D_R^tau(y)=0
does NOT imply tau is identified from data.
Reason:
all admissible selectors may choose the same point even though other target-different points remain in I(y).
Exact control:
I(y)=[-1,1],
tau(x)=x,
R contains only the selector s_r(y)=0.
Then D_R^tau=0,
but tau(I(y))=[-1,1].
Thus:
METHOD-INVARIANT SELECTED POINT
!=
DATA IDENTIFIED TARGET.
CERTIFICATE D - SOURCE-SUPPORTED CONSTRAINT
Let C_source subset X be independently source-supported evidence.
Then the scientific identified set becomes:
I_source(y)=I(y) intersect C_source.
Target point identification is earned iff tau is constant on I_source(y).
Contraction caused by C_source is attributable to new evidence.
By contrast, a convenience penalty or numerical tie-breaker does not contract the scientific identified set.
CERTIFICATE E - PRIOR/REGULARIZER PROVENANCE
Every constraint/penalty should be typed as one of:
SOURCE_EVIDENCE;
PHYSICAL_ASSUMPTION;
MODEL_CLASS_DEFINITION;
METHOD_PRIOR;
NUMERICAL_STABILIZER;
UNKNOWN.
Only the first three can change the scientific admissible set, and only within their declared claim scope.
METHOD_PRIOR and NUMERICAL_STABILIZER select/weight points but do not become source evidence by optimization.
CERTIFICATE F - BAYESIAN GUARD
A posterior can be sharply concentrated even when likelihood fibers are nonidentified.
That sharpness may be prior-driven.
Therefore:
POSTERIOR CONCENTRATION
!=
LIKELIHOOD IDENTIFICATION.
Scientific attribution requires separating:
likelihood information;
source-supported prior information;
method-only prior/regularization.
CERTIFICATE G - TARGET-RELATIVE REPORTING
Recommended output hierarchy:
1 DATA_IDENTIFIED_TARGET_SET = tau(I(y));
2 SOURCE_SUPPORTED_TARGET_SET = tau(I_source(y));
3 PROCEDURE_SELECTED_POINT = tau(s_r(y));
4 METHOD_SELECTION_SPREAD = D_R^tau(y);
5 PRIOR/REGULARIZER PROVENANCE.
A point estimate may be reported at layer 3 without promoting layer 1 or 2 to point identification.
PROJECT ROLE
This strengthens DAX-S6 regularization gate without changing its conclusion.
Exact new distinction:
METHOD SELECTION ROBUSTNESS
is neither DATA IDENTIFICATION nor SOURCE-SUPPORTED IDENTIFICATION.
LOWER HOST
Partial identification / regularization / inverse problems / Bayesian prior sensitivity.
CLAIM CEILING
No claim one admissible method family R is canonical.
No claim method sensitivity alone measures full scientific uncertainty.
No novelty inference.
REV020 active / REV021 not created / TPE thin compiler.
