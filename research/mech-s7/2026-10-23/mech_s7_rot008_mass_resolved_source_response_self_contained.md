# Mech-S7 ROT008 — mass-resolved source-law response and prior-volume subtraction gate

```yaml
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
RETURN_ID: MECH-S7-FRONTB-MASS-RESOLVED-SOURCE-CONTRAST-ROBUSTNESS-008_20261023
PROBLEM_ID: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
TYPE: EXECUTED_CONDITIONAL_SEVEN_DIMENSIONAL_MASS_WINDOW_CONTROL / NO_NEW_PHYSICS
STATUS: SOURCE-LOCAL_DIAGNOSTIC / LOW-MASS_E2b_HOLD
NO_CANON: true
NO_EXEC_SIGN: true
NO_NOVELTY: true
NO_MODERN_Yp_DH: true
NO_PBH_BOUND: true
ORIGINAL_JULIA_10D: NOT_EXECUTED
BW_INGEST: NOT_VERIFIED
```

## 1. Research question and material answer

**Question**: In conditional Mech-S7 ROT006–007 seven-variable Wu–Xu terminal kinetics, *which PBH mass bands* contribute most to the opposing paper-versus-public source-law terminal neutron-fraction contrasts? Does this location persist across source-amplitude, inherited-population, integrator, and numerical-tolerance changes? This is different from ROT007's *species*-wise Shapley attribution and ROT005's *survivor*-population memory window.

**Answer**: A bounded (deliberately counterfactual) mass-window source-law replacement shows that the largest single effect comes from M=5e8..2e8g in both charge maps. Replacing public source spectra by paper M^-1.3 only at **M > 1e8 g** reproduces 87.3127% (B_exec) and 91.0156% (B_sym) of the respective complete below-edge endpoint contrasts. Replacement only above 2e7g gives 99.0729% / 99.1053%. Relative mass localization persists at source amplitude multipliers 0.5,1,2, **even though at 0.5 the B_exec total sign flips**. Population initial-state zero/archived/double perturbations give nearly identical mass response fractions. These are a precisely typed CONDITIONAL model result; they are NOT a universal sensitivity bound on unknown physical hadron emission.

Crucial subtraction: the source-only **emitted-hadron paper-minus-public fluence difference** is already ~91.0% above 1e8g under the two power laws and a constant mass-cube rate. Thus most localization is **not a newly discovered preferential kinetic window**, but inherited from the mass distribution of the imposed power-law contrast. The detailed distinction lies in the map-specific response efficiency: B_exec has a notably weaker endpoint contribution from the highest 1e9–5e8g shell than source-only fluence, and a stronger contribution from the 5e8–2e8g and 2e8–1e8g shells; B_sym follows source-only proportions more closely. No physical novelty asserted.

## 2. Provenance, carrier and actual execution

