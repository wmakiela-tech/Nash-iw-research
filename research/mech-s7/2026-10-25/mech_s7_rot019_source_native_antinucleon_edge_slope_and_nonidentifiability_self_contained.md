# Mech-S7 ROT019 — native Wu–Xu antinucleon spectral ratio at the lower table boundary

**DATE:** 2026-10-25 (Europe/Warsaw)  
**RETURN_ID:** `MECH-S7-FRONTB-NATIVE-ANTISPECTRAL-EDGE-SLOPE-GATE-019_20261025`  
**PROBLEM:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**CLASS:** SOURCE-PINNED EXACT EDGE FINITE DIFFERENCE / CONDITIONAL 7D SIGN-THRESHOLD COMPARISON / ANALYTIC POSITIVE C1 NONIDENTIFIABILITY WITNESS / NEGATIVE KNOWLEDGE  
**STATUS:** `SOURCE_EDGE_CALC_PASS / DECIMAL65_PASS / POSITIVE_CONTINUATION_WITNESS_PASS / NO_FRESH_DYNAMIC_7D_OR_JULIA_10D`.

## 1. Source fidelity, scope and prior-art subtraction

Source pinned to Wu–Xu, `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d`:

- `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, Git blob `06d0883a27b108692720422294ba2baacd381a64`, 100 tabulated masses from `5.609588603804452e32 GeV` (~1e9 gram) upwards. This rotation faithfully embeds **the first 12 rows of mass, proton and neutron** as a partial, explicitly labeled extract; all source-edge numerical claims below derive from those exact text entries.
- `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl`: source code applies log(rate)-versus-log(mass) `LinearInterpolation` with `ExtrapolationType.Linear` separately to protons and neutrons. Therefore immediately below the smallest tabulated mass it carries the *first-cell* species slopes (the source implementation, not a particle-physics proof).
- `arXiv-2509.05618/main-scan.jl`: the two source rates feed the pbar and nbar abundance equations. Source semantics: `proton_from_PBH` / `neutron_from_PBH` become **antiproton/antineutron populations** in the kinetic system.
- **Others first:** MECH ROT004 derived the **constant** `N_BH(T_BH)` plateau and exact mass cube from the pinned `N_s_from_PDG2024` + `N_rho_OVER_N_s` upper table extrapolations, `Γ=4.207579833788249e27 g³/s`; this is **not a new ROT019 finding**. MECH ROT007 first found tiny anti-spectral sign-kill roots in a transplanted 7D edge state; MECH ROT013 repaired the missing pre-edge state transport and **superseded** those numeric thresholds; we use the revised ROT013 `χ_EM=0.5, η_B const` root `ε_exec=9.7439681491e−5` and `ε_sym=−1.3709072411e−4`, **without re-running that 7D ODE**. DAX-S7/PRF11 EOS currentness, REC10 postsource memory, MT13/NC/LT5 time-weighted target identifiability remain earlier, different scientific contributions.

## 2. Source-native first-cell anti-ratio slope

Let `R(M)=Q_proton(M)/Q_neutron(M)`. The pinned first two source rows are:

| `M` in GeV | `Q_proton` | `Q_neutron` |
|---:|---:|---:|
| 5.609588603804452e32 | 34849.08026691193 | 34656.17773724596 |
| 6.099798045788406e32 | 31504.591028094237 | 31328.963561830213 |

At the edge, `R0=1.0055661801808757`. The exact first-cell secant in log coordinates is

```
alpha_p  = ln(Qp1/Qp0) / ln(M1/M0) = −1.20429142853845866...
alpha_n  = ln(Qn1/Qn0) / ln(M1/M0) = −1.20476306398303284...
S_native = alpha_p−alpha_n            = +0.00047163544457418033960...
```

An independent Decimal calculation at **65 digits** verifies `S_native` to Float64 difference `6.28e−16` with a second independent identity `ln(R1/R0)/ln(M1/M0)`. The original Julia extrapolation extends `R(M)/R0=(M/M0)^S_native` for `M<M0`; this is a statement about what the pinned *code* does below the tabulated domain.

The log-ratio slopes from source-window least-squares fits using 2,3,4,5,8,12 first entries are, respectively: `0.000471635444575`, `0.000461876680916`, `0.000456757712553`, `0.000461526503420`, `0.000512993988106`, `0.000579228554462`. **All** lie above the ROT013 conditional `B_exec` threshold described below. Window dependence and large mass evolution show that no exact constant physical exponent should be inferred from the table beyond the first interpolation cell.

## 3. Properly typed comparison to ROT013 antispectral root

ROT013's hypothetical `paper` source family uses `α_p=−1.3+ε, α_n=−1.3−ε`, so its source *ratio* exponent is `S=2ε`, while the geometric-mean source rate follows the unperturbed paper exponent `−1.3`.

- `B_exec` numerical root (in the executed ROT013 conditional bridge+7D, `χ_EM=0.5, η_B const`): `ε*=+9.7439681491e−5`, hence `S_crit=+1.94879362982e−4`. Exact pinned table `S_native/S_crit=2.4201405`.
- `B_sym` numerical root: `ε*=−1.3709072411e−4`, hence `S_crit,sym=−2.7418144822e−4`; the native source slope is **positive**. Comparing only absolute values would be misleading: the two signed directions are opposite and this observation does NOT trigger the sym root.
- At `M=1e8g` (`u=M/M0=.1`), native *public* source ratio would be `R_native=1.0044747474171243`, i.e. **−0.108539128%** from the edge. The `B_exec` paper-family sign-kill **threshold** represents −0.044862565% in source ratio at that mass. This is a **comparison of counterfactual source families**, not a performed calculation of the paper+native-skew 7D endpoint.
- The original public source has very different **mean slopes** (`alpha_p≈−1.20429`, `alpha_n≈−1.20476`) from the common paper family (`−1.3`); one may NOT conclude that plugging `S_native` into the paper family produces the actual public or physical endpoint. The executed `B_exec` sign-root is an existing *model sensitivity*, not an uncertainty measured on `Qp/Qn`.

### Source-only analytic subtraction

At constant exact Gamma (already ROT004), with `Q_i=Q_i0 u^{alpha_i}` and the source-on terminal cutoff `u_cut~1.23669e−8`, the **emitted particle count ratio** over subedge is:

```
Np/Nn = R0 * [ (1-u_cut^(3+alpha_p))/(3+alpha_p) ] /
             [ (1-u_cut^(3+alpha_n))/(3+alpha_n) ].
