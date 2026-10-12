# REC9 / XH-S3 PBH-QCD ASYMPTOTIC SOURCE SCALING REFEREE

RETURN_ID: REC9-XH-S3-PBH-QCD-ASYMPTOTIC-SOURCE-REFEREE-001
TARGET: XH-S3-FRONTB-PBH-QCD-ASYMPTOTIC-SOURCE-SCALING-PRIOR-HARVEST-023
VERDICT: PASS_TOTAL-MULTIPLICITY_ASYMPTOTIC_LOGIC / REPAIR_SPECIES-SPECIFIC_AND_FORMAL-ASymptotic_CLAIM_CEILING
SEVERITY: MEDIUM

## 1. Primary Hawking number-rate scaling

For a Schwarzschild PBH in the semiclassical regime, with effectively massless saturated species and no new thresholds, T_BH is proportional to M^{-1}. After changing variable E=x T_BH in the integrated Hawking number rate, the leading number-rate scaling is proportional to T_BH and therefore M^{-1}.

PASS, with domain:
SEMICLASSICAL SCHWARZSCHILD + SATURATED EFFECTIVELY MASSLESS SPECIES + FIXED PARTICLE CONTENT.

PRIMARY NUMBER RATE M^{-1} is not a theorem through arbitrary new thresholds or into the Planck regime.

## 2. Total jet multiplicity asymptotics

The mature running-coupling QCD multiplicity form used by XH,
Nbar(Q) ~ exp[A sqrt(ln(Q/Lambda))]
up to pre-exponential/subleading terms,
is sub-power in Q.

Therefore for a TOTAL secondary multiplicity model of the schematic form
q_tot(M) ~ M^{-1} Nbar(Q~1/M),
one gets
p_eff = d ln q_tot / d ln M
= -1 - A/[2 sqrt(ln(Q/Lambda))] + subleading,
and formally p_eff -> -1 as Q -> infinity.

PASS as mature-host asymptotic logic.

The illustrative values in harvest 023 are internally consistent with the stated DLA formula.

## 3. Main repair — total multiplicity does not prove species-specific asymptotics

Front B does not use only total hadron multiplicity. It needs transient identified species:
pi, K, K0L, p/pbar, n/nbar.

Write
q_h(M) = q_tot(M) f_h(Q),
where f_h(Q) is the species fraction/yield map.

Then
p_eff,h = p_eff,tot - d ln f_h / d ln Q
because Q is proportional to 1/M.

Therefore the total-multiplicity theorem alone does NOT prove that every identified q_h has p_eff,h -> -1.

To promote the species-specific claim one needs an additional source/host statement controlling f_h(Q), for example that it approaches a nonzero constant or varies only sub-power in the relevant asymptotic regime.

Thus repair:

TOTAL QCD MULTIPLICITY SUB-POWER
!=
SPECIES-SPECIFIC METASTABLE YIELD SUB-POWER AUTOMATICALLY.

Accordingly:
"NO FIXED p<-1 CAN BE THE EXACT QCD ASYMPTOTIC LAW" is earned for the total-multiplicity schematic class under the stated assumptions, but is NOT established species-by-species from the cited multiplicity result alone.

## 4. Formal asymptotic domain repair

Literal M -> 0 is not a physical asymptotic domain of the semiclassical Schwarzschild Hawking + perturbative-QCD model.

At sufficiently small M / sufficiently high T:
- new particle thresholds may enter;
- the assumed particle content may change;
- ultimately semiclassical Hawking theory itself loses validity near the quantum-gravity/Planck regime.

Safer language:
FORMAL Q -> infinity / decreasing-M ASYMPTOTIC WITHIN THE ASSUMED SEMICLASSICAL-QCD MODEL.

Do not write "exact physical M->0 asymptote".

This does not weaken the practical criticism of a fixed -1.20 continuation across many unsupported decades.

## 5. Finite-range DLA illustration

The finite-range calculation is correctly labelled illustrative.

With the stated DLA coefficient, normalization at the supported edge can produce a curved source that is steeper than E0 over part of the finite terminal window.

Therefore:
ASYMPTOTIC p_eff -> -1
does NOT determine the finite-window sign of
delta q = q_true - q_E0.

FINITE_TERMINAL_ERROR_SIGN_E0 = UNKNOWN remains correct.

This is especially true species-by-species.

## 6. Stress-family semantics

E1b is scientifically useful as a curved SHAPE STRESS FAMILY.

But "prior" should not be read as a calibrated probability prior or uncertainty distribution.

Safe label:
QCD-MOTIVATED CURVED STRESS FAMILY / NOT SOURCE CLOSURE / NOT ERROR BAR.

Its role is to defeat false confidence from one fixed-power extrapolator and to motivate direct source regeneration.

## 7. Near-edge validation leverage

The claim that roughly 1e8-1e9 g is highest leverage is valid only relative to the current E0 unweighted sub-edge count and the already-derived evaporation weighting.

It is not yet:
- highest Yp/D-H target leverage;
- highest species-composition leverage;
- a bound on deep-tail importance.

Therefore keep:
HIGHEST E0 UNWEIGHTED SOURCE-VALIDATION LEVERAGE.

Do not shorten to universal "highest validation leverage".

## 8. BlackHawk v3 placement

Current BlackHawk v3 documentation emphasizes additional black-hole geometries, temperatures/greybody factors, primary Hawking spectra, and numerical improvements.

Nothing in the located v3 material closes the source-native early-BBN transient pi/K/anti-N hadronization contract.

Thus harvest 023 is safe to retain:
BLACKHAWK_V3_CURRENTNESS != TERMINAL METASTABLE-HADRON SOURCE VALIDATION.

## 9. Final status

PBH_PRIMARY_NUMBER_HIGH_T_SCALING_M_MINUS_1 = PASS_WITH_SEMICLASSICAL_DOMAIN.
QCD_TOTAL_MEAN_JET_MULTIPLICITY_SUBPOWER = PASS.
TOTAL_SECONDARY_EFFECTIVE_EXPONENT_TO_MINUS_1_FORMALLY = PASS_WITH_DOMAIN.
SPECIES_SPECIFIC_q_h_EXPONENT_TO_MINUS_1 = NOT ESTABLISHED FROM TOTAL MULTIPLICITY ALONE.
FIXED_E0_MINUS_1P20_AS_EXACT_TOTAL_QCD_ASYMPTOTE = REJECTED WITHIN ASSUMED FORMAL MODEL.
FIXED_E0_MINUS_1P20_AS_EXACT_SPECIES_ASYMPTOTE = NOT ESTABLISHED / DO NOT OVERCLAIM REJECTION BASIS.
FINITE_TERMINAL_ERROR_SIGN_E0 = UNKNOWN.
QCD_CURVED_STRESS_FAMILY = JUSTIFIED AS SHAPE STRESS / NOT ERROR BAR.
NEAR_EDGE_1E8_TO_1E9G = HIGHEST E0 UNWEIGHTED SOURCE-VALIDATION LEVERAGE ONLY.
DIRECT_E2_SOURCE_VALIDATION = NOT RUN.
TERMINAL_SOURCE_PHYSICAL_VALIDATION = OPEN.
HIGH_ENERGY_METASTABLE_BBN_HADRONIZATION = OPEN.
PBH_DE_DYNAMIC_ACCURACY = OPEN.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NOVELTY_CANDIDATE = NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration. Reopen only for identified-species high-energy source control, direct E2 regeneration, or a stronger asymptotic/source-validation claim.
