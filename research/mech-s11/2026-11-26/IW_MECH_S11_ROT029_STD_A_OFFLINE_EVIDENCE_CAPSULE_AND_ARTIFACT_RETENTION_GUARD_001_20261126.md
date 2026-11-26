---
artifact_id: IW_MECH_S11_ROT029_STD_A_OFFLINE_EVIDENCE_CAPSULE_AND_ARTIFACT_RETENTION_GUARD_001_20261126
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-26
status: OFFLINE_REPLAY_PASS / LOCAL_CAPSULE_VERIFIED / DURABLE_REPO_INDEX
ceiling: CUSTODY_AND_CONDITIONAL_MODEL_EVIDENCE / NO_NEW_SOLVER_RUN / NO_SOLVER_ERROR_BOUND / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
## Owner currentness
Read full latest B1 §F rows 142 r2 at f9d3cf036995ccbaac2d280ce7e9a938444cd010, confirms ROT028 repairs to environment and tested s values, preserves output sensitivity vs error bound. Original B1 question remains HOLD_SOURCE distinct from narrower STD_A/Q-B; no cross-cell history custody inference. Tiny numerical wording repair: exact computed maxima .023133927907847... and .015394491687041... dex; if written as upper bounds, round outward to .02314 and .01540, or say approximately .023/.015 (not <= rounded-down values). No change of result or gate.
## Actual retention and original custody
Direct GitHub Actions artifact API verified expiry and digest:
- H1 run 45616230955, artifact 15023132612, 50865 bytes, expires 2027-02-23T12:41:45Z, SHA256 5140a3e3f7fef4699f45a9fe27fce260c266d35363b344287b3c1c6f36445342.
- H2 run 45620537732, artifact 15028500895, 44405 bytes, expires 2027-02-23T13:08:22Z, SHA256 86a928c051fdaa338c9a290e21fc295cf55582d3b038e2a32ece322ce9ef4626.
Both currently unexpired; links are not durable indefinitely.
## Actual assembled and tested offline capsule
Local file mech-s11-rot029-std-a-offline-evidence.zip, 98553 bytes, SHA256 02c3f86b717b0ec9260565e45005032bc18ac10e46ee2fd63f7be86c05cc755e. Seven files including both original ZIPs byte-for-byte, original ROT028 certificate, portable standard-library verify.py, README with immutable locators, replay result, manifest. Verifier SHA256 dc49765abca9962a0f7e46342d23400c940249b33d3520f10be6befde051e14b. Executed twice in actual local Python: assembled directory, then independent temporary extraction of final ZIP. ZIP CRC PASS, all six outer manifest file hashes PASS, inner 49/49 file hashes and exact coverage PASS, 86 native output points across nine arms, two identical Project/Manifest pairs. Independently regenerated certificate byte-identical to prior ROT028 SHA256 a24c0668f620b4f1b24f35b8326af674b080ca004902750888f3a84e10c078b9. Verified all sampled sign margins >1e-4, H1 fixed-bracket conditional changes <.03, H2 three points remain within frozen intervals, bracket containment 2/3. No new ODE or generator run. Replay uses stored decimal outputs and does not require network or Julia.
## Limits and handoff
The capsule is an actual downloadable local deliverable, NOT uploaded as binary to GitHub or BW. This report is the immutable repo index and hash receipt, not substitute for ZIP bytes. Recommend durable archival copy by Moderator/KN within authorized storage, before February expiry. Julia upstream source/package binaries not vendored; future native regeneration still requires upstream source/environment. No automatic task cascade, no reclassification, no further B1 runs. Main product remains owner §F 142 r2 and brief141. STOP A/B/G_DEP unchanged.
