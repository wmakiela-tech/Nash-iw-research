# IW / M13 — ROT36: globalna odległość projektowa przy zagnieżdżonych maskach DTC0a

**RETURN_ID:** `M13-ROT36-DTC0A-GLOBAL-SHELL-PROFILE-SEPARATION-AND-B26-FOLD-001_20261025`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**PROBLEM:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**TYPE:** EXACT CLASSICAL COVARIANCE/PROJECTIVE-GAIN ALGEBRA + SOURCE-SPECIFIC NUMERICAL NONLOCAL PARAMETER SEPARATION. NO NEW PHYSICS.  
**GATES:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 1. Currentness and subtraction

- ROT23–27 reconstructed the source finite Fourier family, RMS series and exact continuum source limit. ROT29–31 gave broader nonmaps for arbitrary low-band sources/TT; these do not contradict source-constrained inversion.
- ROT32–33 established one-common-amplitude identifiability of `alpha` from different source channels A/C, with an interval source certificate in ROT33.
- ROT34 classified **30 single-channel two-mask ratios** (`18` strictly monotone, `12` with source-certified folds), including the B2/6 fold.
- ROT35 **already** derived the nested-mask covariance and independent shell decomposition and calculated **local** profiled Fisher information. MT13 independently owns general gain-nuisance projective geometry/noise-balls. This report does not present either as new.

**ROT36 delta:** evaluate *nonlocal*, gain-profiled separation of a known N41 source model from every alternative at least `Delta alpha = 0.01` away; optimize mask-pair choices globally, compare them with locally Fisher-optimal pairs, quantify a concrete B2/6 fold and show the information provided by the remaining masks.

## 2. Precisely declared source and observation host

Grid N41, 3D odd periodic torus, retained DTC0a generator `C1=(0.05 sin x,0.05 cos y,0)`, `C2=(0.04 cos z,0,0.04 sin x)`, `h=0.1 sin x cos y I`; original source's centered derivative, filter `E_lin=I+alpha dx²Delta_N`, Fourier `P_TT`. We **do not rerun the operator** in this rotation. We consume the 15 channel/mask quartic squared-RMS models `g_{j,k}(alpha)` from ROT32, whose N41 historic `45/45` frozen RMS values were independently matched to relative error at most `1.4433e-14` here and source-controlled in ROT32–34. The original `dtc0a_runtime_v0_3_1.py` bytes remain unavailable.

For one channel j at a time, observation of five **squared RMS** means `Y_k=t*g_{j,k}(alpha)+noise`, `k=2..6`, with **one** unknown common positive `t=s²` (same for all masks). Use ROT35's **synthetic** iid per-voxel additive *energy* noise `eta_v ~ N(0,tau²)`, leading to known covariance `Cov(Y_k,Y_l)=tau²/n_min(k,l)`. After the exact shell unmixing matrix `B`, `m(alpha)=B*g(alpha)`, the five independent shell observations have inverse-covariance metric `W=diag(v)` with shell counts `v=(7778,6938,6146,5402,24389)`.

**Positive-scale profiled distance (units of squared-RMS times sqrt(voxel count)):**

`d_j(alpha,beta;I) = min_{t>=0} ||U_I (g_j(alpha)-t*g_j(beta))||_{W_I}`,

where `I` is the five-mask set or a mask pair, and `W_I` is the inverse of its covariance matrix divided by `tau²`. For full five masks use `U=B,W=diag(v)`; for pairs use the mask selector and exact inverse covariance. Positive source norm vectors ensure the fitted scale is strictly positive:

`t* = <u(alpha),u(beta)>_W / ||u(beta)||_W²`,

`d² = ||u(alpha)||_W² - <u(alpha),u(beta)>_W²/||u(beta)||_W²`.

The source-specific **global conditional separation** is `D_j(alpha;I,Delta)=min_{0<=beta<=.2, |beta-alpha|>=Delta} d_j(alpha,beta;I)` at Delta `.01`. The minimization is **NUMERICAL**: bounded minimization plus independently checked 4097-point grids on every admissible interval. The source polynomial coefficients are floating-point reconstructions; the global minima are **not** interval-certified. The covariance projection and minimax gain formula are exact classical algebra, separately checked with Python `fractions`.

To express distances in a noise-specific unit, for each channel choose `tau_j = 0.01*g_{j,2}(alpha=.05)` (1% *per-voxel energy* standard deviation, **not** 1% error of each observed RMS or mask mean). All comparisons across channels should be treated as separately normalized synthetic hosts, **not physically measured precision**.

## 3. Results for alpha=true 0.05

| Channel | Best two-mask pair by global Delta=.01 separation | D_pair/tau | D_all5/tau | All5/pair distance gain |
|---|---|---:|---:|---:|
| A | (2,5) | 1.388267 | 1.453699 | 1.0471 |
| B | (2,6) | 564.969374 | 578.077189 | 1.0232 |
| C | (2,3) | 100.275312 | 109.870071 | 1.0957 |

