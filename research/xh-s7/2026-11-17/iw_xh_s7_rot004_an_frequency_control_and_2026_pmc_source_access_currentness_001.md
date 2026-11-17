---
artifact_id: IW_XH_S7_ROT004_AN_FREQUENCY_CONTROL_AND_PMC_SOURCE_ACCESS_CURRENTNESS_001_20261117
exposure: PUBLIC
origin_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
created_at: 2026-11-17
document_type: SOURCE_NATIVE_BOUNDED_SCIENCE_REPORT
class: ORIGINAL_AN_AUTHOR_PUBLISHED_FREQUENCY_CONTROL / POSTHOC_COVARIANCE_ROBUST_NUMERIC_GUARD / OTHER_APPARATUS_SEISMIC_CMR_PRIOR_ART / PMC_2026_ACCESS_MIGRATION
status: REPRODUCIBLE_CONDITIONAL_SOURCE_ARITHMETIC_PASS / RAW_ARTICLE_SI_TORQUE_VECTOR_COVARIANCE_HOLD / NO_NASH_BRIDGE
claim_ceiling: NO_NEW_EXPERIMENTAL_FORCE / NO_NEW_ALPHA_LIMIT / NO_FREQUENCY_DEPENDENCE_DISCOVERY / NO_CMR_TRANSPORT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT004 — actual original frequency-control data, unknown-covariance guard, same-team noise prior art and 2026 PMC data-access correction

DATE: 17 November 2026, Europe/Warsaw. This bounded turn follows ROT003. Predecessor XH-S6 physical raw torque HOLD is inherited; XH-S7 ROT001, ROT002 and ROT003 are not retroactively rewritten. In existing B1 source issue #16 latest states show LT9 T3 done, AUD3 T1/T2/T3 bounded read-only audit, and Mech-S10 T2R still pending unique executor lease. No B1 rerun or owner overlap.

## Original sources and actual access level

1. An, Tan, Dong et al. (firstness), *Test of the gravitational interaction between milligram masses using a miniature torsion pendulum*, Nature Communications 17, 11425 (2026), published 7 Oct, DOI https://doi.org/10.1038/s41467-026-78187-4 . Original journal site https://www.nature.com/articles/s41467-026-78187-4 ; original author's full open-access article indexed on PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC13737168/ ; PubMed PMID42982831 https://pubmed.ncbi.nlm.nih.gov/42982831/ . Direct PMC page-open failed in this tool environment, but search-index retrieval surfaced extended original article sections (*Experimental setup*, *Experimental data*, *Data analysis* and explicit frequency control paragraph) including named original statistical observations. **This is original publisher-derived indexed article text, NOT a byte-verified full downloaded HTML/PDF or SI, NOR raw measured voltage series**.
2. Tan, Lu, Long et al. (independent same-laboratory but DIFFERENT DEVICE original primary), *Suppressing seismic coupling noise in torsion pendulums based on common-mode rejection with dual pendulums*, Phys. Rev. Applied **26, 044045** (published 16 Oct 2026), DOI https://doi.org/10.1103/tcb8-csbs , original APS abstract https://journals.aps.org/prapplied/abstract/10.1103/tcb8-csbs . Authors include Wen-Hai Tan, Zheng-Jie An and Shan-Qing Yang. APS abstract only, not full paper PDF or full method.
3. NIH NLM PMC official developers' documentation (verified source) https://pmc.ncbi.nlm.nih.gov/tools/textmining/ and https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/ . Dataset distribution migrated **26 Aug 2026**; old OA Web Service / old FTP files retired in August. New public AWS bucket `pmc-oa-opendata`, per article version directory `PMC<id>.<version>/` with JSON/XML/TXT, optional PDF/supplement files conditional on rights. Official AWS access is not evidence that this particular article's supplement objects have been read.

## 1. Distinct original experimental falsifier: same apparatus, sixfold frequency variation

The ORIGINAL An et al. article *Experimental data* explicitly reports a source rotation period varied from 600 to **3600 seconds**, with an actual 16-fold torque frequency respectively `16/600 Hz=26.666667mHz` and `16/3600 Hz=4.444444mHz`, at **unchanged test-source separation 0.654mm**. The original measured amplitudes (statistical error **only**, 1σ) are:

| original source measurement | frequency | torque aNm | 1σ STAT aNm |
|---|---:|---:|---:|
| `tau_1` | 26.667mHz | 11.16 | 0.27 |
| `tau_2` | 4.444mHz | 11.41 | 0.46 |

The author reports 15 lower-frequency measurement sets, 13 full turntable rotations per set, and states no frequency dependence observed within uncertainties. Do not mistake 13 rotations for 13 independent Gaussian experimental realizations or use a sample-size rescaling of the reported published SE. Source owner FIRST remains An et al.

### New XH bounded numerical checks (no raw experiment)
Let `Delta = tau_2 - tau_1`, from the published two central values. Then `Delta=+0.25aNm`, i.e. `+2.24014%` relative to high-frequency amplitude. Under **the explicitly unverified assumption** that author quoted one-sigma statistical errors are independent Gaussian SDs, `sigma_Delta=sqrt(0.27^2+0.46^2)=0.5333854141aNm`, `z=0.46870423`, two-sided standard-normal p≈0.639281, and a conventional approximate two-sided 95% statistical interval is `[-0.7954354,+1.2954354] aNm`. This interval includes zero, not proof of exact frequency invariance. Its maximum positive boundary is 11.61% of 11.16 aNm; a two-sided percent interval is asymmetric around zero. No systematics/correlated model covariances included.

