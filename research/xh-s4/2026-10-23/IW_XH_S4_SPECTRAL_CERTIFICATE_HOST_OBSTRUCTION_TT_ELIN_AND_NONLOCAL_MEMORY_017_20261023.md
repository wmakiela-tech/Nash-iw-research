# XH-S4 — Rotation 017: spectral certificate host obstruction, TT spatial tails, E_lin finite symbol, memory/nonlocality
RETURN_ID: XH-S4-MAYOCT2026-TT-LOCALITY-ELIN-COLBROOK-WITTIG-ZW-017_20261023
DATE: 2026-10-23
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
RESULT_CLASS: PRIMARY_SCIENCE_FOUNDATION / EXECUTED_FINITE_DTC0A_OPERATOR_HOST_TEST / RESEARCH_QUESTIONS Q29–Q31
EVIDENCE: original Cambridge 2026 monograph CHAPTER SUMMARIES (not full book); Wittig 2026 arXiv full text/source version; Zeng/Dong 2026 PRB primary ABSTRACT; independently implemented numerical calculations using supplied DTC0a verification script's TT and E_lin definitions, double checked by independent direct Fourier loops.
CLAIM_CEILING: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_INTERPRETATION / NO_KJ3_INVARIANT / NO_DTC_CONTINUUM_PROOF / NO_PBH_BOUND / NO_BW_INGESTION_ASSUMPTION / NO_NEW_OWNER_TASKS.
This is a science-first direct applicability countertest, not a new assertion that the full DTC0a runtime source 2a35d357... was byte-audited.

## 1. New major theoretical foundation — Colbrook 2026 monograph (not a newly discovered theorem)
Matthew J. Colbrook, *Infinite-Dimensional Spectral Computations: Foundations, Algorithms, and Modern Applications*, Cambridge UP, ONLINE PUBLISHED Aug 1 2026; print Aug20, 712 pp, DOI https://doi.org/10.1017/9781009382502 .
Source publisher:
https://www.cambridge.org/core/books/infinitedimensional-spectral-computations/25F488D387A2653D9D133DC14A274506
Chapter3 (Computing Spectra with Error Control) https://www.cambridge.org/core/books/abs/infinitedimensional-spectral-computations/computing-spectra-with-error-control/A6C4A25C433BDE26E9A79E0FF7E83642 ; publisher claims PseudoSpec/CompSpec resolvent/lower singular certification, absence-of-general-one-limit, conditioning functions.
Chapter8 (Essential Spectra) https://www.cambridge.org/core/books/abs/infinitedimensional-spectral-computations/essential-spectra/164D3BE5515482C7EC4F71F3F2D747C6 ; pollution + essential numerical range, certified absence potentially harder than spectrum computation.
Chapter10 (Nonlinear Spectral Problems) https://www.cambridge.org/core/books/abs/infinitedimensional-spectral-computations/nonlinear-spectral-problems/13ABC18B579E55E98EFDB6A35FEC160A ; holomorphic operator pencils, gap topology, Keldysh/resolvents, spectral pollution, contour quadrature. SOURCE SCOPE: publisher chapter abstracts only; do not claim full proof hypotheses were read or this theory directly applies to NASH.
Links to Q11 Colbrook/Mezic/Stepanenko 2026 Nature Communications 10.1038/s41467-026-74220-8 with ordered Koopman multi-limit SCI, to Q24 Wittig and Oct FEEC 2610.01501; mathematical object types differ.
**Q29**: What maximum certificate type is attainable from current DTC0a data: (a) test-field RMS, (b) full operator norm bound, (c) pseudospectral error enclosure, (d) continuum spectral theorem? Declare Hilbert spaces, domain, projection, regularization, actual target/cross-level maps. Existing finite N residual tables only (a); no free implication (a)->(d).

## 2. Wittig 2026 source-narrow theorem vs NASH implementation host
Mattes Wittig, arXiv:2608.03526 v1 Aug4, v2 Aug26, https://arxiv.org/html/2608.03526 .
Bounded finite-range operators on ℓ2(Gamma) of a uniformly discrete subset of a doubling metric-measure host. Rectangular spatial windows enlarged on output by interaction range m; lower norms of BOTH H-z and H*-conj(z) for nonnormal spectral target; authors prove pseudospectral enclosure
  gamma_(L,eps)(H) subset sigma_eps(H) subset gamma_(L,eps+C0/L)(H).
This relies on declared finite interaction radius and uniform degree plus full spatial coverage, not just local mask RMS or arbitrary FFT projection. Current DTC0a has local E_lin and periodic central stencils, BUT globally Fourier-defined P_TT. The full projected transport composition therefore does NOT automatically meet Wittig's fixed-small spatial range hypothesis.

