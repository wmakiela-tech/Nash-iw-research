---
artifact_id: IW_DAX_S9_ROT015_EXACT_BORN_HELICITY_ADDBACK_AND_SOURCE_CENTRAL_ANGULAR_PHASE_ENVELOPE_GATE_001_20261122
date: 2026-11-22
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_08 / DAX-S9
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: EXACT_SCALAR_QED_BORN_SOURCE_REEXEC / COHERENT_FSI_F2_SOURCE_MODEL / BELLE_12_CELL_PHASE_SHAPE_GUARD
claim_ceiling: NO_FULL_HADRONIC_FIT / NO_HEPDATA_PRIMARY_BYTES / NO_EXPERIMENTAL_CI / NO_NEUTRINOS_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX9 ROT015 — exact Born angular higher waves restore scope of prior two-wave no-go

22 November 2026. This is a bounded source audit and conditional model falsifier, NOT a first discovery of physics or experimental tension. ROT014 prior report GitHub pinned readback PASS; original Slack dispatch completed.

## ORIGINAL SOURCE / PRECEDENCE

Original physics actually re-read from author publisher full HTML: S.P. Klevansky, R.H. Lemmer, A. Beygi, EPJA 61:49 (2025), DOI https://doi.org/10.1140/epja/s10050-025-01524-6 , Eqs (5),(6) exact scalar-QED helicity Born, (9),(13) projected J00 and J22 Born, (21) exact Born differential rate, (65) original photon FSI, (66)–(70) tensor resonance, (74)–(75) unpolarized rate. Experiment original: T. Mori et al, JPSJ 76 (2007) 074102, DOI https://doi.org/10.1143/JPSJ.76.074102 ; 140 author Appendix B W central values independently crosschecked against official packed SECONDARY Rivet reference 140/140 PASS. Both original official-secondary compressed references read with pinned SHA256: Belle 28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403, MarkII ff9a573f34b469ef76b145913506dfa20774243332772c1f7ba2c31b8422986d. NOT original primary HEPData exports. Mature Dai/Pennington PRD90 036004 (2014) already noted anomalous angular Belle rise and hypothesized, not proved, muon-pair background difficulties.

## NEW ORIGINAL EXACT BORN ADD-BACK

At W, beta squared=1−4m_pi²/W², z=abs cos theta, source Born photon helicity amplitudes B0(z)=−2i e²(1−beta²)/(1−beta² z²) and B2(z)=2i e² beta²(1−z²)/(1−beta² z²) times azimuthal phase exp(2i varphi). Construct A0(z)=B0(z)−i e²(F_s−B_s); A2(z)=B2(z)+exp(i phi)R_22 Y_22, with original source ROT012 coherent F_s and the exact J00 Born B_s subtracted, avoiding double counting. Original ROT014 f2 conditional fixed, q5 and Blatt line shapes and source-normalized inputs retained without change. Different photon helicities add INCOHERENTLY; Born-FSI and Born-f2 within each helicity add coherently. d sigma/dabs z = beta/(32pi W²)(abs(A0)²+abs(A2)²). Not a complete source physical prediction: strong rescattering at higher J missing, gamma-gamma f2 relative complex phase unfitted, PDG charged isospin model and gamma width are conditional.

Executed exact-Born no-hadron no-resonance fallback reproduces published Eq21 at seven W times three angular regions, maximum relative error 1.33226762955e-15. Restricted-J Born fallback reproduces ROT014 source two-wave cross section <8e-13 relative at six W times three widths times two phases. Independent scipy adaptive versus Gauss32/80 source direct amplitude integration max relative 2.22e-16. Original restricted two-wave 1/3 high-angle ceiling also verified as regression in 40 cases.

## PRECISE LOGICAL CORRECTION TO ROT014

Pure J00+J22 has d sigma/dz=A+B(1−z²)², A,B >=0; hence P(0.4<=z<=0.6 |0<=z<=0.6) <=1/3 for ANY two-wave phase. AFTER restoring exact Born higher waves, this universal bound DOES NOT HOLD. At W0.90GeV, exact Born alone has high share 32.3047%; full Born+FSI+original fixed-f2 phi=0 has 29.5582%, but phi=pi gives 38.2799% >1/3. Do not transfer two-wave algebraic no-go to a general physical photoamplitude.

