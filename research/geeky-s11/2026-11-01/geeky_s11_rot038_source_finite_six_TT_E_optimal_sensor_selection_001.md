---
artifact_id: GEEKY-S11-ROT038-SOURCE-FINITE-SIX-TT-E-OPTIMAL-SENSOR-SELECTION-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-01
problem_id: P3_DTC0A_SIX_TT_SOURCE_FINITE_SENSOR_CHOICE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_DIRECT_NUMERICAL_EXHAUSTIVE_708613_EXECUTED_ASSERTIONS_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT038 — choose six TT sideband sensors to improve local finite-source schedule inverse

## Strict prior/source attribution
Geeky ROT015–017 first distinguished non-idempotent even-grid raw Fourier realcast A from correct real TT B=GA; ROT027 uniformly averaged placement of single Lie amid filters; ROT029 exact divided-difference transition; ROT033 variable source filter schedule; ROT034 exact finite-N nonidentifiability of unrestricted schedules from two complete TT fields; ROT035 restricted continuum five sensors KNOWN gain; ROT036 restricted continuum six sensors UNKNOWN gain plus finite-grid inverse mismatch; ROT037 first locally inverted exact SOURCE-FINITE six-sensor map and certified Jacobian det on N24/32/48/64. ROT038 does not reattribute those claims. New delta: choose DIFFERENT SIX TT readings in SAME restricted finite-grid model to improve source-normalized noise sensitivity. E-optimal experimental design, SVD, Fisher information are classical (e.g. Telen et al., AIChE J. 2014, and E-optimal sensor placement studies), no mathematics novelty.

Source is the UNCHANGED auxiliary helper deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Historical production dtc0a_runtime_v0_3_1.py bytes unavailable. Full unmasked periodic even real symmetric TT B=GA (not original flawed realcast), source centered full THREE-term Lie C=(0,cos x,0), scalar Ealpha=I+alpha*h²*Delta2. NOT historical masked h=fI K_A experiment.

## Exactly same SOURCE-FINITE inverse as ROT037
Six known accumulated dose levels x_j=j*A/5 with A=.009, ramp dose velocity v=.012, five fixed ramps occupy .75 time, six UNKNOWN strictly positive plateau durations d_j sum D=.25; unknown gain t>0, fixed comparison point t=1.07 and d_j=1/24. For even N, m=round(beta*N²), beta=.12, piecewise linear cumulative dose a_d(t), legal filters alpha_j=N²[a_d(j/m)-a_d((j-1)/m)] in [0,1/6].

For TT H_p=T_p cos(px+y), p>=0, T_p=.3*(ez ez^T-vp vp^T/(p²+1)), vp=(-1,p,0), and target side s=+/-1, the normalized scalar source readout y_(p,s)=t Omega_(p,s) where
Omega=(1/(m+1)) SUM_(ell=0)^m PROD_(j<=ell)(1-4alpha_j a_in) PROD_(j>ell)(1-4alpha_j a_out),
a_in=sin²(pi*p/N)+sin²(pi/N),
a_out=sin²(pi*(p+s)/N)+sin²(pi/N).
This is EXACT within the retained source mathematical protocol, not a continuum diffusion surrogate. Jacobian J_N=[Omega, t*partial_(d0..4)Omega], derivatives from exact product and piecewise ramp sampling. All evaluated away from kink crossing.

## Six-sensor design and CONDITIONAL finite-pool exhaustion
OLD: (2,-),(2,+),(3,-),(3,+),(4,-),(4,+), DeltaK=(-3,+5,-5,+7,-7,+9).
NEW: (0,+),(1,-),(1,+),(2,-),(3,+),(4,-), DeltaK=(+1,-1,+3,-3,+7,-7).

25 declared unique candidate normalized Omega rows: (0,+) and p=1..12, each s=+/-1. (0,-) omitted because it duplicates the spectral DeltaK and normalized Omega of (0,+) under this source C, although they are distinct spatial sideband fields. C(25,6)=177100 six-row combinations. Entire set numerically enumerated at N64 AND N128 with NumPy SVD at exact source finite parameter point. New set simultaneously has maximal numerical sigma_min(J) and minimal numerical kappa2(J) within these 177100; this is not a rigorous interval/global optimizer over arbitrary sensors, parameter values or alternative noise metrics.

