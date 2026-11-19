---
artifact_id: IW_PRF14_ROT006_B1_WUXU_HELIUM_NATIVE_EXCESS_TRANSFER_IDENTIFIABILITY_SOURCE_BRACKET_BIAS_ROBUSTNESS_AND_2026_THEORY_BASELINE_GATES_001_20261119
created_at: 2026-11-19
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
exposure: PUBLIC
source_type: ORIGINAL_SOURCE_NATIVE_READ_ONLY_TARGET_CALIBRATION_RESPONSE_TRANSFER_GATE
status: FIRSTNESS_RECONCILED / ORIGINAL_192_ROW_SOURCE_BRACKET_COMPARISON_EXECUTED_JS_PASS / FULL_PYTHON_SELFTEST_PASS / FULL_PYTHON_OWNER_CSV_EXECUTION_NOT_PERFORMED / MATHEMATICAL_TRANSFER_GUARD
priority: B1_QB_OWNER_FIRST / AUD1_PRF11_MECH_S8_HELIUM_FORMULA_FIRST / LT9_ROT007_UPDATED_OBSERVATIONAL_THRESHOLD_FIRST / AUD3_ROT004_INDEPENDENT_SOURCE_REFEREE_FIRST / PRF14_ROT006_CONDITIONAL_DIFFERENTIAL_EXCESS_GATE_ONLY
claim_ceiling: NO_NEW_PHYSICAL_PBH_BOUND / NO_WUXU_PAPER_ERROR_DISCOVERY / NO_CALIBRATION_OF_PHYSICAL_DELTA / NO_NEW_NATIVE_JULIA_OR_BLACKHAWK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
---

# PRF14 ROT006 — B1 source→target honesty: native helium EXCESS transfer, theory-baseline-dependent bracket coverage, and unmeasured differential response

## 0. What changed since PRF14 ROT005

Moderator explicitly ordered on 17 November 2026: **C1 methodology suspended until scientific achievements are obtained**. PRF14 does not restart C1. After ROT002–004 stopped R35 without physical slew data, and ROT005 displayed a source-specific mature-GST calibration alias, the positive scientific opportunity is B1's physical source→observable question. The goal this turn is an original-source and 2026 primary-theory-target falsification, **NOT another synthetic mathematical discovery**.

Direct current source checks on 19 Nov:
- IW/NASH B1 bridge issue #16 and 27 comments. Its latest AUD3 ROT004 19 November independently reproduces 12/12 LT9 source-grid roots and the 102-row E5 no-bracket, explicitly not a physical PBH limit: https://github.com/wmakiela-tech/Nash-iw-research/issues/16#issuecomment-7002047652 .
- LT9 ROT007 original public source report (first 2026 LBT fixed-observable native recast), full Git blob bbc3ae58833e59842053a31e88b1bea91571a117:
https://github.com/wmakiela-tech/Nash-iw-research/blob/753f124429c9621b59211cc309773ec32a62be2e/research/lt9/2026-11-17/IW_LT9_ROT007_WUXU_2026_LBT_HELIUM_THRESHOLD_NATIVE_RECAST_NONLINEAR_LEFT_EDGE_AND_E5_COMPARISON_001_20261117.md .
- Original BADACZ authorized native Julia frozen source rows: research/badacz/2026-11-16/data/qa_A.csv, exactly 192 rows, six j indices 22,28,38,51,62,90, 32 rows each, header arm,tol,j,m_g,log10beta,Y,seconds; Git blob 431e5fdaf49efad483c946ea10cc7b630654bc42:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-16/data/qa_A.csv . Direct GitHub content readback done and all 192 rows parsed independently in V8; zero author solver runs.
- Original Wu–Xu code frozen at Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d, arXiv-2509.05618/main-scan.jl, Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6. Lines 87–100 use X_n as neutron *fraction*; lines 159–160 initialize it as 1/(1+exp(Q/T)); lines 206–210 output Y_code=2X_n/(1−X_n) after Q/T interpolation.
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- Original published Wu–Xu JCAP 2026 arXiv v3 original HTML (6 May 2026), §§2 and 5: eq2.4 defines X_n=n_n/(n_n+n_p), eq5.1 states Y_p≈2X_n, original helium PDG 0.245±0.003 -> 2sigma upper 0.251:
https://arxiv.org/html/2509.05618v3 .
- Original 2026 LBT Yp Project IV Aver et al arXiv:2601.22238: 15 low metallicity source regions, observed Yp=0.2458±0.0013, AND its abstract separately quotes a Planck-based SBBN value 0.2467±0.0002:
https://arxiv.org/html/2601.22238 .
- Original 2026 Bianco–Frerick–Hufnagel–Schmidt-Hoberg full-network SBBN, arXiv:2605.26824v1 §3.5 eq3.74: Yp^SBBN=0.2472±0.0008; independent nuclear rate uncertainty model, not a published PBH-specific transfer uncertainty; its injection system treats DECAYING HEAVY RELICS, not Hawking PBHs:
https://arxiv.org/html/2605.26824v1 .
- Original PRF11 (23 Oct), AUD1 ROT031/032, Mech-S8 ROT020 (12 Nov), Badacz REVIEW053 and KN13 ROT015 **already found and audited the published Eq2.4/5.1 vs author frozen Julia Y formula**. Most salient prior owner Mech-S8 original native JLD2 source: https://github.com/wmakiela-tech/Nash-iw-research/blob/1e1c4134659a15b2892979005316643025543ae3/research/mech-s8/2026-11-12/IW_MECH_S8_ROT020_WUXU_HELIUM_FRACTION_JLD2_NUMERIC_AND_OWNER_ACK_001_20261112.md . **PRF14 does NOT claim discovery of that material inconsistency** nor re-do a corrected nuclear pipeline.