```

For pinned code exponents this gives `1.005302072374088`; for paper common exponent −1.3 it is exactly `R0=1.005566180180876`. Relative difference: `−0.0262645873%`. It is **not** the propagated population ratio, not the signed hadronic conversion impulse, and not the final neutron fraction. MECH ROT005 and MT13/NC target sufficiency prohibit replacing those objects by total emitted counts.

## 4. Source-edge derivative still does not identify subedge spectrum (exact constructive negative witness)

For any `λ>0`, define for `u≤1`:

```
R_lambda(u) = R0 * exp[S_native * λ * tanh(ln(u)/λ)]
```

and above the edge simply retain the original table interpolation. This **positive** function obeys `R_lambda(1)=R0` and `d ln R_lambda/d ln u|_{u=1}=S_native`, matching the exact source-table ratio value **and derivative** at the boundary. The log-ratio also matches the first-cell **second derivative** (zero) at the boundary because `tanh''(0)=0`.

Two exact legal mathematical continuations (not proposed actual source theories):

1. `R_power(u)=R0*u^S_native` (original public software extrapolation).
2. `R_0.05(u)` from the saturating formula, matching the same edge ratio and first derivative.

At `u=0.1`, the first changes relative to `R0` by `−0.108539128%`, the second by only `−0.0023581494%`, **~46× smaller**, despite identical local first derivatives and continuity. Both can be implemented by positive p/n rates with a common arbitrarily specified positive geometric mean. Thus the *edge ratio plus even its first two local derivatives without global regularity bounds* are insufficient to determine the subedge ratio and hence cannot guarantee a 7D sign. More generally, adding `A*exp(-1/(ln u)^2)` to `ln R` for `u<1`, with value zero at `u=1`, changes the subedge ratio while matching **every** derivative at the boundary; this is the standard smooth flat-function nonidentifiability witness. This is a standard function-extension counterexample, not a new theorem or a sign-flip ODE experiment.

## 5. Decision, future falsifier, claim ceiling

**Material owner implication:** validating only the p/n source ratio at `M=1e9g`, or even its one-sided derivative, does **not** settle the critical source-shape gate. A source-admitted below-edge **mass-resolved** proton/neutron ratio and its covariance with total hadron power are needed to interpret the conditional sign. The original accepted-step 10D Julia event and source/kinetic history, micro EOS and time-target typing remain prerequisites. No new cascade of cell tasks: route to existing Front B scientific owners and existing BW intake.

**Observed controls:** 12 source rows pinned; 6 regression windows PASS; signed sym-root guard PASS; 35 positive continuation examples; 65-digit Decimal control PASS; analytic source-only fluence subtraction PASS; local numeric evaluations and source archive readback PASS. **Not executed:** fresh integrated 7D for perturbed continuations; original 10D Julia; any particle-physics validation below `1e9g`; any physical helium/deuterium/BBN bounds.

**STOP/guard:** `SOURCE_EDGE_SLOPE_VERIFIED / CONDITIONAL_MODEL_SIGN_THRESHOLD_COMPARED / EDGE_TO_SUBEDGE_IDENTIFIABILITY_FAIL / NO_SOURCE_VALID_E2B / NO_JULIA_10D / NO_MODERN_Yp_DH / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / BW_INGEST_UNKNOWN`.


---

## APPENDIX A — COMPLETE EXECUTED PRIMARY REPRODUCER

```python
#!/usr/bin/env python3
"""Mech-S7 ROT019 — exact pinned source-table antinucleon ratio derivative.
Pure Python/stdlib. First 12 source rows copied from
Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d
arXiv-2509.05618/data/out/hadrons_from_PBH.dat (blob 06d0883a27b108692720422294ba2baacd381a64).
This is a *partial extract*, not a replacement for the upstream source file.
This script does NOT integrate full original Julia 10D or claim source-valid subedge physics.
"""
import csv, json, math, hashlib
from pathlib import Path

