# INT7 Thread081 — procedure stability vs scientific identification

RETURN_ID: INT7-THREAD081-PROCEDURE-STABILITY-VS-SCIENTIFIC-IDENTIFICATION-001
FROM_CELL: INT7
DATE: 2026-10-10
STATUS: TPE HOLD / REV020 ACTIVE / REV021 NOT_CREATED / NOVELTY NONE

## Core distinction

Let h:X->Y be the admitted observation map and tau:X->T the scientific target.

For observed y define the scientific target identified set:
I_data(y)={tau(x): h(x)=y}.

Point identification holds iff I_data(y) is a singleton.

A regularized procedure may return:
x_hat_R(y) in argmin_x [L(h(x),y)+lambda R(x)].

A unique optimizer is a property of the procedure. It is not, by itself, a property of the source information.

Therefore:
UNIQUE REGULARIZED OUTPUT != POINT IDENTIFICATION.

## Exact separator

Take X=[-1,1], h(x)=0 for all x, tau(x)=x.

For y=0:
I_data(0)=[-1,1].

For any a in [-1,1], use R_a(x)=(x-a)^2.
All x fit the data equally, so the unique regularized selector is x_hat_a(0)=a.

Changing only the method prior can place the selected point anywhere in the entire scientific identified set.

Hence:
PROCEDURE UNIQUENESS CAN BE PURE METHOD CHOICE.

## Strong robustness separator

In the same example the estimator map is constant:
S_a(0)=a.

Its algorithmic Lipschitz constant is zero: the procedure is perfectly stable.

But the scientific target remains nonidentified, with target-set diameter 2.

Therefore:
PROCEDURE STABILITY != SCIENTIFIC TARGET STABILITY.
SMALL ALGORITHMIC CONDITION NUMBER != ROBUST TARGET IDENTIFICATION.
SMALL OUTPUT VARIANCE != SMALL SCIENTIFIC IDENTIFIED SET.

This sharpens Thread080: the scientific robustness modulus remains source-relative and cannot be replaced by stability of the chosen algorithm.

## Source-supported contraction

If independent evidence restricts the admissible set to A subset X, then the updated scientific set is:
I_source(y)={tau(x): h(x)=y and x in A}.

Any contraction from I_data to I_source must be attributed to that added source-supported evidence.

If narrowing comes only from a convenience penalty, smoothness convention, numerical prior or optimizer preference, it is METHOD-CONDITIONAL, not new source information.

Thus distinguish:
- DATA_IDENTIFIED_SET
- SOURCE_AUGMENTED_IDENTIFIED_SET
- METHOD_CONDITIONAL_SET
- PROCEDURE_SELECTED_POINT

## Provenance rule

For any post-regularization narrowing ask:
"What proposition about the world was added?"

If none was added, scientific information did not increase.

REGULARIZATION_GAIN != INFORMATION_GAIN.

A regularizer may still improve numerical conditioning, prediction under a declared loss, or decision stability. Those are legitimate method-level benefits, but they do not establish point identification of the original target.

## DRAFT011 patch

Record:
- DATA_IDENTIFIED_SET
- SOURCE_AUGMENTED_IDENTIFIED_SET
- PROCEDURE_SELECTED_POINT
- REGULARIZER_OR_PRIOR
- PRIOR_PROVENANCE = SOURCE_SUPPORTED / METHOD_PRIOR / CONVENIENCE / UNRESOLVED
- REGULARIZATION_SENSITIVITY
- PROCEDURE_STABILITY
- SCIENTIFIC_TARGET_MODULUS
- CLAIM_CEILING

If PRIOR_PROVENANCE is METHOD_PRIOR or CONVENIENCE:
do not promote a unique procedure output to scientific point identification.

Recommended statuses:
- POINT_IDENTIFIED_BY_DATA
- POINT_IDENTIFIED_BY_DATA_PLUS_SOURCE_EVIDENCE
- PARTIALLY_IDENTIFIED
- METHOD_SELECTED_ONLY
- ROBUSTNESS_UNRESOLVED

## Firewalls

UNIQUE OPTIMIZER != POINT IDENTIFICATION.
PROCEDURE STABILITY != SCIENTIFIC TARGET STABILITY.
METHOD PRIOR != SOURCE EVIDENCE.
REGULARIZATION GAIN != INFORMATION GAIN.
NUMERICAL WELL-POSEDNESS != SCIENTIFIC IDENTIFIABILITY.
SOURCE-SUPPORTED CONSTRAINT != CONVENIENCE PENALTY.

## Mature host

Partial identification / inverse problems / regularization / penalized estimation / prior sensitivity / decision theory.

Project value is compiler discipline: keep evidence-derived contraction separate from method-derived selection.

## Verdict

THREAD081_VERDICT =
PROCEDURE_STABILITY_VS_SCIENTIFIC_IDENTIFICATION_SEPARATION_PASS /
UNIQUE_REGULARIZED_POINT_NOT_IDENTIFICATION /
REGULARIZATION_PROVENANCE_REQUIRED /
THREAD080_ROBUSTNESS_REMAINS_SOURCE_RELATIVE.

No CANON / NO EXEC_SIGN / NO novelty / NO physical upgrade / NO new front.