Pinned upstream Wu–Xu public Julia `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, particularly `arXiv-2509.05618/main-scan.jl`, `tool_script-hadrons_from_PBH.jl`, and `tool_script-parameters.jl`. Original archived external 2x2 raw Actions trajectory ZIP SHA256: public `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`, paper `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`; checksum verified in the fully executed scripts. Exactly one background T(t), a(t) selected from archived `public_exec`; map-dependent X and six initial hadron populations selected from public_exec/public_sym at sample 1469. **Surrogate edge**: that initial state was measured at approximately M=1.84e9g in the archived run but is re-used at the exact analytic M=1e9g table edge for the reduced 7D analysis. This mismatch is not repaired or concealed.

7D carrier: neutron fraction X and six hadron populations; source-native reaction/decay terms, X-dependent rates, SM weak neutron evolution; exact mass-cube clock `Gamma=4.207579833788249e27 g³/s`; source-active `u=M/1e9g` in `[Ucut,1]`, `Ucut=6exp(-20)`; no physical subedge hadronization; then full hadron decay/reactions are retained after PBH source OFF until the PCHIP common-temperature event T_nuc=0.078185270688319950 MeV. Every **one-shell** perturbation sets all five source spectra to paper power law inside that bin, and returns them to source-public slopes outside it. Piecewise ODE integration is explicitly STOPPED/RESTARTED at each jump to prevent adaptive steps jumping source discontinuities. Use common source initialization and exact fixed-T event, not comparisons at common a.

Tolerances: SciPy Radau `rtol=3e-8` (`atol=rtol*1e-3` state variable scale), repeat Radau `3e-9`, plus independent BDF `3e-8`. More detailed rows in CSV. BDF agrees in high-response windows but shows outliers ~1e-7 in some tiny/deep mass bins; accordingly fine (<1e-7-level) mass-bin attributions are NOT accepted as numerically precise. The sign and dominant 1e8..1e9g region are reproducible. We did NOT execute original Julia 10D, its source-active accepted steps, a corrected adiabatic PBH cosmological background or any modern nuclear network.

## 3. Mass-shell results

At `rtol=3e-8`, complete law contrast (paper-public at fixed T): `B_exec = -6.872832670923312e-6`, `B_sym = +2.245634883379921e-5`.

| M high → M low [g] | B_exec shell ΔX | B_exec % of full | B_sym shell ΔX | B_sym % of full |
|---|---:|---:|---:|---:|
| 1e9 → 5e8 | -8.570214e-7 | 12.470% | +7.941298e-6 | 35.363% |
| 5e8 → 2e8 | -3.687235e-6 | 53.649% | +9.548360e-6 | 42.520% |
| 2e8 → 1e8 | -1.503272e-6 | 21.873% | +3.085849e-6 | 13.742% |
| 1e8 → 5e7 | -5.965555e-7 | 8.680% | +1.280683e-6 | 5.703% |
| 5e7 → 2e7 | -2.367565e-7 | 3.445% | +5.758524e-7 | 2.564% |
| below 2e7 | sum small conditional | ~0.90% | sum small conditional | ~0.93% |

One-at-a-time shell ΔX are **not additive identities** because each interval's forward solve starts from the unchanged public baseline and the nonlinear neutron dynamics couples intervals. Sum all 12 isolated shell differences: exec -6.942587673e-6 (interaction/full minus shell sum +6.97550e-8); sym +2.263962984e-5 (interaction -1.83281e-7). These residuals are dynamic nonlinear interactions as well as integrator discretization, not statistical uncertainties.

## 4. Direct cumulative switch and amplitude/initial controls

| Source law PAPER applied ONLY for M above boundary | Exec relative to full | Sym relative to full |
|---|---:|---:|
| M > 2e8 g | 65.870% | 77.527% |
| M > 1e8 g | 87.313% | 91.016% |
| M > 5e7 g | 95.760% | 96.597% |
| M > 2e7 g | 99.073% | 99.105% |

At exact complementary boundary M=1e8 g, paper ONLY below contributes 13.056% exec / 9.177% sym, and the remainder to 100% is the nonadditive cross-window term. Do not interpret either as an unconditional uniform error bound for a source replacement.

| Frozen hadron-source scale (not physical β scan) | Exec ΔX | Exec fraction M>1e8 | Sym ΔX | Sym fraction M>1e8 |
|---:|---:|---:|---:|---:|
| 0.5 | +1.054285e-6 | 89.527% | +1.541205e-5 | 90.712% |
| 1.0 | -6.872833e-6 | 87.313% | +2.245635e-5 | 91.016% |
| 2.0 | -3.059061e-5 | 86.619% | +2.094575e-5 | 92.460% |

This is a clean discriminating separation: sign robustness **FAILS** with source amplitude, but relative mass-location robustness **PASSES** under the stated frozen-source normalization stress. Since the PBH expansion/energy-injection background is NOT recomputed when changing source amplitude, this is NOT a self-consistent physical variation of primordial β.

| Initial hadron populations at surrogate edge | Exec ΔX | Exec M>1e8 fraction | Sym ΔX | Sym M>1e8 fraction |
|---|---:|---:|---:|---:|
| ZERO | -6.872555e-6 | 87.3126% | +2.245667e-5 | 91.0156% |
| ARCHIVE | -6.872833e-6 | 87.3127% | +2.245635e-5 | 91.0156% |
| DOUBLE | -6.873103e-6 | 87.3128% | +2.245604e-5 | 91.0156% |

These zero/double controls do not cover uncertainty in X at table edge nor in earlier cosmological state; those are distinct unclosed error sources.

## 5. Source-only fluence subtraction and its limits

Pinned first-two-row source slopes are `s_pion=-1.200486`, `s_K=-1.196651`, `s_K0L=-1.196805`, `s_pbar=-1.204291`, `s_nbar=-1.204763`. In the executable mass law `dt/du=-3(M_edge³/Gamma)u²`, per-PBH emitted paper-minus-public fluence in any window `[lo,hi]` is (apart from common units and edge amplitude)

\[\Delta N_h(lo,hi)\propto Q_h(M_{edge})\int_{lo}^{hi}(u^{2-1.3}-u^{2+s_h})du.\]

The closed expression is `[hi^1.7-lo^1.7]/1.7 - [hi^(3+s_h)-lo^(3+s_h)]/(3+s_h)`. The executable six-species source-column weights (including literal vs 0.5 charge mappings) give virtually identical proportional source-only mass distributions for both maps: 34.18% at 1e9..5e8, 42.95% at 5e8..2e8, 13.90% at 2e8..1e8; total >1e8 about 91.03%. (The text uses rounded percentages; exact CSV retains coefficients.)

**Host subtraction / negative knowledge**: Finding most endpoint influence at M>1e8 is largely **expected from elementary power-law integration**: it is not novel dynamical physics. The source-only 91% comparison exposes the nontrivial conditional response: B_exec 12.47% versus ~34.18% emitted contrast in highest bin (response efficiency ~0.365), and 53.65% versus ~42.95% in next bin (~1.249). B_sym gives ~35.36% vs 34.18% and ~42.52% vs 42.95%, closer to unweighted fluence. This difference is an X-dependent directional reaction/kinetic effect in this 7D carrier, NOT certified real PBH phenomenology.

## 6. Scientific decision and falsifiers

1. **Source-validation targeting**: for reproducing this specific 7D paper/public contrast, the first low-mass source certification priority is the whole band **1e9..1e8 g**, not exclusively M<1e7g where survivor populations become very sensitive. But since ALL these masses lie below the source tabulation edge M=1e9g, no portion currently establishes a physically supported endpoint.
2. **Numerical acceptance**: original source-native common-background Julia 10D with exact mass M³ control, accepted internal states M<1e9g and a tolerance/step ladder; target fixed T_nuc with terminal moving-event numerical error. MT13 criterion `uniform global endpoint epsilon_X<6.33356560558e-6` was sufficient for the archived four-cell signs (not a certified bound here). Sensitivity to original background's nonadiabatic cooling anomaly needs separate model-legal correction, not an arbitrary T(t) fudge.
3. **Mechanism kill**: supply alternative source-valid low-mass hadronization; if source-law X response mass-bin distribution or map sign is not stable under justified source variations, demote the claimed mechanism. Compare full 2x2 interaction and source corrections after subtracting mature ODE response hosts.
4. **Source-version helium gate**: DAX-S7 / PRF11 R20 / LT5 determined article/v3/Julia helium observable retyping mismatch, and DAX-S7 / PRF11 R21 found no-PBH thermodynamic-tabulation cooling mismatch. We calculate **only X** and no Yp/D/H / likelihood / PBH upper bound. Claim transfer to physical abundance explicitly PROHIBITED.

Provenance priorities: DAX-S7 first cooling mismatch, PRF11 R21 independently source-table integrated; DAX/PRF11 helium-version custody; MT13/LT5 event-time and identifiability theory; Mech ROT006–007 initial mechanistic conditional 7D; Mech ROT008 only mass localization/controls. Physics/external novelty: NONE.

**STOP**: no E2b physical source, no original 10D global error certificate, no covariant/gravity claim, no Yp/DH endpoint; no new institutional EXEC or BW state implied by GitHub publication.


---

## Reproducibility Appendix 1: reproduce_mass_shell_response_008.py

```python
#!/usr/bin/env python3
"""Mech-S7 rotation 006: independent 7D (X plus six hadron densities)
conditional last-table-edge-to-cutoff and postsource replay, exactly controlled
M^3(t), source-native Wu-Xu 6-channel collision rates, 2x2 variants.
NOT original Julia 10D, no credible subtable hadron emission, no physical bounds.

Input 2 original actions archives with enforced SHA256 checks; SciPy/Numpy/Pandas.
"""
import argparse, hashlib, io, json, math
from pathlib import Path
from zipfile import ZipFile
import numpy as np, pandas as pd
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

