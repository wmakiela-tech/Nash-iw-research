---
artifact_id: GEEKY-S10-MIXED-RESET-TOTAL-DOSE-COLLAPSE-WITHOUT-COMMON-STORAGE-001
problem_id: P2-WEAK-RESET-RESOURCE-DOSING-001
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
document_type: PUBLIC_SCIENCE_RETURN
exposure: PUBLIC
claim_ceiling: EXACT_CONDITIONAL_FINITE_DIMENSIONAL_THEOREM / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
bw_ingestion_event_id: PENDING
canonical_path: research/geeky-s10/2026-10-23/geeky_s10_mixed_reset_total_dose_collapse_without_common_storage_001.md
source_revision: exact GitHub commit recorded in dispatch/readback
supersedes: []
---

# Geeky-S10 — Mixed/raw reset total-dose collapse without common storage

## 0. One problem — one state

**Question.** Can weak statistical-information collapse still be guaranteed when:
- the deterministic heterogeneous reset family has no known finite common storage \(V_*\);
- current readout noise may enter the reset, including the fully raw endpoint \(\alpha=1\);
- sample count may grow arbitrarily?

**Best prior positive result.** INT8 ROT006 gives, for deterministic heterogeneous reset-flow records with bounded vectors, finite horizon \(T\), per-shot strength \(s_j\le\varepsilon\), and total strength dose \(\sum_j s_j\le B\),
\[
\sum_j b_j^2
\le
\varepsilon B E^2
\exp(2\mu_+T+2DEB)\|x_0\|^2,
\]
without common \(V_*\).

**Best prior negative result.** Geeky-S10 raw-noise reset shows that without a resource bound, the scalar \(\alpha=1\) carrier is exactly equivalent to passive observations and has Fisher \(Ns^2/\sigma^2\), so \(N\sim s^{-2}\) preserves nonzero information.

**Current discriminator.** Replace sample count by a source-like total strength/dose budget and ask whether this closes the raw/mixed-reset escape without common storage.

**Result.** YES. A bounded total strength dose is independently sufficient. The exact control object is a two-dose pair:
\[
B:=\sum_j s_j,
\qquad
K:=\sum_j \kappa_j s_j,
\quad
\kappa_j:=1-\alpha_j.
\]
The conditional parameter-sensitivity energy obeys
\[
\boxed{
\sum_j c_j^2
\le
\varepsilon B E^2
\exp(2\mu_+T+2DEK)\|v\|^2.
}
\]
This includes the fully raw endpoint \(K=0\).

## 1. Typed carrier

Let \(X=\mathbb R^n\), with free flow
\[
\dot x=Gx.
\]

At shot \(j\), choose:
- time \(t_j\), with all shots contained in a finite physical horizon \(0\le t_j\le T\);
- readout vector \(e_j\), \(\|e_j\|\le E\);
- reset vector \(d_j\), \(\|d_j\|\le D\);
- strength \(0\le s_j\le\varepsilon\);
- noise-injection fraction \(0\le\alpha_j\le1\).

Define
\[
b_j=s_j e_j^\top x_j^-,
\qquad
Z_j=b_j+\eta_j,
\]
and the mixed reset
\[
x_j^+
=
x_j^-
-
d_j\big[(1-\alpha_j)b_j+\alpha_j Z_j\big].
\]

Write
\[
\kappa_j:=1-\alpha_j.
\]

For a scalar parameterized preparation
\[
x_0=\theta v,
\]
condition on one common observed past history. Then the conditional sensitivity state \(\xi_j=\partial x_j/\partial\theta\) obeys
\[
\xi_j^+
=
(I-\kappa_j s_j d_j e_j^\top)\xi_j^-,
\]
while the conditional observation coefficient is
\[
c_j=s_j e_j^\top \xi_j^-.
\]

This is the same conditional-sensitivity typing established in the mixed-reset theorem, but here **no finite common \(V_*\)** is assumed.

## 2. Semigroup and reset growth bound

Let
\[
\mu_+
=
\max\left\{
\lambda_{\max}\!\left(\frac{G+G^\top}{2}\right),
0
\right\}.
\]

Then
\[
\|e^{G\tau}\|_2\le e^{\mu_+\tau}
\qquad(\tau\ge0).
\]

For each conditional-sensitivity reset,
\[
R_j
=
I-\kappa_j s_j d_j e_j^\top.
\]
Hence
\[
\|R_j\|
\le
1+\kappa_j s_j DE
\le
\exp(\kappa_j s_j DE).
\]

Define the actual measurement-strength dose
\[
B:=\sum_j s_j,
\]
and the conditional-reset dose
\[
K:=\sum_j \kappa_j s_j.
\]

For every prefix of every finite realized protocol path,
\[
\|\xi_j^-\|
\le
\exp(\mu_+T+DEK)\|v\|.
\]

More sharply, the prefix dose can replace \(K\), but the global bound is enough for a uniform theorem.

## 3. Main theorem

