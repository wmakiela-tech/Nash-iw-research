---
artifact_id: IW_REC13_ROT018_WUXU_TWO_AUTHOR_ORIGINAL_JLD2_TWOSIDED_CHI2_LOW_BETA_REJECTION_TWO_CROSSING_V3_NONPHYSICAL_REBASE_FALSIFIER_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
mode: SCIENCE_FIRST / AUTHOR_PRIMARY_TWO_ORIGINAL_10000_CELL_JLD2_BINARY_I1 / INDEPENDENT_WOLFRAM_V15_SHA256_HDF5_SOURCE_REPLAY / TWO_SIDED_CHISQUARE_UPPER_LOWER_BRANCH / NO_PBH_PHYSICS_SOLVER / NEGATIVE_KNOWLEDGE
prior_owner_firstness: WuXu_2025_2026_original_research / EKS1_ROT018_FIRST_CARR_WINDOW_v1_CODE_PROVENANCE / REC13_ROT016_THREE_WAY_Yp_FORMULA / REC13_ROT017_FIRST_FULL_NATIVE_JLD2_AND_BASELINE_NONIDENTIFICATION
original_distinct_rec13_rot018: NATIVE_TWO_SIDED_CHI2_LOWER_BRANCH_COUNTERFACTOR_SOURCE_I1 / ALL_100_LOW_BETA_HYPOTHETICAL_CONFLICT / TWO_BOUNDED_INTERVALS_VS_UCI / DUAL_VINTAGE_49_73_CONTROLS
status: ORIGINAL_BINARY_SHA256_2_OF_2_PASS / HDF5_2X100X100_Y_CHI2_PASS / SOURCE_OLD_78_78_ROOT_REPRODUCED / POSTPROCESS_ONLY_LOW_BETA_REJECTION_100_OF_100_BOTH_SNAPSHOTS / NO_PUBLISHED_FIG5_SOURCE_EXECUTION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3
custody: GITHUB_PENDING_BW_INGEST
---

# REC13 ROT018 — independent source-native two-sided helium χ² falsifier: the naive Wu–Xu v3 postprocessor cannot define a one-sided upper PBH abundance bound on either archived original scan

## 0. Science and firstness: latest EKS1 resolution acknowledged, distinct REC13 test

This rotation continues REC13 ROT016–ROT017, which established directly from the authors' public arXiv text that the same **neutron fraction** `X_n=n_n/(n_n+n_p)` has THREE different helium postprocessors: paper v1/v2 Eq. (5.1) `2X/(1-2X)`, original author public Julia `main-scan.jl` `2X/(1-X)`, paper v3 Eq. (5.1) `2X`. REC13 ROT017 was the first in this local referee sequence to independently access the original *actual* author binary 100×100 `scanning.jld2`, validate its SHA256 and two 100×100 stored datasets, and examine a direct counterfactual `F(Y)=2Y/(2+Y)` that moves the **UPPER** contour j62 by +0.83369 dex **without** any SBBN baseline reanchor. That old counterfactual was explicitly marked physically invalid because the SBBN reference would move from .245 to .21826.

EKS1 ROT018 has since independently and **FIRST** discovered an important temporal figure-provenance source link: author `main.ipynb`, cell14 reportedly plots its solid contour from CURRENT `data/out/scanning.jld2`, and previous v1 `data/out/scanning_old.jld2` as a dashed companion; the authors' Carr2020 exception [3.2,7.4]×10^9g is reproduced with **v1 mesons-only CODE** scan as 30 CONTIGUOUS mass rows [3.301,7.526]×10^9g, but not with the newer scan (0/65). EKS1 report firstness at private `wmakiela-tech/Nash-Priv@ddc8ad22c559095dfcf92adf79bf208eb15be38c`, `research/eks1/2026-11-22/IW_EKS1_ROT018_GAP006_G0_EXPLAINED_CARR_WINDOW_REPRODUCED_ONLY_BY_V1_MESON_ARCHIVE_AND_DIR009_AFTER_REVIEW100_001_20261122.md`. REC13 HAS READ THIS ORIGINAL EKS1 SOURCE, and does NOT claim discovery of the Carr window, nor independent author notebook cell14 read. Author notebook content is still not directly available to REC13 as full text through connector (Git blob `171c4a29...` produced empty text); EKS1's direct read is separately attributed. The new **within-project firstness of REC13 ROT018 is different**: one-sided upper v3 crossing is not a two-sided Yp χ² upper-limit operation, due to a mathematically necessary LOWER excluded branch, independent of which archive generated the published image.

