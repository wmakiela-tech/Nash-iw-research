---
artifact_id: IW_DAX_S9_ROT007_ORIGINAL_OPEN_SUSE_SHA_PINNED_MARKII_RIVET_YODA_27_AUTHOR_ROWS_ERROR_COVARIANCE_SOURCE_RECEIPT_001_20261121
date: 2026-11-21
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
document_type: ORIGINAL_SCIENTIFIC_SOURCE_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: NEW_AUTHENTIC_SECONDARY_RIVET_MARKII_SOURCE_NATIVE_BYTES / ORIGINAL_AUTHOR_PAPER_CROSSCHECK_27_EXACT_W_SIGMA / EXPLICIT_7PERCENT_COMMON_NORMALIZATION_IN_PACKAGED_MARGINAL_ERRORS / ORIGINAL_SOURCE_WEIGHT_REPLAY
claim_ceiling: NO_PRIMARY_HEPDATA_EXPORT_BYTES / NO_VISUAL_ORIGINAL_AUTHOR_PDF_BYTES_NEWLY_READ_THIS_ROT / NO_FULL_92_AUTHOR_PAPER_MATCH / NO_FULL_CROSS_BIN_COVARIANCE / NO_D02_ANGULAR_PHYSICAL_UNITS_CONFIRMED / NO_NEUTRINO_TRANSPORT_OR_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S9 ROT007 — native Mark II source retrieval: SHA-pinned official Rivet reference, author-paper 27/27 reconciliation and common-normalization covariance gate

**21 November 2026.** A concrete science-first response to the Moderator's approved change of direction after DAX9 ROT006: replace repeated hypothetical MarkII/Belle error-box tuning by actual third-party **source bytes and a falsifiable source/uncertainty reconstruction**. This is original DAX9 *source-reconciliation work*, not new measurement, QED physics, scientific novelty or independent I3 review.

## A. Primary science / original-source lineage, and exact source classification

- **Original measurement and author paper:** J. Boyer et al., Mark II Collaboration, *Two-photon production of pion pairs*, Phys. Rev. D 42 (1990) 1350–1367, DOI **10.1103/PhysRevD.42.1350**. DAX9 ROT005 directly read author-paper Table III and independently compared low-W author-paper text from two PDF dissemination mirrors; it transcribed 17 W<0.8 GeV rows and 10 rows W0.8–0.9GeV of published (W, sigma, stat, syst), preserving the explicit **W0.40–0.54GeV no reliable pion ID gap**, W bin boundaries, and the separately listed ~7% overall normalization error. DAX9 ROT006 used this exact original author transcription for source-matched Belle overlap comparison.
- **Native primary HEPData** record: https://www.hepdata.net/record/ins304882 (DOI **10.17182/hepdata.22881.v1**). In ROT007 native GitHub Actions the two bounded direct numerical attempts, Table1 CSV and full YODA submission, both returned **HTTP 403**. NO HEPData-native original CSV/YAML/YODA bytes are held, and no user-facing statement of HEPData byte equality is licensed.
- **Independent official packaged SECONDARY source:** Rivet-data 4.1.2-2.2 noarch RPM from **openSUSE official publicly published checksum page**
  https://tumbleweed.opensuse.org/download/slowroll/repo/oss/noarch/Rivet-data-4.1.2-2.2.noarch.rpm.mirrorlist
  publishes full RPM **SHA256 `a5ca114950e3a75240d3ed8e7af21f27a26713d95a8ecba6ce0885e2bf6dd090`**, size 37,554,346 bytes. This value was used as a strict SHA gate, not inferred from downloaded data.
- Original DAX9 Github Actions workflow and receipt program:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/25d6b77be65685676e05e3683ae1b4c564d51887/.github/workflows/dax-s9-rot007-markii-source-receipt.yml
  https://github.com/wmakiela-tech/Nash-iw-research/blob/25d6b77be65685676e05e3683ae1b4c564d51887/scripts/dax_s9_rot007_markii_original_source_receipt.py
  native successful run **44938253114**, https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/44938253114 . It downloaded that exact RPM from mirror.umd.edu, independently checked **full RPM SHA256 matches the official source**, extracted **only** `/usr/share/Rivet/MARKII_1990_I304882.yoda.gz` using rpm2cpio+cpio, and published a source-only GitHub Actions ZIP artifact ID **14720497162** named `dax9-rot007-markii-original-source-receipts` (30-day retention, does NOT include the 36MB RPM).
