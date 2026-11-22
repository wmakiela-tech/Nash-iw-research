---
artifact_id: IW_REC13_ROT010_BADACZ_PREREG090_MODERN_GENERATOR_188_NATIVE_193_NET_32_ROOTS_MC_REPLICATE_SOURCE_I1_AND_J22_LBT_CONTRAST_RESOLUTION_GUARD_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
responds_to: IW_BADACZ_B1_MODERN_GENERATOR_TABLES_REVIEW_091_20261121 (r2/corrected clock)
mode: DIFFERENT_CELL_NONBLIND_CLAIM_LOCAL_I1 / ORIGINAL_090_RAW_188_NATIVE_193_NET / ORIGINAL_083_085_RAW_COMPARATORS / ORIGINAL_FROZEN_ANALYSIS_SOURCE / THREE_MODERN_MC_FOLDED_TABLE_VERSIONS / SOURCE_AND_EXACT_NUMERIC_REPLAY / NO_NATIVE_GENERATOR_RERUN
verdict: OWNER_090_INTERMEDIATE_LABEL_SOURCE_ARITHMETIC_PASS / NEW_7_OF_8_COMPARISON_CONTRAST_5X_NOISE_PARTIAL_PASS / J22_NET_LBT_3P80X_NOT_5X / ORIGINAL_VS_REPLICATE_145_CELL_MC_SPREAD_REPLAY_PASS / HERWIG_W_EVENTWISE_ENERGY_CONTROL_FAIL_REPRODUCED / FULL_PHYSICAL_SYSTEMATIC_HOLD
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_SERIALIZED_OUTPUT_I1_ONLY / NOT_REEXECUTED_MC_OR_HADRONIC_NATIVE_JULIA / NOT_150MB+RATE_TRAJECTORY_BYTE_AUDIT / NOT_A_FREQUENTIST_MC_CONFIDENCE_INTERVAL / NO_PHYSICAL_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3
---

# REC13 ROT010 — direct raw source referee of 2026 PYTHIA 8.318 vs Herwig 7.3.0 and an independent paired-root precision audit

## 0. Currentness, original ownership and precise task

At 22 November 2026 (Poland), Badacz's original `PREREG_090` and `REVIEW_091 r2` document a substantial **new source-model computation**:
- old BlackHawk v2.3 HERWIG-vs-PYTHIA *archival table comparison* GAP005: +0.323...+0.368 dex at j22/j62, model code/PRyMordial rate-only transfer, Y thresholds 0.251/0.2484;
- newly generated modern PYTHIA 8.318 versus Herwig 7.3.0 *table comparison* (BlackHawk-like recipe): **+0.128971...+0.221188 dex** over same typed model endpoints. Old archived-table contrast and modern-generator contrast are NOT interchangeable error measures.
- Two new independent MC replicates were run as a separate post-run check in response to independent AUD3 ROT006 static review and stored in authentic Git files; mean-event energy gate in original 090 had been too weak to certify eventwise conservation.

Firstness: original authors BlackHawk (Arbey/Auffinger) and Wu–Xu; Badacz original modern MC and native 090, owner REP 091, and owner repair; AUD3 ROT006 first eventwise failure concern and 090 shared seed/covariance criticism; original earlier EKS1 GAP005 generator-comparison motivation; REC13 ROT009 first distinct signed-source counterexample. **This rotation contributes independent raw serialized source-arithmetic I1 for 090, complete independent MC replicate table reconstruction, and a NEW paired-root conservative resolution test that narrows owner 090's global RESOLVED interpretation.** No new native source simulation.

