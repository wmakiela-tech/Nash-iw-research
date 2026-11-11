---
artifact_id: IW_DAX_S8_ROT012_CHARGED_PION_BORN_CHANNEL_COMPLETENESS_GATE_001_20261111
created_at: 2026-11-11
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SOURCE_TYPED_CHARGED_PION_BORN_FOUR_CHANNEL_FIRST_EVENT_COUNTERMODEL / ANGULAR_PLANCK_REDUCTION
reproduction_status: AUTHOR_REPRODUCED_WITH_INDEPENDENT_NUMERICAL_FORM
claim_ceiling: NO_PHYSICAL_HADRONIC_RATE / NO_FULL_SM_COMPLETENESS / NO_QED_4E_DIFFERENTIAL / NO_NEUTRINO_YIELD / NO_DEPOSITION / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT012 — charged pion Born branch and three-channel R68 scope audit

Date 11 November 2026. DAX-S7 R68 originally analyzed FIRST photon interaction probability for ONLY gamma gamma -> e+e-, gamma gamma -> mu+mu-, and gamma gamma -> 2(e+e-). R68 explicitly did NOT claim Standard Model completeness, final neutrino/EM deposition or PBH bounds. All that precedence and negative knowledge remains valid. The earlier DAX-S8 ROT001-011 source and kinematic gates are unchanged.

This source-typed new branch tests adding a kinematically allowed fourth first-event competitor, gamma gamma -> pi+pi-, using **point-like scalar charged-pion Born** cross section. This is NOT the full experimentally constrained hadronic amplitude and does NOT provide a physical hadronic bound: coherent strong-interaction final-state amplitudes may enhance OR suppress the Born term.

## Source receipts and model definitions

- R68 original source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-11-02/IW_DAX_S7_ROTATION_68_SCIENTIFIC_LEDGER_20261102.md ; pinned read source Git blob 06a9be92c6772143fccab3e10930c2967274cbc8.
- Klevansky, Lemmer, Beygi, European Physical Journal A 61,49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 , **Eq. (22)** charged pion total Born cross-section. Paper independently treats strong final state interactions and resonance effects, its Fig.10 compares Born and full models. Full primary HTML equation read 2026-11-11.
- Particle Data Group 2025 charged pion mass m_pi=139.57039 MeV, https://pdg.lbl.gov/2025/listings/rpp2025-list-pi-plus-minus.pdf , page 1, text+visual screenshot checked.
- BW total spin-1/2 expression independently source-confirmed DOI https://doi.org/10.1140/epjp/s13360-022-02920-3 ; the DPP asymptotic shape from R68 is source-typed separately from full differential QED.

Fixed ideal Planck bath benchmark E=1436554 MeV, T=0.07818527068831995 MeV, alpha=1/137.035999084, me=0.51099895 MeV, mmu=105.6583755 MeV. Charged pion mass as above. Isotropic background and unpolarized total gamma gamma cross sections. No cosmological expansion, electromagnetic/hadronic transport, decay channels or other source processes.

For s>=4m² let b=sqrt(1-4m²/s). Total Breit-Wheeler fermion-pair cross section:
 sigma_BW(s;m)=(2 pi alpha²/s)*[(3-b⁴)*log((1+b)/(1-b)) - 2b(2-b²)],
zero below threshold.

For s>=4m_pi², the pion point-scalar Born source, Eq.(22) above:
 sigma_pi,Born(s)=(2 pi alpha² b/s)*[2-b² - ((1-b⁴)/(2b))*log((1+b)/(1-b))],
zero below threshold. This is not equivalent to the full strong interacting pion source.

For s>=16me² R68-style DPP source total sigma=alpha⁴(175 zeta(3)-38)/(36 pi me²), zero below. An optional sensitivity test uses the scalar CRPropa3-data threshold-softened factor (1-16me²/s)^6, not a QED 2->4 differential kernel.

## Exact isotropic angle reduction

Let x=epsilon/T and u=(1-cos theta)/2, with relative photon flux 2u. Each collision hazard is proportional to

 K_i = integral_0^infty dx x²/(exp(x)-1) integral_0^1 du 2u sigma_i(4ETxu).

