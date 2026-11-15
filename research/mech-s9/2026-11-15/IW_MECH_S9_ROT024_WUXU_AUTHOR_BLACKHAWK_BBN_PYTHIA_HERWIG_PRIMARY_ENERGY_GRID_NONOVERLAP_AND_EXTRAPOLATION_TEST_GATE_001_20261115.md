---
artifact_id: IW_MECH_S9_ROT024_WUXU_AUTHOR_BLACKHAWK_BBN_PYTHIA_HERWIG_PRIMARY_ENERGY_GRID_NONOVERLAP_AND_EXTRAPOLATION_TEST_GATE_001_20261115
date: 2026-11-15
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_08 / Mech-S9
document_type: ORIGINAL_AUTHOR_SOURCE_PRIMARY_ENERGY_GRID_VS_RELATED_FORK_BBN_TABLE_SUPPORT_STATIC_AUDIT
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
scientific_status: FROZEN_SOURCE_READBACK / GEOMETRIC_GRID_17_OF_100_PASS / NOMINAL_TABLE_NODE_OVERLAP_4_AND_1_PASS / DECIMAL70_INDEPENDENT_PASS / NO_NEW_JULIA_OR_BLACKHAWK
claim_ceiling: AUTHOR_SOURCE_GRID_PLUS_RELATED_PUBLIC_FORK_TABLE_METADATA_ONLY / ORIGINAL_V23_TAR_NOT_BYTE_VERIFIED / NO_PHYSICAL_GENERATOR_ERROR_BAR / NO_CAUSAL_X_N / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S9 ROT024 — source-native Wu–Xu PYTHIA versus HERWIG BBN primary-energy grid support: 17 below-table source points and nominal 4/1 coincident nodes

## Question and precedence

B1 requires an ORIGINAL-source-matched physical hadronization comparison after correcting the numeric 10D solver and fully preserving source firstness. The original science/software is due to **Wu and Xu** and BlackHawk authors **Arbey and Auffinger**; this is a bounded read-only original-source consistency audit. Relevant PRIOR RESULTS from other project cells:
- **LT8 ROT025 FIRST** identified mature PYTHIA-BBN choice0 / HERWIG-BBN choice1 and the two source metadata lower energies **5 vs 25 GeV**, plus 2026 generator/BBN hadron chemistry prior art.
- **LT8 ROT026 FIRST** read real PYTHIA and HERWIG tables for five hadron groups in a public modified SUSY BlackHawk fork at a 10 TeV primary energy, preserving NOT-AUTHOR-V2.3 identity guard; direct generator numerics remain that cell's firstness.
- **INT9 ROT031 FIRST** read Wu–Xu's FULL 1.675 MB executed original producer notebook, validating choice0, the 100-point primary spectrum and all five column keys; REC12 ROT004 independently refereed it.
- **PRF13 ROT027 FIRST** independently read that notebook and related fork's sign-aggregated PDG counters, and contrasted per-initial-parton vs per-final-charge normalization. **Mech-S9 ROT023** independently calculated the six-source on-path conditionally rescaled RHS, explicitly noncausal and unverified.
- **KN14 / MT15 / PRF13 / REC12** own separate numeric source/event and entropy consistency gates.

ROT024's DISTINCT smaller result is a **quantitative grid-support and nominal tabulated-node-overlap audit** for the original author-producer default energy discretization if HERWIG were substituted, not a generator run or an assertion that a numerical bug exists. No new Julia, no BlackHawk execution and no physical hadronization model comparison.

## Exact frozen original author source and separate related public fork

