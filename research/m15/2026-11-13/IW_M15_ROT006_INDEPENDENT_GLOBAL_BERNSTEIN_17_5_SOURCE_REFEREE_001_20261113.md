---
artifact_id: IW_M15_ROT006_INDEPENDENT_FULL_M13_B25_17_BERNSTEIN_SOURCE_AUDIT_001_20261113
return_id: IW_M15_ROT006_INDEPENDENT_SOURCE_B25_FULL_POSITIVE_GLOBAL_BERNSTEIN_17_PLUS_5_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: I1_INTERNAL_DIFFERENT_CELL_NONBLIND_INDEPENDENT_ALGORITHM_EXACT_RATIONAL_GLOBAL_POSITIVE_SOURCE_REFEREE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_M13_AUXILIARY_B_COEFFICIENT_BOX_EPS_1E_MINUS_7_ONLY / NO_HISTORICAL_DTC0A_PRODUCER_IDENTITY / NO_I3_EXTERNAL_REVIEW / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT006 — new independent rational/interval Bernstein audit of all 17 global-positive gates for M13 B

## 0. Material scientific decision and sharp audit scope

**I1 NONBLIND DIFFERENT-CELL MATHEMATICAL REFEREE: PASS ALL 17/17 GLOBAL POLYNOMIAL GATES AND 5/5 GLOBAL SHELL POSITIVITY GATES.**

M15 has now independently authored and ACTUALLY EXECUTED a standalone BigInt normalized-rational interval program reconstructing the original M13 five-shell N41 channel B geometry and EVERY source-critical polynomial certificate in Geeky-S12 ROT007 and its 25-independent-coefficient epsilon=10^-7 enlargement in ROT013. No Geeky-S12 ROT007, 012, 013 source code, library, mathematical function, reported machine result, or output interval was imported or invoked by the M15 verifier. Original source was fetched from its byte-frozen M13 Git blob, not reconstructed from a Geeky report.

This closes M15's formerly explicit **independent-program positive-gates review gap** from ROT005, subject to the exact frozen source/model, and allows a conditional in-cell conclusion about the mathematical theorem: for EVERY independent choice of 25 source quartic coefficients in the fixed widened M13 box of relative epsilon<=10^-7, EVERY alpha in [0,1/5] and EVERY REAL 0<delta<=1/40, the globally minimum squared profile loss among legal beta in [0,1/5] with |beta-alpha|>=delta is attained by at least one of the two closest legal beta=alpha+-delta points. This is source-typed **ONE COMMON POSITIVE AMPLITUDE** geometry, not a physical sensor/NASH proof. When the closest left or right beta is out of [0,1/5], only the valid side is considered. The proof is conditional on the explicitly checked algebra and exact certificate-to-topological-argument combination below.

**New independent corroboration is not a claim of first discovery.** M13 first owns the auxiliary N41 source and quartic data; Geeky-S12 ROT007 first owns the theorem and original 17+5 certificate, ROT013 first owns epsilon=1e-7 positive source-coefficient robustness; M15 supplies NEW independent source-backed code and mathematical audit, not its first result. REC11 ROT029 independently extended the epsilon=1e-7 NEGATIVE phase at delta=.02514 and reexecuted owner's POSITIVE source code but did not rewrite the 17 positive gates. AUD2 ROT004 independently checked 5 shell signs and epsilon=1e-8 negative example, but NOT all 17 positive gates. Thus M15 ROT006 adds the previously missing independent implementation of the 17 global-positive Bernstein gates. The neighboring negative phase remains REC11 FIRST at eps1e-7 and Geeky FIRST at eps1e-8; M15 ROT005 independently covered eps1e-8 negative.

## 1. Frozen original source, model, and mathematical chain

Original M13 coefficient source public:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
GIT blob exactly a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, 7501 source bytes, five masks k=2..6, quartic coefficient indices j=0..4. Actual independently fetched source blob verified BEFORE computation. Coefficient i,j original [lo,hi] source interval widened to [lo−eps*|lo|,hi+eps*|hi|] with eps=1e-7, separately for each of all 25 coefficients; all decisions exact, no binary64 decisions. The actual original directed intervals remain inputs and are not rounded to midpoints.

