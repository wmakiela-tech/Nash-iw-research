#!/usr/bin/env python3
"""Mech-S7 rotation003, frozen Wu-Xu channel decomposition from the saved 2x2 trajectories.
No Julia reexecution or source-valid low-mass interpolation claimed.
Inputs: Mech-S6 PUBLIC and PAPER original Actions ZIPs (SHA256 checked).
"""
from __future__ import annotations
import argparse,csv,hashlib,io,json
from pathlib import Path
from zipfile import ZipFile
import numpy as np
import pandas as pd

SHA_PUBLIC='75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5'
SHA_PAPER='3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e'
SPECIES=['pi_minus','pi_plus','K_minus','K0L','pbar','nbar']
NAMES=['n_'+s+'_cm3' for s in SPECIES]
ALPHA_EM=1/137.035999084
M_P=938.27208816


def unarchive(path, sha, labels):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha,'original ZIP SHA256 fail: '+str(path)
    with ZipFile(io.BytesIO(raw)) as z:
        return {lab:pd.read_csv(io.BytesIO(z.read('trajectory_'+name+'.csv')))
                for lab,name in labels}


def fc(T, mass):
    ve=np.sqrt(T/mass)+np.sqrt(T/M_P)
    x=2*np.pi*ALPHA_EM/ve
    return x/(-np.expm1(-x))


