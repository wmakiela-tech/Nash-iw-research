---
artifact_id: GEEKY-S11-ROT034-FIXED-BUDGET-TT-SCHEDULE-NONIDENTIFIABILITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-29
problem_id: P3_DTC0A_VARIABLE_FILTER_SCHEDULE_FINITE_TT_READOUT_IDENTIFIABILITY_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_FINITE_TOPOLOGICAL_NONINJECTIVITY_AND_EXPLICIT_CONTINUUM_LAPLACE_MOMENT_COLLISION
status: PROOF_2768_EXECUTED_CHECKS_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT034: fixed-budget filter schedules cannot be reconstructed from two full TT output fields

## Own scientific lineage and mature references

ROT015–017 FIRST identified even-grid raw-k TT realcast A non-idempotence and repaired compatible real orthoprojector B=GA. ROT021–023 first constructed smooth true TT witnesses and projected memory. ROT024–026 investigated single/repeated filter alpha identification and placement. ROT027 defined uniform Lie insertion; ROT028 3/5 integer-node moment quadrature; ROT029 spectral divided differences; ROT030–032 certified truncation/diffusion gates. ROT033 FIRST generalized to variable source filters E_(alpha_j), gave exact insertion spectral transition and distinguished total smoothing budget from schedule order. ROT034 does NOT reclaim these. New question: does a fixed finite family of full TT outputs IDENTIFY an arbitrary schedule? Answer NO, with finite-grid topological theorem and an explicit continuum collision.

Classical hosts are Brouwer invariance of domain/dimension (https://encyclopediaofmath.org/wiki/Domain_invariance ; NTNU lecture https://gereonq.folk.ntnu.no/TMA4192V2022/TMA4192_Lecture19.pdf) and generalized exponential Vandermonde/Chebyshev systems (Karlin & Studden 1966, https://books.google.com/books?id=pAmVzwEACAAJ). This is NOT a mathematical novelty or priority claim.

Actual source is UNCHANGED auxiliary deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, NOT unavailable historic production dtc0a_runtime_v0_3_1.py. Flat full unmasked even N³ real symmetric Frobenius L2, N>=12; correct compatible B=GA; original centered THREE-TERM tensor Lie with C=(0,cos x,0), source E_alpha=I+alpha h²Delta2, alpha in [0,1/6], full-grid contraction. NOT original masked h=fI K_A, or physical J3/K/GR/PBH.

## R34.1 exact FINITE-N nonidentifiability from only four numbers

Let m>=6 and fixed sum A_N strictly between 0 and m/6. Let D={alpha=(alpha1,...,alpham) in (0,1/6)^m: sum alpha_j=A_N}; this has relative interior dimension m-1>=5. Define EXACT ROT033 insertion operator
 U_seq(C)=(m+1)^-1 sum_(ell=0)^m (E_m...E_(ell+1)) B L_C B (E_ell...E_1).
The source Fourier transition k->k' has symbol
 Omega_seq(k',k)=(m+1)^-1 sum_(ell=0)^m [prod_(j>ell)(1-4alpha_j S_N(k'))] [prod_(j<=ell)(1-4alpha_j S_N(k))],
S_N(k)=sum sin²(pi k_i/N).

Two fixed smooth true-TT input tensors p=2,3 are H_p=T_p cos(px+y), T_p=.3*(zz - v_p v_p^T/(p²+1)), v_p=(-1,p,0). Since C is single harmonic cos x, each full output U_seq(C)H_p is a linear combination of only TWO fixed real TT sideband polarizations p-1 and p+1, with ONE schedule-dependent real scalar Omega per sideband. Therefore BOTH ENTIRE OUTPUT FIELDS depend on at most FOUR real parameters (p2±,p3±), not on all m alpha_j individually.

The map F:D->R^4 of those four scalar Omega values is polynomial/continuous. A continuous injective map from an open set of R^(m-1), m-1>=5, to R^4 would contradict Brouwer invariance of dimension (embed R^4 in R^(m-1) and apply invariance of domain). Thus FOR EVERY finite even N>=12, every m>=6, and every fixed interior legal sum A_N, there EXIST distinct STRICTLY LEGAL schedules with the SAME budget and EXACTLY IDENTICAL FULL TT OUTPUT FIELDS for both probes. This is an EXISTENCE result, not an explicit finite N pair, not a statement that every schedule has a twin, and not about time-resolved observations or arbitrary additional probes. The gain may be known; it does not resolve the degeneracy.

## R34.2 continuum observation = four exponential/Laplace moments

Let m_N/N²->beta>0 and a_N(t)=N^-2 sum_(j<=floor(m_N*t)) alpha_(N,j) -> a(t) uniformly, where a:[0,1]->[0,A] is monotone. At fixed low modes k=(p,1,0) and k'=(p+side,1,0), write K_in=p²+1, K_out=(p+side)²+1. Since q_j(k)=1-4alpha_j*pi²*K_in/N²+O(alpha_j/N^4), the exact ROT033 discrete Omega tends to
 Omega_infty=integral_0^1 exp[-4pi²(K_out*(A-a(t))+K_in*a(t))]dt
 =exp(-4pi² K_out A)*J_(DeltaK),
 J_delta=integral_0^1 exp(4pi² delta a(t))dt.
