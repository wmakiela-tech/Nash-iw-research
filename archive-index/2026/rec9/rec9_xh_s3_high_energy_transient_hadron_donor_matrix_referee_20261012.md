# REC9 / XH-S3 high-energy transient-hadron donor-matrix referee

RETURN_ID: REC9-XH-S3-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-REFEREE-001
TARGET: XH-S3-FRONTB-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-HARVEST-025
VERDICT: PASS_DONOR-GAP_MAP / REPAIR_DONOR-TO-SOURCE_INTERFACE_AND_SOURCE-COLUMN_SEMANTICS
SEVERITY: HIGH

## 1. Donor matrix — bounded-search verdict passes

The located hosts support the stated partial-coverage picture:
- HDMSpectra supplies ultra-high-scale stable-state spectra, including p/ap, but not transient pi/K/K0/neutron outputs.
- Aloisio-Berezinsky-Kachelriess supplies UHE pion/nucleon/all-hadron spectral information to very high scales.
- NNFF1.0/NPC23 supply identified charged pi/K/p information but have small-z limitations; NPC23 explicitly constrains pions lower in z than kaons/protons.
- HAPS 2026 supplies current charge-separated charged-pion/charged-kaon FFs.
- Xing-Bian-Cui-Roberts 2025 supplies pion/kaon/K0 cascade FF structure and multiplicity information but no adequate baryon sector.

Therefore:
NO SINGLE DONOR LOCATED THAT CLOSES THE FULL FRONT-B CONTRACT = PASS AS BOUNDED-HARVEST STATUS.

Do not promote this to:
NO SUCH DONOR EXISTS.

## 2. Main repair — fragmentation donor != PBH source

A donor FF/spectrum is not itself q_h(M).

A source-complete construction requires, schematically,

q_h(M)
=
sum_i integral dE [d2N_i^PBH/(dt dE)] Y_{i->h}(E; source contract),

with:
- PBH primary species/antiparticle weights i;
- greybody/threshold content;
- energy support;
- fragmentation/hadronization donor;
- small-z/total-multiplicity completion;
- transient-state definition;
- secondary-energy integration semantics.

Thus:
DONOR COVERAGE != SOURCE CLOSURE.
PATCHWORK FF COVERAGE != E2 automatically.

The harvest objects called E2_piK / E2_baryon are better typed as:
E2_CANDIDATE_DONOR_COMPONENTS,
until the PBH convolution and source-interface contract are actually constructed.

## 3. Source-column semantics — load-bearing exact code finding

The public Wu-Xu PYTHIA table generator aggregates:
- pipm: PDG +211 and -211;
- Kpm: PDG +321 and -321;
- proton: PDG +2212 and -2212;
- neutron: PDG +2112 and -2112;
- K0L: PDG 130.

The generated hadrons_from_PBH.dat therefore stores aggregate source columns:
Q = (Q_pipm, Q_Kpm, Q_K0L, Q_p/pbar, Q_n/nbar).

The downstream evolution then maps them nontrivially:
- Q_pipm is used as the source term for BOTH n_pi- and n_pi+;
- Q_Kpm is used as the source term for n_K-;
- Q_K0L -> n_K0L;
- the column named proton is used as source for n_pbar;
- the column named neutron is used as source for n_nbar.

Therefore:
GENERATOR SOURCE COLUMN != DOWNSTREAM REACTION SPECIES AUTOMATICALLY.

Harvest 025's vector
S=(S_pi,S_Kpm,S_K0L,S_pbar,S_nbar)
silently identifies aggregate generator columns with downstream reaction species.

That identification is not source-native until the split/projection convention is frozen and justified.

## 4. Correct interface object

Freeze two levels separately:

SOURCE-COLUMN VECTOR
Q=(Q_pipm,Q_Kpm,Q_K0L,Q_p/pbar,Q_n/nbar)

and a SOURCE-TO-REACTION map B producing the downstream reaction-species injection vector R.

Then:
R = B Q.

Any donor splice must either:
1. reproduce Q under the same aggregation convention and retain B; or
2. replace Q and B together with a newly validated species-resolved source contract.