ROWS = '''5.609588603804452e32 34849.08026691193 34656.17773724596
6.099798045788406e32 31504.591028094237 31328.963561830213
6.632845798026921e32 28387.973269731203 28228.650640502765
7.212475404948756e32 25521.031717558253 25376.846686105455
7.842757550984395e32 22914.14992967101 22783.765726686597
8.528118648601441e32 20557.039300656503 20439.153412336287
9.273371924584742e32 18435.545939209584 18328.895469639596
1.008375122287719e33 16528.826829228834 16432.30301047628
1.0964947761375425e33 14817.06284452867 14729.692480456592
1.1923150100819998e33 13281.613213630904 13202.542287707794
1.2965087606477704e33 11903.9851614509 11832.467514437843
1.4098077707843446e33 10668.546806711036 10603.888797031783'''
DATA = [tuple(map(float,row.split())) for row in ROWS.strip().splitlines()]
SOURCE_COMMIT='d395183674cace6c9906a8911bdeb7234ba4040d'
SOURCE_BLOB='06d0883a27b108692720422294ba2baacd381a64'
# The source prior result from executed conditional 10-component pre-edge bridge (ROT013, chi_EM=0.5, eta fixed).
ROOT_EXEC=9.7439681491e-5
ROOT_SYM=-1.3709072411e-4


def lin_slope(x,y):
    xbar=sum(x)/len(x);ybar=sum(y)/len(y)
    return sum((a-xbar)*(b-ybar) for a,b in zip(x,y))/sum((a-xbar)**2 for a in x)


