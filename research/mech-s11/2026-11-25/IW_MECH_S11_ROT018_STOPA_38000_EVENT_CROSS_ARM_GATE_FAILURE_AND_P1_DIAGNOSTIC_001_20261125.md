---
artifact_id: IW_MECH_S11_ROT018_STOPA_38000_EVENT_CROSS_ARM_GATE_FAILURE_AND_P1_DIAGNOSTIC_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
status: PARTIAL_NATIVE / G_E_FAIL / P1_DIAGNOSTIC_BOTH_OFF_ARMS
claim_ceiling: NO_STOPA_CLOSURE / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Actual direct custody
Read seven downloaded original ZIPs locally, provider ZIP SHA exact, CRC PASS, full manifest coverage 131/131 hashes. Original 4 artifact identities recorded ROT016 aef5c51d90e7df497ae13929fa0fb15d26a89797. Continuation run 45703311781 artifacts up off 15064625969 (d4f7db13fea7d4d8b86d51e5bad76df85c8cb51d1d2d31b775d2cae97eba065e), up on 15062869783 (05ce2aa7d60c9e88f7ee809bc5a38fea1c969946c7db009837fb61dd5549efa6), gluon off 15063813273 (0eea5a8d9f4835dd451dd3d77c85164213f0846f69176dea7dcf2ff527552b83). g on still in progress at final read. All 19 available cells distinct, 2000 accepted each. Recomputed counts, signed charge, energy, paired charge asymmetry, pion means/SE, count sum and cross-product matrices from actual CSVs, matched exported event/energy/charge counts and pion means. 38000 accepted; 2376 G_E exceedances, 1179 positive and 1197 negative; zero net charge3 violations; 76/76 paired charge tests pass. 10/19 cells G_E pass. No generator failures among available cells. Local machine certificate mech-s11-rot018-partial-certificate.json SHA256 0e1a7555307ac47a686da52271441e94183501dcfd36ea39a3daed9f9815bc69 (local deliverable, not claimed repo stored).
# New cells
|arm,E TeV|G_E bad /2000|pion per-primary mean|SE|positive/negative energy residual exceedances|change after hypothetical bad-event deletion|
|---|---:|---:|---:|---|---:|
|u on,1000|277|231.63925|2.25841728|141/136|+2.80761%|
|u on,2000|757|278.93975|2.88108520|378/379|+4.18315%|
|g off,2000|258|527.952|3.64142916|131/127|+1.60305%|
Each FAIL, retained; all newly attempted cells complete, no rerun. u on rejected 1029/3029 and 1114/3114 attempts, u off zero. Conditional accepted means only; no inclusive interpretation. 
Full energy violation rates at E=10,30,100,300,1000,2000 TeV: u off 0,0,0,.3,14.1,36.25%; u on 0,0,0,.15,13.85,37.85%; g off 0,0,0,0,3.35,12.9%. g on 10 TeV .05%, remaining unknown. Energy residual exceedances occur with weakShower off and on; no unique causal explanation. Negative event-count correlation with abs residual in all 19 cells; posthoc descriptive, not proof causal. No sample deletion.
# P1 diagnostic
Owner PREREG129 frozen alpha pion .22..34 both off arms. Endpoint secants between 100 and 2000 TeV u off .2851422962591652 ± .004552220202589496; g off .2883426590120842 ± .003200521038200493; u on exploratory .2812668926332931 ± .0047483008038421886. SE first-order independent MC endpoints. All within band but PeV endpoint G_E FAIL; not admissible P1 PASS and not local derivative over interval. H1/H2 unaffected. No G_OVL/G_COV/W or splot. 
# Next scientifically useful check
After complete data inventory, distinguish recorded nominal beam energy from actual event initial-system four-momentum and generator internal conservation checker. Requires separate diagnostic with full event record, independent seeds, before-output design; no replacement of frozen failed cells. Investigate potential numerical cancellation/boost or event bookkeeping; currently unproven. Avoid reruns or relaxed threshold as retrospective repair. No BW write.
