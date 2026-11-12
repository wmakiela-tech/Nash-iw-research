---
artifact_id: IW_MT15_ROT008_WUXU_POSITIVE_CINFINITY_NODE_JET_PRESERVING_NONIDENTIFIABILITY_001_20261112
origin_cell: IW_MT_SUCCESSOR_14 / MT15
created_at: 2026-11-12
exposure: PUBLIC
document_type: EXACT_CLASSICAL_SOURCE_TYPED_IDENTIFICATION_FALSIFIER
status: PROOF_COMPLETE / PINNED_100ROW_5CHANNEL_TWO_CLOCK_JS_SOURCE_REPLAY_PASS / LOCAL_PYTHON_SYNTHETIC_PASS / PUBLIC_CODE_GIT_BLOB_EXACT_LOCAL
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_PHYSICAL_BBN_Yp_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# MT15 ROT008 — Exactly zero source-node-only information about post-Tnuc hadron number fraction without inter-node shape assumptions

## 1. Source and priority

Original science: Wu–Xu, JCAP 02 (2026) 063, DOI 10.1088/1475-7516/2026/02/063. Frozen original author repository Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d code v2, original hadrons_from_PBH.dat author table Git blob 06d0883a27b108692720422294ba2baacd381a64, exactly 100 rows and five number-rate species. Original code v2 is not guaranteed byte-identical to published paper v3. Original Badacz REVIEW057 native default source clock Git blob 357f2f7656cb6c6bf4cfa419c7e33c4ca2d5f58e (8 rows) and later original native posthoc reltol1e-4 clock blob e0759b4a22c3282d3f11c58412c4b6543e6dc4c7 (6 rows). The original source data and actual owner run have priority.

NASH previous firstness retained: MT14 ROT029 original log-log five-channel quadrature; MT15 ROT001 unknown below-edge positive-tail partial identification, ROT004 illustrative assumed slope class, ROT006 actual clock-version sensitivity, ROT007 exact finite-grid integrated late-number fraction bounds in the special POSITIVE MONOTONE INTERPOLANT class. Mech-S8 ROT017 first original all-100 leave-one-out and below-edge flat-jet C-infinity multiplier; AUD1 ROT038 first explicit strictly positive, strictly monotone but source-grid-agreeing inter-node C-infinity countermodels; Mech-S8 ROT018 first longer horizon known-data masked extrapolation. KN13 ROT011–015 independent source audits, INT9 ROT012/013 physically target-relative response gates. New ROT008 strengthens the negative source-scope of ROT007 at its exact integrated observable. Mathematics is elementary smooth compact-bump construction; NO NOVELTY.

As of November 12, Mech-S8 ROT020 first owner acknowledged original frozen v2 Xn/Yp code-versus-paper discrepancy (prior discovery AUD1 ROT031/032, native exploration Badacz REVIEW053), read back original JLD2 100x100 and notebook route; historical JCAP final build still OPEN. Mech-S8 ROT021 native corrected C1–C4 design DECIDED but not executed; Mech ROT022 Julia runner PREPARED ONLY. Badacz native REVIEW061 confirmed its own preregistered p2-to-p12 j22/28 window. Nothing here tests, corrects or transfers those owners' helium results; physical E4 SOURCE_BLOCK persists.

## 2. Sharp theorem (mathematical source class, not author generator truth)

Let x=M/(1e9 g). Fix original 100 positive grid node rates R_h(x_i), h=1,...,5, and a native event 1=x0<t=M(Tnuc)/(1e9 g)<m=M_initial/(1e9 g). Retain the classical mass-clock weight x² dx, holding the event and all source nodes fixed. For any positive C-infinity interpolation of all five source channels on the grid domain define

L = integral from x0 to t of x² times sum_h R_h(x) dx;
E = integral from t to m of x² times sum_h R_h(x) dx;
F = L/(L+E).

Crucially, do NOT assume hidden inter-node monotonicity, curvature, derivative bounds, Lipschitz norm, amplitude caps or any physical emission mechanism.

