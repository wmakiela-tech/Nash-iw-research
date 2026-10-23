# MECH-S7 ROT009 — conditional clock/baryon competing-error test on Front B Wu–Xu

```yaml
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
RETURN_ID: MECH-S7-ROT009-FROZEN-THERMAL-CLOCK-BARYON-SOURCE-CONTRAST-GATE-001_20261023
PROBLEM_ID: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
CLASS: EXECUTED_7D_CONDITIONAL_2FACTOR_STRESS / SOURCE_CLOCK_VS_COLLISION_KINETICS
RESULT: MATERIAL_NUMERICAL_DIAGNOSTIC / NO_PHYSICAL_UPGRADE
CANON: NO
EXEC_SIGN: NO
NOVELTY: NO
BW_INGEST: UNVERIFIED
```

## 1. Scientific question and context

Previous MECH-S7 ROT006 and ROT007 reconstructed the opposite signs of the Wu–Xu source-law contrast at source-native fixed-temperature `Xn(T_nuc)` using independent seven-variable kinetic integration (six hadron populations plus neutron fraction), controlled PBH mass-cube law, and the *common* archived Wu–Xu temperature history. The signs were sensitive to microscopic antinucleon spectral-slope differences at ~1e-4 index and source amplitude; ROT008 located mass-response mainly at 2e8–5e8 g but subtracted the trivial mass-power fluence host.

New scientific question: are these opposite-sign contrasts equally fragile under (i) the *post-evaporation thermal event clock* and (ii) the baryon density in hadron collision loss rates? This is a **causal discrimination between parameter directions** within the same conditional 7D mathematical executor, NOT thermodynamic repair or BBN sensitivity inference. It directly complements DAX-S7 ROT34–39, PRF11 R21–22, Rec10 ROT08 and MT13 fixed-temperature event-ledger results without appropriating their independent discoveries.

## 2. Exact model definition and controlled interventions

Primary Wu–Xu code pin `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`, arXiv-2509.05618. Original MECH-S6 Actions trajectory archive SHA256 public `75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5`, paper `3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e`. Input script checks both hashes. Four cells law {public logarithmic extrapolation from first two table rows, article M^-1.3} × map {B_exec, B_sym}. Re-use map-specific `Xn`, hadron populations from **last saved active sample M≈1.84e9g**, relocated as surrogate initial conditions to precisely `M_edge=1e9g`, a known unvalidated initialization of ROT006–008. Background `T(t)` and `a(t)` from public_exec single archived branch.

PBH mass follows the exact source-native hot coefficient `Gamma=4.207579833788249e27 g^3/s`, `M^3=M_edge^3-Gamma*(t-t_edge)` until fixed executor cutoff, then `SOURCE_OFF` but hadrons retained. Source-native rates/decay cross-sections reused unchanged, with one controlled artificial baryon-density multiplier `b` in the *hadron loss* equations:

`n_B,stress(T) = b × n_B,WuXu(T)`, `b ∈ {0.90,1.00,1.10}`.

This is **not** a conserved-baryon construction and is **not** a physical uncertainty interval for `eta_B`; it changes only the collision/annihilation loss rates in all stages, not PBH number, emission or weak neutron terms.

Independent *postsource clock-only* multiplier `c ∈ {0.97,0.985,1.00,1.015,1.03}` is implemented for `t>=t_cut` via

`T_c(t) = T_ref(t_cut + (t-t_cut)/c)`;
`t_nuc(c) = t_cut + c*(t_nuc(ref)-t_cut)`.

For `t<=t_cut`, the **entire source-on** and exact-mass trajectory are unchanged. This is a rigorously defined conditional deformation of an archived PCHIP `T(t)`, not the alternate adiabatic EOS from DAX/PRF and not the PRF11 R21 2.9326% time ratio. The numerical ±3% window is an a priori stress size, not a measured uncertainty or a direct physical transfer of the 1 MeV→Tnuc no-PBH host.

All 4 branch results read out at the **same branch-shared perturbed physical temperature `T_nuc=0.078185270688319950 MeV`**, not at the same `a` or arbitrary fixed `t`. Radau relative tolerance 3e-8, absolute tolerance 3e-11, piecewise source stage exact mass coordinate and postsource time solve. Clock-only change does not affect `Xn(t_cut)` at all, verified numerically as a **zero** difference in both X_cut and t_cut.

## 3. Executed results — all 15 2×2 cells have opposite law-response signs

Definition `Delta_exec=Xn(paper,exec)-Xn(public,exec)`, `Delta_sym=Xn(paper,sym)-Xn(public,sym)`. Factorial `I_X=Delta_sym-Delta_exec`. All controls are applied identically to both law branches within each charge map. Full 15-row table and 4 raw X columns exported as `thermal_clock_baryon_2factor_009.csv`.

