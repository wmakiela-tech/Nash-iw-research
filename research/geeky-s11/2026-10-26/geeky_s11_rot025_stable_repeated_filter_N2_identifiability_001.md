---
artifact_id: GEEKY-S11-ROT025-STABLE-REPEATED-SOURCE-E-N2-RESOURCE-GATE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
problem_id: P3_DTC0A_SOURCE_E_REPETITION_COST_VS_ALPHA_IDENTIFIABILITY_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_STABLE_REPEATED_FILTER_IDENTIFIABILITY_AND_GAUSSIAN_RESOURCE_GATE
status: ANALYTICAL_PROOF_PLUS_1647_TYPED_CONTROLS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT025 — the N² resource threshold for repeated stable filtering of two low-band TT memory echoes

## Scope and own/external prior art

Geeky ROT015–017 first distinguished the retained source-helper's even-N nonidempotent realcast raw-k operator A from strict orthogonal compatible real-TT B=GA. ROT021 FIRST proved a rational two-step TT return for a fixed smooth carrier; ROT022 first studied finite-time Mori–Zwanzig projected memory, ROT023 first constructed two scalar two-branch fixed-low-band echoes p=2,3; ROT024 FIRST proved with a SINGLE initial E_alpha step that unknown-gain filter alpha is structurally identifiable yet its nuisance-profile Fisher information is Theta(N^-4) and an exact Gaussian simple-pair needs Theta(N^4) repetitions. ROT025 subtracts these results and varies ONLY the number m of initial scalar E applications. M14's masked h=fI/K_A, INT8 geometric TT, PRF12 process memory and XH primary research are distinct.

External mature hosts: Fourier symbols of forward-Euler heat filters/CFL and the diffusion-semigroup limit (Numerical Analysis lecture notes, numerical.rl.ac.uk); design and practical identifiability (Gross et al., Bioinformatics 36, 2020, DOI 10.1093/bioinformatics/btaa404); standard efficient Fisher/Schur and Gaussian hypothesis testing. NO mathematical novelty or scientific priority claim.

Source: SHA256-verified original auxiliary helper deepseek_python_20260627_a87249.py digest 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. HISTORIC production dtc0a_runtime_v0_3_1.py bytes still unavailable. The explicitly MODIFIED mathematical experimental protocol applies the same E_alpha m times BEFORE both TT memory-echo branches, not once as historically. Flat full unmasked even N³, N>=12, fixed smooth source-style three-term Lie generator C=(0,cos x,0), strict B=GA, half-echo time tau=.01.

## R25.1 exact two-echo law and inverse

For prior exactly TT low modes H_p=T_p cos(px+y), p=2,3, denote their original exact unfiltered finite-time scalar two-branch echo f_p(N)>0. With common UNKNOWN positive gain t and m>=1 applications of unchanged scalar E_alpha=I+alpha h²Delta2 to each initial H_p, the final contrast is EXACTLY

  y_p=t f_p(N) q_p(alpha,N)^m,
  q_p=1-4alpha a_p,
  a_p=sin²(pi p/N)+sin²(pi/N).

Every source E is a full 3D L² contraction iff 0<=alpha<=1/6; hence repeated E remains contractive. For this interval q2>=q3>0, with equality at alpha0. Set z_p=y_p/f_p and r=(z3/z2)^(1/m)>0. Exact unique finite-grid inverse for any t>0 is

  alpha=(1-r)/[4(a3-r a2)],
  t=z2/[1-4alpha a2]^m,

since a3-a2=sin(5pi/N)sin(pi/N)>0 and a3-r a2=(a3-a2)/q2. This is structural, NOT noise-robust inversion.

Gain-free log-ratio derivative is EXACT:
  d/dalpha log[(y3/f3)/(y2/f2)] = -4m(a3-a2)/(q2 q3).

## R25.2 sharp resource threshold within this TWO-carrier repeated-E protocol

For fixed beta>0 and integer m_N=ceil(beta N²),
  a_p(N)=(p²+1)pi²/N² + O(N^-4),
  q_p(alpha,N)^m_N -> exp[-4beta alpha pi²(p²+1)].

Thus the limiting two observations retain nonzero alpha-dependent projective separation despite fixed low-frequency probes and alpha in full-grid stable [0,1/6]. The log-ratio slope tends -20 beta pi² (nonzero). With t restricted to t_min<=t<=t_max, t_min>0, and fixed Gaussian noise, nuisance-profile Fisher remains bounded below for fixed beta.

