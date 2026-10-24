---
artifact_id: IW_INT8_ROT025_EXACT_AFFINE_ALIAS_TT_CORRECTION_RANK_AND_HS_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC_SAFE
evidence: EXACT_FINITE_PROJECTOR_PRINCIPAL_ANGLES / SOURCE_HELPER_EXECUTION / CLEAN_ZIP_REPLAY
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT025 — exact rank and Hilbert–Schmidt norm of affine raw-wavevector TT correction

## Currentness and other-cell precedence
Fresh Slack #iw-dispatch consulted 2026-10-24. MT13 first constructed exactly covariant *metric-transported local stencil* E_g U_A=U_A E_alpha, and first exposed high-band non-covariance of naively recalculated raw-k target metric TT projection. XH-S4 owns moving York and nonflat metric tests. INT8 ROT023 owns exact no-fold count and a near-unit-loss true TT source witness. INT8 ROT024 owns exact full filtered operator spectral norm and regularity-weighted Hs rate. The NEW delta here is the complete 6D singular spectrum, exact full and TT-restricted *ranks*, exact global Schatten-2 accounting and synthetic white-input statistical validation. M13 owns historical h=fI K_A/masks, PRF11 Lie/TT collocation, Geeky-S11 even matched TT; no reattribution.

## Definitions
Odd N=2m+1>=9, signed Fourier cube B_N=[-m,m]^3, periodic three-torus grid, real Sym(3) tensor arrays of total dimension 6N^3 in orthonormal Frobenius basis. Source raw-k Fourier TT projection P is rank2 for k!=0, with *original helper convention* k=0 -> rank5 trace-free projector; hence total source TT dimension 2N^3+3. Source E_alpha=I+alpha sum_i(shift_ei+shift_-ei-2I), with exact multiplier e_alpha(k)=1-4alpha sum_i sin^2(pi*k_i/N). Retained helper deepseek_python_20260627_a87249.py independently SHA-checked: 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Shear A=[[1,1,0],[0,1,0],[0,0,1]], U_A H(x)=A^T H(Ax) A, g=A^T A intrinsically flat. Pullback U_A is isometric from source Frobenius L2 to target geometric L2(g). Original E_alpha transported to E_g by the known MT13 affine family. Target P_g^raw is recomputed from wrapped representative raw k, NOT equal in general to U_A P U_A^-1.

Declare D=P_g^raw E_g U_A - U_A P E_alpha, full-grid unmasked Hilbert spaces.

## Theorem 025.1 — full singular-value list and exact minimal repair rank
On nonfolded k with |kx+ky|<=m, D(k)=0. On each folded input Fourier mode, let sigma=sign(kx+ky), ell=(kx,ky−sigma*N,kz), c=|k dot ell|/(|k||ell|), 0<=c<1. Under isometric Euclidean-frame conjugation the Fourier block equals e_alpha(k)(Pi_ell-Pi_k), where both Pi are rank2 orthogonal TT projectors on six-dimensional symmetric matrices. Their two principal-angle cosines are c (cross) and (1+c^2)/2 (plus).

Thus EXACT singular values of the full 6x6 block, with multiplicities:
 |e| sqrt(1-c^2) twice;
 |e| sqrt(1-(1+c^2)^2/4) twice;
 zero twice.
For source TT restriction D P, the two distinct positive values occur ONCE each; the remaining four are zero.

For alpha=.05, min e_alpha>=.4>0, all folded blocks have rank4 (rank2 on source TT). Number of folded original modes:
 M_N=N^3 - N(3N^2+1)/4 = N(N^2-1)/4  [INT8 ROT023].
Therefore
  rank D=4 M_N=N(N^2-1);
  rank(DP)=2 M_N=N(N^2-1)/2.
Signed complex Fourier wave ±k pairing yields precisely these REAL ranks, not double these ranks. Total full dimension 6N^3, TT dimension 2N^3+3; asymptotic correction rank fractions respectively 1/6 and 1/4.

Minimality TYPING: Exact correction of this SPECIFIED raw operator to the transported one has a unique difference D, thus this correction rank is unavoidable. Not a lower bound across changed observable/projector algorithms or arbitrary approximate fixes. For other alpha, modes with e_alpha(k)=0 can lower rank; no unjustified all-alpha rank claim.

## Theorem 025.2 — exact Schatten-2 and isotropic white-input response
For each folded k:
 ||D(k)||_HS^2 = e_alpha(k)^2 (7−6c^2−c^4)/2;
 ||D(k)Pi_k||_HS^2 = e_alpha(k)^2 (7−6c^2−c^4)/4.
For nonfolded k both vanish. Summing over B_N gives the EXACT full-grid HS squared norm, no fit or Monte Carlo theorem. For independent standard normal coefficients along all six Frobenius orthonormal source tensor components (SYNTHETIC, nonphysical):
 sqrt(E||DH||^2 / E||H||^2) = ||D||_HS / sqrt(6N^3).
