---
artifact_id: IW_MT15_ROT005_FRONTA_ERFC_POSITIVE_YUKAWA_FULL_INTERVAL_SHARP_UNIFORM_RELATIVE_MINIMAX_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
exposure: PUBLIC
document_type: SOURCE_TYPED_EXACT_CLASSICAL_APPROXIMATION_THEOREM_AND_INDEPENDENT_NUMERICAL_REPLAY
status: SHARP_WHOLE_COMPACT_INTERVAL_THEOREM_PROVED / 5_SOURCE_MODEL_POINT_RADIUS_EXAMPLES_EXECUTED / STDLIB_FULL_SCRIPT_AND_JSON_GITHUB_BYTE_IDENTICAL / HIGH_PRECISION_INDEPENDENT_CHECK_PASS
claim_ceiling: NORMALIZED_POINT_SOURCE_ERFC_DEFICIENCY_POSITIVE_YUKAWA_CONE_ONLY / NOT_SIGNED_LINEAR_SPAN / NOT_SOURCE_NATIVE_LEE_APPARATUS_TORQUE / NOT_ACTUAL_EOTWASH_LIKELIHOOD / NO_GAUSSIAN_IDG_PHYSICAL_BOUND / NO_MATH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# MT15 ROT005 — Entire-interval sharp relative-uniform erfc approximation by all nonnegative Yukawa mixtures

## Source, original science owner and mature host FIRST

ORIGINAL published physical source: Edholm, Koshelev and Mazumdar, *Behavior of the Newtonian potential for ghost-free gravity and singularity-free gravity*, Phys. Rev. D **94**, 104033 (14 Nov 2016), DOI https://doi.org/10.1103/PhysRevD.94.104033 , arXiv:1604.01989. In a particular point-source ghost-free nonlocal gravity model, the *normalized correction/deficiency relative to a Newton 1/r potential* is the complementary error function f_ell(r)=erfc(r/(2ell)). **Neither the full Newton potential nor torsion-pendulum torque is directly f_ell(r)**. The sign of the correction to full potential may be negative; we study positive nonnegative weights of this normalized deficiency in a separate source/model-class question.

MATURE MATHEMATICS: complementary Gaussian tail hazard and Mills inequality; preservation of log-convexity under positive mixtures (classical Hölder/Artin mixture principle, see Marshall–Olkin–Arnold *Inequalities*, B.8 and general convex analysis Boyd–Vandenberghe); Bernstein–Widder characterization of positive exponential mixtures; relative Chebyshev/equioscillation approximation. Literature context from publicly consulted journal and convexity sources, but NO novelty/prior-art exhaustion claim.

PROJECT FIRSTNESS:
- Historical M12 positive/source-typed point-source template families and Mech-S5 original Lee Eöt-Wash apparatus Source L1 PARK already exist. Original Lee experiment marginal Yukawa fit has no verified Gaussian target Gram/cross-overlap transfer.
- EKS1 DIR-001 ROT003–005 owns F1/F2' question; ROT005 published synthetic F2' signed-span proxy, not actual apparatus bound.
- MT15 ROT002 FIRST resolved F1 diagnostic-only and F2' source HOLD with exact Gram-target nonidentification; this remains.
- MT15 ROT003 FIRST proved the SHARP THREE NODE positive mixture lower bound for a symmetric radius triple; at three points a single exponential saturates (+epsilon,-epsilon,+epsilon), and a signed three-exponential interpolation was its negative control.
- KN13 ROT012 FIRST independent Python check of the four ROT003 cases and signed negative control, using published source model without Lee apparatus. Exact original source priority retained.
- This ROT005 adds a **FULL CONTINUOUS COMPACT INTERVAL** SHARP infimum, attained by a uniquely determined positive single exponential, not just a selected 3-node gate.

## Typed theorem (exact and complete interval, relative L-infinity error)

