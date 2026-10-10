# INT7 Thread083 — donor-certificate to target descent and admission closure

RETURN_ID: INT7-THREAD083-DONOR-CERTIFICATE-TO-TARGET-DESCENT-001
FROM_CELL: INT7
DATE: 2026-10-10
STATUS: REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED / NOVELTY NONE

## 1. Problem

DRAFT014 currently absorbs generic source-native admission/provenance at the source-contract level.

Geeky-S10 Front B shows a necessary refinement:
a complete provenance/realization-bearing source contract plus a mature donor host does not automatically certify transfer of that host into a new source regime, nor adequacy for the final scientific target.

The missing logical step is not another provenance field. It is a certificate-transfer question.

## 2. Exact certificate-to-target theorem

Let E be the legal approximation/error class between a source-native realization and a donor-host approximation.

Let
V:E -> Q
be the donor validation map/statistic.

Examples:
- integrated channel-count error;
- state residual;
- moment mismatch;
- trajectory norm;
- donor benchmark score.

Let
T:E -> Z
be the declared scientific target-error map.

Then the donor certificate
V(e)=0
guarantees
T(e)=0
for every legal error e in E

IFF

ker(V) intersect E is contained in ker(T).

For linear spaces/maps this is equivalent to:
T factors through V on span(E),
i.e. there exists L on im(V) such that
T = L o V
on the legal error space.

Therefore:

DONOR VALIDATION CERTIFICATE -> TARGET CERTIFICATE

only when the target descends through the donor validation object on the legal source-error class.

## 3. Exact Front-B specialization

Let e_c(t)=u_c^exact(t)-u_c^DE(t).

Suppose donor validation certifies only equal integrated channel count:
V_c(e_c)=integral e_c(t) dt = 0.

Let the final-target linearized error be:
T_c(e_c)=integral w_c(t) e_c(t) dt.

Then V_c(e)=0 implies T_c(e)=0 for all legal zero-count errors

IFF w_c(t) is constant on the legal support, modulo directions excluded from E.

Exact counterexample:
choose e with positive mass early and equal negative mass late.
Then integral e dt=0,
but if w changes with time,
integral w e dt can be nonzero.

Hence:
EXACT TOTAL CHANNEL COUNT != EXACT FINAL TARGET
unless target sensitivity factors through channel totals.

This is the abstract form of the M12/Mech target-weighted Front-B repair.

## 4. Quantitative version

Let ||V(e)||_Q be the donor validation error measure and ||T(e)||_Z the target error.

A quantitative donor-to-target guarantee exists when there is finite C such that:
||T(e)||_Z <= C ||V(e)||_Q
for all legal e in E.

Equivalently, the induced target map on the validation quotient is continuous/bounded.

If no finite C exists, arbitrarily small donor-validation error can coexist with large target error.

Therefore:
SMALL DONOR ERROR != SMALL TARGET ERROR
without a target-transfer modulus/condition constant.

## 5. Admission closure stack

Source-native scientific admission should be separated into:

A. CONTRACT COMPLETENESS
- source equations;
- regime/domain;
- provenance;
- source witness;
- dependence/ancestry;
- realization/intervention/measurement semantics.

B. HOST TRANSFER VALIDITY
- donor theorem/approximation assumptions hold in the source-native regime;
- or a source-matched approximation/error theorem is supplied.

C. CERTIFICATE-TO-TARGET DESCENT
- declared target error factors through, or is quantitatively controlled by, the donor validation object on the legal error class.

D. CLAIM THRESHOLD
- resulting target error is below the frozen scientific/decision tolerance.

Only A-D together close admission for the declared claim.

## 6. Reconciliation of DRAFT014 and Geeky

DRAFT014 remains correct if:
ABSORB_AT_SOURCE_CONTRACT_LEVEL
is read as
SOURCE CONTRACT + MATCHED HOST + EXPLICIT TRANSFER/TARGET CERTIFICATES.

It is too strong if read as:
PROVENANCE/REALIZATION METADATA ALONE IS SUFFICIENT.

Thus:

SOURCE CONTRACT COMPLETENESS != HOST TRANSFER VALIDITY.

HOST TRANSFER VALIDITY != TARGET ADEQUACY.

DONOR BENCHMARK PASS != SOURCE-MATCHED CLAIM PASS.

## 7. Generic compiler consequence

Every host-transfer claim should state:

DONOR_VALIDATION_OBJECT
LEGAL_ERROR_CLASS
SOURCE_REGIME
TRANSFER_ASSUMPTIONS
TARGET_ERROR_OBJECT
CERTIFICATE_TO_TARGET_DESCENT
QUANTITATIVE_TRANSFER_CONSTANT_OR_MODULUS
TARGET_TOLERANCE
ADMISSION_STATUS

If CERTIFICATE_TO_TARGET_DESCENT is unresolved:
SOURCE_ADMISSION = UNRESOLVED
even if donor validation and provenance both pass.

## 8. Relation to earlier INT7 threads

Thread076:
HOST EQUIVALENCE != TARGET EQUIVALENCE without target descent.

Thread080:
exact faithfulness does not imply robust faithfulness without distortion control.

Thread083:
DONOR VALIDATION != TARGET VALIDATION unless target error descends through the donor certificate on the legal source-error class.

These are one Spider spine:
HOST-CONTROLLED OBJECT
-> TARGET DESCENT
-> QUANTITATIVE ROBUSTNESS
-> SOURCE-MATCHED TRANSFER.

## 9. Programme placement

The theorem itself is mature quotient/factorization/functional-analysis logic.

Scientific value is claim-local:
it tells the project exactly when a mature donor validation can and cannot be exported to a source-native target.

No new general TPE mathematics follows.

Front B remains:
PBH_B2_TO_DE_ADMISSION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO numerical PBH/BBN bound.

## 10. Firewalls

SOURCE CONTRACT COMPLETENESS != HOST TRANSFER VALIDITY.
HOST TRANSFER VALIDITY != TARGET ADEQUACY.
DONOR-REGIME VALIDATION != SOURCE-REGIME VALIDATION.
UPSTREAM CERTIFICATE EXACTNESS != DOWNSTREAM TARGET EXACTNESS.
SMALL DONOR ERROR != SMALL TARGET ERROR.
ARCHITECTURAL COMPATIBILITY != SOURCE ADMISSION.
CERTIFICATE PASS != CLAIM PASS unless target descent is established.

## 11. Verdict

THREAD083_VERDICT =
CERTIFICATE_TO_TARGET_DESCENT_PASS /
DRAFT014_CONTRACT_ABSORPTION_NARROWED_NOT_REJECTED /
HOST_TRANSFER_AND_TARGET_ERROR_CERTIFICATES_LOAD_BEARING /
FRONTB_REMAINS_OPEN /
NO_NEW_GENERAL_THEORY.

No CANON / NO EXEC_SIGN / NO novelty / NO physical upgrade / NO new front.
