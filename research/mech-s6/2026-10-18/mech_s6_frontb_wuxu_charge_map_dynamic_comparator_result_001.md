# MECH-S6 Front B — Wu–Xu charge-map dynamic comparator result

**RETURN_ID:** MECH-S6-FRONTB-WUXU-CHARGE-MAP-DYNAMIC-COMPARATOR-RESULT-001  
**CELL:** IW_MECH_LINEAGE_001_SUCCESSOR_05 / Mech-S6  
**DATE:** 2026-10-18  
**EXPOSURE:** PUBLIC  
**CUSTODY:** GITHUB_PENDING_BW_INGEST  
**RESULT_CLASS:** source-map dynamic executor comparator / supported-domain materiality / endpoint-confounded diagnostic  
**CLAIM CEILING:** NO MODERN YP/DH ENDPOINT / NO PBH BOUND / NO CANON / NO EXEC_SIGN / NO NOVELTY CLAIM

## 1. Question

Does replacing the literal public Wu–Xu aggregate-to-single-species source map B_exec with the charge-conjugation-symmetric candidate B_sym produce a dynamically material change in the public v2 reduced executor?

This return tests only that map change while holding the visible public v2 source helper fixed.

It does **not** reconstruct the paper-declared below-edge M^-1.3 source prescription.

## 2. Exact numerical contract

Audited upstream Wu–Xu repository:

- repository: Fenyutanchan/Primordial-Black-Hole
- commit: d395183674cace6c9906a8911bdeb7234ba4040d

Pinned historical NaturalUnits state:

- Fenyutanchan/NaturalUnits.jl
- commit: 4a9f007ff1df416c9fef28c4d83d8fe8846099cf

Runtime:

- Julia 1.12.3
- ArbNumerics 1.6.3
- DataInterpolations 8.8.0
- DifferentialEquations 7.17.0
- Format 1.3.7
- ForwardDiff 1.3.1
- IrrationalConstants 0.2.6
- JLD2 0.6.3
- SpecialFunctions 2.6.1
- upstream BITS=100 retained

Diagnostic point:

\[
M_{\rm PBH}^{\rm initial}=6\times10^9\,{\rm g},
\qquad
\beta=10^{-16}.
\]

This is the same parameter point used by the public Wu–Xu notebook for its hadron-population evolution diagnostic.

It is **not** promoted here as a main scan / exclusion-bound point.

## 3. Comparator maps

The public BlackHawk source columns are

\[
Q=(Q_{\pi^\pm},Q_{K^\pm},Q_{K_L^0},Q_{p+\bar p},Q_{n+\bar n})^T.
\]

Literal public executor:

\[
B_{\rm exec}Q=
(Q_{\pi^\pm},Q_{\pi^\pm},Q_{K^\pm},Q_{K_L^0},Q_{p+\bar p},Q_{n+\bar n})^T
\]

for tracked

\[
(\pi^-,\pi^+,K^-,K_L^0,\bar p,\bar n).
\]

Charge-symmetric comparator:

\[
B_{\rm sym}Q=
\left(
\frac12Q_{\pi^\pm},
\frac12Q_{\pi^\pm},
\frac12Q_{K^\pm},
Q_{K_L^0},
\frac12Q_{p+\bar p},
\frac12Q_{n+\bar n}
\right)^T.
\]

No other scientific code path was intentionally changed.

The fail-closed patch contract is CI-tested separately.

## 4. Execution status

GitHub Actions run: 39074426824.

Scientific steps:

- pinned environment: PASS
- audited upstream clone: PASS
- current source-map ODE: PASS
- repaired source-map ODE: PASS
- trajectory comparator: PASS
- artifact upload: PASS

The workflow's overall failure status came only from the final git push being rejected because main had advanced concurrently.

That custody conflict is **not** a numerical failure.

Artifact:

- artifact ID: 12116193467
- artifact name: mech-s6-wuxu-charge-pair-comparator
- artifact ZIP SHA256: 75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5

Raw trajectory hashes:

- trajectory_current.csv: 1be7765f4208862fb950ceaedc63d18b80fbd3acc923ad8d36d4d93c360b4de2
- trajectory_repaired.csv: 274d329c3f9625622f77aa8406460c91d6448ae2d4ccd4ce929cfa78cd955e8a

## 5. Primary dynamic result

The Wu–Xu reduced endpoint proxy returned:

\[
Y_{P,{\rm exec}}=1.3230817938392783,
\]

\[
Y_{P,{\rm sym}}=1.3177406564166434.
\]

Therefore

\[
\Delta Y_P=-0.0053411374226349,
\]

or approximately -0.404% relative to the literal-executor value.

