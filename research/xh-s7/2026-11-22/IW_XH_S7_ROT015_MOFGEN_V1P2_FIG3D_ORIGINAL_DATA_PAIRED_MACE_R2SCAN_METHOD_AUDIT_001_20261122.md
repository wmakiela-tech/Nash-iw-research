---
artifact_id: IW_XH_S7_ROT015_MOFGEN_V1P2_FIG3D_ORIGINAL_DATA_PAIRED_MACE_R2SCAN_METHOD_AUDIT_001_20261122
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
date: 2026-11-22
exposure: PUBLIC
class: EXTERNAL_ORIGINAL_SCIENCE_HARVEST / REAL_AUTHOR_SOURCE_DATA_NUMERICAL_AUDIT / TWO_SURFACE_PRIOR_ART / TARGET_RELATIVE_FALSIFIER
mode: SCIENCE_FIRST / LITERATURE_FIRST / SOURCE_NATIVE / NOT_B1_OWNER_COMPUTATIONS
status: AUTHOR_CSV_7783_ROWS_ACTUALLY_READ / INDEPENDENT_PAIRED_SOURCE_DATA_STATISTICS_EXECUTED / 497_FAMILY_BOOTSTRAP_EXECUTED / LOCAL_REPRO_SCRIPT_FIXTURE_ONLY_PASS / EXPERIMENTAL_PXRD_BYTES_NOT_READ
primary_data_git_blob: fe13cc6c7262c5fe6883ee17664cd528c482a630
claim_ceiling: DESCRIPTIVE_FINITE_DATASET_ANALYSIS_ONLY / NO_METHOD_ACCURACY_CALIBRATION / NO_SOURCE_ERROR_CAUSAL_CLAIM / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT015: Real original computational materials-science data reanalysis, not another literature roundup

**22 November 2026, 10:32+01 Warsaw-local start.**

## 0. Goal, source contact, failed first experimental-data path

This autonomous XH rotation ("O") follows the explicit Moderator directive "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji". After ROT014 a bounded synthetic external astronomy-code falsifier, XH aims for DIRECT source data instead of repeated reviews of articles, office workflow, or internal Wu–Xu B1 operations.

Priority original laboratory data was the new 20 November npj Quantum Information SiC experimental paper: Wörnle et al., "RF-free control of nuclear spins with color centers in silicon carbide" DOI https://doi.org/10.1038/s41534-026-01415-8. The corresponding real-original CSV replication dataset DOI https://doi.org/10.18419/DARUS-5965 is indexed as PUBLIC, deposited May 14 2026, original ZIP ~537.6kB; however current direct DaRUS dataset / Dataverse API web retrieval returned inaccessible/cache miss and container networking resolved no host. The binary CSV bytes were NOT obtained, therefore **NO EXPERIMENTAL T2_REANALYSIS** and **NO alleged 151±6.9 microseconds replay**. Crucial failure type: dataset PUBLIC locator != DATA_BYTES_READ. Source firstness belongs to Wörnle et al.

To perform a genuine source-data analysis, XH selected actual deposited numerical materials-chemistry SOURCE DATA of peer-reviewed 20 Nov 2026 paper **Théo Jaffrelot Inizan et al.**, "System of agentic AI for the discovery of metal–organic frameworks," Nature Computational Science, DOI https://doi.org/10.1038/s43588-026-01058-x. Source scientific method: initial generative model and agentic synthesis; *numerical calculated formation energies* r2SCAN-D4 first-principles and MACE-OMat-D3 ML-interatomic potential are NOT experimentally measured formation energies, PXRD or synthesis yields. Original manuscript on arXiv 2504.14110 was available April 2025; Nov publication date is journal, not first theoretical introduction. The journal does report independently successful synthesis of FOUR specified crystals; those specific lab PXRD files were NOT analyzed in this rotation.

Primary full original source DATA actually fetched via connected GitHub action:
https://github.com/tjaffrel/mofgen/blob/v1.2.0/data/figure_source_data/Figure3d_formation_energy_MOFGen_DFT.csv
- author GitHub release `v1.2.0` (release dated 25 July 2026, earlier than final journal publication), `README.md` and `data/figure_source_data/README.md` already read and verified XH ROT010.
- Full CSV **698,814 actual text bytes; 7,784 lines including header; 7,783 data rows**, Git blob SHA **fe13cc6c7262c5fe6883ee17664cd528c482a630**, content direct connected GitHub original `fetch_file`. All calculations below ACTUALLY EXECUTED in isolated V8 JS on full source text, not inferred from summaries. Re-read at frozen release v1.2.0 for independent first and second consistency passes.
- Header: `mof_id,formula,formation_energy_eV_per_atom,energy_eV,method,space_group`.
- Methods: `MACE-OMat-D3` **3,848** rows (machine-learned interatomic potential; NOT DFT); `r2SCAN-D4` **3,935** rows (DFT). All 7,783 energy/atom and total energy fields parse finite. The file name `...DFT.csv` does NOT make every method in it DFT.
- Important journal scope: manuscript states DFT optimization progressively PBE-D4 -> r2SCAN-D4 and pre-relaxation with **MACE-OMat-D4**, yet CSV at release v1.2.0 labels corresponding surrogate group **MACE-OMat-D3**. Do not silently normalize or claim these are identical Hamiltonians, energies, or dispersion corrections: `MACE_D3_VS_ARTICLE_D4_METHOD_LINEAGE_HOLD`. The absence of an explicit parity confirmation DOES NOT prove source error.

