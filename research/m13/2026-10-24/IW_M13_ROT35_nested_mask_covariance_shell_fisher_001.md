# IW / NASH — M13 ROT35: zagnieżdżone maski, rozłączne powłoki i uwarunkowana informacja Fishera

**RETURN_ID:** `M13-ROT35-NESTED-SHELL-COVARIANCE-AND-CONDITIONAL-FISHER-001_20261024`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-24  
**PROBLEM:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**CLASS:** EXACT CLASSICAL NESTED-AVERAGE COVARIANCE + SOURCE-MATCHED LOCAL FISHER PROFILE UNDER DECLARED SYNTHETIC NOISE  
**GATES:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / TPE HOLD`.

## 1. Scientific difference and priority

ROT18/23/27/28 established the historical moving mask, replayed source operators, extracted shell energies and mask bias. ROT29–31 proved strong non-identifiability for broader classes of fields. ROT32–33 certified source-constrained two-channel alpha/common-gain inversion, and ROT34 certified 18/30 monotone pairs for one channel, testing **bounded unknown relative error per mask** without assuming a covariance model. MT13 had already established projective nuisance-gain / noise geometry; do not reassign that result.

**ROT35 delta:** derive the exact measurement covariance when all five nested mask averages share the SAME noisy voxel energies; calculate the equivalent independent disjoint-shell observations; profile a common unknown amplitude to quantify **local** alpha information for the source-matched quartic RMS family. Optimize pair choice **under this new explicitly conditional noise law**, and falsify naive diagonal covariance. No claim that actual DTC0a voxel fields are independently noisy.

## 2. Inputs / source-boundary

N=41 odd periodic 3D grid, masks `k=2,3,4,5,6` on cube indices `[k:N-k)^3`, central second-order difference stencil, filter `E_lin=I+alpha dx² Δ_N`, Fourier `P_TT`, source generators `C1=(.05 sin x,.05 cos y,0)`, `C2=(.04 cos z,0,.04 sin x)`, `h=.1 sin x cos y I`.

For each channel j=A,B,C, denote known **source-family** quartic squared-RMS `g_{j,k}(alpha)` obtained by M13 ROT32 (source-matched NUMERIC coefficient reconstruction, separately interval-checked in ROT33/34). Independent readback original helper remains unavailable byte-for-byte; historical RMS CSV at N41 k2..6 alpha0,.05,.2 used as frozen verification (**45/45**, max relative error `1.45e-14`). This rotation does not evaluate source operator again: it uses established quartic model and historical RMS, and must not be mislabelled as an independent native runtime replay.

## 3. Declared synthetic statistical host

At each voxel `v` in V_2, let an observed **energy-density** response be

`X_v = t e_{j,v}(alpha) + eta_v`, with `t=s²>0` a common unknown positive gain and independently distributed `eta_v~Normal(0,tau²)` **for the exact Gaussian Fisher calculation**. More generally centered independent homoscedastic finite-variance errors suffice for the covariance identity, but NOT for assuming Gaussian Fisher information.

A masked energy average is `Y_k=(1/n_k) Σ_{v∈V_k} X_v`, `n_k=(N−2k)^3`, mean `t g_{j,k}(alpha)`. Correlation comes automatically from the overlapping source voxels. The RMS readout equals `sqrt(Y_k)` when the observed mean is positive; using squared readouts is an invertible transformation on this positive event, but the observation model is in energy units, not additive Gaussian RMS noise. **No real instrument calibration, voxel stochastic independence, or measured tau was supplied.**

Nested covariance is EXACT for this host:

`Cov(Y_k,Y_l) = tau²/n_min(k,l)`, `n_min(k,l)=(N−2 min(k,l))³`.

For five masks `n=(50653,42875,35937,29791,24389)`. Define disjoint shells `W_k=V_k\V_{k+1}` of sizes `v=(7778,6938,6146,5402)` and core `W_6=V_6`, `v_6=24389`. Their energy-average observations are:

`Z_k=(n_k Y_k−n_{k+1}Y_{k+1})/(n_k−n_{k+1})`, k=2..5; `Z_6=Y_6`.

Let `B` be this linear map `Z=BY`. Then `B Σ B^T=tau² diag(1/v_k)` EXACTLY, and B invertible, so full five-mask data and five shell means contain precisely the same information. Exact rational stdlib verification: **25/25 covariance components + 25/25 inverse relations PASS**. Monte Carlo 30,000 jointly Gaussian realizations from shells: maximum relative pairwise covariance discrepancy 2.07%, within prespecified 5.5% sampling tolerance.

## 4. Conditional Fisher information with unknown common gain

For one channel, at alpha, let `m(alpha)=B g(alpha)` be the shell-mean energy shape and `d=dm/dalpha`. With Gaussian additive energy noise, shell inverse covariance is `tau^{-2} diag(v)`. Eliminate `t=s²` by orthogonal weighted projection:

`J0(alpha) = Σ_k v_k d_k² − (Σ_k v_k m_k d_k)²/(Σ_k v_k m_k²)`.

The efficient local Fisher information for alpha is `I_alpha|t = (t²/tau²) J0`. Consequently the **local Cramér–Rao lower bound** is `Var(alpha_hat) ≥ tau²/(t² J0)` for regular unbiased estimators under this host (not a bound guaranteeing the success of a global nonlinear inverse). Equivalence using the full correlated five-mask covariance Σ was checked numerically for 12 cases (channels A/B/C × alpha0,.05,.113,.2), largest relative agreement better than `2e-11`. All 10 two-mask subexperiments carry at most the full-five-mask information (data processing).

Fix alpha=.05, t=1 and illustrative **per-voxel energy-noise standard deviation** `tau=0.01*g_{j,2}(.05)`, which is 1% of the channel's mask-2 squared-RMS baseline **at each voxel**, not 1% relative uncertainty of each mask aggregate:

| Channel | Best pair among k2..6 at alpha=.05, Gaussian energy-noise host | Fraction of full-five information | Conditional local CRLB sigma_alpha with stated tau |
|---|---|---:|---:|
| A | 2/5 | 91.1917% | 0.00686916 |
| B | 2/6 | 96.3609% | 0.0000156748 |
| C | 2/3 | 83.3905% | 0.0000898243 |

These are **model-relative within-channel** comparisons, NOT a ranking of independently instrumented A/B/C channels under a shared empirical noise source. Different channel-specific tau normalizations were chosen deliberately, so absolute numbers cannot be used as evidence one physical measurement is better. In particular B2/6 has an ROT34 **fold**, so excellent *local* information is not *global* identifiability. A/C pairwise channel comparisons from ROT33 require cross-channel covariance, which is absent.

ROT34's robust deterministic-sup-norm monotone-mask criterion selected C2/4. ROT35's **local Gaussian independent-voxel energy host** selects C2/3 (83.39% full-five information vs C2/4 68.28%). This difference is rationally explained by the loss model; it is not contradictory.

## 5. Negative controls and direct numeric checks

1. Historical N41 frozen k2..6 at alpha0,.05,.2 × channels A/B/C =45/45 squared-RMS quartic checks; max relative RMS `1.4433e-14`.
2. Exact shell covariance rational matrix identity verifies 25 elements without NumPy or floating-point.
3. Correlated full-five GLS information equals shell-diagonal information at alpha four points, three channels; covariance round-trip relative error `6.13e-16`.
4. Gaussian shells 30,000 draws sampled with fixed seed recover all pairwise masked covariances, max relative error `0.02069`.
5. Separate linearized Gaussian local-alpha influence-function Monte Carlo with 20,000 independent draws per channel matches calculated standard deviations to within ~0.4%:
   - A empirical/theory = 1.000258;
   - B = 1.001519;
   - C = 0.996058.
   This checks the **local linearization**, not a globally convergent nonlinear estimator or finite-sample attainability.
6. **Negative control:** mistakenly replacing nested-mask covariance by its diagonal produces at alpha=.05 (using same observed mask marginals) only 43.36%, 41.82%, 19.27% of the correctly profiled local information (A/B/C). Hence diagonal treatment changes inference; it **does not always inflate** precision: here it *underestimates* information because correctly exploiting correlated noise improves contrast accuracy. This is more precise than claiming double-counting always leads to false confidence.

## 6. Interpretation / claim ceiling

- Algebraically the five nested mask means are invertible into five disjoint spatial shells; no gain of observations is manufactured.
- Whether any optimal mask pair under the synthetic Gaussian host is meaningful depends on actual spatial correlation, heteroscedasticity, shared algorithmic rounding, and physical readout interface. None is measured here.
- Source quartic coefficients are reconstructed from retained alternative helper, not the unavailable declared byte-exact `dtc0a_runtime_v0_3_1.py`; `K_A` is an ambient residual on pure-trace input, not a genuine TT-restricted physical invariant.
- The Fisher test is an information/conditioning discriminator, not claim of physical discovery, experimental sensitivity, new field dynamics or NASH K/J3/TPE status.
- No independent referee, BW ingestion, owner/EXEC acceptance or new task authorized.

## 7. Reproduction

Stand-alone directory inputs: this report, `verify_m13_rot35.py`, `verify_m13_rot35_exact.py`, ROT32 source quartic JSON, frozen N41 mask CSV, output JSON, README and SHA256SUMS. Run under Python3 with NumPy:

```
OPENBLAS_NUM_THREADS=1 python verify_m13_rot35_exact.py
OPENBLAS_NUM_THREADS=1 python verify_m13_rot35.py
```

`verify_m13_rot35_exact.py` independently verifies the geometry via Python `fractions.Fraction`, without NumPy. `verify_m13_rot35.py` executes conditional Fisher comparisons, noise Monte Carlo, and frozen 45/45; the generated JSON is deterministic under explicit seeds. The root ZIP contains all inputs, outputs and SHA256 manifest; it needs no project connector or prior chat.

**STATUS:** `EXACT_CLASSICAL_COVARIANCE_PASS / CONDITIONAL_FISHER_PASS / 45_FROZEN_RMS_MATCH / SOURCE_TYPED_SYNTHETIC_NOISE / NO_CANON / NO_EXEC_SIGN / TPE_HOLD`.