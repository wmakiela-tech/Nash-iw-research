---
artifact_id: IW_REC12_ROT004_INT9_ROT031_WUXU_ACTUAL_PRODUCER_NOTEBOOK_FIVE_TO_SIX_SOURCE_NORM_I1_REFEREE_001_20261115
date: 2026-11-15
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_11 / REC12
mode: I1_NONBLIND_DIFFERENT_CELL_ORIGINAL_FULL_NOTEBOOK_SOURCE_STATIC_REFEREE
review_target: INT9_ROT031_ORIGINAL_WUXU_BBN_PYTHIA_PRODUCER_NOTEBOOK_AND_FIVE_RATE_TO_SIX_SOURCE_MAPPING
status: PASS_INT9_ORIGINAL_NOTEBOOK_PYTHIA0_PRODUCER_CODE_WITH_GUARDS / CONDITIONAL_CHARGE_NORMALIZATION_UNIDENTIFIED / B1_PHYSICAL_AND_NUMERIC_HOLD
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
ceiling: NO_NEW_BLACKHAWK_RUN / NO_NEW_NATIVE_JULIA / NO_ORIGINAL_BINARY_TABLE_REPRODUCTION / NO_EXTERNAL_I3 / NO_PHYSICAL_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# REC12 ROT004 — original Wu–Xu full producer notebook independently reviewed, with exact five-to-six source normalization guard

## 0. Source priority and one bounded review object

Single material referee target: independently falsify or confirm INT9 ROT031's primary-source result that the ORIGINAL archived author hadron-rate producer notebook intends PYTHIA at BBN epoch (choice0), produces the five named 100-mass input rate columns for the six-hadron-state 10D model, and leaves charge-conjugate output normalization unresolved. This review does **not** commission external provider work, re-run BlackHawk or revisit full 10D native Julia numerical correctness.

Original FIRST: Wu and Xu source and physics (JCAP02(2026)063), BlackHawk Arbey and Auffinger source and mature interface. LT8 ROT025 FIRST identified the PYTHIA/HERWIG historical dual-BBN table family and close 2026 heavy axion-BBN generator prior art. REC12 ROT003 independently confirmed the patched C dual-choice source interface and original Julia BBN setter with strict real-v2.3-table HOLD. INT9 ROT031 FIRST in current source-analysis line directly read FULL original notebook and established its intended choice0 producer source; PRF13 ROT025/026, KN14 ROT007 and SCOPE11 ROT008 contemporaneously inspected source table-to-ODE mappings. No priority reassignment or claim of newly discovered physics.

Original INT9 primary analyzed report: `Nash-Priv@1a515177647e97a4abbe4a4c1d3dab92227ca337/research/int9/2026-11-15/IW_INT9_ROT031_WUXU_BLACKHAWK_V23_ORIGINAL_NOTEBOOK_PYTHIA_BBN_PRODUCER_AND_FIVE_TO_SIX_CHANNEL_NORMALIZATION_GATE_001_20261115.md` Git blob `5911eb9bad7ea9a924c29ec2af3a233861611cd2`, DIRECT READ. Source-first independent REC12 conclusion below does NOT derive its predicates from this report: all evaluated on original author objects.

## 1. Original immutable sources DIRECTLY read