def decompose(df):
    T=df.T_GeV.to_numpy()*1000
    X=df.Xn.to_numpy()
    n=np.column_stack([df[col].to_numpy() for col in NAMES])
    fp=fc(T,139.57039)
    fk=fc(T,493.677)
    # Exact coefficient shape from Wu-Xu tool_script-parameters.jl (common factor 1 mbarn omitted).
    # A: p->n; B: n->p.  K0L survives charge-map split.
    cA=np.column_stack([1.5*fp,np.zeros_like(T),31*fk,7*np.ones_like(T),np.zeros_like(T),28*np.ones_like(T)])
    cB=np.column_stack([np.zeros_like(T),1.7*np.ones_like(T),26*np.ones_like(T),7*np.ones_like(T),28*np.ones_like(T),np.zeros_like(T)])
    a=cA*n; b=cB*n
    F=(1-X[:,None])*a-X[:,None]*b
    A=a.sum(axis=1);B=b.sum(axis=1)
    total=F.sum(axis=1)
    Acode=df.A_GeV.to_numpy();Bcode=df.B_GeV.to_numpy()
    valid=np.where((Acode>0)&(Bcode>0))[0]
    alphaA=A[valid]/Acode[valid]
    alphaB=B[valid]/Bcode[valid]
    assert np.all(np.isfinite(alphaA)) and np.all(np.isfinite(alphaB))
    assert np.nanmax(abs(alphaA/np.median(alphaA)-1))<3e-8, 'A channel reconstruction mismatch'
    assert np.nanmax(abs(alphaB/np.median(alphaB)-1))<3e-8, 'B channel reconstruction mismatch'
    assert abs(np.median(alphaA)/np.median(alphaB)-1)<3e-8, 'A/B conversion ratio mismatch'
    kappa=np.divide(np.abs(F).sum(axis=1),np.abs(total),out=np.full_like(total,np.nan),where=np.abs(total)>0)
    r=np.divide(A,A+B,out=np.full_like(A,np.nan),where=A+B>0)
    return dict(F=F,A=A,B=B,total=total,kappa=kappa,q=r,q_minus_X=r-X,
      unit_A=float(np.median(alphaA)),unit_B=float(np.median(alphaB)),X=X)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--public',type=Path,required=True)
    ap.add_argument('--paper',type=Path,required=True)
    ap.add_argument('--outdir',type=Path,required=True)
    args=ap.parse_args();args.outdir.mkdir(parents=True,exist_ok=True)
    ds={};ds.update(unarchive(args.public,SHA_PUBLIC,[('public_exec','current'),('public_sym','repaired')]))
    ds.update(unarchive(args.paper,SHA_PAPER,[('paper_exec','paper_exec'),('paper_sym','paper_sym')]))
    results={k:decompose(d) for k,d in ds.items()}
    allrows=[]
    for label,d in ds.items():
        res=results[label]
        for i in [1300,1400,1450,1460,1465,1468,1469]:
            parts=res['F'][i];F=res['total'][i]
            row=dict(branch=label,i=i,T_MeV=float(d.T_GeV[i]*1000),mass_g=float(d.m_PBH_g[i]),Xn=float(d.Xn[i]),
                     q=float(res['q'][i]),q_minus_X=float(res['q_minus_X'][i]),
                     A_over_B=float(res['A'][i]/res['B'][i]),kappa_cond=float(res['kappa'][i]),
                     net_F_native=float(d.F_had_GeV[i]),
                     signed_F_rel_1pct_nbar_change=float(.01*parts[5]/F),
                     signed_F_rel_1pct_pbar_change=float(.01*parts[4]/F),
                     total_relative_effect_pbar_plus1pct_nbar_minus1pct=float(.01*(parts[4]-parts[5])/F))
            row.update({f'signed_F_channel_fraction_{name}':float(parts[j]/F) for j,name in enumerate(SPECIES)})
            allrows.append(row)
    rows=pd.DataFrame(allrows)
    rows.to_csv(args.outdir/'channel_conditioning_selected_rows.csv',index=False,float_format='%.17g')
    summary={}
    for label,d in ds.items():
        r=results[label]
        m=(d.source_active.to_numpy()==1)
        sel=np.flatnonzero(m&(d.m_PBH_g.to_numpy()<5e9))
        i=1469
        summary[label]={
           'A_B_unit_ratio_match':r['unit_A']/r['unit_B'],
           'samples_active':int(m.sum()),
           'max_mass_source_active_g':float(d.m_PBH_g[m].max()),
           'min_mass_source_active_g':float(d.m_PBH_g[m].min()),
           'last_source_active_index':int(np.flatnonzero(m)[-1]),
           'last_active_q':float(r['q'][i]),'last_active_Xn':float(r['X'][i]),
           'last_active_kappa':float(r['kappa'][i]),
           'last_active_kappa_l2_independent_fractional':float(np.linalg.norm(r['F'][i,:])/abs(r['total'][i])),
           'critical_iid_fractional_one_sigma_for_unit_RMS':float(abs(r['total'][i])/np.linalg.norm(r['F'][i,:])),
           'critical_anticorrelated_pbar_nbar_each_fractional':float(-r['total'][i]/(r['F'][i,4]-r['F'][i,5])),
           'critical_pbar_plus_fractional':float(-r['total'][i]/r['F'][i,4]),
           'critical_nbar_minus_fractional':float(r['total'][i]/r['F'][i,5]),
           'last_active_F':float(d.F_had_GeV[i]),
           'max_kappa_under5e9':float(np.nanmax(r['kappa'][sel])),
           'median_kappa_under5e9':float(np.nanmedian(r['kappa'][sel])),
           'fraction_F_positive_under5e9':float((r['total'][sel]>0).mean()),
           'signed_fractions_last_active':{sp:float(r['F'][i,j]/r['total'][i]) for j,sp in enumerate(SPECIES)},
           'effect_1pct_pbar_plus_nbar_minus_on_total':float(.01*(r['F'][i,4]-r['F'][i,5])/r['total'][i]),
           'effect_1pct_pbar_nbar_common_on_total':float(.01*(r['F'][i,4]+r['F'][i,5])/r['total'][i]),
           'effect_1pct_all_six_common_on_total':float(.01*r['F'][i,:].sum()/r['total'][i])
        }
    out={'status':'EXECUTED_ARCHIVED_TRAJECTORY_CHANNEL_DECOMPOSITION','date':'2026-10-23',
         'sha256':{'public_zip':SHA_PUBLIC,'paper_zip':SHA_PAPER},
         'source':'Fenyutanchan/Primordial-Black-Hole d395183674cace6c9906a8911bdeb7234ba4040d tool_script-parameters.jl',
         'rows':summary,'claim_ceiling':'instantaneous saved-point conditioning only; not source-valid subedge, solver convergence, physical bound, or independent causal mechanism'}
    (args.outdir/'channel_conditioning_summary.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