Do not mix a charge-separated donor with the old aggregate B without an explicit map.

## 5. Charged pion/kaon consequence

HAPS provides charge-separated pi+/pi- and K+/K- FFs.

That is richer than the current Wu-Xu aggregate source interface.

But:
RICHER DONOR RESOLUTION != DROP-IN REPLACEMENT.

A charge-separated E2 must decide whether to:
- sum back to the old Q_pipm/Q_Kpm convention; or
- change downstream injection semantics.

Changing the latter is a model-interface change, not merely source-table regeneration.

## 6. Proton/neutron consequence

The public PYTHIA generator counts p and pbar together in the "proton" channel, and n and nbar together in "neutron".

Downstream currently injects those columns into antiproton/antineutron populations.

Therefore:
PROTON COLUMN != ANTIPROTON SOURCE BY LABEL.
NEUTRON COLUMN != ANTINEUTRON SOURCE BY LABEL.

This may be a symmetry/convention choice, but it must be stated and verified before a donor p/ap or nucleon spectrum is used as E2.

HDMSpectra's p/ap separation is therefore useful precisely as an audit component, not a direct replacement for the current aggregate nucleon columns.

## 7. K0L

Xing 2025 supplies K0/K0bar production structure, not automatically K_L source.

K0/K0bar -> K_L requires an explicit neutral-kaon mixing/propagation/decay convention consistent with BBN timing.

Thus:
K0/K0bar DONOR != K0L BBN SOURCE AUTOMATICALLY.

Harvest 025 correctly keeps K0L mapping open.

## 8. Small-z / total multiplicity

The small-z warning passes.

Wu-Xu needs total integrated hadron number rates.
A fixed-order moderate-z FF grid does not by itself control the z->0 contribution to total multiplicity.

NPC23 itself reports substantially deeper constraint for pions than for kaons/protons; the latter remain much less constrained at small z.

Thus:
HIGH-Q DGLAP EVOLUTION != TOTAL PBH HADRON RATE.

## 9. Uncertainty object

Vector-valued uncertainty is required, but a 5-scalar vector is still not generically sufficient.

A donor patchwork can induce:
- cross-species correlations;
- common primary-parton uncertainties;
- shared normalization;
- support-dependent singular additions;
- charge/particle-antiparticle correlations.

So the safe object is a JOINT SOURCE UNCERTAINTY SET / covariance-or-envelope contract on Q (and, if B changes, on B), not independent scalar multipliers by default.

Rec9 singular-support guard remains:
lambda_alt = m lambda0 + lambda_s.

## 10. Final status

SINGLE_HIGH_ENERGY_TRANSIENT_HADRON_DONOR_NOT_LOCATED = PASS_BOUNDED_SEARCH_ONLY.
HDMSPECTRA_FULL_FRONTB = NO.
UHE_PION_NUCLEON_DONOR = PASS_PARTIAL.
NPC23_NNFF = PASS_PARTIAL_SMALLZ_LIMITED.
HAPS_2026_PI_K = PASS_CURRENT_PARTIAL.
XING_2025_PI_K_K0 = PASS_STRONG_PARTIAL.
DONOR_COMPONENT_EQ_E2 = NO.
PBH_PRIMARY_CONVOLUTION = REQUIRED.
SOURCE_COLUMN_TO_REACTION_SPECIES_MAP = REQUIRED.
CURRENT_WUXU_AGGREGATION_SEMANTICS = LOAD_BEARING.
P_PBAR_AND_N_NBAR_COLUMN_TO_ANTINUCLEON_USE = REQUIRES_EXPLICIT_JUSTIFICATION.
K0L_BBN_MAPPING = OPEN.
TOTAL_SMALLZ_MULTIPLICITY = OPEN_LOAD_BEARING.
SOURCE_VALID_E2B = OPEN.
TERMINAL_SOURCE_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NOVELTY = NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration. Reopen only for a constructed PBH donor convolution, a frozen source-column->reaction map, or a source-valid E2 splice.