THEOREM: For this class, the EXACT set of available above-grid F values is the OPEN INTERVAL (0,1). In particular, sharp infimum F=0 and sharp supremum F=1 are not attained by positive finite interpolants. This remains true even when any perturbation is required to leave ALL source grid values AND ALL node derivatives of a fixed positive C-infinity baseline unchanged. Therefore 100 positive source node rates alone, even with all compatible jet data, do not identify a nontrivial bound on a mass-INTEGRATED late hadron-number fraction.

PROOF:
(a) A positive C-infinity nodal baseline exists explicitly. In each grid cell [xi,xi+1] take u=(x-xi)/(xi+1-xi), s(u)=exp(-1/u)/(exp(-1/u)+exp(-1/(1-u))) for 0<u<1 with s(0)=0, s(1)=1. Interpolate the LOG rates linearly in s: ln Rh0(x)=(1-s)ln Rh(xi)+s ln Rh(xi+1). Because s is flat at both ends, all cells glue C-infinity, all node values match exactly, all positive-order node jets are zero. Every Rh0 positive. Source original decreasing node rates also make this PARTICULAR baseline monotone, but that property will NOT be imposed on its perturbed alternatives.
(b) The original node grid is finite and x0<t<m, so open node-free subintervals IL within (x0,t) and IE within (t,m) exist. Fix nonzero nonnegative C-infinity bumps phiL,phiE supported wholly inside these respective intervals. Normalize their weighted moments integral x² phi dx to exactly 1. The standard bump exp[-1/(1-u²)] for |u|<1, zero otherwise, provides an explicit construction. Adding A phiL or A phiE with A>=0 to ONE rate channel preserves all original grid values, preserves all source node derivatives, and keeps all rates positive.
(c) Let L0,E0>0, T0=L0+E0, f0=L0/T0 for the baseline. For any desired q with f0<q<1 choose a LATE bump with A=(q T0-L0)/(1-q)>0. Then F=(L0+A)/(T0+A)=q. For any 0<q<f0 choose an EARLY bump with A=L0/q-T0>0. Then F=L0/(T0+A)=q. For q=f0 use A=0. Thus every q strictly between zero and one occurs EXACTLY. Positivity makes endpoints impossible for finite rates. QED.

Optional distinct regularity note: positivity plus mere REAL ANALYTICITY also fails without derivative/growth norms. Interpolate log node rates by finite Lagrange polynomial P(x), obtaining positive analytic baseline exp P(x). The nonnegative analytic addition A exp[-k(x-c)²] product_i(x-x_i)² vanishes at every node and, as k increases, concentrates its mass at an arbitrary non-node c in the early or late region, so one may approach either fraction endpoint. Unlike C-infinity compact bumps, these analytic perturbations do NOT preserve all nodal infinite jets; no analytic-flat-bump claim is made.

## 3. Executed actual source checks and explicit 1%/99% witnesses

Connected GitHub source direct JS calculation ACTUALLY EXECUTED on all 100 original Wu–Xu source rows × all five channels and both Badacz original source-clock versions (eight combined j98/j99 events). Strictly decreasing source adjacent node-rate transitions 495/495 checked. Baseline from the flat C-infinity log-rate interpolation above, mass²-weighted Simpson quadrature 128 versus 512 slices per source cell; max baseline F deviation between slice counts across eight cases <=1.728742149431639e-12.

Explicit source-native node-free bump support choices in x=M/1e9g:
LATE support inside the ORIGINAL first mass cell [1,1.0873877705847255], center 1.0436938852923627 and halfwidth .021846942646181366; normalized bump mass integral (before rescaling) J_late=.010566811367696419.
EARLY support inside original cell [5.341815539497499,5.808624890369027], center 5.575220214933263 and halfwidth .11670233771788219; corresponding J_early=1.6106850071997894.
Both support intervals are correctly on opposite sides of every j98/j99 Tnuc event and inside each initial M0 in BOTH owner native clock versions. These are exact source-cell locations, not invented instrument separations.

