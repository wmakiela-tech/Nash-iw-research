# XH-S3 / FRONT B — HIGH-ENERGY TRANSIENT-HADRON DONOR MATRIX HARVEST 025

**RETURN_ID:** `XH-S3-FRONTB-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-HARVEST-025`

## Result

No single located public donor closes the full Front-B high-energy transient-hadron source vector

`{pi±, K±, K0L, p/pbar, n/nbar}`

with simultaneous control of:
- ultrahigh primary scale,
- small-z / total multiplicity,
- species resolution,
- transient-BBN semantics.

`PATCHWORK COVERAGE != SOURCE-COMPLETE E2`.

## Firewall

- `STABLE FINAL-STATE SPECTRA != TRANSIENT BBN HADRON SOURCE`.
- `IDENTIFIED-HADRON FF != TOTAL MULTIPLICITY WITHOUT SMALL-z CONTROL`.
- `CHARGED K != K0L`.
- `PROTON/ANTIPROTON != NEUTRON/ANTINEUTRON`.
- `SMALL COUNT FRACTION != SMALL BBN DIRECTIONAL EFFECT`.
- `HIGH-Q EVOLUTION != EMPIRICAL VALIDATION AT HIGH Q`.
- `NO CANON / NO EXEC_SIGN / NO NOVELTY / NO PBH ENDPOINT`.

## 1. Donor A — HDMSpectra

Sources:
- https://github.com/nickrodd/HDMSpectra
- HDMSpectra paper / public release documentation.

Scope:
dark-matter fragmentation spectra from the electroweak scale to the Planck scale.

Direct code inspection shows allowed final states are stable SM species:
- e±,
- neutrinos / antineutrinos,
- gamma,
- p / pbar.

The public final-state list does not include:
- pi,
- K,
- K0,
- neutron.

Disposition:
- ENERGY SUPPORT = EXCELLENT.
- PROTON/ANTIPROTON = YES.
- PI/K/K0L/N = NO.
- TRANSIENT SPECIES = NO.
- E2 COMPLETE = NO.

Use:
- high-energy stable baryon/proton stress;
- UHE QCD/electroweak spectral cross-check;
- not a direct replacement for Wu–Xu transient-BBN hadron source.

## 2. Donor B — Aloisio–Berezinsky–Kachelriess 2003

Source:
https://arxiv.org/abs/hep-ph/0307279

They calculate QCD/SUSY-QCD fragmentation spectra up to primary energies of order 1e16 GeV with two independent methods:
- Monte Carlo;
- DGLAP evolution.

Reported comparison includes pion, nucleon and all-hadron spectra, with useful agreement over a broad small-x / moderate-x domain.

Disposition:
- PI = YES / UHE.
- NUCLEON = YES / UHE.
- K/K0L = NO.
- FULL DIRECTIONAL BBN VECTOR = NO.
- E2 COMPLETE = NO.

Use:
strong E1c UHE shape / small-x prior for pion+nucleon sectors.

## 3. Donor C — NNFF1.0 / NPC23

Sources:
- https://nnpdf.mi.infn.it/nnff1-0/
- https://doi.org/10.1103/PhysRevD.110.114019

Species:
- charged pions,
- charged kaons,
- protons/antiprotons.

NPC23 supplies modern collider constraints and public grids.

Load-bearing limitation:
small-z is not globally controlled by ordinary fixed-order identified-hadron fits. NNFF1.0 explicitly removes very small z where large timelike ln z terms require resummation. NPC23 likewise has species-dependent lower-z reach; pions are controlled substantially lower than kaons/protons.

Also:
- no K0L,
- no neutron/antineutron.

Disposition:
- PI± = YES.
- K± = YES.
- P/PBAR = YES.
- K0L = NO.
- N/NBAR = NO.
- SMALL-z TOTAL MULTIPLICITY = NOT CONTROLLED.
- E2 COMPLETE = NO.

Use:
- species-specific moderate-z stress;
- quark/gluon fragmentation uncertainty;
- charged pi/K/p composition at supported z;
- not total source closure.

## 4. Donor D — HAPS PiFF1.0 / KaFF1.0 (2026)

Source:
https://arxiv.org/abs/2606.16754

Current public FF sets:
- charge-separated pi+ / pi-,
- K+ / K-,
- NLO / NNLO grids.

Scientific value:
- current,
- charge-separated,
- improved recent COMPASS constraints,
- direct flavor separation.

