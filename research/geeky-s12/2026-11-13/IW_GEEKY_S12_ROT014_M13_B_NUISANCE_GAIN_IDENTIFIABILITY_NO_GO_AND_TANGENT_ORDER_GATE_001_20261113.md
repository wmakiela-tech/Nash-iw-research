---
artifact_id: IW_GEEKY_S12_ROT014_M13_B_NUISANCE_GAIN_IDENTIFIABILITY_NO_GO_AND_TANGENT_ORDER_GATE_001_20261113
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-13
exposure: PUBLIC
class: NEW_NUISANCE_CLASS_CONSTRUCTIVE_NONIDENTIFIABILITY / EXACT_SOURCE_INTERVAL_BERNSTEIN_DERIVATIVE_BOUND / SINGLE_SHAPE_NUISANCE_TANGENT_ORDER_LOSS / INDEPENDENT_BOUNDED_REFEREE_INTEGRATION
status: AUTHOR_EXACT_SOURCE_RATIONAL_SOURCE_BOUND_PASS / AUD2_M15_EXTERNAL_CELL_BOUNDED_NEGATIVE_AND_SHELL_PASS / GLOBAL_POSITIVE_ROT007_REFEREE_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_FUNCTIONALLY_MATCHED_AUXILIARY_N41_B_FIVE_MASK_SOURCE / NO_ORIGINAL_HISTORIC_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT014 — strukturalny brak identyfikowalności po zmianie modelu wzmocnień; nowe niezależne zwroty AUD2 i M15

## 0. Najważniejszy kontekst: NOWE niezależne werdykty do ROT013

13 listopada AUD2 ROT004 oraz M15 ROT005 niezależnie przejrzały oryginalne, bajtowo zamrożone 25 skierowanych współczynników M13 kanału B, oryginalny Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Obydwie komórki wykonały NOWE implementacje BigInt rational, NIE uruchamiały oryginalnego kodu matematycznego Geeky ROT007/ROT013.

AUD2 ROT004: niezależny I1 INTERNAL NONBLIND DIFFERENT-CELL PASS ograniczony do (a) pięciu dodatniości powłok N41 B przy KAŻDYM 25-współczynnikowym zaburzeniu relative eps<=1e-7 oraz (b) ścisłego kontrprzykładu source przy alpha=.03082, delta=.02514, far beta*=.000001, gdy wszystkie 25 coefficients niezależnie zaburzono eps<=1e-8. Dolny exact directed gap D²*1e24 left - far +0.00001966189681927486940139; right - far +0.20316849802330542162994. Public dispatch:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT
Private pinned report:
https://github.com/wmakiela-tech/Nash-Priv/blob/0885f2239004941501f815ffd6fe82173579d9ab/audits/aud2/2026-11-13/IW_AUD2_ROT004_GEEKY_S12_ROT013_25_COEFFICIENT_ROBUST_NEGATIVE_WITNESS_AND_FIVE_SHELL_GATES_BOUNDED_INDEPENDENT_REFEREE_001_20261113.md

M15 ROT005: independently authored, publicly pinned exact normalized-rational shell/wedge 25-coefficient implementation, same strict negative eps=1e-8 pointwise source witness PASS, no global positive verdict:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f1afc1d67dd3188fae6a81d5bc39b8bfca48c6ba/research/m15/2026-11-13/IW_M15_ROT005_INDEPENDENT_M13_B25_RELATIVE_BOX_POINTWISE_REFEREE_001_20261113.md

KEY HONEST LIMIT: neither referee checked all 17 bivariate/line/univariate Bernstein P/F0 inequalities of Geeky ROT007 positive GLOBAL theorem (all alpha, all real delta<=.025); that positive claim remains OWNER-CERTIFIED, independent full-review PENDING. Neither audit is external blind I3 or physical validation; neither is a BW numeric promotion. The negative phase and five shell positivity have now acquired independent different-cell bounded I1 corroboration.

## 1. Newly tested scientific branch — nuisance-model sensitivity, NOT delta threshold refinement

ROT007 optimizes ONE common positive scalar gain r multiplying five shell energies s_i(beta). That assumption is SOURCE-DEFINING. ROT014 analyzes TWO DISTINCT nuisance classes as explicit mathematical stress tests; they are NOT source-native DTC0a physical assumptions:

(A) Five independent per-shell gains g_i constrained within [1-kappa,1+kappa].
(B) One extra shape nuisance theta in addition to common positive gain c, with gain pattern c*(1+theta*h_i) designed from log-derivative at a fixed anchor alpha0=1/20.

Both are classical nuisance-tangent/projection mechanisms, not a novel general method. Their relevance is to expose what ROT007 cannot transfer to.

## 2. Theorem A — exact zero-loss neighborhood with independently bounded shell gains