Frozen ORIGINAL author `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`:
- `arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb`: Git blob **`8a10396ae771b17059808fc2b91235dd194cba8d`**. DIRECT complete `fetch_blob` entire **1,675,240-character valid JSON**, 14 cells including original author code cells with stored execution_counts 1..10 and final stream statement documenting a saved file. Previous source browsing difficulty did NOT prevent this direct read. Notebook's embedded plotted images were NOT treated as numerical raw data.
- `arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c`: Git blob `f517b0a71a3c994e396600ce73cb9658e440d646`; original patched C branch `case 0:case1` at source lines532+.
- `arXiv-2509.05618/tool_script-BlackHawk_extension.jl`: Git blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`; setter at lines230–233; reader at261–287.
- `arXiv-2509.05618/main-scan.jl`: Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, source six-hadron injection equations 103–128.
- `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`: Git blob `06d0883a27b108692720422294ba2baacd381a64`, full original 100 numeric rows ×6 columns.
- Further primary Julia `tool_script-hadrons_from_PBH.jl` Git blob `cc73432910f872d526113ce59b6204f38d0766a9` confirms five log-log interpolated input rates (reviewed earlier REC12 turns).

## 2. Precise actual notebook code and its documentary execution ceiling

Original notebook cell8 (saved execution_count6) calls `BlackHawkParameters()`, `set_BlackHawk_energy_spectrum!(params,GeV(5),GeV(1e5),100)`, `set_BlackHawk_BBN!(params)` for a 5e9g benchmark. Cell9 (execution_count7) runs `run_BlackHawk_inst(params)` and reads instantaneous primary/secondary spectra.

Original CELL12 (execution_count9) defines `m_PBH_list=geomspace(1e9,4e12,100).*NU.g`; for each of the 100 mass values it makes fresh `BlackHawkParameters()`, sets primary grid 5..100000GeV with100 bins, explicitly calls `set_BlackHawk_BBN!(params)` BEFORE `run_BlackHawk_inst(params)`, then reads original instantaneous spectra. The original Julia helper's literal function body unconditionally assigns `hadronization_choice=0` = PYTHIA BBN. No notebook code cell selects HERWIG choice1. The original constructor DEFAULT choice2 is irrelevant once the notebook calls the BBN setter.

Cell12 integrates five secondary spectra using an E-weighted trapezoid in log E, using dictionary keys EXACTLY `pipm`, `Kpm`, `K0L`, `proton`, `neutron`. Cell13 (execution_count10) writes columns in EXACT order `charged_pion,charged_kaon,kaon_zero_long,proton,neutron` with the mass as first column, and its archived stream says `Saved hadron yields from PBH evaporation to data file.` Thus the archived notebook is consistent with a recorded successful execution of the intended PYTHIA BBN route, and the stored 100-row table has the same structure.

**Critical boundary:** an archived executed notebook plus table names does NOT authenticate that the original recorded run used the exact presently declared BlackHawk v2.3 tar/hack binaries, five PYTHIA source secondary table bytes, source tune or exact numeric mass-run output; no native reproduction was performed here. It is impossible to treat HERWIG choice1 as having been run.

## 3. A conditional K/KL source-mismatch allegation is NOT supported by actual notebook

The patched C BBN source slots0-based are 6:pipm, **7:K0L,8:Kpm**,9:proton,10:neutron. The five Wu–Xu scalar rate columns order is pi,Kpm,K0L,p,n, so naïve C slot [6,7,8,9,10] positional copying would swap Kpm and K0L.

But actual original Julia `read_BlackHawk_instantaneous_spectra` uses `secondary_spectra[secondary_spectra_header[ii]]=secondary_spectra_data[:,ii]`: it creates a **HEADER-KEYED DICTIONARY**, not a position-indexed five-column vector. Author notebook cell12 explicitly asks for `["Kpm"]` when calculating charged-K rate, and `["K0L"]` for neutral-K rate; the writer then puts charged-K before K0L by name. **Source-code mapping passes.** There is NO evidence of a Wu–Xu charged/neutral K swap from the observed different internal C array ordering. Actual C writer's physical payload labeling and raw `infos.txt` remain unverified; that separate question is not silently resolved.

## 4. Five source functions -> SIX native hadron states; exact unresolved normalization

Original `main-scan.jl` implements EXACT six direct hadron injection terms
`J=nPBH * (R_pi,R_pi,R_K,R_KL,R_p,R_n)` for state order
`(pi_minus,pi_plus,K_minus,KL0,antiproton,antineutron)`.
The 6x5 injection matrix is

```text
B = [[1,0,0,0,0],
     [1,0,0,0,0],
     [0,1,0,0,0],
     [0,0,1,0,0],
     [0,0,0,1,0],
     [0,0,0,0,1]]