Since \(\|e_j\|\le E\),
\[
c_j^2
=
s_j^2(e_j^\top\xi_j^-)^2
\le
s_j^2E^2
\exp(2\mu_+T+2DEK)\|v\|^2.
\]

Because \(s_j\le\varepsilon\),
\[
s_j^2\le\varepsilon s_j.
\]

Summing,
\[
\boxed{
\sum_j c_j^2
\le
\varepsilon B E^2
\exp(2\mu_+T+2DEK)\|v\|^2.
}
\tag{3.1}
\]

Since \(K\le B\), the coarser one-dose form is
\[
\sum_j c_j^2
\le
\varepsilon B E^2
\exp(2\mu_+T+2DEB)\|v\|^2.
\tag{3.2}
\]

### Interpretation

There are now two independent sufficient mechanisms for weak-protocol collapse:

1. **Common-storage mechanism:** finite \(V_*\), allowing arbitrarily large total dose/sample count.
2. **Finite-dose mechanism:** finite \(B\) and \(T\), requiring no common \(V_*\).

Neither subsumes the other.

## 4. Fully raw reset endpoint

For \(\alpha_j=1\) at every shot,
\[
\kappa_j=0,
\qquad
K=0.
\]

Then
\[
\boxed{
\sum_j c_j^2
\le
\varepsilon B E^2e^{2\mu_+T}\|v\|^2.
}
\tag{4.1}
\]

Thus the raw-noise-reset counterexample does **not** defeat weak collapse when total strength dose is bounded.

In the scalar sharp control
\[
G=0,\quad E=D=1,\quad s_j=\varepsilon,\quad \alpha_j=1,
\]
the transformed experiment has
\[
c_j=\varepsilon.
\]
Therefore
\[
\sum_j c_j^2
=
N\varepsilon^2
=
\varepsilon B
\]
because \(B=N\varepsilon\).

So (4.1) is **exactly sharp in constant** for this scalar raw endpoint.

The earlier noncollapse regime
\[
N\sim \varepsilon^{-2}
\]
corresponds precisely to
\[
B=N\varepsilon\sim\varepsilon^{-1},
\]
i.e. a diverging total dose.

Hence:
\[
\text{RAW RESET + UNBOUNDED SAMPLE COUNT}
\neq
\text{FREE INFORMATION};
\]
the information survival consumes a diverging total measurement dose.

## 5. General asymptotic criterion

Allow \(B=B_\varepsilon\) and \(K=K_\varepsilon\) to vary with \(\varepsilon\).

A sufficient collapse condition is
\[
\boxed{
\varepsilon B_\varepsilon
\exp(2DEK_\varepsilon)
\to0
}
\tag{5.1}
\]
for fixed \(T,E,D,G,v\).

This is more informative than “bounded dose” alone.

### Raw endpoint
\(K_\varepsilon=0\):
\[
\varepsilon B_\varepsilon\to0.
\]
The scalar example proves the threshold \(B_\varepsilon\asymp\varepsilon^{-1}\) is sharp.

### Uniformly mixed reset
If \(K_\varepsilon\le K_0<\infty\):
\[
\varepsilon B_\varepsilon\to0
\]
still suffices.

### Growing conditional-reset dose
If \(K_\varepsilon\to\infty\), the product-norm mechanism allows exponential sensitivity amplification; then total-dose growth and oblique reset geometry cannot be separated.

This matches INT8 ROT006’s negative oblique examples: dose is genuinely load-bearing when common storage is absent.

## 6. Adaptive causal policies

The theorem is pathwise.

Actions, times, strengths and \(\alpha_j\) may be chosen causally from previous observed data under one parameter-independent policy, provided every realized protocol:
- is finite;
- remains within \(t\le T\);
- obeys the same deterministic bounds \(E,D,\varepsilon\);
- obeys realized dose bounds \(B_\varepsilon,K_\varepsilon\).

At a frozen history the choices are fixed numbers, and the same norm-product proof applies.

Thus causal noisy-history adaptation does not evade the dose budget.

## 7. iid Gaussian statistical consequences

Assume current innovations
\[
\eta_j\stackrel{\mathrm{iid}}{\sim}N(0,\sigma^2),
\]
independent of the past and of \(\theta\).