## EXACT SOURCE-MODEL ARBITRARY SINGLE-PHASE RATIO BOUND

For a fixed W or positive R68 thermal band, the model rates are H(phi)=a_h+Re(exp(i phi)d_h), T(phi)=a_t+Re(exp(i phi)d_t), positive denominator T. The MAX ratio r=H/T over any one d-wave phase is the unique root of (a_h−r a_t)+abs(d_h−r d_t)=0. Minimum has a minus modulus. Independently substitute maximizing phase back in direct amplitudes: PASS.

Belle real packed SECONDARY source central W0.85−0.95GeV high-z [.4,.6] share=0.39519081247603166, MarkII broad band original=0.29239766081871343. All units and native angular bin boundaries preserved (Belle 12 densities times .05; MarkII six partial-bin nb without .1). R68 benchmark E_gamma=1436554MeV; Planck T=.07818527068831995MeV, unchanged.

| Original source-typed f2 width | high share phi 0 | high share phi pi | MAX any common phi | Belle excess above max in percentage points |
| --- | ---: | ---: | ---: | ---: |
| Fixed Gamma | .2953854530 | .3811956976 | .3925684974 | .262232 |
| Running q5 | .3088277444 | .3423752621 | .3425016128 | 5.268920 |
| q5 plus Blatt-Weisskopf | .3035049319 | .3551535438 | .3558409490 | 3.934986 |

At the same sourced/frozen model parameters, all three enlarged models still fail the original Belle CENTRAL high-angle mass even with ANY single phase; this is a model-parameter specific conditional statement, NOT a universal theorem or statistical experiment rejection. The fixed-width deficit .262pp is small and not robust to unfitted parameters. Independently, each native 5MeV Belle W bin was compared to its OWN arbitrary phase maximum (even more permissive): 10/20 exceed fixed-Gamma, 20/20 exceed q5, 19/20 exceed q5+Blatt. The ROT014 20/20 was valid for restricted TWO-WAVE geometry only; explicitly preserve this updated count.

## ALL TWELVE ANGULAR BINS / NO COVARIANCE

Using all twelve actual native 0.05 Belle bins for W0.85−0.95GeV, positive R68 weighting, and ONE common unknown d-wave phase in all bins, numerically minimize TV12=.5 sum_j abs(p_obs,j−p_model,j(phi)); 361-point circular scan + refinements of all detected local minima. TVmin fixed=.057692562213 (phase2.428996rad), q5=.061796560600 (phase3.056469rad), q5+Blatt=.058856965777 (phase3.009019rad). Numerical minima, not formally sharp global TV certificates; 12 angular model bins still do not reproduce all Belle source central values at these source-frozen parameters. TV is NOT chi-square, significance, a detector covariance test or evidence of lepton contamination.

## CUSTODY / SCIENCE CEILING

Full local report and executing reproducibility bundle in originating user conversation: DAX9_ROT015_Exact_Born_Higher_Waves_Phase_Envelope_Source_Repro.zip; actual ZIP SHA256 e5d43f9479291f03b7d8c7ecdb222f0c2a405a716613d4a258ade658aa33c1d7, 13/13 source+code+data member SHA256 PASS, ZIP CRC PASS, independently executed clean-directory replay twice of JSON+2 CSV, 2×3/3 byte-identical PASS. The GitHub object is REPORT ONLY, not code or data upload. Strict HOLD: original experimental covariance and background subtraction; higher-J *hadronic* amplitudes; f2 fitted charged phase/physical dispersive widths; original primary HEPData exports; split KK charged/neutral thresholds; full collider/fiducial support, pion stopping and daughter neutrino moments. Cannot claim PBH/BBN or novelty from source shape. No BW write, no external I3, NO_CANON/NO_EXEC_SIGN.

RETURN: EXACT_BORN_EQ21_SOURCE_REEXEC_PASS / ROT014_TWO_WAVE_GUARD_PASS / 1OVER3_SCOPE_TRANSFER_FALSIFIED / SOURCE_FIXED_MODEL_ARBITRARY_PHASE_CENTRAL_NO_GO / 12BIN_TV_NUMERIC_RESIDUAL / NO_STAT_CI / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.