Fix ell>0 and nonnegative radii 0<=a<b<infinity. Put
\`\`\`
f(r) = erfc(r/(2ell)) > 0
h(r) = exp( ((b-r)/(b-a))*ln(f(a)) + ((r-a)/(b-a))*ln(f(b)) )
D = max_{r in [a,b]} f(r)/h(r) > 1
E* = (D-1)/(D+1) in (0,1).
\`\`\`
Let \`Y_+\` be ALL nonzero finite **positive mixtures of Yukawa exponentials** on this interval:
\`\`\`
g(r) = integral_[0,infty) exp(-m r) dmu(m), mu>=0,
\`\`\`
with g(a),g(b) positive finite. Finite mixtures with nonnegative amplitudes and m>=0 are included. In particular no restriction to a single Yukawa, nor a fixed finite set of m, is imposed.

Then
\`\`\`
inf_{g in Y_+} max_{r in [a,b]} abs(g(r)/f(r)-1)
       = (D-1)/(D+1) = E*.
\`\`\`
The infimum is attained by the **single positive Yukawa exponential**
\`\`\`
g*(r) = (1+E*) h(r)
      = A* exp(-m* r),
m* = (ln f(a)-ln f(b))/(b-a) > 0,
A* = (1+E*) f(a) exp(m*a) > 0.
\`\`\`
It is in fact unique in \`Y_+\` as a function on [a,b], because equality in Hölder at an interior radius forces concentration of the mixing measure at the one exponent m*. Adding positive Yukawas cannot improve the optimum.

The unique worst interior radius r* is the solution of the strictly monotone scalar equation
\`\`\`
(d/dr)ln f(r*) = [ln f(b)-ln f(a)]/(b-a) = -m*.
\`\`\`
At a,r*,b the optimal relative residual has exact alternating values (+E*,-E*,+E*). For EVERY other radius the residual lies between those two endpoints. Thus the continuous supremum and the minimizing function are analytically certified without trusting a numerical grid.

## Proof, no unproved physical bridge

(1) **Strict log concavity of erfc on r>=0.** Write F(u)=erfc(u), u=r/(2ell). Then F'=-2exp(-u²)/sqrt(pi), F''=4u exp(-u²)/sqrt(pi). Thus
\`\`\`
(d²/du²) ln F =
 [4 exp(-u²)/(sqrt(pi) F(u)^2)] * [u F(u) - exp(-u²)/sqrt(pi)].
\`\`\`
For u>0, Gaussian Mills inequality F(u)<exp(-u²)/(u sqrt(pi)), from the defining Gaussian tail integral and t/u>1 for t>u, makes the bracket strictly negative. At u=0 it is also negative. Hence log f(r) strictly concave. Consequently f(r)>h(r) in the open interval, and f/h has unique strict maximum D at the interior point where the logarithmic derivatives agree. The normalized f is strictly decreasing, so m*>0.

(2) **Any positive exponential mixture is log convex.** Hölder for the positive measure mu yields for r=(1-t)a+t b:
\`\`\`
g(r) <= g(a)^(1-t) g(b)^t, 0<=t<=1.
\`\`\`
Suppose its relative sup error is E<1. Then g(a)<=(1+E)f(a), g(b)<=(1+E)f(b), but g(r*)>=(1-E)f(r*). By Hölder,
\`\`\`
(1-E)f(r*) <= g(r*) <= (1+E)h(r*),
\`\`\`
so (1-E)/(1+E)<=1/D, giving E>=(D-1)/(D+1). If E>=1 the same lower bound is trivial.

(3) **Sharp and unique witness.** Let g*=(1+E*)h, a valid single exponential with m*>0. Since 1<=f/h<=D everywhere,
\`\`\`
g*(r)/f(r) = (1+E*) / (f(r)/h(r))
    belongs to [(1+E*)/D,1+E*] = [1-E*,1+E*].
\`\`\`
At both endpoints and r*, equalities hold. This saturates the universal lower bound for the ENTIRE INTERVAL, not merely three points. For any other minimizer g, equality in the chain must hold at a,b,r*, including equality in the Hölder relation for t* strictly between 0 and1; for a Laplace positive measure, equality implies mu concentrated at a single mass, and endpoints then force g=g*. QED.

The theorem is standard convex-analytic reasoning applied to the erfc host, with no independent mathematical novelty claim.

## Five actually computed examples

Units for ell, a, b and r* are micrometres. These are ILLUSTRATIVE POINT-SOURCE RADII, not source-native Lee torsion-pendulum separations or generated torques.

| ell [um] | interval [a,b] um | ROT003 midpoint 3-node floor | ROT005 exact whole-interval minimax | unique interior r* [um] | single exp decay length 1/m* [um] |
|---:|---|---:|---:|---:|---:|
| 40 | 52–108 | .05151916548641618 | **.05152304247523157** | 80.24289752659078 | 30.25617472898575 |
| 40 | 52–148 | .15497633346374692 | **.15499642144122250** | 100.54989441717925 | 25.976556951844305 |
| 30 | 52–108 | .09521694795158592 | **.09522317590367857** | 80.22690723110759 | 18.632559874327015 |
| 50 | 52–108 | .031923263135683916 | **.03192567123705321** | 80.24309181002931 | 43.271021073296836 |
| 40 | 0–200 | .585227809835805 | **.5855129295539937** | 102.52205033449786 | 25.618641278562134 |

The infinitesimal difference between an evenly spaced 3-node floor and the exact continuous interval floor is positive (worst r* is typically near but not exactly at the midpoint). ROT003 remains completely valid, simply weaker. For ell40, [52,108] the exact full-interval minimax is ~5.1523%, NOT a device signal mismatch estimate.

## Executed reproducibility / numerical evidence

PUBLIC, byte-identical Git source code:
\`research/mt15/2026-11-11/mt15_rot005_continuum_erfc_positive_yukawa_minimax.py\`
Local SHA256 \`5fa60d66b157d29cd662bbfc730405da08ae43bc7558b8ac46f444f279d653cc\`, original local Git blob \`ca54f26fe3e57f885f30a3b0ed657a15c56cc2f8\`.

PUBLIC, byte-identical local Git result JSON:
\`research/mt15/2026-11-11/mt15_rot005_continuum_erfc_positive_yukawa_results.json\`
Local SHA256 \`19016d951338f1c03de55f0f787e0945892c3422a64c3136bbb6942457d2e614\`, local Git blob \`2af72bff0cf56dd545c6b1b2d9f4a3c0d3c10f94\`.

ACTUALLY EXECUTED local Python 3 stdlib, five radius/ell pairs, 100-step bisection each, exact equioscillation witness at [a,r*,b], 15,005 dense-grid checks of a **preproven** minimizer, 305 finite three-component positive-mixture negative controls against violating the lower bound. Mathematical proof is analytic, no sample-based inference.

INDEPENDENT Python mpmath calculation at 70 decimal digits for all five cases (separate derivative-root code and model evaluation): maximum relative-error fraction absolute discrepancy from the stdlib script **1.53e-16**, maximum interior-radius discrepancy ~5.69e-14 um, largest amplitude discrepancy 8.89e-16. These are independent arithmetic checks of the same mathematical model, not a source apparatus replay, independent physical referee or I3 audit.

Files were created through GitHub connector and FULL content fetched back with exact byte equality to already executed local content; no BW source event is claimed unless KN13 separately records it.

## Exact negative scope and scientific use

1. The theorem assumes **NONNEGATIVE COEFFICIENTS a_j>=0 and NONNEGATIVE Yukawa masses m_j>=0**, fitting the normalized positive point-source deficiency f. NEGATIVE Yukawa coefficients can interpolate three values exactly as already shown in MT15 ROT003 and KN13 ROT012. The theorem gives no obstruction to EKS1 F2' UNRESTRICTED SIGNED linear span.
2. It is POINT-SOURCE FUNCTIONAL MISMATCH, not a bound on actual patterned-source Eöt-Wash torque. Force derivatives, source geometry, higher harmonics, finite body shape, nuisance projection, whitening and real noise can alter model cone, metric and minimax target. Transferring this % as a physical exclusion, significance or Gaussian mass constraint is prohibited.
3. Real Lee source L1 Newton chi² mismatch / incomplete geometry ledger = PARK, F1 diagnostic-only, F2' target-Gram/source overlap missing = HOLD as MT15 ROT002. EKS1 owns proposal, Mech-S8 physical E4 work (distinct Wu–Xu work), REC11/AUD1 independent reviews. No owner task cascade, no CANON or executive signature.
4. The bound's significance is narrow but exact: a mathematical certificate that **even arbitrarily many positive point-source Yukawa exponentials cannot approximate the erfc deficiency on a continuous compact radius interval more accurately than the single best one**. Any claim about generic signed combinations or physics exceeds this theorem.

END: \`CLASSICAL_FULL_INTERVAL_SHARP_POSITIVE_CONE_MINIMAX_PROVEN / LOCAL_STDLIB_AND_INDEPENDENT_MPMATH_PASS / PUBLIC_GITHUB_FULL_READBACK_PASS / NO_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST\`.
