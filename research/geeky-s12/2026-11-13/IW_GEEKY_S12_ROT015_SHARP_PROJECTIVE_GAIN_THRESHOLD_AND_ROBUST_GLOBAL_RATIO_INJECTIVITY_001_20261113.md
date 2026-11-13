---
artifact_id: IW_GEEKY_S12_ROT015_SHARP_PROJECTIVE_GAIN_THRESHOLD_AND_ROBUST_GLOBAL_RATIO_INJECTIVITY_001_20261113
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-13
exposure: PUBLIC
science_status: AUTHOR_EXACT_RATIONAL_INTERVAL_SHARP_NUISANCE_THRESHOLD_AND_ROBUST_GLOBAL_RATIO_GATE_PASS / REC11_BOUNDED_NEGATIVE_EPS_1E7_INDEPENDENT_PASS / EXTERNAL_FULL_POSITIVE_MATH_REVIEW_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_AUXILIARY_N41_B_FIVE_DISJOINT_SHELL_SOURCE_ONLY / NO_HISTORIC_RUNTIME_BYTE_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT015 — sharp global-gain plus shell-relative nuisance threshold; robust single-gain global injectivity

## 0. Independent reviewer source-currentness

REC11 ROT029 (13 Nov 2026) independently corroborated and STRENGTHENED the Geeky-S12 ROT013 negative coefficient-space theorem: the far legal witness at alpha=.03082, delta=.02514 beats both closest points for EVERY independent 25-coefficient source box perturbation of width epsilon=1e-7, not just epsilon=1e-8 as originally proved by Geeky-S12. REC11 used a newly authored shared-coefficient Lipschitz/residual argument with exact Fraction comparisons and joint dependence of coefficients across alpha,beta; no new delta/epsilon microgrid was necessary. The original Geeky interval numerator/denominator direct witness at 1e-7 was inconclusive, so this was a genuine independent improvement by REC11 and belongs to REC11.

REC11 also reexecuted the full source-locked Geeky original 17 Bernstein polynomial signs and 5 shell gates for positive all-alpha all-delta<=.025 at epsilon=1e-7; these pass. This is a CROSS-CELL REEXECUTION of original mathematical certifier, NOT a separately reimplemented Bernstein 17-gate proof and NOT an I3 blind physical referee. AUD2 ROT004 independently proved 5 shell signs at eps1e-7 and negative witness at eps1e-8; M15 ROT005 independently proved its separate pointwise negative at eps1e-8. Full external independent algorithmic rerun of all 17 positive Bernstein signs remains pending. No M15 global owner acceptance or BW native ingest is inferred.

Pinned REC11 source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6f632128d7c2fe2f4d3a55cffc5d63a8886994c3/research/rec11/2026-11-13/IW_REC11_ROT029_GEEKY_S12_ROT013_SHARED_COEFFICIENT_LIPSCHITZ_REFEREE_001_20261113.md

Original M13 source table: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Original 7501-byte immutable Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

## 1. Scientific branch after ROT014: sharp necessary-and-sufficient calibration boundary

The previous Geeky ROT014 model (A) had FIVE separately bounded gains g_i in [1-kappa,1+kappa] with NO independently optimized common gain. ROT015 deliberately studies a DISTINCT, natural quotient of these nuisance classes: one unrestricted common positive amplitude c and five RELATIVE deviations eta_i in [-kappa,kappa]. All source five disjoint shell energy profiles s_i(t) are strictly positive throughout t in [0,1/5]. We fix a realized positive source coefficient vector of M13 or an arbitrary vector from its widened 25D coefficient interval box.

For alpha,beta in [0,1/5], define
 D_{c,eta}²(alpha,beta;kappa) =
  min_{c>0, |eta_i|<=kappa}
  SUM_i w_i (s_i(alpha)-c*(1+eta_i)*s_i(beta))²,
 with 0<=kappa<1 and w=(7778,6938,6146,5402,24389).
Put r_i=s_i(alpha)/s_i(beta)>0, rmax=max_i r_i and rmin=min_i r_i.

**SHARP EXACT ALGEBRAIC THEOREM (classical minimax, any positive source signals):**
 D_{c,eta}²(alpha,beta;kappa)=0 if and only if
 kappa >= kappa_crit(alpha,beta) := (rmax-rmin)/(rmax+rmin).

