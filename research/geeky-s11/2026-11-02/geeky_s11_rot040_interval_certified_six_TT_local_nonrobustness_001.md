---
artifact_id: GEEKY-S11-ROT040-INTERVAL-CERTIFIED-SIX-TT-LOCAL-NONROBUSTNESS-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-02
problem_id: P3_DTC0A_SOURCE_FINITE_TT_SENSOR_NONROBUST_INTERVAL_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_type: SOURCE_TYPED_COMPUTER_ASSISTED_DIRECTED_INTERVAL_LOCAL_FALSIFIER
status: 17804_EXECUTED_TYPED_CONTROLS_PASS / CLEAN_REPLAY_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT040 — rigorous interval neighborhood for ROT039's six-TT sensor nonrobustness falsifier

## Own-prior and source contracts
ROT015–017: real even-grid raw-k TT caveat, genuine source-compatible B=GA. ROT027/029 exact one-Lie uniform insertion and Fourier kernel. ROT033 variable Ealpha schedule. ROT034 unrestricted schedule nonidentifiability. ROT035–036 restricted continuum six-level inverse with gain/noise bias; ROT037 EXACT source finite six-TT local inverse; ROT038 FIRST numerical finite-pool six-channel nominal optimum; ROT039 FIRST LEGAL N64 NUMERICAL COUNTEREXAMPLE to universal parameter robustness of that nominal design and two-scenario minimax. ROT040 does NOT discover that witness or reassign ownership. Its sole new task is to turn ROT039's high-precision numerical case into a DIRECTED-INTERVAL SOURCE-FINITE CERTIFICATE on an OPEN 6D LEGAL parameter neighborhood. Uses classical Weyl singular perturbation, strict interval LDL^T positive definiteness and explicit low-response vector, NO novel mathematics.

SOURCE TYPE: UNCHANGED retained auxiliary deepseek_python_20260627_a87249.py. Verified ACTUAL SHA256 = 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. This corrects a two-character transposition in some previous explanatory metadata (incorrect fragment ...f9d4c1f9dcb9f1d5... vs actual ...f9d4c1f9cdb9f1d5...). Source code itself unchanged: original ROT039 source-native test embedded the CORRECT checksum and passed. Historical original production dtc0a_runtime_v0_3_1.py bytes unavailable. Host full flat unmasked even N³ real symmetric tensors, B=GA, original centered three-term Lie C=(0,cos x,0), stable Ealpha=I+alpha*h²Delta2. NEVER historic h=fI/masked K_A, NCDG physical J3/K/GR/GW/PBH.

## Model, exact finite input and two sensor sets
Known six cumulative-dose levels x_j=j*.009/5, five ramp slopes .012, plateau durations d_j>0 summing .25, unknown positive common gain t. N64; m=round(.12N²)=492; alpha_j=N²[a_d(j/m)-a_d((j-1)/m)] in [0,1/6]. One Lie transport averaged across all m+1 insertion positions, exactly
 Omega_(p,s) = 1/(m+1) SUM_ell [PROD_(j<=ell)(1-4alpha_j a_in)][PROD_(j>ell)(1-4alpha_j a_out)],
 a_in=sin²(pi*p/N)+sin²(pi/N), a_out=sin²(pi*(p+s)/N)+sin²(pi/N).
Readout y=t*Omega, analytic 6x6 Jacobian J=[Omega|t*dOmega/dd0..4], d5=.25-sum first five.

OLD ROT037: H2-,H2+,H3-,H3+,H4-,H4+. NEW ROT038: H0+,H1-,H1+,H2-,H3+,H4-.
ROT039 CENTER first five durations, treated as exact decimal rationals:
(.003160219022080221,.0026756342224162114,.0022914955572644483,.0027910331414697223,.04707365145084304);
d5 exact complement to .25, gain center .8123225702365454.

Consider the entire OPEN BOX with each of five independent dwell parameters and gain t within radius rho=1e-10 of center. All entries positive and schedules source-legal. Exact stdlib Fraction enumeration of all 2^5 dwell corners plus affine dependence of time nodes proves every intermediate schedule remains in the SAME kink-free parameter chamber. At corners min grid-knot distance >.0004637314779 and exact alpha_j in [0,.09990243902439025], sum alpha=N²*.009.

