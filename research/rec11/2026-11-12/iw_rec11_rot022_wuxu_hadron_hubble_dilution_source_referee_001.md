---
artifact_id: IW_REC11_ROT022_WUXU_HADRON_HUBBLE_DILUTION_SOURCE_REFEREE_001_20261112
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-12
exposure: PUBLIC
review_class: I1_NONBLIND_DIRECT_ORIGINAL_AUTHOR_SOURCE_REFEREE_AND_SHARP_FIXED_BACKGROUND_ORDER
source_firstness: IW_MECH_S9_ROT003_WUXU_TNU_AND_BARYON_COMOVING_NULL_SOURCE_FIRST_001_20261112
claim_ceiling: PHYSICAL_DENSITY_SEMANTICS_CONDITIONAL / NO_FULL_COUPLED_NATIVE_JULIA / NO_FIG5_PRODUCER / NO_E4_SPECTRA / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REC11 ROT022 — six Wu–Xu hadron-density ODEs omit FRW expansion dilution; sharp frozen-background comparison

## 1. Ownership and full source evidence

**Mech-S9 ROT003 FIRST** called attention to missing explicit `−3H n_h` in the original Wu–Xu hadron RHS. REC11 independently inspected **ALL SIX** source-channel equations in the immutable AUTHORS' repository and derives a new sharp conditional error envelope. We neither reassign owner firstness nor claim physical BBN consequence.

Original author `Fenyutanchan/Primordial-Black-Hole` Git commit `d395183674cace6c9906a8911bdeb7234ba4040d`, `arXiv-2509.05618/main-scan.jl`, original Git blob **b368ba55d5a493f7bc185909730f7fe5691f10d6** was directly fetched (not a downstream note). Key source lines:
- 39–44: source η=ln a, state has **log six number densities**;
- 53–58: six hadron n_j use energy-density dimension 3 (number per physical volume in natural units);
- 60: `n_PBH=n_PBH_ini (a_ini/a)^3` explicitly redshifts physical BH number density;
- 64–65: `n_B=η_B*2ζ(3) T_SM^3/π²`, another physical density proxy;
- 103–128: six injection terms `n_PBH*dN_j/dt` minus loss via decay/scattering, for π−, π+, K−, K0L, anti-proton and anti-neutron;
- 135–140: **six** `du[k]=d_n_j_dt/(H*n_j)`; no `−3` in η equations, equivalently **no `−3H n_j` in time-density equations**.

The original paper's v3 §4.1 Eq. 4.6 says the production-vs-decay/scattering steady relation holds when relevant reaction and injection rates dominate H, whereas when H competes the actual number densities require numerical Boltzmann equations (https://arxiv.org/html/2509.05618v3). Standard physical FRW transport contains `dn/dt+3Hn=collisions/sources` (https://www.astro.uzh.ch/~jyoo/class/2024/07.early.universe.pdf Eq.1.49; https://www.damtp.cam.ac.uk/user/tong/cosmo/cosmohtml/S3.html). Paper v3 vs code v2 historical JCAP build identity remains **UNKNOWN**. A deliberate approximation to short-lived meson channels is plausible if `λ≫H` but would need a source-typed error budget; the same cannot automatically be presumed for stable antinucleons.

## 2. Exact source-typed discrepancy

Under the source's physical-density reading, for each of the six channels write `J(t)=n_PBH(t)*dN_j/dt>=0` and `λ_j(t)>=0` combining its decay/scattering terms. Holding background and neutron conversion state frozen, the source equations read

`dn_code/dt = J(t)−λ(t)n_code`.

Standard FRW density balance on that **same background** reads

`dn_FRW/dt = J(t)−[λ(t)+3H(t)]n_FRW`.

Thus for state `u=ln n` with η=ln a, the missing correction is exactly **−3 in `du/dη`**, not −3H in `du/dη`. Whether an owner change to full 10D should be made remains controlled by source semantics and model validation; no change made by REC11.