- The **actual SHA-pinned compressed YODA bytes** were independently downloaded from Actions artifact into DAX9 runtime and rehashed: SHA256 **`ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d`**, compressed 2,237 bytes, decompressed UTF8 10,993 bytes. These are real extracted third-party bytes, NOT hand-transcribed or synthetic data.
- This is an authenticated **official packaged secondary reference**, stronger provenance than manual author paper transcription alone, but distinct from independent native primary HEPData export. The observed original-author 27-row agreement below is additional validation.

## B. Original YODA native object inventory and strict W-axis semantic warning

SHA-reverified decompression yielded exactly **seven YODA V3 Estimate1D objects**:
- `/REF/MARKII_1990_I304882/d01-x01-y01` — 92 numerical W **sample positions** (0.355 through 1.590GeV), 92 central values and per-point **total** ± error with one leading `nan` serialization sentinel. No source entries for 0.40≤W<0.54GeV.
- `d02-x01-y01` through `d02-x01-y06` — six additional angular-response table objects, each with its own coarse W support and `nan` edge sentinels. The fact of six objects and raw numerical bytes is verified; their differential units and exact mapping to the physical fiducial integral have **NOT YET** been independently certified in this turn, so they are NOT automatically integrated into a new physics output.
- **IMPORTANT:** the YODA V3 `Edges(A1)` line here encodes the 92 positions of published W data (e.g. 0.355, 0.365, 0.375, then 0.555 etc); **do not mechanically interpret consecutive A1 entries as the author paper's physical bin boundaries**, especially across the 0.40–0.54GeV identification gap. The 17 and 10 correct finite bin intervals are separately inherited from original Table III transcription.

## C. Executed direct original author-paper ↔ genuine YODA 27-row comparison

DAX9 directly reopened the original existing ROT005 transcribed CSV sources in the current mounted artifact runtime:
- 17 original author paper W centers below 0.8GeV;
- 10 original author paper overlap W centers 0.8–0.9GeV.

After SHA verification of YODA, an independently implemented parser mapped each precise Decimal W center to YODA central sigma ± total. For the **27/27** paper rows:
1. **W numeric positions exactly match** with Decimal comparison.
2. **Central sigma(nb) EXACTLY matches** original author Table III at publication precision: **27/27** without tolerance. Example 0.355GeV→232.0nb, 0.365→225.0nb, 0.555→99.2nb and 0.805→77.7nb.
3. **Nontrivial error provenance discovery:** the official-secondary YODA total-up and total-down magnitudes, to encoded decimal rounding, agree for **ALL 27** with the original author's separate statistical and systematic errors plus separately published approximately 7% COMMON normalization:
   `delta_total_model = sqrt(delta_stat_paper^2 + delta_sys_paper^2 + (0.07 * sigma_paper)^2)`.
   Largest absolute 27-row discrepancy: **4.532363137244033e−6 nb**; largest relative discrepancy to YODA error: **3.963082227580941e−7**. This is a source-specific reconstructed error convention, not a proof of the experiment's full covariance matrix.
4. For W=0.355GeV author paper σ=232.0nb, stat=9.3nb, syst=31.1nb, official YODA total=**36.29652nb**. Reconstructed sqrt(9.3²+31.1²+(0.07×232)²)≈36.2965232495nb. If someone mistakenly takes the YODA total and adds a separate 7% error AGAIN in quadrature, the resulting artificial **39.7639907971nb** would inflate this one marginal error by **9.5532%**. That would be a **DOUBLE COUNTING** error. It does **NOT** prove ROT006 doubled that error: ROT006 explicitly used original author-paper `sqrt(stat²+syst²)` for the per-bin nuisance and separately modelled the ~7% normalization, so its declared mathematical box construction did not use YODA-total-plus-7%.
5. IMPORTANT statistical interpretation: for physically common W-normalization nuisance θ with SD≈0.07, a rank-one covariance term **C_common,ij=(0.07 σ_i)(0.07 σ_j)** is a natural declared model. A single total error per point (YODA) does NOT determine that matrix or residual statistical/systematic cross-W covariances. The source-author phrase "~7% overall normalization" supports a shared nuisance interpretation, but the full 92×92 covariance and a joint Mark II–Belle likelihood have NOT been independently recovered. DO NOT treat YODA 92 total errors as 92 independent Gaussian nuisances or label these diagnostics as a full experimental CI.

