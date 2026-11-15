---
artifact_id: IW_REC12_ROT003_LT8_ROT025_BLACKHAWK_DUAL_BBN_PROVIDER_SOURCE_CONTRACT_I1_REFEREE_001_20261115
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_11 / REC12
date: 2026-11-15
review_target: LT8_ROT025_PRIMARY_SOURCE_HISTORICAL_DUAL_BBN_GENERATOR_ELIGIBILITY
review_mode: I1_NONBLIND_INDEPENDENT_ORIGINAL_SOURCE_STATIC_CONTROL / SINGLE_BOUNDED_REVIEW
exposure: PUBLIC
science_class: ORIGINAL_BLACKHAWK_BBN_INTERFACES_AND_WUXU_SOURCE_WRAPPER_CONTRACT_ONLY
scientific_status: HISTORICAL_DUAL_TABLE_INTERFACE_PASS / EXACT_WUXU_WRAPPER_PYTHIA_ONLY_BBN_SETTER_PASS / REAL_V23_HERWIG_TABLE_BYTES_AND_RATE_COMPARISON_HOLD
sync_state: GITHUB_PENDING_BW_INGEST
guards: NO_NATIVE_JULIA / NO_GENERATOR_EXECUTION / NO_PHYSICAL_BBN_CONSTRAINT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_CASCADE
---
# REC12 ROT003 — referee of LT8 ROT025 BlackHawk dual-BBN source eligibility

## 1. Bounded question, priority, independent source reads

One material test only: does LT8 ROT025 validly identify an EXISTING original BlackHawk PYTHIA/HERWIG BBN five-hadron provider interface suitable to investigate before commissioning a new hadronization generator? Where does the exact ORIGINAL Wu–Xu author implementation stop supporting an executable comparison?

LT8 first primary-source/generator and close-prior-art discovery: `Nash-Priv@eb166e64b0f293ff1447313ab0fcfc3153e23681/research/lt8/2026-11-14/IW_LT8_ROT025_B1_EXISTING_BLACKHAWK_BBN_DUAL_GENERATOR_TABLES_AXION_2026_PRIOR_ART_AND_SOURCE_ELIGIBILITY_001_20261114.md`, Git blob `1986601004faaafd18c443a5b0002903413d6c95`, directly read. Earlier Wu–Xu FIRST physics/source; LT8 ROT024 first mass-band count decomposition, independently source-audited REC12 ROT002; earlier Mech-S9 original 10D source/native checks. This is a DIFFERENT source-availability / exact wrapper interpretation review, no firstness reassignment.

DIRECT PRIMARY HISTORICAL SOURCE:
- Arbey and Auffinger, *BlackHawk: a public code for calculating the Hawking evaporation spectra of any black hole distribution*, Eur Phys J C79 693 (2019), DOI https://doi.org/10.1140/epjc/s10052-019-7161-1. Its original published HTML Sect 4.6 `hadronization_choice=0` PYTHIA early-Universe/BBN, `=1` HERWIG BBN, `=2` new PYTHIA today; original TABLE 3 for BBN long-lived `tau>1e-8s`. Source original PYTHIA parton initial energies `5..100000GeV`; HERWIG `25..100000GeV`; explicitly warned extrapolation beyond table ranges not guaranteed.
- 2021 revised BlackHawk v2.0 manual PRIMARY https://arxiv.org/pdf/1905.04268 (2021 arXiv v3, *same historical original authors*, note numbering changes: analogous BBN content is TABLE IV, not Table III; original 2019 HTML Table 3 remains correct). 2021 source lists pi±,K±,KL0,p/pbar,n/nbar; present-epoch-only table excludes live mesons. The primary web PDF source text was read; screenshot request failed due provider cache, so no claim of successful image screenshot inspection. 2019 primary journal HTML independently supports presence/semantics.