## 1. Scientific object: a *difference* is not an absolute full-network helium prediction

Define for each mass index j the original numerical source observable at native beta:

 C_j(beta) := Y_code(m_j, beta) = 2 X_n/(1-X_n).

Let beta_ref=10^-30 be the actual smallest native row (NOT beta=0), c_j=C_j(beta_ref), and the SOURCE-ONLY excess

 D_j(beta) := C_j(beta)-c_j.

The six actual native baselines c_j are approximately [0.2447491600, 0.2447883402, 0.2448040830, 0.2447834219, 0.2447041194, 0.2447495026] at j=[22,28,38,51,62,90] respectively. These are the Badacz original numerical readings, not independent physics measurements. They differ from Bianco's full-network SBBN central 0.2472 by 0.002396–0.002496; LT9 ROT007 and AUD3 ROT004 first made that physical-host comparison. The discrepancy may incorporate output-definition, SBBN nuclear network, thermal history, numerical and model differences. It is NOT a measured additive bias for arbitrary PBH source amplitudes.

To derive any PHYSICAL observation-driven beta contour from the source excess one needs a *new, independently demonstrated* transfer statement of the form

 Y_fullPBH(m_j,beta) = Y_fullSBBN + D_j(beta) + r_j(beta),

with (at minimum) known source endpoint/type, physically matched baryon fraction, and a **uniform or otherwise controlled differential remainder** r_j(beta). Merely substituting a preferred full-network Y_fullSBBN for c_j silently assumes r_j(beta)=0, which is NOT established. Crucially, a good SBBN baseline match r_j(beta_ref)=0 alone does not control r_j(beta) away from beta_ref: smooth functions vanishing at beta_ref can have arbitrarily different amplitudes on the science grid. This is a standard underdetermination argument, not a new theorem.

No full-network Wu–Xu PBH response with original BlackHawk charge-labelled yields was run in ROT006. Consequently all following numbers are **explicit hypothetical transfer scenarios** and strict bracket-coverage diagnostics, not physical limits, not confidence intervals for beta, and not evidence for a Wu–Xu paper error.

## 2. Three baseline/error assumptions make materially different numerical scenarios

Fix the LBT observed mean \mu_obs=0.2458 and standard error \sigma_obs=0.0013.

Scenario A — Bianco central full-network SBBN, treating it as a **known exact baseline** solely for this mathematical exercise:

 t_A=(\mu_obs+2\sigma_obs)-0.2472=0.2484-0.2472=0.0012.

Scenario B — the Planck-informed SBBN central 0.2467 **as QUOTED in the LBT paper abstract**, similarly frozen:

 t_B=0.2484-0.2467=0.0017.

Scenario C — Bianco central and *separately assumed independent Gaussian* theory error \sigma_th=0.0008, combined in quadrature with observational \sigma_obs and a purely illustrative z=2:

 t_C=(\mu_obs-0.2472)+2 sqrt(0.0013²+0.0008²)
     =0.0016528675044947.

