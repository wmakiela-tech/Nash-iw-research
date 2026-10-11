# INT7 Thread091 — G_TIME observation-resolution diffusion mismatch

RETURN_ID: INT7-THREAD091-GTIME-OBSERVATION-RESOLUTION-DIFFUSION-MISMATCH-001
DATE: 2026-10-11

Consider on fixed horizon T:
dX = mu dt + sigma dW,
dY = mutilde dt + sigmatilde dW.

Observe n equal increments, Delta=T/n.

Each increment is Gaussian:
P: N(mu Delta, sigma^2 Delta)
Q: N(mutilde Delta, sigmatilde^2 Delta).

Let r=sigma^2/sigmatilde^2.

Exact KL for the n-increment experiment:
KL(P_n||Q_n)
=
n/2 [r-1-ln r]
+
T (mu-mutilde)^2/(2 sigmatilde^2).

Therefore:

DRIFT MISMATCH:
fixed-horizon KL contribution is finite and independent of sampling resolution n.

DIFFUSION MISMATCH:
for any fixed r != 1, KL grows linearly with n.

Pinsker:
TV(P_n,Q_n) <= sqrt(KL/2).

So a sufficient TV<=epsilon certificate is:
n[r-1-ln r] + T(mu-mutilde)^2/sigmatilde^2 <= 4 epsilon^2.

For sigma=sigmatilde(1+delta), small delta:
r-1-ln r = 2 delta^2 + O(delta^3),
hence KL_diffusion ~ n delta^2.

Thus finite-readout closeness under increasing resolution requires approximately:
|delta| sqrt(n) << 1.

For zero drift mismatch the Gaussian affinity is:
Aff(P_n,Q_n)
=
[2 sigma sigmatilde/(sigma^2+sigmatilde^2)]^(n/2).

If sigma != sigmatilde, Aff -> 0 as n -> infinity, hence TV -> 1.
This is the finite-readout precursor of continuous-path quadratic-variation singularity.

Core scientific consequence:
PROCESS APPROXIMATION + OBSERVATION CONTRACT is required.

A pair of process models can be approximately equivalent at coarse resolution and nearly perfectly distinguishable at fine resolution.

Therefore:
FINITE-READOUT CLOSENESS != CONTINUOUS-PATH CLOSENESS.
DRIFT ERROR SCALING != DIFFUSION ERROR SCALING.
ONE TV BOUND AT FIXED n != RESOLUTION-UNIFORM DEFICIENCY BOUND.
SMALL DIFFUSION PARAMETER ERROR != SMALL FULL-PATH LAW ERROR.

Blackwell/Le Cam placement:
for each fixed n, the finite Gaussian readout gives a regular statistical experiment and exact law-distance certificate.
No n-independent small-deficiency claim follows for fixed diffusion mismatch as resolution increases.

For G_TIME OU:
common diffusion retains the Girsanov branch.
Different diffusion requires comparison at the actual admitted finite observation law, e.g. Gaussian state-space mean/covariance KL on the declared readout grid.

VERDICT:
FINITE_READOUT_DIFFUSION_MISMATCH_KL_PASS /
DRIFT_VS_DIFFUSION_RESOLUTION_SCALING_SPLIT_PASS /
CONTINUOUS_PATH_SINGULARITY_RECOVERED_AS_RESOLUTION_LIMIT /
OBSERVATION_CONTRACT_LOAD_BEARING /
G_TIME_DIFFUSION_MISMATCH_BRANCH_SHARPENED /
NO_NEW_GENERAL_THEORY.

REV020 ACTIVE / TPE HOLD / NO NOVELTY / NO HARDWARE GO.