For the original source coefficient family, let s_i(t) be the five disjoint-shell quartic energy polynomials. Define, for alpha,beta in [0,1/5], kappa in (0,1),

 D_5g²(alpha,beta;kappa)
  := min_{g_1,...,g_5 in [1-kappa,1+kappa]}
      SUM_i w_i [s_i(alpha)-g_i*s_i(beta)]².

The source-weight vector is w=(7778,6938,6146,5402,24389), original n_k=(50653,42875,35937,29791,24389). s_i positive throughout the interval.

**PROVED EXACT SOURCE-INTERVAL BOUND:** for EVERY realization of the ORIGINAL source directed 25 quartic coefficient intervals and for ALL t∈[0,1/5],
 s_i(t)>0 and sup|s_i'(t)|/inf s_i(t)<566 for all i=1,...,5.
The proof is an independent exact rational Fraction interval monomial-to-Bernstein upper/lower enclosure for degree4 and its degree3 derivative, not a sampling of t. Original 25 source bracket endpoints are verified against immutable Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 before calculation. Actual exact comparisons M_i < 566*m_i PASS for all 5 shells.

Detailed reader display (all shell and derivative values scaled by 10^12):
 shell 1: min s>=.009861818352395729, max|s'|<=5.5744486344003015, ratio<565.256;
 shell 2: min s>=.013090462972866413, max|s'|<=5.760107445098132, ratio<440.024;
 shell 3: min s>=.018239007511768848, max|s'|<=5.992179145336571, ratio<328.537;
 shell 4: min s>=.024583138646238557, max|s'|<=6.0866733331361464, ratio<247.596;
 shell 5: min s>=.033356545541269086, max|s'|<=5.613204221406068, ratio<168.279.
All signs were decided on exact rational comparisons. Displayed decimals do not replace certificate.

