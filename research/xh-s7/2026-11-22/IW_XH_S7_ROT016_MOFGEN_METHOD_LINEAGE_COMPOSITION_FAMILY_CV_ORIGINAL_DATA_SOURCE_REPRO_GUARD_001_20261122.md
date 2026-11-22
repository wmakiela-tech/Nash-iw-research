---
artifact_id: IW_XH_S7_ROT016_MOFGEN_METHOD_LINEAGE_COMPOSITION_FAMILY_CV_ORIGINAL_DATA_SOURCE_REPRO_GUARD_001_20261122
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
date: 2026-11-22
function: EXTERNAL_SOURCE_NATIVE_SCIENCE / PRIOR_ART_TWO_SURFACE / NEGATIVE_KNOWLEDGE / PROVENANCE_VALIDATION
exposure: PUBLIC
original_data_tag: tjaffrel/mofgen v1.2.0
source_csv_blob: fe13cc6c7262c5fe6883ee17664cd528c482a630
status: AUTHOR_ORIGINAL_SOURCE_PDF_TEXT_AND_CODE_DIRECTLY_READ / FULL_ORIGINAL_7783_RECORDS_PROCESSED_IN_CONNECTED_JS / FORMULA_FAMILY_CV_EXECUTED / OFFLINE_PYTHON_SCRIPT_FIXTURE_ONLY_PASS
claim_ceiling: ORIGINAL_RAW_COMPUTATIONAL_DATA_DESCRIPTIVE_ANALYSIS_ONLY / GEOMETRY_AND_ENERGY_REFERENCE_UNCONFIRMED / NO_CONVEX_HULL_CERTIFICATION / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT016: Original MOFGen scientific-method provenance, family-blocked composition falsifier and a reproducible source-typed guard

## 0. Scientific scope and governing claim

Date of execution 22 Nov 2026 (after XH ROT015). Human Moderator's last explicit role directive: "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji." "O" instructs next independent bounded XH external research rotation. XH does not duplicate internal NASH B1/BBN numerical owner operations or claim novelty by cross-domain analogy. This work continues one precise EXTERNAL open-source empirical-computational finding from ROT015: paired MACE-OMat-D3 and r2SCAN-D4 formation-energy numerical shift, where source calibration, identity of structures and the model's actual dispersion variant were not established. ROT016 prioritizes *falsification and interpretation boundary*, not merely re-counting rows.

PRIMARY publisher peer-reviewed paper: Théo Jaffrelot Inizan et al. "System of agentic AI for the discovery of metal–organic frameworks", **Nature Computational Science** 6 (2026) 1223–1234, published **20 Nov 2026**, DOI https://doi.org/10.1038/s43588-026-01058-x ; the underlying preprint arXiv:2504.14110 originally submitted **18 Apr 2025**. Primary Nature PDF **actual original text was retrieved** at https://www.nature.com/articles/s43588-026-01058-x.pdf using web open, method lines and full Fig3 caption verified; requested PDF screenshot page3 returned CACHE MISS. Therefore source text verified, NO claim independent PDF visual figure inspection / screenshot, no original instrument imaging. Publisher indexed article independently searchable and explicitly distinguishes true Fig3d r2SCAN result from multi-method source data.

## 1. Original author code lineage: THREE DIFFERENT method labels and stages, not interchangeable

Original paper QHarden (§Computational details, Nature paper PDF 2026):
- QForge low-level pre-screening: MACE-MP-0 MLIP (source paper methods), and GFN-xTB; zeo++ porosity validity constraints.
- Higher-level QHarden initial pre-relaxation is described as **MACE-OMat-D4**, followed by geometry optimization **PBE-D4** and **r²SCAN-D4** with VASP. r²SCAN-D4 forces <=0.05 eV Å⁻¹. Paper Fig3d caption explicitly says **formation energy computed at r²SCAN-D4 level** versus Materials Project — it does **NOT** claim that paired MACE/r²SCAN formation energy error was independently validated.

