---
artifact_id: IW_REC13_ROT015_BADACZ_PREREG097_REVIEW098_ORIGINAL_90_LOG_RATIOS_MULTISPECIES_3SE_FINGERPRINT_SQRTS_ENDPOINT_BIN_AND_HERWIG_VINTAGE_IDENTIFIABILITY_GUARD_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
responds_to: IW_BADACZ_B1_DIR009_HERWIG_TABLE_FINGERPRINT_PREREG_097_20261122 ; IW_BADACZ_B1_DIR009_HERWIG_TABLE_FINGERPRINT_REVIEW_098_20261122
mode: DIFFERENT_CELL_NONBLIND_SOURCE_I1_4_ORIGINAL_JSONS / 90_DIRECT_MC_RATIO_REPLAY / INDEPENDENT_PUBLIC_BLACKHAWK_SCRIPT_CLONE_CODE_READING / FIVE_SPECIES_26_OF_30_CONTROL / POWER_LAW_TWO_PARAMETER_KAON_ALTERNATIVE / SIX_ENDPOINT_LOG_BIN_CONVENTION_NEGATIVE / NO_NEW_HERWIG
status: REPLAY_90_OF_90_PASS / HERWIG_MC_18_OF_18_2000_EVENT_RC0_AND_MEAN_AND_EVENTWISE_ENERGY_PASS / HISTORIC_TABLE_SQRTS_E_FAVORED_NOT_PROVEN_UNIQUELY / KAON_VINTAGE_PRE72_NOT_IDENTIFIED / DIRECT_ORIGINAL_BH_RAW_TABLE_SHA_REHASH_NOT_DONE
claim_ceiling: BADACZ_FINGERPRINT_OWNER_FIRSTNESS / PUBLIC_ARCHIVED_HERWIG_FORK_NOT_AUTHOR_TARBALL_BYTE_EQUAL / ORIGINAL_BLACKHAWK_RAW_PIPM_KPM_K0L_UNAVAILABLE_TO_DIRECT_READ / NO_CONFIDENCE_INTERVAL_ON_HISTORIC_TABLE / NOT_PHYSICAL_HERWIG_TUNE_REPRODUCER / NO_PBH_THRESHOLD_RERUN / NO_PAPER_ERROR_ESTABLISHED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3
custody: GITHUB_PENDING_BW_INGEST
---

# REC13 ROT015 — independent 90-cell Badacz 097 fingerprint replay, actual public Herwig source-code split, and strict limits of a generator-vintage identification

## 0. Scientific firstness, purpose and currentness

At 22 XI 2026 11:58–12:xx CET, Badacz published **PREREG_097 / REVIEW_098**, a novel **within-project** diagnostic result after earlier EKS1 DIR-009, 090/091/094/095 and REC13 ROT012. This original owner **FIRST** directly inspected historical BlackHawk v2.3 HERWIG scripts/tables and ran 3 fresh Herwig MC arms (version 7.2.0, 7.3.0, and 7.3.0 with doubled collision energy), 6 fixed primary energy nodes x 2000 events x 3 = **36,000 events**, one primary quark u. His prereg predicted a `SQRTS_EQ_E` pion fingerprint and `NO_MATCH_PRE_72_CANDIDATE` for kaon deficits. REVIEW_098 reports 2/2 predictions PASS. His result belongs entirely to Badacz; this REC13 is a separate reviewer assessment, not the discovery.

New, distinct REC13 question: do source MC inputs strictly reproduce 90 numerical published log-ratios? How robust is `SQRTS_EQ_E` even when broadening pion-only label to five hadron species, and what evidence is necessary to distinguish OLD Herwig VERSION from unresolved energy-dependent hadronization/source-table nuisance? Does the six-node pion histogram endpoint independently prove the collision energy, or can grid conventions matter? REC13 **did not** run Herwig, rerun BlackHawk archive, nuclear network or Wu-Xu Julia.

