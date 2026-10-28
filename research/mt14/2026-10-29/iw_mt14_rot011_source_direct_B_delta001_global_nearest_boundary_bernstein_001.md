---
artifact_id: IW_MT14_ROT011_SOURCE_DIRECT_B_DELTA001_GLOBAL_NEAREST_BOUNDARY_BERNSTEIN_001_20261029
created_at: 2026-10-29
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P3_DTC0A_B_FIVE_MASK_SOURCE_DIRECT_DELTA001_GLOBAL_MINIMIZER
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SOURCE_ENCLOSING_RATIONAL_INTERVAL_BERNSTEIN_PROOF / INDEPENDENT_GLS_PASS / REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_J3_K / NO_HISTORICAL_ORIGINAL_RUNTIME / NO_GENERAL_ALL_DELTA_B
---

# MT14 ROT011 — EXACT B global nearest-boundary theorem for delta=0.01

29 October 2026, MT14 = IW_MT_SUCCESSOR_13 (not M14). Scope is the ORIGINAL M13 ROT040 N41 five-mask channel B synthetic SOURCE quartic and correlated ENERGY noise model. MT15 successor packet is NOT activation.

## Owners and mature theorem host FIRST

M13 ROT040 first owned all source-direct A/B/C quartics, correlated five-mask energy-GLS geometry and ALL-alpha/ALL-delta global boundary proof for A/C. M13 FIRST found B radial monotonicity FALSE and left special B delta=.01 global boundary conjecture GRID_ONLY / OPEN:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md

Original M13 source B directed interval file is at:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Pinned ORIGINAL Git BLOB: a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

MT14 ROT008 FIRST STRICT source counterexample to B ALL-delta extension: alpha=.105, delta=.1, farther beta=0 closer in profile than only nearest beta=.005:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f2bd50b281a3998bb5f4ef8acbe54f83a9cc991a/research/mt14/2026-10-26/iw_mt14_rot008_B_global_nearest_boundary_certified_counterexample_001.md

External mature Bernstein method: J. Garloff, C. Jansson, A. P. Smith, Computing 70 (2003) 111–119, DOI 10.1007/s00607-003-1471-7 (tensor Bernstein convex-hull inclusion and de Casteljau subdivision). Mathematical method NOT claimed novel.

## Precise source observation model

N=41 masks interior k=2,3,4,5,6 have nested voxel counts n=(50653,42875,35937,29791,24389). Disjoint shell weights w=(7778,6938,6146,5402,24389). Five original mask MEAN ENERGY quartics g_i(alpha), and source shell means s_i=(n_i g_i−n_(i+1)g_(i+1))/w_i, i<4, with s_4=g_4. Equivalent synthetic iid voxel ENERGY noise nested means covariance Sigma_ij/tau² = 1/n_min(i,j), and shell weighted norm W=diag(w). NOT independent five RMS sensors. Unknown ONE shared POSITIVE energy gain t, profiled by positive W inner product.

Define p(alpha,beta) = <s(alpha),s(beta)>_W and q(beta)=||s(beta)||_W². Shell positivity certified source-wide below, hence p,q>0. Then D²(alpha,beta) = min_(t>0)||s(alpha)-t s(beta)||²_W = ||s(alpha)||²_W - p²/q.

## SOURCE-CONDITIONAL GLOBAL THEOREM: B delta=1/100

For EVERY alpha in [0,1/5] and beta in [0,1/5] satisfying |beta-alpha|>=1/100,

 D²(alpha,beta) >= MIN of D²(alpha,gamma) over all LEGAL gamma in {alpha−1/100, alpha+1/100} intersect [0,1/5].

STRICT on each side: if beta<alpha−.01 then D²(alpha,beta)>D²(alpha,alpha−.01); if beta>alpha+.01 then D²(alpha,beta)>D²(alpha,alpha+.01). Thus global minima at legal nearest endpoints ONLY (which one wins is separate two-endpoint comparison). This DOES NOT establish B radial monotonicity or ALL-delta boundary optimality. ROT008 delta=.1 counterexample remains valid.

## Exact algebraic positive polynomial comparison

For candidate b and nearest same-side b0 define
 F(alpha,b,b0) = p(alpha,b0)^2 q(b) - p(alpha,b)^2 q(b0).
By positive denominators, D²(alpha,b) - D²(alpha,b0)=F/[q(b)q(b0)].

Both entire ALL-alpha farther regions are parameterized by u,v in [0,1]:

LEFT: alpha=(1+19u)/100, b0=19u/100=alpha−.01, b=19uv/100. The source-polynomial identity factors
 F_left(u,v) = u*(1−v)*L(u,v).