Author Wu–Xu frozen source repository `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:
- ORIGINAL executed `arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb` Git blob `8a10396ae771b17059808fc2b91235dd194cba8d`. The full notebook was directly retrieved by GitHub fetch_blob; code cell 12 explicitly uses `set_BlackHawk_energy_spectrum!(params,GeV(5),GeV(1e5),100)` for 100 black-hole masses in `[1e9,4e12] g`, and `set_BlackHawk_BBN!(params)` selects **PYTHIA BBN choice 0**. No author HERWIG choice1 output observed in the notebook.
- ORIGINAL author patched `external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c` Git blob `f517b0a71a3c994e396600ce73cb9658e440d646`, lines 416–418, defines exactly `E_j=10^(log10(Emin)+j*(log10(Emax)-log10(Emin))/(E_number-1))` for j=0…99.
- ORIGINAL `tool_script-BlackHawk_extension.jl` Git blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818` selects choice0 despite constructor default2 (present-epoch).
- ORIGINAL `Artifacts.toml` Git blob `324cb54a6d2d1beca970931534345f589eb68c56` pins the standalone external `blackhawk_v2.3.tar.bz2` SHA256 **`dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`**. We DID NOT obtain/rehash this tar; source patched C and notebooks do NOT establish its binary identity.

**CRUCIAL DISTINCT PROVIDER:** modified related public BlackHawk fork `michellekwok2/blackhawk_SUSY@534441d7884fd570124ecbe3abcf031c16434043`, **NOT** authenticated as Wu–Xu's v2.3 tar:
- fork `src/tables/hadronization_tables/infos.txt` Git blob `efa9dd0af8a27a71388bae8f7760018610f8197a`: PYTHIA BBN initial primary table energy `[5,100000]` GeV with **250** logarithmic nodes; HERWIG BBN initial primary table `[25,100000]` GeV with **100** logarithmic nodes; distinct secondary table sizes 500 vs 100.
- fork `scripts/pythia_scripts/formatting.c` blob `f89bf329e3316ff472b61ac4f51c23084fbb6970`, `scripts/herwig_scripts/formatting.c` blob `829780acdcbca6bb97e9f0a1d55aeda5911e6b4a` explicitly use logarithmic primary grid generation at those quoted endpoints.
- fork `src/secondary.c` Git blob `c5ce1cf2e4312877d8c22991568300c91b44de3c`, lines 789–900, for hadronization choice1 sets `lim_init_en=0,lim_fin_en=64` and handles `E_primary<initial_energies[lim_init_en]` by a **shifted first-table hadronization spectrum**, rather than treating that region as a normal in-grid kernel. This is a related-fork static source statement, **not proven about exact Wu–Xu original v2.3 tar**. It is also not the same as the author PYTHIA choice0 old table support.

## Exact finite-grid result — source metadata algebra, NO physics

For the original author 100-node primary grid, as directly defined in the author's patched C source,
`E_j = 5*(100000/5)^(j/99) GeV` for `j=0…99`.

Original (E_{min}=5) GeV, related-fork HERWIG (E_{min}=25) GeV:
- Original j0…j16 are all BELOW HERWIG's table, **17/100** original primary energies.
- Original j16 `E=24.779124812801886 GeV`; j17 `E=27.386132854786407 GeV`; crossing occurs at noninteger grid index `j*=16.08871142471148`.
- Of **99** original adjacent primary log-energy intervals, **16** are wholly below 25 GeV, **one** straddles 25 GeV and **82** wholly above 25 GeV.
- The range [5,25) is **16.25122366132473% of the total LOGARITHMIC ENERGY AXIS**, NOT 16.25% of particles, Hawking energy, hadron number, temperature, reaction RHS or BBN endpoint.
- The nominal logarithmic Wu–Xu grid has only **four** matching PYTHIA grid nodes: zero-based `[WuXu j,Pythia k]=[(0,0),(33,83),(66,166),(99,249)]`; nominal HERWIG grid only **one** matching node, `(99,99)`, at 100,000 GeV. Match defined at <1e-12 absolute log energy distance. The related-fork table files serialize rounded energies, so this is a statement about NOMINAL generator grid definitions, not bytewise equality of all table file energy tokens. Pythia and Herwig interpolation for other nodes is expected, NOT per se a defect.