```

with rank5. Each pi± state gets the ENTIRE SAME rate `R_pi` from a single original producer `pipm` column. The Kpm class is used to inject only the K-minus state; unsuffixed proton/neutron producer columns feed original ANTI-proton/ANTI-neutron states. This is exact code behavior, not proof that a physical grouping multiplier is wrong.

At original first source mass `M0=5.609588603804452e32GeV` (nominal 1e9g), five rates (natural GeV rate units) are
`(489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596)`.
Thus sum of Wu–Xu SIX source rates as literally injected per one BH is `1,135,908.9944317022` (before nPBH); exactly TWO pi entries account for `978,211.0252017162`. Under **one explicitly hypothetical alternate semantics** where the BlackHawk `pipm` column is BOTH CHARGES SUMMED, charge symmetry would assign HALF `R_pi` to each state, reducing this source-sum by `489,105.5126008581` = **43.0585121694% of literal six-rate sum**, holding other source rates fixed. If `pipm` is per charge, the literal code instead may be consistent. These are BOTH logically compatible with the FIVE scalar saved source table unless the original provider grouping convention is inspected. The number 43.06% is NOT a physical BBN prediction or an observed author error, and says nothing about signed neutron RHS after lifetime/interaction cancellations.

## 5. Actually executed independent referee static tests

A fresh V8 source-check program independently requested all five ORIGINAL GitHub files by frozen full commit/blob, parsed the complete notebook JSON and all 100 original table rows, and evaluated **23/23** positive original-source predicates PASS:
(1) 14 cells; (2) recorded notebook execution counts6,9,10; (3) original setter literal choice0; (4) benchmark BBN call; (5) loop BBN setter before run; (6) no choice1 in notebook; (7) mass grid 100 from1e9 to4e12g; (8) original primary energy5..1e5GeV 100; (9) BlackHawk run inside loop; (10) original secondary spectra read BY HEADER keys; (11) pipm source integrand and rate; (12–15) exact independent Kpm,K0L,proton,neutron keys in their respective **bounded source assignment blocks**; (16) author writer column order; (17) original table100×6 finite positive; (18) mass increasing and all five rates decreasing throughout source rows; (19) original table header matches writer; (20) original patched C BBN five slot labels; (21) original π− and π+ duplicate source term; (22) original four other ODE injection source terms; (23) recorded output writer stream.

Original single-line first test parser was overly narrow: it truncated assignment source expressions at the next newline and incorrectly produced three artificial source-key FAILs. The source parser was fixed to use full **field assignment regions** bounded by next field, and to verify all THREE occurrence instances of every field key. Only the corrected, actually executed 23/23 test run supplies this verdict; the prior helper's false negatives were audit-script faults, not upstream author evidence.

Five deliberate, separately evaluated negative tests all FAIL CLOSED, **5/5**: single wrong Kpm source integrand key; single wrong K0L source integrand key; removal of BBN mode setter from producer loop; mutation of second pion ODE injection; swap of the two header labels. These are tests of independently authored STATIC source predicates, not runtime tests of BlackHawk numerical software and not external I3. No packaged local source ZIP or binary reproduction asserted.

## 6. Exactly one next science gate; no task cascade

**Independent I1 verdict:** `PASS_WITH_GUARDS` for INT9 ROT031 actual ORIGINAL PRODUCER NOTEBOOK PYTHIA0 100×5 code path, named K/KL alignment, and five-source-to-six-state bridge. The full notebook is now directly read by REC12; no reliance on inferred execution from constructor default. Claims about a 2026 new physical effect, numeric PBH constraint, actual HERWIG parity and assumed factor-of-two actual error remain forbidden.

Physical B1 two-source input gate remains **HOLD_CHARGE_CONJUGATE_NORMALIZATION_AND_EXACT_BLACKHAWK_TABLE_BYTES**; original Julia native 10D BBN solver event/tolerance and owner approval remain **HOLD_NUMERIC_AUTH**. One read-only future source eligibility check—if capacity is explicitly assigned by source owners—is original installed BlackHawk v2.3 `infos.txt`, hadronization producer C generator conventions (per-sign vs two-sign), and actual PYTHIA/HERWIG five channel definitions under identical primary source. After that, not automatically, consider a source-matched five-vector rate comparison. No new run, no owner ACK, no BW native ingestion inferred by this public write.

Historical REC10 R09 false full-LOCC PASS/withdrawal and all project FAIL/HOLD remain intact.

**FINAL**:
`REC12_ROT004_PASS_WITH_GUARDS_SOURCE_NOTEBOOK_I1 / 23_OF_23_STATIC_SOURCE_GATES / 5_OF_5_FAIL_CLOSED_MUTATIONS / ORIGINAL_BBN_PYTHIA_CHOICE0 / NO_ACTUAL_K_KL_COLUMN_SWAP_PROVED / CHARGE_CONJUGACY_UNIDENTIFIED / REAL_HERWIG_TABLE_UNREAD / B1_PHYSICAL_NUMERIC_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / STOP`.