ORIGINAL Github v1.2.0 files DIRECTLY READ:
- `agents/agent_4_qforge/mof_discovery.py` Git blob `b9173090a3e87d4e465e77045f0a61682747f62a`: source constructor `ForceFieldRelaxMaker(force_field_name=MLFF.MACE_MP_0, calculator_kwargs={"default_dtype":"float64","dispersion":True})`; this is specifically QForge stage, not an executable specification for original QHarden MACE-OMat-D4. It does NOT prove the paper uses the same calculator under another name.
- `agents/agent_4_qforge/mof_modeller.py` blob `7641bd5f5cac8fa8da5c3e112896fd3d6ff6a646`: wrapper executing QForge/zeo++ and MACE relaxations.
- `dft_analysis/plot_formation_energies.py` blob `b9c31c4716352b087d6ce7bcc11119725123b5c3`: source plotting of precomputed `mof_final_structures.json.gz` and `unary_energy_per_atom.json.gz`; both required original numeric ingredient datasets explicitly "NOT included in repo", preventing verification of elemental reference convention from this checked-in plotting code alone. No evidence these reproduce exact Fig3d source CSV directly; script specifies a supplementary Fig S3d from 2025 preprint.
- `scripts/mp_data_extraction.py` blob `26c3c23d0ac52001d258ed7d4c2f27e9e59ed940`: source MPContribs `MOFGen_2025` data downloader requires authenticated MP_API_KEY; not run. This is the cited primary export source for Fig3d CSV in data README.
- `scripts/mp_reference_data.py` blob `d59dfa62b797395e56fce09a1a58595410e1cc53`: **material executable reproducibility guard**. `formation_energy(thermo_type,elements,output)` sends `kw={fields:material_id,formula_pretty,formation_energy_per_atom, elements?}` to `mpr.materials.summary.search(**kw)`, but does NOT supply `thermo_type` nor `thermo_types` criteria. It only writes `reference = f"Materials Project ({thermo_type})"` in each output row. Therefore executing `--thermo-type R2SCAN` **DOES NOT ENFORCE R2SCAN-ONLY RESULTS BY THIS UTILITY SCRIPT**. Note the fact is about static source control/data-label semantics, not proof the authors' original final Fig3d plot was produced using this script. Correct MP query semantics: explicitly select thermo collection or appropriate mixed-thermo specification; original MP docs https://docs.materialsproject.org/downloading-data/using-the-api/querying-data ; https://docs.materialsproject.org/downloading-data/using-the-api/examples . No raw MP reference query launched and no rate estimates for actual mixed results.
- `data/figure_source_data/README.md` blob `ba18ac8a0243f80c104440521b00dee353d60dbe`: calls Fig3d "full MOFGen DFT set (7,783 MOFs: 3,935 r2SCAN-D4 + 3,848 MACE-OMat-D3)". **This file contains 7783 ENTRIES across TWO methods, not 7783 independently verified r2SCAN DFT calculations**. Article data availability references "DFT-computed database of 7,783 MOFs"; do NOT assume the public Fig3d CSV exhausts the underlying MPContribs DFT database or that its count label is entirely incorrect. The public **file's** method segmentation is unambiguous, author underlying database may have additional raw provenance.

These source labels form an unresolved pipeline map, NOT one automatically contradictory "model bug":
`QFORGE: MACE_MP_0(+dispersion) -> QHARDEN: claimed MACE-OMat-D4 pre-relax -> PBE-D4 -> r2SCAN-D4`
while **Figure3d source CSV** exposes `MACE-OMat-D3` and `r2SCAN-D4` rows with stripped-pair IDs. Neither atomic positions/geometry identity nor the MLIP elemental reference convention have been source verified. Source's full dataset (178189 candidate structures) Zenodo DOI https://doi.org/10.5281/zenodo.18452718 is public but BYTES NOT OBTAINED. No model run or source calculation reproduction.

## 2. Direct raw source-data numerical test, repeat pinned

Original authors' full source file actually read through connected Github action and processed directly in isolated JS runtime:
`tjaffrel/mofgen@v1.2.0/data/figure_source_data/Figure3d_formation_energy_MOFGen_DFT.csv`, original blob SHA `fe13cc6c7262c5fe6883ee17664cd528c482a630`, 698814 ASCII bytes / 7783 CSV rows / methods 3848 MACE-OMat-D3 + 3935 r2SCAN-D4. Strip only trailing `-MACE-OMat-D3` or `-r2SCAN-D4` from `mof_id`, get 4002 source base IDs, 3781 pairs, 67 MACE-only and 154 r2SCAN-only.

Signed numerical definition `d_i = E_form(MACE-OMat-D3) - E_form(r2SCAN-D4)`, unit eV/atom. Direct results (also previously XH ROT015, repeated):
- sample mean `-0.04346515576725726`, median `-0.042014`, SD `0.029891743699830272`;
- paired Pearson `r=0.9857851450128623`, 3513/3781 have MACE numerically lower; 140 have MACE negative and r2SCAN positive.
**These are raw source-file NUMERIC COMPARISONS, NOT prediction error relative to experimentally established ground truth.** Signed energy and method mismatch do not identify which method is better.

