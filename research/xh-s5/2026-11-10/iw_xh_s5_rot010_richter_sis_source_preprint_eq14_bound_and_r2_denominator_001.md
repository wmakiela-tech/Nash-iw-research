# XH-S5 ROT010 — Richter 2026 SIS: exact PREPRINT bound counterexample, published Eq(1) domain, original-code R² sign gate

artifact: IW_XH_S5_ROT010_RICHTER_SIS_BOUND_AND_R2_GATE_20261110
date: 2026-11-10
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
return_id: XH-S5-ROT010-RICHTER-SIS-PREPRINT-EQ14-AND-PUBLISHED-CODE-DENOMINATOR-GATE_20261110
exposure: PUBLIC
ceiling: SOURCE_VERSION_SPLIT / EXACT_CLASSICAL_INFORMATION_THEORY_COUNTERMODEL / ORIGINAL_CODE_SOURCE_READ_NOT_EXECUTED / NO_BIOLOGY_REPRO / NO_NOVELTY / NO_FINAL_2026_METHODS_ERROR_CLAIM / NO_CANON / NO_EXEC_SIGN / BW_PENDING

## Primary published and author preprint: do not conflate

Till Richter, Eric Zimmermann, James Hall et al., "Multimodal cell foundation models require synergistic integration beyond alignment", Nature Machine Intelligence, published Nov 9, 2026, DOI https://doi.org/10.1038/s42256-026-01328-3; publisher full-indexed body https://www.nature.com/articles/s42256-026-01328-3 . Actual paper Eq(1) defines SIS=(I(Y;Z3)-Imax)/Imax, Imax=max(I(Y;Z1),I(Y;Z2)); paper explicitly states empirical implementation substitutes linear-probe macro-F1 or R² and DOES NOT obtain unique PID atom. Results concern spatial transcriptomics/morphology from three organ datasets, 10 fusion methods. No author biology dataset or full pipeline reproduced.

CRITICAL VERSION SPLIT: AUTHORS EARLY FEBRUARY PREPRINT "Beyond alignment: synergistic integration is required for multimodal cell foundation models" bioRxiv Feb24 2026 DOI 10.64898/2026.02.23.707420v1 https://www.biorxiv.org/content/10.64898/2026.02.23.707420v1, text indexed also at https://www.researchgate.net/publication/401163781_Beyond_alignment_synergistic_integration_is_required_for_multimodal_cell_foundation_models . Preprint Methods Eq(14), around original text lines 525–542, ASSERTS SIS ∈ [-1,1] from incorrectly general "subadditivity of mutual information" I(Y;Z3) <= I(Y;Z1)+I(Y;Z2) where Z3 concatenates projected modalities. This bound is NOT VALID without restrictions excluding synergy. **We have NOT VERIFIED that final Nov2026 publication carries Eq(14)**. The general statement in this report is a falsification of specific PREPRINT Eq(14) and a mathematical boundary on the PUBLISHED Eq(1) definition. No claim of final journal peer-review failure, original biology results failure, or priority.

## Mature host: no novelty

Classical Williams & Beer 2010 Partial Information Decomposition, arxiv:1004.2515; XOR synergy and conditional mutual information are mature. The author preprint already distinguishes PID's unique/redundant/synergistic atoms and explicitly discusses approximation due to weaker-modality unique signal. No new PID or original theory. Public Nash-iw-research literal searches on "synergistic information score" and "PID mutual information" empty; cannot rule out private prior art.

## Exact eight-cell source-local falsifier
Let fair independent binary X,Z; independent selector U~Bern(eps). Y=X xor Z if U=0, Y=X if U=1. 8-cell PMF enumerated with Fraction for rational eps, including zero cells, normalized EXACT.

Binary Shannon entropies:
I(Y;X)=1-h2((1-eps)/2), I(Y;Z)=0, I(Y;X,Z)=1-(1/2)h2(eps).
Thus I(Y;X,Z)>I(Y;X)+I(Y;Z) for 0<=eps<1, falsifying PREPRINT Eq14's putative universal MI subadditivity. eps=0 gives 1 joint bit and 0 each marginal bit, so SIS is UNDEFINED (zero denominator), NOT +infinity numeric. For eps>0 all numerators/denominators well-defined and SIS positive and can diverge as eps→0+. Asymptotics Ix~eps²/(2ln2), Ijoint→1, SIS~(2 ln2)/eps²→infinity.

Executed independently:
eps=1/2, SIS=1.649401393277943;
eps=1/4, SIS=12.043957686071906;
eps=1/10, SIS=104.94385558042454;
eps=1/100, SIS=13301.706547005566;
eps=1/1000, SIS=1378385.876429667.
All are exact-PMF Shannon computations, NOT biological benchmark scores.