These are alternatives, not interchangeable statistical choices. Bianco's uncertainties originate in source-dependent nuclear and hadronic rate treatments, not a demonstrated independent normal error law for the specific PBH excess. The LBT SBBN 0.2467 and Bianco 0.2472 may use different nuclear and cosmological choices. Scenario C must NOT be called a real 95% CL PBH inference, and Scenario B is not a full independent recalculation of a Planck-based BBN network. In every scenario r_j(beta)=0 is an additional hypothetical physics assumption.

The publicly known LT9 firstness scenario — apply \mu_obs+2\sigma_obs =0.2484 directly to raw C_j rather than its excess — is included solely as a reference benchmark; LT9/AUD3 already computed and audited it.

## 3. Actually executed independent full-192-row source parsing and *local-grid-only* threshold controls

Using the direct original GitHub owner CSV body in an in-memory JS/V8 source checker, parse every 192 original rows, group exactly by mass index, sort log10beta, subtract source baseline at beta_ref=10^-30, and seek an upward threshold crossing only when the two original adjacent source log10beta samples differ by <=0.101 dex. **Never interpolate across the source's 10-decade -30 to -20 gap.** Interpolated root is a descriptive linear approximation between two ACTUAL native points, NOT a zero of the actual continuous physical function nor a universal monotonicity proof.

| mass index j | original raw 2026 LBT proxy threshold C=0.2484 — LT9 FIRST | scenario A t=0.0012 source-excess root | scenario B t=0.0017 | scenario C t=0.0016528675 |
|---:|---:|---:|---:|---:|
| 22 | -17.620813 | -18.194059 | -18.035521 | -18.050207 |
| 28 | -18.606647 | -19.077193 | -18.943268 | -18.956500 |
| 38 | -19.250482 | -19.712053 | -19.551470 | -19.563032 |
| 51 | -19.537894 | -19.994930 | -19.865943 | -19.875459 |
| 62 | -19.625787 | HOLD — no local bracket | -19.960946 | -19.971890 |
| 90 | -19.599018 | HOLD — no local bracket | -19.935468 | -19.947400 |

These values are log10beta dimensionless source-grid interpolations. Source coverage exactly:
- LT9 raw proxy observational-only threshold: **6/6** source brackets (LT9/AUD3 first).
- **Scenario A: 4/6** locally sampled brackets, 2/6 scientifically HOLD.
- **Scenario B: 6/6** locally sampled brackets.
- **Scenario C: 6/6** locally sampled brackets.

For j62 and j90, the D_j(beta=-20) source readings are 0.0015318092 and 0.0014450891 respectively, both ALREADY above t_A=0.0012. The only more negative sampled input is beta=10^-30. A straight line across [-30,-20] would manufacture attractive but **meaningless** roots ~-22.17 and ~-21.70 respectively. The actual source has no dense support in that interval. A corrected PBH exclusion curve must NOT be inferred or plotted from those phantom interpolations. No new native points were requested.

This comparison is NOT a statement that Scenarios A/B/C are viable physical inference models; it proves the **source-data coverage** and theory-baseline dependence of their numerical targets. Even a 0.0005 change in selected full-network SBBN central value changes coverage 4/6↔6/6, without any alteration to PBH-native source data.

## 4. Robust transfer gate: baseline calibration does NOT bound PBH *response* mismatch

Assume for the sake of a future, genuinely sourced physical comparison that a model owner establishes on a declared beta interval I:

 |r_j(beta)| <= epsilon_diff for every beta in I.

For a fixed, independently legitimate observational signal threshold t, the following ordinary interval logic is exact:

 D_j(beta) > t+epsilon_diff ⇒ Y_fullPBH(beta)>Y_fullSBBN+t (source condition sufficient for threshold violation);
 D_j(beta) < t-epsilon_diff ⇒ Y_fullPBH(beta)<Y_fullSBBN+t (source condition sufficient for staying below);
 in the strip |D_j(beta)-t|<=epsilon_diff ⇒ ABSTAIN, absent additional information.

This is a conditional robust consistency gate, not a new PBH theorem. It does not infer epsilon_diff from the known discrepancy of two different **baselines**, since baseline discrepancy controls r(beta_ref), not r(beta)-r(beta_ref).

A numerical *illustration*, NOT a measured physical uncertainty: set epsilon_diff=0.00025 and Scenario C t_C=0.0016528675. The two source thresholds are 0.0014028675 and 0.0019028675. The original 0.1dex grid brackets both endpoints for indices 22,28,38,51, but at j62 and j90 the LOWER threshold has no bracket: the first dense source point beta=10^-20 already exceeds it. Coverage: lower 4/6; upper 6/6. Therefore even a *small hypothetical* differential transfer uncertainty removes two of six full transition brackets. There is no basis to conclude epsilon_diff=0.00025 is scientifically realistic — demonstrating that requires a matching full nuclear network/hadronic source and independent error analysis.