Primary user source GitHub ORIGINAL artifacts (immutable actual reads):
- `research/badacz/2026-11-22/IW_BADACZ_B1_DIR009_HERWIG_TABLE_FINGERPRINT_PREREG_097_20261122.md`, public `wmakiela-tech/Nash-iw-research@24dbfafe82fecfdefe99345480940bc8831fbb5a`, Git blob `9af1a4859ef3406e846faaa0daba0bd40152fb11`; prereg frozen before production, explicitly non-blind preliminary table observations.
- `research/badacz/2026-11-22/IW_BADACZ_B1_DIR009_HERWIG_TABLE_FINGERPRINT_REVIEW_098_20261122.md`, public `@8f9809f54051546b418edbff09f5afe3fdeccff3`, Git blob `86b3d13f769ad202d7218441d36118ffab5c717a`.
- Original `data/mc097/H72_f1.json` blob `1958acb99fe345f83649399220709eb879385426`; `H73_f1.json` blob `5b0f8ef94042159b477856d17b64649f74d83748`; `H73_f2.json` blob `505707fed0184acc5d987ca336a5ccca9af48049`, all under Badacz `@8f9809f5`; complete 18 original MC node result records + 5 particle mean multiplicities, per-energy SE and per-event max energy residual.
- Original frozen `data/analysis097.json` blob `f6043967d386e6e7a46f8cb2c66b5529ec7bd6a9`, pinned as **HISTORICAL BBN TABLE AGGREGATE** (30 BH-u multiplicities) and held-out original owner 90 log-ratio comparison and source endpoint values.
- Frozen `code/analysis_097.py` blob `5055810ab1bfabb2cdffc88079b03d4acd5fcd04`, `code/mult_herwig_097.py` blob `9aa1a22c420a182465459fee85adc7c04a5a651d`, `code/run097.sh` blob `e250480f850199c89b0a336214cac9f94b9d91ec`, all `@24dbfafe`, direct read to assess owner gates and physics input typing, **NOT executed**.
- Original Badacz logged SHA-256 of 5 **PRIVATE owner-local BlackHawk source table files** from `data/inputs_sha_097.log` Git blob `e145cec0874694e84c7fa7f969e491c91fdfdb88`. The original huge BH v2.3 `pipm.txt, Kpm.txt, K0L.txt, proton.txt, neutron.txt` file CONTENTS were NOT supplied through the direct connected readable dataset for this review; direct independent recomputation of the **30 BlackHawk counts from those raw 5×100×100 arrays** and their digest comparison is therefore **NOT CLAIMED**. Values in `analysis097.json/bh` are separately source-layered **OWNER-EXTRACTED** table counts, not REC13 original tabulation I1. The executable replay is **I1 of original serialized REVIEW097 MC and owner archived aggregates**, not an I2 recertification of original archived BlackHawk tabulation.
- Independently discovered public BlackHawk-related source snapshot `michellekwok2/blackhawk_SUSY/scripts/herwig_scripts/up/main.cpp` original Git blob `433be3ab483064b11c7a4661fee837d84222441a` and `.../up/LEP.in` original blob `eafce728a4fb071f3f6681eb17dac21d6cd401c3` and `.../herwig_scripts/formatting.c` original blob `829780acdcbca6bb97e9f0a1d55aeda5911e6b4a`. These source texts were fetched **directly** from an externally maintained GitHub mirror/fork, NOT byte-equal-proven official BlackHawk-v2.3 release tarball or original historical production. `LEP.in` contains `LuminosityFunction:Energy %`; `main.cpp` replaces % by `initial_energies[i]` with NO factor 2; `formatting.c` preserves the `initial_energies[j]` labels and divides final event multiplicity by 2 for most columns. This is a directly source-backed **possible** code path `√s=E'`, not identification of the actual archived data-producing binary.
- External *original published BlackHawk manual*: Alexandre Arbey and Jérémy Auffinger, EPJC 79, 693 (2019), DOI `10.1140/epjc/s10052-019-7161-1`, §Appendix B.3 publicly states `E'` is **half the center-of-mass energy**, i.e. `√s=2E'`, for simulated PYTHIA/HERWIG event tables. Verified on full publisher HTML primary source `https://link.springer.com/article/10.1140/epjc/s10052-019-7161-1` §B.3, not an unverified inferred reference. Combined with the *mirror* code path this is a genuine documentation/source-script semantic tension, subject to historical archive provenance.

## 1. Independent 90/90 source JSON arithmetic — original firstness Badacz

A newly authored stand-alone pure JavaScript function was **actually executed** in REC13 connected tool runtime on 4 original complete GitHub JSON file reads, independent of Badacz's Python `analysis_097.py`; the EXACT executed function source was then serialized as a public reproducible Node.js program:
`research/rec13/2026-11-22/code/rec13_rot015_badacz097_multispecies_fingerprint_and_kaon_nuisance_i1.js`
at Git commit `3aac53c4eea655dc915a743d78a3b327da9b93c4`, original Git blob `6c8821b625764cac7944bec11c9859c33aaa37ac`. Source includes a rerunnable `node ... analysis097.json H72_f1.json H73_f1.json H73_f2.json > result.json` interface. GitHub full-file readback verified.

