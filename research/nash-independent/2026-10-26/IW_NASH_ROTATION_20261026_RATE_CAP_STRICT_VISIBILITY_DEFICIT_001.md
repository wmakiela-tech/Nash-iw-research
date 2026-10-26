---
artifact_id: IW_NASH_ROTATION_20261026_RATE_CAP_STRICT_VISIBILITY_DEFICIT_001
created_at: 2026-10-26
origin_cell: NASH_INDEPENDENT_SCIENCE_ROTATION / NO_LT6_ACTIVATION
problem_id: PRF11_R35_FIXED_PROTOCOL_MAX_SWAP_CADENCE_VISIBILITY_NO_GO
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_EXACT_PROOF / FINITE_NUMERIC_SELF_CHECK_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_DEVICE / NO_FULL_ADAPTIVE_PROCESS_TESTER / NO_BW_INGEST_ASSUMPTION
---

# NASH independent rotation: fixed-switch-rate cap forces a strict asymptotic discrimination deficit

**Date 2026-10-26.** Precise scope: extension of PRF11 R35 with a fixed rate floor; not a novelty claim. Source-first / two-surface prior art: PRF11 R29–R32 original Cauchy common-phase vs independent-increment hypotheses and ideal SWAP probes; PRF11 R34 equal-grid age-memory marked Poisson; MT13 ROT040 exact count/age-bin compression; PRF11 R35 general unequal-grid states and the schedule with zero asymptotic age; earlier local NASH G1/G2 (2026-10-26) asymptotic full-X versus optimal final-POVM comparison and Poisson count limit. The PRF11 R35 text already noticed that a lower interval floor prevents its sufficient zero-age construction; **the present narrower scientific delta** is an explicit strictly positive *full-final-POVM* bound and a sharp *count-only* design envelope. External mathematical host: common-noise Markov garbling, Helstrom trace distance, Le Cam Poisson-binomial approximation. Publication priority and external referee unestablished.

## 1. Exact source model and domain

Fix `a=gamma*T>0`, `beta>0`, `0<c<=1`, and positive deterministic time increments `d_j=Delta_j/T` for j=1,...,n, satisfying

`sum d_j=1`, `E_n=sum d_j^2 -> 0`, `d_j>=c/n`.

Define `u_j=sum_{k>j} d_k=(T-t_j)/T`, common memory dephasing `r_j=exp(-beta*u_j/n)`, independent-increment visibility `q_j=exp(-a*d_j)`. The complete terminal n-qubit states are **precisely PRF11 R35 equation (35.1)**, under the fixed ideal-SWAP schedule with age-dependent endpoint dephasing; no adaptive process testers, active error correction, physical memory calibration, SWAP errors or jitter. The relevant quantum discrimination is `D_Q=||rho_A-rho_B||_1/2` (all **final** POVMs only).

## 2. Exact finite-n single-click overlap inequality (E1)

For the full local X readout under a **commuting reference pair**, introduce independent bits `Z_j~Bern(b_j)`, `S_j~Bern(s_j)`, where `b_j=(1-exp(-beta*u_j/n))/2` and `s_j=(1-exp(-a*d_j))/2`. The first law `P=Law(Z)` is the X measurement of reference `Sigma_A=otimes_j(I+r_j X)/2`, and `Q=Law(Z XOR S)` is exactly the X law of `rho_B=otimes_j(I+r_j*q_j X)/2`. Write `p0=prod(1-s_j)`, `B0=prod(1-b_j)`. Then

`TV(P,Q) <= 1-p0-delta_n`,

`delta_n=B0*sum_j min{(1-p0)*b_j/(1-b_j), p0*s_j/(1-s_j)} >=0.` **[E1]**

Proof: `Q(y)>=p0*P(y)` because S=0 has probability p0. Thus the overlap `sum_y min(P(y),Q(y))` equals `p0+sum_y min((1-p0)P(y), Q(y)-p0 P(y))`. For each distinct singleton word y=e_j, `P(e_j)=B0*b_j/(1-b_j)` and `Q(e_j)-p0P(e_j)>=B0*p0*s_j/(1-s_j)` (one signal flip at j and zero background). Summing these n nonnegative singleton lower bounds proves E1.

## 3. Strict asymptotic quantum deficit (E2)

Put `p=exp(-a/2)` and

`Delta(a,beta,c)=exp(-beta/2)*(beta*c/4)*min{1-p, p*a*c/beta}>0`.

**Theorem E2.**

`limsup_{n->infty} D_Q <= 1-exp(-a/2)-Delta(a,beta,c).`

In trace norm, the corresponding bound is multiplied by 2. Hence for all fine deterministic schedules obeying the fixed `c/n` floor, even the globally optimal **terminal** quantum measurement cannot attain PRF11 R35's ideal-memory asymptotic limit `1-exp(-a/2)` in total-variation units.

