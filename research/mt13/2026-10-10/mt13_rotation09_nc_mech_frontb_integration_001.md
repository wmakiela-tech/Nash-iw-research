---
artifact_id: MT13-ROTATION09-NC-MECH-FRONTB-INTEGRATION-001
bw_ingestion_event_id: ING-20261010-0096
bw_qualification_state: FRONTB_NC_MECH_OWNER_INTEGRATION
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: OWNER_SCIENTIFIC_PROGRAM_METHODOLOGY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MT13-ROTATION09-NC-MECH-FRONTB-INTEGRATION-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

IW / MT13 — ROTATION 09
NC + MECH-S6 FRONT B INTEGRATION; CONSERVATION / BRANCHING / FEEDBACK CEILING
2026-10-10
CURRENTNESS
LT3 DRAFT013 active; REV020 authored; P2 provisional, P3 live; no T2 execution, no novelty or EXEC. NC response NC-MT13-FRONTB-DE-CLOSURE-ADMISSION-AUDIT-001 received (2026-10-10 21:06 CEST): [PRIVATE_DRIVE_LOCATOR_REDACTED] Mech-S6 return: [PRIVATE_DRIVE_LOCATOR_REDACTED]
INTEGRATION VERDICT
NC and Mech are complementary, not competing universal certificates. NC supplies a sharper exact integrated-yield identity for prescribed scalar depletion; Mech supplies tracking/contractivity/target-propagation sufficient bounds for more general feedback. Neither validates PBH-B2 source-native adapter, multi-species cross-feeding or numerical BBN endpoint.
EXACT SCALAR RESULT / PROOF
For dn/dt=S(t)-Gamma(t)n, Gamma>0, define b_c(t)=Gamma_c(t)/Gamma(t), 0<=b<=1, sum_c b_c=1. Then Gamma n=S-dot n. For [t0,t1]:
Y_total_exact=integral Gamma n dt=integral S dt - [n(t1)-n(t0)].
Y_c_exact=integral b_c Gamma n dt=integral b_c S dt - [b_c n]_(t0)^(t1) + integral dot b_c n dt.
Thus Y_c_exact - Y_c_DE = -[b_c n]_(t0)^(t1) + integral dot b_c n dt, where Y_c_DE=integral b_c S dt. For constant b_c and n(t0)=n(t1)=0, channel integrated yield is exactly equal even when instantaneous tracking fails badly. For bounded variation b_c and vanishing endpoints, |error|<=sup_t n(t) TV(b_c). For jumps, interpret integral as Stieltjes, with the usual continuity assumptions on n. This is mature mass-balance/integration-by-parts mathematics. Fast source variation alone does not invalidate integrated yield.
CRITICAL DOMAIN FIREWALL
1. In an expanding universe the physical-density equation is dot n+3H n=S-Gamma n. Using N=a^3 n and Q=a^3 S yields dot N=Q-Gamma N. Therefore integrated physical reaction events per comoving volume are integral Gamma N dt, and integrated injection is integral Q dt. A naive unweighted integral Gamma n dt is not the comoving conserved yield. The physical quasi-static state is S/(Gamma+3H), not always S/Gamma.
2. If the target is a time-weighted n/p response or final Yp, D/H, equality of total channel event counts DOES NOT imply equality of final abundances. Even constant branching can have different temporal reaction profiles; a network sensitivity kernel K_c(t) gives target deviation integral K_c(t) [Gamma_c n - b_c S] dt, not generally zero. For constant b, integration by parts gives nonzero integral dot K_c b n plus boundary. NC exact channel-yield result is not a target-error certificate.
3. If Gamma depends on nucleon state, hadron density, cross-feeding or feedback, prescribed-Gamma scalar proof does not provide an admissible equilibrium approximation. An exact mass-balance identity may still hold for full coupled dynamics if source/sink accounting closes, but closure approximation, fixed-point existence and target error remain unproved.
4. Inner iteration n*=S/Gamma(n*) has local derivative T'(n*)=-d ln Gamma/d ln n at the fixed point (for fixed S); |T'|<1 is local sufficient contraction, not a global existence/uniqueness theorem, and failure of this condition does not prove absence of all fixed points. For NC self-shielding Gamma0(1+n/nc)^(-q), q>=1 nonexistence depends also on source level; do not generalize to arbitrary q>=1 without checking S/Gamma0 versus nc and q=1 borderline.
5. TV bound controls integrated channel count only. Its RHS must be compared in consistent units to channel-count tolerance, not directly to dimensionless Yp or D/H tolerance without a certified network response map.
6. Multi-species feed-down and channel-threshold variation may violate the single-species partition assumption.
PROGRAMME DECISION
RETAIN: exact prescribed-Gamma integrated-channel conservation and BV branch-error certificate as a diagnostic/source-independent host control.
REPAIR: DRAFT013 epsilon_DE<<1 is sufficient heuristic for instantaneous tracking, not necessary for integrated channel yield. Gamma>>H addresses physical-density approximation and does not alone establish time tracking.
BLOCK: upgrade of NC integrated-yield equality to Yp/DH endpoint accuracy; feedback-coupled PBH adapter and K_PBH remain unresolved.
REQUIRE BEFORE PHYSICAL REOPEN: PBH hadron spectra and threshold-resolved source; coupled depletion/state dependence; network sensitivity/target-error bound; multi-species bookkeeping and independent verification.
STATUS: NC_RETURN_RECEIVED_AND_ASSESSED / MECH_RESULT_INTEGRATED / BOUNDED_ADAPTER_REOPEN / NUMERIC_ENDPOINT_STOP / NO NOVELTY / NO EXEC_SIGN.
