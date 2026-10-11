# M12 — Front B DE population tracking: exact residual bound

RESULT_CLASS: EXACT LOCAL CONTROL / SOURCE-NATIVE ERROR BRIDGE / NO NUMERICAL PBH ENDPOINT / NO NOVELTY

## Setup
For one hadron species on one prescribed legal background/state path:
n'(t)=S(t)-D(t)n(t), with D(t)>0.
Define instantaneous DE state n_*(t)=S(t)/D(t) and e(t)=n_*(t)-n(t).

## Exact tracking identity
Since S=D n_*:
n'=D(n_*-n)=D e,
so exactly
e'+D e=n_*'.

Hence
e(t)=exp[-∫_{t0}^t D]e(t0)
+∫_{t0}^t exp[-∫_s^t D] n_*'(s) ds.

Therefore
|e(t)| <= exp[-∫D]|e(t0)|
+∫ exp[-∫_s^t D]|n_*'(s)| ds.

If D>=d_min>0:
|e(t)| <= e^{-d_min(t-t0)}|e(t0)|
+(1-e^{-d_min(t-t0)}) sup|n_*'|/d_min.

Where S,D>0:
n_*'=n_*[(S'/S)-(D'/D)].

Thus the tracking control is variation of the ratio S/D relative to depletion D, not source variation alone.

## Exact limit
If n_*'=0, then e(t)=exp[-∫D]e(t0).
If also e(t0)=0, algebraic DE is exact on that interval.

## Multispecies bridge
For n_h'=S_h-D_h n_h, n_h^DE=S_h/D_h and e_h=n_h^DE-n_h^FULL:
e_h'+D_h e_h=(n_h^DE)'.

Let E_h(t) denote the exact kernel bound above. At common state X:
deltaA=sum_h e_h k_h^pn,
deltaB=sum_h e_h k_h^np,
deltaF_had=(1-X)deltaA-X deltaB.

Hence
|deltaF_had|
<=sum_h E_h[(1-X)k_h^pn+X k_h^np].

This closes the noncircular chain:
independent source/depletion variation
-> population tracking error
-> directional-rate error
-> reduced X_n RHS error.

## Common-path guard
The theorem is exact along one prescribed/common X/background path.
Comparing FULL on X_FULL(t) with DE on X_DE(t) mixes:
A population-tracking error at fixed path,
B state-feedback/path mismatch.

Legal validation order:
1 same X_ref(t);
2 full source-sink integration vs S_h/D_h on that same path;
3 obtain E_h;
4 propagate to deltaF_had;
5 only then propagate into X_n trajectory error.

COMMON TIME != COMMON STATE remains controlling.

If S_h,D_h depend on X, use the TOTAL derivative of S_h/D_h along the chosen common path.

## Claim ceiling
This does not prove PBH B2 waterfall transfer, dynamic X_n accuracy, BBN endpoint accuracy, source-matched K_PBH, or any PBH bound.

STATUS:
INDEPENDENT_POPULATION_ERROR_CERTIFICATE=PASS_EXACT.
SOURCE_NATIVE_ERROR_CHAIN_TO_deltaF=PASS_EXACT.
PBH_DE_DYNAMIC_X_ACCURACY=OPEN.
PBH_B2_WATERFALL_TRANSFER=OPEN.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
