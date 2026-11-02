---
artifact_id: IW_MECH_S8_ROT004_WUXU_FIG5_EXECUTION_LINEAGE_STATIC_SOURCE_AUDIT_001_20261103
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
date: 2026-11-03
exposure: PUBLIC_SAFE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: STATIC_CODE_PATH_PASS__HISTORIC_FIG5_PROVENANCE_OPEN__NO_CANON__NO_EXEC_SIGN
---

# ROT004 — Wu–Xu Fig.5 source-code dependency / historical artifact distinction

**Verdict:** STATIC_CODE_PATH_PASS / HISTORICAL_FIG5_EXACT_EXECUTION_OPEN / E4_HOLD-SOURCE_BLOCK.

## Original primary sources (pinned author Git)

Repo Fenyutanchan/Primordial-Black-Hole commit d395183674cace6c9906a8911bdeb7234ba4040d. Read complete v3 and v1 notebooks via GitHub blob interface, source scripts via fetch_file, Git tree with file modes and both scanning JLD2 as base64. No Julia/BlackHawk/BBN execution.

- data/out/hadrons_from_PBH.dat Git blob 06d0883a27b108692720422294ba2baacd381a64: 100 masses from 1e9 g; five aggregate hadron channels.
- tool_script-hadrons_from_PBH.jl blob cc73432910f872d526113ce59b6204f38d0766a9: five log-log LinearInterpolation calls with ExtrapolationType.Linear, no explicit subedge T_H^1.3 branch.
- main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6: includes above module at line37, uses hadron rates in ODE lines103–107 and writes data/out/scanning.jld2 (Y_P_mat, chi2_mat).
- data/out/scanning.jld2 blob 10cc9b3f078fcadb91b5e520e75845859ca00b74, 151089 bytes, header JLD2 Julia 1.12.3.
- main.ipynb blob 171c4a29e414860d724c817641896628f35982b0: cell4 includes hadron module; cell9 contains same 10D source; cell14 loads scanning.jld2 and uses Y_P_mat heatmap and solid blue chi2_mat=4 contour for Y_P.png.

## The separate v1 overlay

In v3 main.ipynb cell14, **after** base Y_P.png plotting, a dashed chi2_old_mat=4 contour is added to create Y_P_with_v1.png. The old dataset is data/out/scanning_old.jld2 Git blob 5dd0a2032c4612a25c0e1a72ab58d0ad8f8ab084, mode 120000, a symlink pointing exactly to ../../arXiv-2509.05618v1/data/out/scanning.jld2, **not** a damaged 47-byte JLD2. Its target Git blob ff08072449c4ef46144cb800778224acd9669a8f, 149272 bytes, JLD2 Julia 1.11.6. Original v1 main.ipynb blob 89a69d1ac23f3024893db51da29c9f573ecf0c5f has an 8D model with three pion/kaon sources; its v1 source file tool_script-mesons_from_PBH.jl blob d9b9b15adaf8e500c67f1d1f1f531ccf26002b35 is log-linear, and v1 main-scan.jl blob 1855db41e67dddbcc4380daf904829833c082d19 includes that module. Thus dashed v1 comparison is not independent same-model validation.

## Strict ceiling and consequence

ROT003 identified the manuscript Section 4.1 boundary-matched analytical subedge law T_H^1.3 versus the log-linear source method in the pinned main-scan code. ROT004 ties the latter to the **public Fig.5 notebook and graph dependency path**, not just a disconnected helper. However, stored JLD2 data contain no verified exact executed source-commit provenance; the mere presence of current source and output assets cannot prove which law was used to generate the historical figure in the published paper (Wu & Xu, JCAP 02 (2026) 063, DOI 10.1088/1475-7516/2026/02/063). Notebook cell3 sets save_plot_flag=false even though cell14 has conditional PNG save branches and saved cell execution outputs. No statement that the paper or its results are incorrect.

**Owner next action:** obtain exact Fig.5 run provenance: source snapshot/hash, log, JLD2 file identity, chosen subedge law, and publication figure/image lineage. Then one blinded paired original native Julia10D source-law comparison only if owner and independent referee authorize. Keep charge-state map, BlackHawk E4 source, stringent numerical and Yp/D/H target gates separate. No percent source shift is a Yp or beta shift.

Disposition: FIG5_PUBLIC_CODE_PATH=PASS; HISTORIC_FIG5_PROVENANCE=OPEN; E4=HOLD/SOURCE_BLOCK; NO_PBH_BOUND; NO_CANON; NO_EXEC_SIGN. GITHUB_PENDING_BW_INGEST: not BW accepted or peer audited. This is a compact public custody report; long local ROT004 report and standard-library pinned-source audit script exist separately.