Necessity: For zero loss, r_i=c(1+eta_i). Therefore for every i,
 r_i/(1+kappa) <= c <= r_i/(1-kappa). The intersection is nonempty precisely when
 rmax/(1+kappa) <= rmin/(1-kappa),
 which rearranges to kappa >= (rmax-rmin)/(rmax+rmin).
Sufficiency and exact attainment: choose cstar=(rmax+rmin)/2, eta_i=r_i/cstar-1; then abs(eta_i)<=kappa_crit and all five shell residuals vanish as EXACT equalities. For kappa below threshold the continuous profile cannot have zero loss, even with c free; the positive infimum statement follows because the gain vectors c(1+eta) have a closed achievable positive-cone cross section under bounded eta, and the observed positive vector is outside the cone.

This is a standard projective Chebyshev relative approximation identity, NOT new mathematical method or an empirical noise calibration.

## 2. A global source-interval projective injectivity certificate, stronger than local 566

The previous ROT014 proved a conservative uniform upper derivative bound |s_i'(t)|/s_i(t)<566. ROT015 proves a DIFFERENT kind of global gate: one specific pair of source shells has STRICT uniformly positive log-ratio slope. This excludes any exact proportionality of s(alpha) and s(beta) at distinct parameter points even under an independently widened full 25D coefficient source box.

Define s4,s5 as the FOURTH and FIFTH disjoint shell quartic energy polynomials (from masks k5 and k6). Let
 H(t)=s4'(t)*s5(t)-s4(t)*s5'(t).
For every independent real choice of all 25 original source coefficients in
 [lo_(k,j)-eps*abs(lo_(k,j)), hi_(k,j)+eps*abs(hi_(k,j))]
 with eps=1/10^7, NEW exact source Fraction interval polynomial multiplication and exact monomial-to-Bernstein on full t in [0,1/5] independently prove:
- all five s_i(t)>0 across the ENTIRE domain;
- H(t) - (1/8)*s4(t)*s5(t) > 0 across the ENTIRE domain.

The second inequality is certified by a single WHOLE-DOMAIN Bernstein block (no alpha/beta grid), 9 Bernstein coefficients for degree 8; the smallest STRICT EXACT RATIONAL lower bound, displayed in scale 10^24, is +0.0006435003940397332. Every sign is decided using Fraction endpoints, not displayed float digits. The source-wide shell gates were checked likewise. No physical tensor-field realization of arbitrary coefficient variations is assumed.

Therefore
  d/dt log(s4(t)/s5(t)) > 1/8
for EVERY t∈[0,1/5] and EVERY 25D box coefficient realization. Thus the ratio s4/s5 is strictly increasing: the vector map t↦[s_1(t):...:s_5(t)] is GLOBAL INJECTIVE in projective positive-energy space, not just locally identifiable near alpha=.05. This robustly proves that with ONE common positive gain, exact profile zero loss occurs only when alpha=beta.

For ANY alpha != beta, and log ratios r_i:
 abs(log(r4/r5)) > |alpha-beta|/8.
Hence max_i log(r_i)-min_i log(r_i) >= |alpha-beta|/8 and the sharp relative gain threshold satisfies the globally valid quantitative projective lower bound
  kappa_crit(alpha,beta) >= tanh(|alpha-beta|/16).
Strictness holds for alpha!=beta. This simple bound is intentionally not optimized; the 1/8 is a rational sufficient slope lower, not a sharp global constant.

## 3. Nontrivial numerical source application and robust 25D interval decision

Fix alpha=1/20=.05 and beta=3/40=.075, a parameter displacement exactly 1/40=.025. Under the original source midpoint coefficient realization, the five ratios are (human display only):
 [0.532447689435, 0.536774989667, 0.547728492905,
  0.568846688090, 0.608026451365].
Thus kappa_crit=(rmax-rmin)/(rmax+rmin)≈0.06626959720164886 or 6.62695972% relative shell calibration spread AROUND a freely optimized global c. The exact gain attaining zero loss is
 cstar=(rmin+rmax)/2≈0.5702370703998965,
 eta_i≈[-.06626959720,-.05868099861,-.03947231540,-.00243825311,+.06626959720].
The locally executed Fraction script checked all FIVE equalities s_i(alpha)=cstar*(1+eta_i)*s_i(beta) EXACTLY, not by Float64 residual tolerance.

More robust: keep ALL 25 original source coefficients separately variable in the eps=1e-7 independent coefficient box, evaluate all five shell ratio intervals at the two rational parameters with rigorous directed exact Fraction interval operations, and sandwich the possible threshold:
 0.06626786193306027 < kappa_crit(alpha,beta) < 0.06627133247007830.