PUB='75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5'
PAP='3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e'
UPSTREAM='d395183674cace6c9906a8911bdeb7234ba4040d'
# Pinned ROT004 source-derived mass-cube rate for hot PBH and mass cutoff:
GAMMA=4.207579833788249e27 # g^3/s
M_EDGE=1e9; M_CUT=6e9*math.exp(-20); U_CUT=M_CUT/M_EDGE
DT_EDGE=M_EDGE**3/GAMMA; T_NUC=.078185270688319950 # MeV
# Wu-Xu table first two rows in natural GeV mass/rate, near 1e9 g:
M1=5.609588603804452e32; M2=6.099798045788406e32
Q1=np.array([489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596])
Q2=np.array([442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213])
SLOPES=np.log(Q2/Q1)/math.log(M2/M1)
INDEX=np.array([0,0,1,2,3,4])
SPECIES=['pi_minus','pi_plus','K_minus','K0L','pbar','nbar']
HBAR_GEV_SEC=6.582119569e-25
C_CMS=299792458e2
MBARN_CM2=1e-27
SIGMA_V_UNIT=MBARN_CM2*C_CMS
M_P_MEV=938.27208816
Q_MEV=939.5654205-M_P_MEV
TAU_N=878.4
ALPHA=1/137.035999084
ETA_B=6.1e-10
ZETA3=1.202056903159594
HBARC_MEV_CM=197.3269804e-13
NSCALE=1e16 # n_h in cm^-3, transform for numerical conditioning

def checksum(path,digest):
    b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()==digest
    return b

