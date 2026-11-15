---
artifact_id: IW_REC12_ROT005_LT8_ROT026_REAL_FORK_TEN_BBN_TABLES_INDEPENDENT_RAW_SUM_SOURCE_I1_REFEREE_001_20261115
date: 2026-11-15
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_11 / REC12
mode: SOURCE_FIRST / ONE_BOUNDED_I1_NONBLIND_DIFFERENT_CELL_REFEREE / FULL_ACTUAL_FORK_TEN_BLOB_DIRECT_READ
review_target: IW_LT8_ROT026_REAL_BLACKHAWK_FORK_PYTHIA_HERWIG_FIVE_HADRON_10TEV_TABLES_SOURCE_HASHED_AND_WUXU_V23_GUARD_001_20261115
result: PASS_ACTUAL_FORK_RAW_COUNT_SUM_10_OF_10 / PASS_FIVE_SPECIES_THREE_ENERGY_TWO_PRIMARY_RATIO_REPRO / HYPOTHETICAL_INPUT_PROVIDER_ONLY / ORIGINAL_WUXU_V23_TAR_AND_EXECUTED_COMPARATOR_UNVERIFIED
claim_ceiling: NO_BLACKHAWK_CODE_RUN / NO_NATIVE_JULIA_RUN / NO_HAWKING_GREYBODY_RATE / NO_BBN_XN_YCODE_Y_P / NO_PBH_CONSTRAINT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---
# REC12 ROT005 — LT8 ROT026 independently audited from all 10 REAL public-fork BlackHawk BBN raw data files

## 0. Referee object, provenance and firstness

Single question: did LT8 ROT026 actually obtain scientifically meaningful raw PYTHIA BBN and HERWIG BBN tables in an IDENTIFIABLY DIFFERENT public BlackHawk fork, and do its five hadron species P/H particle multiplicity ratios at primary parton energies 1, 10 and100 TeV follow from those original tables? Can that result be promoted to a physical Wu–Xu v2.3 rate/BBN result? Review is one bounded independent I1 source DATA audit; not an AI physics or theorem discovery.

Original BlackHawk authors Arbey/Auffinger FIRST published code and table architecture, original Wu–Xu FIRST PBH–BBN 10D source, original LT8 ROT025 FIRST in NASH recovered historical two-BBN-generator interface and contemporaneous heavy-axion BBN cross-generator prior art. LT8 ROT026 FIRST in this cell directly fetched all TEN real data table bytes from the named public SUSY fork and computed its specific five-species ratios. REC12 here independently reads original fork's ten actual Git blobs and computes its own diagnostic numbers; NO firstness transfer. Previous REC12 ROT003 checked Wu–Xu patched BlackHawk v2.3 C dual selection; ROT004 checked original Wu–Xu BBN-PYTHIA0 producer notebook and five rate→six-state charge normalization HOLD. Historical R09 full LOCC false PASS and all project HOLD/FAIL retained.

Owner original LT8 private report DIRECT READ `Nash-Priv@76b0e08dc6718856d439e681f793c459713fb046/research/lt8/2026-11-15/IW_LT8_ROT026_REAL_BLACKHAWK_FORK_PYTHIA_HERWIG_FIVE_HADRON_10TEV_TABLES_SOURCE_HASHED_AND_WUXU_V23_GUARD_001_20261115.md`, Git blob `a185c733a3078eca966cb5b0d4fc7da965120a44`.

