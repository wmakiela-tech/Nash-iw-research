---
artifact_id: IW_DAX_S9_ROT023_BELLE_SOURCE_CORRECTION_COVARIANCE_NONIDENTIFIABILITY_PSD_EXTREMA_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_REPORT_ONLY_PENDING_BW_INGEST
result_class: ORIGINAL_BELLE_AUTHOR_POINT_CORRECTION_SOURCE / PSD_COVARIANCE_DIAGONAL_IDENTIFIABILITY_FALSIFIER
claim_ceiling: NO_NATIVE_EXPERIMENT_COVARIANCE / NO_P_VALUE / NO_PHYSICAL_AMPLITUDE_FIT / NO_NEUTRINOS_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT023 — Why Belle pointwise error marginals cannot identify angular dual-witness uncertainty

**22 Nov 2026**, source-audited bounded mathematics. Prior ROT021 established a *central-value* paired charged-v-neutral quartic-annihilating angular dual witness; ROT022 established its fragility under hypothetical independent pointwise error **boxes**. ROT023 does NOT add yet another uncertainty box. It derives an exact positive-semidefinite *covariance identifiability obstruction* from the genuine native Belle error margin values and source-author correction provenance.

## Direct primary author document and source receipts

**Primary Belle charged**: T. Mori et al, *High Statistics Measurement of the Cross Sections of gamma gamma -> pi+ pi− Production*, JPSJ **76** 074102 (2007), DOI https://doi.org/10.1143/JPSJ.76.074102, original author arXiv **0704.3538**, https://arxiv.org/abs/0704.3538 , original full paper TEXT actually reread this rotation, Secs 4–6.1, Eq2–4 and Table I. Publisher/full author PDF text https://hanyang.scholarworks.kr/api/assets/b219502c-147a-4ee3-91e5-6fc988cbc109/download . Original author assumes pi/mu misidentification probabilities are W-INDEPENDENT for the Eq2 correction estimate; P(pi pi -> mu mu) differs across angular cells, .08–.13. Point-by-point systematic error is estimated by **one half the neighboring-bin correction difference**. Mu/pi discrimination and trigger correction functions are smoothed, and the authors already discussed possible angular measurement bias at large |cos(theta)| below 1.1GeV, without proving cause. A marginal error obtained from neighboring correction variation is NOT a known independent random detector error or experimental covariance. Original author PDF full text was read, but both web PDF screenshot attempts returned CACHE MISS; no direct PDF-visual/native-byte identity claimed. Search candidate arxiv 0704.2672 was confirmed UNRELATED and not used; original right source is 0704.3538.

**Primary Belle neutral**: S. Uehara et al PRD **79** 052009 (2009), DOI10.1103/PhysRevD.79.052009 and original HEPData https://www.hepdata.net/record/ins815978 metadata; native primary export gave HTTP403 and not acquired, and energy-unfolding correlated errors cannot be reconstructed.

**Actual original source-numeric bytes read and independently SHA256 matched** from official PACKAGED SECONDARY Rivet YODA compressed sources:
- BELLE_2007_I749358.yoda.gz = `28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403` (charged published labels stat,sys_1,sys_2).
- BELLE_2009_I815978.yoda.gz = `65ed96b71a3e03e5528c406c336aa07277bff3fd9cf1c6b9596a708f14c573dd` (neutral labels stat,sys).
The original official whole-Rivet RPM neutral byte acquisition was externally SHA checked and GitHub Actions sourced in prior ROT018 run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45025075860. Source label mapping from `sys_1` to point errors and `sys_2` to overall errors is a declared working interpretation of the primary paper, NOT access to an original experiment covariance matrix.

## Unchanged data object and exact gradient

Native original common W=[.84,.94]GeV, 20 charged 5MeV cells ×12 angular .05 bins, 5 neutral 20MeV cells ×12, original positive R68 H(W) using Egamma=1436554MeV,T=0.07818527068831995MeV, neutral approximate beta(charged)/beta(neutral) correction. Re-reparsed original two YODA sources and independently checked 60 original source-cell values against ROT018 frozen CSV to relative 4e−13. Existing original ROT021 dual `lambda_j,mu` reused unchanged, exact angular-bin quartic moment nullspace `G^T(lambda−mu1)=0` confirmed. Source central normalized L_charged=**0.04688212712744676**, L_neutral=**0.00019011124179592**, paired D=**0.04669201588565083 =4.6692016pp**. Dual chosen ON CHARGED DATA; not blinded preregistered hypothesis test.

For original individual native y_(W,j), positive source weights w_W∆z, and within a channel total T and normalized dual L:
`d L / d y_(W,j)= w_(W,j) [(lambda_j−mu)/2−L]/T`.
Neutral term enters D with negative sign. This derivative also proves EXACT cancellation for truly common per-channel multiplicative normalization: sum g_i y_i=0. Direct native-cell finite-difference check, no SciPy in independent verifier, PASS.

