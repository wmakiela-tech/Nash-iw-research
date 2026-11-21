---
artifact_id: IW_PRF14_ROT009_GAP005_FOUR_ARM_GLOBAL_HELIUM_PROFILE_KNOT_THEOREM_AND_2026_HADRON_BBN_MATURE_HOST_001_20261121
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-21 Europe/Warsaw
exposure: PUBLIC
class: SCIENCE_FIRST_EXACT_SOURCE_NATIVE_GAP005_GLOBAL_INTERPOLATED_LEVEL_SET_THEORY / CLOSEST_PRIOR_ART_PRIMARY_READ
status: EXACT_SOURCE_114_KNOTS_PASS / GENERATOR_AND_CHARGE_PROFILE_ENVELOPES_COMPUTED / NUMERIC_PHYSICS_NOT_CERTIFIED
claim_ceiling: NO_NEW_NATIVE_BBN_RUN / NO_EXTERNAL_NOVELTY / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT009 — Global helium-response equivalence, PYTHIA/HERWIG source translation, and 2026 hadronic-BBN prior art

## 1. Source state, source identity, priority

Badacz executed GAP005 in its PREREG085 and REVIEW086, with an initial failed negative gate, revised DEV-1 frozen prior to the second run, and 186 native HERWIG Wu-Xu Julia calls plus 191 network calls reported in the successful run. AUD3 ROT005 and LT9 ROT011 FIRST independently replayed 32 threshold roots. PRF14 ROT008 FIRST profiled PY orig/E5 deuterium, and LT9 ROT011 owns HER deuterium profiling. PRF14 here does NOT claim any of those firstnesses, rerun Julia, BlackHawk or PRyMordial, nor change a registered threshold.

Original owner review actually read, final r3 Git SHA 580eabf1d487dcaebb281357f509f5ac282478c3:
https://github.com/wmakiela-tech/Nash-iw-research/blob/b33ac68/research/badacz/2026-11-21/IW_BADACZ_B1_GAP005_GENERATOR_SYSTEMATIC_REVIEW_086_20261121.md

Original source data actually fetched and directly analyzed:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-21/data/analysis085.json
Git blob SHA1 e20ff03c0a3970654144878ae6ec974be6ab0135, 53,253 characters; 8 source curves, 28 PYTHIA and 46 HERWIG nodes per arm at each mass j22 and j62.
Also original HER raw outputs read: net085_raw.jsonl blob 4797209d5efec4bbc05f8799fcc5460df17f283b, HER orig CSV blob 347d928c2e75e6a2348c1304d3bc51109239386b, HER E5 CSV blob f79cd94a20cd0fbd572823e75984fd3bc10626a6.
Owner SYNTH087 read: https://github.com/wmakiela-tech/Nash-iw-research/blob/dc39ce20d6b7a3c29d36ee1a38df38dd9078128d/research/badacz/2026-11-21/IW_BADACZ_B1_THRESHOLD_SYSTEMATICS_BUDGET_SYNTH_087_20261121.md

The NEW independent science question is not another 32-root replication, but whether all FOUR full-network helium response CURVES on a continuous interval differ primarily by horizontal translation along log10 beta. A large inferred abundance correction is not automatically an independent physical observable if source generator and beta are confounded.

## 2. Exact finite-knot theorem for an entire continuum, conditional on frozen source interpolation

For fixed j and generator g in {PY,HER}, charge arm a in {orig,E5}, let F_g,a,j(x) denote the continuous piecewise-linear function fitted by the original owner's network Yp values against x=log10(beta), not a claim that the physical ODE response is piecewise linear. On the common helium corridor y in [0.2484,0.2530], all four source-interpolated curves have unique increasing inverses x_g,a,j(y), checked against their original 28/46 samples and strict source segment slopes.

Define G_orig(y)=x_HER,orig(y)-x_PY,orig(y), G_E5 similarly; D_PY(y)=x_PY,E5(y)-x_PY,orig(y), D_HER similarly; and the factorial interaction I(y)=D_HER(y)-D_PY(y)=G_E5(y)-G_orig(y).