Original M13 derived disjoint five shell mean energy profiles s_i(t) from the nested mask quartics g_k(t)=sum_j g_kj*t^j, n_k=(41−2k)^3:
  w=(7778,6938,6146,5402,24389),
  s_i(t)=(n_i*g_i(t)−n_(i+1)*g_(i+1)(t))/w_i, i=2..5;
  s_6(t)=g_6(t).
The computation scales all source coefficients by exact 10^12 so its loss D² is scaled by 10^24, preserving all signs and source extrema. No empirical meaning of these scales.

For a=s(alpha), b=s(beta), p=<a,b>_w, q=<b,b>_w:
  D²(alpha,beta)=min_(c>0)||a−c*b||_w²
                 =||a||²_w−p²/q
                 =N(alpha,beta)/q,
  N=sum_(i<j) w_i*w_j [a_i*b_j−a_j*b_i]².
The five independent global shell-Bernstein positivity checks ensure s_i(t)>0 for ALL t in [0,.2] and ALL source coefficient choices, so p>0 and q>0 and the positive gain minimizer c=p/q is admissible.

By differentiating the profile loss at fixed alpha, with p_beta,q_beta and H=2p_beta q−p q_beta,
  partial_beta D²=−p H/q².
The elementary exact finite wedge identity factors
  H=(alpha−beta)P(alpha,beta),
  P=2 sum_(i<j) w_i*w_j Q_ij(alpha,beta)*R_ij(beta),
where Q_ij is the FORMAL polynomial quotient
  [s_i(alpha)s_j(beta)−s_j(alpha)s_i(beta)]/(alpha−beta)
and R_ij=s_i'(beta)s_j(beta)−s_i(beta)s_j'(beta).
This is an algebraic identity for quartics: the numerator vanishes symbolically at alpha=beta and the quotient is a finite sum of antisymmetric monomial factors. The M15 source independently constructs each Q coefficient from m>n pairs and each R from the integer factor m−n. No numerical division by alpha−beta, no near-diagonal cancellation. P is bivariate of alpha degree<=3 and beta degree<=9. The exact rational directed intervals enclose every real source coefficient choice, including dependencies in repeated source terms (outward interval arithmetic can overestimate but never under-enclose).

The sign of partial_beta D² is the sign of (beta−alpha)*P for p,q positive. Thus positivity of P along the relevant beta branches establishes strict radial monotonicity; P_beta>0 inside the exceptional small-beta region confines any interior critical point on the left to a MAXIMUM rather than a strict minimum. Every global minimum of the source-profile objective in the legal domain therefore belongs to {0,alpha−delta,alpha+delta} intersection legal beta domain, with 0 only if alpha>=delta.

Uniform two-nearest condition for delta<=.025 requires two more directed certificate families:
  (i) P(alpha,alpha−.025)>0 for alpha∈[.028,.033]. Combined with P_beta>0 below beta=.008 and P>0 above beta=.008, this prevents a lower legal beta interval between alpha−.025 and alpha from containing an interior minimum.
  (ii) F0(alpha)>0 on alpha∈[.028,.2], with
     F0=N(alpha,0)*q(alpha−.025)−N(alpha,alpha−.025)*q(0).
This is an exact polynomial comparison D²(alpha,0)>D²(alpha,alpha−.025) because both denominators q(0),q(alpha−.025) are positive. For delta<=.025 and alpha>=.028, radial monotonicity from alpha−.025 to alpha implies D²(alpha,alpha−delta)<=D²(alpha,alpha−.025)<D²(alpha,0). Therefore 0 never wins against a nearer left legal beta. For alpha<=.028 global P>0 already gives simple monotonicity and nearest minimizers on both sides. Combining covers ALL real delta<=.025 continuously and all alpha, not grid samples.