def load(pub,pap):
    data={}
    with ZipFile(io.BytesIO(checksum(pub,PUB))) as z:
        for name,fn in [('public_exec','current'),('public_sym','repaired')]:
            data[name]=pd.read_csv(io.BytesIO(z.read('trajectory_'+fn+'.csv')))
    with ZipFile(io.BytesIO(checksum(pap,PAP))) as z:
        for name,fn in [('paper_exec','paper_exec'),('paper_sym','paper_sym')]:
            data[name]=pd.read_csv(io.BytesIO(z.read('trajectory_'+fn+'.csv')))
    for d in data.values():
        assert len(d)==1600 and d.source_active.iloc[1469]==1 and d.source_active.iloc[1470]==0
    return data

def coulomb(T,hadron_mass):
    ve=math.sqrt(T/hadron_mass)+math.sqrt(T/M_P_MEV)
    z=2*math.pi*ALPHA/ve
    return z/(-math.expm1(-z))

def rates(X,T):
    # Source-native temperature, baryon density, decay + scattering
    nB=ETA_B*(2*ZETA3/math.pi**2)*(T/HBARC_MEV_CM)**3
    fp=coulomb(T,139.57039); fk=coulomb(T,493.677)
    a=np.array([1.5*fp,0,31*fk,7,0,28.])
    b=np.array([0,1.7,26,7,28,0.])
    decay=np.array([1/2.6033e-8,1/2.6033e-8,8.1e7,2e7,0,0])
    loss=np.array([a[0]*(1-X),b[1]*X,
                    (34+26)*X+(31+14.5)*fk*(1-X),
                    17*X+17*(1-X),
                    28*X+37*(1-X),
                    37*X+28*(1-X)])
    D=decay+loss*nB*SIGMA_V_UNIT
    # Weak standard model rates: x=Q/T, Γ=(255/tau) polynomial / x^5
    x=Q_MEV/T; g=(255/TAU_N)*(12+6*x+x*x)/x**5
    weak=g*((1-X)*math.exp(-x)-X)-X/TAU_N
    return D,a,b,weak