Correct broad bound when Imax>0 and Z3 computed from source pair by DPI:
-1<=SIS<=H(Y)/Imax-1, not universally <=1.
A SUFFICIENT (not universal) condition for <=1 is I(Y;Z1,Z2)<=I(Y;Z1)+I(Y;Z2), for example if I(Z1;Z2|Y)<=I(Z1;Z2). Chain rule exactly: I(Y;Z2|Z1)-I(Y;Z2)=I(Z1;Z2|Y)-I(Z1;Z2). In this model the right side is positive except eps=1. Negative-fusion control SIS=-1; duplicate perfectly redundant modality SIS=0.

## Source-pinned ORIGINAL AUTHOR CODE READ; only independent algebra executed

Author GitHub repo https://github.com/microsoft/cell_synergy ; file src/cell_synergy/sis.py at PINNED COMMIT c979e32234364e8fa9dc1acbc712aca581257bba, exact readback Git blob SHA b6861b1f6ccd2927daf98f8f5794386ebc9b8ef4:
https://github.com/microsoft/cell_synergy/blob/c979e32234364e8fa9dc1acbc712aca581257bba/src/cell_synergy/sis.py

In compute_sis, authors' program computes mean macro-F1 and mean R² of IMG, GEX and multimodal, then sis_r2=(multimodal_r2-max_unimodal_r2)/max_unimodal_r2 and analog for F1. No division-by-zero or negative-denominator guard in read source. **NOT EXECUTED ORIGINAL MODULE**; independently executed exactly this arithmetic with synthetic input values, exposing conditional problem:
GEX R²=-0.10, IMG R²=-0.20, multi R²=+0.20 => SIS_R²=-3.0 though model improved.
GEX R²=-0.10, IMG R²=-0.20, multi R²=-0.50 => SIS_R²=+4.0 though model worsened.
GEX R²=.001, IMG R²=.0005, multi R²=.20 => SIS_R²=199.0.
If both baseline R²=0 => denominator0, undefined/nonfinite depending Python float type.
F1 (GEX=.25, IMG=.20, multi=.75) => SIS_F1=2 although all F1 between0,1; no universal upper1 without baseline>=.5.

These are CONDITIONAL score-domain issues. We did not examine whether ANY actual real published experimental F1/R² values trigger them, so NO CLAIM author experimental results are wrong.

## Three independent executed routes

(1) pure stdlib Fraction exact 8-cell joint distribution, generic MI from contingency including marginalization, independent entropy analytic formulas for 8 eps, frozen exact_results.json.
(2) independent NumPy 2x2x2 tensor entropies, Monte Carlo 500000 iid joint observations each for eps=.1,.25,.5, seeded RNG260922. Author-shaped relative F1/R² algebra and negative/near-zero denominator controls. Frozen independent_results.json. Source author module source read only.
(3) independent stdlib entropy chain-rule marginalization, 6 eps including 0, conditional co-information witness, negative fusion/redundancy controls, frozen chainrule_results.json.

Moderator-local FULL ZIP IW_XH_S5_ROT010_RICHTER_SIS_BOUND_AND_R2_GATE_REPRO_20261110.zip, SHA256 861764f01e78f82954134ccf1eb9ef41b518df7ae580758319aca9dce0381ad1, bytes15835. Contains 10 members: full Polish report SHA256 1b8db56ed77cda0e8d9b8d5fabf8c2a8f6d8b839c68d30e5b73244cc5cc68ea2, README, three source executables, three frozen JSON, standalone clean verifier, manifest (file member hashes). ZIP CRC PASS; all 9 payload hashes verified; clean isolated extraction and ALL THREE reexecution gives JSON BYTE_IDENTICAL PASS. No external author raw dataset, GPU or author-code-execution claim. GitHub report NOT full ZIP.

## Existing open dependency EKS1 and project governance

Current Slack #iw-dispatch read: no new DIRECT XH-S5 task after T1 Schall ACCESS_BLOCKED report, which was actually routed earlier:
https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794316397879199
Schall original Source Data binary still not acquired; do not assert no time series from raw ZIP. The user separately approved private DTC0a Untitled0.ipynb migration, tasked to SYSS6, not XH. New scientific host does not substitute for Schall T1; owner wait is an explicit separate bounded source dependency, not task closure.

NEXT SOURCE-NATIVE KILL TEST (proposed, not delegated): obtain full final Nature Machine Intelligence Methods and test whether Eq14 bound remains there, run original pinned sis.py on synthetic score triplets if source execution is required, check original paper benchmark R² base values to see if negative/zero domain ever occurs. Do not ask to change science owner status until referee source-version check.

NO_BIOLOGY_RESULT_REPLAY / NO_NEW_PID_THEOREM / NO_SOURCE_AUTHORS_FAULT_CLAIM / NO_NASH_PHYSICS / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED / NO_TASK_CASCADE.