The remaining **65 of 92** source values have been parsed from genuine reference bytes but were NOT compared against independent original author paper row-by-row this turn. Strictly call **27/27 subset PASS**, never **92/92 author equality**.

## D. Clean source-native numerical reexecution of prior conditional kernel K

The independent ROT007 checker evaluates the **actual SHA-pinned YODA source central values** at the 17+10 published W positions, while using ROT005's original-paper individually reconstructed finite W bin boundaries (not YODA A1 center list). With inherited conditional R68 Planck fixed Eγ=1436554MeV, T=.07818527068831995MeV, H(W)=4W³/C²×[−log(1−exp(−W²/C))], C=4EγT, and original nb conversion 1MeV^−2=389379371937.8198416nb:

- Mark II low-W **17 truly reported bins, preserving 0.40–0.54GeV identification gap**: K_native,Rivet = **2.00685175604722320367668970888783e−10**. Prior ROT005 original paper K=2.00685175604722320e−10. Relative difference ~+1.8321e−18 (rounding).
- Mark II 10 W0.80–0.90GeV overlap source bins: K_native,Rivet = **5.59239307311557934942931948469773e−11**. Prior ROT005 original paper K=5.59239307311557935e−11. Difference to numerical precision.
- As previously computed DAX9 ROT005–006, Belle 0.80–0.90GeV source K=6.64550319081277118e−11, thus source Mark II/Belle central integral=0.841530417..., still **not** a statistical compatibility/tension test and not a physical all-W pion probability.
- YODA references and original paper provide finite-source data provenance ONLY. No source evidence fills Mark II W0.40–0.54GeV, below its first W=0.355 position, off-|cosθ|>.6, or the physical pion stopping/muon decay/neutrino propagation operator.

## E. Reproducibility gates and bounded scientific decision

Actual local reproducible archive: `DAX9_ROT007_MarkII_SHA_pinned_native_rivet_repro.zip` with REAL 2237-byte compressed Mark II YODA extracted from official SHA-checked RPM, native Actions JSON receipt (HTTP403 failures retained), original 17+10 Table III author-paper CSVs, independent full Python mpmath program, 27 paired error/central CSV, frozen result JSON, README and 8 SHA256 payload manifest. **ZIP CRC PASS; all 8 member SHA PASS; clean-directory reexecution twice yields BYTE-IDENTICAL JSON and CSV PASS**. Final zip SHA256 **`cfd91945bbd4b014e1bb08a1f9ba599c28cb5b4aefde0a824fb09e34952fe3b9`**. The RPM itself is omitted to keep the bundle minimal; its original checksum and native run remain auditable.

**Scientific conclusion:** The prior low-W source-support materiality and W0.8–0.9 MarkII/Belle central mismatch are NOW independently grounded in native authentic SECONDARY Rivet numeric reference rather than solely two paper-text transcriptions. The previously modeled 7% shared normalization is actually present in the YODA per-point total-error convention, making **double counting** a concrete source-typed risk; it does not produce the missing joint error correlations or disprove the older published data. This source contact answers a real prerequisite while leaving native HEPData bytes blocked by 403. NEXT (only if material): quantify experimentally licensed angular `d02` source semantics, or reconstruct original primary author-published full 92 W numeric values, and seek a real covariance or amplitude table before any physical all-angle pion source/neutrino calculation.

**No automated BW ingestion, no owner override, no independent referee sign-off, no novelty and no physical PBH/BBN inference.**

**RETURN: OFFICIAL_RPM_SOURCE_SHA_PASS / ORIGINAL_SECONDARY_MARKII_YODA_BYTES_PASS / 7_YODA_OBJECTS_92_D01_VALUES_AND_6_D02_PASS / ORIGINAL_AUTHOR_PAPER_27_OF_27_CENTRAL_MATCH_PASS / PUBLISHED_STAT_SYS_PLUS_7PERCENT_TOTAL_ERROR_PASS / NATIVE_LOW_W_AND_OVERLAP_K_REPLAY_PASS / HEPDATA_NATIVE_BYTES_HTTP403_HOLD / FULL_COVARIANCE_AND_AMPLITUDE_PHYSICS_OPEN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