def simulate(df,mapname,law,rtol,initial,with_weak=True,floor=0,temperature_variant='saved',post_memory=True,method='Radau',source_scale=1.0,switch_window=None):
    # TRUE common background extracted from the SINGLE archived 'public_exec' cell.
    # All four 2x2 branches share it, regardless of their archived own T(t).
    time=df.t_sec.to_numpy(); temp=df.T_GeV.to_numpy()*1000
    aa=df.a.to_numpy()
    t0=float(time[0]);m0=float(df.m_PBH_g.iloc[0])
    t_edge=t0+(m0**3-M_EDGE**3)/GAMMA
    t_cut=t_edge+(M_EDGE**3-M_CUT**3)/GAMMA
    # Exact event readout for the selected PCHIP common background, not linear-in-time
    # nor Wu-Xu's archived linear-in-Q/T output interpolation.
    fT=PchipInterpolator(time,temp,extrapolate=False)
    end_idx=int(np.where(temp<T_NUC)[0][0])
    t_eval=float(brentq(lambda z:float(fT(z))-T_NUC, float(time[end_idx-1]),float(time[end_idx]),xtol=1e-12))
    assert abs(float(fT(t_eval))-T_NUC)<1e-12
    fa=PchipInterpolator(time,np.log(aa),extrapolate=False)
    nPBH0=source_scale*float(df.n_PBH_cm3.iloc[1469]); a0=float(df.a.iloc[1469])
    def nPBH(t):
        return nPBH0*math.exp(-3*(float(fa(t))-math.log(a0)))
    # Edge rates: natural GeV emitted per PBH per time, convert by HBAR, multiply by nPBH
    factor=np.ones(6) if mapname=='exec' else np.array([.5,.5,.5,1,.5,.5])
    exponent=SLOPES if law=='public' else np.full(5,-1.3)
    edge_Q=Q1[INDEX]
    expo=exponent[INDEX]
    if initial=='archive':
        y0=np.concatenate([[float(df.Xn.iloc[1469])],np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in SPECIES])/NSCALE])
    elif initial=='zero':
        y0=np.concatenate([[float(df.Xn.iloc[1469])],np.zeros(6)])
    elif initial=='double':
        y0=np.concatenate([[float(df.Xn.iloc[1469])],2*np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in SPECIES])/NSCALE])
    else:raise ValueError(initial)
    def dXdt(X,pop,T):
        D,a,b,weak=rates(X,T)
        converted=np.sum(pop*NSCALE*SIGMA_V_UNIT*((1-X)*a-X*b))
        return (weak if with_weak else 0)+converted,D,converted
    segment_paper = False
    def rhs_u(u,y):
        # u=M/M0, so dt/du=-3*(M0^3/GAMMA)*u^2; source finite in u even as u->0
        t=t_edge+DT_EDGE*(1-u**3)
        T=float(fT(t))
        X=float(y[0]);n=y[1:]
        f,D,_=dXdt(X,n,T)
        # All five source spectra switch together within this mass shell.
        # Piecewise boundary-aware integration below ensures source jumps are not crossed blindly.
        effective_expo = (np.full(6,-1.3) if segment_paper else SLOPES[INDEX]) if switch_window is not None else expo
        s=edge_Q*factor*nPBH(t)/HBAR_GEV_SEC * u**effective_expo /NSCALE
        return -3*DT_EDGE*u*u*np.concatenate([[f],s-D*n])
    cuts=[1.,U_CUT] if switch_window is None else sorted(set([1.,U_CUT, *switch_window]), reverse=True)
    sols=[]; y_current=y0.copy(); total_nfev=0; total_nsteps=0
    for u_start,u_end in zip(cuts[:-1], cuts[1:]):
        if u_start==u_end: continue
        u_middle=math.sqrt(u_start*u_end)
        segment_paper = bool(switch_window and (switch_window[0] < u_middle < switch_window[1]))
        sol=solve_ivp(rhs_u,(u_start,u_end),y_current,method=method,rtol=rtol,atol=rtol*1e-3,
                     max_step=.02,dense_output=True)
        if not sol.success:raise RuntimeError(f'{u_start} to {u_end}: {sol.message}')
        y_current=sol.y[:,-1];total_nfev+=sol.nfev;total_nsteps+=len(sol.t)
        sols.append((u_start,u_end,sol))
    probes_u=[1.,.5,.25,.1,.05,.02,.01,.005,.001,1e-4,1e-5,U_CUT]
    probes=[]
    for uu in probes_u:
        found=[sp for high,low,sp in sols if low-1e-14<=uu<=high+1e-14]
        assert found,(uu,cuts)
        probes.append({'u':float(uu),'X':float(found[0].sol(uu)[0]),'time_after_edge_s':DT_EDGE*(1-uu**3)})
    ycut=y_current;
    def rhs_post(t,y):
        T=float(fT(t)); X=float(y[0]);pop=y[1:]
        f,D,_=dXdt(X,pop,T)
        return np.concatenate([[f],-D*pop])
    post_init=ycut.copy()
    if not post_memory:post_init[1:]=0.
    post=solve_ivp(rhs_post,(t_cut,t_eval),post_init,method=method,rtol=rtol,atol=rtol*1e-3,
                   max_step=2.,dense_output=True)
    if not post.success:raise RuntimeError(str(post.message))
    Xend=float(post.y[0,-1])
    return {'map':mapname,'law':law,'rtol':rtol,'initial':initial,'weak':with_weak,'post_memory':post_memory,'method':method,'source_scale':source_scale,'X_at_mass_probes':probes,
      'T_edge':float(fT(t_edge)),'t_edge':t_edge,'t_cut':t_cut,'t_nuc_target':t_eval,
      'X_start':float(y0[0]),'X_cut':float(ycut[0]),'X_target':Xend,
      'F_cut_per_sec':dXdt(float(ycut[0]),ycut[1:],float(fT(t_cut)))[2],
      'edge_populations_cm3':list((y0[1:]*NSCALE).astype(float)),
      'cut_populations_cm3':list((ycut[1:]*NSCALE).astype(float)),
      'u_nfev':int(total_nfev),'post_nfev':int(post.nfev),'u_nsteps':total_nsteps,
      'post_nsteps':len(post.t),'step_end_min_u':float(sols[-1][2].t[-2]-sols[-1][2].t[-1]),
      'condition':'7D conditional subedge, initial state at saved last active mass reassigned to exact table edge; no preedge repair, no Julia or source-valid emission.'}