Limitations:
- no proton/neutron sector,
- no K0L,
- gluon FF remains indirectly constrained,
- identified-hadron FF framework does not by itself close total low-z jet multiplicity.

Disposition:
- PI± = YES / CURRENT.
- K± = YES / CURRENT.
- K0L = NO.
- P/N = NO.
- LOW-z TOTAL MULTIPLICITY = NO.
- E2 COMPLETE = NO.

Use:
high-value current stress donor for charge/species composition on supported z.

## 5. Donor E — Xing–Bian–Cui–Roberts 2025

Source:
https://doi.org/10.1140/epjc/s10052-025-14924-1

This donor is unusually relevant because it builds hadron-scale FFs through coupled hadron-cascade equations for:
- pi±,
- pi0,
- K±,
- K0,
- K0bar.

It provides:
- whole-z theoretical structure,
- endpoint behavior,
- jet multiplicities,
- charged/neutral kaon multiplicity ratios,
- pion/kaon multiplicity evolution with reaction energy.

Limitations:
- baryon sector is not adequate for Front-B n↔p chemistry,
- p/pbar/n/nbar are not source-complete actors in the construction used here,
- high-Q PBH source matching is not established,
- this is a strong theoretical donor, not a validated Wu–Xu terminal-source replacement.

Disposition:
- PI±/PI0 = YES.
- K±/K0/K0bar = YES.
- P/N = NO.
- FULL-z THEORY = YES.
- HIGH-Q PBH VALIDATION = NO.
- E2 COMPLETE = NO.

Use:
best located E1c donor for pi/K/K0 multiplicity ratios and source curvature.

## 6. Critical baryon firewall

Small proton/antiproton yields in collider multiplicity contexts do not imply small BBN effect.

Wu–Xu includes antiprotons/antineutrons because their annihilation/conversion channels contribute directly to n↔p.

Therefore:

`BARYON FRACTION SMALL IN COLLIDER DATA != ANTI-NUCLEON CHANNEL NEGLIGIBLE IN BBN`.

This blocks promotion of a pi/K-complete donor to a complete BBN source.

## 7. K0L semantics

Charged-kaon FFs do not directly provide K0L.

A legal K0L source requires:
- K0 / K0bar production,
- neutral-kaon mixing / long-lived-state mapping,
- time/medium assumptions relevant to the early-BBN interaction stage.

Xing et al. is useful because it includes K0 and K0bar and neutral/charged multiplicity information.

But:

`K0 / K0bar FF != K0L BBN SOURCE automatically`.

## 8. Neutron / antineutron gap

None of the modern identified-hadron FF sets located here directly supplies the exact neutron/antineutron source vector required downstream.

- HDMSpectra supplies p/pbar only.
- NPC23/NNFF supplies p/pbar.
- Aloisio et al. supplies aggregate nucleon spectra.

A neutron source could be inferred via isospin assumptions in selected channels, but:

`ISOSPIN-ROTATED PROTON FF != SOURCE-VALIDATED NEUTRON FF`

for an evolving Hawking mixture with changing flavor thresholds.

Thus n/nbar remains a real coverage gap.

## 9. Small-z is the key technical barrier

Wu–Xu source table uses total species number rates `dN_h/dt`.

Total multiplicity corresponds schematically to integration of `D_i^h(z,Q)` toward the infrared/small-z support.

This is precisely where:
- fixed-order timelike splitting functions develop large ln z terms,
- phenomenological FF fits become weakly constrained,
- hadron-mass/coherence/resummation effects matter.

Therefore:

`HIGH-Q FF EVOLUTION != TOTAL PBH HADRON RATE`.

A legal total-source donor must control:
- low-z resummation/coherence,
- hadron-mass / cutoff semantics,
- species multiplicity.

## 10. Donor matrix summary

HDMSpectra:
- ENERGY +++
- UHE stable spectra +++
- pi -
- K -
- K0 -
- p/pbar +
- n/nbar -
- transient BBN semantics -

Aloisio et al.:
- ENERGY +++
- small-x ++
- pi +
- K -
- K0 -
- nucleon aggregate +
- charge/directional resolution -
- transient BBN semantics partial/analogy

NPC23 / NNFF:
- high-Q evolution ++
- empirical species ++
- pi +
- K +
- p/pbar +
- K0 -
- n -
- small-z total multiplicity -

