---
artifact_id: GEEKY-S11-ROT024-GAIN-ALPHA-STRUCTURAL-VS-PRACTICAL-IDENTIFIABILITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-26
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
status: PROOF_AND_476_TYPED_CHECKS_PASS / INDEPENDENT_REFEREE_PENDING
---

# ROT024 — two scalar TT memory echoes detect memory but poorly identify filter alpha

## Source/own-science boundary

Geeky ROT015–017 first established the real even-grid raw-k compatible orthogonal TT projector B=GA, distinct from the original helper's non-idempotent real-cast A. ROT021 first rational TT memory coefficient c2=1643/20000; ROT022 first memory kernel; ROT023 first all-alpha TWO-CARRIER finite-time scalar-echo detection and new rational c3=261977/5780000. THIS rotation does not reclaim these. Different from M14 masked pure-trace h=fI K_A, PRF12 quantum memory, INT8 geometric TT. Mature statistical identification, Gaussian decision and Schur-complement Fisher mathematics (Curr Opin Systems Biol 2021 DOI 10.1016/j.coisb.2021.03.005; J Multivar Anal 2013 DOI 10.1016/j.jmva.2013.05.010); no mathematical novelty.

Only unchanged retained auxiliary helper deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, NOT byte-unavailable historical production dtc0a_runtime_v0_3_1.py. Full unmasked flat real TT, even N>=12, C=(0,cos x,0), source three-term centered Lie, and scalar Ealpha ONCE on initial input. Two fixed low-band B-TT carriers p=2,3 and scalar two-branch echo at tau=.01 from ROT023.

## Exact finite-N inversion versus unstable inverse

Let f_p(N)>0 be each unfiltered exact finite-time echo from ROT023; let t>0 be UNKNOWN common gain; alpha real UNKNOWN. The signed scalar echo is exactly

y_p=t f_p(N) [1-4 alpha a_p(N)],
a_p=sin²(p pi/N)+sin²(pi/N).

Set z_p=y_p/f_p. EXACT d=a3-a2=sin(5pi/N)sin(pi/N)>0, and
t=(a3 z2-a2 z3)/d,
t alpha=(z2-z3)/(4d),
alpha=(z2-z3)/[4(a3 z2-a2 z3)].

Thus global structural identifiability for all finite even N>=12 and ALL real alpha when gain t>0. But N²d -> 5pi²: normalized gain-alpha inversion for fixed absolute observation error is NOT uniformly stable; alpha sensitivity to noise grows O(N²). At t=0 alpha is not identifiable. With t arbitrarily close to 0 there is no positive uniform noisy memory-detection floor.

## Exact profiled Gaussian information

Synthetic noise host ONLY: four terminal scalar observations, two branches x two carriers, iid additive N(0,sigma²), sigma=1e-7, so two independent echo differences have covariance 2sigma² I. Mean vector mu=t(f2 e2,f3 e3), e_p=1-4alpha a_p. Exact Fisher-Schur information on alpha with nuisance t:

I_(alpha|t)=[8t²/sigma²]*(f2 f3)² (a3-a2)²/[f2²e2²+f3²e3²].

For fixed t>0, sigma>0, alpha finite and fixed, f2,f3 -> nonzero, e_p ->1, so I_(alpha|t)=Theta(N^-4). Fisher by itself is LOCAL and does NOT prove global confidence. The following global witness is separately exact.

## Finite-global pair, no asymptotic Wald shortcut

Two STABLE model values: H0=(alpha0=0,t0=1), H1=(alpha1=1/6,t1=1/[1-(2/3)a2]). Under these parameters carrier p2 has exactly the SAME mean. The p3 mean difference is

Delta3=f3 * [(2/3)(a3-a2)]/[1-(2/3)a2] > 0.

For the independently noisy echo differences, one-repetition Gaussian KL is EXACT:
KL=Delta3²/(4sigma²)=Theta(N^-4).
M independent repetitions have KL=M*KL. Optimal equal-prior SIMPLE-vs-SIMPLE test has success Phi(sqrt(M*KL/2)). Thus success >=75% if and only if M >= 2 Phi^-1(.75)²/KL (integer rounding), so M=Theta(N^4). Numbers at sigma 1e-7: N64 28; N128 441; N256 7037; N512 112517; N1024 1800031. One repetition involves FOUR raw scalar branch readouts. These are MODEL measurements, not real device limits or universal sample guarantees.

## Stable-source filter restriction

Source scalar full FFT multiplier ealpha(k)=1-4alpha sum_i sin²(pi k_i/N) has all-grid operator norm <=1 IFF 0<=alpha<=1/6 for even 3D grids. Thus both tested hypotheses obey this mathematical stability contract. Scaling alpha=beta*N² would preserve a nonvanishing low-frequency response for beta !=0 but blows up the full-grid E norm as Theta(N²); it changes admissibility, not a source-legal automatic remedy.

## Independent actual controls and custody

Three independently runnable Python programs:
(A) sparse original-Lie 6N Fourier exponentials N12..1024, source scalar multipliers, exact inverse, Fisher-Schur and Gaussian pair testing: 302/302 PASS;
(B) separate genuine full N³ source-native unmodified Lie, TT, E helper and nine-term Taylor at N12/16/24: 30/30 PASS, sparse/full discrepancy max 9.375689108545235e-16;
(C) separate Python-stdlib Fraction synthetic algebra for inverse and Fisher determinant: 144/144 PASS (rational algebra, NOT exact trig).
476/476 typed executed PASS. Single local ZIP with full 12KB report, three executed scripts, three JSON, unchanged helper, README/STDOUT and SHA manifest: CRC PASS; 12/12 content SHA PASS; clean extraction and all three scripts rerun to BYTE-IDENTICAL JSON PASS. ZIP SHA256 d257432d2f5a966853f65ab1f74fe14ea3c9ff61e612a955e099931c6ad05130. This GITHUB note is the full self-contained mathematical executive record, while separately runnable source/JSON ZIP is in Moderator-local conversation, not falsely claimed GitHub-hosted.

## Strict firewall

ROT023 detection floor assumes normalized t=1; with arbitrary unknown t>0 the signal is proportional to t and no fixed-noise detection guarantee exists. Structural injectivity is not robust parameter estimation; Fisher is local, exact two-simple-Gaussian KL is global only for the DECLARED pair and noise. No real-world measured noise, physical non-Markovian gravity, masked source K_A, J3/K invariant, GR/GW/PBH/BBN, independent referee, BW ingestion, canon, or EXEC. NO_NEW_TASK.