## MATHEMATICAL conditional covariance guard, NOT an experiment variance

As a purely CONDITIONAL FIRST-ORDER DIAGNOSTIC symmetrize originally reported *asymmetric* point margins to `s_i=(abs(down_i)+up_i)/2`. **These are not asserted to be Gaussian experimental standard deviations.** Suppose *hypothetically* s_i are fixed marginal standard deviations and only covariance positive-semidefiniteness is known. With g_i=gradient of D and lengths l_i=abs(g_i)*s_i, every matching PSD covariance produces linearized SD(D) somewhere in **sharp** interval

`[max(0,2 max_i(l_i)−sum_i(l_i)), sum_i(l_i)]`.

Proof standard Gram vectors + triangle/polygon inequality. Upper realized by rank-ONE covariance `C_ij=s_i s_j sign(g_i)sign(g_j)`, lower when polygon closes realized by rank≤TWO covariance with the SAME identical diagonal s_i². No prior art novelty claimed. These PSD completions are MATHEMATICAL, not assumed physically realistic Belle correlations.

Numeric actually executed:

| Conditional original-margin inputs | hypothetically diagonal SD(D) | hypothetically W-coherent / angular-independent SD(D) | mathematically max SD(D), arbitrary 300×300 PSD | max SD(D), channels independent but within each arbitrary PSD |
|--|--:|--:|--:|--:|
| stat charged + stat neutral | .00330336596 | .00945254952 | .04235242228 | .02995010980 |
| charged hypot(stat,sys_1) + neutral stat | **.00392343546** | **.01316171145** | **.05432402045** | **.03941835434** |
| charged sys_1 ONLY | .00211686542 | .00909221597 | .02507464958 | .02507464958 |
| charged hypot(stat,sys_1) + neutral hypot(stat,sys) treated as point-level source (UNPHYSICAL) | .00935990966 | .02306088385 | .09910071033 | .07369550158 |

All dimensionless SD of fractional witness D: multiply by 100 for **percentage points**. The extreme PSD minimum was actually **ZERO** in all four original-margin source vectors; rank-2 explicit polygon with <=1.3e−18 residual, same verified individual diagonal variances; independent rank-1 maximum attained to <1e−14 relative. For main charged combined point+stat vs neutral stat scenario, these **hypothetical** SD values span 0 to **5.43240 percentage points**, while source central D is 4.66920pp. There is NO unique Belle p-value or experimental confidence interpretation.

Additional narrower **SOURCE-INSPIRED BUT STILL UNVERIFIED** illustration: assume native stat diagnostic independent in each W×angle cell, *charged sys_1 perfectly W-correlated within each of 12 angular columns*, independent among those 12 angular correction columns, independent channels, and neutral stat diagonal: SD(D)=**0.00967370756 (0.96737pp)**. If ALL charged angular correction columns share one adversarial correlated sign, under same independent stat baseline SD(D)=**0.02529130835 (2.52913pp)**. These are chosen covariance models, not author-supplied nuisance parameters. The author's W-INDEPENDENT mu/pi correction assumption motivates considering W-coherence but **does not determine cross-angular covariance**.

Independent original checker:
- Fresh re-derivation of native derivative via numerical finite difference.
- Full source SHA and original ROT018 60-cell checks.
- Constructive *planar polygon* (not simply quoting bounds): rank≤2 PSD completion with same s_i marginal diagonal and zero witness sensitivity at 300 real source bins; independent direct rank-1 upper completion.
- Delta-normalization cancellation and original quartic-dual annihilator verified.
- Two clean independent-directory replays regenerate JSON plus **two CSV byte for byte** (2×3/3 PASS); ZIP CRC and all payload SHA PASS.

Local **complete original source+code+data+scientific report** in originating user conversation: `DAX9_ROT023_Belle_Source_Covariance_PSD_Identifiability_Repro.zip`, **SHA256 68bb7f4db55a390b0adf40c19051a3c0f877e20d7a7844af930846bd9689bd95**, 16 files, 15/15 payload SHA256 PASS, ZIP CRC PASS; GitHub source report TEXT ONLY, no claim full ZIP was hosted in repo. Source manuscript contains explicit mathematical scope and independent source receipt.

**RETURN / STOP:** `PRIMARY_BELLE_AUTHOR_CORRECTION_SOURCE_PASS / OFFICIAL_SECONDARY_BOTH_YODA_SHA_PASS / EXACT_PSD_DIAGONAL_NONIDENTIFIABILITY_PASS / INDEPENDENT_RANK1_MAX_RANK2_ZERO_PSD_WITNESSES_PASS / FULL_CORRELATED_EXPERIMENTAL_LIKELIHOOD_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`. The missing gate is **actual corrected detector response or original angular systematic covariance** or preregistered truly independent channel test, NOT arbitrary uncertainty-band or resonance-phase proliferation. No BW write, I3 signature, physical neutrino/PBH/BBN or discovery claim.