**More robust algebraic check without assuming independence:** for unknown correlation coefficient `rho∈[-1,1]` of the two published marginal statistical SDs, `Var(Delta)=0.27²+0.46²-2*rho*0.27*0.46`, hence `0.19≤sigma_Delta≤0.73 aNm` and `0.34246575≤|z|≤1.31578947`. Within this covariance-only family, **the observed difference fails a 1.96σ threshold for every rho**. This statement holds algebraically assuming reported numbers are comparable SDs; it does not solve non-Gaussian errors, common systematic shifts, all-frequency phenomenology or changes in actual test-mass geometry.

Strong discrimination: A claim of `no source-supported frequency variation` within the two stated frequencies is compatible with measured data. Any supposed **NASH-predicted** more precise change in frequency would require a predeclared source-typed dimensionful law with the same frequencies, measured harmonic phase, background and full covariance, NOT a posthoc reading of the author-compatible 0.25aNm difference.

## 2. Additional mature same-lab seismic reference — SOURCE-NATIVE no transport

The original APS **distinct dual-pendulum device** under deliberately driven seismic vibration reports raw torque noise amplitude spectral density about `1.4×10^-14 Nm/sqrt(Hz)` at approximately 2mHz, and common-mode rejected `1.1×10^-15 Nm/sqrt(Hz)` at the same regime. Arithmetic ratio = `12.72727`. Original Tan et al. achieved CMR >order of magnitude for THEIR setup; it does **not** establish CMR was implemented in An's miniature rotating-source torsion apparatus or that such suppression occurs there. Nor can its noise values at around **2mHz** be substituted for the An instrument 4.444 or 26.667mHz noise bands. The An article's own low-noise band near ~30mHz and separate control already specify its readout constraints. THIS IS MATURE/ADJACENT METROLOGY HOST; not direct prior-art for a new NASH force claim.

## 3. Actual 2026 PMC archival access protocol — exact bounded state

Official NLM developer guidance says old PMC FTP archive and old OA Web Service were retired by Aug26. A current, source-legal route for *eligible CC-BY articles* is the PMC AWS public dataset. Search/verify article `PMC13737168` by listing all available version prefixes before any data download, **do not assume version 1 or file names**:

```sh
aws s3api list-objects-v2 --no-sign-request \
 --bucket pmc-oa-opendata \
 --prefix "PMC13737168." \
 --delimiter "/" --query "CommonPrefixes[].Prefix" --output text
```

For an AUTHENTIC returned version `PMC13737168.<v>`, list all its files with `aws s3 ls ... --no-sign-request`, select original supplementary PDFs and copy the **actual returned paths**, then verify bytes length + SHA-256 + PDF pages and compare tables. The NLM cloud service offers JATS XML/TXT and supplementary objects *if available* and if article/license eligible. This session's container cannot resolve outside DNS; web source could not open direct PMC HTML or hypothetical S3 object. Thus **no S3 listing was executed, no authentic article version selected, no supplementary PDF bytes acquired**, and PMC's August migration is a **separate real infrastructure fact**, not a verified explanation for why nature.com/page web cache missed.

The precondition to reanalyze original Yukawa limits remains physical source volume CAD, spokes metrology, raw five-gap complex 16th-harmonic amplitude+phase vector with covariance, calibration/systematics and author's likelihood; ROT023 synthetic ring does not satisfy it. A real measured frequency-control pair is now identified, but two published scalar amplitudes cannot replace full vector/covariance. Full NASH bridge needs independent source-typed `delta_tau(theta,s,omega;NASH parameters)` preregistered against original observables.

## 4. Reproducibility and claim custody

The companion local standard-library script `xh_s7_rot004_frequency_gate.py` and its emitted JSON `xh_s7_rot004_frequency_gate.json` independently re-evaluate ALL reported arithmetic including unknown-rho extrema, frequencies and APS noise ratio, without network or source-model execution. Original publisher numbers have not been run through author analysis; this is explicit posthoc **derived arithmetic**. Local script SHA256 `5d28d621477f19bcc2a832b8dd8df6f2dabe6e799b48f6e3cc30d22c4bb83e3d`, JSON SHA256 `9e86d53c055038d4cf9e8ae59f0f855a298a25842273eb40b554087ecf95a995` at time of local execution. Artifact publication via GitHub is NOT an independent cross-cell referee, and writing the report is not owner ACK.

NO new gravitational experiment, no new alpha(lambda) bound, no novelty, no proof of frequency invariance across all frequencies, no invalid CMR transfer, NO_NASH_BRIDGE, NO_CANON, NO_EXEC_SIGN, BW GITHUB_PENDING_BW_INGEST.

FINAL: ROT004_ORIGINAL_AN_2FREQUENCY_SOURCE_NUMBERS_RECOVERED / DELTA_0P25_ANM_0P469_SIGMA_UNDER_INDEPENDENCE / ALL_RHO_SOURCE_STAT_NOT_SIGNIFICANT / SAME_TEAM_APS_2MHZ_NONTRANSFER / PMC_AUG2026_MIGRATION_VERIFIED / SUPPLEMENT_BYTES_RAW_COVARIANCE_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN.
