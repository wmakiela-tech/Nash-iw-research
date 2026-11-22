---
artifact_id: IW_XH_S7_ROT014_NOV19_NATURE_COSMOLOGY_RETRACTION_DESI_FLAMINGO_AND_ORIGINAL_ADPD_CODE_BOUNDED_PROBE_001_20261122
date: 2026-11-22
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
exposure: PUBLIC
class: EXTERNAL_ORIGINAL_SCIENCE_SOURCE_HARVEST / RECENT_CORRECTION / PRIMARY_SOURCE_RETRACTION / NATIVE_CODE_FORMULA_AUDIT / BOUNDED_INDEPENDENT_TOY_REPLAY
source_status: PUBLISHER_RETRACTION_ORIGINAL_PRIMARY_TEXT_PASS / AUTHORS_GITHUB_ORIGINAL_SCRIPTS_DIRECT_READ / SAWALA_REPRO_NOTEBOOK_AUTHOR_READ / SYNTHETIC_FORMULA_REPLAY_EXECUTED / RAW_DESI_FLAMINGO_DATA_NOT_FETCHED
claim_status: RETRACTION_AND_CORRECTED_SIGNIFICANCE_SOURCE_PASS / CODE_LEVEL_RADIAL_BIN_REPLAY_PASS / PAPER_CAUSAL_LINEAGE_AND_DESI_EFFECT_HOLD
claim_ceiling: NO_FULL_OBSERVATIONAL_REANALYSIS / NO_PAPER_CODE_PROVENANCE_ESTABLISHED / NO_NASH_PHYSICAL_PREDICTION / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT014 — One high-value 2026 external physics correction with original-source numerical boundary check

**External science target date**: 19 November 2026 (original Nature retraction), crosschecked 22 November 2026.
**Scientific orientation**: external original science and literature, not NASH B1/BBN owner arithmetic, internal audit proliferation, or generic AI-agent benchmarking. The moderator's prior explicit direction: "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji." This O authorizes this bounded autonomous external research rotation.

## 1. Critical correction to a highly consequential real physics claim — PRIMARY ORIGINAL PUBLISHER

Original paper: Francesco Sylos Labini and Marco Galoppo, "Detection of anisotropic cosmic structures on a gigaparsec scale", *Nature*, published **24 June 2026**, DOI https://doi.org/10.1038/s41586-026-10702-5 .

It used DESI DR1 redshift surveys and angular distribution of pairwise distances (ADPD), comparing observed galaxy projected distributions with Poisson/angular-random controls and cosmological N-body mock catalogs. It claimed anisotropy persisting to Gpc scales beyond expected ΛCDM structure and reported nominal >3 sigma discrepancies. Since **19 Nov 2026** the publisher permanently marks the original **RETRACTED ARTICLE**; its original >3 sigma conclusion is NOT a valid established challenge to the cosmological principle.

Actual primary **RETRACTION** (source directly indexed in publisher and PDF text):
Sylos Labini & Galoppo, "Retraction Note: Detection of anisotropic cosmic structures on a gigaparsec scale", *Nature*, **19 November 2026**, DOI https://doi.org/10.1038/s41586-026-11388-5 . Authors unequivocally say they **erroneously compared COMOVING DISTANCES of observed galaxies with LUMINOSITY DISTANCES between simulated galaxies in mocks**, an estimand/measurement-convention mismatch. They report after correcting the analysis, apparent disagreement now only **1.48 to 2.75 sigma depending on the selected sample**, below a conventional 3-sigma interpretative reporting threshold. Both authors agree to retraction. They still describe at best tentative anisotropy evidence, not statistically supported original major discovery. Editors suggested the retraction; original authors intend to submit an updated paper elsewhere but this does NOT license assuming later success or new paper already exists.

The independent critic, Till Sawala, original preprint arXiv:2607.01172 first submitted **1 July 2026**, followed by peer-reviewed *Astrophysical Journal Letters* **1007, L22**, first online 6 Aug 2026 and print 10 Aug 2026, DOI https://doi.org/10.3847/2041-8213/ae908f . This critic sources the same data, compares observed DESI DR1 distribution to FLAMINGO hydrodynamical galaxy mocks in ΛCDM, emphasizes correct COMOVING distance and galaxy tracer bias / redshift-space distortions. Reports data consistent with standard cosmological principle for studied sample; cannot infer proof of exact global isotropy at all scales.

Two-surface prior art:
A = standard FLRW distance duality, comoving/transverse vs luminosity distance, galaxy bias and redshift-space distortions, cosmological two-point directional statistics and model-comparison sample selection.
B = original Sylos Labini & Galoppo paper, exact independently published Sawala 2026 correction, original Github source-native DESI-FLAMINGO reanalysis and the 19 Nov Nature retraction. Firstness belongs to independent critic and publisher correction, not NASH/XH.

