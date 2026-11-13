---
artifact_id: IW_GEEKY_S12_ROT016_EXACT_TWO_ACTIVE_SHELL_GAIN_RISK_FLOOR_AND_GLOBAL_REFEREE_INTEGRATION_001_20261113
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-13
exposure: PUBLIC
science_status: AUD2_ROT005_AND_M15_ROT006_INDEPENDENT_I1_M13_B_GLOBAL_POSITIVE_17_PLUS_5_PASS / ROT016_AUTHOR_SOURCE_EXACT_FRACTION_TWO_ACTIVE_RISK_FLOOR_PASS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_N41_B_FUNCTIONALLY_MATCHED_AUXILIARY_25COEFF_SPACE_ONLY / HISTORICAL_DTC0A_RUNTIME_MISSING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT016 — niezależne recenzje ROT007/013 domknięte I1; ostre dodatnie minimum po dopuszczeniu kalibracji względnej 6,6%

## A. Materialnie nowy, niezależny status naukowy — źródłowa matematyka dodatnia

**AUD2 ROT005**, oryginalny osobny Python Fraction code, prywatny raport Git blob a2e2d7ecd2182de1e871f46f6de3199d23994081, i **M15 ROT006**, oryginalny osobny JS BigInt rational code, publiczny raport Git blob eb6bceead6f2c17225d61cee34c37cba7421725f, niezależnie od komórki Geeky wykonały od nowa wszystkie **17/17** ścisłych wielomianowych skierowanych nierówności Bernsteina oraz **5/5** dodatniości rozłącznych powłok. Oba niezależne kodowo source audits: PASS dla każdego wyboru wszystkich 25 współczynników M13 z przedziałów oryginalnych rozszerzonych niezależnie o ±epsilon=1e-7.

Jest to rzeczywiste uzyskanie **dwóch oddzielnych międzykomórkowych recenzji algorytmiczno-matematycznych I1** na źródłowym modelu: globalne trzy punkty i nearest przy dowolnych realnych alpha in[0,.2], delta in(0,.025] warunkowo na modelu z JEDNĄ wspólną dodatnią amplitudą. Wcześniej istniała tylko recenzja kontrprzykładu i pięciu powłok, albo reexecution 17 sign script przez REC11; status dziś podniesiono wyłącznie do SCOPED_I1_PASS, NIE I3_EXTERNAL, a tym bardziej nie do dowodu historycznej fizyki.

AUD2 private source:
https://github.com/wmakiela-tech/Nash-Priv/blob/24cd7664b7dd6d628268da509e98c1b0643d0e9b/audits/aud2/2026-11-13/IW_AUD2_ROT005_GEEKY_S12_M13_B_GLOBAL_17_BERNSTEIN_25_COEFFICIENT_INDEPENDENT_EXACT_REFEREE_001_20261113.md
M15 public source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/c88fc8cfc92f1c6734336f8169825cb8f31749ad/research/m15/2026-11-13/IW_M15_ROT006_INDEPENDENT_GLOBAL_BERNSTEIN_17_5_SOURCE_REFEREE_001_20261113.md
REC11 ROT029 first independent SHARED-source-coefficient Lipschitz proof of the negative witness at epsilon=1e-7 remains:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6f632128d7c2fe2f4d3a55cffc5d63a8886994c3/research/rec11/2026-11-13/IW_REC11_ROT029_GEEKY_S12_ROT013_SHARED_COEFFICIENT_LIPSCHITZ_REFEREE_001_20261113.md

FIRST: M13 original source 25 directed B quartic coefficients, first five-shell source model; Geeky ROT007 original positive global topology and negative counterexample; Geeky ROT013 original coefficient robustness; AUD2/M15/REC11 original independent tests belong to each respective reviewer. None of this authorizes a physical NASH claim.

## B. Nowa gałąź naukowa ROT016 — dodatnia strata poniżej progu nieidentyfikowalności

ROT015 already first proved the sharp zero-loss threshold for a DIFFERENT nuisance model, compared with ROT007: global positive amplitude c plus FIVE relative shell calibrations eta_i in [-kappa,kappa]. In ROT016 we go beyond a binary zero-fit test to the **exact strictly positive global minimum below that threshold**. We do NOT scan further delta, epsilon or sharp root values.

Let for arbitrary positive source signals:
 r_i=s_i(alpha)/s_i(beta), A_i=w_i*s_i(beta)^2>0, u=1-kappa, v=1+kappa.
Optimizing eta_i independently FOR FIXED c>0 gives the exact scalar profiled objective
 Phi(c)=SUM_i A_i * max(r_i-v*c, u*c-r_i, 0)^2.

Each term is a nonnegative squared hinge function of c and therefore Phi(c) is convex and piecewise quadratic. Its minimum is global. An active shell has r_i<uc or r_i>vc; otherwise its residual vanishes.

For alpha=1/20, beta=3/40, kappa=33/500=.066, an entirely NEW source-locked exact Python Fraction computation proves that for EVERY independent source coefficient realization inside M13's 25D relative epsilon=1e-7 box:
- r_1 strictly less than the other 4 shell ratios, r_5 strictly larger than the other 4;
- the two extreme active errors have the strict correct directions: shell1 r_1 <u*cstar, shell5 r_5>v*cstar;
- shells2,3,4 satisfy u*cstar<r_i<v*cstar STRICTLY (their three residuals are exactly zero);
- the unique convex minimizer is therefore obtained by balancing ONLY the two extreme shells.