## 3. EXECUTED project-host test: periodic Fourier TT projection of unit tensor impulse
Provenance sources provided by Moderator:
- /mnt/data/deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 (verification script)
- /mnt/data/dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv SHA256 1ed5dec5797ed1bc0ae9c4a924e1f18ef0a118f5602be99f03c953fd532cd66e
- /mnt/data/dtc0a_field_class_control_custom_gaussian_N31_v0_3_1.csv SHA256 3c8ce933c18a77e9d23699ae75c7f87bb3fbdd7e46bc988283e1377e820e2a3a
- manifest claims original runtime source hash 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084, but THIS ORIGINAL SOURCE WAS NOT BYTE-READ in this specific turn. Verification script matches formula used, not proof of original SHA.
Finite periodic N³ torus, symmetric tensor space with unweighted nodewise Frobenius ℓ2. Impulse h(x)=delta_(x,0) e1 tensor e1, unit norm exactly. On Fourier mode k!=0, P_ij(k)=delta_ij-k_i k_j/|k|²; projected impulse matrix ˆhTT_ij=P_i1 P_1j -0.5 P_ij P_11. At k=0 the supplied runner uses traceless projection h -> h-tr(h)/3*I.
Inverse FFT recovers real convolution kernel. Independent direct triple nested frequency-loop exactly matches vectorized implementation on N=7 and 9, max abs errors 2.08e-17 and 2.78e-17 in stand-alone GitHub reproducer; finite-grid only.
Let r(x)=max_j min(x_j,N-x_j), a periodic Chebyshev radius from source; E_tail(N,m)=sum_(r(x)>m) ||(P_TT h_imp)(x)||_F².
For ANY B_m whose action on a delta impulse is supported in the spatial radius m, support orthogonality gives
 ||P_TT-B_m||_op >= || (I-chi_(r<=m)) P_TT h_imp ||_2 = sqrt(E_tail(N,m)).
This is a mathematically immediate VALID LOWER BOUND, not an upper certificate, not a continuum theorem. No claim operator B_m is translation-invariant needed for the bound at this one impulse.

VERIFIED NUMBERS (double precision)
N17 ||PTT h||=0.506787... ; fraction outside r3=0.04018196, lower op >=0.101588.
N31 ||PTT h||=0.506740...; outside r3=0.04438020, lower >=0.106753, r6 >=0.073553, r8>=0.059960.
N41 ||PTT h||=0.506739...; outside r3=0.04513326, lower >=0.107655; r6 >=0.076166; r8>=0.064302.
N41 r0 outside energy 61.48228%, r1 10.90494%, r2 6.84643%, r3 4.513326%; noncompact impulse response in finite periodic torus.
Interpretation: no B_3 with exactly 3-cell output radius can approximate this P_TT in standard op norm better than 0.10765 at N=41. A claim of upper error < 0.001 would be directly contradicted in that fixed host.
STOP: for each finite N the torus is finite, hence P_TT trivially has some finite interaction radius up to N/2; we have NOT proved an N-uniform tail lower bound as N->infty or impossibility of global/local decomposition with growing m. Single input lower bounds CANNOT be substituted for a global op norm UPPER BOUND. Do not compare magnitudes to the DIFFERENT DTC0a K_A masked RMS 4e-5 as if same norm and object.

## 4. EXECUTED project-host test: Fourier spectrum of E_lin, alpha positivity boundary
Supplied DTC0a verification script uses E_lin h = h + alpha dx² Δ_2nd h, with periodic centered stencil, componentwise tensor. Fourier symbol:
  e_alpha(k)=1-4alpha sum_(j=1)^3 sin²(k_j dx/2).
