---
artifact_id: GEEKY-S11-ROT036-SIX-TT-UNKNOWN-GAIN-INVERSE-FINITE-GRID-BIAS-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-29
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT036 — sixth TT sideband identifies unknown gain in the restricted continuum class but the inverse is ill-conditioned

## Ownership and mathematical host

Geeky ROT015–017 first established the proper real even-grid raw-k TT projector B=GA; ROT027/029 established uniform Lie insertion and spectral divided difference; ROT033 generalized to variable stable Ealpha schedules; ROT034 first proved exact finite-grid non-identifiability for two TT output fields and explicit four-moment continuum collision; ROT035 first inverted a SIX-LEVEL restricted continuum dwell family using FIVE TT sidebands with KNOWN gain, proving an unknown-gain continuum family remained. ROT036 DOES NOT reattribute those. Mature linear reparameterization, interval determinant and SVD math; NO novelty.

Frozen unchanged auxiliary DTC0a helper deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, NOT historical production dtc0a_runtime_v0_3_1.py. Full unmasked even N³ real symmetric tensor; genuine source-compatible B; full THREE-term centered Lie with C=(0,cos x,0); stable scalar E_alpha in [0,1/6]. Not masked historic h=fI/K_A or physical GR/GW/PBH/J3.

## NEW exact continuum restricted known-level model

Fixed beta=.12, accumulated dose A=.009, known ramp speed v=.012, six KNOWN dose levels x_j=jA/5, j=0..5, 5 ramps total time .75, six UNKNOWN positive dwell durations d_j with sum D=.25. Stable filter alpha=.1 on ramps and zero on dwell segments. **Common GAIN t>0 unknown**.

Six TT scalar readouts from FULL projected fields: H2-,H2+,H3-,H3+,H4-, NEW H4+; their spectral DeltaK=(-3,+5,-5,+7,-7,+9), all distinct. With Kout=(p+side)^2+1 and lambda=4pi² DeltaK, exact continuum:
Omega_i=exp(-4pi² Kout_i A)[R(lambda_i)+sum_(j=0)^5 d_j exp(lambda_i x_j)]
R(lambda)=(exp(lambda A)-1)/(lambda v).
Write d5=D-sum_(j0..4)d_j, b_i=exp(-4pi² Kout_i A)[R(lambda_i)+D exp(lambda_i x5)],
W_ij=exp(-4pi² Kout_i A)[exp(lambda_i x_j)-exp(lambda_i x5)].
Observed y=t*(b+W d_(0:4)). Set z=(t,t*d0,...,t*d4). Then **EXACT LINEAR** six-by-six y=M z with M=[b|W]. Recover t=z0 and d_j=z_(j+1)/z0, d5=D-sum_(j0..4)d_j.

## R36.1 certified nonzero det for THESE numbers only

Unlike five-sensor exponential Vandermonde, ramp column b is not a point mass and nonzero determinant is NOT asserted universally. Independent 85-decimal-precision directed interval mpmath.iv computation of exact pi, exp and **720 Leibniz signed permutation terms** encloses
det(M) in [-4.050088609179766229235921655742248958085314119986504884012128804373195569993215083e-16,
           -4.050088609179766229235921655742248958085314119986504884012128804373195569986386896e-16].
Both endpoints STRICTLY negative. Separate 105-digit direct reconstruction yields <1e-95 residual. Thus global injectivity for the **specified known-level six-plateau continuum class with one positive unknown common gain**, not general arbitrary schedules. A computer-directed-interval certificate is conditional on the interval backend and not a formal proof-assistant development.

## R36.2 bad practical condition, five-vs-six calibration

SVD of actual unscaled six Omega-units M:
singular values [.568984566,.212175159,.0247225431,.00117596105,9.7676546e-5,1.18138956e-6].
kappa2(M)=481623.153669; ||M^-1||2=846460.8403.
ROT035 calibrated five-sensor W kappa2=70100.4406. A synthetic additive vector perturbation eta=1e-7 in the least stable left-singular direction gives worst **LINEAR** z error eta/s_min=.0846461. In the synthetic interior example t=1 and all d_j=1/24, converting reconstructed z to d yields norm dwell error ~.084809 and smallest dwell -0.010981, outside legal positivity. The unconstrained SVD test is a condition demonstration, NOT an estimate of constrained inversion or measured noise.

The explicit ROT034 two-history continuum pair remains equal for the FIRST FOUR sensors exactly; H4- differs by 4.96109247539e-7 and NEW H4+ differs by 3.74258220579e-8 for their exact source Omega factors. This is not an exact finite-N pair.

## R36.3 silent finite-grid model mismatch falsifier

Legal source finite-N schedules sample a fixed known six-level continuous profile: m=round(.12 N²), alpha_(N,j)=N²[a(j/m)-a((j-1)/m)] in [0,1/6], sum alpha_j/N²=A; true six d_j=1/24 and gain=1.07. Their source EXACT FINITE Fourier averaged Lie symbols from the standalone recurrence are not the continuum affine y=M z.

Feeding these noiseless finite-N data into the CONTINUUM M inverse gives:
N128: Omega mismatch L2=1.08999e-4; d reconstruction error L2=.50427, min recovered d=-.21928.
N256: Omega mismatch=2.71336e-5; d error=.12246, min d=-.02217.
N512: Omega mismatch=6.77661e-6; d error=.03040, min d=.02579.
N1024: Omega mismatch=1.69374e-6; d error=.007585, min d=.03770.
This is an EXECUTED NEGATIVE procedural control: continuum identifiability does not authorize direct continuum inversion of finite-grid data. No claim finite-N exact inverse is singular; a source-discrete calibrated inversion would require new independent work.

## Independent execution and custody

Four standalone programs: (1) mpmath 105-digit inverse/cofactor/gain + NumPy SVD 23 executed typed assertions; (2) INDEPENDENT 85-digit directed interval determinant 11 assertions; (3) LITERAL source helper full REAL 3D three-term Lie/apply_E/apply_P_TT H2/H3/H4 both sidebands N12/16, 42 assertions, max relative gap 2.421641269105601e-16; (4) independent six-sensor finite schedule recurrence and continuum-bias N24..1024, 39 assertions. **TOTAL 115/115 PASS**. Original tests while constructing scripts that failed through an incorrect five-vs-four equality assertion, a transposed SHA pair, and a mistyped counter were fixed before final 115 and not counted.

One Moderator-local self-contained ZIP GEEKY_S11_ROT036_SIX_TT_UNKNOWN_GAIN_IDENTIFIABILITY_FINITE_GRID_BIAS_REPRO_001.zip contains full Polish 10.6 KB proof, FOUR runnable Python scripts, FOUR JSON, FOUR stdout logs, README, SHA manifest, unmodified helper. ZIP SHA256 dc7d44a64cb1a761a0a27bc98c0b7333ac4eca1b65b0711d38947615b25decbc; independent clean extraction CRC PASS, manifest SHA256 15/15 PASS, FOUR scripts rerun, FOUR JSON BYTE IDENTICAL PASS. ZIP and scripts local to Moderator conversation, not claimed separately uploaded to GitHub.

NO historical K_A, physical J3/K or GR/GW/PBH, empirical calibration, independent scientific referee, BW ingestion, CANON or EXEC. NO_NEW_TASK.