**Fork, NOT original Wu–Xu 2.3 artifact:** `michellekwok2/blackhawk_SUSY@534441d7884fd570124ecbe3abcf031c16434043`. Distinct public fork has modified SUSY physics; these archived data are source evidence for the fork ALONE. Wu–Xu original `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d` Artifacts.toml declares a completely different original downloaded BlackHawk-v2.3 archive SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`; its actual bytes, exact tables, production tune and charge-group semantics remain unverified.

## 1. Primary source native ten Git blobs actually read BY SHA

Original fork source metadata `src/tables/hadronization_tables/infos.txt`, Git blob `efa9dd0af8a27a71388bae8f7760018610f8197a`, directly read. Pythia BBN initial-E 5..100000 GeV, 250 initial nodes×500 final bins; Herwig BBN initial-E 25..100000 GeV, 100×100; both declare 14 primary and 11 secondary channels. Original fork `src/secondary.c` Git blob `c5ce1cf2e4312877d8c22991568300c91b44de3c`, directly read: mode0 paths and mode1 paths under `src/tables/hadronization_tables/{pythia_tables,herwig_tables}`, source species C slots 6 pipm,7 K0L,8 Kpm,9 p,10 n. At source C lines121–133 the RAW count per final-energy bin is divided by bin width when constructing differential branching ratios dN/dE; hence SUM of original unconverted RAW count bins is correctly typed as integrated multiplicity per source primary entry, NOT a Hawking spectrum or a rate per time.

All ten real numeric file contents obtained via connected GitHub `fetch_blob(repository_full_name,blob_sha)`, not only metadata/fetch_file responses. Entire contents parsed; every numeric source row has exactly 16 columns (E_initial,E_final,14 primary species); source primary `up` column10 and `gluons` column3 (zero-based). NONNEGATIVE numerical counts, no malformed lines; 250×500=125000 data rows per P species and 100×100=10000 per H species, 5 each => **675000 REAL original source rows in total**.

| Secondary filename | PYTHIA raw Git blob | HERWIG raw Git blob |
|---|---|---|
| pipm.txt | b6e3e3a7fe8417db745fa805ac17826c6e17b762 | 7c56248ccfaa6e0430d605b75ed4e0a567fec613 |
| K0L.txt | 5e665fd51c49e33ec9eaf28de2d77d11b98a9132 | 75a8a2d76a435ba7b323d9f0cefc0204dd4d6c9e |
| Kpm.txt | 1ce7394991e4c596efe693c1803b2f5de8a75578 | bc8fe92cb561d92577624474d8e4d7ce5b8d303f |
| proton.txt | 912451b3b4a3fea63333fa4913328fbf4ef025e0 | 3898ea472c90d043e5f3933f1148338a08137e36 |
| neutron.txt | e35ba1cef35639fa5a0f306782628f39709b553b | 099eb0d04f863e2a8acbbf490bd283b08797e9fb |

These exact sha keys are source locators, not fabricated downstream checksum receipts. No complete 160MB+ source data archive was uploaded to public NASH or user container.

## 2. Independent mathematical source reconstruction

For every generator g, secondary species s, primary c (up or gluon), original tabulated primary E_i:
`Y[g,s,c,E_i] = SUM over all original final-energy bins j of RAW_COUNT[g,s, E_i, E'_j, c]`.
This aggregation uses raw species counts, without the C loader's additional final-bin-width division (that division is for dN/dE and would be inappropriate for RAW-count summation). Each grid is organized as repeated fixed initial energies with 500 or100 consecutive final bins.

For target E=1000 or10000 GeV between native initial nodes `E_l < E < E_h`, explicitly use this bounded LT8 diagnostic, independently coded in REC12:
`t = log(E/E_l)/log(E_h/E_l)`,
`Y(E) = exp((1-t)*log(Y(E_l))+t*log(Y(E_h)))`.
This is interpolation of the **already summed multiplicity**, NOT a promise it equals the published BlackHawk interpolation of the differential distribution or the final Hawking source. At E=100000GeV both P and H have an EXACT native final initial-energy NODE: no interpolation. P near 10TeV nodes [9957.58,10361.6], H [9577.13,10414.1], both native source grid evidence.

### Direct independent 10TeV results, primary *up* quark
| species | P raw count total interpolated | H raw count total interpolated | P/H (8dp) |
|---|---:|---:|---:|
| charged pi (pipm) | 58.0043963756 | 38.8122602103 | 1.49448643 |
| K0L | 3.3346984016 | 1.5239095116 | 2.18825224 |
| charged K (Kpm) | 6.8266481775 | 3.1264124577 | 2.18354049 |
| proton | 4.1975075147 | 2.0412857100 | 2.05630574 |
| neutron | 4.1443422360 | 2.0289942690 | 2.04255985 |

### Direct independent 10TeV results, primary *gluon*
| species | P raw total | H raw total | P/H (8dp) |
|---|---:|---:|---:|
| charged pi (pipm) | 106.3822743111 | 65.8891557893 | 1.61456423 |
| K0L | 6.2521825863 | 2.3903544739 | 2.61558805 |
| charged K (Kpm) | 12.6791210939 | 4.9229748868 | 2.57549985 |
| proton | 7.6946239446 | 3.2686570342 | 2.35406280 |
| neutron | 7.6644425154 | 3.1920108456 | 2.40113298 |

### Additional independent controls: up-quark P/H ratios at 1 and100TeV
| species | 1TeV (interpolated) | 100TeV (EXACT raw table node) |
|---|---:|---:|
| charged pi | 1.40683643 | 1.53829657 |
| K0L | 1.87037487 | 2.39187361 |
| charged K | 1.89253875 | 2.36857964 |
| proton | 1.87625033 | 2.18057877 |
| neutron | 1.82148657 | 2.19129649 |

Additionally all 15 gluon P/H source ratios (5 species ×3 energies) were independently evaluated from the actual ten source files, not assumed identical to up-quark ratios. For 1TeV P/H gluon in species order pi,KL0,Kpm,p,n:
`[1.58354501,2.42999586,2.40350171,2.21238593,2.25327944]`.
For 100TeV exact-node P/H gluon:
`[1.60793385,2.67411058,2.64122302,2.41406344,2.46352530]`.

**Result**: 10/10 direct tables parsed PASS, 15/15 up P/H diagnostic values and all 15 gluon P/H values independently recomputed from original source, LT8 ROT026 10TeV source figure 5/5 reproduced to displayed 8 decimal places. At 100TeV both tables' final source nodes are directly used, so it is specifically wrong to call those numbers an extrapolation outside the tabulated parton E range (but all >100TeV source is outside the table).

## 3. Referee falsifiers and physical-transfer ceiling

- Do NOT substitute the modified `blackhawk_SUSY` fork's real data for original `Wu–Xu BlackHawk v2.3`: binary/source SHA identity is not established, and the original BBN mode0 notebook's source table files are not verified as these fork bytes. Thus original Wu–Xu physical P/H five-rate generator comparison is **NOT DONE**.
- Do NOT compare 1.5–2.6 per-parton table P/H ratios directly with original Wu–Xu 5% paper-v-code PBH emitted-NUMBER difference: different definitions, mass trajectory and generator data. Raw per-primary yields require a full primary Hawking spectral convolution by primary species and energy, integration over SECONDARY energy, compatible per-sign and particle/antiparticle normalization and the same BBN energy/decay status before obtaining original 5 source R_h(M).
- Interpolation of scalar TOTAL multiplicities is a diagnostic operator, NOT source canonical BlackHawk output or a proof of native interpolation identity. The original P vs H native E_min are different (5 vs25GeV) and both E_max=100TeV, so common support/extrapolation and source energy weighting must be established to obtain physically meaningful generator differences. 100TeV is a primary-parton energy node, NOT a Hawking temperature-mass boundary.
- Fork C labels `pipm`, `Kpm`, `proton` and `neutron` do NOT resolve charge-conjugate grouping per source source and original 6x5 Wu–Xu native ODE injection matrix. The original per-charge convention remains HOLD, not a claimed factor-of-two bug.
- No new original 10D Julia run, BlackHawk program execution, live source physically generated X_n, helium-4 or PBH constraints in this rotation; public original GitHub original data were **read and mathematically reduced only**. No external blind I3.

## 4. Verdict, one gate only, custody

`PASS_WITH_GUARDS_LT8_ROT026_REAL_PUBLIC_FORK_TABLE_SOURCE_10_OF_10` and `PASS_SOURCE_RAW_COUNT_SUM_1_10_100TEV_FIVE_CHANNELS_AND_GLUON_CONTROL`.
`HOLD_ORIGINAL_WUXU_V23_BINARY_TABLE_IDENTITY`;
`HOLD_ORIGINAL_PYTHIA_VS_HERWIG_HAWKING_GREYBODY_CONVOLVED_FIVE_RATE_COMPARE`;
`HOLD_CHARGE_CONJUGATE_AND_BBN_NATIVE_NUMERIC_SOLVER_AUTH`.

Single appropriate owner-controlled next gate, NOT a task creation: SHA-pin original Wu–Xu 2.3 BlackHawk tarball and its actual installed BBN `infos.txt` and ten channel table payloads and check equality/inequality of the actual upstream production bytes with this modified fork. If exactly matched and scientifically eligible, separately authorize a small physical five-rate Hawking convolution comparison; if absent, label `HOLD_V23_PROVIDER_IDENTITY`. An authorized native 10D original-source solver run is a further distinct decision and needs its own numerical calibration. Do not generate a new broad search/audit chain merely from this pass.

This is public source-typed RECEIPT only. `GITHUB_PENDING_BW_INGEST`, no claim of native BW ingest, Moderator/owner adoption or executive sign. No science-canon promotion or new physics/theorem novelty.

RETURN_ID: `IW_REC12_ROT005_LT8_ROT026_PUBLIC_FORK_TEN_REAL_TABLE_RAW_COUNT_I1_REFEREE_001_20261115`.
FINAL: `REC12_ROT005_ONE_BOUNDED_I1_COMPLETED / 10_REAL_TABLE_BLOBS_READ / 675000_ORIGINAL_FORK_ROWS_VALID / FIVE_SECONDARIES_x_TWO_INITIAL_PARTON_TYPES_x_THREE_ENERGIES_RECHECKED / ORIGINAL_WUXU_V23_NOT_IDENTIFIED / B1_PHYSICAL_NUMERIC_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / STOP`.