| c (postsource clock) | b (hadron baryon-density scale) | Delta_exec | Delta_sym | I_X |
|---:|---:|---:|---:|---:|
|0.97|0.90|-1.0110132243e-5|+2.2678949812e-5|+3.2789082055e-5|
|0.97|1.00|-6.9190153893e-6|+2.2608910123e-5|+2.9527925512e-5|
|1.00|0.90|-1.0043596091e-5|+2.2526236929e-5|+3.2569833021e-5|
|1.00|1.00|-6.8728326709e-6|+2.2456348834e-5|+2.9329181505e-5|
|1.00|1.10|-4.2866348312e-6|+2.2232927598e-5|+2.6519562429e-5|
|1.03|1.00|-6.8260914396e-6|+2.2304754353e-5|+2.9130845793e-5|
|1.03|1.10|-4.2575913054e-6|+2.2082379662e-5|+2.6339970968e-5|

Extremal full-grid ranges:

`Delta_exec ∈ [-1.0110132243e-5, -4.2575913054e-6]`,
`Delta_sym ∈ [+2.2082379662e-5, +2.2678949812e-5]`.

For fixed `b=1`, clock c=0.97→1.03 changes **absolute** `public_exec Xn` from `0.40050537215` to `0.39511552766` (swing **0.00538984449**) and shifts the source-law **contrast** by only `9.29239496e-8` (exec) and `3.04155770e-7` (sym). The former is ~776× nominal `|Delta_exec|`; the source-law subtraction cancels a large common-clock effect. This is a **common-mode subtraction within a four-cell derived diagnostic, not validated accuracy of absolute Xn or helium**.

For fixed c=1, the b=0.90→1.10 span changes Delta_exec by **5.75696126e-6 (83.76% of nominal |Delta_exec|)** but Delta_sym by only **2.93309332e-7 (1.31% of nominal |Delta_sym|)**. Thus the *directional* dependence on hadron-loss normalization is asymmetric across maps, even though both retain original contrast sign on the initial 15-cell grid.

## 4. Baryon-normalization sign boundary (separate falsifier)

At c=1, extending the stress outside the ±10% grid finds `Delta_exec(b=1.3)=-3.54334329e-7` and `Delta_exec(b=1.4)=+1.16670260e-6`. An explicit Radau (rtol3e-8) scalar root gives **b*=1.321797157**, residual `-1.81e-11` at tested resolution. This boundary is a conditional mathematical stress result; it is **not a cosmological eta_B constraint** or a validated physical parameter range. Radau with rtol3e-9 root was attempted but became prohibitively stiff; no cross-tolerance root certification claimed. ROT007 antinucleon slope ±4.6358e-5 index stress is different in type from this b perturbation.

## 5. Numerical guards and limitations

- 15/15 sign tests were executed and archived; independent re-read of CSV plus exact source-initial event calculations PASS.
- Radau `rtol=3e-8` versus `3e-9` for baseline plus four stress corners gives max `|deltaX difference|`: exec `1.43026e-9`, sym `2.22001e-9` (observed convergence only; NOT rigorous global error bound).
- `BDF` at very tight rtol3e-9 fails with `Required step size is less than spacing between numbers`, and some extreme-run BDF controls do not finish within allocated execution limits. **BDF independent-method convergence FAIL/INCONCLUSIVE, not PASS.** Results rely on Radau.
- No original source-native Julia 10D run, accepted internal adaptive steps or explicit solver global error certification. Common background is archived, not dynamically re-solved under new thermodynamics; use of exact `M^3` does NOT make background thermodynamics source-valid.
- At M<1e9g hadron emissivities are **unsupported extrapolations**; map B_exec vs B_sym are executor source-path options, not validated physical charge resolution. Nonzero hadron populations persist after source evaporation (Rec10 ROT08). Upstream hadron neutron forcing includes density floor and population kinetics; conditional replay is not the original numerical solver.
- Published JCAP/v2, pinned Julia proxy `2X/(1-X)`, and arXiv-v3 helium mass-fraction proxy `2X` are different observables (DAX-S7/PRF11 R20/LT5). This report computes `Xn` only, with no physical helium, deuterium, likelihood or bound.
- DAX-S7 ROT34–39 uncovered temperature source-code versus adiabatic mismatch; PRF11 R21 integrated source-table no-PBH code/ad ratio; PRF11 R22 reconstructed 2-temperature EOS/pressure showing nearly adiabatic micro pressure in a *specified no-PBH host*. **DO NOT substitute the ±3% scalar stretch for that two-temperature EOS or infer entropy violation from one-temperature proxy.** No neutrino kinetic effects modeled.

