---
artifact_id: IW_DAX_S8_ROT008_SCALAR_DPP_COLLIDER_CUT_EVENT_WEIGHTED_BOUND_001_20261110
created_at: 2026-11-10
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: ANALYTIC_SOURCE_TYPED_COLLISION_WEIGHTED_SUPPORT_BOUND / INDEPENDENT_QUADRATURE / NEGATIVE_KNOWLEDGE
claim_ceiling: NO_NATIVE_MADGRAPH_RUN / NO_FULL_QED_DIFFERENTIAL / NO_PHYSICAL_QED_EVENT_FRACTION / NO_DEPOSITION / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT008 — Exact analytic bounds for collision-weighted high-COM fraction in the CRPropa scalar DPP model

Date: 10 November 2026. This is a source-typed mathematical result, NOT the physical QED fully differential gamma gamma -> e+e-e+e- process and NOT a physical PBH/BBN constraint.

## Precedence and reason for this rotation
DAX-S7 R68 first identified total DPP rates versus full differential QED and subsequent cascade targets. ROT001 (on-shell insufficiency), ROT002 (first/eventual events), ROT003 (CRPropa two-hard-lepton surrogate), ROT004 (thinning variance), ROT005 (conditional hot-table input support), ROT006 (original amplitude literature), ROT007 (Sotsky collider-cut versus R68 support) remain separate first-owner results. ROT007 calculated a Planck photon NUMBER tail and explicitly warned this is not a rate-weighted event fraction. ROT008 closes exactly that gap for ONE fully declared scalar-cross-section source model. It does not close full-QED transfer.

Bounded GitHub/Slack search on 10 Nov did not locate XH-S5 source-owner acceptance or a runnable full massive uncut QED generator for the DAX request. NO_MATCH does not establish absence; ROT006 task proposal is not duplicated. Focus remains source-type explicit; no automatic science cascade.

## Checked original source and input
Original CRPropa3-data scalar generator: https://github.com/CRPropa/CRPropa3-data/blob/master/calc_electromagnetic.py , pinned Git blob 030af585f62357e4522f64f7a7daa81c635b20d3, source expression sigma(s) = sigma_inf (1-16me^2/s)^6 for s>=16me^2, zero below. It is an INTEGRATED source approximation, not a differential 4e matrix element.

Sotsky 2006 original arXiv https://arxiv.org/abs/hep-ph/0604020 was checked in ROT007 with 1 GeV per outgoing final lepton and angular collider cuts. Four final leptons with COM energies >=1 GeV require sqrt(s)>=4 GeV; satisfying this necessary condition does not ensure acceptance under the other cuts. Source model is isotropic ideal Planck bath, real incoming photons and instantaneous gamma-gamma encounter at the inherited R68 E_gamma=1436.554 GeV, T_gamma=0.07818527068831995 MeV, me=0.51099895 MeV.

## Definitions
Let x=epsilon/T, u=(1-cos theta)/2 in [0,1] and relative flux weight 2u; s=4 E_gamma T x u. Define s0=16me^2, Scut=(4GeV)^2, chi=s0/(4ET)=9.29936099340773333878e-6, a=Scut/(4ET)=35.6133716172868214623, rho=s0/Scut=2.611199269011025e-7.

The dimensionless total scalar collision hazard relative to constant sigma_inf is

D = (1/(2*zeta(3))) integral_0^infinity [x^2/(exp(x)-1)] dx
                           integral_0^1 2u * sigma(4ETxu)/sigma_inf du.

N is the same positive integral restricted to s>=Scut. The desired SOURCE-MODEL high-COM interaction fraction is P=N/D, not a fraction of physical QED DPP events.

In the constant-sigma limit the angular integral over u>=a/x is 1-(a/x)^2 for x>=a. Define

B(a)=(1/(2*zeta(3))) integral_a^infinity (x^2-a^2)/(exp(x)-1) dx
    = (1/zeta(3)) sum_(n>=1) exp(-na)*(a/n^2 + 1/n^3).

By source monotonicity for s>=Scut,
(1-rho)^6 * B <= N <= B.

For any z>0, the source factor max(0,(1-z)^6) above threshold and zero below obeys source_factor >= 1-6z. Integrating the right-hand side over ALL Planck photon x and isotropic u with positive 2u flux yields

D >= 1-6chi*zeta(2)/zeta(3)=1-chi*pi^2/zeta(3) >0,
and trivially D<=1.

THEREFORE the exact analytic source-model bound is

(1-rho)^6 B <= P <= B/(1-chi*pi^2/zeta(3)).

This is a rigorous inequality for the DECLARED scalar model, not a rigorous bound for the full physical 2->4 QED rate.

## Numerical results
B=1.03997744732956912208796708509565336e-14.
Rigorous analytic bracket with high-precision evaluations of constants:
P in [1.0399758179776226101e-14, 1.0400568591054100338e-14].
Earlier photon NUMBER fraction for x>=a: 1.905274252983205879e-13.
B/number_fraction = 0.0545841337907764215: the angle/relative-flux eligibility suppresses the constant-sigma value by a factor about 18.32 compared with simple photon counting.

Independent source-model numerical integral at 55-digit mpmath:
D=0.99992371424013570555355875860733789,
N=1.0399758624791494047640706647073958e-14,
P=N/D=1.0400552038806782559869698102634501e-14.
This falls strictly inside the analytic interval.

The source is an exact POSITIVE series; after truncation at n=12 a conservative bound on its omitted remainder is 2.610565637253948e-200. Arithmetic numerical evaluations are reproducible; they are not themselves a proof of physical model applicability.

## Falsification and positive boundary
FALSE: ROT007 Planck photon number tail is itself the DPP event fraction.
TRUE UNDER X: for ideal isotropic Planck bath, scalar CRPropa sigma(s), fixed R68 inputs and full collision flux, the event fraction with COM>=4GeV obeys the analytic bracket above. This provides only a necessary upper-support control on the paper-cut accepted source-model fraction.
OPEN: physically exact total sigma(s), massive 4-lepton QED differential operator, cuts in actual source frame, lepton energy-sharing, transport and EM/neutrino deposition, PBH/BBN consequences. No source-native MG5 or native CRPropa run performed; no asserted physical BBN limit.

## Reproduction and custody
Primary full local bundle includes stdlib Decimal/Chudnovsky/Apéry analytical proof code, independent mpmath 55-digit quadrature, JSON output, execution environment, exact source audit, hashes and clean-room ZIP validation. The math itself is fully stated here, so this is not a pointer-only science body. No independent BW event, owner receipt or qualification verified: GITHUB_PENDING_BW_INGEST.

ROT008_SCALAR_SOURCE_ANALYTIC_BOUND_PASS / UNCUT_FULL_QED_OPEN / NO_NEW_OWNER_QUEUE / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
