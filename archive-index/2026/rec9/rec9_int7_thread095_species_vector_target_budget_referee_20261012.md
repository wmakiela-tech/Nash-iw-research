# REC9 / INT7 Thread095 species-vector target-budget referee

RETURN_ID: REC9-INT7-THREAD095-SPECIES-VECTOR-TARGET-BUDGET-REFEREE-001
TARGET: INT7-THREAD095-FRONTB-SPECIES-VECTOR-SOURCE-BUDGET-001
VERDICT: PASS_FIXED-LINEAR_SPECIES_BUDGET / REPAIR_SOURCE-REACTION_MAP_AND_KERNEL-FEEDBACK_CLAIM_CEILING
SEVERITY: MEDIUM

## 1. Core fixed-linear theorem — PASS

For a frozen set of source channels h, with
lambda1_h = m_h lambda0_h + lambdaS_h
and fixed real target kernels W_h,

C = sum_h integral W_h d lambda_h

implies exactly

Delta C = sum_h [
  integral W_h(m_h-1)d lambda0_h
  + integral W_h d lambdaS_h
].

With epsilon_h = ess sup |m_h-1|,

|Delta C|
<=
sum_h [
  epsilon_h integral |W_h| d lambda0_h
  + integral |W_h| d lambdaS_h
].

Thus:
NO SINGLE SOURCE-COMPLETE DONOR != NO TARGET CERTIFICATE AUTOMATICALLY

is mathematically correct for a fixed linear target map.

The support-expansion/singular term is correctly retained.

## 2. Main Front-B repair — define the channel index after the source interface

Current Wu-Xu source semantics are not one-to-one identified-species labels.

The public PYTHIA table aggregates:
Q_pipm = pi+ + pi-,
Q_Kpm = K+ + K-,
Q_p/pbar = p + pbar,
Q_n/nbar = n + nbar,
plus Q_K0L.

Downstream reaction equations then use these aggregate columns through a nontrivial source-to-reaction map B.

Therefore the target should first be written schematically as

R = B Q,

then for a fixed linear target functional L,

C = L R = L B Q.

Equivalently the effective source-channel kernel is
W_eff = B^* L
(or the finite-dimensional transpose analogue).

Hence:
DONOR SPECIES INDEX != TARGET REACTION-CHANNEL INDEX AUTOMATICALLY.

INT7's theorem remains exact if h indexes the frozen source columns Q, or if B has already been absorbed into W_h.

This contract must be explicit before applying the species-wise budget to Front B.

## 3. Aggregate column feeding multiple reactions

Because one aggregate source column can feed more than one reaction population, splitting it into multiple h terms without the map B can double-count or incorrectly treat correlated copies as independent source uncertainties.

Example:
the same Q_pipm source is used for both pi- and pi+ populations in the current downstream model.

Therefore:
ONE SOURCE COLUMN -> MULTIPLE REACTION CHANNELS
does not create multiple independent lambda_h.

Preserve the common-source coupling in B.

## 4. Patchwork donors and joint legality

INT7 correctly says patchwork evidence can support a claim-local target certificate if every load-bearing contribution is simultaneously bounded under one legal contract.

Add:
the bounds must be jointly compatible with the same
- PBH primary-parton mixture;
- source normalization;
- energy/support convention;
- source-column aggregation;
- source-to-reaction map B;
- target kernel/trajectory contract.

Individually valid donor bounds that correspond to mutually inconsistent source conventions cannot simply be summed.

Thus:
MARGINAL DONOR VALIDITY != JOINT PATCHWORK LEGALITY.

The simple triangle-sum bound does not require probabilistic independence, but the underlying bounds must refer to one common admissible source model/class.

## 5. Fixed kernel versus coupled BBN dynamics

Thread095 is exact for fixed W_h.

If changing the source changes the BBN trajectory, composition, branching, or reaction kernels, then W_h becomes source-dependent.

The previous Rec9 guard remains:

FIXED-LINEAR SOURCE BUDGET != FULL COUPLED BBN TARGET ERROR.

A full source-to-endpoint certificate then needs either:
- a source-matched secant/adjoint representation;
- a nonlinear stability/small-gain bound;
- or a direct full comparator.

The fixed W_h result remains a valid local/template certificate, not a PBH endpoint bound.

## 6. "Unresolved species may be harmless" — repair wording

Safe form:

An unresolved source channel can be omitted from a claim-local target certificate only if, under the SAME legal source-to-target contract, its contribution is proven:
- identically zero;
- annihilated by the effective kernel;
- or bounded within the declared target tolerance.

A merely small source abundance, weak donor coverage, or presumed symmetry is not enough.

For Wu-Xu specifically, the p/pbar and n/nbar aggregate-to-antinucleon use makes this especially important.

## 7. Multi-target family

For multiple fixed targets j,

|Delta C_j| <= sum_h B_jh

passes.

But:
TARGET-FAMILY COMPLETENESS
requires the same source contract to control every declared target j.

A channel harmless for one endpoint may be load-bearing for another.

Therefore the split
SOURCE COMPLETENESS != TARGET-FAMILY COMPLETENESS
is correct and useful.

## 8. Final status

SPECIES_VECTOR_FIXED_LINEAR_DECOMPOSITION = PASS_EXACT.
ABSOLUTE_SPECIES_TARGET_BUDGET = PASS_EXACT.
SINGULAR_SUPPORT_TERM = PASS_REQUIRED.
NO_SINGLE_DONOR_IMPLIES_NO_CERTIFICATE = REJECTED; INT7 split PASS.
SOURCE_COLUMN_TO_REACTION_MAP_B = REQUIRED_FOR_FRONTB_APPLICATION.
DONOR_SPECIES_EQ_REACTION_SPECIES = NO.
COMMON_SOURCE_COLUMN_COPIES_INDEPENDENT = NO.
MARGINAL_PATCHWORK_BOUNDS_EQ_JOINT_LEGAL_CONTRACT = NO.
FIXED_KERNEL_BUDGET_EQ_FULL_COUPLED_BBN_ERROR = NO.
NEUTRON/K0L OPENNESS = TARGET-RELATIVE, BUT ACTUAL LOAD-BEARING STATUS NOT YET CERTIFIED.
SOURCE_VALID_E2B = OPEN.
TERMINAL_SOURCE_VALIDATION = OPEN.
PBH_DE_DYNAMIC_ACCURACY = OPEN.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NOVELTY = NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
LT4 ACTIVE/APPEARED; MT13 TEMP LT COVERAGE ENDED per current programme state.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration. Reopen only for a frozen source-column->reaction map, source-matched kernels, or a claimed endpoint certificate.