At this anchor the closest alternative is `beta≈0.06` for all three full five-mask measurements. Under the **conditional** Gaussian five-dimensional noise law, a 95% noise ellipsoid has radius `sqrt(chi²_5(0.95))=3.32723574360` in whitened units. A sufficient separation criterion for two such error balls is `D/tau > 6.65447`. Thus this specific synthetic host does **not** establish disjoint 95%-radius balls for A (1.45), but does for B and C (>100). This is a conditional error-ball geometry check, **not** a real experimental power/significance assessment. In particular the tau's are independently channel-normalized.

## 4. Global versus local: design depends on the target

The best global two-mask pair need not be the best pair by the *local* Fisher derivative. Exact local tangent is

`sqrt(J_0)=||u'(alpha)-u(alpha)<u,u'>_W/||u||²||_W`,

and `d(alpha,alpha+delta)/|delta| -> sqrt(J_0)`.

`verify_m13_rot36.py` tests the limit at 27 nonzero increments with max relative mismatch at `delta=1e-5` below `1.83e-4` (finite-difference truncation).

For anchor `alpha=0`:

- Channel **B**: global-best pair `(5,6)`, local Fisher-best `(2,4)`; full-five global distance exceeds global-best pair by factor **2.6701**.
- Channel **C**: global-best pair `(2,3)`, local Fisher-best `(2,4)`; full-five/global-best factor **1.1038**.
- Channel **A**: both methods select `(2,5)` in the seven anchors tested.

Over anchors `(0,.02,.05,.10,.15,.18,.2)`, optimal pairs for B change with alpha: `5/6` at `0`, `3/6` at `.02`, `2/6` at `.05`, `2/5` from `.10` onwards. Therefore no universal optimal pair can be claimed without specifying the parameter range, loss and noise law.

## 5. B2/6 fold: source-specific global falsifier

At true `alpha_1=0` and channel B, solve the quartic source-ratio equation `g_B,2(beta)/g_B,6(beta)=g_B,2(0)/g_B,6(0)`, using source coefficients. The second positive root is

`alpha_2 ≈ 0.015151964071294542`,

and the best refitted gain in squared-RMS units for the two-mask observation is `t_2/6≈0.9109103178137407`. Thus

`d_B(alpha_1,alpha_2; masks2/6)=9.86e-28` in the direct double-precision evaluation (zero to numerical accuracy), consistent with the ROT34 rigorous interval-certified fold.

The **same** pair of parameter hypotheses does NOT align all five masks: after independently reoptimizing the common gain across all five,

`d_B(alpha_1,alpha_2; all five)=1.6741727946781903e-13` source-energy weighted units,

or `d/tau_B=273.2424015` in the declared synthetic host. This is a concrete source-model rescue of a folded **two-mask** readout by **five-mask** overidentification. Full-five noiseless projective injectivity on alpha0..0.2 also follows from ROT34's interval-certified strictly monotone B5/6 ratio; it is NOT proven by the 7-anchor numerical test alone.

## 6. Numerical replay and adversarial limits

- Frozen N41 alpha 0,.05,.2 × masks 2..6 × three channels: **45/45** matched, max relative deviation `1.4433e-14`.
- Seven true-alpha anchors for each of three source channels, all ten two-mask combinations plus full-five => `21*(10+1)=231` numeric globally profiled scenarios. Each admissible alternative interval independently dense-tested with 4097 uniform points plus a bounded minimizer.
- Exact rational control: 25/25 shell covariance matrix elements; 150/150 positive-gain projection/Pythagoras identities with independently randomized rational source vectors.
- The five-mask global distance obeys `D_all5 >= D_pair` in every experiment (data processing).
- Local Fisher distance tangent checked at three alphas × three channels × three displacements = **27** checks.

**Restrictions:** This is a known, narrow, functionally source-matched source model. It does not demonstrate mathematical uniqueness for unknown generators, arbitrary TT tensors, independent mask/channel gains, correlated voxel noise of unknown form, or measured physical quantities. The synthetic Gaussian scale is chosen for illustration and is not estimated from data. Gaussian 95%-radius balls are a conditional robust-separation convention rather than a measured confidence statement. Numeric minima are not interval-global certificates; source coefficients inherit ROT32 source-match limitations. No author claims novelty for standard inverse-problem nuisance scaling, Fisher geometry or nested sample covariance.

**Status:** SOURCE_SPECIFIC_NUMERIC_GLOBAL_PROFILE_PASS / EXACT_COVARIANCE_GAIN_ALGEBRA_PASS / B2_6_FOLD_SOURCE_MATCHED / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD.