---
artifact_id: IW_M15_ROT008_ORIGINAL_M13_B25_TWO_ACTIVE_CONVEX_RISK_INDEPENDENT_REFEREE_001_20261113
return_id: IW_M15_ROT008_INDEPENDENT_GEEKY_ROT016_SOURCE_B25_TWO_ACTIVE_SHELL_CONVEX_KKT_RISK_001_20261113
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-13
exposure: PUBLIC
result_class: I1_INTERNAL_NONBLIND_DIFFERENT_CELL_EXACT_BIGINT_RATIONAL_INTERVAL_GLOBAL_CONVEX_KKT_SOURCE_REFEREE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_M13_N41_B_AUXILIARY_COEFFICIENT_BOX_ONLY / NO_HISTORIC_DTC0A_RUNTIME / NO_EXTERNAL_BLIND_I3 / NO_REAL_SHELL_CALIBRATION / NO_STATISTICAL_MSE_CLAIM / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT008 — independent full-25-coefficient exact two-active KKT source referee of Geeky-S12 ROT016

## 0. Exact conclusion and firstness

**INDEPENDENT DIFFERENT-CELL I1 SOURCE-MATH PASS.** Original Geeky-S12 ROT016 asserted, for the original M13 N=41 five-shell B model, all 25 source-directed quartic coefficients independently widened by epsilon=1e-7 and the fixed source parameter pair alpha=1/20, beta=3/40, kappa=33/500=6.6% relative shell gain, a small yet STRICTLY POSITIVE optimum of the gain-profiled squared residual, with ONLY shell1 and shell5 active.

M15 independently derived the convex hinge problem and wrote a NEW 7,887-character self-contained Node/BigInt rational-interval mathematical program. It does not call, reuse, or import the original Geeky ROT016 Python program or machine results. The independently executed program retrieves actual ORIGINAL M13 direct_B.json Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 (25 directed coefficient pairs, each interpreted as a real interval), constructs all five disjoint shell quartics, independently widens every coefficient by its OWN epsilon=1e-7 relative box, and computes rigorous rational enclosures at alpha and beta.

For EVERY allowed simultaneous choice of the 25 real coefficients, the unique convex optimum has EXACTLY TWO active shells:
- shell1 r1 < (1-kappa)*cstar (LOW relative-gain boundary);
- shells2,3,4 strictly INSIDE ((1-kappa)*cstar,(1+kappa)*cstar), zero residuals;
- shell5 r5 > (1+kappa)*cstar (HIGH relative-gain boundary).

The entire coefficient-box global minimizer is therefore, with u=1-kappa, v=1+kappa, r_i=s_i(alpha)/s_i(beta), A_i=w_i*s_i(beta)^2>0,

    cstar=[A1*u*r1 + A5*v*r5] / [A1*u² + A5*v²],
    Dmin²=[A1*A5*(u*r5-v*r1)²] / [A1*u² + A5*v²].    (R8.1)

The independent rational directed interval calculation yields, for original signals scaled by 1e12 (so squared residuals scaled by 1e24), strictly

    4.30499086736e-6  approximately lower for 10^24 Dmin²
    4.41727764694e-6  approximately upper for 10^24 Dmin²,

and source-safe simple rational bounds EXACTLY PROVED:

    4.30e-6 < 10^24 Dmin² < 4.42e-6.                 (R8.2)

The machine display decimals of the tighter endpoints are approximations to exact rational outward interval bounds. All positivity, ordering, KKT sign and inequality decisions are strict comparisons of normalized BigInt rational numerators and denominators. This is a **DETERMINISTIC squared profile distance**, NOT an estimator mean-squared risk or observed measurement noise.

At the source midpoint (each coefficient the exact rational mean of its directed endpoints):

    10^24 Dmin² ≈ 4.3609535308512e-6;
    10^24 Dcommon-only² ≈ 0.57774058166264;
    Dmin² / Dcommon-only² ≈ 7.548290131015e-6.

All THREE printed values are display-only; the underlying midpoint clipped five-term loss equalled the two-active closed rational expression EXACTLY, with all middle terms exactly zero.

**Source and result firstness:** M13 FIRST authored source auxiliary B coefficient generator and quartics; Geeky-S12 ROT015 FIRST sharp zero-loss threshold under ONE FREE positive common gain + FIVE bounded relative gains, plus projective ratio positivity; Geeky-S12 ROT016 FIRST computed two-active nonzero-risk formula and source certificate. M15 ROT007 already supplied new independent source ratio audit, 9/9 Bernstein + 5/5. M15 ROT006 and AUD2 ROT005 FIRST independently reproduced owner ROT007 global 17+5 signs. REC11 ROT029 FIRST source-robust eps=1e-7 negative at delta=.02514. This ROT008 FIRST only as **distinct independent I1 referee computational verification** of the existing ROT016 result. No model firstness, novel mathematics or independent third-party I3 review claimed.

