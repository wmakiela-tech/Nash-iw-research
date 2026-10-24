# MT13 ROT038 — source-specific rational Bernstein certificates for globally rejecting M13 DTC source families

Date 2026-10-25
RETURN_ID MT13-ROT038-M13-LT5-DUAL-BERNSTEIN-GLOBAL-SOURCE-SEPARATOR-001_20261025
PROBLEM_ID P3-DTC0A-SOURCE-CONSTRAINED-PROJECTIVE-FALSIFICATION
STATUS EXACT_FINITE_DECIMAL_CERTIFICATE / SYNTHETIC_GAUSSIAN_TEST / NO_NOVELTY / NO_PHYSICAL_CLAIM / NO_CANON / NO_EXEC / OWNER_ADOPTION_PENDING / BW_PENDING

## Others first
M13 ROT32–34 originally owns N41, masks k2..6, three channels A/B/C source-matched quartic g_{j,k}(alpha)=RMS², one shared positive energy scale t=s², legal alpha∈[0,.2]. Source coefficients are in https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/IW_M13_ROT32_alpha_amplitude_identifiability_001.json
M13 ROT35 owns exact nested-mask covariance and transform to five independent disjoint shell ENERGY means, local profiled Fisher under its declared SYNTHETIC iid Gaussian voxel-energy noise: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/IW_M13_ROT35_nested_mask_covariance_shell_fisher_001.md
M13 ROT36 owns numerical global gain-profile distances, not interval-certified global minimization: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-25/IW_M13_ROT36_global_shell_gain_profile_nonlocal_identifiability_001.md
MT13 ROT037 owns an exact finite-sample chi-bar 5-mask confidence/test threshold c95=10.371033903003577, but its global model rejection required a mathematical lower bound on globally minimized Q*: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-25/mt13_rot037_m13_lt5_nested_mask_chibar_finite_sample_model_test_001.md
LT5 ROT19/20 owns DIFFERENT deterministic admissible-class minimax; NC ART023 and XH-S4 Q88 own source/measurement class visibility. This report makes no mathematical novelty claim; mature hosts are convex-cone separating hyperplanes, Bernstein polynomial positivity, Gaussian linear contrasts and Cauchy-Schwarz.

## Exact source-algebra
Nested N41 mask counts n=(50653,42875,35937,29791,24389), independent disjoint shells v=(7778,6938,6146,5402,24389).
Shell mean m_j(alpha)=B g_j(alpha): m_i=(n_i g_i - n_{i+1}g_{i+1})/v_i for i=0..3; m_4=g_4. All source coefficients are the archived FINITE DECIMALS from M13, treated as exact rational numbers in THIS narrow host. Not interval-enclosed original trigonometric expressions or unavailable historical DTC runtime.

For a fixed rational 5-vector ell, p_j(alpha)=ell·m_j(alpha)=sum_{k=0}^4 c_k alpha^k. With x=5alpha ∈[0,1], its degree-4 Bernstein coefficients are
 b_r=sum_{k=0}^r (c_k/5^k)*binom(r,k)/binom(4,k), r=0..4.
All b_r STRICTLY NEGATIVE imply p_j(alpha)<0 for ALL alpha∈[0,.2], by positive Bernstein basis.

**Three independently checked exact rational source certificates** (weights ordered shell W2,W3,W4,W5,W6):
- Channel A ell=(1,0,0,0,-1.273); max Bernstein b=-1.6235308532858994e-12.
- Channel B ell=(1,-1.47,0,0.72,-0.28); max Bernstein b=-2.828046343206605e-16.
- Channel C ell=(1,-1.361,0,0,0); max Bernstein b=-1.4862797691453357e-15.
The displayed max b are rounded decimals, but the actual negativity assertion was made with exact Python fractions on all 15 source-decimal quartics: five negative Bernstein coefficients per channel, no alpha grid. For EVERY common source gain t>=0, ell·t m_j(alpha)<=0. This holds for arbitrary POSITIVE MIXTURES of the legal source vectors as well.