DIRECT AUTHOR PUBLIC WU–XU SOURCE frozen `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:
1. `arXiv-2509.05618/README.md` Git blob `ea52003db19307c07b4164fd4144483752d21a32`: original code uses BlackHawk v2.3 and a bundled custom source *hack* copied atop its external distribution; original author JS/Julia code source native not substituted by historical 2019 BlackHawk source.
2. `arXiv-2509.05618/Artifacts.toml` Git blob `324cb54a6d2d1beca970931534345f589eb68c56` has original upstream URL `https://blackhawk.hepforge.org/downloader?f=blackhawk_v2.3.tar.bz2` and original recorded archive SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7` plus git tree SHA1 `80511176a03378517e15b705713256f686ce9016`. Archive bytes NOT downloaded or hash reverified here. The sha is source metadata, not our verification receipt.
3. `arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/src/include.h` Git blob `3a1eaefd6d884c864056ea45233513493794ee7e` line 108 explicitly documents v2.3 `hadronization_choice = 0` BBN PYTHIA, `1` BBN HERWIG, `2` today PYTHIA, `3` today HAZMA, `4` today HDMSpectra. L206-210 declares distinct Pythia/Herwig table readers.
4. `arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c` Git blob `f517b0a71a3c994e396600ce73cb9658e440d646` lines 532–546 and 581–593, DIRECT original read: EXACT shared `case 0: case 1` BBN index semantics with 11 secondary categories; hadrons exactly index6 pi±, 7 KL0, 8 K±, 9 proton, 10 neutron. Five hadron compute flags ALL `1` for both choices. `BlackHawk_tot.c` Git blob `76758e05a71688b94979b326723d02dbdf630dc5` independently has BBN `choice==0 || choice==1` with the same species mass channel layout (lines 546–557). This establishes a dual BRANCH/source index contract in the AUTHOR-PATCHED interface, not actual double-run numerical output or equal numeric tables.
5. `arXiv-2509.05618/tool_script-BlackHawk_extension.jl` Git blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`: `BlackHawkParameters` default `hadronization_choice=2` at line113 (TODAY), `set_BlackHawk_BBN!(params)` at lines230–233 **ASSIGNS 0 ALWAYS** (PYTHIA BBN), and `write_parameters` writes selected `hadronization_choice` to a source input file line164. `prepare_BlackHawk` lines 289–313 copies the upstream v2.3 artifact and overlays custom `*-hack` files before compiling. Thus the supplied BBN helper itself does NOT execute the HERWIG BBN path. To use HERWIG one must deliberately set 1 after the helper or otherwise control input, inspect exact table metadata, and validate source labels; NO code was edited or run by REC12.
6. `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl` Git blob `cc73432910f872d526113ce59b6204f38d0766a9` labels five original interpolation outputs by a fixed source table column order: pi, K, KL0, proton, neutron. Original `data/out/hadrons_from_PBH.dat` Git blob `06d0883a27b108692720422294ba2baacd381a64` same literal headers. A source header `proton`/ `neutron` is NOT a proof of separately charge-resolved anti-particle RHS weights; that mapping requires original RHS/input review.

## 2. Countercontrols and exact scientific status

**PASS historical interface**: five logically required BBN hadron groups and both PYTHIA and HERWIG table selection were specified by original BlackHawk and remain present as two explicit selection paths in Wu–Xu's own patched BlackHawk source. Hence insisting a brand-new generator must FIRST be written is unsupported; a lower-cost source table eligibility check is available.

**Source-level negative selection witness**: calling Wu–Xu's `set_BlackHawk_BBN!` on any params results in `choice=0` by its literal one-line body. The same function call **cannot** produce a HERWIG choice=1 experiment; the mere existence of `case 1` C branch is not a completed dual-generator control. This is a testable source logical fact, NOT an executed Julia control or source-provider numerical result.

**HOLD actual tables**: upstream distribution archive contents, exact installed version, two `infos.txt` records, generated file header metadata, energy-window coverage, table normalization and an actual per-channel rate vector were NOT directly read/run in this review. A source-code branch does NOT establish that the HERWIG table files are present or compatible in the authors' real environment, nor that resulting rates are physically credible.

**HOLD physical comparability**: original historical parton-energy grids differ at low E (PYTHIA 5GeV vs HERWIG 25GeV) and both top at 100TeV; need SAME Hawking quark/gluon emission weighting and explicit outside-common-range mass and parton-energy influence. T_BH=100TeV is NOT a sharp parton energy cutoff. Comparing two full generators modifies shower AND hadronization and tuning; generator spread is not a calibrated frequentist error bar. Hadron NUMBER-rate differences are not a BBN neutron/helium response or PBH constraints.

## 3. External 2026 originality guard (LT8 firstness preserved)

- Original *New bounds on heavy QCD axions from big bang nucleosynthesis*, Jung/Okui/Tobioka/Wang, Phys Rev D113 055002 (2026), DOI https://doi.org/10.1103/l2m1-h1cp, arXiv:2510.23695v3 (20 Oct2026), compares Pythia vs Herwig hadronic injection and BBN n/p, secondary hadron scattering; its latest v3 explicitly repairs Appendix C.2 and Eq(C24) cross sections without changing claimed headline. That paper studies *axion decay*, not a Wu–Xu PBH source, so transferable INPUT-INTERFACE precedent, NOT a transferable PBH rate/BBN uncertainty number. No NOVELTY for two-generator hadron-BBN method. Direct publisher paper and arXiv version metadata confirmed.
- Divisova/Myska/Sarmah/Siodmok *Herwig 7 with the Lund string model*, EPJC86 3 (2026), DOI https://doi.org/10.1140/epjc/s10052-025-15182-x, original publisher full article: Herwig angular-ordered shower with both cluster and Pythia Lund string via TheP8I is already mature prior art for controlled hadronization-model comparisons; no claim that this compiled interface is already in Wu–Xu v2.3 source/runtime. A normal PYTHIA vs HERWIG run is NOT such a shower-held-fixed experiment.

## 4. Referee verdict and single next gate only

- `PASS_LT8_ROT025_HISTORICAL_BLACKHAWK_BBN_DUAL_PROVIDER_DOCUMENTED`.
- `PASS_WUXU_V23_PATCHED_C_DUAL_CHOICE_SHARED_FIVE_SOURCE_CHANNEL_INDEX_CONTRACT`.
- `PASS_NEW_EXACT_JULIA_BBN_HELPER_PYTHIA_ONLY_SOURCE_CONTROL`.
- `HOLD_WUXU_ACTUAL_V23_TABLE_BYTES_AND_EXECUTED_HERWIG_RESULT`.
- `HOLD_B1_PHYSICAL_SOURCE_MAPPING_AND_NATIVE_NUMERIC_AUTH`.
- `NO_I3 / NO_EXTERNAL_BLIND / NO_NEW_NATIVE_JULIA / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.

ONE proposed low-cost owner-eligible check, NOT a new automated assignment: exact original Wu–Xu BlackHawk v2.3 artifact SHA and installed files for `src/tables/{pythia_tables,herwig_tables}/infos.txt` and five channels + an explicit BBN setting 0-vs-1 source input sample/readback; if physically available, align charge grouping and common parton energy support *before* any small rate-vector comparison. Stop on missing table, mismatched units/source status, missing exact input metadata, or unsupported energy range. No owner ACK or BW ING inferred from GitHub writeback. Historical R09 full-LOCC false PASS/withdrawal and other project negative knowledge unchanged.

REVIEW_LEVEL: `I1_NONBLIND_DIFFERENT_CELL_STATIC_ORIGINAL_SOURCE_REFERENCE_COMPARISON`; no numeric actual HERWIG data. REPORT is public source-typed review; not a runnable table archive.

END: `IW_REC12_ROT003_DONE / GITHUB_PENDING_BW_INGEST / ONE_BOUNDED_AUDIT_STOP`.