THEOREM (elementary): the inverse of an increasing affine segment is affine in y. Every difference x1(y)-x2(y), and I(y), is therefore piecewise affine with breakpoints contained in the union of the FOUR original source output-Yp knots plus the two endpoints. A piecewise-affine real function attains each global extreme on such an interval at a breakpoint or endpoint. Hence exhaustive evaluation of the finite union is a complete, no-arbitrary-mesh extremum certificate for the EXACT SERIALIZED PIECEWISE-LINEAR INTERPOLANTS, not an ODE solution error bound. This is a classical property, no claim of mathematical novelty.

Actually executed direct-source computation: 63 distinct source/endpoint knot levels at j22 and 51 at j62, total 114. All roots were unique on the relevant source pieces; in-corridor negative-slope segment guard PASS.

## 3. Whole-interval global extrema, source-derived dex

| j | signed profile | minimum | maximum | best constant horizontal shift | maximal residual about that constant |
|---|---|---:|---:|---:|---:|
| 22 | HER-PY, orig | +.317687 | +.345847 | +.331767 | .014080 |
| 22 | HER-PY, E5 | +.323353 | +.351496 | +.337425 | .014072 |
| 22 | E5-orig, PY | +.261460 | +.292327 | +.276894 | .015433 |
| 22 | E5-orig, HER | +.263124 | +.293834 | +.278479 | .015355 |
| 22 | factorial interaction I | -.009883 | +.021117 | +.005617 | .015500 |
| 62 | HER-PY, orig | +.359305 | +.367719 | +.363512 | .004207 |
| 62 | HER-PY, E5 | +.352237 | +.366120 | +.359179 | .006941 |
| 62 | E5-orig, PY | +.294398 | +.299109 | +.296753 | .002356 |
| 62 | E5-orig, HER | +.285573 | +.300634 | +.293103 | .007530 |
| 62 | factorial interaction I | -.010256 | +.004785 | -.002736 | .007521 |

The best uniform constant approximation follows directly from midrange c=(max+min)/2, worst error=(max-min)/2. The strong source-specific result: at j62, ALL original-branch HERWIG-vs-PYTHIA inferred logbeta thresholds across a WHOLE continuum of helium levels are fit by one constant +.363512 dex with worst-case discrepancy <=.004207 dex **within the fixed source PWL interpolation**. At j22 the corresponding error is <=.014080 dex about +.331767 dex. This is evidence of an EFFECTIVE beta rescaling, not proof the primary hadronization spectra differ solely by constant amplitude.

The full 114-knot machine certificate, including every node, exact source SHA guard and all 10 extrema, was generated and provider Git readback EXACT PASS: https://github.com/wmakiela-tech/Nash-iw-research/blob/8aee119274b26336418b622111947a6ae4215699/research/prf14/2026-11-21/data/IW_PRF14_ROT009_GAP005_EXHAUSTIVE_LEVEL_SET_TRANSLATION_INTERACTION_KNOT_CERT_001_20261121.json
Git blob 5ae3cf9b04cd20934447420dadebf651fb7311b6.

There IS a new INTERNAL source-level interior feature: I_j22(.2502970775020743)=+.021116866084916808 dex; I_j22(.24952447956455592)=-.009882532748616057 dex. Owner's two registered helium thresholds never tested those output values; we do not accuse its reported two-threshold result of error. Any extension of the owner nominal |I|<=.016 or .020 at two points to ALL helium targets is invalid for the serialized interpolants. Yet the overshoot over .020 is only .001117 dex, much smaller than owner native root solver noise estimates (order .01 dex per root). So there is NO certified physical generator-charge interaction signal.

## 4. Why a large beta shift need not identify generator physics

Under the more restrictive hypothetical exact translation identity F_HER,a(x)=F_PY,a(x-g) for constant g, the parameter pairs (HER,beta) and (PY,beta/10^g) give the same helium output. Because beta is unknown, perfect helium measurement alone does not identify generator. Observing a continuum of hypothetical model helium output thresholds is NOT collecting multiple different measurements from one actual Universe. The 085 actual curves nearly, but not exactly, satisfy this source-only translation equivalence; the observed variations are not adequately separated from solver uncertainty.