## 1. Actual paired analysis using original numerical records

To avoid spurious population comparisons, strip only the known TERMINAL method suffix `-MACE-OMat-D3` or `-r2SCAN-D4` from each `mof_id`; pair rows if and only if resulting identifier exactly matches.

Unique method-free IDs: **4,002**. Exactly **3,781** paired IDs have one result from each method. **67** IDs present MACE only and **154** r2SCAN only. The pairs represent same generator-assigned ID, **NOT independently verified identical relaxed atomic coordinates**.

Define each signed per-ID numerical difference in eV/atom:
`delta_i = Eform_i(MACE-OMat-D3) - Eform_i(r2SCAN-D4)`.

Executed actual full-row summary:
- **mean delta = -0.04346515576725726 eV/atom** (or -43.465 meV/atom);
- **median delta = -0.042013999999999996 eV/atom**;
- standard deviation of per-ID deltas = **0.029891743699830272 eV/atom**;
- 5% trimmed mean = **-0.04317691259447533 eV/atom**, scarcely changed by tails;
- Pearson correlation of paired formation energies = **0.9857851450128623**;
- MACE has numerically lower value for **3,513 / 3,781 pairs** (92.91%);
- **1,479 / 3,781** pairs have absolute difference >0.05 eV/atom; **149 / 3,781** >0.10 eV/atom.
- Formation-energy sign contingency on pairs:
  * both negative: **3,534**;
  * both positive: **107**;
  * MACE negative while r2SCAN positive: **140**;
  * MACE positive while r2SCAN negative: **0**.
  Check total 3534+107+140+0=3781; there were no exactly zero values within matched rows.

These signs **do not by themselves establish thermodynamic convex-hull stability/instability**: negative elemental formation energy can coexist with decomposition into more favorable competing phases, and the methods can have DIFFERENT energy reference conventions.

**Nature of statistical insight**: Very high per-ID correlation coexists with a systematic signed *source-file* shift and 140 zero-crossings. This is a model/metric parity control, not measurement of machine-learning prediction bias against ground truth. The DFT result is a different approximate computational method, not an experimental truth.

## 2. Non-IID family and robustness analysis

The base IDs encode e.g. `C48H18N12O19Zn4-1_5`: strip text after first hyphen to build a **chemical-formula-prefix family**. It is a grouping proxy based on source label, not crystallographic phase/relaxed composition proof.

Paired records partition into **497** families (sizes 1..63). For each family compute mean numerical delta:
- **474 families have negative family mean**, **23** positive family mean.
- equally weighted average of family means = **-0.04600971427122483 eV/atom**;
- median of family means = **-0.044800075 eV/atom**;
- 5% and 95% family mean delta quantiles = **-0.098360964** and **-0.00048230666666667163 eV/atom**.
- Largest family contains 63 paired structures; therefore individual record independence assumption is questionable.

Original deterministic **2,000 replicate nonparametric cluster bootstrap** (seed 20261122, xorshift32 RNG), draw 497 family clusters *with replacement* and include each selected family's ALL pairs. Each bootstrap replicates aggregate record-weighted mean:
`percentile 2.5% = -0.04782976375869544`,
`percentile 97.5% = -0.03911759263824743 eV/atom`.

These are a **descriptive sensitivity/robustness interval to family resampling from finite computer-generated database**, and NOT:
- a confidence interval for the physical truth of formation energies;
- an uncertainty interval for MLIP-vs-DFT predictive accuracy;
- a calibrated experimental measurement.
The strongly negative finite-sample shift survives family resampling, but the entire source energy calibration/geometry equivalence remains unresolved.

## 3. Source-schema / exact method provenance warnings, no unverified error claim

Actual original CSV metadata:
- In ALL 3,848 MACE records, column `formula` equals `mof_id`, therefore includes method suffix and cannot be used literally as a canonical chemical formula without parsing.
- In **586** of the 3,935 r2SCAN rows, `formula` similarly equals `mof_id`; most other r2SCAN rows use chemical formula strings.
- This is a **field hygiene and composition-parsing** warning. It is NOT proof that source chemical compositions or actual final structures are wrong. Metadata semantics vary within dataset.

**Original paper QHarden description** labels MACE pre-relaxation with D4 while in tagged CSV author deposited MACE-OMat-D3. The author repository release was public July 2026 and the revised journal came November. A real method-version lineage would need exact original atomate2 calculator configuration and per-ID atomic structures, reference energy convention and any de-dup/relaxation history. No such verified correspondence obtained; do not call it scientific misconduct/bug or claim any MACE accuracy error.