Since 22 November 17:40 CET, EKS1 ROT019 had already disposed B1 cards and moved to Front A line, so this audit is source-protective and creates NO new unwarranted work for EKS1/Badacz. KN15 passed lineage to KN16 and BW Sheets 403 had recently been documented; Github write + Slack transport never implies BW acknowledgment.

## 1. Exactly two original author binary archives, not a reconstructed surrogate

Independent author repository `Fenyutanchan/Primordial-Black-Hole`, pinned at `d395183674cace6c9906a8911bdeb7234ba4040d`. Original primary files (not derived EKS1 JSON):
1. LATER: `arXiv-2509.05618/data/out/scanning.jld2`, Git blob `10cc9b3f078fcadb91b5e520e75845859ca00b74`, 151089B, binary SHA256 `51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786` exactly validated from the bytes, same checksum EKS1 originally reported;
2. V1: `arXiv-2509.05618/arXiv-2509.05618v1/data/out/scanning.jld2`, Git blob `ff08072449c4ef46144cb800778224acd9669a8f`, 149272B, SHA256 `7f8ebe6c6c7b380f20c725908d900c5508bb4f16519a7f17e10955a55e78ecf1` independently computed.

Both binary files fully decoded from original GitHub source base64, temporarily recreated with Wolfram binary write, and HDF5 `/Y_P_mat`, `/chi2_mat`, `/m_PBH_list [gram]`, `/β_PBH_list` directly imported with an independent Wolfram v15 mathematical runtime. Dataset arrays transposed to [mass,beta] after explicit axis check. Both have 100 masses 6×10^8–10^10g and 100 `log10β=-20..-17` nodes (same actual axes). Maximum numeric residual reconstructing ORIGINAL per-source `χ² = ((Y_P−.245)/.003)²` over 10,000 cells: later `4.3655745685100555e−11`; v1 `1.8189894035458565e−12`. PASS. Source original root count 78 for each, j22/j62 exact source EKS1 replay:
- later j22 −17.220222662721067, j62 −19.389217861290064;
- v1 j22 −17.172054587347045, j62 −18.27393300972919.

