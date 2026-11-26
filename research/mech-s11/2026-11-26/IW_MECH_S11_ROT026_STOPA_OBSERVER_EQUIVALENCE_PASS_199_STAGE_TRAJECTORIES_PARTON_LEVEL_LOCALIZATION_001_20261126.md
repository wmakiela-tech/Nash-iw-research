---
artifact_id: IW_MECH_S11_ROT026_STOPA_OBSERVER_EQUIVALENCE_PASS_199_STAGE_TRAJECTORIES_PARTON_LEVEL_LOCALIZATION_001_20261126
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-26
status: OBSERVER_FEASIBILITY_PASS / DIRECT_STAGE_LOCALIZATION / MECHANISM_OPEN
claim_ceiling: MODEL_CONDITIONAL / NO_UNIVERSAL_NONINVASIVENESS / NO_CAUSAL_SUBROUTINE_IDENTIFICATION / NO_GATE_CHANGE / NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Actual execution and custody
Frozen prereg 9353ddf69bc809cc110faa113a0724001fef5ba7 blob 2011d22f135172b629cfd40ec57f513dfc097bf2; driver 0e05f7ee7fc2e501d08d6216cc432475b2977dc5 blob 825740bfdc0ef52519cd28dcfb96426960b3a60f; workflow a35c041c22df716d65df529b4a61b2beb893e693 blob ee88d27852bb515cb8ffc8bca9d4c346a98eaae5. Run 45709884256 all four jobs PASS, CI and public locator guard PASS. Four actual ZIPs downloaded and locally replayed using Python script /mnt/data/mech_rot026_replay.py SHA256 d8e9c9c13d8dcb0d33c5e1b096f4d586819a120ad5138e82868a3f20db6763e3. All provider hashes, CRC, exact manifest coverage 60/60 verified. IDs and SHA:
0 15067117066 5b055cbf803e89f5196655a03fb22aa570c80734646d20f18be3bb23135069f9
1 15066707952 0165effbc770caccd337af38e67cdebaed27f77d6b0e78339277ba92777d537f
2 15067700427 dc5642e67daabd0bc8cea6d7c5ac157b665df30ee32339072d7146b57e227819
3 15065824686 28bb7028e8a48b44363ab462ed9528f633920a796cfcfbfa8ae10a8d8b4f140c
All declared wheel hashes match 0ebe2dff962631571100dc427fbaa95e388df054ac06cdc8f63b31af07eb3de8. Recomputed recorded equivalence (not raw particle field hash regeneration; only snapshots and hashes retained in this experiment): all 200 baseline/observer pairs same successful call sequence, event snapshot including SHA, process SHA, qualification, settings and recorded effective settings. G_OBS PASS, G_HOOK PASS. No claim about full RNG/internal state equivalence. 199 strict AB sequences with all references exactly nominal; one g-off call18 ABAB excluded by frozen criterion. No new simulations this rotation.
# Direct stage trajectories
A post-parton before boostAndVertex; B post-hadronization callback; F returned final. L1 normalized sum of absolute components, threshold 1e-6 diagnostic only. Source identity and exact checker ROT024.
|cell|strict|L1 trajectories A/B/F|energy-only trajectories|max AB vector L1|max BF vector L1|
|---|---:|---|---|---:|---:|
|u off 100TeV|50|000:50|000:50|5.1227663715357026e-8|2.7279072660978122e-16|
|u off 2PeV|50|111:30,000:17,100:1,011:2|111:17,000:32,011:1|4.236492987137336e-6|1.7957048850954414e-16|
|u on 2PeV|50|111:26,000:23,011:1|000:30,100:2,111:16,011:2|4.3935309456928316e-5|2.187921572262524e-16|
|g off 2PeV|49|111:16,000:33|000:44,111:5|7.371875491427597e-7|1.7166207937072066e-16|
75/199 final L1 exceedances, 72 already at A, 3 first at B, none first F. 1 A-only L1 failure recovered by B. Energy-only 41 final failures, 38 already at A, 3 first B; 2 A-only energy failures recovered by B. L1 and energy estimands distinct. Maximum AB vector change 4.3935309456928316e-5, energy component 1.9511072948807853e-5, both u-on; maximum BF vector change 2.7279072660978122e-16 across strict subset. Thus post-B is not material in this subset, and A already contains most observed final-threshold violations. However AB change can be substantial and can cancel or create failures: no statement all errors from shower or that hadronization is negligible. A includes parton-level processing, not solely one shower routine. AB includes frame/vertex transformation and hadron-level operations, not isolated fragmentation. No general frequency claim from feasibility design. 
# Deliverable and decision
Local certificate /mnt/data/mech-s11-rot026-observer-certificate.json SHA256 779b86abcb7d748ed70cf9431d4caa8650e63b7b198289bc2588c533e39cb9e0 records all strict trajectories and excluded call. Reproducer and certificate local, not separately repo-stored. Existing 48k G_E/P3 FAIL unchanged; no retrospective gate change, no W/P2/fold/G_OVL/G_COV. Next inspect exact source of parton-level internal checkpoints and use only material discriminators; no claim causal routine, no automatic new run. Independent bounded referee pending. No BW write.
