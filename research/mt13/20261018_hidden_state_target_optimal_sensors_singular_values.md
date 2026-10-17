# MT13 — Target-relative optimal linear measurements of a hidden initial state

**DATE:** 2026-10-18  
**RETURN_ID:** MT13-HIDDEN-STATE-TARGET-OPTIMAL-SENSORS-KWIDTH-001_20261018  
**CLASS:** exact finite-dimensional linear minimax / classical SVD and optimal recovery / science-programme bridge  
**STATUS:** FOUNDATION-LEVEL / NO NOVELTY / NO CANON / NO EXEC / NO QUANTUM PROCESS OR PHYSICAL ADMISSION.

## Primary project sources and placement

LT4's source-native mathematical construction:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt4/2026-10-17/lt4_hidden_state_target_minimax_gramian_001.md

LT4 defines hidden preparation y in a Hilbert ball ||y||<=R, a fixed endpoint-target map M_T=GP exp(T L) J_Y and known term K_T x0. Without additional information, exact worst-case endpoint-target error is R||M_T||. PRF11's consolidated source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-18/IW_PRF11_FOUNDATION_IDENTIFIABILITY_DECISION_MEMORY_REPORT_001_20261018.md
distinguishes target-relative sufficiency, law-identifiability and finite-sample decision risk.

**This note adds a finite-budget intervention-free measurement-design comparison.** No claim that any specified physical instrument can measure these linear forms, no transfer to quantum combs, no prior-art novelty.

## Exact theorem — fixed measurement map

Let Y=R^n or C^n, Z=R^m or C^m with Euclidean norms. Let M:Y->Z be a known linear target map, y unknown with ||y||<=R, R>0, and let an exact noiseless pre-target measurement return b=Ly, where L:Y->F^k is any linear map. The known baseline Kx0 is suppressed. Define the minimax worst-case reconstruction risk
E(L)= sup_{||y||<=R} inf_{estimator evaluated at b=Ly} ... more precisely
E(L)= inf_{a:ran(L)->Z} sup_{||y||<=R} ||My-a(Ly)||.
Then:
**E(L)=R ||M restricted to ker L|| = R||M P_ker L||.**

Proof lower bound: b=0 is produced by any y in ker L of radius<=R. For opposite y,-y, the same observation b=0 yields target opposite My,-My, so every estimator has worst-case error >=R||M|ker L|| (operator norm attained finite dimension).
Upper bound: for an observed b, write y=y_b+v with y_b=L^dagger b the minimal-norm lift, v in ker L orthogonal to y_b, and ||v||<=sqrt(R^2-||y_b||^2). Choose estimator a(b)=M y_b. Then residual Mv <=R ||M|ker L||. Equality attained at b=0. QED.

## Optimal k unconstrained sensors: singular-value formula

Suppose rank L<=k. Then
**inf_{rank(L)<=k} E(L)=R sigma_(k+1)(M),**
with singular values arranged sigma1>=sigma2>=...>=0 and sigma_(k+1)=0 if k>=rank M.

Proof: for arbitrary L, codim ker L<=k. By Courant-Fischer/minimax singular-value principle, max_{v in ker L,||v||=1}||Mv|| >= sigma_(k+1)(M). Select L to measure the coefficients of y along the first k right singular vectors of M. Then ker L is their orthogonal complement and remaining norm is sigma_(k+1). QED.

Thus a target-adapted k-dimensional observation can suppress minimax hidden-preparation error from R sigma1 to R sigma_(k+1). This is a statement about fully free exact linear sensors, **not about parameter statistical identifiability in noisy trials or available laboratory instruments**.

## Fully explicit example

Let Y=Z=R^3, M=diag(3,1,0.2), R=1. No hidden observation: E0=3. Measure only y1: E1=1. Measure y1,y2: E2=0.2. Measure all three: E3=0. Right singular-vector measurements attain these values. A one-component scalar target M:R^n->R has rank one, so one exact unrestricted linear sensor aligned with M makes the target fully known; this may be physically tautological or impossible if target-directed sensor is unavailable.

## Legal sensor access changes the answer

If physical allowed measurements are only L=HC for a fixed accessible channel C:Y->W, then ker C subset ker L for every permitted H. Hence every such experiment satisfies:
**E(L)>=R||M|ker C||.**
Zero worst-case error is impossible unless **ker C subset ker M**. If the inclusion holds, M factors linearly through C on its range in finite dimensions; with enough accessible linear readouts, zero error is possible.

Elementary blocked-access witness: Y=R^2, M(y1,y2)=y2, permitted access C(y1,y2)=y1. Then despite any number of repeated noiseless linear postprocessings of C, E>=R. This separates mathematical sensor count from legal observability of the physical carrier.

Conversely M(y1,y2)=y1+y2, measurement only y1 leaves error R, but one freely chosen target-aligned measurement y1+y2 gives zero error. **Measurement rank without admitted measurement orientation says nothing about target risk.**

## What the theorem does NOT say

- No claim about noisy or finite-sample risk, statistical estimators, priors, non-linear adaptive testers, or restrictions on actual sensors.
- No claim about physical intervention legality, state preparation, nondemolition measurements, cross-context copying, quantum process or Bayesian experiment equivalence.
- No transfer to noncompact infinite-dimensional M without singular-value/approximation-number analysis. LT4 bounded-generator framework is enough for bounded M but NOT automatically compact.
- This is standard finite-dimensional SVD, classical optimal recovery and experimental design; prioritization of measurement is target-relative, not full microscopic reconstruction.
- The measurement occurs on the fixed hidden preparation before prediction; it is not observation of future target by fiat, unless allowed by the specified instrument class.
- One fixed endpoint target and its sensor design do not certify whole-trajectory or intervention-conditioned fidelity.

## Programme conclusion

In the LT4 / PRF11 science spine, add an **ACCESS-CONSTRAINED EXPERIMENT GATE** when claiming that extra observations make reduced predictions reliable: declare the target map M, hidden uncertainty radius R, accessible channel C, admissible sensors L, rank or cost budget k, measurement noise, and whether the desired contract concerns endpoint/histories/controlled futures. A high singular value of M on ker C is an irreducible worst-case endpoint target uncertainty under that accessible channel.

Science programme status is unchanged: REV020 authored head; P2 current, P3 fallback, TPE HOLD, novelty NONE, NO EXEC. LT4 retains scientific/book integration authority. The proof is placed as a separate note rather than modifying LT4's manuscript.