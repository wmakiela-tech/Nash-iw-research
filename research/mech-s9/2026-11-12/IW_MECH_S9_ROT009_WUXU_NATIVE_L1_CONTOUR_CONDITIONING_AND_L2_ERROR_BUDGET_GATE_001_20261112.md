---
artifact_id: IW_MECH_S9_ROT009_WUXU_NATIVE_L1_CONTOUR_CONDITIONING_AND_L2_ERROR_BUDGET_GATE_001_20261112
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
created_at: 2026-11-12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
document_type: SOURCE_NATIVE_NUMERIC_CONDITIONING_DIAGNOSTIC
claim_ceiling: MODEL_INTERNAL_NONBLIND_SOURCE_DATA_CONDITIONING / NOT_INDEPENDENT_L2 / NO_PHYSICAL_BOUND / NO_FIG5_IDENTITY / NO_CANON / NO_EXEC_SIGN
---

# ROT009: Wu–Xu original-source V0/V1/V2 contour conditioning before independent native L2 referee verdict

## Science first and original-first custody

Original authors: Wu and Xu, source frozen `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`, original `arXiv-2509.05618/main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. Badacz (Claude) first native original code REVIEW053 2026-11-08, owner L1 reference `research/badacz/2026-11-08/data/yp051/yp_a.csv` blob `df78f479277d85c7a558e132428d8846c64f9512` and `yp_b.csv` blob `a8f3fea64b46d5c42c69e155a3690b99581cc1aa`. EKS1 first recovered Mech-S6 remote native Julia runner and commissioned a bounded non-Claude GPT native L1+independent L2 return, prior to Grok. Mech-S9 native full L1 workflow `43304075848` reproduced all printed numeric source tokens in 53 original Badacz rows; verified downloaded source output ZIP artifact `13983688155`, SHA256 `2120d9c103e948db112ae3b4846d7b9003e469d1daa83c5c92318c9c39789603`. These are source-model numeric results, not a physical PBH constraint.

## Source numerical conditioning diagnostic

Using the ACTUAL GitHub native L1 `replica_full53_raw.csv` (not refitted source models), for j=22 and j=62 take source grid response in log10(beta), with same REVIEW053 target definitions:

```
V0(x) = Y_code(m,beta)-0.251.
V1(x) = 2 X_n(T1;m,beta)-0.251.
V2(x) = 2 [ X_n(T0;m,beta) - X_n,SBBN(T0;j22) ] - 0.006.
x=log10(beta), T0=0.07818527068831994 MeV; T1_j22=0.099688851247 MeV.
```

Find each first negative-to-positive neighboring sampled sign change `[x_i,x_(i+1)]`, let `s=(V(x_(i+1))-V(x_i))/(x_(i+1)-x_i)`. It is a **sampled secant**. The first-order inverse-sensitivity relation `|delta_x|≈|delta_V|/|s|` is **LOCAL, approximate and conditional**; it is NOT a certified global derivative bound, upper bound on native solver noise or statistical error bar.

| Mass j | Channel | Native L1 zero bracket x | Secant s (per dex) | Approx δx for |δV|=1e−4 (dex) | Allowable first-order |δV| for EKS1 tolerance |
|---|---|---|---:|---:|---:|
| 22 | V0 | [-17.219678,-17.144678] | .0068957745962673 | .01450163410 | 1.37915e−4 at .02 dex |
| 22 | V1 | [-17.144678,-17.069678] | .0074917443602670 | .01334802620 | 1.49835e−4 at .02 dex |
| 22 | V2 | [-17.069678,-16.994678] | .0040123602465333 | .02492298644 | 8.02472e−5 at .02 dex |
| 62 | V0 | [-19.394162,-19.319162] | .0149881823250133 | .00667192311 | 1.49882e−4 at .01 dex |
| 62 | V1 | [-19.394162,-19.319162] | .0135458310144256 | .00738234516 | 1.35458e−4 at .01 dex |
| 62 | V2 | [-19.319162,-19.244162] | .0144642490617336 | .00691359777 | 1.44642e−4 at .01 dex |

## Actual source-native and audit implications

- At j22 V2, a hypothetical ordinate discrepancy 1e−4 implies approx .024923 dex shift, which exceeds EKS1 j22 root comparison acceptance .02 dex. EKS1 .02/.01 windows are comparison windows, NOT numerical error certification.
- At j22 V0 and V1, the same discrepancy corresponds approx .01450 and .01335 dex; at j62 around .00667–.00738 dex. These are different response condition numbers, so a single absolute ordinate tolerance need not imply a uniform root uncertainty.
- The finite grid's V0, V1, V2 source values were each observed increasing between all eight adjacent j22 or j62 sample points (48/48 tested secants >0). This does NOT prove uniqueness or monotonicity between knots.
- The independent GPT L2 operator is `research/mech-s9/2026-11-12/mech_s9_rot008_independent_native_L2_FIXED_INCLUDE.jl` at commit `3d69cfc72fb31fe03e6719f2ea835830ffbb880c`, exact original author `magic()`, original 10D system, independent Float64 q=Q/T linear interpolation and independent bisection, and separate post-run comparison. It has different default result extraction from Badacz DataInterpolations; a discrepancy must be investigated in context of source numeric conditioning BEFORE any physical claim. A short final bisection bracket (~0.00039 dex) measures algorithmic bracket width, NOT ODE error or model accuracy.
- Native workflow `43310359194` was independently checked live at ROT009 report preparation time: exact author source and pinned Julia env PASS, native adaptive L2 solving IN_PROGRESS, artifact and new numeric roots NOT AVAILABLE. This report does not claim L2 PASS.

## Strict ceilings

E4 original physical hadron production blocking still open, published final JCAP figure source build identity unknown, entropy equation, comoving baryon number and late-time hadron dilution source-semantic issues remain from Mech-S9 ROT002/003/004. No physical PBH bound, no new physics, no novelty, no canon, no execution sign. Independent review REC11/AUD1 pending. GitHub write and readback are distinct from BW source-ingest; `GITHUB_PENDING_BW_INGEST`. No full 100×100 and NO_NEW_TASK_CASCADE.
