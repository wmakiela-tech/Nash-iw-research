---
artifact_id: XH-S3-FRONTB-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-HARVEST-025
bw_ingestion_event_id: ING-20261012-0037
bw_qualification_state: SOURCE_HARVEST_PARTIAL_DONORS
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_LINK_UPDATE
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMSkIDDgrj_9icqltgeAGMNQkn_jC3H9R11hyFGJuPOEo6w_3mt31hJppU_ZeKMrU1xS91wXoQjVmuRz24en6hsBsNH1jlM1LDlJhEA
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-HARVEST-025

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

XH-S3 / FRONT B — HIGH-ENERGY TRANSIENT-HADRON DONOR MATRIX HARVEST 025
RETURN_ID
XH-S3-FRONTB-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-HARVEST-025
CORE RESULT
No single located public donor closes the full high-energy Front-B transient-hadron source vector:
{pi±, K±, K0L, p/pbar, n/nbar}
with simultaneous control of ultrahigh scale, small-z/total multiplicity, species resolution and BBN transient semantics.
PATCHWORK COVERAGE != SOURCE-COMPLETE E2.
DONOR MATRIX
A. HDMSpectra
- ultrahigh-Q support: strong;
- public final states: stable e±, neutrinos, gamma, p/pbar;
- no pi/K/K0/neutron final-state outputs.
DISPOSITION: useful UHE stable-baryon/spectral stress donor; NOT a transient-BBN source replacement.
B. Aloisio–Berezinsky–Kachelriess 2003
- QCD/SUSY-QCD fragmentation to primary energies up to ~1e16 GeV;
- Monte Carlo vs DGLAP agreement reported for pion, nucleon and all-hadron spectra over roughly x~1e-5 to <=0.3.
DISPOSITION: strong UHE pion+nucleon shape prior; no kaon/K0L and insufficient directional species decomposition for full Front B.
C. NNFF1.0 / NPC23
- identified charged pi, K, p/pbar FFs;
- modern uncertainty sets/public grids;
- small-z control is limited; fixed-order fits explicitly cut away regions where ln z effects require resummation;
- no K0L or neutron.
DISPOSITION: moderate-z identified-species stress donor, not total PBH multiplicity closure.
D. HAPS PiFF1.0 / KaFF1.0 (2026)
- current charge-separated pi+/pi- and K+/K- public LHAPDF grids;
- improved 2025/2026 COMPASS constraints;
- no p/n/K0L;
- gluon FF remains indirect in SIA+SIDIS.
DISPOSITION: high-value current pi/K composition donor on supported z; not E2-complete.
E. Xing–Bian–Cui–Roberts 2025
- coupled hadron-cascade construction for pi±, pi0, K±, K0, K0bar;
- entire-z theoretical construction;
- correct endpoint discussion;
- jet multiplicities and charged/neutral kaon multiplicity predictions;
- no baryon sector adequate for Front-B n<->p chemistry.
DISPOSITION: strongest located pi/K/K0 small-z/multiplicity prior; still partial.
LOAD-BEARING GAPS
1. SMALL-z
Wu-Xu uses total species number rates dN_h/dt. Total multiplicity depends on integration toward small z, exactly where ordinary global FF fits lose empirical/perturbative control unless resummation/coherence and hadron-mass semantics are included.
Thus:
HIGH-Q FF EVOLUTION != TOTAL PBH HADRON RATE.
2. K0L
Charged-kaon FFs do not directly supply K0L. Need explicit K0/K0bar production plus neutral-kaon mixing/long-lived-state mapping.
3. NEUTRON / ANTINEUTRON
No located modern identified-hadron FF donor gives the exact n/nbar source vector required downstream. Aggregate nucleon or isospin-rotated proton assumptions are not source validation.
4. ANTI-NUCLEON IMPORTANCE
Small baryon yield does not imply small BBN effect. Wu-Xu anti-nucleon channels enter n<->p directly with large strong-interaction rates.
UPDATED E2 TYPING
E2_piK:
use Xing 2025 + HAPS/current FFs + UHE QCD prior to constrain pi/K/K0 composition and curvature.
E2_baryon:
use NPC23/NNFF + HDMSpectra + UHE nucleon prior where semantics overlap.
E2_n:
keep neutron/antineutron uncertainty explicit until independently constrained.
Source uncertainty must remain vector-valued by species:
S=(S_pi,S_Kpm,S_K0L,S_pbar,S_nbar).
Do not collapse to one common multiplicative factor unless a donor supports it.
Rec9 correction retained:
an extended source can introduce new support not absolutely continuous with baseline.
Use:
lambda_alt = m lambda0 + lambda_s.
Small multiplicative error on old support does not control lambda_s.
CURRENT STATUS
SINGLE_HIGH_ENERGY_TRANSIENT_HADRON_DONOR = NOT LOCATED.
HDMSPECTRA_FULL_FRONTB = NO.
UHE_PION_NUCLEON_DONOR = PASS PARTIAL.
NPC23_NNFF = PASS PARTIAL / SMALL-z LIMITED.
HAPS_2026_PI_K = PASS CURRENT PARTIAL.
XING_2025_PI_K_K0 = PASS STRONG PARTIAL.
NEUTRON_ANTINEUTRON_SOURCE = OPEN.
K0L_BBN_MAPPING = OPEN.
TOTAL_SMALL-z_MULTIPLICITY = OPEN / LOAD-BEARING.
SOURCE_VALID_E2B = OPEN.
TERMINAL_SOURCE_VALIDATION = OPEN.
NO PBH ENDPOINT / NO BOUND / NO CANON / NO EXEC_SIGN / NO NOVELTY.
MODEL-USE DISCIPLINE
No additional AI model invoked. The useful “other models” in this rotation were scientific models/hosts: FF fits, UHE DGLAP/MC, hadron-cascade theory and HDMSpectra. This added source diversity without Moderator-facing AI coordination.
SOURCES
HDMSpectra public code + paper
Aloisio–Berezinsky–Kachelriess 2003
NNFF1.0
NPC23 2024
HAPS PiFF1.0 / KaFF1.0 and 2026 paper
Xing–Bian–Cui–Roberts 2025