In spatially flat FLRW, d_L=(1+z)d_C, with d_C line-of-sight comoving distance (more generally d_L=(1+z)d_M with transverse comoving distance d_M). Thus z=0.2 gives 1.2x d_L/d_C. This analytic relationship demonstrates a plausible *type* mismatch, but XH did NOT calculate the published 1.48–2.75 sigma and CANNOT infer its magnitude or dependence on data solely from the d_L relation. The retraction itself is the authority for corrected significance and original code path. More context: no claim that the original ADPD statistic is inherently invalid when properly applied.

## 2. Original source authors' code and independent critic's separate pipeline, actual direct reads

**Retraction-side author ORIGINAL repository**, code first added **11 May 2026** (BEFORE the Nature publication and the later retraction):
https://github.com/MarcoGaloppo/Code-and-Data-Detection-of-anisotropic-cosmic-structures-on-a-gigaparsec-scale
Direct GitHub read:
- `README.md` blob `6eee1469bd066c5a2f033fd20147c9badd394af9`, author file describes DESI BGS/LRGS, actual original sample S1–S4/LRGS Zenodo DOI https://doi.org/10.5281/zenodo.20118015, ADPD algorithm, Poisson and bootstrap references, LCDM mock selection.
- `Compute_adpd_python.py` blob `2d5243e0a8feb6a04ca78acc6c801f7d1ea6b4b9`, DIRECT complete source read, commit `c9810c2beb6c` (last public repo update May 11).
- `Compute_LCDM_statistics.py` blob `07d344a5d0103061dcf9dc083ed2fe60f35faa81`, directly read.
- `Generate_LCDM_mock_samples.py` blob `61ba577b013daf9528d3bce266b414bc8b8d50de`, directly read; generates N-body DARK MATTER particle slice catalogs (not galaxy observations) matched geometry and N target. Distinguish physical tracer bias/redshift-space mocks; do not assume the raw code is the exact published or ultimately corrected simulated galaxy catalog object without run receipts.

**Independent critic Till Sawala ORIGINAL source**:
https://github.com/TillSawala/DESI-FLAMINGO
- `README.md` blob `60a636b2055cc1a57b112509fec6ae40ed734694` directly read: includes a `DESI_FLAMINGO.ipynb` ~3.24MB author analysis, data retrieval DESI DR1, SDSS and FLAMINGO particle AND galaxy catalogs, redshift-space corrections, comoving-vs-luminosity demonstrator, comparison original S2 and ADPD. Source tests default FLAMINGO L1_m8 snapshot 0075 z=.15 and L1_m9_DMO snapshot 0074. Direct original notebook **file inventory verified**, notebook complete ~3.24MB NOT loaded into working process because connected tool response size boundary, so NO claim each notebook cell or all saved figures directly inspected. Main README was originally committed July19 latest. `CITATION.cff` blob `a28bf201f98bea683b6b630dcf91a26538362f9c` full read; versioned archive software Zenodo https://doi.org/10.5281/zenodo.21445576 . Distinguish source accessible vs source RUN.
- Real source data DESI DR1, source S2 sample Zenodo DOI20118015 and FLAMINGO simulation original public service: declared by original authors, but raw galaxy simulation bytes and Fig outputs not fetched by XH.
- No re-run of entire DESI→FLAMINGO notebook, no 2000 mock sample 27,685-galaxy N-body computations, no published ADPD p-value reproduction.

## 3. New distinct source-native exact micro-falsifier: radial bins of AUTHOR PUBLIC standalone ADPD script

The public `Compute_adpd_python.py` defines:
```python
r_point = np.sqrt(x*x + y*y)
rmin = np.min(r_point)
rmax = np.max(r_point)
dbin = (rmax - rmin) / dist_bins
# Later for DIFFERENT quantity:
dist = np.sqrt((x[j]-x[i])**2 + (y[j]-y[i])**2)
d_bin = np.floor((dist-rmin) / dbin).astype(np.int64)
good = (d_bin>=0)&(d_bin<dist_bins)
```
This makes the pair-separation radial support `[min center-to-point radius,max center-to-point radius)`, **not** the full observed separation range `[min pair separation,max pair separation]`, which can approach 2R for points inside a radius-R circle. Its README describes pair-distance shells but does NOT document the center-radius restriction as a deliberate estimator definition.

**Actual XH standalone mathematical formula replay EXECUTED on independent synthetic data**: four collinear points x=(-6,2,4,6), y=(0,0,0,0); exactly six unordered pair distances sorted (2,2,4,8,10,12). Center radii min=2,max=6, 50 bins => retained only pair distances (2,2,4), excluded (8,10,12). **3/6 are excluded from source's declared pair-distance histogram in this toy.** The actual Python implementation in the author's repo was not executed; XH copied precisely the relevant original formulas in an independent script, ran it with NumPy, and confirmed assertions. It is SOURCE-FORMULA REPLAY, not full author program reproduction or observation of the original DESI sample.