For each of (3 MC arms × 6 source energies × 5 hadron species) = **90** genuine published input comparisons, REC13 recomputed
`L_g(E,h)=log10[N_BH_owner_aggregate(E,h)/N_MC_original(E,h)]`
and checked AFTER the calculation against owner `analysis097.json/ratios`. Maximum absolute IEEE754 double discrepancy **0.0 dex** (90/90 exact). All 18 native-result row `events==2000`, `rc_read==0`, `rc_run==0`, `|E_final/√s - 1|<=1e-3` and even directly supplied `max_abs_event_Eresidual<1e-3`: **18/18 PASS**. Largest recorded eventwise residual among all 18 rows: `9.929817542886354e-6` (H73_f2, E'=100 TeV), below prereg mean-only gate and also below a conservative eventwise .001 check. This report thus does NOT repeat prior high-energy W± per-event-energy failure seen in distinct 090: PREREG097 tests ONLY primary up, not W±.

Original owner 2/2 prereg predictions **reproduced** as declared:
- `L_SQRTS = SQRTS_EQ_E`: `max_E |L_pi(H73_f1)|=.026636122786616426dex`; `max_E |L_pi(H73_f2)|=.10213361328744265dex`.
- `L_VER = NO_MATCH_PRE_72_CANDIDATE`: both 7.2.0 and 7.3.0 at f1 have some |L|>.04; K± log deficit changes from +.04044→−.26911 dex for 7.2 and +.02141→−.20632 dex for 7.3. **The label contains the suffix CANDIDATE, NOT a strict detection of historical version.**
- Across all FIVE species and SIX nodes when comparing same Herwig 7.3.0 f1 vs f2, **26/30** show smaller |L| under f1. Exactly four exceptions occur for *proton and neutron* at the TWO lowest energies E'=25 and 133.545 GeV, where f2 happens to be closer. All SIX pion energies select f1.

## 2. New MC-only quantitative six-node convention margin, not population-confidence claim

For SAME 7.3.0 with either f1 or f2, for each pion energy E calculate `L1=log10(N_BH/mean_pi_f1)`, `L2=log10(N_BH/mean_pi_f2)`. Their pointwise absolute-fit advantages are:

| E' GeV | |L2|-|L1| dex | σ_MC_f1 dex | σ_MC_f2 dex |
|---:|---:|---:|---:|
| 25 | .0794615946 | .003775003 | .003723867 |
| 133.545 | .0517356285 | .003725044 | .003690066 |
| 713.375 | .0517859744 | .003784870 | .003750660 |
| 3810.72 | .0527499145 | .003858905 | .004071971 |
| 20356.1 | .0532185105 | .003901686 | .004115803 |
| 100000 | .0441399096 | .004178320 | .004242063 |

Here the MC-only scalar standard-error plug-in is `σ_MC=(se_pi/mean_pi)/ln10` (first-order delta method). At ALL SIX source energies, strict nonoverlap of individually inflated 3-SE *MC-only* absolute discrepancies holds:
`|L1|+3σ1 < |L2|−3σ2`.
Minimum uninflated margin `0.044139909604488714 dex`. This bolsters the finite-data comparison of f1 vs f2. **NOT** a 3σ joint confidence statement for actual historical binning, **NOT** a test of actual historical generator release, and no multiplicity covariance, archived BH 100000-event uncertainty, tune uncertainty, shared-seed energy covariance or 95% CI is calibrated here.

## 3. Independent new low-dimensional source-nuisance falsifier of unique historical version inference

The original Badacz label `NO_MATCH_PRE_72_CANDIDATE` is an appropriately qualified candidate: Herwig 7.2/7.3 default tunings do not reproduce all five historic hadron multiplicity classes at six nodes. Interpreting this result as **IDENTIFIED `original version <7.2`** would be logically unsound because alternative flexible hadron source acceptance/hadronization response models exist.

Construct a deliberately minimal and **explicitly only phenomenological** 2-parameter response `q(E)` that multiplies **K± and K0L counts together** in modern 7.3 f1 source comparison:
`q(E)=A (E/25 GeV)^b`.
For each of 6 source energies fit `v_j=[log10(NBH_Kpm/N73_Kpm)+log10(NBH_K0L/N73_K0L)]/2`; ordinary unweighted least squares on `x_j=log10(E/25)` yields ACTUALLY independently evaluated:
`log10 A = -0.013079769675782657`,
`b=-0.062405525368310705`,
`A=0.9703317237742344`.
Over the 6 archived source nodes q smoothly decreases from ~0.9703 (25 GeV) to ~0.5783 (100 TeV). Compare the same two-parameter q across **12 REAL K data points** (2 species × 6 energies):
- Maximum `|log10 NBH_K − log10(q(E)*N_H73_f1,K)|` = **0.0344917101545434 dex**, *strictly below original owner 097 `TOL=.04 dex`* when applied only to the two kaon species.
- A single constant kaon factor cannot do so: best minimax constant over 12 source K log ratios has a guaranteed worst absolute error **0.11935731136345239 dex**, well above .04. The data demand energy-varying K response if the only nuisance is a shared scalar.
- Crucial **NEGATIVE predictive guard**: six leave-one-energy-out refits of the above 2-param law have worst held-out error **0.0724355280029718 dex** (lowest source energy); therefore **this smooth model was NOT prospectively validated** at the 0.04 dex tolerance. It is a finite-data observational-equivalence construction and diagnostic of identifiability only.

This q(E) is **NOT an implemented release/tune parameter of Herwig**, does not fit proton/neutron/pion residuals, and cannot establish that Herwig 7.3 with some realistic tune physically produced the archive. Rather, it proves that **the observed kaon trend alone cannot logically distinguish software VERSION from an unmeasured energy-dependent nuisance**, even with only TWO flexible parameters at the six existing nodes. It also confirms that original `PRE_72_CANDIDATE` is correctly weaker than `HERWIG_PRE_72_PROVEN`. The actual physical version/tune must remain **UNKNOWN** absent archival run settings, unique independently authenticated version marker, or a fully source-calibrated common-generator test.

## 4. New histogram endpoint non-implication and source script tension

Owner's actual `analysis097.json/endpoint` carries six maximal *nonzero labeled final-energy grid nodes* for pion output; `max_nonzero_pi_node/(E'/2)` computed independently:

| E' GeV | highest nonzero π node / (E'/2) |
|---:|---:|
| 25 | 1.03324 |
| 133.545 | 0.89780 |
| 713.375 | 1.00755 |
| 3810.72 | 1.13072 |
| 20356.1 | 0.98251 |
| 100000 | 1.198968 |

So **4/6** maximal labeled output nodes are actually **ABOVE E'/2**. This is NOT a disproof that collisions used √s=E'; table values are binned secondary-energy labels, not validated individual event records. The original archived 100 secondary bins span 10^-6→10^5 GeV, so the multiplicative grid-step is `exp[ln(1e11)/99]=1.2915496650148839`. Every one of the 4 above-half endpoints lies **within one original bin step** of E'/2. Depending on whether the archived histogram label is bin lower edge, center or upper edge, this can be a perfectly ordinary finite-resolution overshoot, but that convention has **NOT been authenticated** from the true production YODA events. Conversely, treating each node as an exact observed individual pion energy and declaring a kinematic contradiction would be unjustified. The endpoint values ALONE do not certify the actual archived collision energy.

Owner PREREG097 itself explicitly finds archived `formatting.c` and Rivet classification/cross-axis inconsistencies and says the archive may not equal the original production chain. Directly read external fork snapshot of `up/main.cpp`, `up/LEP.in`, global `formatting.c`: the source code's `Energy=%` replaced with initial `E'` is an exact semantics issue **for that published C++ script path**, confirmed independently. But the snapshot is a 3rd-party fork and not proven equal to original v2.3 data-generation source; no chronology proof or binary provenance was provided. The manual on publisher says `E' = √s/2`, and the computed pion source comparisons favor f1; cumulatively the evidence is strong for **ARCHIVED_DATA_CONSISTENT_WITH_SQRTS_E**, but does not license the more universal `ALL_HISTORICAL_HERWIG_TABLES_DEFINITIVELY_GENERATED_BY_THIS_SCRIPT_AND_NO_OTHER_IMPLEMENTATION` without authenticating the 100k-event per-primary production chain.

Further typological check: Badacz `REVIEW098` calls “third source is sqrt(s) label” relative to REC13 ROT012's suggested `T_HERBH*B_H/B_P` counterfactual. A **6-energy, one-primary multiplicity fingerprint is a different source level** from a complete third 100-PBH-mass×5-species **folded BBN rate table** with actual 8 Wu-Xu/PRyMordial beta crossings. Thus it can explain a potential major origin of old-vs-modern table differences, but CANNOT by itself decompose the older `dhold≈0.134–0.219 dex` into separate beta threshold effects of grid, sqrt(s), version/tune. This is a strict operator/domain/nontransfer distinction, not a rejection of the 097 original label.

## 5. Science decision and targeted recommendation

**PASS:** independent published source arithmetic `90/90` original MC versus owner archived table aggregates, `18/18` rc0, required events, mean and eventwise energy checks; Badacz prereg declared `Pr1,Pr2` PASS and owner interpretation as source `SQRTS_EQ_E` **FAVORED**. Original BlackHawk 2019 B.3 manual center-of-mass `E'=√s/2` and a separate public mirror source `main.cpp` E' energy setting verified.
**PASS source-specific new**: under the original archived six-node, u-only inputs, f1 wins 26/30 species slots and all pion nodes even after individually three SE from fresh MC (conditional on owner BH aggregates). Alternative 2-parameter smooth energy-dependent K source multiplier fits 12/12 measured K logs to ≤.03449 dex; fixed multiplier cannot (<.1194 dex minimax error), LOOCV held-out max .07244 dex => explanatory confounding model, **not predictive or a real Herwig tune**.
**HOLD:** historical actual Herwig generator version and default tune: evidence supports older version plausibility, not identification. Original archived BlackHawk table five raw source SHA values are owner-reported but REC13 has not byte-read or rehashed them. Histogram endpoints are binned; 4/6 exceed E'/2 labels but within one energy-grid increment, so no strict eventwise kinematic proof nor eventwise contradiction from labels.
**HOLD:** attribution of beta threshold shift `dhold` to sqrt(s), version/tune or binning without a **complete** changed 100-row 5-group native BBN source and actual model reexecution. No physical PBH bound or novelty established. EKS1's public Slack ROUTE ROT016 separately recommended downgrading the historical version/tune candidate to technical/systematic budget; preserve Moderator authority and Badacz owner firstness. No request to contact authors against Moderator's explicit preference.