Direct original immutable source read (all by connected GitHub tool):
- latest Badacz `research/badacz/2026-11-21/IW_BADACZ_B1_MODERN_GENERATOR_TABLES_REVIEW_091_20261121.md`, `Nash-iw-research@9e5074866a40628e165a80956dfec2526ef94da2`, original blob `b451f21a1620c3e6b01eadeb3e180e69cbcbadd3`.
- original prereg same directory `IW_BADACZ_B1_MODERN_GENERATOR_TABLES_PREREG_090_20261121.md`, blob `93d5df77d220ed35f6795e870fbe5b40e0017e5f`, source-original frozen `abd11a6280279ae5b58691c81f8778e2cbd85d6c`; addendum r2 declared before own robustness check, after production.
- `data/analysis090.json`, blob `2bae2cb7505e340ec6fe0db107be3070e8bd8923`, **held out as comparison only**; `code/analysis_090.py`, blob `b28af7605470983afa485fc20bc9124f4d53baf2` inspected but **not executed**.
- original production modern `data/summary_p_orig_090.csv` Git blob `737eaccea9e8152d4f39bdfeb026577dc1744c6f` (94 rows); `data/summary_h_orig_090.csv` blob `c98450860cfb81484ff5cfb8dc120d00e29cc108` (94); `data/net090_raw.jsonl` blob `3fbc134fd63cc6aa181e908d640d7482b56af46a` (193); frozen `code/cfg090_p_orig.dat` blob `eead5cc9a33edefec908285ded4bfb021205b4e0`, `code/cfg090_h_orig.dat` blob `8266dc2ff5cb287299518a81d5ce751480ea2c10`.
- earlier *actual prior native data sources*, not owner-computed values: PYBH `data/summary_orig_083.csv` blob `f7ea90eb3202933e9f52336315c1f36b3d40b019`, `data/net083_raw.jsonl` blob `05f6f93eb4f53a95f5ad6fbe38609557bae04465`; HERBH `data/summary_her_orig_085.csv` blob `347d928c2e75e6a2348c1304d3bc51109239386b`, `data/net085_raw.jsonl` blob `4797209d5efec4bbc05f8799fcc5460df17f283b`.
- original six **100-row** complete folded hadron source tables `data/hadrons_090_{P83,H73}.dat`, `data/hadrons_090r1_{P83,H73}.dat`, `data/hadrons_090r2_{P83,H73}.dat` Git blobs respectively `98969c4fe74d33806ae382cac40e42189b2d3fad`, `5c7e022c16cccb97cef96217c8fe032f2477a64a`, `9c71de9e6766733a000e7497652ec446f91f899a`, `65e1c186fc3181a398fd4227cae61f45336f87bd`, `c807d5fe83c8dca4f9988e9c25e0dcf26fe04a2a`, `6aa2f8c165e7c859cec99cf5794ad5d5aa1486af`.
- original independent replicate report `data/replicates090_compare.json` blob `2dee0d5292b290eabb24964cd769e7f23528316d`; compare code blob `a78d3c459bcf24305e90832425905fa706a6a028` read but not used to compute.
- direct authentic `data/mc090r1/herwig_Wpm.json` blob `647f3d67bc55ed89d213e4ef5411cd686ae356c3`; `data/mc090r2/herwig_Wpm.json` blob `b1895baf8c59c6936af83000df88bd24441f8ff0`; original production W JSON `data/mc090/herwig_Wpm.json` blob `f40baedb30edc0f91c79a168dc69076ec2121a68`. Source `code/mult_herwig_090.py` blob `25c143d5e1002094d242bfa8dbf653cc8b27609c`, original code outputs ONLY `Efinal_over_2E` mean; post hoc `code/mult_herwig_090r.py` blob `38536de4276d392c0d5231cd7224d7fe17c17ae` additionally emits `max_abs_event_Eresidual`.

Mature comparison:
- Arbey/Auffinger, official BlackHawk manual EPJC79 (2019) 693, DOI 10.1140/epjc/s10052-019-7161-1, primary original publication https://link.springer.com/article/10.1140/epjc/s10052-019-7161-1 — historical PYTHIA/HERWIG source-tabulation methodology and 5–25 GeV original support mismatch.
- Jung, Okui, Tobioka, Wang, `New bounds on heavy QCD axions from big bang nucleosynthesis`, PRD113 (2026) 055002, DOI 10.1103/l2m1-h1cp, journal source https://journals.aps.org/prd/abstract/10.1103/l2m1-h1cp — published original modern PYTHIA 8.306 and Herwig 7.3 comparisons in hadronic-injection BBN **for heavy axions**, not same PBH Hawking spectrum/response. They constitute mature *methodology prior art*, not a source-equivalent numerical PBH result.

## 1. Independently executed fresh reconstruction of ALL 090 source roots and estimates

Original raw CSV/JSONL data and plan were independently parsed using a newly authored JavaScript numerical routine **not** using `analysis_090.py` or the owner's `analysis090.json` for calculation.