Original author `arXiv-2509.05618/main-scan.jl` (Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`), line210 computes `2X/(1−X)`, lines 243–249 writes `Y_P_mat` and `chi2_mat=((Y_P_mat−.245)/.003)^2`. Original v1 archive code `arXiv-2509.05618/arXiv-2509.05618v1/main-scan.jl` blob `1855db41e67dddbcc4380daf904829833c082d19`, same helium formula. The exact physical production execution provenance of the two files is still CONDITIONAL rather than proven merely from current repo code.

Author published Wu–Xu v3 `https://arxiv.org/html/2509.05618v3`, Sec 5 states PDG `Yp=.245±.003` and the **upper one-sided region** above the reported Fig5 line has `Yp>.251`. v3 also claims separate BBN-simple nuclear-network check, NOT independently run here. Importantly, paper is allowed to use a one-sided scientific inference; merely writing chi² in an archive does NOT prove it actually used the two-sided lower tail to publish the upper curve. Preserve this distinction.

## 2. A precise logical defect in the HYPOTHETICAL unanchored v3 reinterpretation

If and ONLY IF the original archived source records `Y_code=2X/(1−X)`, then the currently published Eq5.1 `Y_v3=2X` corresponds to
[
F(Y_{code})=2 Y_{code}/(2+Y_{code}).
]
Rec13 ROT017 took the upper root `F(Y_code)=.251`, at source code `Y_code=.28702115494568325`, and correctly marked a large but uncalibrated shift in `log10β`.

The author's literal **SOURCE chi² field**, however, implements a symmetric residual; if one applies the same source-typed two-sided statistic to this new F(Y), acceptance under χ²≤4 requires `Y_v3∈[.239,.251]`. As β approaches zero at fixed m, a physically interpretable one-sided UPPER parameter confidence interval `[0,β_max]` normally requires the zero-effect/standard baseline to remain admissible. Contrariwise, **if the lower-β region is REJECTED**, one upper intersection by itself describes only ONE END of a potentially TWO-SIDED ALLOWED ISLAND. That is a pure logic test on the SAME grid, independent of posterior/model novelty, demanding a lower-root check that REC13 ROT017 and EKS1's 4 scenario G0 source script did not perform.

Exact actually computed source-native statistics, both archives:

| Original archived source | Original Y as stored: smallest-β source mass rows inside .239..251 | Hypothetical unanchored v3: smallest-β mass rows inside .239..251 | v3 low-β χ² range | v3 mass rows with BOTH lower and upper Y crossings |
|---|---:|---:|---:|---:|
| later 151089B | 100/100 | **0/100** | **73.0445–81.2356** | **73/100** |
| v1 149272B | 100/100 | **0/100** | **79.0402–81.2481** | **49/100** |

The **original** later archive contains 4,469 of 10,000 source grid cells with χ²≤4; v1 original 7,244/10,000. After naïve F(Y) transformation with unchanged empirical .245±.003, only **513/10,000** later and **387/10,000** v1 cells remain in the 2σ symmetric acceptance band. Of these, later 6,131 source transformed cells lie BELOW .239, 3,356 ABOVE .251; v1 8,760 BELOW, 853 ABOVE. At smallest β, all 100 masses in BOTH archives are below .239, not just outlying numbers.

Mass-by-mass lower/upper source counterfactual roots (interpolated Y versus log10β between **adjacent sampled nodes**, NOT interval-certified continuum):

| Archive and mass | lower (Y_{v3}=.239) logβ | upper (Y_{v3}=.251) logβ | smallest-β χ² |
|---|---:|---:|---:|
| later j22 1.121×10^9g | no source crossing | no source crossing | 80.5609168 |
| later j27 1.292×10^9g | −17.4671638433 | −17.0646264779 | ~80.4957 |
| later j62 3.494×10^9g | **−18.7554350688** | **−18.5555281420** | **73.6120331** |
| v1 j62 same mass | **−17.6390037839** | **−17.4391316593** | **80.1453796** |

The later archive has **74** masses with a lower crossing and **73** with an upper crossing; 73 have both (the 74th remains admissible up to the endpoint of the scanned β domain). V1 has 58 lower and 49 upper, with 49 both. The prior REC13 ROT017 “73 roots” counts ONLY UPPER intersections; the literal transformed two-sided χ² yields 73 **bounded allowed islands** and NOT 73 conventional one-sided upper bounds. This is a genuine and easily falsifiable additional source-level result, not a new cosmological physical bound.

At later j62 the true set of 2σ accepted beta values under this **only hypothetical transformed + unchanged observation** model is approximately
[
10^{-18.7554351} lesssim β lesssim 10^{-18.5555281},
]
not `0<β≤10^-18.5555281`. Both smaller and larger sampled β values are rejected under that exact **two-sided** test. Under a deliberately *one-sided* alternative `Y_v3≤.251`, one would retain small β by definition, but then the transformed low-beta helium observable `.21926` disagrees with the quoted observational central value .245; **its physical model calibration has not been established**. This difference between a one-sided decision convention and the symmetric archived `χ²` must remain explicit, not merged.

## 3. Why the baseline problem cannot be cured by just one algebraic β shift

Archived code Y baseline near .245 maps to `F(.245)=.21826280623608016`, a deficit of .026737 and ~8.912 times the quoted measurement σ .003. This number is a SOURCE-NORMALIZATION comparison to paper observation (no calibrated statistical (p), no covariance, no physical significance statement). REC13 ROT017 showed different *arbitrary* baseline anchors give j62 shifts +.0960 or +.1651 dex rather than +.8337 dex; these are mathematically explicit but NOT validated physical alternatives. ROT018 strengthens the argument: under the actual two-sided archived χ² definition, the unanchored alternative **inverts the topology of the admissible β set**. Any claim “the publication should be corrected by +.8337 dex” is unsupported even as a logically typed two-sided exclusion, before considering paper and code provenance.

For physically meaningful correction, minimum original-source gate:
1. Verify whether final v3 Fig5 solid line really is the later archive `Y_P_mat`, or separate adjusted or nuclear BBN-simple computation. EKS1 ROT018 has direct notebook cell14 evidence for **repository's** plot: later solid, v1 older dashed. This source cannot be substituted for a byte-identical proof that printed v3 figure is the same producer. REC13 cannot independently read notebook full cell text in this tool.
2. Establish the model's standard BBN helium baseline in the same `X_n` definition as v3 Eq5.1, with its nuclear network or valid observational nuisance prescription, rather than arbitrary renormalization.
3. Only then recompute a one-sided or two-sided likelihood on the appropriately matched physical observable and estimate beta contours. A new ODE solver is unnecessary if robust producer trace reveals an already-corrected archived figure; otherwise owner should decide. Do not automatically alter interpretation of Kohri/Keith/Carr direct curves.
4. No external paper-error allegation, no claim of refuting authors, no external priority assertion.

## 4. Reproducer, live execution, custody, firstness

A standalone source audit Wolfram Language code `research/rec13/2026-11-22/code/rec13_rot018_wuxu_original_dual_archive_twosided_chi2_yp_source_guard.wl` was newly authored, original-source SHA256 gated for BOTH exact author files. After publishing, the **byte-for-byte published code body was retrieved from GitHub and actually re-executed** by Wolfram Language v15 on the two directly fetched original author JLD2 binary bytes, with HDF5 decode, all 20,000 original Y cells and 20,000 χ² cells, both archive SHA gates, chi² residual gates, correct beta axis, low-β classification and lower+upper crossing algorithms. The full direct kernel readback returned `SOURCE_SHA256_CHI2_I1_PASS_TWO_SIDED_CONTRACT_ONLY` for both snapshots and every count and j62 numeric interval above. This is a real independent original source binary reexecution, NOT paraphrasing EKS1's summary.

Machine source `research/rec13/2026-11-22/data/rec13_rot018_wuxu_author_v1_current_two_sided_Yp_chi2_lower_upper_branch_source_001.json` retains archive original exact SHA, source-cell counts, low-β χ² ranges, j22/j27/j62 numeric crossing brackets, and negative scope constraints.

EKS1 ROT018's archived v1 Carr source match remains **its scientific firstness**. REC13 ROT017 initial one-sided conditional postprocessor firstness remains REC13's. NEW to REC13 ROT018 is the explicit *two-sided* original χ² source logic proof that a raw helium formula change makes the small-β null region inadmissible on ALL original source masses of BOTH archives; the physical correction `β` is therefore **not identifiable as a corrected upper limit** from these binary arrays. This adds science negative knowledge, not a paper-level new physical theory.

The most precise status:
`REC13_ROT018_AUTHOR_ORIGINAL_BINARY_TWO_OF_TWO_SHA_PASS / TWO_X_10000_CELL_CHI2_I1_PASS / UNANCHORED_F_LOW_BETA_100_OF_100_REJECTED_BOTH_ARCHIVES / CURRENT_F_73_TWO_SIDED_ISLANDS_V1_F_49_TWO_SIDED_ISLANDS / TWO_SIDED_LOWER_BRANCH_ESSENTIAL / PUBLICATION_ONE_SIDED_PHYSICAL_CONTOUR_PROVENANCE_AND_CALIBRATION_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3`.