Use y=xu, apply positive Fubini and evaluate integral_{x=y}^infty dx/(exp(x)-1) = -log(1-exp(-y)). Exactly:

 K_i = integral_{y_threshold}^infty dy 2y[-log(1-exp(-y))] sigma_i(4ETy), with y_threshold=s_threshold/(4ET).

No approximate angular averaging and no photon-count-only proxy. This angularly reduced total-rate identity is NOT a differential outgoing-event kernel.

## Frozen numerical results, 48-digit mpmath source model

All K are positive common unnormalized MeV^-2 kernels; their normalization cancels in first-event probability.

| Channel | K_i |
| --- | ---: |
| gamma gamma -> e+e- (BW) | 5.983877841687106e-8 |
| gamma gamma -> mu+mu- (BW) | 9.433089008347292e-9 |
| gamma gamma -> four electrons (DPP asymptotic step) | 3.978875327380886e-8 |
| DPP alternative threshold-soft source | 3.978571797579239e-8 |
| gamma gamma -> pi+pi- (charged-pion Born) | 9.097617621183627e-10 |

- **R68-replicated 3-source muon first-event** P3 = 0.08649399708057440685496638475, compared to R68's 0.0864887438349: absolute difference 5.25325e-6; this is close within original reported quadrature spread, NOT byte-exact reproduction or re-optimization.
- **Four-source conditional Born pion case** P4 = 0.08577845049943483461485531404.
- Difference P3-P4 = 0.00071554658113957224; relative drop (P3-P4)/P3 = 0.00827278892514352388 = 0.8272788925%.
- K_pi,Born / K_BW_mu = 0.09644367410434897644; K_pi,Born / (K_e+K_mu+K_DPP) = 0.0083417989.
- Alternative softened-DPP source control P3_soft = 0.0864964044 and P4_soft = 0.0857808181.
- Conditional charged-pion Born event-weighted median COM mass sqrt(s) = 644.33426993 MeV; fraction with sqrt(s)>1 GeV = 0.144026725367.

## Independent validation, including direct angular quadrature

Executable A: Python 3.13.5 + mpmath 1.3.0, 48-digit high precision integration of all five source rates and pion mass support (frozen results_mp.json).

Executable B: separate Python 3.13.5 + SciPy 1.17.0 code integrates original 2D x,u Planck+angle formula directly AND separately evaluates 1D formula. Relative disagreement: BW_mu 1.06144870e-10, charged-pion Born 3.76988543e-11; both PASS declared <2e-8 tolerance (frozen results_scipy.json). Clean extraction and two repeated scripts byte-identical locally. These are independent integration forms, not independent experiments or measured hadronic physics.

Local source bundle in originating ROT012 conversation: full Markdown, executable mpmath and SciPy programs, two frozen JSONs, README, source audit, manifest, verifier; ZIP CRC PASS, 7 SHA256 member checks PASS and clean standalone double replay PASS. The local bundle is not represented to have been uploaded to GitHub by this Markdown.

## False transfer and precise science boundary

FALSE: numeric first-event muon probability computed among only three candidate channels automatically remains the same when another physically allowed source-model channel is added.

TRUE UNDER X: for exactly the BW_e/BW_mu/DPP-asymptotic/charged-pion-Born four-channel IDEAL isotropic Planck model, adding pion Born decreases P_first,mu by 0.8273% relative. Under true hadronic QCD+EM dynamics this NUMBER need not be a lower bound, an upper bound, or a useful error estimate.

OPEN: full real-photon gamma gamma -> pi+pi- amplitude including interference/strong final-state effects and resonances in this COM domain, neutral-pion/multihadron channels, complete Standard Model interaction rates, hadron decay and scattering, eventual muons/neutrinos, QED 4e differential energy kernel, deposition and PBH/BBN. Existing XH-S5 massive 4e source request is ACKED and not duplicated. No new owner task. A distinct future hadron-source owner request requires explicit Moderator/MT15 decision if physically material; REOPEN on inclusive angular-source constrained full pion cross sections with uncertainties and a physically specified target observable.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE. BW source receipt and public GitHub write are not science acceptance; GITHUB_PENDING_BW_INGEST.