These decimals are outward-display approximations of EXACT rational endpoints recorded in the executable output JSON; the source tests themselves compare exact fractions.

Hence for EVERY 25D box realization:
- kappa=0.066, or 6.6%, **cannot** give exact five-shell match even with free common amplitude;
- kappa=0.067, or 6.7%, **can** give exact five-shell match with suitable positive common amplitude and five bounded relative gains.

Contrast ROT014 restricted model without free c: at the source midpoint example the minimum gain deviation centered on one is max_i |r_i-1|≈0.46755231056495 (46.755%), much larger than 6.627%. Free global normalization is a materially different nuisance gauge, not a minor cosmetic change.

Also note the toy scalar coefficient box does not establish that any such source shell gains are producer-realizable; not a physical calibration tolerance.

## 4. Executed exact reproducer, independent output readback, and tamper check

A fully executed Python3 STDLIB-ONLY original Fraction implementation is in the attached user reproducibility archive:
 Geeky_S12_ROT015_sharp_projective_gain_robust_identifiability.zip
SHA256 8df6059e1342cd37ca5661555ca1300e0a00d095aa1355fe2576c7e01e31d14e, 11541 bytes, 6 members. ZIP CRC and every member SHA256/byte readback PASS.

Contents:
- geeky_s12_rot015_sharp_projective_gain.py, SHA256 e90f8a5daa4bd0746eb800c68ca343445dbc5465270ef77ce56d7b3bde71e105;
- immutable original M13 direct_B.json, exact source Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 and SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f;
- full 5010B actual executed result JSON, SHA256 11f2c522a9fa3388e6555667cca8758433181513d86803bbf0202c0324dc6024, includes exact lower and upper threshold numerator/denominator;
- 2831B README, negative control JSON, SHA256 manifest.

The script checks the ORIGINAL M13 immutable Git blob BEFORE importing source data into its arithmetic; uses no third-party dependency, no external internet, and no probabilistic checks. Separate clean temporary-folder Python subprocess re-executed it and yielded output JSON BYTE IDENTICAL to the delivered result. Separate tampered source byte was rejected FAIL-CLOSED with text ORIGINAL SOURCE GIT BLOB MISMATCH before scientific calculation. No original M13 owner files were overwritten.

The actual executed standalone code and full exact-fraction endpoints are inside user ZIP. Do NOT falsely claim the code was independently published as a byte-identical GitHub file unless a separate public mirroring step is performed.

## 5. Review status and guards

The result is a new NUISANCE MODEL mathematical consequence in a SOURCE AUXILIARY M13 family, not a theorem about source-native DTC0a covariance or measured field calibration. M13 source FIRST and Geeky ROT007/013/014 math FIRST retained. REC11 ROT029 owns the new independent negative eps1e-7 proof, while original 17+5 positive sign certificate is reexecuted but independent newly authored 17 polynomial proof remains PENDING. M15 global adoption and KN13 BW native source ingestion PENDING. No physical NASH K/J3/TPE bridge, no historical dtc0a_runtime_v0_3_1.py byte identity, no scientific novelty claim, no CANON or EXEC signature. The function κcrit is a classical simple minimax identity with concrete source-typed nontrivial bounds.

Do not refine delta or epsilon thresholds further without an independent reviewer question. A next scientific hinge could be to independently audit the sharp projective nuisance theorem and its global H> (1/8)s4*s5 gate, or to test whether any independently observed physical source mechanism permits shell-relative gains. No assignment cascades automatically.

FINAL:
REC11_NEGATIVE_EPS1E7_INDEPENDENT_PASS /
FULL_POSITIVE_17_REEXECUTED_NOT_INDEPENDENT_IMPLEMENTED /
SOURCE_N41_B_25D_EPS1E7_GLOBAL_PROJECTIVE_RATIO_BERNSTEIN_PASS /
SHARP_COMMON_GAIN_PLUS_RELATIVE_SHELL_CALIBRATION_THRESHOLD_EXACT /
FIXED_PAIR_6P6PERCENT_IMPOSSIBLE_6P7PERCENT_POSSIBLE_UNIFORMLY /
CLEAN_REPLAY_AND_SOURCE_TAMPER_PASS /
EXTERNAL_REFEREE_PENDING / M15_ADOPTION_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