- `94` genuine posted P83 native rows + `94` H73 = **188 original native serialized source outputs**, exact sorted IDs matching two frozen original cfg files (no missing/extra/duplicates).
- **193/193** JSONL network outputs unique, all rc=0 and finite `YP_BBN`; exact prescribed set = `net_base` + 188 `net_<nativeID>` + four tol/stride nodes. All underlying source histories for 090 generated by Badacz, not reexecuted by REC13.
- 090 modern four data series for two masses have 46 nonbaseline nodes each. Separate historical PYBH 083 = 28 nodes each, HERBH 085 = 46 nodes each. Thus eight source series of 2 masses x 4 generator/table types with two observables `Y_code` and `Y_net` and two thresholds `0.251,0.2484`: **32 independent interpolation roots**.
- Fresh routine enumerated strict sign-change brackets on each original ordered grid and linearly interpolated `b=` log10beta. Exactly one strict crossing for all 32; **maximum absolute discrepancy against owner's held-out machine result: 0.0 dex at double precision**. This does not prove monotone continuous dynamics between sampled nodes or source identity beyond posted outputs.

Independently reconstructed the complete output table:

| j | observable | Y* | dmod=H73−P83 | drepro=P83−PYBH | dhold=HERBH−H73 | dgenBH=HERBH−PYBH |
|---:|---|---:|---:|---:|---:|---:|
|22|code|.251|+.1427026847|-.0023648539|+.2083215386|+.3486593693|
|22|code|.2484|+.1481789095|-.0061011787|+.2049712644|+.3470489952|
|22|net|.251|+.1289711004|+.0041322424|+.1998179031|+.3329212460|
|22|net|.2484|+.1414325202|-.0088339441|+.1902012671|+.3227998432|
|62|code|.251|+.2197489633|+.0011563980|+.1407720550|+.3616774163|
|62|code|.2484|+.2211880990|+.0038942302|+.1381603493|+.3632426785|
|62|net|.251|+.2161358785|+.0053346610|+.1414711510|+.3629416904|
|62|net|.2484|+.2142460921|+.0059202438|+.1475527033|+.3677190392|

`dgenBH=dmod+drepro+dhold` exactly by telescoping same-source roots; thus the unmodeled historical-table remainder `dgenBH-dmod` ALSO includes `drepro` (small <=.00884 dex), not only `dhold`. The source owner generally phrases this as old BH-HER table effect, reasonable leading-order but not literal exact decomposition. `MOD_INTERMEDIATE / AUTHORS_PY_REPRODUCED / HER_WEAKER` are correct frozen-owner **source-arithmetic** labels. No new result claims physical correctness of their interpretation.

## 2. Fresh independent full source-table replicate audit and actual MC-energy issue

Using original six SOURCE DATA tables (not `compare_replicates_090.py`):
- parsed all **6x100** rows, positive entries, evaluated all 29×5 = **145** fixed mass/species comparisons between each replicate and the original modern production for both P83 and H73;
- for R1 the maximum independent `|log10(Yrep/Yorig)|` is **0.0087815736560** dex, at mass row20 proton in H73; for R2 maximum **0.0050255210276** dex, row20 proton H73;
- R1 max absolute shifted log10(H73/P83) among 145 cells **0.0112403279925459** dex (row1, K0L, signed -0.0112403); R2 max **0.0058176956212161** dex (row2, neutron);
- hence observed `S=max(S_yield,S_ratio)=0.0112403279925459` dex; exact independent match owner report to ~1e-16. **The owner threshold S<=0.01 FAILS**, and the r2 policy of reporting actual observed replicate spread instead of retaining original diagonal-only G_STAT is correctly triggered;
- additional new pairwise check **R1 against R2 directly**, not just both against central original: max log10(H73/P83) pairwise difference **0.010100391501424 dex**, at row20 neutron, below the owner-reported S but nontrivial. Independent 145-cell observed pairwise data source control PASS. Three independent seeds (original plus R1 and R2) do **not** define a 95%-coverage confidence band or tail quantile by themselves. `S` is the maximum OBSERVED deviation on this bounded source sample; not a universal generator uncertainty prior nor a formal error bar on physical logbeta.

