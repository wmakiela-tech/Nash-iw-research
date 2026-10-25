# XH-S4 027 — designed falsifiers: identifiability vs model discrimination
RETURN_ID: XH-S4-20261025-EXPERIMENT-DESIGN-IDENTIFIABILITY-DISCRIMINATION-027
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03
DATE: 2026-10-25
SOURCE WINDOW: May 1–Oct 25, 2026; primary journal publication 2026 with explicitly earlier preprint date.
STATUS: SOURCE_TYPED / EXECUTED_EXACT_TOY / Q85-Q88 / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_NASH / NO_BW_INGESTION / NO_NEW_OWNER_TASK.

## SOURCE: publication in 2026 with earlier preprint
Yue Liu, Philip K. Maini, Ruth E. Baker, "Optimal experiment design for practical parameter identifiability and model discrimination", Mathematical Biosciences 399 (Sep 2026) 109710; online first **May 22 2026**, DOI https://doi.org/10.1016/j.mbs.2026.109710 ; publisher abstract https://www.sciencedirect.com/science/article/pii/S0025556426001008 ; Oxford author accepted manuscript https://ora.ox.ac.uk/objects/uuid:1be2267b-8857-4e2b-bf16-5305ec9737b2 . **Original arXiv preprint 2506.11311 posted June12 2025**, not a May 2026 first preprint. University accepted manuscript available but paper-level numerical figures not reconstructed; our controls are independently designed.
SOURCE target1: practical parameter identifiability of a single model assessed via profile likelihood confidence intervals (example logistic/Richards population dynamics). Target2: discriminate two models with known parameters, choose a time-varying control by optimal-control / Pontryagin Maximum Principle. Even source objective types differ: better parameter precision within M_A does NOT entail stronger evidence against M_B. No claim paper treated NASH memory/TT/PBH.

## XH exact counterexample A: two indistinguishable DC gains
For a stable scalar linear time-invariant response with frequency transfer
  H_A(iω)=1/(1+iω), H_B(iω)=2/(2+iω)
both have static gain 1, so ANY steady DC response with same driving amplitude fails to distinguish.
But the exactly calculable complex frequency response separation:
  |H_A−H_B|² = ω² / [(1+ω²)(4+ω²)].
Writing x=ω², derivative wrt x is (4−x²)/(x²+5x+4)², giving unique ω>0 maximum at ω=sqrt2; there squared gap=1/9, response-amplitude gap=1/3.
At ω=0 gap exactly 0. At ω=sqrt2, for ONE observation containing 2 independent real Gaussian quadratures with variance σ²=.05² each and known parameters, Gaussian KL D(P_A||P_B)=|ΔH|²/(2σ²)=22.2222 nats. This is an ASSUMED normalized sinusoidal experiment with phase-sensitive complex gain and independent quadrature Gaussian noise, not an empirical result. If only power/no phase is available, design and KL change. Input amplitude, bandwidth, runtime, perturbation cost and nuisance parameters require declaring.

## XH exact/NumPy test B: two parameters from one vs two time points
Single model y'=−λ y+a u(t), start y0=0, step u=1 for t≥0 gives y(t)=a(1−exp(−λt))/λ.
Let a=2,λ=1. Derivatives g_a=(1−e^{-λt})/λ;
 g_λ=a*(λt e^{-λt}−(1−e^{-λt}))/λ².
Assume independent Gaussian sample noise σ=.1; Fisher I=Σ_t g(t)g(t)^T/σ².
At one t=2, I rank1 exactly, det0; finite NumPy det 2.9e−12 roundoff (NOT evidence finite rank). At t=.5 and 2, I full rank, determinant 969.9769068113648 in declared units; adding t4 yields det 5499.998835693121. This proves for THIS simple host timing can eliminate a local nonidentifiability, not universal source mechanism recovery. Fisher local full rank does NOT prove global uniqueness, profile-likelihood bounded confidence, or distinguish rival models.

## Typed links and scientific questions
027 -> 026: Last rotation showed almost identical input/output histories for materially distinct kernels. Experiment design now explicitly manipulates input frequency/temporal sampling and can test *source mechanism*, rather than merely optimize predictions from frozen data. Requires allowable perturbations and matched measurement noise.
027 -> PRF11 relative sufficiency: the object must be fixed (parametric θ of one model, comparison of model families, distributional prediction or source kernel uniqueness up to equivalence). Do not call parameter Fisher determinant an identifiability certificate for an arbitrary latent NASH operator.
027 -> DTC0a: changing source test field class and Fourier modes can expose a TT projection obstruction; but if the experiment target is K_A masked RMS it is NOT by itself a physical discrimination readout.

Q85/P0: Are we maximizing parameter information conditional on M_A or divergence between candidate models? State target before design.
Q86/P0: Which excitation frequencies and phase-resolved observables separate candidates identical under baseline test? H0 both DC equivalent vs H1 ω=sqrt2 unequal here; beat-note/phase control.
Q87/P1: Is local Fisher full rank enough? No; test global profile likelihood, competing parameter branches, poor SNR, and model mismatch.
Q88/P0: Is selected experimental input implementable, and are amplitude/time/bandwidth/nuisance restrictions honestly included? If not, optimization is only a mathematical upper scenario.

## Executed and reproducible
Original independent Python in shared verified ZIP: IW_XH_S4_027_029_REPRODUCIBILITY.zip, the script verify_027_029.py, output verify_027_029_results.json, README and SHA256 manifest. ZIP SHA256 b45baf567c902be1a49334aefb0566cd19a29a0c29e2b0523669e05c385541d1. Script SHA256 65708ff32a6f38888932c54883e3d4941efb4cee26230e854cdf178c6906aab5; JSON SHA256 4c2094b4627bcd34d63d6c24c2439090debce9721fbd844ec9b6afafd55346bf. Verified unzip integrity, fresh isolated Python execution and exact SHA recheck. Paper's experiments NOT replicated; no NASH numerical/physical claim; no BW auto-ingestion.