Negative exact thought test: set J=λ=0, H>0 and initial density positive. Source predicts `n_code(a)=n_i`, whereas FRW predicts `n_FRW(a)=n_i (a_i/a)^3`. For a doubling of a, the two densities differ by factor **8**. This is an exact structural null, not a prediction for real hadrons when their injection/decays remain switched on.

## 3. New REC11 sharp all-source fixed-background comparison

Let the same t interval, same positive nondecreasing a, same nonnegative time-dependent integrable J,λ and same initial `n_i>=0` be supplied to both laws. Define `E_s=exp(-∫_s^t λ(v)dv)`, `a_i=a(t_i)`, `a_f=a(t_f)`. Integrating factors give:

`n_code(t_f)=n_i E_i+∫_(t_i)^(t_f) J(s)E_s ds`;

`n_FRW(t_f)=n_i E_i (a_i/a_f)^3+∫_(t_i)^(t_f) J(s)E_s (a(s)/a_f)^3 ds`.

Since `(a_i/a_f)^3<= (a(s)/a_f)^3 <=1`, for **all** nonnegative source and loss histories:

**`(a_i/a_f)^3*n_code(t_f) <= n_FRW(t_f) <= n_code(t_f)`.**

When `n_code>0`, the interval `[(a_i/a_f)^3,1]` for the corrected/unadjusted density ratio is **globally SHARP in this model class**:
- lower endpoint: J=0, n_i>0;
- upper supremum: positive injection arbitrarily concentrated at terminal time.

There is no universal tighter inequality from expansion history alone. More importantly, this is NOT an ordering of actual fully coupled Wu–Xu 10D outcomes, since modifying hadron equations changes n_j, neutron fraction X_n, bath background and perhaps H/source trajectories. It does NOT determine the sign or magnitude of corrected Yp or any β contour.

Constant positive H,J,λ with n_i=0 at long times gives exact limiting `n_FRW/n_code=λ/(λ+3H)`; for λ/H=.1,1,10,100,1000, respectively ratios 1/31, 1/4, 10/13, 100/103,1000/1003. A demonstrably large loss/H ratio can suppress this correction, but this ratio has not been source-evaluated at every time for six channels.

## 4. Independent executed controls and limitations

Direct source line/block inspection and Git original blob PASS. Independent LOCAL Python3 stdlib `verify_rec11_rot022_source_dilution.py`, not imported from the owner:
- exact `Fraction` lower bound 1/8 for expansion-factor 2;
- five independent positive-source/loss/fixed-H cases using closed-form and separate RK4 integrator (10,000 steps, both source/FRW), all PASS;
- all six source channel name accounting;
- five analytic steady λ/H cases PASS;
- deterministic JSON/stdout generated.

LOCAL six-member ZIP `IW_REC11_ROT022_WUXU_HADRON_EXPANSION_DILUTION_REFEREE_REPRO_001_20261112.zip` SHA256 **6642027439971dd44714fddf115293745b41d292c62e68304c24a1ccc3a17a59**: CRC PASS, five payload SHA256 PASS, clean isolated re-execution JSON/stdout byte-identical PASS. The ZIP is local only, not claimed hosted GitHub.

**HOLD:** no native Wu–Xu Julia 10D execution, real loss/H timeline or E4 spectra, final journal Fig5 executable identity, empirical BBN/Yp or PBH exclusion, physically validated comoving-vs-physical source reinterpretation. The journal authors may have intended a quasi-steady closure; this must be validated rather than silently editing code.

**PASS scoped original source mismatch and exact conditional envelope / NOT physical correction validated / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN**. Owner Mech-S9 to decide model meaning; Badacz owns original Julia native runs; Moderator owns execution budget; AUD1 may independently referee. No automatic task cascade, BW ingest or owner acceptance.

RETURN_ID: `IW_REC11_ROT022_WUXU_HADRON_HUBBLE_DILUTION_SOURCE_REFEREE_001_20261112`.