## COMPUTER-ASSISTED interval inequalities, not numerical SVD assertions
With 55-digit experimental directed mpmath.iv intervals, construct exact source-symbol product and its analytic derivatives for all nine distinct probe sidebands; rational time knots and alpha_j enclosed, trigonometric sin² interval-evaluated.

1. At CENTER: interval LDL^T on J_OLD^T J_OLD - (1.30e-6)^2 I yields six STRICTLY POSITIVE interval lower pivots. Hence sigma_min(J_OLD center)>1.30e-6.
2. At CENTER: explicit, published decimal-rational nonzero right test vector w for NEW gives interval ||J_NEW w||² < (1.36e-7)^2 ||w||². Hence sigma_min(J_NEW center)<1.36e-7. An SVD may SUGGEST w, but interval direct-vector verification, not SVD correctness, proves the bound.
3. Across ENTIRE BOX: interval enclosures of each source-analytic J entry give Frobenius distance ||J(theta)-J(center)||2<=||...||F<6e-8. Weyl yields sigma_min(OLD)>1.24e-6, sigma_min(NEW)<1.96e-7 for ALL theta in the six-dimensional box.
4. Independently interval verify ||J_NEW e_gain||2>0.9 and ||J_OLD||F<0.6. Therefore for ALL theta in box kappa2(OLD)<600000, kappa2(NEW)>4500000; NEW condition strictly >7.5x worse. Numerical ROT039 point ratio (~21.8x) is NOT promoted to certified uniform ratio.

A direct interval LDL^T on the whole box had interval dependency overestimation and was NOT successful; factoring at a single center PLUS uniform perturbation bound resolves this rigorously within the declared interval arithmetic backend. This very SMALL box is NOT an apparatus-noise robustness threshold. The TT-polarization-weighted observation host was checked numerically in ROT039 only; ROT040's interval certificate is for declared equal-variance normalized Omega host. No all-N, all-schedule or finite-pool/global-optimality claim.

## Independently executed controls / custody
Seven clean runnable programs, some RETAINED from ROT039 to establish input and source correspondence:
(A) rot040_interval_counterexample.py 14 strict checks (six LDL pivots, explicit vector, uniform box perturbation, singular/condition inequalities).
(B) rot040_exact_legal_chamber.py 15936 stdlib Fraction checks on 32 exact corner schedules (not trig exact).
(C) rot040_local_numerical_stress.py 804 checks on 201 additional legal N64 synthetic profiles with perturbations |delta dwell|<=1e-5 and |delta gain|<=.01. Every tested profile prefers OLD, but NO interval guarantee for this larger region.
(D) rot039_robust_plateau_scan.py 975 replay checks reconstructing 195 synthetic cases and the original ROT039 N64 witness.
(E) rot039_high_precision_witness.py 8 independent 75-digit original source-finite all-product/derivative checks, sharper point SVD only.
(F) rot039_source_native_crosscheck.py 30 LITERAL unchanged source helper apply_P_TT/apply_E/THREE-term Lie on small full 3D N12/16, modal gap <=2.39044e-16 (NOT full N64 m492 source tensor replay).
(G) rot039_independent_forward_fd.py 37 separate forward finite-difference Jacobian checks, worst absolute gap 3.12572e-9.
TOTAL 17804/17804 actually executed typed tests; not 17804 independent physical experiments or peer reviews.

FULL LOCAL Moderator/user conversation ZIP: GEEKY_S11_ROT040_INTERVAL_CERTIFIED_SIX_TT_LOCAL_NONROBUSTNESS_REPRO_001.zip SHA256 db77e164b995f5d4d6a6f88b195989e287a5c1eeb7be8b5a1e5fbb90600e7160. Includes expanded 11k Polish proof, seven executable scripts, seven original JSON, seven stdout, unchanged auxiliary source, prior source-independent ROT039 core, README and manifest. CLEAN ZIP CRC PASS; content SHA256 25/25 PASS; ALL SEVEN separate scripts rerun from clean extraction and SEVEN JSON BYTE IDENTICAL PASS. Source ZIP and scripts LOCAL, not separately GitHub-hosted.

No original historical DTC production h=fI K_A, no NCDG physics, no actual noise, no external independent referee, BW ingest/owner acceptance, canon or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
