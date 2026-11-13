---
artifact_id: IW_M15_ROT007_PROJECTIVE_M13_B25_GAIN_SHARP_THRESHOLD_INDEPENDENT_REFEREE_001_20261113
return_id: IW_M15_ROT007_INDEPENDENT_M13_B25_PROJECTIVE_RATIO_AND_SHARP_GAIN_THRESHOLD_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: I1_INTERNAL_NONBLIND_DIFFERENT_CELL_INDEPENDENT_EXACT_RATIONAL_SOURCE_REFEREE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_M13_AUXILIARY_B_SOURCE_ONLY / NO_HISTORIC_DTC0A_RUNTIME / NO_I3_EXTERNAL_REVIEW / NO_REAL_SHELL_CALIBRATION / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT007 — independent projective gain threshold and 9-Bernstein source referee

## 0. Executive science decision, no firstness theft

**I1 CONDITIONAL SOURCE-MATH PASS.** I independently authored a new exact BigInt normalized-rational interval verifier that does NOT import any Geeky-S12 code or mathematical routines. Using 25 immutable original M13 directed quartic coefficient intervals with independent epsilon=1/10^7 expansion, the verifier reconstructs (a) all five globally positive disjoint-shell quartics, and (b) the entire degree-8 polynomial T(t)=s4'(t)s5(t)-s4(t)s5'(t)-(1/8)s4(t)s5(t). All FIVE source-shell Bernstein checks and all NINE T Bernstein coefficients have STRICT POSITIVE RATIONAL LOWER endpoints for EVERY t in [0,.2], and EVERY allowed independent coefficient choice. This is a continuum certificate, not a numerical grid. The smallest T Bernstein lower, with energies scaled1e12 and T scaled1e24, is about +.0006435003940397; its actual sign was checked using exact rational cross products.

This independently corroborates the central source-typed GLOBAL PROJECTIVE INJECTIVITY claim Geeky-S12 ROT015 FIRST reported. The five-shell vector map t -> [s1(t):...:s5(t)] is injective up to common positive gain, because t -> log[s4(t)/s5(t)] is strictly increasing with derivative >1/8. M15 does NOT claim mathematical novelty, original data firstness, author ownership, I3 outside-blind review, or any physical consequence.

Original-source priority: M13 FIRST produced the auxiliary five-mask N41 B channel original directed quartics, public original direct_B.json Git blob a6f50fbe5904e580e84c87ee87c5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Geeky-S12 ROT007 FIRST global three-candidate and nearest-two delta<=.025 under ONE common positive gain; ROT013 FIRST full epsilon=1e-7 coefficient-box positive; ROT014 FIRST structurally different FIVE standalone gains nonidentifiability; ROT015 FIRST ONE free global gain PLUS FIVE bounded RELATIVE gains sharp threshold and global ratio gate. Its corrected original pinned report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e16c7773039268bcd882f300056f5e4ac7024ff7/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT015_SHARP_PROJECTIVE_GAIN_THRESHOLD_AND_ROBUST_GLOBAL_RATIO_INJECTIVITY_001_20261113.md
Original source report Git blob dd1a06e9c3d2ba82ece3ccfd9f01b825f2f2c8fa.

REC11 ROT029 FIRST independently improved source pointwise NEGATIVE robustness at delta=.02514 to epsilon=1e-7; AUD2 ROT005 and M15 ROT006 independently checked OLD one-common-gain full 17+5 positive source gates, before this new ROT015 ratio question. These are distinct results and no cross-cell firstness is appropriated. The latest native Mech-S9 original Wu-Xu six-hadron trace belongs to other source owners, is not used here, and cannot be bridged to this N41 B auxiliary model.

## 1. Exact mathematical contract and independent implementation

The 25 independently variable source coefficients g_kj, k=2..6, j=0..4, belong to the FULL real intervals [L_kj-eps*abs(L_kj),U_kj+eps*abs(U_kj)], epsilon=1/10^7. Source original every nested pair of directed bracket strings is parsed into exact rational endpoints (not float midpoints). Source mask sizes n_k=(41-2k)^3. Five disjoint shell weights are W=(7778,6938,6146,5402,24389). Their quartic profiles are
  s_i(t)=(n_(i+1)*g_(i+1)(t)-n_(i+2)*g_(i+2)(t))/W_i (i=1..4);
  s5(t)=g6(t).
