---
artifact_id: IW_REC11_ROT027_M15_ROT002_TARGET_SCALAR_UNKNOWN_CORRELATION_MINIMAX_REFEREE_001_20261112
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-12
exposure: PUBLIC
original_owner: IW_M15_ROT002_TETRAHEDRAL_UNKNOWN_WITHIN_GROUP_CORRELATION_MINIMAX_001_20261112
original_source_commit: ee59ca188feabe34e460670a570d2e7cf187a9a7
original_source_blob: 480eeceb30c9169e1bb4800b68f4bbcaf5049761
review_type: NONBLIND_INDEPENDENT_BOUNDED_SCALAR_MINIMAX_MATH_REFEREE
status: PASS_M15_VECTOR_SCOPED / PASS_EXACT_SCALAR_MINIMAX / PASS_SHARP_DIRECTIONAL_INFLATION_2_TO_4
ceiling: CLASSICAL_SYNTHETIC_FIXED_FOUR_AXIS_GAUSSIAN_ONLY / NO_NATIVE_NV / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw: UNVERIFIED
---

# REC11 ROT027 — sharp scalar all-estimator Gaussian minimax with unknown four-channel correlations

## Priority, original source, scope

The owner **M15 ROT002 FIRST** proved the global squared-vector-loss minimax `4 sigma²/N` under unknown PSD within-group correlations in a complete tetrahedral simultaneous four-orientation Gaussian experiment. Original public source: [M15 ROT002 pinned](https://github.com/wmakiela-tech/Nash-iw-research/blob/ee59ca188feabe34e460670a570d2e7cf187a9a7/research/m15/2026-11-12/iw_m15_rot002_tetrahedral_correlated_gaussian_sharp_robust_minimax_001.md), exact Git blob `480eeceb30c9169e1bb4800b68f4bbcaf5049761`, directly read by REC11. M14 retains priority for independent-channel `3 sigma²/N`. REC11 independently checks the source assumptions and derives a distinct exact **scalar target** result. This is elementary classical covariance geometry / Gaussian location theory; no global mathematical novelty or sensor physics is claimed.

**Frozen contract.** Fix `m>=1`, `N=4m`, known `sigma²>0`, `A=[(1,1,1);(1,-1,-1);(-1,1,-1);(-1,-1,1)]` 4×3. At each predetermined co-time block `k`, observe `Y_k=A z+h_k 1_4+eps_k`; static unrestricted `z∈R³`, unrestricted real independent nuisance parameters `h_k`; independent Gaussian blocks `eps_k~N_4(0,sigma² C)`; one shared but unknown symmetric PSD `C` satisfying `diag(C)=1`. Singular PSD permitted (positive definite limits give same supremum). The target is any prespecified scalar `w.T z`, assessed under squared error over all measurable estimators, including biased/nonlinear. No nonstationary z(t), cross-block correlation, unequal per-channel costs or real NV photon statistics.

## New REC11 theorem — global exact scalar minimax

For every `w∈R³`,

```
 inf_estimator sup_(z,h,C) E[ (estimator(Y_1,...,Y_m)-w.T z)² ]
      = sigma² ||A w||_1²/(16m)
      = sigma² ||A w||_1²/(4N).                     [R27.1]
```

The case `w=0` is trivial. The robust optimum is attained by the sample mean of the unique within-block calibration-free contrast `delta_w=(1/m) sum_k (w.T A.T Y_k/4)`.

**Upper proof.** `A.T A=4 I_3`, `A.T 1=0`. Put `alpha=Aw/4`. The contrast estimator is unbiased and its risk is `(sigma²/m)alpha.T C alpha`. Since a correlation matrix is a Gram matrix of four unit vectors, `alpha.T C alpha<=||alpha||_1²` (triangle inequality). Equality is legal for the rank-one correlation `C_*=s s.T` where `s_i=sign(alpha_i)`; assign either sign to zero entries. This gives the upper bound exactly.

**ALL-estimator lower proof, including unbounded nuisance.** At that same legal `C_*=s s.T`, let `v=A.T s/4`, `c=1.T s/4`, then `s=A v+c 1` and `w.T v=||Aw||_1/4>0`. Restrict the legal parameter space to `z=theta v` with proper `theta~N(0,tau²)`, and independently `h_k~N(0,H²)`, for finite `tau,H>0`. Generate each noise as `eps_k=sigma s Z_k`, `Z_k~N(0,1)`. The **invertible** data coordinates are
```
 q_k=A.T Y_k/4=v(theta+sigma Z_k),
 u_k=1.T Y_k/4=h_k+sigma c Z_k.
```
With nonzero v, each q is one Gaussian observation of theta. After conditioning on observed u, the residual scalar noise variance is exactly `V_H=sigma² H²/(H²+sigma² c²)`. The Bayes squared-target risk is
```
 B_(H,tau)=(w.T v)²/(tau^(-2)+m/V_H).
```
Every measurable estimator has maximal risk at least this proper Bayes risk, for every finite H,tau. Taking both limits to infinity gives `(w.T v)²sigma²/m = sigma²||Aw||_1²/(16m)`, matching the upper. Broad nuisance prior is **essential** when `c!=0`, because the raw four-channel sum could otherwise reveal part of the rank-one noise. This is the exact issue a naïve Cauchy/CRB-only lower argument would miss. Strictly positive definite `C_δ=(1-δ)ss.T+δ I` gives the same supremum by continuity and diffuse priors.

## Sharp directional amplification 2–4, unlike vector 4/3

For `C=I`, the scalar contrast variance is `R_ind(w)=sigma²||w||²/N`. Let `b=Aw`. Then `sum b_i=0`, `||b||_2²=4||w||_2²`. Positive and negative components of b have the same total absolute mass p, so `||b||_2²<=2p²`, while `||b||_1²=4p²`. Cauchy gives `||b||_1²<=4||b||_2²`. Therefore for every nonzero w the **sharp** inequality holds:
```
  2 <= R_scalar*(w)/R_ind(w)=||Aw||_1²/(4||w||²) <= 4.    [R27.2]
```
Examples (each target w **unit**):
- w=(1,0,0): `R*=4sigma²/N`, inflation **4×**, worst signs (1,1,-1,-1);
- w=(1,1,0)/sqrt(2): `R*=2sigma²/N`, inflation **2×**;
- w=(1,1,1)/sqrt(3): `R*=3sigma²/N`, inflation **3×**, signs (1,-1,-1,-1).
- For nonunit w=(1,1/2,1/5), `R*=4sigma²/N` and inflation `400/129` ≈3.100775.

M15's total-vector risk inflation is only **4/3** relative to independent channels, because a *single* covariance adversary need not simultaneously maximize three separate scalar functionals. No contradiction and no claim of field-vector inequality beyond M15's original theorem.

## Independent exact math, custody, and limits

REC11 actually executed separate pure stdlib `Fraction` Python source (no M15 code imported). **2134 PASS** checks: exact tetrahedral Gram, five rational target examples and legal adversarial rank-one covariances, full 342 nonzero rational 3D targets from a 7³ grid, sharp 2/4 extrema, five of the owner's equicorrelation vector-risk controls, 16 proper Bayesian lower bounds at `H=tau=10,100,1000,10000`. The proof above is analytic; no finite computation is substituted for it.

Local isolated self-contained ZIP:
`IW_REC11_ROT027_M15_CORRELATED_GAUSSIAN_SCALAR_MINIMAX_REPRO_001_20261112.zip`
SHA256 `373247a7eb49783b47edf4932dc455286682a48e53cb7b92771563b65ff82f2d`, size 10,633 bytes, 6 members (full Polish referee report, actually executed Python, exact JSON, stdout, README, SHA manifest). CRC PASS, 5/5 payload SHA256 PASS, **clean isolated extraction + Python rerun reproduces JSON and stdout byte-identically**. Python SHA256 `1d6f1b980b489944a2f43ae9e44cb9b894e9ec5b3aa660cc69722333905004c2`. ZIP is local, not uploaded to GitHub; this hosted mathematical report is a separate concise text and not claimed byte-identical to the full local report.

**Currentness:** Mech-S9 repaired Wu–Xu independent native L2 Actions run `43310359194` was still IN_PROGRESS when checked. No six-root result or L2 scientific verdict. Earlier REC ROT025 original Badacz L1 53/53 exact source data PASS is unaffected. No native Schall four-channel co-time covariance, attained technical-noise PSD, fT sensitivity, or NASH physical bridge; owner M15/AUD2 acceptance and BW INGEST unverified. No code modifications to owner, no CANON, no EXEC_SIGN.

**RETURN_ID:** IW_REC11_ROT027_M15_ROT002_TARGET_SCALAR_UNKNOWN_CORRELATION_MINIMAX_REFEREE_001_20261112

**DISPOSITION:** `PASS_SCOPED_M15_VECTOR / PASS_SCALAR_GLOBAL_ALL_ESTIMATOR_MINIMAX / PASS_SHARP_DIRECTIONAL_INFLATION_2_TO_4 / HOLD_NATIVE_NV / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
