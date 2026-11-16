---
artifact_id: IW_MECH_S9_ROT029_T1_PREREG_001_PREEXEC_OUTPUT_GRID_ERRATUM_002_20261116
date: 2026-11-16
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
status: PREEXEC_ERRATUM_FROZEN / NO_GENERATOR_EXECUTION_AT_DOCUMENT_CREATION
predecessor_prereg: https://github.com/wmakiela-tech/Nash-iw-research/blob/c896351e537d79c401eee9a36a80cfac3a47f19d/research/mech-s9/2026-11-16/IW_MECH_S9_ROT028_B1_T1_ORIGINAL_BLACKHAWK_V23_FIVE_MASS_SOURCE_RATE_REPRO_PREREG_FROZEN_001_20261116.md
scope: SAME_APPROVED_MODERATOR_T1_ONLY
ceiling: NO_NEW_10D_JULIA / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRE-EXECUTION scientific erratum v002, source-grid only — prereg T1 unchanged on all discriminating gates

An important author-source typing correction was made strictly **before starting any of the five original BlackHawk T1 runs**. The prior prereg uses the phrase "z instantaneous_secondary_spectra.txt odczytać 100 energii E_i", conflating author config `E_number=100` **PRIMARY input** energies with `nb_fin_en_pythia=500` **SECONDARY output** energies. Original author 10D source-producing notebook `valid_hadrons_from_BlackHawk.ipynb` Git blob `8a10396ae771b17059808fc2b91235dd194cba8d` sets 100 primary energies `Emin=5 GeV,Emax=1e5 GeV` for BlackHawk, but it explicitly integrates `inst_secondary_spectra["energy"]` returned by the original BBN PYTHIA table provider. Original BlackHawk v2.3's `src/tables/hadronization_tables/infos.txt` defines the FINAL table size `nb_fin_en_pythia=500` as an independently specified value, distinct from `nb_init_en_pythia=250` and `E_number=100`. Source `BlackHawk_inst.c` writes `instantaneous_secondary_spectra.txt` from `final_energies`, not primary `energies` (the original author code patch Git blob `f517b0a71a3c994e396600ce73cb9658e440d646`). User's frozen original notebook correctly uses *all* output secondary energies.

**Correction:** `E_number=100` remains unchanged for **PRIMARY input**, while the postprocess trapezoid on the **SECONDARY output** must take exactly its provider-generated secondary-energy rows, expected 500, and their actual log-energy abscissae. Reject outputs with unexpected header or row count rather than truncating to 100. Use observed secondary energy values to calculate the mean `h` (no recalibration of quadrature). Exact source five channel keys `pipm,Kpm,K0L,proton,neutron` unchanged.

Everything that can influence T1 scientific verdict is fixed without modification: masses (100-table 0-based indices `[0,22,49,74,99]`), one exact original tar SHA, three author overlays, model PYTHIA BBN choice0, all five author reference columns/indices, **25 comparisons**, agreed `1e-5` maximal relative difference, group-vs-half-four-group branches, `T1-GROUPED/T1-PERSTATE/T1-NOREPRO`, unit conversion, build-type/HARDTABLES and active-old/current source-fingerprint requirement. No generated T1 numeric output was available before this erratum. The failure to distinguish primary and secondary axes in v001 is an internal prereg drafting error; this correction is a necessary source-faithful implementation, NOT a new hypothesis, optimized posthoc fit, extra permission or extra run.

Additional mandatory **runtime-identity check**: the exact author overlay `src/include.h` has literal `//#define HARDTABLES` (Git blob `3a1eaefd6d884c864056ea45233513493794ee7e`), i.e., not active unless another build layer defines it. The official source `src/hadro_pythia.c` uses `#ifdef HARDTABLES`. The T1 report must record the **effective compiler flags** and source table path selected by the actual C executable; never assume source text alone certifies final compiled configuration.

STATUS `T1_PREREG_ERRATUM_002_PREEXEC_FROZEN / T1_FIVE_MASS_AUTH_ONLY / T1_NOT_STARTED_AT_PUBLISH / NO_NEW_JULIA / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.