No new firstness or general-theory result is claimed for Lagrange identity, weighted projections, Chebyshev/Bernstein positivity, or exact rational interval arithmetic: established classical hosts.

## 2. Independent precise 17+5 calculation and sign margins

The M15 DIFFERENT implementation uses source direct_B with all 25 independent epsilon=1e-7 coefficient intervals and BigInt normalized reduced rationals for all interval endpoints. Builds five disjoint shell quartics, then reconstructs Qij,Rij,P, P_beta and F0 entirely from source, with separate polynomial arithmetic and binomial monomial-to-Bernstein conversions. All tests are sign comparisons of rational interval LOWER bounds, not float signs.

The 5 shell global polynomial positivity tests [lower values, scale1e12], each >0:
  +.00986178294683, +.0130904291119, +.0182389743451, +.0245831059585, +.0333565421813.

The 17 polynomial gates are separated as:
- P>0 on five exact alpha-beta rectangles covering beta >= .008 in [0,.2]: lower displays
  +6815.74212379, +14507.4405312, +1317614.37380, +2772.05104509, +179364.762393.
- P>0 in exceptional small rectangle alpha∈[0,.028], beta∈[0,.008]: lower +309.955394682.
- P_beta>0 for alpha∈[.028,.2], beta∈[0,.008]: lower +38287.6732417.
- F0(alpha)>0 on eight exact rational subintervals partitioning [.028,.2]: lower
  +.790166440397, +.467680779954, +2.39879938607, +7.29847425773, +31.9870044877, +268.564041389, +2965.44835907, +1145455.93840.
- P(alpha,alpha−.025)>0 on the two alpha segments [.028,.03] and [.03,.033]: lower
  +1679.09762537, +3224.46560746.

All 17 lower endpoints and all 5 shell lower endpoints are EXACT RATIONAL STRICTLY POSITIVE. Printed decimals are rounded presentation only. The smallest of the eight F0 lower bounds is about +0.467680779954, and its exact sign is verified from BigInt rational arithmetic. ALL interval arithmetic retains the original 25-dimensional coefficient dependencies by inclusion (possibly conservative bounds). This is not based on random finite alpha/beta sampling.

The results reproduce the original Geeky-S12 epsilon=1e-7 widened box sign margins but arise from wholly NEW independently authored polynomial/rational code, not by calling the author's certifier. Agreement is an independently executed source certificate, NOT third-party I3 review or physical validation.

## 3. Reproduction and fail-closed control

Standalone public M15 mathematical reproducer (independently authored, 9690 UTF-8 characters):
https://github.com/wmakiela-tech/Nash-iw-research/blob/1cf31e99b02cfba48e50ac3f62d07f71f92b2d7f/research/m15/2026-11-13/m15_rot006_independent_exact_B25_bernstein_17_gates.js
Exact Git commit 1cf31e99b02cfba48e50ac3f62d07f71f92b2d7f, Git blob 2faa1ed97e3fb5c126bcff7e9b90242d883d2bae; full original fetched file byte-text identical PASS.
The pure mathematical function independentCertificate(source), from its exact pinned PUBLIC source, was EXECUTED IN V8 against separately GitHub-fetched exact original M13 direct_B.json SHA-verified bytes. In order to compile the Node standalone source body in V8, only the first #! interpreter shebang line was removed; the entire pure mathematical body was otherwise identical. Result 17/17 strict polynomial tests and 5/5 shell tests PASS. The Node CLI optional file-lock wrapper was PUBLISHED and verified by source readback but not run as a separate standalone Node process; do not substitute the V8 run for an unexecuted CLI invocation.

A SECOND exact source retrieval from the pinned code and M13 source was executed independently again: 17/17 PASS, 5/5 PASS. A negative fixture modifying the M13 k2,j0 source coefficient pair to [-100,-100] while leaving the other coefficients unchanged produced the expected fail-closed error SHELL_SIGN_FAIL, not a false all-signs-positive return. The V8 tool fetch independently checked source M13 Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 and M15 public script Git blob 2faa1ed97e3fb5c126bcff7e9b90242d883d2bae. The test verifies one negative corruption, not an exhaustive parser/fuzz audit.