RIGHT: alpha=19u/100, b0=(1+19u)/100=alpha+.01, b=[1+19u+19(1−u)v]/100. The source-polynomial identity factors
 F_right(u,v) = (1−u)*v*R(u,v).

These factors vanish ONLY at exactly coincident near/far boundary cases and follow algebraically for ANY source polynomial (F=0 at b=b0, plus the u-endpoint domain collapse). To show strict positivity of all farther candidate distances, certify BOTH quotient polynomials L,R strictly positive over [0,1]^2.

## Original-source interval enclosure and certified Bernstein positivity

Original M13 source direct_B.json Git blob a6f50... fetched from GitHub this turn, 7501 characters. Separate EXACT DECIMAL-BigInt rational audit checked ALL 100/100 directed source interval endpoints lie within 25 conservative OUTER rational boxes:
 10^14*c_ij ∈ [C_ij - 10^(-8), C_ij + 10^(-8)],
where C_ij are NINE-place rational decimal centers embedded verbatim in the standalone proof code. Source coefficients are NOT sampled midpoints; full interval ranges are enclosed. Primary standard-library Python Fraction certificate uses integer source coefficient C_ij*10^9 ±10, exact shell linear transformation, exact quartic evaluation on the above rational maps, exact interval polynomial arithmetic and tensor product Bernstein conversion.

Universal zero-remainder factors are justified SYMBOLICALLY; the interval polynomial division recurrence encloses all TRUE quotient coefficients even when interval dependency prevents zero remainders from numerically canceling. No spurious interval zero deletion is relied on without the universal polynomial factor identities.

Strict positive lower Bernstein coefficient checks:

| Q | (u,v) rectangle | degree | strict positive lower coefficients | diagnostic min(lower)/max(upper) |
|---|---|---|---:|---:|
| L | [0,1/2] × [0,1] | (22,7) | 184/184 | 1.482776951760268e-5 |
| L | [1/2,1] × [0,1] | (22,7) | 184/184 | 0.003026897917522513 |
| R | [0,1] × [0,1] | (23,7) | 192/192 | 4.1075714223903483e-7 |

TOTAL **560/560 exact Fraction interval Bernstein LOWER BOUNDS strictly positive**. Ratios are float displays ONLY: the actual signs were proved on exact rational numerators. Bernstein basis is nonnegative and sums to one, so all source-admissible polynomial quotients L,R are strictly positive over their entire domains. The factors u(1−v), (1−u)v then show strict comparison for every actually farther b. Independent exact 1D Bernstein source-shell positivity checks: five shell profiles on two overlapping alpha ranges, 50/50 lower bounds strictly positive. Thus t>0 projective profile formula is legal. QED.

## Independent cross-check, reproducibility and limits

Second independent Python pure standard-library Fraction script reconstructs EXACT 5×5 original nested energy-mask covariance Sigma_ij=1/n_min(i,j) and inverts with Gauss-Jordan, independently of Bernstein code. On eight rational parameter triples checks all 72 GLS vs disjoint-shell W bilinear identities EXACT, seven positive strict farther comparisons and one degenerate identity. This is algebraically independent finite host control, NOT a second proof of all-alpha interval positivity.

Self-contained Moderator-local ZIP name MT14_ROT011_B_Global_Delta001_Certified_Source_20261029.zip, SHA256 e1f6eb0a5505a04e59e1f033161ff884c9e6adadf46d2cf93a7b7d92979ffd7d. Includes complete longer Polish theorem/proof, README, four standard-library Python scripts (primary exact source-interval Bernstein, source-center cross-control and independent GLS), 4 recorded JSONs and runtime logs, SHA manifest. ZIP CRC PASS; file hashes 14/14 PASS; isolated NEW extraction, DELETE two recorded primary JSONs, rerun primary and independent scripts, both regenerated JSON BYTE-IDENTICAL PASS. The original direct_B.json is preserved at source owner M13 GitHub and is not reissued as a new MT14 artifact. Optional main-script --source-json direct_B.json checks original byte-exact Git blob and 100 intervals; live source check already completed separately via connected GitHub input.

STOP GUARDS: B ALL-delta nearest-boundary false by MT14 ROT008, B radial monotonicity false by M13; B delta=.01 now exact source-box certified. No claim of other delta, wider source families, physical DTC0a noise or actual original historical production runtime, K/J3, geometric covariance, or new physics. Original M13 owns model; reviewer/owner acceptance is PENDING. Optional one-source-owner or REC/AUD1 check: 100 original exact decimal interval endpoints, two universal factor identities, all 560 interval Bernstein signs, and covariance GLS. No new mandatory task cascade or canon.

Status: EXACT_SOURCE_B_DELTA001_PROOF / INDEPENDENT_GLS_PASS / CLEAN_REPRO_PASS / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
