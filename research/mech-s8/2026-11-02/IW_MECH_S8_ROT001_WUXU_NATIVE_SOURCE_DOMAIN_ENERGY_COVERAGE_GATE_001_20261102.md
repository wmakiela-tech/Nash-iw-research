---
artifact_id: IW_MECH_S8_ROT001_WUXU_NATIVE_SOURCE_DOMAIN_ENERGY_COVERAGE_GATE_001_20261102
created_at: 2026-11-02
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: SOURCE_NATIVE_DOMAIN_AND_KINEMATIC_ACCOUNTING_ONLY / NO_HADRON_SOURCE_VALIDATION / NO_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT001 — Wu–Xu original input-domain and subedge energy gate

**Function:** SOURCE/APPARATUS → MECHANISM → LEGAL TRANSFER → CHEAP FALSIFIER → SOURCE_BLOCK → OWNER DISPOSITION.

## Source, precedent and currentness

Original Wu–Xu arXiv:2509.05618 / JCAP02(2026)063, author source Fenyutanchan/Primordial-Black-Hole pinned commit d395183674cace6c9906a8911bdeb7234ba4040d. Main scan parameters blob 53faee65beda383348580c28d0424188da69b660: 100 logarithmically spaced initial masses from 6e8 to 1e10 gram. Hadronic source table blob 06d0883a27b108692720422294ba2baacd381a64: 100 rows, first mass 5.609588603804452e32 GeV, corresponding to about 1e9 gram. Original main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6 uses entire charged-pion column in BOTH pi-minus and pi-plus population source terms, the charged-K column for K-minus and entire proton/neutron columns for individual anti-proton/anti-neutron populations. Independent source/charge semantics: BADACZ REVIEW044 T1 FIRST, MT14 ROT021/022/023; native Julia 10D was previously run project-wide by Mech-S6 and Badacz. SCOPE9 TOPDOWN016/017, Badacz T2/T3 and AUD1 ROT021 leave strict numerical endpoint error and figure provenance pending.

## Single bounded calculation

For initial mass M0 and tabulated source edge Me = 1e9 gram, monotonic complete evaporation with negligible final mass gives F_subedge = min(1, Me/M0): fraction of ALL emitted rest-mass energy released after the instantaneous PBH mass falls below the tabulated hadronic-source domain. This is an energy/mass accounting identity, NOT the fraction of hadron yield, hadron deposited energy, BBN sensitivity or observable effect. With a remnant Mr < Me and M0 > Me, replace by (Me - Mr)/(M0 - Mr).

Selected author zero-based scan indices:

| j | initial mass [gram] | total gross emitted energy below source edge |
|---:|---:|---:|
| 0 | 6.000000e8 | 100% |
| 17 | 9.726658e8 | 100% |
| 18 | 1.000704e9 | 99.93% |
| 22 | 1.121174e9 | 89.19% |
| 24 | 1.186744e9 | 84.26% |
| 99 | 1.000000e10 | 10.00% |

Of 100 initial masses, 18 start beneath the tabulated hadron source floor; at 43 grid points at least half of total gross emitted energy occurs after crossing the floor. Thus the description 'subedge is automatically only a negligible TOTAL-energy tail' is falsified in these input regimes. This does not, without physical spectra and reaction transfer, imply anything quantitative about the hadronic target. Badacz native V2 already established sensitivity in a separate model comparison; no novelty or first-priority claim here.

## Physical admission disposition

**HOLD/SOURCE_BLOCK** for Front-B source-valid physical Yp/DH/PBH bounds. The one remaining priority source-native object is E4: reliable sub-1e9-g hadron production with spin-dependent greybody factors, heavy t/W/Z/H primary channels, source-generator/table identity and valid source→reaction transfer. After E4, require paired author-native Julia10D, numerical/root error certificate and independent physical BBN endpoint (Yp,D/H), with Fig5 paper/version provenance separately resolved. No substitute perturbation ROT038.

Author source→reaction type audit is source-code evidence and does not prove published Figure 5 used that exact code/version. BlackHawk v2.3 official table byte identity not established. No Julia/BlackHawk/PYTHIA execution in this return. No physical claim promotion or owner/REC/AUD/BW acceptance.

## Reproduction

Standalone Python >=3.11, stdlib only: mech_s8_rot001_wuxu_native_mass_domain_gate.py, colocated here. Local run PASS; assertions 18/100 and 43/100. Local script SHA-256: 612828b997025f0b19533afe0f68e73e482bd514363a2056748415e1f4642d74; generated JSON SHA-256: 501a6922684534754181d242c5f399a258a80ceb3b24f0eb44cb2e42b307c24b (JSON currently in local handoff, not asserted published in repository). Source input values pinned above; no independent runtime source download in script.

NO_NOVELTY / NO_PHYSICAL_SOURCE_ADMISSION / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN.