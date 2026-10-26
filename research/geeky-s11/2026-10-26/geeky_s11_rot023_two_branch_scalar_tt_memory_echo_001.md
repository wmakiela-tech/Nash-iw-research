---
artifact_id: GEEKY-S11-ROT023-TWO-BRANCH-SCALAR-TT-MEMORY-ECHO-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_FULL_REAL_RAW_TT_MEMORY_SCALAR_IDENTIFIABILITY_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_RATIONAL_SCALAR_MEMORY_ECHO_TWO_BAND_ALL_REAL_ALPHA
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT023 — finite-time scalar two-branch TT memory echo, all alpha

## Scope and source credit

The retained auxiliary helper deepseek_python_20260627_a87249.py, SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, supplies source-type centered D, three-term Lie and raw-k P. Its real-cast raw TT map A is NOT a projector on even grids (Geeky ROT015). ROT016-017 first constructed the genuine orthogonal real raw-TT-compatible B=GA by removing mixed-Nyquist frequencies. ROT021 first proved the p2 fixed smooth Fraction witness 1643/20000 and ROT022 first proved Mori-Zwanzig projected-flow memory and frequent-projection limit. ROT023 extends those to one scalar terminal observation per branch, two independently prepared smooth TT carriers, and a nonzero finite-time guarantee for ALL real scalar filter strengths. Existing Mori-Zwanzig/Chapman-Kolmogorov theory is mature; no novelty claim. PRF12 quantum memory, INT8 geometric TT and M14 original masked puretrace h=fI KA are different scopes. Original DTC production dtc0a_runtime_v0_3_1.py is not available.

## Exact controlled contrast

On even N>=12, h=2pi/N, full normalized real tensor L2, let C=(0,cos x,0), L=the FULL centered covariant Lie derivative, Q=I-B and Ealpha=I+alpha h^2 Delta2 applied ONCE initially. Define F(t)=B exp(tL) B. For B-TT input H define the scalar-only two-branch diagnostic

D_H(tau,alpha)=<H,[F(2tau)-F(tau)^2] Ealpha H>/<H,H>.

Branch one evolves for 2tau with only final B. Branch two evolves tau, projects B, evolves tau, finally projects B. The scalar is a signed projection onto the originally prepared tensor, not the full tensor output; one scalar reading is taken from EACH branch. This is an active controlled intervention, not a passive time-series Markov test. Exactly

F(2tau)-F(tau)^2=B exp(tau L) Q exp(tau L) B.

## Two fixed smooth rational TT carriers

For p=2,3 let k=(p,1,0), v=(-1,p,0), T_p=(3/10)(e_z e_z^T-vv^T/(p^2+1)), H_p=T_p cos(px+y). Both H_p and C are fixed smooth as N changes; H_p is exactly B-TT and ||T_p||F^2=9/50. In the +1 y-frequency band the centered L equals d_N times the continuum Lie matrix, with d_N=sin(2pi/N)/(2pi/N). Exact stdlib rational sideband projection gives

[B L Q L B H_p] at its own k = c_p d_N^2 H_p,

c2=1643/20000=0.08215 (PRIOR ROT021), while the second rational carrier has c3=261977/5780000=0.04532474048442907. No claim the OTHER output frequencies vanish.

Source scalar filter e_p(N,alpha)=1-4alpha a_p, with a_p=sin^2(pi p/N)+sin^2(pi/N). Hence each scalar echo is

D_Hp(N,alpha,tau)=e_p(N,alpha)[c_p d_N^2 tau^2+R_p(N,tau)].

Since ||L||<=3 on each invariant ky=+/-1 sector and an odd number of x-shifts cannot return to its starting x-frequency on even N, the expansion of this particular scalar is EVEN in tau. A uniform exact remainder follows from summing all Taylor orders >=4:

|R_p| <= cosh(6tau)-1-(6tau)^2/2.

Take tau=.01. The remainder is at most 5.400648042347238e-7. Since for all even N>=12 d_N^2>=(3/pi)^2, BOTH unfiltered scalar echoes are positive and >=

g0=c3 (3/pi)^2 (.01)^2 - remainder = 3.5930559145130016e-6.

For arbitrary real alpha the factors e2 and e3 cannot vanish simultaneously. Set a=a2,b=a3. Direct two-sample minimax gives max(|1-4alpha a|,|1-4alpha b|)>=(b-a)/(b+a). For x=pi/N<=pi/12, b-a=sin^2(3x)-sin^2(2x)>=(72/pi^2-4)x^2, and b+a<=15x^2. Therefore rho0=(72/pi^2-4)/15=0.21967501481655 is a certified all-N lower bound.

**ALL-REAL-ALPHA FINITE-TIME SCALAR CERTIFICATE:**
max_{p=2,3}|D_Hp(N,alpha,.01)|
 >= rho0 g0 = 7.89304611257353e-7
for every EVEN N>=12 and EVERY real alpha, including alpha chosen adversarially as a function of N.

One carrier can be blinded by setting alpha=1/(4a_p); the TWO together cannot. This is a mathematical absolute signed-readout certificate, not physical detection performance. If each of two final scalar branch readouts has an explicitly assumed deterministic error <=eta, the difference error <=2eta, so eta<3.946523056e-7 is sufficient for guaranteed nonzero detection in at least one contrast. A trace-only observable is blind since the B outputs are traceless.

## Independently executed controls and reproducibility

First fully independent 6N signed Fourier sparse matrix/scipy expm script with all tensor Lie derivative terms plus exact Python fractions: N12,16,20,24,32,48,64,96,128,256, two TT carriers, seven alpha cases including zero, source .05, negative, two filter roots, minimax and huge 1e8: 150 typed assertions PASS. It compares the actual finite two-branch exponential, rational memory coefficient, Taylor error, filter minimax and unchanged original helper's TT status.

Second independent FULL N^3 real tensor program directly invokes literal original source functions lie_derivative_tensor/apply_P_TT/apply_E and overlays compatible Nyquist guard; performs two nine-term real-space Taylor evolutions, and compares final scalar to sparse-matrix values. N12,16,24 x both carriers plus original helper E controls: 24/24 PASS, maximum full-grid-versus-sparse scalar gap 1.117119566881701e-15. Combined 174 typed checks PASS, NOT 174 physical datasets.

Sample unfiltered scalar echoes at tau=.01:
N12 p2 7.49085e-6; p3 4.13291e-6.
N32 p2 8.10958e-6; p3 4.47428e-6.
N128 p2 8.20801e-6; p3 4.52859e-6.
N256 p2 8.21295e-6; p3 4.53131e-6.

A complete expanded 11KB report, both standalone executed scripts, both JSON outputs, immutable original helper, README, stdout and nine-content-entry SHA manifest are stored in the local user-conversation ZIP GEEKY_S11_ROT023_SCALAR_TT_MEMORY_ECHO_ALL_ALPHA_REPRO_001.zip, SHA256 8f99864d211ff00af2047b40ecee32d8b77b57c4a73e4e1a1065528ce248d7dd. Clean extracted ZIP CRC, SHA256 9/9, and independent reexecution of BOTH scripts with BYTE-IDENTICAL outputs PASS. This report publication does NOT claim separate GitHub code upload.

## Guardrails

No claim of real-world non-Markovian TT dynamics, original history masked source h=fI K_A, an NCDG K/J3 gauge invariant, GR/GW/PBH/BBN prediction, original missing DTC production binary, theorem priority, mathematical novelty, independent referee, BW ingestion or Moderator EXEC. No new tasks or automatic owner promotion.

NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING.