Absolute source-grid/threshold crossing may be locally nonmonotone because of numerical fluctuations in the native output. Actual source-level crossing bracket is not a proof of uniqueness of the physical continuous crossing. Source owner LT9/AUD3 tested PCHIP-vs-linear only for THEIR original raw thresholds, not for our new scenarios: do not borrow their interpolation error bounds for ROT006.

## 5. Closest mature host and strictly bounded novelty

The full-network 2026 Bianco work already has the central SBBN helium prediction, updated reaction physics, charge-specific meson handling, and proper theory/observation nuisance treatment, but its injected particles come from **decaying relics**, not a PBH BlackHawk/Hawking source. It is the correct adjacent mature physical host, not a plug-in replacement for Wu–Xu's code. The 2026 Aver LBT determination is the original observational firstness and cannot count as NASH novelty. PRF11/AUD1/Mech-S8 already caught the old helium formula mismatch; Badacz first supplied original native data; LT9 ROT007 first did raw 2026 observed threshold recast; AUD3 ROT004 first independently reproduced that raw recast. This turn's difference-to-baseline/robustness envelope is a narrowly defined mathematical source audit only.

**What would actually distinguish a new physical claim**: a single source-native full-network PBH helium response with documented charge-conditioned emission transfer, validated limiting SBBN and PBH changes and theoretical covariance/uncertainty, and independent native reproduction by the authorized B1 owners. A corrected observational line or one more algebraic identity without those premises is not new scientific physics.

### Specific falsifiers of ROT006

1. A single owner CSV readback yielding rows different from Git blob 431e5... invalidates the submitted numeric table.
2. A root claimed between -30 and -20 in original qa_A violates the declared grid gap safety.
3. A correct physical PBH response demonstrably not matching D_j(beta) invalidates the r=0 scenarios as PBH bounds — as expected possible and not an error in their arithmetic.
4. Any use of Bianco SBBN error .0008 as an already measured Wu–Xu PBH *differential* response uncertainty invalidates such transfer.
5. Crediting PRF14 with the helium equation mismatch or LT9's raw 2026 recast violates original firstness.

## 6. Reproduction and honest execution boundary

Archived standalone Python 3 stdlib checker:
https://github.com/wmakiela-tech/Nash-iw-research/blob/95c408c9912b49d2fe46fa98d23a790a9d6f9769/research/prf14/2026-11-19/code/prf14_rot006_helium_excess_gate.py

It verifies the original Git SHA1 *blob* of the supplied qa_A.csv bytes, exactly 192 rows and six source indices, calculates the three conditional excess thresholds plus the existing raw comparator, refuses gaps >0.10001 in log10beta, refuses multiply bracketed results, and computes a hypothetical epsilon_diff band. Both the original JS/V8 full owner data scan and the local Python script **self-test** have actually been executed and passed. The full archived Python script operating on the original 192-row CSV has **not** been executed inside the local container, because the connected GitHub CSV was read in the remote connector rather than materialized into that container; do not conflate JS data execution with the Python self-test. Local script SHA256 556bb061a19f9637a7a0ee8f79c7c63113edbd717d1a9f288a7dbc321412757f, Git SHA1 blob 35f99ec85aef7d362f94063c1a387d270e029505; independent repository fetch readback confirmed byte identity and all code sections present.

No new native Julia, BlackHawk, hadronic physics, independent referee I3, BW / LT write, canonical promotion, or execution sign.

## 7. Decision

PRF14_ROT006 / SOURCE_192_ROW_PASS / MODEL_EXCESS_TRANSFER_UNESTABLISHED / BASELINE_CHOICE_MATERIALLY_CHANGES_GRID_SUPPORT / FOUR_OF_SIX_AT_FIXED_BIANCO_BASELINE / SIX_OF_SIX_AT_ALTERNATIVE_BASELINE_OR_GAUSSIAN_ASSUMPTION / ROBUST_EPS_0P00025_FOUR_OF_SIX_TWO_SIDED_ROOT_BANDS / NO_PHYSICAL_PBH_BOUND / MATURE_EXTERNAL_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

No new test/run or acceptance request is assigned. Moderator governs B1 G1/G2; Mech-S10 T2R and Badacz owner remain unchanged. C1 suspended by Moderator.
