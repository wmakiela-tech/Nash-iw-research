---
artifact_id: IW_MECH_S11_ROT021_STOPA_800_EVENT_FOURVECTOR_LOCALIZATION_PROCESS_EXACT_FINAL_RECORD_MISMATCH_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
status: DIAGNOSTIC_COMPLETE / PERSISTENT_RECORDED_MISMATCH / NO_GATE_CHANGE
claim_ceiling: MODEL_CONDITIONAL / NO_CAUSAL_SUBROUTINE_IDENTIFICATION / NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# §F uncertainty delta
Separate diagnostic, not repeat of ROT019 (48000 accepted, strict G_E FAIL). Prereg b78ec95f891704f869f01fdc52fd5c800684635a blob 2834dc3dd6773ff30d1b5c7a6b08feb08c41ab95; driver 21a188f9f6f85c9e468f577c671735315c60c459 blob 7e1a8f51db28b3407ef900909d3e98ced7520f33; workflow 8bbdaded41647c5bfb5e16a0d7e965e7da8c3fc9 blob 8eb48babb0389a0829e357b9e0c21dd75d769150. AUD4 ROT013 firstness for checker distinction and arithmetic guard; SCOPE13 ROT012 firstness for missing-outcome sensitivity. 
Actual run 45705655584 all 4 jobs success, CI and locator guard success. Four original ZIPs downloaded locally, all provider SHA256 match, CRC PASS, 40/40 manifest files and complete coverage verified. Artifacts cell0 id15063829036 SHA256 6d4df00c6bfedf3f6612b8d19188a633d1901bc6bd1c794bcfa0e7a161656e92; cell1 id15065820572 c89885224b16b0415c87b839827ee7193c780e70cd7ac1dddb26b69505004c16; cell2 id15064329886 6cb87c55b43ce4dbd99c6a4021f1f4afabf88dd40e82581eb5510cd69959870b; cell3 id15063569516 10ae4d177f626b29d3feb24a7dea99ffa247b3a6c4be772404b9d1449ada1d2f.
Run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45705655584
Local independent Python replay of 800 actual gzipped event+process records (3263261 particle entries), exact fsum, explicit sequential sum (local built-in sum compensated, corrected replay to explicit ordinary accumulation), both exactly match stored driver vectors. Reconstructed qualification, nine counts, charge, residuals and classification; all match. All 800 beam identities valid; beam sums and system vector exactly nominal; final entries of PROCESS record sum exactly nominal in all 800, including all 170 energy-failing EVENT records. This is a comparison of two stored records, not proof of precise causal subroutine or local vertex conservation. All final EVENT charge sums zero. 
# Frozen diagnostic results
| cell | primary,weak,E | successful | qualified | old energy fail | persistent | momentum component >1e-6 | max abs energy residual |
|---|---|---:|---:|---:|---:|---:|---:|
|0|u off 100TeV|200|200|0|0|0|4.854034836171195e-8|
|1|u off 2PeV|200|200|70|70|59|1.5145241864491254e-5|
|2|u on 2PeV|200|137|82|82|72|1.713455132849049e-5|
|3|g off 2PeV|200|200|18|18|13|1.2398990332963876e-5|
170/800 energy fail (151 qualified, 19 rejected), 144 momentum component failures. 0 summation-sensitive, 0 nominal-reference-sensitive, 0 unresolved. 88 surplus and 82 deficit. Max naive-fsum difference 4.074536263942718e-15 normalized. Final multiplicity ranges 120..5301 across cells. Exact energy+momentum L1 maxima per cell 1.1593598314798194e-7,3.851427043064826e-5,4.838794374685387e-5,3.200082697796664e-5; L1 computed here is descriptive and not presumed exact internal checker formula. No gate relaxation. 
# Effective internal settings confirmed in actual wheel
Every cell Check:event=true, Check:epTolWarn=1e-6, Check:epTolErr=1e-4. Generator stdout stats reports energy-momentum warnings counts 0 (no matching line),114,127,64, and one internal error in cell1 despite zero failed next() calls reported: do not identify internal messages one-to-one with successful events or infer how retries handled. Observed full-record residuals compatible with more permissive abort tolerance. No assertion physical nonconservation; no claim exact implementation of internal checker formula yet. 
# Rejected population diagnostic
Cell2 63/200 rejected by hard filter, 137 qualified. Pion count per nominal incoming pair (divide by two) qualified mean 274.46715328467155 SE 10.714804292756988; rejected mean 287.07936507936506 SE 16.73331224390354; ratio 1.04595 approximately, not statistically resolved. Both means are conditional on this new small sample; do not combine with old 48k, do not assert inclusive physically correct estimand or causal weak-shower effect. Qualified hard-size2=136, size4=1; rejected cardinalities 3:1,4:33,5:4,6:16,7:2,8:5,10:2. Complete ancestry archived, not yet analyzed. 
# Disposition
Local certificate mech-s11-rot021-fourvector-certificate.json SHA256 5ede59371209dd4315394ae9e8fbda30296a239b5f32dffd96500fdae3d36f86; replay script mech_rot021_replay.py SHA256 df059cca6bd3f801efe0efb20a6a505df5d550f5127293e03398872ffb59fc7d (local deliverables, not repo claims). Next useful bounded analysis on existing records: source-native exact checker implementation and event genealogy/status semantics, isolate discrepancy between process record and later stages without assuming vertex interpretation; no new simulation needed before that. Stage1 G_E/P3 FAIL unchanged, P2/G_OVL/G_COV/W untested, STOP A HOLD. No new run, no BW write.