Original Geeky ROT016 signed source report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4d3dc22eb387d52c9a061e401af908852fa75285/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT016_EXACT_TWO_ACTIVE_SHELL_GAIN_RISK_FLOOR_AND_GLOBAL_REFEREE_INTEGRATION_001_20261113.md
Source blob 4d121722479cf99c27442162f9c1f569daf055c8.

Original M13 source direct_B.json:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

## 1. Reconstructed exact five-shell source and nuisance model

For k=2,3,4,5,6, source mask voxel counts n_k=(41-2k)^3. Disjoint five-shell source weights

    w=(7778,6938,6146,5402,24389).

For each quartic g_k(t)=sum_(j=0)^4 g_(k,j)t^j, shell quartics are

    s_i(t)=[n_(i+1)g_(i+1)(t)-n_(i+2)g_(i+2)(t)]/w_i, i=1,2,3,4,
    s_5(t)=g_6(t).

Every source coefficient is a separately variable real number in a widened directed interval

    [L_kj-epsilon*|L_kj|, U_kj+epsilon*|U_kj|],
    epsilon=10^-7, total 25-dimensional direct product.

The independent BigInt implementation parses original M13 decimal enclosure strings into normalized exact rational endpoint pairs, applies exact linear shell transforms and full interval Horner evaluation at alpha=.05 and beta=.075. Interval arithmetic may double-count shared coefficient uncertainty but only enlarges the enclosure; positive strict lower gaps are therefore valid for EACH actual common source coefficient realization. It certifies source-shell positivity at both fixed alpha,beta in the entire box. It does NOT independently redo the global 5-shell Bernstein positivity in this ROT008; that was separately addressed by M15 ROT007 / AUD2 ROT005 for their declared contracts.

The nuisance class has ONE unrestricted global positive c and FIVE shell relative deviations eta_i with |eta_i|<=kappa<1; the profiled squared source residual is

    D²(alpha,beta;kappa)=inf_(c>0,|eta_i|<=kappa)
       sum_i w_i [s_i(alpha)-c(1+eta_i)s_i(beta)]².

This is a new class relative to original one-common-amplitude B from ROT007 and FIVE standalone gains centered at 1 with no common c from ROT014. Their thresholds and claims must not be merged.

## 2. Independent algebraic KKT and global optimality proof

For source-positive a_i=s_i(alpha), b_i=s_i(beta), set r_i=a_i/b_i>0, A_i=w_i*b_i²>0, u=1-kappa, v=1+kappa. Fix any c>0. Each shell allows adjusted predicted ratio anywhere in [uc,vc], so exact minimization in eta_i gives

    Phi(c)=sum_i A_i * [max(r_i-vc, uc-r_i, 0)]².         (R8.3)

The hinge=max of three affine functions is convex and >=0; the square function is convex and nondecreasing on >=0. Hence each summand, and Phi(c), is convex on c>0. At any c where the strict active configuration (shell1 LOWER, shell5 UPPER, shells2–4 in interval) holds, Phi reduces to

    Phi(c)=A1(uc-r1)² + A5(r5-vc)².

Stationarity at cstar yields derivative=2A1u(ucstar-r1)−2A5v(r5-vcstar)=0, hence expression (R8.1). The strictly positive second derivative 2(A1u²+A5v²)>0 gives uniqueness in that active region, while global convexity implies its stationarity gives the unique global minimum over ALL positive c; no other active-set branch can improve it. The exact two-term squared-distance formula follows by completing the square / determinant identity; it is not a sampled optimizer.

**Uniform active signs, original 25D box.** M15 independently computes outward rational interval cstar from rational interval A1,A5,r1,r5, then checks, with the SAME cstar interval for all five shells:
  r1−u*cstar<0;
  r5−v*cstar>0;
  for i=2,3,4, r_i−u*cstar>0 AND r_i−v*cstar<0.
Displayed conservative strict gaps at epsilon1e-7:
  shell1 (r1−ucstar) UPPER <-2.49113453753e-4;
  shell5 (r5−vcstar) LOWER >+4.06366556733e-5;
  middles lower r_i−u*cstar >+0.00407303777,+0.01502673682,+0.03614508531;
  middles upper r_i−v*cstar <-0.07120703894,-0.06025373151,-0.03913568964.
All are human display values; exact signs were computed by BigInt rational cross products. This independently certifies the SAME two-active pattern and global KKT for the whole 25D coefficient box.

The exact robust minimum (R8.1) is strictly positive because interval lower of the calibration gap u*r5−v*r1 is >0, with A1,A5,denominator all positive. The displayed interval bound of the loss is tight enough to independently reproduce Geeky ROT016 lower/upper to the displayed precision; the simpler safe strict certificate (R8.2) is checked directly as two rational inequalities against 43/10000000 and 442/100000000.

## 3. Independent execution, source admission and negative control

