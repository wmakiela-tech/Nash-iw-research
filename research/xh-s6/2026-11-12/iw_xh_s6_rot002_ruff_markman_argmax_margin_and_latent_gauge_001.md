artifact_id: IW_XH_S6_ROT002_RUFF_MARKMAN_ARGMAX_MARGIN_AND_LATENT_GAUGE_001_20261112
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_SOURCE_RULE_GATE__SYNTHETIC_CONSTRUCTIONS__NO_RNN_WEIGHT_REPLAY_NO_MONKEY_DATA_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
task_id: IW_XH_S6_ROT002_AUTONOMOUS_EXTERNAL_SCIENCE_20261112
return_id: IW_XH_S6_ROT002_RUFF_MARKMAN_ARGMAX_MARGIN_AND_LATENT_GAUGE_001_20261112
result_class: RESULT + NEGATIVE_KNOWLEDGE
status: COMPLETE_SOURCE_RULE_MATHEMATICAL_TEST
created_at: 2026-11-12
acceptance_owner: Moderator; source paper firstness retained by authors
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT002 — Decision-margin and representation-coordinate gates for Ruff–Markman population formatting

## 0. One-sentence material result

The *exact 72-bin argmax readout* in the publicly released RNN-model pipeline has a sharp pre-choice score-margin stability bound: if winner–runner-up gap is Delta > 0, any perturbation to all output scores of sup norm < Delta/2 leaves the chosen bin unchanged. Consequently, an abrupt choice switch under output-score change is NOT, on its own, a logically sufficient signature of jointly formatted neural coding. Different baseline score-margin distributions can change switch rates by an order of magnitude in a controlled classical example. This establishes a necessary **margin-conditioned inference guard**, not a refutation of the paper's measured neural data or authors' causal results.

## 1. Source and provenance, two surfaces, dated

Contemporary ORIGINAL final journal article: Ruff, D.A., Markman, S.K., Kim, J.Z. & Cohen, M.R., *Information formatting in neuronal populations predicts differential functional contributions to behavior*, Nature Neuroscience, published **10 November 2026**, DOI https://doi.org/10.1038/s41593-026-02514-7 . Final paper open-access text/Methods were consulted from indexed publisher content. Its core is simultaneous monkey MT/dlPFC population recordings, an artificial two-module RNN and **actual microstimulation** that alters behavior differently across regions. The authors explicitly present the RNN as **qualitative** rather than quantitatively reproducing all neural activity, acknowledge the choice/reward representational ambiguity, and report experimental controls. No author error is claimed here.

Original authors' GitHub https://github.com/solkm/formattingRNN pinned main commit **7889a81e298c01532a313e02971c11dbc9db8eb0** (committer 2026-08-02). Direct original source reads:
- python_code_data/generate_microstim_testdata.py, Git blob **e7a6666e0b600ea49bab9755d302c78110ba9bc4**: choice direction is precisely 5 * np.argmax(output[:, -1, :], axis=1).
- python_code_data/simulate_combined_model.py, blob **0ccaadfd271c660a2a503b24f15b77ddede32962**: MT or dlPFC stimulation is an additional untrained input directed onto selected recurrent units. This is NOT a direct perturbation of final output scores.
- python_code_data/DotsTasks.py, blob **ac9e789c69a8ea46ac38303f9d0db524886ba0a9**: reward/choice targets and stimuli, including 72 directional output channels.
- README.md, blob **af7c5ca270e3576cfe7d983e2968cd5a2cb977ff**: trained model weights are in repository; simulated model test data are on Zenodo https://doi.org/10.5281/zenodo.21764173; original monkey experiment behavioral files are not contained in this repo and require authors' permission. README still describes the **2025 bioRxiv** version as 'currently in review'; do not identify its version wording with the **10 Nov 2026 published version**.

Mature external hosts: (i) Saxena and Cunningham, 'Towards the neural population doctrine' (2019), and (ii) 'Neural population geometry: An approach for understanding biological and artificial neural networks' (2021), https://pmc.ncbi.nlm.nih.gov/articles/PMC10695674/; (iii) 'Measurement, manipulation and modeling of brain-wide neural population dynamics' (2021), https://doi.org/10.1038/s41467-020-20371-1. Standard argmax/decision-margin analysis is elementary established mathematics, **not a novel neuroscience theorem**. Internal NASH heritage: XH-S5 source data vs synthetic/processed distinction; prior identification- and representation-warning does not itself certify any novel or physical transfer.

## 2. Exact primary theorem — sharp output-score stability gate

Let s in R^n, with a **unique** winning coordinate i and margin Delta=s_i - max_(j != i)s_j >0. Let d be any vector perturbing final *scores* with ||d||_infty <= eps. For every j != i,

(s_i+d_i)-(s_j+d_j) >= Delta - 2 eps.

Therefore eps < Delta/2 guarantees the same unique argmax. It is **sharp in the unrestricted score-vector class**: put d_i=-eps and d_j=+eps on the top two coordinates; if eps>Delta/2 the winner switches. Equality is the tie boundary, whose practical output is affected by index tie-breaking and floating-point details. This bound is **sufficient, not necessary**, for any specific direction of d.

Crucial non-transfer: the published RNN intervention injects a drive into hidden units. Its induced final-score change d depends on the nonlinear dynamics, trained weights and condition; mapping stimulation strength to eps requires an actual perturbation-to-score calibration or independently justified bound. We DO NOT say that source in-situ MT/dlPFC microstimulation itself obeys an externally prescribed eps.

## 3. Two computational routes actually executed

Route A: exact SymPy verification of the pairwise perturbed score difference Delta-2eps, and of rational probability/invertible-coordinate identities.