For p2 ± and p3 ± the FOUR DeltaK are exactly {-3,+5,-5,+7}. Thus all four outputs are FOUR fixed exponential moments of the pushforward of uniform t by a(t), NOT a complete schedule trace.

## R34.3 explicit positive continuum collision, exact by cofactors

Set beta=.12, A=.009, v=.012, six levels x_j=j*A/5, j=0,...,5. Build a piecewise-linear monotone cumulative dose profile that spends d_j positive time at level x_j and moves along identical positive-slope ramps (speed v) between consecutive levels. Total ramp time A/v=.75; total plateau time .25. On ramps the original stable filter parameter is alpha(t)=v/beta=.1, on plateaus zero. Both profiles have identical duration, total dose and legal stable alpha.

Let 5x6 matrix M with rows indexed delta=(-5,-3,0,+5,+7) be M_(delta,j)=exp(4pi² delta x_j). Because distinct real exponentials form a Chebyshev system, every ordered 5x5 minor is nonzero. Define exact nullvector w_j=(-1)^j det(M_without_column_j)/max_i|det(M_without_column_i)|. Cofactor expansion gives Mw=0 EXACTLY and max |w|=1. Now choose
 d_j^(plus)=1/24+.018*w_j, d_j^(minus)=1/24-.018*w_j.
Every duration is positive, and each six-vector sums exactly to .25. Maximum plateau time difference is EXACTLY .036 of total experiment. Their common ramp contribution to J_delta is (exp(4pi²delta A)-1)/(4pi²delta v), plus sum_j d_j exp(4pi²delta x_j), with J_0=1. Since Mw=0, J_delta^(plus)=J_delta^(minus) for ALL four probe deltas. Therefore BOTH FULL CONTINUUM TT OUTPUTS are exactly the same, although the two source-legal cumulative-dose histories differ.

A fifth additional TT probe H4, reading downshift p4->p3, has DeltaK=-7, not in the original four. The sixth exponential function makes the generalized Vandermonde 6x6 invertible, so the collision MUST be broken. For this explicit pair the fifth scalar Fourier transition Omega differs by approximately 4.96109247539115e-7, before instrumental gain/noise and known tensor polarization. No universal experimental sensitivity claim.

High-precision check using independently computed 5x5 cofactors (mpmath 110 decimal digits): ||Mw||_max ~=4.19975e-109; exact equality rests on the cofactor identity, NOT treating those decimal calculations as exact transcendental arithmetic. Explicit positive plateau durations and results are in the local JSON.

## R34.4 legitimate finite-N realizations converge but are NOT the exact finite-N collision from R34.1

For each continuum profile set m_N=round(beta N²), and source-legal alpha_(N,j)=N²[a(j/m_N)-a((j-1)/m_N)]. All alpha_(N,j) are nonnegative and <=v N²/m_N~.1<1/6, and sum alpha_(N,j)=A N² exactly. The finite Fourier symbol Omega_seq is independently evaluated from source formula, at N=32..1024. The four TT differences converge to 0 with N. At N1024,m125829 double-precision normalized differences are ~1.05661714e-11 for H2 and 3.05848836e-11 for H3, with numerical precision limits. THESE finite-N schedules are NOT falsely claimed to have exactly equal fields. R34.1 separately guarantees some exact finite-N collision without identifying that pair.

## Actual tests, archive, limits

1. Standalone 110-digit mpmath generalized exponential cofactor builder, exact-identity checks, two legal profiles/fifth probe: 14/14 executed PASS.
2. Independently coded finite-grid source-symbol legal schedule realizations N32..1024, FFT sideband norm geometry, continuum convergence: 201/201 PASS.
3. Independently coded literal original UNCHANGED helper full N³ real source apply_E, lie_derivative_tensor, apply_P_TT for p=2,3,4 and N12/16: 63/63 PASS, max relative disagreement 6.97886256466231e-16.
4. Separate Python stdlib Fraction polynomial moment analogue to order 14, exact integer Vandermonde factor, open-simplex checks: 2490/2490 PASS. Fraction tests DO NOT claim exact exponential evaluation.

TOTAL 2768/2768 typed actually executed PASS. This execution does NOT substitute independent referee proof scrutiny. LOCAL self-contained ZIP (full 14KB Polish report, FOUR standalone scripts, FOUR actual JSON, unchanged frozen source helper, stdout and manifest):
GEEKY_S11_ROT034_FIXED_BUDGET_TT_SCHEDULE_IDENTIFIABILITY_REPRO_001.zip
SHA256 3a1be4be4927cd4065a1ba5ad5f5dcf7b7d95c4e3f751a3962ec33604c1bc98e.
Independent clean extraction ZIP CRC PASS, content manifest SHA256 15/15 PASS, all four scripts rerun and four JSON BYTE IDENTICAL PASS. ZIP/code local to Moderator conversation, NOT claimed separately GitHub-hosted.

**Claim ceiling:** mathematical helper host and four-probe measurement geometry only. ROT033 order sensitivity does NOT entail schedule recovery; the explicit continuum pair is a collision only in the limit. No historical masked h=fI K_A, physical NCDG J3/K, GR/GW/PBH, original production runtime, external referee, BW/owner adoption or EXEC. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK.