Thus **simply flipping choice0→choice1 with original [5,100000] author grid** would include 17 primary energy grid points in a related-fork HERWIG *lower-energy extrapolated* branch; even the same 100-node count does NOT imply matched numeric primary-energy nodes. This is a **design/identifiability warning** and not evidence of a quantitatively significant effect without primary spectral weights. Original producer already integrates its five channels over the primary energy domain; saved final `hadrons_from_PBH.dat` 100x5 rate data alone do NOT provide the source-resolved 5–25 versus 25–100000 GeV decomposition. Recovering actual fractions requires original per-energy spectra or rerunning an explicitly approved generator branch.

## Discriminating bounded future comparison — not authorized execution

Separate two contributions at identical mass and physically matched primary Hawking/greybody spectrum:
1. compare PYTHIA choice0 with HERWIG choice1 **on common input support 25…100000 GeV**, using one deliberately matched integration quadrature and explicit five-group charge mappings (pi±, K±, K0L, p/pbar, n/nbar);
2. separately measure the 5…25 GeV contribution in original PYTHIA and the *extrapolated* HERWIG low-energy treatment instead of attributing their difference solely to shower physics.

Do NOT silently change both `Emin` and `E_number=100` while attributing all variation to the generator; this also changes internal quadrature knots. Fix and publish original grid weights/overlap and all five output mappings before a generator spread claim. A source-verified analysis of actual original Wu–Xu BlackHawk v2.3 tar (hash above) remains the first fail-closed provenance gate. Also: original hadronization per-FINAL-charge vs per-PRIMARY-parton normalization has NOT been verified in exact archived tar; avoid factor-of-two physical-error assertion.

No actual author BlackHawk alternative, greybody-integrated hadron rate or full 10D `X_n(T0)` calculation performed in this rotation; the original source one-point numerical solver default mass-clock and evaporation stop inconsistencies and beta out-of-grid remain. Moderator individual native Julia permission not verified.

## Executed reproducibility and source-bound limits

Python3 stdlib source-metadata test actually executed and produced:
`mech_s9_rot024_wuxu_blackhawk_dual_mode_energy_support_contract.py` SHA256 `2ba1e103d9b2a4314612a19cf218c463fa174a3971a3e27b039081e1c92d3955`;
`mech_s9_rot024_wuxu_blackhawk_dual_mode_energy_support.json` SHA256 `069c9c23a7fd715aa2355b21a6154e028bc5df465462f31b898aa6ce0cb3c27d`.

Source parameter fixtures explicitly preserve upstream author and related-fork Git blob identities, but package does NOT embed raw original notebook / C source / binary table files or the original v2.3 tar; **no source-byte replay claim**. Four deliberate incorrect source fixture parameter controls fail closed. Independent Decimal70 calculation `j*=16.08871142471148003063647199` and fractional log domain `.16251223661324727303673204` agrees with JSON float. Isolated extracted source-script replay produces byte-identical result JSON. Self-contained conversation-local ZIP `mech_s9_rot024_blackhawk_dual_energy_support_REPRO.zip`, SHA256 `97552449ca6951de02bbf8212d6967868e9984011f9616d9ca1a682995e967be`, 6737 bytes, ZIP CRC PASS, **3/3 fixture payload SHA256 PASS**. No actual author tar or fork binary tables in this small package.

PROVENANCE: source Git URLs above and original tar SHA. The exact original v2.3 artifact has been unavailable to the project for direct content verification; a web search did not establish a second source whose bytes matched the pinned tar SHA. DO NOT promote public fork metadata to original v2.3 identity. No physical/source novelty, NO_CANON / NO_EXEC_SIGN / NO_PBH_BOUND / NO_NEW_JULIA / NO_BLACKHAWK_RUN / NO_TASK_CASCADE; this public GitHub file is not BW ingestion. 

**FINAL** `ROT024_AUTHOR_WU_XU_SOURCE_GRID_PASS / FORK_PYTHIA_HERWIG_BBN_17_OF_100_EXTERNAL_SUPPORT_EXTRAPOLATION_DIAGNOSTIC_PASS / GRID_MATCH_PYTHIA_4_HERWIG_1_PASS / DECIMAL70_PASS / AUTHOR_V23_TAR_SHA_HOLD / AUTHOR_CHARGE_NORMALIZATION_HOLD / B1_NUMERIC_HOLD / NO_NEW_JULIA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