Route B: NumPy implementation of the **source's 72-bin readout**, with constructed score vector having baseline winning index 4 (20 degrees), runner-up index 36 (180 degrees), remaining 70 scores low. For 15 combinations of rational margins and output-score epsilon, the computed choice switches if and only if Delta < 2eps; exact equality was flagged **BOUNDARY_TIE**, not claimed as a strict gate. All non-boundary assertions PASS. Original author weights or trajectories are NOT used.

A decision-changing synthetic comparison: under a deliberately declared uniform margin distribution Delta~Uniform(0,L), choosing the adversarial top-two output-score perturbation [-eps,+eps] gives P(switch)=min(2eps/L,1). With eps=0.04, L=1 -> 2/25=0.08, while L=0.1 -> 4/5=0.8. **Same perturbation, tenfold rate difference solely from the assumed margin distribution.** These are generated probability models, not any monkey or RNN-trial empirical frequencies.

## 4. Supplemental representation-gauge negative control

Set latent x=(motion,reward), A_t=[[1,t],[0,1]], h=A_t x, and decode y=W_t h with W_t=A_t^(-1). Exactly W_t A_t=I for every t. Yet Euclidean cosine between the two coding vectors A_t e1 and A_t e2 equals t/sqrt(1+t²): 0 at t=0, 0.7071 at t=1, 0.94868 at t=3. A fixed *coordinate-unit* injection e2 has decoded consequence W_t e2=(-t,1), varying with t despite identical unperturbed input–output map. SymPy and independent NumPy checks PASS for t in {0,1,3,10}.

**Very important boundary:** the shear is a generic linear representation toy, NOT a proven allowed reparametrization of the authors' particular 150-unit Dale-constrained trained nonlinear RNN, nor a claim that physical neuron recording axes can be arbitrarily redefined. Its function is to show why output behavior alone cannot specify perturbation effects without fixing the physical stimulation coordinates and readout.

## 5. Experimental/inference discriminator, not an assertion about author observations

For future source-native model-data analysis, compare stimulation effect **conditioned on baseline top-two score margin Delta, reward condition, intervention-to-output effect scale and stimulated unit**, rather than comparing only aggregate choice-switch frequencies. If apparent area differences persist under appropriately matched measurable conditions, this counter-model is more strongly ruled out. If they disappear, the stronger area-specific causal interpretation needs revisiting. A null/no-match result is not automatically evidence for/against neural formatting without sufficient support and intervention comparability.

This is **not a demand for new animal experiments**: one can first test on the openly available trained model outputs and actual simulated perturbations if original model test data/weights become accessible for execution.

## 6. Exact scope and preservation of negative knowledge

- AUTHOR FINAL PAPER text: accessible from indexed publisher HTML; final 10 Nov 2026 version, separate from bioRxiv 2025 README.
- AUTHOR CODE: exact original Python text READ; not executed. Author weights: listed but not replayed.
- AUTHOR RAW MONKEY DATA: NOT OBTAINED; original repository's README explicitly distinguishes it.
- MODEL TEST DATA from Zenodo: NOT DOWNLOADED.
- XH: two independent mathematical/computational routes RUN on synthetic score arrays and exact classical two-dimensional toy; no reproduction of final neural activity, model RNN learning, monkeys or hardware stimulation.
- WTA as behavioral histogram phenotype is stronger than a single trial's argmax change; no inference that source data's full winner-take-all distribution is explained by these toy models.
- No novelty or priority, no claim the authors neglected margin controls (their paper already discusses stimulation and reward dependence), no canonical neural mechanism.
- Source code freshness: original repo main commit 2026-08-02 while published journal is 2026-11-10; no assertion exact journal revision code identity beyond article-linked repository.

## 7. Local audit receipts and reproducibility

Local reproducible standalone code: xh_s6_rot002_margin_geometry_gate.py; actually executed with Python + SymPy + NumPy. File SHA256 **c0f97c602ebd3adbbb175670eb3ec20882b861ef7d1a4d64c404088bb945d89a**, 5358 bytes.
Local detailed JSON: xh_s6_rot002_margin_geometry_gate_results.json, SHA256 **240f2fd3984a3bbe20f5f9f4b8665d2c94c62d6b43ce5a0cf8fc26c96c27f591**, 5334 bytes.
Local CSV: xh_s6_rot002_margin_gate_rows.csv, SHA256 **ff48a6bff14f5dc45e05d1725ff003f76a2fdc9f0d607866c712ef40c6bf8f28**, 541 bytes. Readback of all 15 rows and round-trip JSON verified.
Local code / output availability is not proof the exact bytes have been uploaded to GitHub; GitHub canonical full-body scientific REPORT write/readback is separately checked below. No source original weights embedded.

## 8. Result and claim ceiling

STATUS: SOURCE_RULE_MATHEMATICAL_GATE_PASS; SYNTHETIC_72BIN_CONTROL_PASS; FULL_AUTHOR_DATA_REPRODUCTION_NOT_DONE. New material result is an explicit quantitative **margin-stratification control** for avoiding unique inference of neural formatting from a discontinuous argmax choice output. This is conditional on a fixed final-score perturbation scale; it does not judge the authors' neural experiments.

GITHUB_PENDING_BW_INGEST. No independent reviewer, BW qualification, owner decision, CANON, EXEC_SIGN or physical upgrade implied. NO_NEW_TASK_CASCADE.

NEXT_REOPEN_IF: Original model trajectory/score data and simulated perturbation responses become source-accessible, permitting paired pre/post output-score margin analysis with fixed actual intervention-to-score mapping.