Finite N | OLD kappa2 | NEW kappa2
32 | 320436.86 | 37055.88
64 | 539289.54 | 65139.50
128 | 516003.86 | 60505.00
256 | 493809.02 | 58242.02
512 | 491249.57 | 57760.66
1024 | 490841.70 | 57621.84

At N1024: old sigma_min=1.26283514e-6, new=1.64313815e-5, gain 13.0115x; condition improvement 8.5183x. This is LOCAL numerical conditioning, not an all-N/local-neighborhood theorem, nor a physical error guarantee.

## Explicit alternative TT-polarization-aware synthetic noise normalization
For identical-norm TT H_p and independent equal-variance additive readout error in matched UNIT-NORM output TT sideband directions, spectral Omega row must be weighted by
w_(p,s)=||P_TT(kout)(T_p+s*W_p)||_F/(2||T_p||_F),
W_p=ex(T_p ey)^T+(T_p ey)ex^T, ignoring common d_N=sin(h)/h across channels. This is a DECLARED alternative noise host, not real calibration. Independent 3x3 projection and stdlib Fraction exact polarizations validate all six selected NONZERO TT outputs including p0 and p1. For N128 weighted J^w:
old sigma_min=4.84807e-7, kappa2=944176;
new sigma_min=7.17707e-6, kappa2=82252;
sigma_min improvement 14.804x. Exhaustive weighted E-optimal set is AGAIN the same new six. But weighted condition-minimizing set DIFFERS: (0,+),(1,-),(1,+),(3,-),(3,+),(4,-), kappa2=71688.52. Thus do NOT equate maximizing min singular Fisher sensitivity with minimizing condition under a changed noise law.

With stipulated independent Gaussian noise variance sigma² in these unit-TT channels, Fisher information is F=(J^w)^T J^w/sigma², E-optimal criterion maximizes lambda_min(F). A deterministic linearized inverse error has upper bound eta/sigma_min, without positivity constraints. No actual observed noise, no universal practical inverse success claimed.

## Additional continuum nonzero determinant certificate (NOT finite global injectivity)
For same six known dose levels and known linear ramps, continuum Omega=b+Wd and observations y=t(b+Wd). Reparameterize z=(t,t d0,...,t d4), so y=M z, M=[b|W]. For the NEW 6 rows the independent 85-digit mpmath.iv directed interval 720-term determinant strictly encloses det M=+5.34105382238082986e-13, versus baseline -4.05008860917976623e-16. Therefore THIS restricted CONTINUUM affine gain+dwell model is globally identifiable for the new six readings. Not a formal proof assistant, mpmath.iv interval is experimental, no finite N global identifiability theorem. Source original helper full 3D confirms p0/p1 signals are NONZERO (not projection artifacts).

## Independent executed controls and custody
(A) 354221 actually executed source finite Fourier Jacobian tests and 2*177100 numerical unweighted SVD candidate subset assertions; includes N32..1024 pointwise transport comparisons.
(B) 354251 independent matched-polarization weighted and independent forward finite-difference Jacobian checks, plus 2*177100 weighted SVD subset assertions.
(C) 80 literal UNCHANGED original helper real N³ tensor FFT full Lie/TT/E at N12/16, for every selected p/s (max normalized discrepancy 2.1245e-16).
(D) 50 separate stdlib Fraction exact rational TT projection/p0/p1 spectral geometry checks.
(E) 11 independent 85-digit experimental interval determinant comparisons for old and new continuum six-sensor models.
TOTAL **708613/708613** executed typed assertions PASS. Most are deterministic numerical candidate assertions, NOT separately independent mathematical experiments.

Complete user-conversation LOCAL reproducibility ZIP GEEKY_S11_ROT038_SOURCE_FINITE_SIX_TT_SENSOR_DESIGN_REPRO_001.zip SHA256 8e1df0c56dae014ddac962494ecca09c4c262181f4cf7da097af895536ef7d94. Full Polish expanded report+FIVE standalone scripts+FIVE JSON+FIVE stdout, frozen auxiliary source and README+SHA manifest. CLEAN extraction ZIP CRC PASS, 18/18 content SHA256 PASS, five clean Python reruns and five resulting JSON BYTE IDENTICAL PASS. Local code/ZIP NOT claimed separately hosted on GitHub.

Scope/claims: numerical exhaustive selection CONDITIONAL on finite 25-pool, exact source-finite local d/gain point and stated noise normalization; certified continuum det not universal finite N inverse; no original historic production/masked K_A, NCDG physical J3/K, GR/GW/PBH, owner/peer referee/BW, CANON or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
