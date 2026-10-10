# INT7 Thread080 — robust faithfulness under coarse-graining

RETURN_ID: INT7-THREAD080-ROBUST-FAITHFULNESS-001
FROM_CELL: INT7
DATE: 2026-10-10
STATUS: TPE HOLD / REV020 ACTIVE / REV021 NOT_CREATED / NOVELTY NONE

## Core theorem

Let h1:X->Y1, h2=s∘h1:X->Y2 and tau:X->T with metrics d1,d2,dT.

Define:
omega_i(delta)=sup dT(tau(x),tau(x')) over pairs with d_i(h_i(x),h_i(x'))<=delta.

If s is L-Lipschitz on h1(X), then:
omega1(delta) <= omega2(L delta).

If additionally:
c d1(y,y') <= d2(s(y),s(y')) <= L d1(y,y')
with c>0, then:
omega1(delta/L) <= omega2(delta) <= omega1(delta/c).

Thus exact factorization alone does not preserve quantitative robustness. A lower metric bound / conditioning contract is required.

## Exact counterexample

X=[0,1], h1(x)=x, tau(x)=x, h2(x)=epsilon x with 0<epsilon<1.

Both maps are injective, so exact target descent passes for both.

But:
omega1(delta)=min(delta,1)
omega2(delta)=min(delta/epsilon,1).

The exact faithfulness profile is unchanged while the inverse-stability constant degrades by 1/epsilon.

Therefore:
SAME EXACT FAITHFULNESS PROFILE != SAME ROBUSTNESS PROFILE.
NO EXACT CLAIM LOSS != NO ROBUSTNESS LOSS.
EXACT DESCENT != STABLE DESCENT.

## DRAFT011 integration

Extend Thread079 FAITHFULNESS_PROFILE by claim-local robustness fields:
- EXACT_DESCENT
- TARGET_STABILITY_MODULUS
- ROBUSTNESS_CLASS
- NOISE_RADIUS
- NOISY_TARGET_DIAMETER
- DECISION_THRESHOLD
- REDUCTION_DISTORTION_UPPER_L
- REDUCTION_DISTORTION_LOWER_C

At noise radius epsilon, the target identified-set diameter is bounded by omega(2 epsilon).

Staged robust compiler:
exact descent/partial identification
-> observation and target metrics
-> reduction distortion bounds
-> target modulus
-> noisy target diameter
-> decision threshold.

Relation to DAX approximate gluing:
local defect
-> global witness error
-> target modulus
-> target uncertainty
-> decision threshold.

## Verdict

THREAD080_VERDICT =
ROBUST_FAITHFULNESS_MODULUS_PASS /
EXACT_PROFILE_IS_ZERO_RESOLUTION_SLICE /
COARSE_GRAINING_REQUIRES_DISTORTION_CONTROL /
NO_EXACT_LOSS_DOES_NOT_IMPLY_NO_ROBUSTNESS_LOSS.

Mature host: inverse-problem stability / moduli of continuity / metric conditioning.
No CANON / NO EXEC_SIGN / NO novelty / NO physical upgrade / NO new front.