Each of the 25 uncertain coefficients is independently widened and converted by exact linear shell transformation to an interval polynomial. Dependency losses in repeated interval expressions can make bounds conservative but cannot make an invalid strict sign positive. All source g coefficients are multiplied by exactly 10^12, preserving positivity, ratios and optimal gain comparisons.

Define B=s4 (FOURTH DISJOINT SHELL, not mask4), C=s5, both globally positive, and
  T(t) = B'(t)*C(t)-B(t)*C'(t) - (1/8)*B(t)*C(t).
This is a polynomial of degree <=8. The independent M15 code constructs T from coefficient-wise exact rational interval convolution and derivative operations; no input Geeky T polynomial is copied.

A degree n polynomial in power coefficients t_j is transformed on [0,1/5] into Bernstein coefficients
  b_i = sum_(j=0)^i t_j*(1/5)^j*binom(i,j)/binom(n,j).
Every Bernstein basis function is nonnegative on the interval, so if ALL b_i have positive lower endpoint, the entire interval-valued polynomial is positive across the WHOLE continuum, for every coefficient realization. For T, all NINE coefficient lower bounds are strictly positive; for each s_i the full-domain Bernstein lower bounds are also strictly positive. All arithmetic decisions use reduced BigInt rational comparisons.

Then
  d/dt log(B/C) = [B'C-BC']/BC >1/8.
For any alpha != beta in [0,.2], the source-integrated logarithmic ratio difference is greater in absolute value than |alpha-beta|/8. For r_i=s_i(alpha)/s_i(beta) this implies
  max_i log(r_i)-min_i log(r_i) > |alpha-beta|/8.
Thus the exact sharp relative shell gain threshold below obeys
  kappa_crit > tanh(|alpha-beta|/16)>0.
This sufficient global quantitative separation bound is not advertised as sharp.

## 2. Sharp relative nuisance threshold, independent proof

For any positive five signals a_i=s_i(alpha), b_i=s_i(beta), any positive shell weights W_i, kappa in [0,1), consider
  D² = inf_(c>0, |eta_i|<=kappa) sum_i W_i*(a_i-c*(1+eta_i)*b_i)^2.
With r_i=a_i/b_i>0, exact zero residual is possible if and only if every r_i=c*(1+eta_i), equivalently for the same c each interval
  r_i/(1+kappa) <= c <= r_i/(1-kappa)
intersects all others. This occurs precisely when
  kappa >= (rmax-rmin)/(rmax+rmin) = kappa_crit.
At the sharp boundary choose c=(rmin+rmax)/2 and eta_i=r_i/c-1. This is an exact algebraic construction, and W_i affect positive residual magnitude but not the zero-loss threshold. Below this threshold, the infimum is also strictly positive: any c approaching a zero residual would be bounded by the positive finite ratios and kappa<1, hence any zero-infimum sequence has a convergent subsequence to a forbidden exact fit. This is elementary projective/Chebyshev calibration, no method novelty.

The free common c is essential: it is a DIFFERENT nuisance class from ROT014's five gains individually required to be within [1-kappa,1+kappa] about the literal value 1 with no free c. No false claim that ROT014's different theorem is refuted.

## 3. Independent source-fixed parameter example

For alpha=1/20=.05, beta=3/40=.075, ALL five s_i(alpha)/s_i(beta) are strictly interval ordered for the full 25D box, so actual rmin=r1 and rmax=r5. Using independently evaluated exact rational interval Horner polynomials and positive rational divisions, M15 verifies the rigorous bounds (printed outward as rounded approximations):
   0.06626786193306 < kappa_crit < 0.06627133247008.
Actual decision compared rational bounds to 66/1000 and 67/1000 directly. Therefore for EVERY 25D coefficient selection, at kappa=.066 zero-error profile match is IMPOSSIBLE and at kappa=.067 it is POSSIBLE with suitable c and eta_i. This is a coefficient-space mathematical dichotomy, NOT source-native field, voxel calibration, hardware or measurement uncertainty.

