# REC9 Geeky-S10 signed-kernel source-stress referee

RETURN_ID: REC9-GEEKY-S10-SIGNED-KERNEL-SOURCE-STRESS-REFEREE-001
TARGET: GEEKY-S10-DRAFT018-FRONTB-SIGNED-TARGET-KERNEL-SOURCE-STRESS-CONDITIONING-GATE-001
VERDICT: PASS_AC-PERTURBATION_THEOREM / REPAIR_ABSOLUTE-CONTINUITY_AND_SINGULAR-SUPPORT_CLAIM_CEILING
SEVERITY: HIGH

## 1. Core theorem on common support — PASS

Let lambda0 be the positive baseline source measure and suppose the stressed source is absolutely continuous with respect to lambda0:

lambda1 = m lambda0, m>=0.

For a fixed real signed kernel W,

C0 = integral W dlambda0,
C1 = integral W m dlambda0,

so

Delta C = integral W(m-1) dlambda0.

If epsilon_inf = ess sup_{lambda0}|m-1|, then

|Delta C| <= epsilon_inf integral |W| dlambda0.

If C0 != 0, define

kappa = [integral |W| dlambda0]/|integral W dlambda0|.

Then

|Delta C|/|C0| <= kappa epsilon_inf,

and kappa epsilon_inf < 1 is a valid sufficient sign-preservation condition.

Jordan/cancellation analysis, the near-cancellation counterexample, the positive-weight kappa=1 special case, and the species-resolved sum bound all pass under the same common-support assumptions.

## 2. Main repair — multiplicative ratio requires absolute continuity

Writing q1/q0=m is not merely notation. It assumes the alternative source measure is absolutely continuous with respect to the baseline source measure.

If the alternative source creates weight on a region where the baseline source is zero, no finite m on lambda0 can represent that contribution.

This is directly relevant after XH-S3 harvest 024:
extending BlackHawk/PYTHIA support can introduce physically admitted source contribution outside the current baseline support.

Therefore:

SOURCE-RATIO ENVELOPE
!=
ARBITRARY SOURCE PERTURBATION.

The present theorem controls only AC perturbations on baseline support.

## 3. Correct general measure decomposition

For an arbitrary positive alternative source measure, use the Lebesgue decomposition

lambda1 = m lambda0 + lambda_s,

where lambda_s is singular with respect to lambda0.

For fixed W:

C1-C0
=
integral W(m-1) dlambda0
+
integral W dlambda_s.

Hence a safe absolute certificate is

|Delta C|
<=
epsilon_inf integral |W| dlambda0
+
integral |W| dlambda_s.

The second term is invisible to the original epsilon_inf ratio bound.

Thus:
SMALL MULTIPLICATIVE ERROR ON OLD SUPPORT
!=
SMALL TOTAL SOURCE ERROR
when new support can appear.

## 4. Nonlinear/kernel-changing case

If the kernel also changes from W0 to W1, the complete decomposition is

C1-C0
=
integral W0(m-1) dlambda0
+
integral (W1-W0)m dlambda0
+
integral W1 dlambda_s.

Geeky-S10 includes the first two terms but omits the singular-support term because its setup silently assumes lambda_s=0.

Therefore the current nonlinear decomposition is exact only under:
lambda1 << lambda0.

## 5. Conditioning notation repair

kappa is not a property of W alone.

It depends on the pair (W,lambda0):

kappa_{W,lambda0}
=
[integral |W| dlambda0]/|integral W dlambda0|.

Changing the baseline source weighting can change cancellation and therefore kappa even with the same mathematical kernel W.

Recommended guard:

KERNEL SHAPE != CONDITION NUMBER WITHOUT BASELINE SOURCE MEASURE.

The notation kappa_W is acceptable only if lambda0 is frozen in the contract.

## 6. Sharpness ceiling

For arbitrary measurable multiplicative stresses satisfying |m-1|<=epsilon and m>=0, the absolute bound is sharp in the usual sign-alignment sense when epsilon<=1.

For epsilon>1, nonnegativity m>=0 prevents unrestricted negative sign-alignment, so the same bound remains valid but generic sharpness is not automatic.

Geeky already states epsilon<=1 in its sharpness sentence; retain this qualifier.

## 7. Front B consequence

Current E0/E1a/E1b comparisons on a shared admitted mass/energy support can use the multiplicative theorem if:
- baseline source is positive where ratios are formed;
- one global finite-window ratio envelope is available;
- kernels are fixed or kernel feedback is separately controlled.

But XH024 shows a future source-complete E2 may enlarge the legal energy/hadronization support.

Then the correct target certificate must include the singular/new-support contribution explicitly.

This makes absolute budgets even more important:
a tiny epsilon_inf on the old support does not control newly admitted high-energy source mass.

## 8. Species-resolved version

For each species h, write

lambda1,h = m_h lambda0,h + lambda_s,h.

Then under fixed species kernels:

|Delta C|
<=
sum_h [
epsilon_h integral |W_h| dlambda0,h
+
integral |W_h| dlambda_s,h
].

Thus:
TOTAL HADRON SOURCE AGREEMENT != SPECIES-RESOLVED TARGET AGREEMENT,
and additionally:
OLD-SUPPORT SPECIES AGREEMENT != NEW-SUPPORT SPECIES CONTROL.

## 9. Final status

SIGNED_KERNEL_AC_SOURCE_STRESS_GATE = PASS_EXACT.
ABSOLUTE_BOUND_ON_COMMON_SUPPORT = PASS_EXACT.
RELATIVE_CONDITIONING_BOUND = PASS_EXACT_IF_C0_NONZERO.
SIGN_PRESERVATION_CRITERION = PASS_SUFFICIENT.
CANCELLATION_COUNTEREXAMPLE = PASS.
POSITIVE_WEIGHT_SPECIAL_CASE = PASS.
ARBITRARY_SOURCE_PERTURBATION_CLAIM = TOO_BROAD.
ABSOLUTE_CONTINUITY_lambda1_LL_lambda0 = REQUIRED_FOR_ORIGINAL_FORM.
SINGULAR_NEW_SUPPORT_TERM = REQUIRED_WHEN_SUPPORT_EXPANDS.
NONLINEAR_DECOMPOSITION_WITHOUT_SINGULAR_TERM = CONDITIONAL_ONLY.
KAPPA_INTRINSIC_TO_KERNEL = NO; BASELINE-MEASURE DEPENDENT.
FRONTB_SOURCE_TO_TARGET_VALIDATION = OPEN_SOURCE_MATCHED.
TERMINAL_SOURCE_PHYSICAL_VALIDATION = OPEN.
PBH_DE_DYNAMIC_ACCURACY = OPEN.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NOVELTY = NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration. Reopen only for a support-expanding E2, a source-matched kernel, or a stronger target-error claim.