## 3. New formula parser normalization check: independent chemical formula coverage bounded to 3349

Each base ID starts with integer chemical formula e.g. `C48H24N24O10Zn4-0_1`. The DFT `formula` field sometimes is e.g. `Zn2H12C24N12O5` (reduced cell relative to ID), and sometimes contains grouped expressions e.g. `Zn4H20C48(N4O3)3`. XH implemented exact simple parser for elements, integer multipliers, parentheses and reduced formulas, and executed on original full 3781 pairs.

- `3349/3781` pairs contain a separately stated **actual chemical composition** in r2SCAN `formula` rather than its own `mof_id`. ALL 3349 match reduced composition from base ID after accounting for stoichiometric cell reduction and grouping.
- `432/3781` pairs have r2SCAN `formula == mof_id`; source's formula field is a placeholder and provides **no independent chemical composition check**. Matching on ID here is tautological.
- Across all paired IDs, canonical parsing of source ID and defined/stated r2SCAN field succeeds, 0 mismatches; but report the caveat correctly as `3349 INDEPENDENT FORMULA CHECK / 432 FALLBACK`, not `3781 INDEPENDENT FORMULA VALIDATIONS`.
- ALL 3848 MACE rows have `formula==mof_id` and therefore no separately stated formula; 586 r2SCAN rows (including unpaired) also have placeholder. This is a source-schema hygiene issue, not proof chemical structures differ or impossible formulas.

Composition match is necessary for comparison but NOT sufficient to guarantee same optimized atomic geometry, identical exchange-correlation functional, consistent reference elemental chemical potentials or thermodynamic convex hull status.

## 4. NEW quantitative discriminant: composition-family explains a dominant share of the in-file method difference

Group 3781 pairs into 497 `family` classes by the formula prefix before the first dash of the base ID. Decompose sum of squared differences around global mean into between-family and within-family component (one-way ANOVA algebra, no "causal" model):
- total delta SD 0.0298917437 eV/atom;
- BETWEEN-family share of in-sample total variance **0.9035040140590636 (90.3504%)**;
- WITHIN-family share **0.09649598594093735 (9.6496%)**;
- pooled within-family SD **0.009962084002030733 eV/atom** across 323 families with ≥2 matched pairs (3607 matched pairs); remaining 174 family groups singletons.
- negative mean difference in **474/497** families, positive in 23. This indicates substantial variation associated with composition/family labels; not proof that model discrepancy is CAUSED by composition or by an elemental reference misalignment.

NEW pre-defined-by-source deterministic **5-fold blocked out-of-family cross-validation**:
- input features `[1, C_atomic_fraction, H_fraction, N_fraction, O_fraction, S_fraction]`; F omitted (only ONE of 3781 matched formulas includes F), Zn fraction is implicit in compositional constraint. Linear fit with tiny 1e-10 normal-matrix ridge on nonintercept; folds assigned by FNV1a32 hash of complete base-family formula mod5; all structural variants within a formula family assigned to SAME fold.
- baseline for each fold = training-set MEAN difference, no composition. Five heldout fold sizes `606,786,693,909,787`, all 3781 pairs evaluated once. Aggregated heldout `RMSE_baseline=0.030508289780816586 eV/atom`, `RMSE_formula_model=0.015115864755389171 eV/atom`, `heldout_squared_error_reduction=0.7545119990452194 (75.4512%)`.
- Fold-level validation error reductions between ~71.2% and ~80.9%, each family held out from its fold's fitting.
- This means the NUMERICAL DIFFERENCE between two source data series is predictable from stoichiometry for unseen formula groups in this finite dataset, but not evidence of an identifiable physical correction, calibrated model accuracy, or real-world property prediction. Systematic method differences and elemental reference offsets are HYPOTHESES, not established mechanisms.

Crucially, a correction fitted to these source pairs may optimize the table while LEAVING geometries, elemental reference schemes or higher-level physical models wrong. NO post-hoc data repair or canon update is justified.

## 5. Closest published scientific prior art and correct stability quantity