**EXACT FORMULAS VALID FOR ALL THESE SOURCE REALIZATIONS**:
 cstar=(A_1*u*r_1+A_5*v*r_5)/(A_1*u^2+A_5*v^2).
 Dmin²=A_1*A_5*(u*r_5-v*r_1)^2/(A_1*u^2+A_5*v^2).

An entirely rational interval-enclosed coefficient computation with exact sign inequalities gives:
  4.304990867358497e-6 <= 10^24*Dmin² <= 4.417277646937626e-6
with shown decimals DISPLAY-ONLY; the full EXACT numerator/denominator of both rigorous bounds are in the executed local JSON. For user-readable outward-conservative bounds safely state 4.30e-6 < 10^24 Dmin² < 4.42e-6. This proves strictly POSITIVE minimum across the ENTIRE 25D source coefficient uncertainty family, not a Monte Carlo observation.

At original source midpoint coefficient realization (exact rational input):
 cstar = 0.5703420558923364 (float display).
 10^24*Dmin² = 4.3609535308512106e-6 (float display).
 Original global-common-only source minimised 10^24 Dcommon² = 0.5777405816626439 (float display).
 Ratio Dmin² / Dcommon² = 7.5482901310153644e-6, i.e. approximately 0.0007548290131%.
 A tiny yet strictly positive residual is compatible with source projective identifiability; a 6.6% shell relative nuisance removes almost all the distance without achieving exact zero. At 6.7% the exact zero-loss construction of ROT015 is legal. These percentages are nuisance class allowances, NOT physically measured calibration error.

## C. NEW exact source witness and fail-closed controls

ACTUALLY RUN independent author Python 3 standard library Fraction (no import from previous Geeky ROT015 code, no mpmath/NumPy), original source SHA-locked with Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 before scientific calculation. The new code calculates original five nested mask source quartics, full independent 25 coefficient eps1e-7 box and exact directed interval values at alpha=.05 and beta=.075. In particular it CERTIFIES uniformly across the whole coefficient box the signs of 10 active/inactive hinge residuals, so the two-active formula is not a guess from midpoint sample.

Two independent algebraic midpoint controls: (i) direct five-shell clipped eta minimization equals derived closed two-active pair formula EXACTLY as Fraction; (ii) kappa=0 gives original common-gain profile EXACTLY, and kappa=.067 gives exact five-shell zero-fit constructive solutions. The independent source code explicitly asserts all three controls.

CLEAN ISOLATED PYTHON SUBPROCESS RERUN: result JSON byte-identical SHA256 904b81ae7ece1e7c5469eed7781a7f592c424ac06541eb4b3a90eb2589241be2. FAIL-CLOSED NEGATIVE: deliberately change exactly one source byte in a TEMPORARY copy; original source files remain unchanged, script exits 1 with SOURCE_GIT_BLOB_MISMATCH, confirmed return code/terminal bytes. No historical runtime impersonation.

LOCAL USER ZIP (not publicly mirrored as source code):
 Geeky_S12_ROT016_two_active_exact_risk_robust_source.zip
 ZIP 11753 bytes, SHA256 5ec201787a9542459f1d7becbc0f87b70ac3029f919fbaf5a9d8088b3b7d0d35; CRC and exact all 7 member readbacks PASS. Contains executed Python 8955 bytes SHA256 3a6b447236ee2ff8266df70977cddd5bc97520fd23540bdc2a0a2a54879189c9, original byte-exact M13 B source 7501 bytes SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f, full exact Fraction JSON SHA256 904b81..., fail-closed control script/output, README, manifest.

The full script and exact fraction JSON are locally downloadable in the ZIP. No false claim these original executed Python source bytes are mirrored to public GitHub.

## D. Limits, owners, logical guards

The new result is a conditional, sharp for THIS parameter pair and THIS nuisance class, exact risk floor for M13 five-shell N41 B source coefficient family, NOT universal closed-form risk for every alpha,beta,kappa: globally one can evaluate the convex 1D hinge-square objective and enumerate its finite active-set transitions, but ROT016 only source-certified this fixed nonzero-risk pair. No physical realization of 25 arbitrary coefficient perturbations or 5 relative gains established. Historic missing dtc0a_runtime_v0_3_1.py byte-exact producer remains HOLD; no external observation, physical instrument, tensor dynamics, J3/K/TPE inference, cosmological or novelty claims.

New two-active theorem is author same-cell and remains **REC11/AUD2/M15 external-to-cell ROT016 referee PENDING**. Global ROT007/013 17+5 at epsilon 1e-7 independently accepted by AUD2 ROT005 and M15 ROT006 I1; source owner M15 actual BW adoption decision NOT VERIFIED, KN13 BW source ingestion NOT VERIFIED. Posted GitHub != BW ingest or canonical approval. No role collapse or automated task cascade.

FINAL:
AUD2_ROT005_AND_M15_ROT006_INDEPENDENT_17_PLUS_5_GLOBAL_SOURCE_PASS_I1 /
REC11_ROT029_INDEPENDENT_NEGATIVE_EPS1E7_PASS /
ROT016_EXACT_FRACTION_TWO_ACTIVE_SHELL_GLOBAL_POSITIVE_RISK_FLOOR_AUTHOR_PASS /
ALL_25_COEFF_EPS1E7_BOX_SOURCE_SIGNS_PASS /
CLEAN_REPLAY_AND_MUTATION_FAILCLOSED_PASS /
ROT016_REFEREE_PENDING / OWNER_GLOBAL_ADOPTION_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