def ratio_continuation(u,slope,lam):
    """Positive C^2-in-log ratio branch at u=1; C^1-matches edge derivative.
    lam=None is exact power-law slope extension, lam>0 saturates below edge.
    """
    ell=math.log(u)
    return math.exp(slope*ell if lam is None else slope*lam*math.tanh(ell/lam))


def fluence_ratio(alpha_p,alpha_n,u=12.3669/1e9):
    """Pure source-only, conditional on common constant Gamma, NOT kinetic X."""
    numer=-math.expm1((3+alpha_p)*math.log(u))/(3+alpha_p)
    denom=-math.expm1((3+alpha_n)*math.log(u))/(3+alpha_n)
    return (DATA[0][1]/DATA[0][2])*numer/denom


def run(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    m0,p0,n0=DATA[0];m1,p1,n1=DATA[1];R0=p0/n0
    alpha_p=math.log(p1/p0)/math.log(m1/m0)
    alpha_n=math.log(n1/n0)/math.log(m1/m0)
    slope=alpha_p-alpha_n
    slope_ratio=math.log((p1/n1)/(p0/n0))/math.log(m1/m0)
    assert abs(slope-slope_ratio)<3e-14,(slope,slope_ratio)
    critical_exec=2*ROOT_EXEC;critical_sym=2*ROOT_SYM
    assert slope>critical_exec>0
    assert abs(slope)>abs(critical_sym)
    windows=[]
    for n in (2,3,4,5,8,12):
        first=DATA[:n]
        xx=[math.log(m/m0) for m,p,q in first]
        yy=[math.log(p/q) for m,p,q in first]
        fit=lin_slope(xx,yy)
        assert fit>critical_exec
        windows.append(dict(n_source_rows=n,log_ratio_slope=fit,
                            relative_to_exec_sign_threshold=fit/critical_exec,
                            max_mass_relative_to_edge=first[-1][0]/m0))
    rows=[]
    for u in (1.0,0.5,0.2,0.1,0.05,0.01,0.001):
        power=ratio_continuation(u,slope,None)
        crit=ratio_continuation(u,critical_exec,None)
        for lam in (None,0.02,0.05,0.20,1.0):
            r=ratio_continuation(u,slope,lam)
            rows.append(dict(mass_ratio_to_edge=u,continuation='power' if lam is None else f'saturation_lambda_{lam:g}',
                ratio_p_to_n=R0*r,ratio_over_edge=r,
                relative_ratio_change_pct=100*(r-1),
                exec_critical_ratio_over_edge=crit,
                exec_critical_change_pct=100*(crit-1)))
    assert abs(ratio_continuation(1.,slope,.05)-1.)<1e-15
    # Analytic derivative d lnR/d ln u at the table edge equals source slope in both families.
    h=1e-5
    for lam in (.02,.05,.2,1.,None):
        y1=math.log(ratio_continuation(math.exp(-h),slope,lam))
        y2=math.log(ratio_continuation(math.exp(h),slope,lam))
        slope_finite=(y2-y1)/(2*h)
        assert abs(slope_finite-slope)<8e-10,(lam,slope_finite,slope)
    flux_public=fluence_ratio(alpha_p,alpha_n)
    flux_paper=fluence_ratio(-1.3,-1.3)
    assert abs(flux_paper-R0)<1e-12
    # Source-only integrated Qp/Qn under a fixed Hawking mass-cube rate: this is not an X response.
    summary={
     'return_id':'MECH-S7-FRONTB-NATIVE-ANTISPECTRAL-EDGE-SLOPE-GATE-019_20261025',
     'source_commit':SOURCE_COMMIT,'source_blob':SOURCE_BLOB,'partial_source_rows':len(DATA),
     'upstream_relative_proton_neutron_table':{'mass_anchor_in_GeV':m0,
       'Qp_anchor_source_GeV':p0,'Qn_anchor_source_GeV':n0,'R0':R0,
       'mass_second_in_GeV':m1,'R1':p1/n1,
       'alpha_p_public_first_cell':alpha_p,'alpha_n_public_first_cell':alpha_n,
       'log_slope_alpha_p_minus_alpha_n':slope,'log_slope_ratio_independent':slope_ratio},
     'conditional_rot013_sign_kill_roots_chi05_fixedeta':{'epsilon_exec':ROOT_EXEC,'delta_alpha_exec':critical_exec,
        'epsilon_sym':ROOT_SYM,'delta_alpha_sym':critical_sym,
        'native_slope_over_abs_exec_root':slope/abs(critical_exec),
        'native_slope_over_abs_sym_root':slope/abs(critical_sym)},
     'window_fits':windows,
     'native_public_pn_source_fluence_ratio_conditional':flux_public,
     'paper_common_slope_pn_source_fluence_ratio_conditional':flux_paper,
     'native_vs_paper_fluence_ratio_relative_pct':100*(flux_public/flux_paper-1),
     'minimal_positive_C1_continuation_witness':{'formula':'R_lambda(u)/R0=exp[slope*lambda*tanh(ln(u)/lambda)]',
      'edge_R0_and_derivative_matched':True,'sufficient_to_determine_subedge_ratio':False},
     'claim_ceiling':['source_table_log_ratio_derivative', 'original pinned code interpolation',
         'comparison_to_previously_executed_conditional_7D_root_only',
         'analytic positive C1 nonidentifiability witness'],
     'not_claimed':['physically validated hadron spectrum below 1e9g','original Julia 10D executed',
       'physical sign flip','helium and deuterium predictions','PBH bound','theorem novelty','EXEC acceptance']}
    for name,items in [('window_regression_019.csv',windows),('source_continuation_witness_019.csv',rows)]:
        with (out/name).open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(items[0]));writer.writeheader();writer.writerows(items)
    (out/'native_edge_source_summary_019.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({'native_edge_ratio_slope':slope,'exec_critical_2epsilon':critical_exec,
        'ratio_to_exec_gate':slope/critical_exec,'fits':windows,
        'fluence_ratio_public':flux_public,'fluence_ratio_paper':flux_paper,
        'native_vs_paper_fluence_pct':summary['native_vs_paper_fluence_ratio_relative_pct'],
        'ratio_1e8_public_power':R0*ratio_continuation(.1,slope,None),
        'ratio_1e8_saturated05':R0*ratio_continuation(.1,slope,.05)},indent=2))