Potential minimally sufficient next source-only check if priority demands: obtain **one independently verified historical BlackHawk v2.3 raw HERWIG `pipm.txt` and its origin SHA-256 from owner** and certify exactly the 6×100 original printed histogram bins, endpoint positions and bin semantics; alternatively independently run a fully pinned 7.1 Herwig for *one* predeclared energy of K production with full tune metadata (Moderator decides). There is no obligation or authorization to rerun entire BBN solver to settle only source provenance. Avoid new task cascade; science-first.

Public source-replay code actually executed **within current REC13 V8 tool invocation** and published as EXACT `function audit` code via `audit.toString()` in the file:
https://github.com/wmakiela-tech/Nash-iw-research/blob/3aac53c4eea655dc915a743d78a3b327da9b93c4/research/rec13/2026-11-22/code/rec13_rot015_badacz097_multispecies_fingerprint_and_kaon_nuisance_i1.js
Git original blob `6c8821b625764cac7944bec11c9859c33aaa37ac`, 4814 chars; exact GET/readback PASS. NODE reexecution from 4 pinned downloaded JSON inputs should yield same summaries; Node execution itself NOT separately performed by REC13.

No new Herwig/Julia/BlackHawk native original generator runtime or high-performance tools run. Public report source-only, `GITHUB_PENDING_BW_INGEST`, no CANON or EXEC_SIGN.

FINAL:
`REC13_ROT015_BADACZ097_REVIEW098_90_OF_90_SERIALIZED_SOURCE_I1_EXACT / 18_OF_18_MC_SOURCE_ENERGY_GATE_PASS / SQRTS_E_FAVORED_STRONGLY_NOT_BINARY_PROVEN / 26_OF_30_MULTISPECIES_F1_WINS / ALL_SIX_PI_MC_3SE_NONOVERLAP / LOWDIM_2PARAM_KAON_NONIDENTIFIABILITY_12_AT_TOL004_BUT_LOOCV_FAIL / FOUR_OF_SIX_ENDPOINT_GRID_LABEL_OVERSHOOTS_WITHIN_ONE_BIN / HERWIG_ORIGINAL_VERSION_TUNE_UNKNOWN / FULL_RAW_BH_TABLE_REHASH_HOLD / NO_PBH_LIMIT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