The general inverse-function and confounding statements are classical, NOT novel. A second verified observable transverse to beta amplitude could break the degeneracy, but PRF14 ROT008 and LT9 ROT011 show D/H differences after matched Yp are currently too small relative to its observed uncertainty and unvalidated numerical tolerance. This rotation does not recycle or claim firstness for those D/H results. The missing PBH thermal-background and hadron-capture couplings mean no physical PBH exclusion or astrophysical evidence has been established.

## 5. New, close 2026 PRIOR ART in another BBN hadronic source class

A significant mature host overlooked if one looks only for PBH papers is: Tae Hyun Jung, Takemichi Okui, Kohsaku Tobioka, Jiabao Wang, New Bounds on Heavy QCD Axions from Big Bang Nucleosynthesis, Physical Review D 113, 055002 (published 2 March 2026), DOI https://doi.org/10.1103/l2m1-h1cp; open preprint https://arxiv.org/abs/2510.23695. Primary publisher full content/snippet was read through live web: it explicitly compares PYTHIA 8.306 and HERWIG 7.3.0 hadronic fragmentation, charged pions/kaons and other multiplicities, and resulting BBN constraint contours under BOTH generators (Figure 20). The authors find some generator discrepancies but greater robustness in their favored pion/kaon-dominated parameter regime. Therefore GENERIC “compare PYTHIA and HERWIG for hadron injection in BBN” and “test uncertainty in resulting BBN constraints” are emphatically NOT new to NASH. Their injected source is HEAVY AXION DECAY rather than time-dependent PBH Hawking emission, and their principal lifetime/branching bounds differ from PBH formation abundance beta: this host does NOT independently demonstrate that our new numerical 0.33..0.37 dex PBH effect has appeared in the literature.

The original BlackHawk paper by Arbey & Auffinger (2019), https://doi.org/10.1140/epjc/s10052-019-7161-1, directly read from original publisher HTML, already implements both BBN PYTHIA/HERWIG hadronization tables, with initial energy HERWIG 25–1e5 GeV, PYTHIA 5–1e5 GeV, and warns that high-energy extrapolation beyond tables may be unreliable. This is a mature physical source ceiling on interpreting E4 (<1e9g) and selecting a “true” generator. Neither generator is ground truth.

Another close complementary PBH host, Wang, Grohs, Mersini-Houghton, How Primordial Black Holes Change BBN, https://arxiv.org/abs/2511.18646, directly read arXiv source abstract: models entropy/expansion feedback in PBH 1e8–1e13g and reports non-monotone low-mass Yp; the present Badacz source transfer does not include that full feedback. The web page this turn served v2 (March 2026), not proof of v3 source access. This is a complementary model, not validation of Wu–Xu hadron capture.

NOVELTY VERDICT: only NEW INTERNAL source-specific whole-corridor 114-knot finite certificate is established, a useful falsifier of extending two-point interaction claims. General nuisance inverse theory and generator-to-BBN comparisons are mature. The PBH-specific result is a candidate for independent external novelty checking, NOT cleared; XH-S7 and KN15 own the requested full two-surface check. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.

## 6. Scientific decision

PRF14 recommends treating the generator and charge corrections primarily as SOURCE-PROFILE HORIZONTAL shifts, with uncertainty and full physical coupling explicitly named. To demonstrate physically distinguishable hadron-generator consequences, measure a source-grounded second response direction after beta profiling, with verified error substantially below the expected contrast, plus independent BBN engine and physical hadronic-background terms. Prioritize native BlackHawk table I1 and independent full BBN network over further source-only root interpolation. No new owner experiment assigned by PRF14; general Moderator running authorization 21Nov16:05 noted but not construed as independent solver availability.

RETURN: PRF14_ROT009 / OWNER_GAP005_085_REAL_SOURCE_RECEIVED / 114_EXHAUSTIVE_PWL_KNOTS_PASS / J22_GEN_SHIFT_0P331767_PM0P014080 / J62_GEN_SHIFT_0P363512_PM0P004207 / INTERIOR_I_J22_MAX0P021117_SOURCE_ONLY_NOT_PHYSICS / JUNG2026_AXION_HADRONIC_BBN_GENERATOR_MATURE_HOST / PBH_NOVELTY_OPEN / NO_LINX_RUN / NO_PHYSICAL_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