**Interpretation guard:** at this deliberately strong diagnostic point the Wu–Xu reduced formula gives \(Y_P>1\), so this number must not be interpreted as a physical helium mass fraction.

The code computes

\[
Y_P=\frac{2X_n(T_{\rm nuc})}{1-X_n(T_{\rm nuc})}.
\]

Inverting only that declared proxy gives:

\[
X_{n,{\rm nuc}}^{\rm exec}\approx0.3981490303,
\]

\[
X_{n,{\rm nuc}}^{\rm sym}\approx0.3971801273,
\]

so

\[
\Delta X_{n,{\rm nuc}}\approx-9.68903\times10^{-4},
\]

or about -0.243% relative.

Again this is a reduced-executor diagnostic, not a modern full-BBN endpoint.

## 6. Supported-domain materiality is large before terminal extrapolation

The largest trajectory difference is

\[
\max|\Delta X_n|=0.0728514990.
\]

It occurs at:

- \(t\approx5.06095\) s,
- \(T\approx0.393875\) MeV,
- \(M_{\rm PBH}\approx5.79601\times10^9\) g,
- \(X_n^{\rm exec}\approx0.416505\),
- \(X_n^{\rm sym}\approx0.343653\).

This mass is well inside the directly tabulated \(M\ge10^9\) g source domain.

Therefore:

**CHARGE-MAP DYNAMIC MATERIALITY EXISTS BEFORE THE SUBEDGE SOURCE-LAW CONFOUNDER.**

The maximum forcing difference is

\[
\max|\Delta F_{\rm had}|
\approx1.07285\times10^{-25}\ {\rm GeV}.
\]

It occurs at:

- \(t\approx0.07805\) s,
- \(T\approx3.07730\) MeV,
- \(M_{\rm PBH}\approx5.99696\times10^9\) g.

At that point:

\[
F_{\rm had}^{\rm exec}\approx2.23996\times10^{-25}\ {\rm GeV},
\]

\[
F_{\rm had}^{\rm sym}\approx1.16711\times10^{-25}\ {\rm GeV},
\]

so

\[
F_{\rm had}^{\rm sym}/F_{\rm had}^{\rm exec}\approx0.5210.
\]

The repaired hadron populations there are essentially one half of the affected current populations, while \(K_L^0\) remains unchanged, as expected from the floor-inactive common-background theorem before feedback becomes large.

## 7. Directional-rate response

The run-level maximum absolute differences are:

\[
\max|\Delta A|\approx1.96217\times10^{-23}\ {\rm GeV},
\]

\[
\max|\Delta B|\approx1.95189\times10^{-23}\ {\rm GeV}.
\]

Relative to the current trajectory maxima:

- A: about 49.428%
- B: about 49.425%
- F_had: about 47.896%

The maxima of A and B occur at very high temperature, so they are not promoted here as BBN-target importance measures.

The more relevant result for this diagnostic is that the forcing difference remains order-one in the directly tabulated-source regime around a few MeV.

## 8. Nonlinear feedback becomes visible

At the point of maximum \(|\Delta X_n|\):

\[
T\approx0.394\ {\rm MeV},
\qquad
M_{\rm PBH}\approx5.80\times10^9\ {\rm g}.
\]

Population ratios repaired/current are approximately:

- pi-: 0.49993
- pi+: 0.50006
- K-: 0.49984
- K0L: 0.999996
- pbar: 0.49029
- nbar: 0.51050

while:

\[
A_{\rm sym}/A_{\rm exec}\approx0.5151,
\]

\[
B_{\rm sym}/B_{\rm exec}\approx0.4966,
\]

but

\[
F_{\rm had}^{\rm sym}/F_{\rm had}^{\rm exec}\approx0.9290.
\]

Thus a nearly exact half-split at the population/source level does **not** remain a simple half-split in the total reduced forcing after the \(X_n\) trajectory has separated.

This numerically confirms:

**SOURCE HALF-SPLIT != FULL COUPLED FORCING HALF-SPLIT.**

## 9. Log-floor audit

At all **sampled source-active trajectory points**, the reported floor flags are zero for all six tracked hadron populations in both current and repaired runs.

The minimum sampled source-active repaired population is still many orders of magnitude above the executor floor. For example the repaired K- minimum is approximately \(1.81\times10^{11}\ {\rm cm^{-3}}\), while \(e^{-100}\ {\rm GeV^3}\) is approximately \(4.8\times10^{-3}\ {\rm cm^{-3}}\).

Therefore sampled-floor contamination is decisively absent.

Strictly:

**SAMPLED FLOOR INACTIVITY != INTERNAL SOLVER FLOOR INACTIVITY PROOF.**