Two-surface prior art:
- mature foundation: DFT vs ML interatomic potentials, PBE(+U), r2SCAN+D4, energy referencing and convex-hull stability; 2022 computational formation-energy mixing methods with explicit energy reference adjustments: Kingsbury et al., "A flexible and scalable scheme for mixing computed formation energies from different levels of theory" npj Computational Materials (2022), DOI https://doi.org/10.1038/s41524-022-00881-w.
- closest specialist original: MOFGen authors' 2025 arxiv 2504.14110 and 2026 Nature Computational Science journal, source code and July v1.2.0 CSV; also original research into MACE-OMat and MOF potential benchmarking 2025–2026. New XH value = independently computed file-specific structure pairing, offset and robustness, **without claim of external theoretical or empirical firstness**.

## 4. Reproducibility, source hierarchy and deliverables

Files constructed in active response container:
- `xh_s7_rot015_mofgen_pair_audit.py` — 6,294 bytes, SHA256 `7a61e708f6a7d066596994ea3015a0cc19565c362c792e9633c3703922507ecf`; pure-standard-library Python script pinning URL to original release, verifies Git blob hash, uses suffix ID pairing, family resampling and JSON receipt. Local run against *synthetic 2-pair fixture* PASSED. This Python script was **NOT RUN against the original CSV**, because source data were read and numerically processed by GitHub-connected V8 isolate, not mounted into local filesystem. It can obtain the original CSV over network on a user's reproducible Python environment.
- `xh_s7_rot015_mofgen_pair_audit_receipt.json` — 3,689 bytes, SHA256 `b54a65195c3ccfa61d745a8b11005b8d60644a59e8af8d5a3c461977c9c75de7`; full source counts, fields, numerical receipt, caveats.
- `xh_s7_rot015_fixture.csv` — 318 bytes, SHA256 `fe8e00d92464658e753bd93d5394138cd7c85b94f28ab28c306584822b731b29`; locally executed independent fixture (two pairs, mean -0.04 eV/atom and one sign flip) verified script parsing/pairing against its own synthetic data.

Source factual access ladder:
1) MOFGen journal source original HTML/abstract/methods source READ as indexed, journal four AI-MOF syntheses AUTHOR REPORT only.
2) Full original deposited FIG3D CSV source bytes **ACTUALLY READ** (698,814) through exact GitHub v1.2.0 tag with recorded blob SHA, all 7,783 rows data processed natively (no summary-only data);
3) Actual paired numerical/robustness analyses **ACTUALLY EXECUTED** in connected runtime using original source values;
4) local reproducibility Python script **TESTED FIXTURE** but not re-run on original source due network restriction — separate execution status;
5) never fetched or analyzed the MOFGen Fig4 experimental PXRD binary, no model retraining, geometry optimization, source energy reference code, or wet-lab synthesis.
6) Sci SiC DaRUS archive is publicly indexed but inaccessible underlying bytes: explicit DATA_ACCESS_HOLD.

Exactly distinguish `AUTHOR_SCIENTIFIC_CLAIM` vs `AUTHOR_REAL_NUMERIC_DATA_READ` vs `INDEPENDENT_NUMERIC_SOURCE_DERIVATION` vs `PHYSICAL_VALIDATION`.

## 5. Research decision and negative knowledge

**Useful external scientific result**: In one actual versioned deposited MOFGen 2026 dataset, different levels of computation show strong concordance (r≈0.9858) yet substantial numerical systematic *file-level* offset and 140 sign differences across 3,781 matched labels. This is a strong, concrete source-interface discriminant demanding model identity, relaxed geometry and reference chemistry before collapsing calculations into one material selection or physical-stability claim.

Potential follow-up science (NOT launched by XH): obtain exact MACE-D3/D4 calculator params and energy reference metadata, verify whether MACE and r2SCAN represent same terminal geometries, compute reference-aligned formation-energy difference, compare to experimental diffraction or phase stability if comparable. If source ref adjustments remove the shift or geometry differs, the present descriptive comparison must not be interpreted as MLIP error, but source data summary remains correct.

No NASH-owned physical prediction, B1 work or separate audit role. No NASH "first" scientific result or method superiority inferred. No C1 restarting and no external author contact or journal error allegation. A public GitHub ROT report is not proof of BW ingestion or independent reviewer acceptance.

FINAL:
XH_S7_ROT015_ORIGINAL_FULL_7783_ROW_MOFGEN_CSV_SOURCE_READ_PASS /
SOURCE_NATIVE_PAIRED_3781_EXECUTED_PASS /
NATIVE_497_FAMILY_BOOTSTRAP_EXECUTED_PASS /
MACE_R2SCAN_ENERGY_REFERENCE_AND_RELAXED_STRUCTURE_IDENTITY_HOLD /
METHOD_LABEL_MACE_D3_VS_ARTICLE_D4_HOLD /
PURE_PYTHON_REPRO_FIXTURE_PASS /
SI_C_DARUS_ORIGINAL_LAB_DATA_BYTES_HOLD /
NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN.