## Exact probabilistic test and dual global-Q certificate
Assume precisely M13 ROT35 SYNTHETIC noise per disjoint ENERGY shell:
 Z_i=t m_j,i(alpha)+epsilon_i, epsilon_i independent N(0,tau_j²/v_i), tau_j=.01*g_j,k2(.05) known PER CHANNEL (not measured).
For sigma_ell=tau_j sqrt(sum_i ell_i²/v_i) and z=ell·Z/sigma_ell, under EVERY alpha and t>=0, E z<=0 and Var z=1. Hence the test z>Phi^-1(.95)=1.6448536269514722 has UNIFORM type-I risk <=5% for this source/noise host. The vector ell must be preselected, not cherry-picked against measured noise.

With whitened x_i=sqrt(v_i)Z_i/tau_j, source f_i(alpha)=sqrt(v_i)m_i(alpha)/tau_j, define Q*(x)=inf_{alpha∈[0,.2], t>=0}||x-t f(alpha)||². The unit vector w_i=(ell_i/sqrt(v_i))/sqrt(sum ell²/v) obeys w·f(alpha)<=0; therefore for every candidate ||x-t f(alpha)||>=w·(x-t f(alpha))>=w·x=z when z>0.
EXACT **Q*(x)>=max(z,0)²** without ANY global nonlinear optimization. In particular z²>c95 from ROT037 is now a mathematical global rejection certificate, not merely a numerically guessed minimum. One-sided cutoff 1.645 and sqrt(chi-bar c95)≈3.220 have DIFFERENT semantics; do not conflate.

## Three fully certified synthetic outer-shell anomalies
Synthetic alpha0=.05,t=1. Increase ONLY first disjoint shell W2 energy mean by 5%, leave other four unchanged; this is NOT an actual experimental observation.
A: z=397.83088032764135, certified Q*>=158269.4093422661, independent numerical Q*_approx 202327.4308308512.
B: z=106.99413838427039, certified Q*>=11447.745648592401, independent numerical Q*_approx 77601.90412527695.
C: z=208.42817875276918, certified Q*>=43442.3056981963, independent numerical Q*_approx 69052.48455463558.
All three rigorous bounds vastly exceed ROT037 c95. The separate 8001-grid+local numeric minimization is only a consistency check. Especially for B, the 4-nonzero-term rational contrast is a GLOBAL source-cone certificate although naive individual shell ratios cannot certify the 5% synthetic anomaly across alpha.

## Repro and limits
Full POLISH 12.5KB proof, literal M13 15-quartic decimal JSON, independent exact Fraction/Bernstein+Monte Carlo Python script, second independent noncertifying profile scan, full deterministic JSON, README and SHA manifest were created in Moderator-local ZIP MT13_20261025_ROT038_certified_global_source_separation_bundle.zip.
ZIP SHA256 01ca51c68375b3b383ce5d37d5d5c06b4b9c7f806097853a0c5083e623612a23. Frozen 15-quartic input JSON SHA256 e1786b45198a3751586d8edc768b152d196857c2add264acc73c10d5bbed826e.
CLEAN UNZIP CRC+6/6 input SHA PASS; DELETE archived result JSON, independently RERUN script INSIDE extracted dir and compare newly regenerated output BYTES, PASS; rerun second separate scan PASS.
Monte Carlo: 3 channels ×3 true alpha values ×3 legal/boundary positive gains ×30,000 full 5-shell Gaussians = 810,000 samples, observed rates within .0045 of exact one-sided Gaussian probabilities. Finite sample fluctuations can exceed 5%, which does not invalidate a <=.05 TRUE risk theorem.

This source-cone hyperplane rejects only observations outside the POSITIVE CONVEX CONE; other illegal source states may not admit any separating linear functional and require full global nonlinear Q*. It does NOT certify original unrounded source operator, missing historic DTC runtime, genuine physical noise, actual detector calibration, original TT physics, PBH/BBN, NASH J3/K or canonical physics. No independent REC/SW referee, BW ingestion or owner/EXEC adoption is implied.
END / NO NOVELTY / NO CANON / NO EXEC / NO NEW TASK CASCADE.