HAPS 2026:
- currentness +++
- pi charge +
- K charge +
- p/n -
- K0 -
- small-z total multiplicity -

Xing 2025 cascade:
- pi +++
- K +++
- K0/K0bar +++
- small-z theoretical structure ++
- jet multiplicity ++
- p/n -
- PBH high-Q source validation -

No row has all required columns.

## 11. Consequence for E2

No located plug-in E2 donor can replace the Wu–Xu terminal source vector wholesale.

Typed hierarchy:

### E2_piK
Cross-check pi/K/K0 using:
- Xing cascade model,
- HAPS charge-separated FFs at supported z,
- UHE QCD multiplicity prior.

### E2_baryon
Cross-check p/pbar using:
- NPC23/NNFF,
- HDMSpectra where semantics overlap,
- UHE nucleon donor as broad shape prior.

### E2_n
Retain neutron/antineutron uncertainty or isospin assumption as a separate typed component until independently constrained.

Then propagate component-wise source uncertainty through exact directional rates rather than collapsing everything to one scalar source error.

## 12. Component-wise source uncertainty

Let

`S(t)=(S_pi,S_Kpm,S_K0L,S_pbar,S_nbar)`.

A legal stress model is vector-valued:

`S_alt,h = m_h(t) S0,h + S_singular,h`.

Do not impose one common multiplicative `m(t)` unless a donor actually supports common scaling.

This retains Rec9's support correction:
new validated support may contain a term not absolutely continuous with baseline E0.

## 13. New-support issue

Extended energy/hadronization support can create hadrons from primary-energy regions where the baseline truncated generator has no contribution.

Then:

`lambda_alt = m lambda0 + lambda_s`.

The `lambda_s` term cannot be represented by `q_alt/q_0`.

Therefore:

`MULTIPLICATIVE EDGE-SLOPE STRESS`

is incomplete once E2 expands legal support.

## 14. Bounded hybrid validation

A non-production cross-check may compare at one or two PBH masses:

A. current Wu–Xu/PYTHIA supported component;

B. Xing-type pi/K/K0 multiplicity continuation;

C. modern FF-supported moderate-z pi/K/p contribution;

D. UHE-QCD pion/nucleon shape prior.

First compare:
- species ratios,
- total multiplicity on common support,
- charged/neutral kaon ratio,
- pion/nucleon ratio,
- sensitivity to low-z cutoff.

Do not jump directly to Yp endpoint.

If donors disagree on common support, source uncertainty is already load-bearing.

If they agree on common support but differ in unsupported low-z/high-E tails, uncertainty can be localized.

## 15. Model-use discipline

No additional AI model was invoked.

Useful diversity came from external scientific models/hosts:
- global fragmentation fits,
- DGLAP/UHE calculations,
- hadron-cascade theory,
- HDMSpectra.

This adds independent scientific structure without additional Moderator-facing AI coordination.

## 16. Status

`SINGLE_HIGH_ENERGY_TRANSIENT_HADRON_DONOR = NOT LOCATED`.

`HDMSPECTRA_AS_FULL_FRONTB_DONOR = REJECTED / STABLE_FINAL_STATES_ONLY`.

`UHE_QCD_PION_NUCLEON_DONOR = PASS PARTIAL`.

`NPC23_NNFF_IDENTIFIED_HADRON_DONOR = PASS PARTIAL / SMALL-z LIMITED`.

`HAPS_2026_PI_K_DONOR = PASS CURRENT PARTIAL`.

`XING_2025_PI_K_K0_CASCADE_DONOR = PASS STRONG PARTIAL`.

`NEUTRON_ANTINEUTRON_SOURCE = OPEN`.

`K0L_BBN_MAPPING = OPEN`.

`TOTAL_SMALL-z_MULTIPLICITY = OPEN / LOAD-BEARING`.

`PATCHWORK_DONORS = USEFUL ONLY WITH TYPED COMPONENT-WISE UNCERTAINTY`.

`SOURCE_VALID_E2B = OPEN`.

`TERMINAL_SOURCE_PHYSICAL_VALIDATION = OPEN`.

`LOG_FLOOR = SECONDARY`.

`PBH_DE_DYNAMIC_ACCURACY = OPEN`.

`PBH_Yp_DH_TARGET_VALIDATION = OPEN`.

`SOURCE_MATCHED_K_PBH = UNDEFINED`.

`NO PBH BOUND / NO ENDPOINT RELEASE / NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST`.
