---
artifact_id: IW_DAX_S9_ROT010_KLEVANSKY_2025_COUPLED_PION_KAON_ONSHELL_UNITARITY_SOURCE_GATE_001_20261121
date: 2026-11-21
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: ORIGINAL_PUBLISHED_HADRONIC_SCATTERING_MODEL_REEXECUTION / COUPLED_CHANNEL_UNITARITY_SOURCE_GATE
claim_ceiling: NOT_DAI_PENNINGTON_SOLUTION_I / NO_PHOTOPRODUCTION_AMPLITUDE / NO_EXPERIMENTAL_PHASE_SHIFT_VALIDATION / NO_NEUTRINO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT010 — source-typed published chiral pi-pi / K-K coupled scattering unitarity

**21 Nov 2026.** After ROT009's original Dai–Pennington 2014 mature prior-art check, the successor shifts from repeated hypothetical cross-experiment scale changes to an actually published **strong-interaction scattering operator**. Dai–Pennington fitted photoproduction amplitude coefficients and underlying hadronic T matrices were NOT recovered. This is an independent reproduction of a **different** original 2025 chiral model, NOT Dai–Pennington Solution I and NOT a full gamma gamma -> pion production rate.

**Original source directly read:** S.P. Klevansky, R.H. Lemmer, A. Beygi, *EPJA* 61:49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 , original publisher open-access HTML, equations 29,31,32–37,55–56,59–65,72–75. This source explicitly separates scalar-QED Born, strong meson rescattering and f2 resonance production components. Original model uses f_pi=93 MeV, m_pi=140 MeV, m_K=496 MeV, cutoff Lambda=1351 MeV. No original author code or native numerical amplitudes were downloaded, so this is an original DAX implementation of source-published equations, NOT author code byte-equality.

**Executed source operator:** real on-shell I=0 potentials in ordered (KbarK, pi-pi) basis, V11=3s/(4f²), V12=s sqrt(3/2)/(2f²), V22=(2s-m_pi²)/f²; I=2 elastic V=-(s-2m_pi²)/f². Published equal-mass loop Pi_m=epsilon/(4pi)²*(1+log(1+Lambda²/m²)+m²/(m²+Lambda²)-2J_m), with epsilon_pi=.5, epsilon_K=1. Below threshold J_m=alpha*atan(1/alpha), alpha=sqrt(4m²/s-1); above threshold J_m=beta*(atanh(beta)-i*pi/2), beta=sqrt(1-4m²/s). T0=(I-V diag(Pi_K,Pi_pi))^-1 V; T2=V2/(1-V2 Pi_pi). For open channels rho_i=epsilon_i beta_i/(16pi), S=I+2i sqrt(rho) T sqrt(rho). Below KK threshold, the virtual kaon loop stays in T but is not an open S channel. From the published loop, Im(Pi)=rho and hence Im(T^-1)=-rho; complete S†S=I follows mathematically, subject to numeric errors.

**Actual independently executed verification:** NumPy 2.3.5 double precision 2x2 linear solve vs separately coded scalar-cofactor expression on 401 W samples [.30,1.45]GeV, and independent mpmath 1.3.0 70-digit matrix implementation on 18 points. Max open-channel S†S-I element < **2.443e-15** in NumPy, < **5.44e-71** in high precision; independent cofactor T22 absolute discrepancy <7.12e-14; independent high-precision complex T relative difference <1.86e-15. Original runtime ZIP CRC PASS, 7/7 member SHA-256 PASS, fresh clean replay frozen JSON+CSV BYTE-IDENTICAL PASS. Repro ZIP SHA256 **6f5bacaa72215e1f6cdab907967237edb63a3950b96c8cf003cd2bb1df9b3ab4**. ZIP with full 14k scientific report, original Python, frozen JSON+CSV, source receipt and manifest is attached in originating conversation; it is NOT represented as GitHub code upload.

| W GeV | abs(S_pi pi -> pi pi, I=0) | abs(S_pi pi -> K K, I=0)^2 | abs(S_pi pi, I=2) |
| --- | ---: | ---: | ---: |
| .80 | 1.000000 | 0 (closed) | 1.000000 |
| .98 | 1.000000 | 0 (closed) | 1.000000 |
| 1.00 | .712554 | .492267 | 1.000000 |
| 1.05 | .694995 | .516982 | 1.000000 |
| 1.40 | .926559 | .141488 | 1.000000 |

At W=1GeV, abs(S_pi pi)^2+abs(S_pi pi -> KK)^2=1 numerically. Demanding abs(single elastic S_pi pi)=1 ABOVE KK threshold would be a false single-channel unitarity audit. Passing a unitarity identity internal to a model does NOT independently validate it against measured scattering phase shifts.

**Material source-anchored threshold limitation:** paper uses a SINGLE isospin-averaged kaon m_K=496MeV -> threshold W=992MeV. PDG 2025 strange-meson original table https://pdgweb.lbl.gov/2025/tables/rpp2025-tab-mesons-strange.pdf gives m(K charged)=493.677MeV (threshold 987.354MeV) and m(K neutral)=497.611MeV (threshold 995.222MeV); true charged/neutral thresholds differ by 7.868MeV. In a sensitivity-only substitution of ONE mass into the same 2-channel model at W=.990GeV, abs(S_pi pi)=.793532 for mK=.493677GeV vs 1.000000 for mK=.496 or .497611GeV. This substitution is NOT a proper coupled charged+neutral 3-channel, isospin-breaking physical calculation. Thus the simplified near-KK-threshold result cannot automatically be used as a precision physical pion source.

**STOP/next gate:** No Born+FSI coherent gamma gamma -> pi+ pi- amplitude, charge/isospin projection, photon helicity, gauge invariance, f2(1270), or fit to MarkII/Belle has been executed. To cross that gate, re-read original 2025 Table2 and Eqs.59–75, reproduce isolated scalar-QED Born previously checked in DAX8 ROT012/017, then add the sourced rescattering and resonance contributions with correct interference and units. Dai–Pennington original fitted amplitude is still ACCESS_HOLD. No full hadronic all-W production, no pion-plasma energy loss, daughter neutrinos, PBH/BBN, novel QCD or independent scientific referee claim. No BW write or owner override.

**RETURN: SOURCE_PUBLISHED_HADRONIC_T_REEXECUTION_PASS / ELASTIC_AND_COUPLED_S_UNITARITY_PASS / PHYSICAL_K_CHARGE_THRESHOLD_SPLIT_GUARD / PHOTOPRODUCTION_AND_DAI_FIT_HOLD / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.**