Proof: the floor yields `u_j>=c(n-j)/n` and mean age `m_n=n^-1 sum_j u_j >=c(n-1)/(2n)`. Since `max d_j<=sqrt(E_n)->0`, we have
- `p0 -> p` since `log p0=-a/2+O(a^2 E_n)`;
- `B0 >= exp(-beta/2-o(1))`;
- `sum b_j/(1-b_j)=sum tanh(beta*u_j/(2n)) >= beta*c/4-o(1)`;
- uniformly in j, `b_j/(1-b_j) <= [beta/(a*c)]*(1+o(1))*s_j/(1-s_j)`, using `tanh(x)~x` for uniformly vanishing arguments and `d_j>=c/n`.

Substitute in E1 to get `liminf delta_n>=Delta(a,beta,c)`. The earlier G1 trace-contractivity lemma yields `|D_Q-TV(P,Q)|<=eta_n/2`, where `eta_n=E_xi min(2,|xi|T*sqrt(E_n))->0` for a single fixed random Cauchy frequency xi, by dominated convergence (no finite first moment required). Hence `D_Q <=1-p0-delta_n+eta_n/2`, proving E2. **This conclusion is specific to the fixed R35 schedule, final readout and fixed beta,c>0; it is not a physical-device or unconstrained process-comb no-go.**

## 4. Sharp count-only envelope (E3)

Let `K` be just the total number of minus-X readouts, discarding individual probe labels. The earlier G2 source-typed result, via Le Cam's Poisson-binomial theorem and G1, says for any subsequence with `m_n->m`:

`Law_A(K) ->TV Pois(beta*m/2)`,
`Law_B(K) ->TV Pois((beta*m+a)/2)`.

Because `m_n>=c(n-1)/(2n)`, and adding the *same* independent Poisson noise to both candidate laws cannot increase TV,

`limsup_n TV(Law_A(K),Law_B(K)) <= V_count(c)`,

`V_count(c)=TV(Pois(beta*c/4),Pois(beta*c/4+a/2)).` **[E3]**

**Sharpness in the count-only class:** for `h_n=ceil(sqrt(n))` choose `d_j=c/n+(1-c)/h_n` for `j<=h_n`, `d_j=c/n` for `j>h_n`. Then `E_n->0` and `m_n->c/2`, reaching `V_count(c)`. This is **not** a claim of optimality for the entire labelled X record or general final POVMs. E2 is nonsharp but applies to a strictly larger measurement class.

## 5. Numerical falsifiers / readback-safe reproducibility

Independent local Python+NumPy+SciPy reproducer `IW_NASH_20261026_schedule_cap_no_go_reproducer.py`, result JSON `IW_NASH_20261026_schedule_cap_no_go_validation.json` and SHA manifest are in the Moderator's downloadable companion ZIP `IW_NASH_ROTATION_20261026_RATE_CAP_STRICT_DEFICIT_REPRO.zip`. They run n=8,12,16,64,256,1024,4096; c=.25,.5,.8,1; uniform, early-concentrated and late-concentrated grids at a=1, beta=2. **84/84 cases PASS**, including **36 full 2^n classical-vector TV enumerations** for n<=16. For larger n no full quantum matrix calculation is alleged; count TV is computed through Bernoulli convolutions.

For c=.5, n=4096:
- uniform: mean age .499878, exact singleton lower overlap delta_n=.113048, count TV=.238656;
- early concentrated: mean age .253784, delta_n=.073971, count TV=.305011;
- late concentrated: mean age .745972, delta_n=.071561, count TV=.186461.

For a=1,beta=2: exact count-only envelope V_count(.25)=.34723547; V_count(.5)=.30643423; V_count(.8)=.26375039; V_count(1)=.23865122. Conservative E2 gap lower bounds respectively .00348641, .01394564, .03570083, .05578254. Ideal memory limit is .39346934.

**Falsifier:** a finite n with legal b_j,s_j for which `TV(P,Q)>1-p0-delta_n` refutes E1, and a legal fixed-a,beta,c fine-mesh sequence exceeding the E2 limsup refutes E2. E3 is falsified by a count-only sequence improving its Poisson-TV envelope. No quantum physical claims or independent manuscript referee.

## 6. Source paths and external mathematics

PRF11 R35 original model & schedule: https://github.com/wmakiela-tech/Nash-iw-research/blob/39979379d8fd9ac3a8f42009c01b5a3baf688f87/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md

PRF11 R34: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md

MT13 ROT040: https://github.com/wmakiela-tech/Nash-iw-research/blob/1ab0a38cc492a4303f2aa007ce615214888424e2/research/mt13/2026-10-25/mt13_rot040_prf11_r34_two_age_bins_sharp_poisson_helstrom_compression_001.md

Le Cam (1960), `An approximation theorem for the Poisson binomial distribution`: https://doi.org/10.2140/pjm.1960.10.1181 ; host-level modern treatment https://link.springer.com/article/10.1186/1029-242X-2014-291 .

**DISPOSITION**: source-typed bounded proof and numerical self-check; public GitHub archival body is neither BW ingestion nor scientific owner adoption; no novelty, physical, canon or EXEC upgrade. LT6 not activated; REV020/REV021 and source PRF11 text remain unchanged.