## 6. Mechanistic placement / competing hypotheses / next kill

`MECH-WX-H9`: Conditional endpoint law contrasts show **strong common thermal clock response but much weaker differential clock response** over c±3%, **map-asymmetric baryonic hadron-loss response**, and distinct sensitivity to tiny pbar/nbar spectral-index splitting from ROT007. This orders priorities in *this* executor: first source-valid spectra and charge map, then source-native full 10D exact-mass / accepted-step / global-error tests, then a two-temperature thermodynamic background recomputation before converting to helium/deuterium observables. No proof these rankings survive the full physical PBH/BBN system.

Cheapest kill (bounded): source-native 10D common-background Julia with exact-mass event and accepted-step source trace through 1e9→1e8 g; calculate event-aligned `X(T_nuc)` after controlled source charge-law replacements and numerical tolerance ladder. Then test an independent source-valid hadronization model and legally retyped observable. If the law-response sign is not stable under source-local variation or solver error bound, HOLD physical mapping.

Science state: `EXECUTED_CONDITIONAL_7D`; GitHub source publication does not imply BW ingest, independent Rec10/M13 referee, owner adoption or EXEC. No novelty or PBH/BBN bound claimed.

## Provenance pointers

- Wu–Xu primary fixed code: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- MECH-S7 ROT008: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_rot008_mass_resolved_source_response_self_contained.md
- PRF11 R21 source-native thermal table: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r21_integrated_thermal_table_cooling_001.md
- PRF11 R22 two-temperature pressure reconstruction: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md
- REC10 ROT08 hadron memory caveat: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-23/rec10_rot08_mech_s7_hadron_memory_gate.md

## Package and independent recomputation

Run from directory containing the two Python files:

`python execute_thermal_clock_baryon_009.py --public PATH_PUBLIC.zip --paper PATH_PAPER.zip --outdir OUTDIR`

`python execute_solver_controls_009.py` and `python execute_baryon_root_009.py` are direct controls using the same locally named source ZIPs at `/mnt/data/`. The package includes the original **SHA256 checked** public and paper Actions archives, all intermediate raw CSV/JSON, executed scripts and SHA manifest. Preserve exact file bytes and source pin. `BDF` negative outcome is retained, not silently omitted.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_SOURCE_VALID_E2B / NO_PHYSICAL_HELIUM_DH / NO_PBH_BOUND`.


---

# Complete reproduction code (appendices)

## APPENDIX — source_7d_clock_baryon_stress_009.py

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

def rates(X,T,baryon_scale=1.):
    # Source-native temperature, baryon density, decay + scattering
    nB=baryon_scale*ETA_B*(2*ZETA3/math.pi**2)*(T/HBARC_MEV_CM)**3
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

def simulate(df,mapname,law,rtol,initial,with_weak=True,floor=0,temperature_variant='saved',post_memory=True,method='Radau',source_scale=1.0,switch_window=None,clock_scale=1.,baryon_scale=1.,return_dense=False):
    # TRUE common background extracted from the SINGLE archived 'public_exec' cell.
    # All four 2x2 branches share it, regardless of their archived own T(t).
    time=df.t_sec.to_numpy(); temp=df.T_GeV.to_numpy()*1000
    aa=df.a.to_numpy()
    t0=float(time[0]);m0=float(df.m_PBH_g.iloc[0])
    t_edge=t0+(m0**3-M_EDGE**3)/GAMMA
    t_cut=t_edge+(M_EDGE**3-M_CUT**3)/GAMMA
    # Exact event readout for the selected PCHIP common background, not linear-in-time
    # nor Wu-Xu's archived linear-in-Q/T output interpolation.
    fTbase=PchipInterpolator(time,temp,extrapolate=False)
    end_idx=int(np.where(temp<T_NUC)[0][0])
    t_eval=float(brentq(lambda z:float(fTbase(z))-T_NUC, float(time[end_idx-1]),float(time[end_idx]),xtol=1e-12))
    t_ref_nuc = t_eval
    # Conditional time-clock deformation starts only AFTER source evaporation.
    # Exact on baseline T(t): T_clock(t)=T_base(t_cut+(t-t_cut)/clock_scale).
    # No PBH source or initial state is changed by clock_scale.
    if clock_scale <= 0: raise ValueError("clock_scale must be positive")
    def fT(t):
        t=float(t)
        return float(fTbase(t if t<=t_cut else t_cut+(t-t_cut)/clock_scale))
    t_eval=t_cut+clock_scale*(t_ref_nuc-t_cut)
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
        D,a,b,weak=rates(X,T,baryon_scale)
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
    return {'map':mapname,'law':law,'rtol':rtol,'initial':initial,'weak':with_weak,'post_memory':post_memory,'method':method,'source_scale':source_scale,'clock_scale':clock_scale,'baryon_scale':baryon_scale,'X_at_mass_probes':probes,
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

## APPENDIX — execute_thermal_clock_baryon_009.py

```python
#!/usr/bin/env python3
"""MECH-S7 ROT009: frozen-background 7D thermal clock and baryon controls.
Source-native Wu-Xu hadron rates, exact PBH mass; NOT full Julia or thermodynamic repair.
Requires source_7d_clock_baryon_stress_009.py in same directory and SHA-verified
archived MECH-S6 original 2x2 Actions ZIPs as CLI args.
"""
import sys,json,hashlib,argparse,math
from pathlib import Path
import pandas as pd
from source_7d_clock_baryon_stress_009 import load,simulate,SPECIES,GAMMA,T_NUC