def run(args):
    data=load(args.public_zip,args.paper_zip)
    ref=data['public_exec']
    rows=[]
    for tol in [3e-5,3e-7,3e-9]:
      for initial in ['archive','zero','double'] if tol==3e-7 else ['archive']:
        for mp in ['exec','sym']:
          # frozen cell-specific initial populations and X are copied from public 2x2 archive
          d=data['public_exec'] if mp=='exec' else data['public_sym']
          # common public_exec background, so use separate initial data in ref via selected rows
          background=ref.copy()
          for key in ['Xn']+[f'n_{sp}_cm3' for sp in SPECIES]:
              background[key]=d[key].to_numpy()
          for law in ['public','paper']:
            row=simulate(background,mp,law,tol,initial)
            rows.append(row)
            print(mp,law,'tol',tol,'init',initial,'Xcut',round(row['X_cut'],10),'Xtarget',round(row['X_target'],10),flush=True)
    out=Path(args.outdir);out.mkdir(exist_ok=True,parents=True)
    (out/'terminal_7d_results_006.json').write_text(json.dumps({'meta':{'SOURCE':UPSTREAM,'PUBLIC_ACTION_SHA256':PUB,'PAPER_ACTION_SHA256':PAP,'MODEL':'7D reduced conditional terminal mass-controlled forward problem; source UNVALIDATED below 1e9g; X initial at edge proxy; common T(t) from archived public_exec','target':'time at PCHIP background T=0.078185270688319950 MeV'},'rows':rows},indent=2))
    summ=[]
    for tol in sorted({r['rtol'] for r in rows}):
      for initial in sorted({r['initial'] for r in rows if r['rtol']==tol}):
        temp={(r['map'],r['law']):r for r in rows if r['rtol']==tol and r['initial']==initial}
        for mp in ['exec','sym']:
            a=temp[(mp,'public')];b=temp[(mp,'paper')]
            summ.append({'rtol':tol,'initial':initial,'map':mp,'Xpub_nuc':a['X_target'],
                         'Xpap_nuc':b['X_target'],'deltaX_paper_minus_public':b['X_target']-a['X_target'],
                         'Xpub_cut':a['X_cut'],'Xpap_cut':b['X_cut'],
                         'deltaX_cut':b['X_cut']-a['X_cut'],
                         'public_min_step_u':a['step_end_min_u'],'paper_min_step_u':b['step_end_min_u']})
    pd.DataFrame(summ).to_csv(out/'terminal_7d_comparisons_006.csv',index=False,float_format='%.17g')
    print('RESULT_COMPARISONS')
    for t in summ:print(t)



# --- Rotation 008: mass-window localization, new science beyond ROT006/007 ---
import argparse as _argparse

def window_scan(args):
    raw=load(args.public_zip,args.paper_zip)
    assert math.isclose(U_CUT,6*math.exp(-20),rel_tol=1e-11)
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    # Log mass windows partition the entire unvalidated M<10^9 g interval.
    edges=[1.,.5,.2,.1,.05,.02,.01,.005,.002,.001,1e-4,1e-5,U_CUT]
    # Shared background from public_exec; map-specific initial X and populations from appropriate public map.
    source={}
    for mp in ('exec','sym'):
        d=raw['public_exec'].copy()
        selected=raw['public_exec'] if mp=='exec' else raw['public_sym']
        for key in ['Xn']+[f'n_{sp}_cm3' for sp in SPECIES]:
            d[key]=selected[key].to_numpy()
        source[mp]=d
    all_rows=[];readouts={};report={}
    for mp in ('exec','sym'):
        d=source[mp]
        pub=simulate(d,mp,'public',args.rtol,'archive',method=args.method)
        pap=simulate(d,mp,'paper',args.rtol,'archive',method=args.method)
        # Boundary-aware control for full window, uses paper source on one domain.
        papseg=simulate(d,mp,'public',args.rtol,'archive',switch_window=(U_CUT,1.),method=args.method)
        assert abs(pap['X_target']-papseg['X_target'])<5e-10, (mp,pap['X_target'],papseg['X_target'])
        total=pap['X_target']-pub['X_target']
        partial=[]
        for hi,lo in zip(edges[:-1],edges[1:]):
            z=simulate(d,mp,'public',args.rtol,'archive',switch_window=(lo,hi),method=args.method)
            dx=z['X_target']-pub['X_target']
            dc=z['X_cut']-pub['X_cut']
            row={'map':mp,'hi_u':hi,'lo_u':lo,'high_mass_g':hi*M_EDGE,'low_mass_g':lo*M_EDGE,
                 'deltaX_target_shell':dx,'deltaX_cut_shell':dc,
                 'full_deltaX_target':total,'source_interaction_fraction':dx/total,
                 'nfev_u':z['u_nfev'],'nfev_post':z['post_nfev']}
            all_rows.append(row);partial.append(row)
            print(mp, f'{hi:.3g}-{lo:.3g}',f'dX={dx:+.10e}',flush=True)
        shellsum=sum(z['deltaX_target_shell'] for z in partial)
        report[mp]={'public_Xtarget':pub['X_target'],'paper_Xtarget':pap['X_target'],
                   'full_contrast':total,'full_contrast_cut':pap['X_cut']-pub['X_cut'],
                   'shell_singles_sum':shellsum,'nonadditive_full_minus_singles':total-shellsum,
                   'percent_localization':[(f'{z["high_mass_g"]:.3e}..{z["low_mass_g"]:.3e}',z['deltaX_target_shell']/total) for z in partial],
                   'paper_segmented_consistency':papseg['X_target']-pap['X_target']}
        readouts[mp]={'full_public':pub,'full_paper':pap}
    cumulative=[]
    if args.cumulative:
        for mp in ('exec','sym'):
            d=source[mp]; reference=report[mp]['public_Xtarget']; total=report[mp]['full_contrast']
            for bound in (.5,.2,.1,.05,.02,.01,.001,U_CUT):
                upp=simulate(d,mp,'public',args.rtol,'archive',method=args.method,switch_window=(bound,1.))
                low=simulate(d,mp,'public',args.rtol,'archive',method=args.method,switch_window=(U_CUT,bound)) if bound>U_CUT else {'X_target':reference}
                record={'map':mp,'mass_boundary_g':bound*M_EDGE,'M_boundary_u':bound,
                    'deltaX_paper_only_above_boundary':upp['X_target']-reference,
                    'deltaX_paper_only_below_boundary':low['X_target']-reference,
                    'fraction_above':(upp['X_target']-reference)/total,
                    'fraction_below':(low['X_target']-reference)/total,
                    'nonadditivity':total-(upp['X_target']-reference)-(low['X_target']-reference)}
                cumulative.append(record)
                print('CUMULATIVE',mp,bound,'above',record['fraction_above'],'below',record['fraction_below'],flush=True)
        pd.DataFrame(cumulative).to_csv(out/'cumulative_source_window_008.csv',index=False,float_format='%.17g')
    pd.DataFrame(all_rows).to_csv(out/'mass_shell_source_response_008.csv',index=False,float_format='%.17g')
    (out/'mass_shell_source_response_008.json').write_text(json.dumps({'metadata':{'type':'CONDITIONAL_7D_SAVED_BACKGROUND_MASS-SHELL_HYBRID_SOURCE',
           'source_commit':UPSTREAM,'Q2x2_zip_hashes':[PUB,PAP], 'ratios':'all 5 spectra public outside mass shell, paper inside mass shell',
           'boundary':'piecewise solve_ivp split at both shell boundaries, postsource hadron forcing retained',
           'no_julia':True,'no_source_valid_e2b':True, 'rtol':args.rtol,'method':args.method},'maps':report,'rows':all_rows,'cumulative':cumulative},indent=2))
    print('REPORT_JSON',json.dumps(report,indent=2))

