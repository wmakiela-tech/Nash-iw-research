---
artifact_id: IW_MECH_S11_ROT017_STOPA_UP_OFF_PEV_ENERGY_RESIDUAL_SELECTION_AND_P1_DIAGNOSTIC_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
status: PARTIAL_NATIVE / G_E_FAIL / P1_UP_OFF_DIAGNOSTIC_ONLY
claim_ceiling: NO_STOPA_CLOSURE / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Actual custody and execution
Run 45703311781 job 139518753066 (up off) complete failure; other three arms in progress at last read. Artifact 15064625969 760684 bytes downloaded; local ZIP SHA256 d4f7db13fea7d4d8b86d51e5bad76df85c8cb51d1d2d31b775d2cae97eba065e matches provider; CRC PASS and 16/16 manifest entries and complete coverage verified. Prior up off artifact 15064287358 independently reopened; 24/24 manifest entries and coverage verified. Both wheels SHA256 0ebe2dff962631571100dc427fbaa95e388df054ac06cdc8f63b31af07eb3de8. Both new cells completed 2000 events, CELL_RC records 2,2 and TIMELINE START/END both: corrected Bash handling works. No repeat or changed physics. Total accessible study events 32000 (prior 28000 + 4000); other 8 cells not yet accessible, not assumed completed.
# Direct raw replay of full up off arm, 12000 events
Computed from all six actual CSVs in local Python, checked per-cell counts against JSON and zero charge violations. Define r=Efinal_over_2E-1, bad=abs(r)>1e-6, pion multiplicity per primary (n_211+n_-211)/2.
| E GeV | bad + | bad - | mean signed r | pion mean | SE |
|---:|---:|---:|---:|---:|---:|
|10000|0|0|2.1280943674e-12|58.803|.5343219727|
|30000|0|0|2.0164758752e-14|81.97125|.7523537514|
|100000|0|0|-1.6977795203e-10|118.15575|1.1135575035|
|300000|2|4|-4.1761764925e-9|166.272|1.6267950821|
|1000000|136|146|-5.2607974343e-9|224.87675|2.2348362275|
|2000000|357|368|2.0776957131e-8|277.609|2.7362889921|
New high-energy cells all charge pairs G_QS true from exported summaries. Maximum abs r 1.1792040521374503e-5 and 4.150721102935684e-5; exceedance 14.10%,36.25%. Both signs frequent; mean small relative to tails, not systematic energy loss. Cause undetermined; no particle-level full event record or internal generator conservation audit. Energy-scale dependence is evidence on this run, not general PYTHIA theorem.
# New selection diagnostic
At 1 PeV, good vs bad mean pion multiplicity 228.44121071012805 vs 203.1613475177305; at 2 PeV 294.45254901960783 vs 247.98758620689654. Deleting bad events would raise per-primary pion mean by 1.585073% and 6.067364% respectively. Pearson correlation abs(r) vs event pion count -0.1040427 and -0.1514461. This is descriptive posthoc evidence of selection bias, not a correction; all events kept, strict G_E FAIL persists.
# P1 diagnostic
Badacz PREREG129 predicts off-arm pion log slope over E'=1e5..2e6 GeV in [.22,.34] for both u,g. For u off endpoint secant log(277.609/118.15575)/log(20)=.2851422962591652, first-order independent MC SE .004552220202589496. Within predicted interval on ALL retained events, but 2 PeV endpoint G_E FAIL, therefore diagnostic agreement only, not admissible P1 PASS; gluon endpoint unavailable. No assertion local derivative throughout interval. No physical validation. No splot, no response W, no G_OVL/G_COV, no STOP A closure, no BW write. 