if __name__=='__main__':
    run(Path(__file__).resolve().parent)

```

## APPENDIX B — COMPLETE EXECUTED INDEPENDENT DECIMAL65 REPRODUCER

```python
#!/usr/bin/env python3
"""Independent decimal 65-digit precision check of ROT019 ratio exponent."""
from decimal import Decimal,localcontext
from pathlib import Path
import importlib.util, json
main_path=Path(__file__).with_name('reproduce_native_antinucleon_ratio_gate_019.py')
spec=importlib.util.spec_from_file_location('rot019',main_path)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
# Read directly from embedded text to avoid Float64-rounding before high precision
with localcontext() as ctx:
    ctx.prec=65
    a,b=[list(map(Decimal,row.split())) for row in mod.ROWS.splitlines()[:2]]
    delta=((b[1]/b[2])/(a[1]/a[2])).ln()/(b[0]/a[0]).ln()
    pexp=(b[1]/a[1]).ln()/(b[0]/a[0]).ln()
    nexp=(b[2]/a[2]).ln()/(b[0]/a[0]).ln()
    assert abs((pexp-nexp)-delta)<Decimal('1e-61')
    import math
    mp0,pp0,np0=mod.DATA[0]
    mp1,pp1,np1=mod.DATA[1]
    source_float_slope=(math.log(pp1/pp0)-math.log(np1/np0))/math.log(mp1/mp0)
    diff=abs(float(delta)-source_float_slope)
    assert diff<1e-12
    report={'precision_digits':65,'source_ratio_slope_decimal':str(delta),'source_proton_alpha_decimal':str(pexp),'source_neutron_alpha_decimal':str(nexp),'float64_vs_decimal_abs':diff}
    Path(__file__).with_name('decimal_check_019.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

```