Sequential Gaussian KL gives
\[
D_{\mathrm{KL}}(P_\theta^\pi\|P_{\theta'}^\pi)
=
\frac{(\theta-\theta')^2}{2\sigma^2}
\mathbb E_\theta
\sum_j c_j^2.
\]

Using (3.1):
\[
\boxed{
D_{\mathrm{KL}}
\le
\frac{(\theta-\theta')^2}{2\sigma^2}
\varepsilon B E^2
e^{2\mu_+T+2DEK}\|v\|^2.
}
\tag{7.1}
\]

Fisher information satisfies
\[
\boxed{
I_\pi(\theta)
\le
\frac{\varepsilon B E^2}{\sigma^2}
e^{2\mu_+T+2DEK}\|v\|^2.
}
\tag{7.2}
\]

For \(\theta\in[-R,R]\), Le Cam distance to the parameter-free comparison experiment is bounded by
\[
\boxed{
\Delta(E_\pi,F_\pi)
\le
\min\left\{
1,
\frac{R}{2\sigma}
\sqrt{
\varepsilon B E^2
e^{2\mu_+T+2DEK}\|v\|^2
}
\right\}.
}
\tag{7.3}
\]

The two-point Bayes/information-radius argument yields
\[
\boxed{
R^2
\left[
1-
\frac{R^2}{\sigma^2}
\varepsilon B E^2
e^{2\mu_+T+2DEK}\|v\|^2
\right]_+
\le
J_\pi
\le
R^2.
}
\tag{7.4}
\]

Thus bounded-dose weak sensing becomes asymptotically no-information at fixed Gaussian innovation noise, even at the fully raw reset endpoint.

## 8. Correlated Gaussian fixed-protocol extension

For a fixed deterministic protocol, after the exact mixed-reset triangular innovations transform,
\[
Y\sim N(\theta c,\Sigma).
\]

If
\[
\Sigma\succeq\sigma_*^2I,
\]
then
\[
I(\theta)
=
c^\top\Sigma^{-1}c
\le
\frac{\|c\|^2}{\sigma_*^2}.
\]

Therefore
\[
I(\theta)
\le
\frac{
\varepsilon B E^2
e^{2\mu_+T+2DEK}\|v\|^2
}{\sigma_*^2}.
\]

PRF11 R14 remains an independent failure seam:
fixed marginal variances do not imply such a precision floor.

## 9. Relation to existing results

### Versus INT8 ROT006
INT8 bounds deterministic output energy for heterogeneous ideal reset-flow:
\[
\sum b_j^2
\lesssim
\varepsilon B e^{2DEB}.
\]

The present result uses the same mature norm-product host but applies it to a different object:
**conditional parameter sensitivity under mixed/raw noisy reset**.

Its sharper exponent is \(K=\sum\kappa_js_j\), not necessarily \(B\).

At \(\alpha=1\):
- INT8 deterministic state reset theorem is not the statistical carrier;
- present conditional sensitivity has \(K=0\), giving exact scalar sharpness.

Therefore this is a cross-carrier extension, not a re-labeling of ROT006.

### Versus common \(V_*\)
The common-storage theorem can handle unbounded sample count/dose but requires finite global \(V_*\).

The dose theorem needs no \(V_*\), but pays with a finite/growing resource budget \(B,K,T\).

### Versus MT13 mixed-reset phase
MT13/common-storage phase controls \(\sum c_j^2\) by \(\varepsilon/\kappa\) when a common \(V_*\) exists.

The present theorem remains valid when \(\kappa=0\), but requires a dose budget.

These are complementary gates.

## 10. Prior-art subtraction / host

The proof uses mature ingredients:
- Euclidean logarithmic norm / semigroup growth;
- submultiplicative product bounds for impulsive/switched linear systems;
- Grönwall-type exponential envelope;
- sequential Gaussian KL/Fisher;
- standard Le Cam/Pinsker and two-point minimax arguments.

No novelty claim is made for these ingredients or their general theory.

What survives project-locally is the **typed separation of three carriers/resources**:
1. reset-flow common storage \(V_*\);
2. conditional reset dose \(K\);
3. total observation-strength dose \(B\),

together with exact raw-endpoint sharpness and the rule for when each mechanism legally controls statistical information.

## 11. Firewalls

FINITE TOTAL DOSE
!=
FINITE COMMON STORAGE.

COMMON STORAGE
!=
RESOURCE BUDGET.

ACTUAL RESET DOSE \(B\)
!=
CONDITIONAL RESET DOSE \(K\).

RAW NOISE RESET
!=
AUTOMATIC NONCOLLAPSE.

RAW NONCOLLAPSE WITH \(N\sim\varepsilon^{-2}\)
=> DIVERGING TOTAL DOSE \(B\sim\varepsilon^{-1}\)
in the scalar model.

FINITE PHYSICAL HORIZON
!=
SHOT-RATE BOUND.

CORRELATED MARGINAL VARIANCE
!=
UNIFORM PRECISION FLOOR.

CLASSICAL MIXED RESET
!=
QUANTUM INSTRUMENT.

STATISTICAL COLLAPSE
!=
PHYSICAL SENSOR LAW
without a source-admitted dose/noise/time contract.

## 12. Disposition / STOP criterion

**PASS exact conditional theorem**:
\[
\sum c_j^2
\le
\varepsilon B E^2e^{2\mu_+T+2DEK}\|v\|^2.
\]

**Sharp endpoint**:
for scalar raw reset, \(\sum c_j^2=\varepsilon B\).

**Cheapest discriminator for any physical transfer**:
derive from the actual source whether measurement strength, shot count, bandwidth/time, state disturbance or energy impose a finite \(B_\varepsilon,K_\varepsilon,T_\varepsilon\).

**STOP** abstract weak-reset work on this seam when a claimed extension merely rephrases:
- common-storage control;
- finite-dose control;
- covariance precision control;
without a new carrier, sharper boundary or source-valid resource relation.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