For any alpha,beta, take the legal choice g_i=s_i(alpha)/s_i(beta), which is strictly positive. By the mean value theorem,

 |g_i-1| = |s_i(alpha)-s_i(beta)|/s_i(beta)
          <= (sup |s_i'|/inf s_i)*|alpha-beta|
          < 566*|alpha-beta|.

Hence whenever |alpha-beta|<=kappa/566, every g_i lies in its stated allowed interval and EVERY term in D_5g² vanishes identically. Thus

 **forall kappa∈(0,1), forall alpha,beta∈[0,.2],
     |alpha-beta|<=kappa/566  =>  D_5g²(alpha,beta;kappa)=0.**

For kappa=.01 (one percent), sufficient exact parameter separation <=1/56600≈0.0000176678445; for kappa=.001 (0.1 percent), <=1/566000≈0.00000176678445. These are conservative SUFFICIENT radii, not maximal nonidentifiability radii. There is no probabilistic or physical claim; independent arbitrary shell gains are a new nuisance class.

**Logical scope:** this proves failure of unique profile-based discrimination among sufficiently close parameter values in the five-gain model. It does NOT, on its own, disprove the claim that a nearest legal beta attains some global minimum: loss=0 produces ties rather than necessarily a farther lower competitor. ROT007 original nearest geometry under ONE shared gain is logically unaffected.

Without gain caps, choose g_i=s_i(alpha)/s_i(beta) at ANY alpha,beta in the full parameter domain and D_5g²=0 identically: the full five-gain model loses all source profile identifiability by construction.

## 3. Theorem B — just ONE additional shape nuisance kills first-order score

Fix anchor alpha0=1/20=.05. For a given source-realization define
  a_i=s_i(alpha0);
  d_i=s_i'(alpha0);
  h_i=d_i/a_i;
and new nuisance profile
  D_shape²(alpha0,beta) =
       min_{c>0,theta real : 1+theta*h_i>0 for all i}
       SUM_i w_i [a_i-c(1+theta*h_i)*s_i(beta)]².

At beta=alpha0+t, Taylor-expand s_i(beta) = a_i+t*d_i+t²*e_i+O(t³) with e_i=s_i''(alpha0)/2. Choose c=1, theta=-t, legal for sufficiently small |t| since all a_i>0 and h_i finite. Then
 (1-t*h_i)*s_i(alpha0+t)
  = a_i+t*(d_i-h_i*a_i)+t²*(e_i-h_i*d_i)+O(t³)
  = a_i+t²*z_i+O(t³),
 where z_i=e_i-d_i²/a_i.
Thus D_shape²(alpha0,alpha0+t) <= SUM_i w_i (t²*z_i+O(t³))² = O(t^4), a guaranteed loss of first-order distinguishability.

By contrast, for the original source ROT007 single common gain, local Taylor expansion yields
 D_common²(alpha0,alpha0+t)
  = t² I_common+O(t³), with
 I_common=||d||_w²-(<a,d>_w)²/||a||_w².

The source interval exact rational minor (shell rows 1,5) of [a,d] is strictly negative, about -0.02160368032249769 when a,d scaled by 1e12; hence I_common>0 for every realization of the original extremely narrow source input coefficient intervals. The new nuisance model has identically zero efficient first-order local score in the direction of alpha. This is the well-known geometric projection onto nuisance tangent space: the parameter derivative d lies in the nuisance span{a,a*h} = span{a,d}. General efficient score/nuisance literature:
https://pmc.ncbi.nlm.nih.gov/articles/PMC6191046/

Exact interval source check also verifies all 5 shape h_i lie inside (-28,28); therefore c=1,theta=-t is legal for all |t|<=1e-3 and beta within domain. The (shell rows 1,3,5) exact directed 3x3 determinant of columns [a,d,z] is strictly negative, about -0.026525143186109795 using scaled 1e12 vectors. So the GENERIC optimized next-order quartic coefficient is positive, not an accidental identically zero local curve. The exact rank checks are valid for all original bracket coefficient realizations (sign no zero crossing).

For the MIDPOINT source realization (not a historical measured field), the exact Fraction least-squares Gram-Schur formulas yield:
 I_common*1e24 = 1527.91885837949,
 C_shape*1e24 = 6428.6649244543905,
 with
 D_common²/t² -> I_common,
 D_shape²/t^4 -> C_shape
 as t -> 0.
Exact rational generated examples:
 t=.001: common D²*1e24≈0.001499246528, shape D²*1e24≈6.070507839e-9, ratio shape/common≈4.049039118e-6.
 t=.0005: common D²*1e24≈0.0003783900653, shape D²*1e24≈3.904132083e-10, ratio≈1.031774468e-6.
 t=.0002: common D²*1e24≈0.0000608868170, shape D²*1e24≈1.016818524e-11, ratio≈1.670014256e-7.

These are EXACT-Fraction-calculated source auxiliary MIDPOINT inputs with FLOAT display only. They quantify different *orders* of local loss. The nuisance h is specifically aligned to the source derivative at alpha0, NOT a general externally calibrated hardware nuisance vector. No claim all possible one-parameter gain patterns must destroy identifiability.

## 4. Exact reproducibility and safety

Executable original Python3 stdlib-only code and original byte-frozen M13 source and full output JSON delivered as one current-turn user ZIP:
 Geeky_S12_ROT014_gain_nuisance_no_go_and_tangent.zip
 ZIP SHA256 e70ec18d9878e2fd7e6c93c01d6554a309a689d4981329265e780e4742680916
 ZIP 9775 bytes, 5 members, CRC PASS, each member full byte readback and SHA256 PASS.

Code SHA256 68bdc0b339f39df28251a7ac2da279ba46f9be6465e8c39aa9ec30957a74ff0d. Original copied M13 direct_B JSON source SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f. Output JSON SHA256 191acd36bc9e090050632c17f14078191b079c6b5ccf38541e020ca1e5b2d9d8. All actually executed local program; no public GitHub code mirror is claimed. Reader can reproduce by Python3 only and two local files in ZIP; script checks source original Git blob SHA before parsing.

There is no requirement for mpmath, NumPy, scipy, Julia or internet at runtime. All exact mathematical positivity tests and determinant signs are checked on Python fractions.Fraction objects; human-facing floating numbers in JSON are presentation only.

## 5. Scientific owner and explicit non-transfer boundary

M13 retains FIRST source generator, N41 B quartics, shell covariance geometry. Geeky ROT007 retains FIRST source conditional one-common-gain global three-candidate / delta<=.025 nearest theorem; ROT013 first coefficient robustness. This ROT014 analyzes a NEW nuisance admissibility class, and its failure of identifiability does NOT contradict prior theorems, since the parameter space changed. The core facts are mature classical weighted least squares and nuisance tangent projection; no novelty claim.

Independent reviews now actually exist but are BOUNDED: AUD2 ROT004 shells and negative witness PASS_EXACT_I1, M15 ROT005 negative witness PASS; none signed all 17 positive Bernstein gates or the topological reasoning. REC11/AUD2 full independent positive theorem review remains PENDING, M15 accepts only its own bounded negative evidence, owner adoption of global theorem NOT VERIFIED, KN13 BW ingestion still PENDING. No extra tasks or threshold toy scans requested.

No physical transfer to original historic DTC0a runtime dtc0a_runtime_v0_3_1.py (byte-missing), NASH K/J3/TPE, experiment, sensor shell gain noise, or prior-art novelty. No source-consistent proof that five gain distortions actually exist in original producer.

FINAL:
AUD2_M15_BOUNDED_NEGATIVE_EXTERNAL_CELL_PASS /
SOURCE_FIVE_SHELL_INTERVAL_LIPSCHITZ_566_PASS /
FIVE_INDEPENDENT_GAIN_EXACT_ZERO_LOSS_LOCAL_NEIGHBORHOOD_PASS /
ONE_SHAPE_TANGENT_FIRST_ORDER_INFORMATION_LOSS_PASS /
GLOBAL_POSITIVE_17_BERNSTEIN_REFEREE_PENDING /
M15_GLOBAL_OWNER_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
