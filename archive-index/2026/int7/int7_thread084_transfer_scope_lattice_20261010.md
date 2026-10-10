# INT7 Thread084 — transfer certificate quantifier lattice

RETURN_ID: INT7-THREAD084-TRANSFER-CERTIFICATE-QUANTIFIER-LATTICE-001
FROM_CELL: INT7
DATE: 2026-10-10

Core result:
Certificate exactness and certificate coverage are independent axes.

For legal error class E, donor certificate V and target error T, define transfer pass on A subset E when every error in A that is invisible to V is also invisible to T.

If A1 is contained in A2, then pass on A2 implies pass on A1. The converse is false.

Exact control:
V(x,y)=x, T(x,y)=y on R^2.
Universal transfer fails because (0,1) is invisible to V but visible to T.
On source family A={(x,0)}, transfer passes.
Therefore:
UNIVERSAL TRANSFER FAIL != SOURCE-FAMILY TRANSFER FAIL.

Certificate scope:
Q0 PAIRWISE
Q1 SOURCE_FAMILY
Q2 REGIME_UNIFORM
Q3 UNIVERSAL_HOST_CLASS

Implication:
Q3 => Q2 => Q1 => Q0.
No converse by default.

Certificate exactness:
EXACT_IDENTITY / SUFFICIENT_BOUND / FIRST_ORDER_LOCAL / EMPIRICAL_BENCHMARK.

An exact pairwise identity can have narrower coverage than a conservative regime-uniform bound.

Therefore:
EXACTNESS != COVERAGE.
PAIRWISE EXACTNESS != SOURCE-FAMILY ADMISSION.
SOURCE-FAMILY PASS != UNIVERSAL HOST THEOREM.
BENCHMARK PASS != REGIME-UNIFORM PASS.
CLAIM SCOPE > CERTIFICATE SCOPE => NOT CERTIFIED.

DRAFT014 fields:
CERTIFICATE_EXACTNESS
CERTIFICATE_SCOPE
LEGAL_ERROR_CLASS
SOURCE_FAMILY_ID
REGIME_DOMAIN
TRANSFER_CONSTANT_OR_MODULUS
TARGET_TOLERANCE
COVERAGE_GAP
ADMISSION_STATUS

Spider spine:
HOST OBJECT -> TARGET DESCENT -> ROBUSTNESS -> SOURCE-MATCHED TRANSFER -> QUANTIFIER-SCOPE MATCH -> CLAIM ADMISSION.

VERDICT:
TRANSFER_CERTIFICATE_QUANTIFIER_LATTICE_PASS /
EXACTNESS_AND_SCOPE_ORTHOGONAL /
SOURCE_FAMILY_RESTRICTION_CAN_RESCUE_TRANSFER /
PAIRWISE_SECANT_NOT_ADMISSION_BY_ITSELF /
DRAFT014_TRANSFER_LAYER_SHARPENED.

REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED / NOVELTY NONE / NO CANON / NO EXEC_SIGN.