Conversely if 1<=m_N=o(N²), sensitivity is Theta(m_N/N²) and Fisher Theta(m_N²/N⁴); a particular exact global matched-gain Gaussian testing problem requires M=Theta(N⁴/m_N²) independent repetitions. Therefore m=Theta(N²) is the sharp filter-use scaling FOR THIS PROTOCOL, not a universal minimax assertion over other probes or instruments. For m/N²->infinity and fixed alpha>0 the two signals are exponentially overattenuated and bounded-gain Fisher tends 0; at alpha=0 that overfiltering caveat does NOT apply.

## R25.3 exact profiled Fisher and global pair

Four independent raw terminal scalar observations each have declared synthetic iid N(0,sigma²) error, sigma=1e-7. Their two differences have covariance 2sigma² I. For q_p=1-4alpha a_p, and t>0, efficient Fisher information in alpha after profiling unknown t is exactly

I(alpha|t) = [8t² m²/sigma²] (f2 f3)² (a3-a2)² q2^(2m-2) q3^(2m-2) /
             [f2² q2^(2m)+f3² q3^(2m)].

Exact determinant: det(u,du/dalpha)=-4m f2 f3 q2^(m-1)q3^(m-1)(a3-a2).

GLOBAL witness, distinct from local Fisher: H0=(alpha0=0,t0=1), H1=(alpha1=1/6,t1=q2(alpha1)^(-m)), so p2 means match EXACTLY. Carrier p3 difference is

Delta3 = f3[1-(q3(alpha1)/q2(alpha1))^m],
KL_per_independent_echo_pair=Delta3²/(4sigma²),
P_success_equal_prior(M)=Phi(sqrt(M KL/2)).

If m=o(N²), KL=Theta(m²/N⁴); if m=ceil(beta N²), it tends f3(infinity)²[1-exp(-(2/3)*5pi² beta)]²/(4sigma²)>0. For beta=.02 t1->exp((2/3)*5pi²*.02)=1.9309, within [1,3], so that exact global two-point comparison needs ONE independent four-raw-reading trial for >=75% optimal simple-pair accuracy for N64...1024 in this SYNTHETIC model. Do not extrapolate to arbitrary unknown-source estimation or real instruments.

N | m=1 required M | m=ceil(.02 N²) | required M with repeated filter
64 | 28 | 82 | 1
128 | 441 | 328 | 1
256 | 7037 | 1311 | 1
512 | 112517 | 5243 | 1
1024 | 1800031 | 20972 | 1

Accounting both carriers, relative source E uses per entire study is baseline M vs repeated m*M, because both use two carriers. At N64 repeated preparation is more expensive; at N1024 about 86 times fewer source E evaluations, ignoring all other computational costs. Every numeric sample figure requires exactly the declared gain choice, noise law and observation pair.

## R25.4 executed controls, reproducibility, custody

(A) Fresh standalone sparse Fourier source-style three-term Lie plus strict raw-k B, actual finite time echos, source eigenvalues, nonexpansiveness, exact Fisher/Gaussian simple KL and filter pass schedule N12..N1024: 383/383 typed controls PASS. 
(B) Independently implemented FULL real N³ original retained helper source-native apply_E called m times, full Lie and original apply_P_TT with separate Hermitian guard; N12/16, two TT inputs, two alpha values, one and ceil(.02N²) filter passes: 44/44 source-native controls PASS. Absolute scalar echo max gap 3.704477418993001e-16.
(C) Independent Python stdlib Fraction rational inverse/Jacobian/Fisher factorization, 300 scenarios including alpha=0: 1220/1220 exact rational checks PASS; DOES NOT claim exact trig certificate.

Total 1647/1647 executed typed checks PASS. Single standalone user-conversation ZIP GEEKY_S11_ROT025_STABLE_REPEATED_FILTER_N2_IDENTIFIABILITY_REPRO_001.zip SHA256 8b3361077e8c116e50f922a476370bfda63f75e593d4ceb4d2ea88976ae27a76 contains full expanded 13KB report, 3 executable standalone scripts, 3 archived actual JSON outputs, unchanged helper, README and stdout logs, SHA256 manifest. CLEAN independent unzip ZIP-CRC PASS, all 12/12 content SHA256 PASS, all three scripts rerun in clean extraction and all three regenerated JSON BYTE IDENTICAL PASS. Initial oversized full-grid validation timed out and is NOT included in reported PASS count; final bounded genuine original-helper rerun succeeded.

## Strict negative knowledge

This is a redesigned preparation protocol, NOT original helper's historical single-E use or masked h=fI K_A test. Nonexpansive repeated E at fixed alpha is stable but costs Theta(N²) operator applications (classical explicit heat filtering) and can suppress physical signals. Fisher local; global simple pair restricted and noise synthetic; without t bounded away from zero no uniform inference floor. No claim to novel physics, NASH K/J3/GR/GW/PBH, original production runtime recovery, canon, owner uptake, BW ingestion, independent referee or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