def prepare(d,original):
    out=d.copy(deep=True)
    for k in ['Xn']+[f'n_{sp}_cm3' for sp in SPECIES]:
        out[k]=original[k].to_numpy()
    return out

def run(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--public',required=True);ap.add_argument('--paper',required=True)
    ap.add_argument('--outdir',required=True)
    args=ap.parse_args(argv)
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    raw=load(args.public,args.paper)
    common=raw['public_exec']
    df={'exec':prepare(common,raw['public_exec']),'sym':prepare(common,raw['public_sym'])}
    rows=[]
    for clock in (0.97,0.985,1.0,1.015,1.03):
      for baryon in (0.90,1.0,1.10):
       by={}
       for mp in ('exec','sym'):
        for law in ('public','paper'):
         z=simulate(df[mp],mp,law,3e-8,'archive',clock_scale=clock,baryon_scale=baryon)
         by[(mp,law)]=z
       row={'clock_scale':clock,'baryon_scale':baryon,
            't_nuc_seconds':by[('exec','public')]['t_nuc_target'],
            't_cut_seconds':by[('exec','public')]['t_cut'],
            'public_exec':by[('exec','public')]['X_target'],
            'paper_exec':by[('exec','paper')]['X_target'],
            'public_sym':by[('sym','public')]['X_target'],
            'paper_sym':by[('sym','paper')]['X_target']}
       row.update(delta_exec=row['paper_exec']-row['public_exec'],
             delta_sym=row['paper_sym']-row['public_sym'])
       row['interaction_X']=row['delta_sym']-row['delta_exec']
       row['opposite_signs']=row['delta_exec']<0 and row['delta_sym']>0
       rows.append(row)
       print(f'CLOCK={clock:.3f}, nBscale={baryon:.2f}, Dexec={row["delta_exec"]:+.10e}, Dsym={row["delta_sym"]:+.10e}, DIX={row["interaction_X"]:+.10e}',flush=True)
    pd.DataFrame(rows).to_csv(out/'thermal_clock_baryon_2factor_009.csv',index=False,float_format='%.17g')
    # Method/tolerance controls are in the separate bounded control script.
    metrics={
     'source_pin':'d395183674cace6c9906a8911bdeb7234ba4040d',
     'model':'source-native 7D hadron+X, exact M^3; archived PBH background frozen; synthetic postsource clock stretch & all-stage nB scaling',
     'clock_stretch':'Only AFTER exact PBH cut t_cut: T_c(t)=T_base[t_cut+(t-t_cut)/c], t_target_c=t_cut+c*(t_target_base-t_cut). All emission-source-stage thermal history unchanged.',
     'baryon_scaling':'For both source-active and postsource stage: nB(T) from native etaB*T^3 multiplied by synthetic b. Does not redefine etaB as physical baryon parameter or conserve baryon number.',
     'clock_reference':'A priori 0.97..1.03 envelope comparable in size (but NOT equivalent) to conditional PRF11 R21 no-PBH integrated code/adiabatic 2.93% from 1 MeV to T_nuc; actual source-active clock correction unknown.',
     'baseline':next(x for x in rows if x['clock_scale']==1 and x['baryon_scale']==1),
     'grid_n':len(rows),'num_opposite':sum(x['opposite_signs'] for x in rows),
     'ranges':{k:[min(z[k] for z in rows),max(z[k] for z in rows)] for k in ('delta_exec','delta_sym','interaction_X')},
     'min_delta_exec_state':min(rows,key=lambda x:x['delta_exec']),
     'max_delta_exec_state':max(rows,key=lambda x:x['delta_exec']),
     'tolerance_control':'See solver_controls_009.csv from separate execute_solver_controls_009.py; no BDF PASS claim',
     'claims':'NO_ORIGINAL_JULIA_10D / NO_THERMAL_SOURCE_REPAIR / NO_PHYSICAL_ENDPOINT / NO_E2B / NO_PBH_BOUND / NO_CANON / NO_EXEC'
    }
    (out/'metrics_009.json').write_text(json.dumps(metrics,indent=2))
    print('METRICS',json.dumps(metrics,indent=2))
if __name__=='__main__':run()

```

## APPENDIX — execute_solver_controls_009.py

```python
#!/usr/bin/env python3
"""Focused Radau tolerance controls for ROT009; BDF stiff challenge separately recorded."""
import sys,json
from pathlib import Path
import pandas as pd
from source_7d_clock_baryon_stress_009 import load,simulate,SPECIES
out=Path('/mnt/data/mech_s7_rotation_009')
raw=load('/mnt/data/mech_s6_public_2x2_raw.zip','/mnt/data/mech_s6_paper_2x2_raw.zip')
base=raw['public_exec']
dfs={}
for mp,orig in [('exec',raw['public_exec']),('sym',raw['public_sym'])]:
 d=base.copy()
 for k in ['Xn']+[f'n_{s}_cm3' for s in SPECIES]:d[k]=orig[k].to_numpy()
 dfs[mp]=d
rows=[]
for c,b in [(1.,1.),(.97,.9),(.97,1.1),(1.03,.9),(1.03,1.1)]:
 for rtol in [3e-8,3e-9]:
  one={'clock_scale':c,'baryon_scale':b,'method':'Radau','rtol':rtol}
  for mp in ['exec','sym']:
   a=simulate(dfs[mp],mp,'public',rtol,'archive',clock_scale=c,baryon_scale=b)
   p=simulate(dfs[mp],mp,'paper',rtol,'archive',clock_scale=c,baryon_scale=b)
   one[f'delta_{mp}']=p['X_target']-a['X_target']
  rows.append(one)
  print(one,flush=True)
pd.DataFrame(rows).to_csv(out/'solver_controls_009.csv',index=False,float_format='%.17g')
main=pd.read_csv(out/'thermal_clock_baryon_2factor_009.csv');sub=main[['clock_scale','baryon_scale','delta_exec','delta_sym']]
errors=[]
for v in rows:
 q=sub[(sub.clock_scale==v['clock_scale']) & (sub.baryon_scale==v['baryon_scale'])].iloc[0]
 for mp in ['exec','sym']:
  errors.append(abs(v[f'delta_{mp}']-q[f'delta_{mp}']))
metrics={'max_abs_delta_shift_Radau3e-9_vs3e-8':max(errors),'n_focused_runs':len(rows),'BDF_tight_problem':'BDF at rtol3e-9 returned Required step size smaller than spacing for nominal exec, attempts at extremes hung; NOT a convergence confirmation', 'num_grid':len(main)}
(out/'solver_metrics_009.json').write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics,indent=2))