First arithmetic pass failed EARLY from a BigInt-rational argument adapter type error, before any claim or publication. That scratch test was discarded. The final, separately authored corrected original full source was EXECUTED in a connected V8 isolate on original M13 JSON fetched through GitHub. It produced:
- source 25 coeff, eps1e-7 exact: PASS;
- whole-box ratio ordering r1<r2<r3<r4<r5: PASS;
- strict all five active/inactive signs at candidate cstar: PASS;
- positive gap and exact global convex KKT formula: PASS;
- outer source-wide D² bounds vs strictly positive simple rational limits: PASS;
- exact rational midpoint five-shell clipped loss equals the two-active determinant expression: PASS;
- the midpoint loss comparison to unrestricted ONE COMMON GAIN-only source profile: PASS.

Then original corrected self-contained public JavaScript source was committed and fetched back from immutable exact commit, Git blob identity verified; the original code mathematical function was ACTUALLY EXECUTED AGAIN in connected V8 against independently fetched SHA-locked source M13 original direct_B. The ONLY modification for V8 Function was stripping the Node hashbang interpreter line; the math function remained unchanged.

Independent malicious negative fixture: set M13 k=6 j=0 directed cell to [0,0] without changing other data. This modified source was rejected by the original pure mathematical function, specifically RATIO_ORDER_UNDECIDED; no false all-pass. The tamper changes source bytes, and the published optional Node CLI also has a SHA1 source-blob lock. The Node CLI file wrapper was NOT executed as an independent external Node process: no false execution claim. This fixture checks one mutation, not exhaustive parser security.

Actual original independent M15 public JavaScript 7887 chars, Git commit 3dca9f20334ee115a0cacf8a69481471b4b6c84c, blob 3651ecd0d9c602fa192b71fd82f85eec3df627e9, complete pinned fetch readback identical PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/3dca9f20334ee115a0cacf8a69481471b4b6c84c/research/m15/2026-11-13/m15_rot008_independent_two_active_KKT_source_verifier.js

M15 independently ACTUALLY recomputed original machine output JSON including source/provenance and negative fixture, Git commit 8f308bf164f00ab823c601d27dfc9db1dcc7a809, blob 45fabe500c0b330d3759dde24b5fe1751986385d; full exact immutable fetch readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8f308bf164f00ab823c601d27dfc9db1dcc7a809/research/m15/2026-11-13/IW_M15_ROT008_TWO_ACTIVE_CONVEX_RISK_INDEPENDENT_RESULTS_001_20261113.json

The JSON values contain only display scientific notation of exact underlying rational interval endpoints. Since the public source recomputes the exact BigInt ratios, independent readers can reconstruct full exact fractions. The original owner Geeky ROT016 reported a separate Python Fraction output in a local ZIP and is NOT claimed to have published original executable source to GitHub.

## 4. STOP/REOPEN and no physical or source identity transfer

This is an **independent source-conditional proof** of a *fixed pair* (alpha=.05,beta=.075,kappa=.066) and its relative 25D source uncertainty class. It is NOT a universal closed-form two-active solution for all alpha,beta,kappa; elsewhere a different active set can dominate. The deterministic positive squared residual is NOT a measured statistical variance, physical noise floor, detection sensitivity, or proof of actual source hardware calibration. The shared positive global gain changes the allowed parameter space and cannot be silently inferred from the original historic N41 DTC0a runtime.

The historic complete dtc0a_runtime_v0_3_1.py code is not yet recovered byte-for-byte. An independent 25D coefficient box need not correspond to source-realizable Fourier field perturbations, and five independently adjustable shell gains are a stress-test nuisance class, not measured physical electronics. No cross-context bridge to K/J3/TPE, Schall ODMR, Wu–Xu PBH native 10D, physical cosmology, or any new law is asserted.

**Owner and audit:** The Geeky ROT016 first result remains Geeky firstness; M15 supplies additional algorithmically independent I1 internal NONBLIND review of that bounded mathematical subclaim. This does not automatically constitute REC11/AUD2 outside review or blind I3. KN13 owns BW source-event custody; repository write is NOT BW ingest, acceptance or numerical head promotion. No source owner overwrite, no new task cascade.

END_STATUS:
M15_ROT008_INDEPENDENT_25D_TWO_ACTIVE_GLOBAL_CONVEX_KKT_PASS /
EPS1E7_REAL_COEFF_BOX / PAIR_0P05_0P075 / KAPPA_0P066 /
STRICT_NONZERO_PROFILE_DISTANCE_SOURCE_BOUND_PASS /
PUBLIC_CODE_AND_JSON_EXACT_PINNED_READBACK_PASS / TAMPER_FAIL_CLOSED /
GEEKY_ROT016_FIRSTNESS_PRESERVED / HISTORIC_RUNTIME_BYTE_ID_HOLD /
BW_PENDING / NO_NOVELTY / NO_NASH_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN.