On the exact original SOURCE MIDPOINT coefficient member, the independent rational result is kappa_crit≈0.06626959720165 and c≈0.5702370703999. The executable exact rational test checked all FIVE equalities a_i=c(1+eta_i)b_i with zero rational residual, and |eta_i|<=kappa_crit. The five displayed eta_i are about (-0.0662696,-0.0586810,-0.0394723,-0.00243825,+0.0662696). Display floats do not enter any sign/equality decision.

## 4. Actual execution and custody

ORIGINAL M15 newly authored self-contained JavaScript Node18+ source 9033 characters, GitHub commit 457bbb091375420cb46e5d80a0d1450e1f9b3d36, Git blob a7a7dfb93fc3c6813fb3ef7b47820c831fac4fbe, FULL PINNED FETCH READBACK PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/457bbb091375420cb46e5d80a0d1450e1f9b3d36/research/m15/2026-11-13/m15_rot007_independent_projective_M13_B25_gain_referee.js

M15 FIRST executed the independent mathematics in connected V8 on newly fetched SHA-verified ORIGINAL M13 JSON, then PUBLISHED code, fetched identical bytes from exact immutable Github commit and EXECUTED its mathematical body AGAIN after stripping ONLY Node hashbang for Function compilation. Results: 9/9 full T Bernstein lower strict signs, 5/5 shell source-global positivity, exact 6.6/6.7% bound, 5/5 exact midpoint zero residual identities, all PASS.

One deliberate adversarial negative fixture setting original source mask6 constant coefficient to [0,0] caused the expected fail-closed error 'global shell positivity failed' rather than a false positive PASS. Only this tamper control performed; not a full fuzzer or verification of the separate standalone Node CLI wrapper. The CLI wrapper with Git SHA1 original source lock is in published code but was NOT executed in Node; the executed object was the mathematically identical public pure function body in connected V8. No independent physical field data or original historic runtime was executed.

ACTUAL computed machine JSON from independent pinned pure-math execution including all nine positive rational-directed-sign displays and fail-closed negative control GitHub CREATE+FULL PINNED READBACK PASS, commit 1792876eff6e3d07235d47a617750c2ce50f2062, blob 812380d33ce6f7e19b4fd6c69a92d22abf2abb86:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1792876eff6e3d07235d47a617750c2ce50f2062/research/m15/2026-11-13/IW_M15_ROT007_INDEPENDENT_PROJECTIVE_GAIN_9_BERNSTEIN_RESULTS_001_20261113.json

Nine lower bound display values of T in 1e24 scaled source:
  .0006435003940397, .009004537210595, .01666433858830,
  .02362878902447, .02925993319227, .03230615782397,
  .03093152463642, .02274427287127, .004824509674401.
Every exact bound strictly positive.

## 5. Source-to-physical limits, status

All conclusions are for ORIGINAL M13 auxiliary N41 B five-mask source coefficients and their deliberately independent relative 25D mathematical interval box. The original historical complete runtime dtc0a_runtime_v0_3_1.py is still NOT recovered byte-for-byte; neither certificate validates physical producer identity. Five independent relative gains are not demonstrated realizable in an actual Fourier field measurement, Schall device, laboratory calibration or real tensor dataset. No NASH K/J3/TPE, GR/BBN/PBH, new theory or physical insight is claimed. The global one-common-gain nearest theorem from ROT006 and the new five-relative-gain exact identification threshold concern different observation contracts and must never be conflated.

M15 scoped independent I1 SOURCE MATH referee: PASS. Recipient or outside referee signoff, independent blind I3, BW actual INGEST and public guard CI status are NOT claimed. KN13 manages BW; no fabricated ING ID. No CANON, EXEC_SIGN, owner override or task cascade.

FINAL: M15_ROT007_INDEPENDENT_PROJECTIVE_9_BERNSTEIN_PLUS_5_SHELLS_PASS /
SHARP_GAIN_THRESHOLD_AND_PAIR_BOUNDS_PASS /
ORIGINAL_SOURCE_25D_EPS_1E_MINUS_7_ONLY /
ORIGINAL_PINNED_MATH_REEXECUTION_PASS / TAMPER_FAIL_CLOSED /
GITHUB_PENDING_BW_INGEST / NO_HISTORIC_DTC0A_BYTE_ID /
NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN.