```

## APPENDIX — execute_baryon_root_009.py

```python
#!/usr/bin/env python3
"""Conditional nB-scale sign boundary in source-native rate model, not a physical eta_B bound."""
import json
from pathlib import Path
from scipy.optimize import brentq
from source_7d_clock_baryon_stress_009 import load,simulate,SPECIES
raw=load('/mnt/data/mech_s6_public_2x2_raw.zip','/mnt/data/mech_s6_paper_2x2_raw.zip')
d=raw['public_exec'].copy()
for k in ['Xn']+[f'n_{sp}_cm3' for sp in SPECIES]:d[k]=raw['public_exec'][k].to_numpy()
res={}
for rtol in (3e-8,):
  def delta(b):
    p=simulate(d,'exec','paper',rtol,'archive',baryon_scale=b)['X_target']
    u=simulate(d,'exec','public',rtol,'archive',baryon_scale=b)['X_target']
    return p-u
  root=brentq(delta,1.3,1.4,xtol=1e-6)
  res[str(rtol)]={'baryon_scale_root':root,'delta_at_root':delta(root),'bracket_delta_1p3':delta(1.3),'bracket_delta_1p4':delta(1.4)}
  print(rtol,res[str(rtol)],flush=True)
res['scope']='Common archived T and exact mass; synthetic b multiplies n_B(T) in hadron losses, NOT global baryon conservation or complete BBN.'
Path('/mnt/data/mech_s7_rotation_009/baryon_sign_root_009.json').write_text(json.dumps(res,indent=2))

```