**MATURE HOST A**: Density functional theory, energy formation referencing, mixing incompatible computational levels (Kingsbury et al., *A flexible and scalable scheme for mixing computed formation energies from different levels of theory*, npj Computational Materials 8,195, 2022, DOI https://doi.org/10.1038/s41524-022-00881-w). This explicitly establishes that material energy levels need reference alignment and mixed energy treatment; NASH/XH does not discover principle of reference mismatch.

**CLOSEST SPECIALIST B**: author's MOFGen 2025 preprint/2026 journal and contemporary MOF simulation benchmarks (MOFSimBench, npj Comput Mater 2025 DOI https://doi.org/10.1038/s41524-025-01872-3) provide actual MOF-specific calibrated modeling context (ML potentials, dispersion and non-equilibrium geometry). Importantly, 2026 JACS original peer reviewed work *Predicting the Thermodynamic Limits of Metal–Organic Framework Metastability*, DOI https://doi.org/10.1021/jacs.5c20253, analyzed computed phase diagrams >20000 MOFs and established **negative formation energy with respect to elements is NOT a reliable proxy for stability against competing phases**; appropriate quantity is decomposition/energy above convex hull with SAME compatible thermodynamic energy convention. This strongly limits physical "stability" interpretation of Fig3d negative values, independently from the inter-method numerical shift. Source DOI JACS and Materials Project phase diagram docs https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds .

Thus high correlation `r=.986`, mean delta `-.0435`, 140 sign crossovers and 90% family association do not prove compound can or cannot be synthesized, is stable against decomposition, or that MLIP matches experiment. NASH source-first negative knowledge needs preserve all these semantic distinctions.

## 6. Reproducibility artifacts, local execution and source ceilings

Locally created **genuine executable Python**:
`/mnt/data/xh_s7_rot016_mofgen_lineage_audit.py` 9.5KB (SHA-256 `54ddd3656d497f825554b67ad9a32dd17f85f82d71b47a28d89d6d63d22d87ae`). It provides an exact tagged Github source URL and Git blob SHA check; parses source CSV, handles full/factored grouped formulas, method ID pairing, source schema and family composition, tests composition cross-validation from source rows. Local `--self-test` fixture **PASS**, including grouped formula parser, but **Python script itself was NOT executed on full original CSV due network restriction**. Original full numerical input WAS INDEED directly processed and independently computed via connected GitHub JS tool. Full original source bytes in that tool are real and pinned, not inferred. Anyone with a copy of original tagged CSV or network can run `python xh_s7_rot016_mofgen_lineage_audit.py --input CSVFILE` or `--download` on a networked machine.

Result receipt `/mnt/data/xh_s7_rot016_analysis_receipt.json` SHA-256 `ce1b6a2799a4a106e6387cc609edcef22f87993d0252464123b491c01b841dbf`: exact source fields, counts, method code provenance, formula coverage, ANOVA and heldout CV.

SOURCE ACCESS LADDER:
1. Journal original PDF TEXT read, requested screenshot cache-miss. No direct figure pixels inspected.
2. Author Github original direct code and formula source inventory READ, git blobs recorded.
3. All 7783 original Figure3d CSV data rows READ & numerical calculations EXECUTED via connected JS.
4. Standalone Python reproduction script self-test PASS but NOT executed full source locally.
5. Author original elemental reference JSON files, final atomic coordinates, raw VASP/MPContribs task documents, and Zenodo 178189 candidate data BYTES NOT obtained. No truly independent physical calibration to experiment.
6. Author lab PXRD source data from Fig4 not downloaded. No external authors contacted.

Recommended next-source scientific discriminator (NOT automatically launch):
- pin each actual Fig3d MACE calculator checkpoint and D3 correction parameters vs cited QHarden D4, distinguish stage QForge/QHarden;
- obtain original `unary_energy_per_atom.json.gz` reference table and r2SCAN data source for same stoichiometric systems, plus per-ID final relaxed structures/cell multiplicities; verify both methods' elemental reference energy consistent;
- compute SAME-GEOMETRY matched single-point method difference vs independently relaxed geometry differences (two separate effects), then compare to heldout DFT/experiment;
- for thermodynamic synthesis, use properly mixed convex-hull/decomposition reference and source-native physical evidence rather than sign of E_form;
- if using MP reference helper, enforce actual thermo_type in API, and preserve provenance `SCRIPT_QUERY_NO_FILTER_PASS / FIGURE_INPUT_LINEAGE_HOLD`.

Research status `SOURCE_METHOD_LABELS_DISTINCT / ORIGINAL_RAW_CSV_PAIRED_FULL_AUDIT_PASS / FAMILY_BLOCKED_CV_PASS / 3349_INDEPENDENT_FORMULA_432_PLACEHOLDER / MP_THERMO_FILTER_UTILITY_MISSING / NO_SCIENTIFIC_PAPER_ERROR_PROVED / NO_CALIBRATED_PHYSICAL_PREDICTION / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN`.

No B1 native work, no C1 resumption, no owner mandates, no automatic external writeback beyond public GitHub source note. Public artifact `GITHUB_PENDING_BW_INGEST` does not imply independent referee acceptance or BW ack.