Complete machine-readable M15 original computed certificate and negative control, pinned GitHub CREATE+READBACK PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f609a888ecf4b316e99ae7b6babf30406a51bd55/research/m15/2026-11-13/IW_M15_ROT006_INDEPENDENT_17_BERNSTEIN_5_SHELLS_RESULTS_001_20261113.json
Commit f609a888ecf4b316e99ae7b6babf30406a51bd55, Git blob a72e288850ca2923cd5bd30278dc50558b9c5e64, byte-exact readback PASS.

The original Geeky proof and 25 coefficient source actually read in this rotation:
https://github.com/wmakiela-tech/Nash-iw-research/blob/402ead39de6839ea1db50c0420d6d4f037213b41/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT007_M13_B_THREE_CANDIDATE_REDUCTION_AND_NARROW_THRESHOLD_BRACKET_001_20261112.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/49fb59ee7c9aa5f967455c4a9969579fbd755fea/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT013_SOURCE_B_QUARTIC_COEFFICIENT_ROBUST_PHASE_GATE_001_20261113.md
REC11 independently derived stronger epsilon=1e-7 negative for the SAME source coefficient box:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6f632128d7c2fe2f4d3a55cffc5d63a8886994c3/research/rec11/2026-11-13/IW_REC11_ROT029_GEEKY_S12_ROT013_SHARED_COEFFICIENT_LIPSCHITZ_REFEREE_001_20261113.md .
AUD2 separately checked eps=1e-7 five shell and eps=1e-8 negative, independent mathematics:
https://github.com/wmakiela-tech/Nash-Priv/blob/0885f2239004941501f815ffd6fe82173579d9ab/audits/aud2/2026-11-13/IW_AUD2_ROT004_GEEKY_S12_ROT013_25_COEFFICIENT_ROBUST_NEGATIVE_WITNESS_AND_FIVE_SHELL_GATES_BOUNDED_INDEPENDENT_REFEREE_001_20261113.md .
This report does not claim to replace either independent review, and their priority is preserved.

## 4. Strict source-transfer and anti-self-sealing ceiling

The object is the M13 auxiliary N41 five-mask channel B profile with one COMMON positive gain. Geeky-S12 ROT014 first showed how a DIFFERENT nuisance class with independent gains in all five shells can destroy parameter identifiability; this does not contradict this global theorem because the allowed nuisance model is different. M15 ROT006 does not claim to test those different gains here.

Original M13 is a functionally matched auxiliary source, not a byte-identical restored full historical runtime dtc0a_runtime_v0_3_1.py. The 25 independent relative coefficient uncertainty box is a purely mathematical coefficient-space assumption, not proven realizable by changes to the original Fourier fields or an actual instrument. M15 ROT006 cannot imply physical K/J3/TPE/NASH, GR/PBH/BBN sensor effects, real measurement noise, numerical producer completeness, new physics, or any mathematical novelty.

This is an I1 internal NONBLIND **different-cell independent implementation** for a declared source-typed mathematical subclaim, not an I3 external blind audit or an experimental acceptance. BW ING ID NOT asserted; KN13 owns source-event-only custody. No Living Theory canon edit, owner override, EXEC_SIGN or new task cascade. Return to Moderator/Geeky/REC11/AUD2/KN13 as informational science, requiring their own independent source/authority decisions.

Final:
M15_ROT006_INDEPENDENT_GLOBAL_17_5_PASS /
EPS_1E_MINUS_7_25_COEFFICIENT_BOX /
ACTUAL_PINNED_NEW_CODE_EXECUTED / FAIL_CLOSED_NEGATIVE_FIXTURE_PASS /
M13_AND_GEEKY_FIRSTNESS_PRESERVED /
NO_HISTORIC_DTC0A_BYTE_ID / NO_NASH_PHYSICAL_CLAIM /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