**Another source-specific empty-shell property**: public author code keeps p(theta,r)=0 when M_pairs(r)=0; its `angular_variance` returns `mean[(p-1/N_theta)^2]`, equal to positive `1/N_theta^2` for empty shells rather than undefined/NaN. With N_theta=720 and that four-point example, 48 of 50 radius bins are empty and each reports `1/720² = 1.929012345679...×10^-6`. In full 27k-galaxy samples the frequency of empty shells may be negligible; actual impact unknown. The toy demonstrates a software-level default that MUST be explicitly masked when interpreting sparse data, not experimental evidence of cosmic anisotropy.

**EXACT NEGATIVE CLAIM**:
Neither test establishes the origin of the retracted 2026 paper's significance nor that the affected standalone script was run for the published plots. The authors' explicit retraction identifies a DIFFERENT error (comoving-vs-luminosity distance mismatching), and XH has no original run manifests connecting source `Compute_adpd_python.py` to the exact manuscript figures, or original observation/mock numerical reanalysis. Do not assert "XH found a second cause of the paper's retraction" or "paper invalid because 3/6 pairs excluded". Rather: **ADPD_PUBLIC_STANDALONE_CODE_REPRODUCIBILITY_FLAG** for source author/independent reviewer if precise code-to-figure provenance is established.

Local executable probe delivered as separately created and executed conversation files:
- `xh_s7_rot014_pair_geometry_probe.py` (2836 bytes, SHA-256 `6f28ff4ed5d2d1a5e98eba68f1a1447e8040f6b7cb31b72cfd5dc31df46d52c7`).
- `xh_s7_rot014_pair_geometry_probe_receipt.json` (SHA-256 `26f9be0aed324313aca456669b8cfe4a459fea6c2ae15d90158d2b3d82f776e0`).
These are **original XH synthetic demonstrations**, not copies of raw DESI measurements and not authors' experimental scripts.

## 4. The epistemic boundary and empirical relevance to NASH

This actual external physics correction supports a very specific general failure mechanism important in science:
`SOURCE_REPO_PASS + CODE_RUN_PASS + STATISTIC_PASS + PAPER_PRESENTATION_PASS ≠ MEASUREMENT_CONVENTION_PASS ≠ PHYSICAL_CLAIM_PASS`.
A numerical observation can be correct yet target a different observable than its counterfactual simulation; 20% dimensional convention differences can be a *source-type issue* before statistical significance is even computed. Separately, pure stable code may drop mathematically allowed data subsets or silently assign a value to empty statistics. Proper assessment needs explicit `DATATYPE (observed/mocks)`, `COSMO_DISTANCE_CONVENTION`, `COSMOLOGY/FIDUCIAL PARAMETERS`, `GALAXY_BIAS/RSD`, `PAIR_RADIAL_RANGE`, `M_EMPTY_HANDLING`, `SOURCE_CODE_COMMIT`, `DATA_RELEASE`, `OUTPUT_RECEIPTS`.

Target-relative novelty of NASH: this is NOT a new NASH physical discovery, a refutation of ΛCDM, or an original firstness of recognizing science provenance faults. It is a concrete, externally anchored 2026 **negative knowledge case** and a bounded actual source-formula test within XH remit. Foundation = established scientific methods of comparing same objects, measurement convention and cosmological distance definitions; contemporary specialist source = Sawala 2026 independent correction and Nature retraction. Existing role/data-trace protocol alone is NOT sufficient, and an external team must demonstrate actual outcome quality before NASH method claims.

Potential one-step falsifier, if a distinct physics hypothesis or reviewer specifically requests it: load verified actual S2 original data and public N-body mocks, freeze original and corrected code paths, run two distance conventions plus bias/RSD-matched mock, verify source unit and same radial bin semantics, and recover original 1.48–2.75 sigma (authors' stated values). No such data-intensive experiment was launched here, and user was not asked to authorize internal B1 work.

No external authors contacted. No new NASH owner tasks, no B1 PREREG, no C1 resume, no independent original cosmological inference claim. Public GitHub report is NOT BW ACK/closed review.

FINAL:
XH_S7_ROT014_PRIMARY_NATURE_RETRACTION_CONFIRMED /
SAWALA_2026_INDEPENDENT_PRIOR_ART_ORIGINAL_CODE_READ /
AUTHOR_2026_ORIGINAL_ADPD_PUBLIC_CODE_READ /
SYNTHETIC_4POINT_RADIAL_BIN_MISMATCH_REPRO_EXECUTED /
EMPTY_SHELL_POSITIVE_DEFAULT_REPRO_EXECUTED /
SOURCE_SCRIPT_TO_PAPER_NUMERIC_LINEAGE_HOLD /
NO_FULL_DESI_REANALYSIS / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN.