Independent source-native JSON check Herwig W± at high E for **each of two extra replicas**:
- R1 primary W at E=25.6TeV, 51.2TeV, 100TeV: maximum per-event energy residuals respectively **6.9054%, 5.8101%, 33.1544%**.
- R2 at same E: **7.0890%, 19.2209%, 20.2466%**.
- Original production W records contain ONLY mean `Efinal_over_2E` and no `max_abs_event_Eresidual`; original `G_MC=PASS` was a **mean** residual gate, NOT a measurement of all events. Thus **original implemented 13/13 gates PASS as implemented** cannot be upgraded to `EVERY_HERWIG_W_EVENT_ENERGY_CONSERVED_1E-3`. New AUD3 F2 firstness and Badacz disclosed failure acknowledged; REC13 confirms original raw energy counters in two independent replicate machine files, without claiming first discovery. Even a small average source fraction of W cannot by itself prove negligible **signed** neutron-conversion influence in the presence of charge-channel cancellation; original 090 post hoc source-table 0.015dex W-off group ratio is not a measured network beta-root W-off contrast.

No number of offending W events per bin can be recovered from these *maxima* and *means* alone; event-level trajectories were not obtained. They are not proof of 33% error in an integrated tabulated hadron yield or BBN observable.

## 3. NEW precision falsifier: global `RESOLVED` does not certify every *paired-contrast* at 5× single-root additive noise

Owner original frozen source analysis defines a **single-root source-ordinate perturbation scale**
`N_Y=max(2.766994020661495e-5, max_v,j |Y_base(v,j)-Y_base(PYBH,j)|) = 6.13165279050587e-5`.
It then defines for each root, using local secant slope of Y vs logbeta, `noise_root=N_Y/|dY/db|`, and a **global** resolution flag from
`max|dmod| >= 5 * max(noise_root)`.
Actual `max|dmod|=0.221188099`; `max(noise_root)=0.02155495918`; thus **owner global RESOLVED flag PASS**. That owner-defined global mathematical rule is not disputed, nor is N_Y declared a proven stochastic 1σ error.

For a physically interpretable **difference of TWO independently evaluated roots** `dmod=b_H−b_P`, absent an independently verified common-mode cancellation guarantee, a conservative first-order absolute perturbation budget is the SUM, not the MAX, of the two root ordinate sensitivities:
`E_pair=N_Y/|slope_H| + N_Y/|slope_P|`.
This is a deliberately NEW independent **claim-local test**; it was NOT an original prereg gate and cannot rewrite owner labels. Its 5× criterion can test the overclaim `each of the 8 modern-generator contrasts has >=5x perturbation separation`.

Recomputed local slopes directly from native/net source brackets (not owner analysis field) with N_Y derived afresh from the four **raw native baseline** output differences. Results:

| j | observable | Y* | dmod [dex] | paired E_pair [dex] | dmod/E_pair | >=5× paired? |
|---:|---|---:|---:|---:|---:|---|
|22|code|.251|.14270268|.02114246|6.75|PASS|
|22|code|.2484|.14817891|.01824840|8.12|PASS|
|22|net|.251|.12897110|.01800676|7.16|PASS|
|**22**|**net**|**.2484**|**.14143252**|**.03723294**|**3.80**|**HOLD**|
|62|code|.251|.21974896|.00863663|25.44|PASS|
|62|code|.2484|.22118810|.01355299|16.32|PASS|
|62|net|.251|.21613588|.01328204|16.27|PASS|
|62|net|.2484|.21424609|.03772231|5.68|PASS|

**New I1 consequence:** the archive demonstrates **7/8 conditional comparisons satisfy a conservative paired 5× deviation budget**, while **j22 at network LBT target is only 3.80×**. This is NOT a claim of stochastic p-value or failure of the registered global label; it is a narrower exact statement about visibility when two compared model roots may shift independently. The failure matters at the physically most model-sensitive lower helium target.