Consequently for alpha>=0, e in [1-12alpha,1]; if 0<=alpha<1/12, E_lin strictly positive on ALL periodic grids; alpha=1/12 nonnegative, strict may hold at fixed odd N; alpha=0.2 is above the positivity regime and can have signed spectrum. E_lin is SELF-ADJOINT but not generally positive for alpha=.2. Absolutely NOT proof of negative physical norm or ghost: it is a computational Fourier stencil symbol only.
Exact FFT grid spectra:
N31 alpha=.05: lambda_min=.4015392029824315, lambda_max=1, neg fraction=0, min abs=.401539...
N41 alpha=.05: lambda_min=.40088025964487795, neg fraction=0.
N31 alpha=.2: lambda_min=-1.393843188070274, neg fraction=.6424759155449632, minabs=.0005220258069762451, conditional spectral cond(maxabs/minabs)=2670.??.
N41 alpha=.2: lambda_min=-1.3964789614204882, neg fraction=.6418363053350938, minabs=.0007376262376461717, conditional spectral cond=1893.2067355369188.
No E inverse is used in tested K_A formulas: high condition number of an INVERSE not present is NOT diagnosis of current solver instability.
**Q30:** Are alpha=.2 residual trends sensitive to near-zero sign-changing Fourier modes of E_lin? Are the tested smooth Fourier state families supported in them at all? Hypotheses H_lowband (smooth fields stay positive E band), H_highband (high-frequency excitation uncovers sign/near-null), H_project (TT changes observed reaction). Cheapest discriminator: fixed N31/41, one Fourier input mode each from positive, near-zero and negative multiplier classes, same h input norm, report E output and projected K separately; never infer physical ghosts.
Observed archived DTC data for alpha .05: K_A N31=3.76475685320836e-5, N41=3.837256...e-5 (+1.926%), while K_C -40.51%, K_B -43.02%; these are SELECTED FIELDS and masked RMS. At N31 alpha .05 custom Gaussian K_A can be 3%–10% of trig reference, direct project file demonstrates field dependence. This does not establish general operator norm plateau, nor prove any K/J3 invariant.

## 5. NEW June 8 2026 physics prior-art: spatial nonlocality versus temporal memory are different axes
Yi Zeng, Jianjun Dong, "Unified statistical theory of heat conduction in nonuniform media", Physical Review B 113, 235204, published JUNE 8 2026, https://doi.org/10.1103/hx28-4ksc .
SOURCE ACCESS: APS PRIMARY ABSTRACT + metadata, article full formulas/derivations not audited; no paper-level validation. Zwanzig projection yields causal two-point spatiotemporal thermal kernel, Green-Kubo relation; in silicon transient grating within relaxation-time model, spatial nonlocality primarily controls departure from Fourier response and short-time memory separately matters. It is heat conduction in phonon systems, NOT NASH nonlocal gravity or particle field.
**Q31:** Given a future NASH nonlocal transport or observational-memory model, can different spatial wavelengths and temporal driving frequencies distinguish nonlocal SPATIAL coupling from TEMPORAL history memory, or are they confounded by a single probe?
Exact XH illustrating first-order model, not author derivation:
 K_space(k,omega)=kappa0/(1+(ell*k)^2), independent omega;
 K_memory(k,omega)=kappa0/(1-i*omega*tau), independent k.
At (k,omega)=(0,0) both =kappa0, so ordinary static homogeneous response cannot distinguish; at k ell=1, omega=0 first halves and second stays 1; at k=0, omega tau=1 first stays 1 and second has complex (1+i)/2. Crossed spatial and temporal probes discriminate if readout measures phase, given linearized causal host. These are generic illustrative kernels, NOT project physical predictions or NCDG E(Box).
Typed edge to Jiang 2610.22286 hidden causal fingerprints and PRF11 history relative sufficiency: same *research-question type*, distinct physical/mathematical hosts. Zeng/Dong model derives microscopic Zwanzig kernel while DTC source is numerical TT/transport residual: NO theorem transfer.

## 6. Cross-paper research graph, prioritized questions and stop gates
Colbrook monograph 2026 (SCI/resolvent/smallest singular certificates) --FOUNDATION/PRIOR_ART--> Wittig v2 August (finite-range lower-norm two-sided brackets) --FAILED_DIRECT_HOST for fixed-small-range--> supplied DTC0a Fourier P_TT. DTC E_lin local signed multiplier further separates finite local stencil from global projection. FEEC Oct 2610.01501 only applies if shared Hilbert op-norm approximation; neither automatically available in DTC0a.
Zeng/Dong June PRB --CROSS-AXIS DISCRIMINATOR FOR MEMORY/SPACE--> Jiang October fingerprint model-conditioned smoothing; NOT same dynamical host. New questions Q29 (what certificate level), Q30 (mode/alpha/restriction), Q31 (space vs time identifiability). No conceptual conflation of residual, pseudospectrum, spatial kernel, physical wave/pole, or measurement.
P0 SOURCE/HOST gate: direct Wittig on full P_TT rejected pending useful tail-upper proof and fixed-range legal surrogate.
P0 MATHEMATICS: require spectral certificate type and full norm vs selected samples.
P1 NUMERICAL SCIENCE: mode-conditioned α probe for E_lin.
P1 PHYSICS/METHOD: space-vs-time pulse protocol is only illustrative, needs measured carrier and state for NASH.
No change to actual NASH research canon. Scientific results persisted in source-native GitHub report and independent reproducer script only.
