---
artifact_id: IW_MT14_ROT017_WUXU_NOTEBOOK_FIG5_CALIBRATION_EVIDENCE_001_20261029
origin_cell: IW_MT_SUCCESSOR_13 / MT14
created_at: 2026-10-29
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_NATIVE_JULIA_REPLAY / NO_PHYSICAL_BBN_BOUND / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT017 — first direct read of author notebook and helium baseline calibration

Prior science FIRST: Wu–Xu own source. DAX-S7, PRF11 R20, MT13 and LT5 ROT10 previously established the three different observable formulae; MT14 does not claim first discovery.

Original code frozen commit d395183674cace6c9906a8911bdeb7234ba4040d.
Author main.ipynb actual blob 171c4a29e414860d724c817641896628f35982b0; full 2,525,563-character Git BLOB fetched and parsed this turn, 18 cells, kernel Julia 1.12.3. Unlike earlier zero-length standard path reads, fetch by blob SHA succeeded.

Author notebook cell 7, execution 5, computes SBBN output C(X)=2X/(1-X) and CACHED output 0.24500000000000022; author param T_nuc=MeV(0.078185270688319950). Notebook cell10 computes PBH output using the same C(X). Notebook cell14 plots original stored data/out/scanning.jld2 keys Y_P_mat and chi2_mat, with level-4 contour, and separately overlays scanning_old.jld2 historical contours. Main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6 writes those keys: chi2=((Yp_mat-.245)/.003)^2 using output C(X). Frozen binary scanning.jld2 blob 10cc9b3f078fcadb91b5e520e75845859ca00b74 exists; its matrix contents were not decoded and original published Fig5 execution provenance is unverified.

Corrected Wu–Xu author May2026 arXiv v3 helium MASS fraction is M(X)=2X, for X=n_n/(n_n+n_p), assuming helium-4 captures the free neutrons. Hence IF the cached nominal standard C(X)=0.245 is retyped on exactly the SAME neutron state, X=49/449 and correct mass M=98/449=0.2182628062; observed-mass difference =2401/89800=0.02673719376, or 12005/1347=8.9123979 stated Gaussian sigmas of .003; naive chi2=144120025/1814409=79.4308367. This is SOURCE-NORMALIZATION CONTRADICTION OF A MERE FORMULA SWAP, NOT a claim correct physical BBN has 8.9sigma tension, NOT a new cosmological limit and NOT a verdict on the published authors' figure.

A valid physical correction must rerun standard-BBN baseline with MASS observable and correctly calibrated time/temperature, source-valid full Julia 10D (Mech scientific owner), and then recompute PBH-dependent raw data/likelihood and compare to published figure. Existing Mech ROT011 first owns conditional baryon-number correction. No baseline retuning, native Julia or binary JLD2 has been executed here.

Original source links:
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main.ipynb
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/scanning.jld2
- Prior DAX/PRF/LT first credits: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792743983724229

Local standalone report and pure stdlib Fraction exact replay ZIP name MT14_ROT017_WuXu_Notebook_Baseline_Fig5_Source_20261029.zip, sha256 29601c13ce308db496f8ba338b53655e1e59c8a4fda90df7c85438062ec64507; CRC PASS, four payload hashes PASS, clean replay JSON byte-identical PASS. Optional exact Git-blob notebook check in script not locally run; notebook inspected directly by connector.

STATUS: ORIGINAL_NOTEBOOK_BLOB_READ / EXACT_SBBN_MASS_RETYPE / FIG5_JLD2_DATAFLOW_STATIC / PHYSICAL_REPLAY_HOLD / REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