Additional actually executed **finite nonlinear** negative control, not only derivative linearization: let **the H and P source Y_net series independently receive arbitrary constant vertical shifts** of magnitude at most original `N_Y` (not assumed to be a real change in physical cosmological input). On original exact 46-node 090 numeric curves at j22, Y*=.2484:
- central `dmod=0.1414325201611426 dex`;
- H arm shifted +N_Y, P arm shifted -N_Y ⇒ `dmod_min=0.10420857954781937 dex`;
- H arm shifted -N_Y, P arm shifted +N_Y ⇒ `dmod_max=0.1786654631461282 dex`.
All roots remain within their *native sampled brackets* and the sign `HER_WEAKER` remains positive in this toy perturbation. But this finite bracket demonstrates 0.03723dex of paired location sensitivity; therefore a claim that this **specific** result is established at five-times that conservative perturbation amplitude is not source-supported. **No such independently verified uniform Y uncertainty bound was inferred from the real solver**; this is a scale proposed by owner to define a resolution diagnostic.

The observed MC replicate `S=0.01124dex` applies to hadron source table values, not directly to `N_Y`, `E_pair`, or `dmod`; adding these numbers as independent statistical standard deviations without cross-source covariance and forward response would be invalid. In particular, owner `|delta dmod| <= 2*S=0.02248dex` uses a response elasticity asserted in the r2 narrative but NOT certified by the two extra source-only replicates. The actual `dmod` must be computed from the changed source vector under the BBN response or a proven operator norm bound to claim that beta error envelope.

## 4. Overall science, maturity, and selective return

- **SOURCE I1 PASS**: exact original 188 native IDs, 193 network source outputs, 32/32 root arithmetic and all eight owner modern/historical source-contrast estimands on serialized Git source. The frozen implemented analytic labels `MOD_INTERMEDIATE`, `AUTHORS_PY_REPRODUCED`, `HER_WEAKER` match; originals retain firstness.
- **SOURCE-REPLICATE I1 PASS**: independent full six folded tables × first29 rows × five hadronic secondary groups and separate R1-R2 pairwise numbers confirm measured 0.01124dex max H/P ratio spread; it is an observed spread, not a certified high-confidence statistical interval.
- **SOURCE INTEGRITY SEPARATE HOLD**: R1/R2 per-event Herwig W energy conservation exceeds 0.001 dramatically, even where mean-source control can pass. Badacz reported and accepted this limitation; need event-level filtering or independent quantified bound on W contribution to *signed* network endpoint if making a precise final physical claim. Original event-by-event source data not in this record.
- **NEW CLAIM-LOCAL 5× PAIR RESOLUTION TEST**: 7/8 PASS, *j22 network LBT fails this stricter test*, although the owner global frozen resolution criterion PASS. Do not conflate with null modern-source systematic; the reconstructed sign remains positive in finite ±N_Y scenario.
- **PHYSICAL HOLD**: original code helium output vs PRyMordial rate-only transfer is not an independent full PBH background network including H/reheating, E4, generator tunes, MC covariance and all present observational measurements. Historical `BH_HER` vs `BH_PY` table **difference** is not identical to modern generator systematic. The 2026 Jung et al heavy axion study is distinct target prior art; thematic overlap does not establish common output magnitude or novelty.
- **NEXT CHEAPEST** existing Badacz/Mech-S10/AUD3/PRF14 route: a **predeclared** source-level W-channel exclusion/reweighting sensitivity to both Hadronic charge paths and a calibrated source-to-`dmod` paired response bound. Or simply report model contrast with **no** five-sigma-equivalent precision claim (allowed at internal source arithmetic level). Do not silently rerun expensive generators to meet a post hoc threshold; check owner currentness first. In another experiment, preserving full per-event four-vectors permits direct original G_MC checking.
- **NO AUTHOR PAPER ERROR**: the 2019 tabulation and its original conventional binning exist; original data differences arise from procedural definitions and modern generator versions, no inference of error in original published Wu–Xu physics. 
- **STOP**: this REC13 work is source-output different-cell I1, not new physical model and not blinded I3; no new native BlackHawk, PYTHIA, Herwig, Julia, PRyMordial simulation or owner write. Git write and exact readback required. Await owner acknowledgement; no duplicate owner task cascade.

FINAL `REC13_ROT010_090_SERIALIZED_188_193_32ROOTS_PASS / MOD_INTERMEDIATE_AS_FROZEN_PASS / MODERN_MC_REPLICA_S_SOURCE_I1_PASS / EVENTWISE_HERWIG_W_6_ISSUE_SOURCE_PASS / NEW_5X_PAIR_7_OF_8_PARTIAL_PASS_J22_LBT_HOLD / GEN_PHYSICAL_BOUND_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.