if __name__=='__main__':
    ap=_argparse.ArgumentParser()
    ap.add_argument('--public-zip',required=True);ap.add_argument('--paper-zip',required=True)
    ap.add_argument('--rtol',type=float,default=3e-8)
    ap.add_argument('--method',default='Radau',choices=['Radau','BDF'])
    ap.add_argument('--cumulative',action='store_true')
    ap.add_argument('--outdir',required=True)
    window_scan(ap.parse_args())

```


---

## Reproducibility Appendix 2: reproduce_cumulative_source_cutoff_008.py

```python
#!/usr/bin/env python3
"""ROT008: independent shell cutoff attribution. Requires adjacent reproduce_mass_shell_response_008.py.
No Julia native 10D; source-unvalidated 7D conditional test only.
"""
import importlib.util, json, sys, argparse
from pathlib import Path
import pandas as pd

ap=argparse.ArgumentParser()
ap.add_argument('--public-zip',required=True)
ap.add_argument('--paper-zip',required=True)
ap.add_argument('--outdir',required=True)
ap.add_argument('--rtol',type=float,default=3e-8)
ap.add_argument('--method',default='Radau')
a=ap.parse_args()
file=Path(__file__).with_name('reproduce_mass_shell_response_008.py')
s=importlib.util.spec_from_file_location('mass_shell_008',file)
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
raw=m.load(a.public_zip,a.paper_zip);out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
rows=[]
for mp in ('exec','sym'):
    d=raw['public_exec'].copy()
    selected=raw['public_exec' if mp=='exec' else 'public_sym']
    for key in ['Xn']+[f'n_{sp}_cm3' for sp in m.SPECIES]:d[key]=selected[key].to_numpy()
    ref=m.simulate(d,mp,'public',a.rtol,'archive',method=a.method)['X_target']
    pap=m.simulate(d,mp,'paper',a.rtol,'archive',method=a.method)['X_target']
    full=pap-ref
    for b in [.2,.1,.05,.02]:
        a1=m.simulate(d,mp,'public',a.rtol,'archive',method=a.method,switch_window=(b,1.))['X_target']
        a2=m.simulate(d,mp,'public',a.rtol,'archive',method=a.method,switch_window=(m.U_CUT,b))['X_target']
        row={'map':mp,'u_boundary':b,'boundary_mass_g':b*m.M_EDGE,'full_delta':full,
             'above_delta':a1-ref,'below_delta':a2-ref,'ratio_above':(a1-ref)/full,
             'ratio_below':(a2-ref)/full,'interaction':full-a1-a2+2*ref}
        rows.append(row)
        print(row,flush=True)
pd.DataFrame(rows).to_csv(out/'cumulative_source_cutoff_008.csv',index=False,float_format='%.17g')
(out/'cumulative_source_cutoff_008.json').write_text(json.dumps({'conditional_model':'7D common archived background; postsource hadrons remain; source below 1e9 g unvalidated', 'rtol':a.rtol,'method':a.method,'rows':rows},indent=2))