For H=PZ with Z likewise isotropic:
 sqrt(E||DPZ||^2 / E||PZ||^2) = ||DP||_HS / sqrt(2N^3+3).
These are square-roots of ratios of **expectations of squared norms**, NOT mean individual relative errors/energy deficits.

As N increases through odd grids at fixed alpha=.05 the dimension-normalized HS norms converge by ordinary Riemann sums. Let u∈[-1/2,1/2]^3, F={|ux+uy|>1/2}, sign sigma=sign(ux+uy), v=(ux,uy−sigma,uz), c(u)=|u dot v|/(|u||v|), e(u)=1-4alpha sum sin^2(pi u_i). Then:
 lim ||D||_HS^2/(6N^3) = (1/6) integral_F e(u)^2 (7−6c(u)^2−c(u)^4)/2 d^3u >0 at alpha=.05.
The TT analog is (1/4) times the SAME integral, so its limiting expected squared RMS ratio is exactly 3/2 times that of full white symmetric inputs. This is a frequency-density Riemann limit, NOT a curved-spacetime continuum operator or field physics.
High-N independent quadrature N101/201/401: full gains .22479931/.22480742/.22480948, TT .27532161/.27533171/.27533425. These are numerical approximations to the integrals.

## Executed table, alpha=.05
| N | Folded modes | rank D | rank DP | Gaussian full input RMS gain | Gaussian source TT RMS gain | Exact L2 operator norm |
|---:|---:|---:|---:|---:|---:|---:|
| 9 | 180 | 720 | 360 | .2234527911 | .2733915374 | .7639983377 |
| 17 | 1224 | 4896 | 2448 | .2244278274 | .2748248800 | .7829569449 |
| 31 | 7440 | 29760 | 14880 | .2246950419 | .2751871724 | .7914102072 |
| 33 | 8976 | 35904 | 17952 | .2247085670 | .2752049216 | .7924791901 |
| 35 | 10710 | 42840 | 21420 | .2247198418 | .2752196594 | .7925520097 |
| 37 | 12654 | 50616 | 25308 | .2247293390 | .2752320302 | .7924726145 |
| 39 | 14820 | 59280 | 29640 | .2247374136 | .2752425147 | .7935566133 |
| 41 | 17220 | 68880 | 34440 | .2247443360 | .2752514777 | .7938538807 |

## Independent reproduction and transparent failed test
Standalone NumPy-only Python independent source hash check and 8-grid full frequency accounting PASS. 28 explicit independent 6x6 real symmetric Frobenius TT projector SVD checks PASS: full rank4, TT restricted rank2, exact complete singular spectrum, HS formula errors <2e-12. 2 full real 3D tensor FFT executions N9/17, source retained unmodified apply_E & apply_P_TT vs separate implementations, metric-adapted E_g and raw-target projection, spectral-block reconstruction: RMS error 4.59e-16/5.51e-16. Independent Monte Carlo 180 isotropic random real tensors EACH at N9 and N17 (360 total) and separately source TT projected versions: ensemble RMS gains agree within .00033. Gaussian trials are a control of ensemble identities; their values are NOT the proof.

An INITIAL direct FFT check FAILED (discrepancy 1.637): target g-covariant components had been projected *as if Euclidean indices*, and the reconstructed Fourier output omitted the spatial shear pullback. Both frame typing and spatial sampling were repaired before acceptance. This was not a change to the theorem or original source.

Local complete 5-file ZIP / Moderator conversation:
 iw_int8_rot025_alias_projector_rank_hs_bundle.zip
 SHA256 0f9a568bc48d4388f6ecc17f0e45674d9314505be52b2112a9393efe4b0b6099
Contains complete scientific Markdown, standalone executed Python, complete JSON results, source-run log, README and SHA256 manifest. Clean unzip ZIP-CRC PASS, 5/5 SHA256 PASS, clean no-helper mathematical rerun PASS with source check explicitly SKIPPED; clean separate helper-PRESENT SHA-confirmed rerun PASS and JSON BYTE IDENTICAL to archived results. Original helper intentionally not redistributed. Historical production dtc0a_runtime_v0_3_1.py bytes UNAVAILABLE. GitHub Python code publication is NOT claimed.

## Limits / disposition
PASS finite spectral rank, HS identity and retained helper-matched calculations; no independent referee / project owner adoption / BW ingestion / Moderator EXEC asserted. Metric-adapted affine E_g covariance owned by MT13 remains true, but naive recomputed raw-k P_g is not natural over high-band folded Fourier modes. Rank fractions are NOT energy fractions. No physical J3/K invariance, GR/gauge gravitational radiation, astrophysical theory or background-covariant spacetime operator inferred. Mature linear-algebra host, NO NOVELTY / NO CANON / NO EXEC / NO PHYSICAL UPGRADE / NO NEW TASK.