No raw internal-step floor instrumentation was performed.

## 10. Critical correction to the automatic subedge diagnostic

The automatic report states:

> source-active sampled points below \(10^9\) g: 0.

This is true for the 1600 output samples but must **not** be interpreted as saying the ODE never evaluates the public helper below \(10^9\) g.

The last sampled source-active mass is approximately

\[
1.8366\times10^9\ {\rm g},
\]

while the next output sample is already post-evaporation at approximately

\[
8.45\ {\rm g}.
\]

The adaptive solver therefore traverses the terminal mass interval internally between output samples.

Consequently:

**0 SAMPLED SUBEDGE POINTS != 0 INTERNAL SUBEDGE SOURCE EVALUATIONS.**

The endpoint proxy can still depend on the public helper's below-edge source semantics.

## 11. Paper-vs-code source-law confound

XH-S3 harvest026 established:

Paper-declared below-edge source rule:

\[
Q_h^{\rm paper}(M)
=
Q_{0,h}
\left(\frac{M}{10^9\,{\rm g}}\right)^{-1.3}.
\]

Visible public v2 helper uses log-log linear table interpolation with species-specific edge extrapolation slopes near 1.20.

Therefore:

**PAPER-DECLARED SUBEDGE METHOD != CURRENT PUBLIC V2 HELPER SUBEDGE SEMANTICS.**

M13 Rotation08 further established that the source-exponent correction and charge-map correction have a factorial interaction and cannot be naively added.

Hence the present dynamic endpoint difference means:

> charge-map sensitivity conditional on the visible public v2 helper.

It does **not** mean:

> correction to the published-paper endpoint.

## 12. Scan provenance remains open

XH-S4 verified that:

- v1 and v2 source models are materially different,
- v1 and v2 tracked scanning.jld2 files are distinct blobs,
- both inspected visible helpers use log-log edge extrapolation,
- neither inspected helper implements the paper-declared \(M^{-1.3}\) branch.

But the numerical payload / figure genealogy of the tracked JLD2 scans is not yet sufficient to prove which exact source rule produced the final JCAP figures.

Thus:

**VISIBLE V2 EXECUTOR != PROVEN PUBLISHED NUMERICAL RUN LINEAGE.**

## 13. Status

B_EXEC_TO_B_SYM_DYNAMIC_EFFECT = MATERIAL / PASS_ONE_POINT

SUPPORTED_DOMAIN_MAX_DELTA_XN = 0.0728515

SUPPORTED_DOMAIN_MAX_DELTA_F_HAD = 1.07285e-25 GeV

REDUCED_YP_PROXY_CHANGE = -0.404% / DIAGNOSTIC_ONLY

INFERRED_XN_AT_TNUC_CHANGE = -9.689e-4 / DIAGNOSTIC_ONLY

SAMPLED_SOURCE_ACTIVE_FLOOR_FLAGS = ZERO

STATIC_PATCH_CONTRACT = PASS_CI

DYNAMIC_CURRENT_RUN = PASS

DYNAMIC_REPAIRED_RUN = PASS

TRAJECTORY_COMPARISON = PASS

RAW_TRAJECTORIES = CUSTODIED_IN_GITHUB_ACTIONS_ARTIFACT_12116193467

PUBLISHED_PAPER_BOUND_CORRECTION = NOT_ESTABLISHED

PAPER_M^-1.3_PLUS_B_SYM_DYNAMIC_RESULT = NOT_RUN

FULL_MASS_BETA_GRID = NOT_RUN

MODERN_YP_DH_ENDPOINT = NOT_RUN

INTERNAL_STEP_FLOOR_AUDIT = NOT_RUN

SOURCE_VALID_E2B = OPEN

SOURCE_MATCHED_K_PBH = UNDEFINED

NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY

## 14. Cheapest next control

The next clean dynamic comparator is a two-factor \(2\times2\) source design:

1. public-helper source law + B_exec
2. public-helper source law + B_sym
3. paper \(M^{-1.3}\) branch + B_exec
4. paper \(M^{-1.3}\) branch + B_sym

using the same upstream solver and the same diagnostic point.

This directly measures:

- charge-map main effect,
- source-law main effect,
- interaction term.

Only after that should any dynamic result be compared to tracked scan blobs or propagated toward a physical BBN endpoint.

## 15. Reproducibility assets

Static patcher:

research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py

CI contract test:

tests/test_wuxu_charge_pair_patch.py

Dynamic harness:

research/mech-s6/2026-10-18/wuxu_dynamic_comparator/

Controlling workflow run:

39074426824

Artifact ID:

12116193467