```


---

## Reproducibility Appendix 3: reproduce_amplitude_mass_cutoff_008.py

```python
#!/usr/bin/env python3
"""Conditional 7D source-normalization robustness of source-law mass localization.
Scale applies ONLY to hadron source, not PBH background. Mechanism stress test, NOT self-consistent beta scan.
Requires adjacent reproduce_mass_shell_response_008.py and original SHA-checked ZIPs.
"""
import argparse, importlib.util, json
from pathlib import Path
import pandas as pd
ap=argparse.ArgumentParser();ap.add_argument('--public-zip',required=True);ap.add_argument('--paper-zip',required=True)
ap.add_argument('--outdir',required=True);ap.add_argument('--rtol',type=float,default=3e-8)
a=ap.parse_args()
s=importlib.util.spec_from_file_location('ms008',Path(__file__).with_name('reproduce_mass_shell_response_008.py'))
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
r=m.load(a.public_zip,a.paper_zip);rows=[]
for mp in ('exec','sym'):
 d=r['public_exec'].copy();src=r['public_exec' if mp=='exec' else 'public_sym']
 for key in ['Xn']+[f'n_{sp}_cm3' for sp in m.SPECIES]:d[key]=src[key].to_numpy()
 for amp in [0.5,1.,2.]:
  opts={'source_scale':amp,'method':'Radau'}
  pub=m.simulate(d,mp,'public',a.rtol,'archive',**opts)['X_target']
  paper=m.simulate(d,mp,'paper',a.rtol,'archive',**opts)['X_target']
  total=paper-pub
  upper=m.simulate(d,mp,'public',a.rtol,'archive',switch_window=(.1,1.),**opts)['X_target']
  lower=m.simulate(d,mp,'public',a.rtol,'archive',switch_window=(m.U_CUT,.1),**opts)['X_target']
  row={'map':mp,'amplitude':amp,'Xpub':pub,'Xpaper':paper,'deltaX':total,'above_1e8':upper-pub,'below_1e8':lower-pub,
       'pct_above_1e8':100*(upper-pub)/total,'pct_below_1e8':100*(lower-pub)/total,'interaction':total-(upper-pub)-(lower-pub)}
  rows.append(row);print(row,flush=True)
out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
pd.DataFrame(rows).to_csv(out/'amplitude_mass_cutoff_008.csv',index=False,float_format='%.17g')
(out/'amplitude_mass_cutoff_008.json').write_text(json.dumps({'metadata':{'type':'7D CONDITIONAL NORMALIZATION STRESS; NOT β_PBH SCAN','rtol':a.rtol},'rows':rows},indent=2))

```


---

## Reproducibility Appendix 4: reproduce_initial_state_gate_008.py

```python
#!/usr/bin/env python3
"""Mech-S7 ROT008: source-mass response dependence on inherited edge populations.
Check conditional 7D initial population sensitivity only; not source-valid interpolation between saved M=1.84e9 and edge M=1e9 g.
Requires reproduce_mass_shell_response_008.py from same folder and validated original zips.
"""
import argparse,importlib.util,json
from pathlib import Path
import pandas as pd
ap=argparse.ArgumentParser();ap.add_argument('--public-zip',required=True);ap.add_argument('--paper-zip',required=True);ap.add_argument('--outdir',required=True);ap.add_argument('--rtol',type=float,default=3e-8)
a=ap.parse_args();spec=importlib.util.spec_from_file_location('ms008',Path(__file__).with_name('reproduce_mass_shell_response_008.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
raw=m.load(a.public_zip,a.paper_zip);rows=[]
for mp in ('exec','sym'):
 d=raw['public_exec'].copy();parent=raw['public_exec' if mp=='exec' else 'public_sym']
 for k in ['Xn']+[f'n_{sp}_cm3' for sp in m.SPECIES]:d[k]=parent[k].to_numpy()
 for initial in ('zero','archive','double'):
  o={'method':'Radau'}
  pub=m.simulate(d,mp,'public',a.rtol,initial,**o)['X_target']
  pap=m.simulate(d,mp,'paper',a.rtol,initial,**o)['X_target']
  high=m.simulate(d,mp,'public',a.rtol,initial,switch_window=(.1,1.),**o)['X_target']
  row={'map':mp,'initial_populations':initial,'delta_full':pap-pub,'delta_above_1e8':high-pub,'frac_above_1e8':(high-pub)/(pap-pub),'Xpub':pub,'Xpap':pap}
  rows.append(row);print(row,flush=True)
out=Path(a.outdir);out.mkdir(parents=True,exist_ok=True)
pd.DataFrame(rows).to_csv(out/'initial_state_cutoff_008.csv',index=False,float_format='%.17g')
(out/'initial_state_cutoff_008.json').write_text(json.dumps({'model':'CONDITIONAL_7D initial population sensitivity','rtol':a.rtol,'rows':rows},indent=2))

```