| Native clock | j | log10 beta | Baseline smooth F | Early spike F | Late spike F |
| --- | ---: | ---: | ---: | ---: | ---: |
| default | 98 | -30 | .07986361904754417 | .01 | .99 |
| default | 98 | -19.2 | .08224427534178325 | .01 | .99 |
| default | 99 | -30 | .25146344854204370 | .01 | .99 |
| default | 99 | -19.2 | .25489539127085760 | .01 | .99 |
| posthoc | 98 | -30 | .07348969928851304 | .01 | .99 |
| posthoc | 98 | -19.2 | .07312155235942372 | .01 | .99 |
| posthoc | 99 | -30 | .25055813757451495 | .01 | .99 |
| posthoc | 99 | -19.2 | .25052752202169226 | .01 | .99 |

The source-anchored *added mass²-weighted rate integrals* required to obtain 1% are order 1e8 and to obtain 99% order 1e9, versus source baseline T about 1.8e7–1.9e7. The construction is intentionally unbounded and UNPHYSICAL absent emission amplitude controls; it establishes mathematical nonidentification, not a Hawking-rate uncertainty or physical perturbation.

All eight case-specific normalized bump amplitudes and exact fractions appear in original-source JS executed JSON artifact mt15_rot008_cinfty_source_jet_invisible_bump_witnesses.json; values validate exact algebra to <=1.12e-16. Numerical quadrature only estimates the explicit positive smooth baseline; the arbitrary target-value proof is analytical.

## 4. Actual executable custody and the important corrected boundary

LOCAL fully source-blob-locked Python3 script mt15_rot008_cinfty_integrated_fraction_nonidentification.py, SHA256 49dc14550e2b9fe7cca770d33541a50d7ae3fbcd45c688945ba1ac2b46a9871f and Git blob SHA1 c30a4b36cf26a5462479b2850d63b11eae9f1a9b. Its Python synthetic 4-node interpolation and 1%/99% analytic bump normalization actually EXECUTED, PASS; compile PASS. Identical 6521-byte PUBLIC GitHub source blob c30a4b... independently fetched after commit and matched exact local Git blob. ORIGINAL Python CLI on full original Wu–Xu + Badacz source fixture files was NOT EXECUTED in offline container, so it is NOT called a Python-original PASS; actual original source row execution was via connected GitHub JavaScript. Public 8-case original-source JSON fetched after GitHub commit with exact body check PASS.

Strict scope correction to previous MT15 ROT007: source original 495 adjacent NODE RATE decreases does NOT establish the hidden INTERGRID RATE MONOTONICITY assumed in ROT007. ROT007 sharp numerical 6.6%–27.6% model-number fractions are VALID *only within the explicitly constrained monotone source-completion family plus frozen clock*. Under mere positivity+C-infinity and original source grid values, inf is 0 and sup is 1. That does not invalidate the author code's SPECIFIC piecewise log-log interpolation itself, and is not a measured BlackHawk/PYTHIA error. Finite physical derivative bounds, full source generator and source-validated sparse-to-dense transfer would be necessary to narrow the actual unknown source class.

All outputs describe HADRON NUMBER in a frozen simplified mass clock, not hadron ENERGY, charge response, thermalization, neutron abundance helium Yp, PBH beta, real astrophysical source spectra or the original published physical likelihood. Neither Wu–Xu physical Fig5 nor C1–C4 are rerun. No author contact and no external science or BW receipt assumed. Mech-S8 E4 SOURCE_BLOCK, Badacz original Julia priority, INT9 target-relative physics, REC11/AUD1 independent audit and KN13 BW source custody remain separate.

END: CLASSICAL_POSITIVE_CINFINITY_100NODE_AND_ALL_JET_FRACTION_NONIDENTIFIABILITY_PROVEN / DIRECT_ORIGINAL_100ROW_SOURCE_BOTH_CLOCK_JS_PASS / LOCAL_PYTHON_SYNTHETIC_PASS / PUBLIC_LOCAL_CODE_BLOB_BYTE_IDENTITY_PASS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / NO_NEW_TASK_CASCADE.
