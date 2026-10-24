#!/usr/bin/env python3
"""MECH-S7 ROT015, reproducible archive-level Wu-Xu PBH mass-cube invariant audit.
No Julia execution, no source-valid hadron extrapolation, no physical BBN claim.

Usage:
  python reproduce_mass_cube_secant_audit_015.py \
    --public /mnt/data/mech_s6_public_2x2_raw.zip \
    --paper /mnt/data/mech_s6_paper_2x2_raw.zip \
    --out /mnt/data/mech_s7_rotation_015
"""
import argparse, csv, hashlib, io, json, zipfile
from decimal import Decimal, getcontext
from pathlib import Path
import numpy as np
import pandas as pd

getcontext().prec=65
GAMMA=4.207579833788249e27  # g**3 / s, fixed Wu-Xu source plateau, ROT004
M_INITIAL=6e9
M_EDGE=1e9
EXPECTED_ZIPS={
 'public':'75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5',
 'paper':'3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e'}
LOOKUPS={
 'public_exec':('public','trajectory_current.csv'),
 'public_sym':('public','trajectory_repaired.csv'),
 'paper_exec':('paper','trajectory_paper_exec.csv'),
 'paper_sym':('paper','trajectory_paper_sym.csv'),
}


def load_zipped(archive, filename):
    with zipfile.ZipFile(archive) as z:
        candidates=[n for n in z.namelist() if n.split('/')[-1]==filename]
        assert len(candidates)==1,(archive,filename,candidates)
        return pd.read_csv(io.BytesIO(z.read(candidates[0])))


def num_float_vs_decimal(df, j):
    # Independent high precision check of BOTH mass cube secant and time-lag.
    # Source values are CSV decimal strings; Float64 CSV serialization is the data carrier.
    a=df.iloc[j-1];b=df.iloc[j]
    ma=Decimal(str(a.m_PBH_g));mb=Decimal(str(b.m_PBH_g))
    ta=Decimal(str(a.t_sec));tb=Decimal(str(b.t_sec))
    gd=Decimal(str(GAMMA));md=Decimal(str(M_INITIAL))
    ratio=((ma**3-mb**3)/(tb-ta))/gd
    lag=(mb**3-md**3)/gd+tb
    return float(ratio),float(lag)


def safe_csv(path,rows):
    assert rows
    with open(path,'w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--public',required=True)
    ap.add_argument('--paper',required=True);ap.add_argument('--out',required=True)
    opts=ap.parse_args();out=Path(opts.out);out.mkdir(exist_ok=True,parents=True)
    zips={'public':Path(opts.public),'paper':Path(opts.paper)}
    sha={k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in zips.items()}
    assert sha==EXPECTED_ZIPS, {'found':sha,'expected':EXPECTED_ZIPS}
    frames={}
    rows=[];heads=[];thresholds=[];controls=[];lasts=[]
    for branch,(z,file) in LOOKUPS.items():
        df=load_zipped(zips[z],file)
        assert df.shape[0]==1600 and np.all(df['i'].to_numpy()==np.arange(1,1601))
        act=df[df.source_active==1].copy()
        assert act.shape[0]==1470 and np.all(act.below_1e9g==0)
        frames[branch]=act
        t=act.t_sec.to_numpy(np.float64);m=act.m_PBH_g.to_numpy(np.float64)
        assert np.all(np.diff(t)>0),branch
        assert np.all(np.diff(m)<0) or np.all(np.diff(m)<=0),branch
        exact=np.cbrt(M_INITIAL**3-GAMMA*(t-t[0]))
        lag=(m**3-M_INITIAL**3)/GAMMA+(t-t[0]);masserr=m/exact-1.0
        # stable factorization avoids catastrophic subtraction of adjacent cubes
        dm=m[:-1]-m[1:];dsec=t[1:]-t[:-1]
        gstep=dm*(m[:-1]**2 + m[:-1]*m[1:]+m[1:]**2)/(dsec*GAMMA)
        eps_step=gstep-1.0
        for j in range(len(act)):
            rows.append({'branch':branch,'iloc':j,'csv_i':j+1,'t_sec':repr(t[j]),
                         'm_arch_g':repr(m[j]),'m_exact_g':repr(exact[j]),
                         'mass_relative_error':repr(masserr[j]),
                         'mass_cube_clock_residual_sec':repr(lag[j]),
                         'step_gamma_over_source':repr(gstep[j-1]) if j else '',
                         'step_gamma_rel_error':repr(eps_step[j-1]) if j else '',
                         'source_active':1})
        last=lasts.append({'branch':branch,'last_csv_i':1470,
                  'last_t_sec':t[-1], 'last_M_arch_g':m[-1],
                  'last_M_exact_g':exact[-1], 'last_mass_error_pct':100*masserr[-1],
                  'last_mass_cube_time_defect_sec':lag[-1],
                  'max_abs_mass_rel_error_active':np.max(np.abs(masserr)),
                  'max_abs_time_lag_active_sec':np.max(np.abs(lag))})
        for label,j in [('i1401',1400),('i1441',1440),('i1451',1450),('i1461',1460),
                        ('i1466',1465),('i1467',1466),('i1468',1467),('i1469',1468),('i1470',1469)]:
            gd,ld=num_float_vs_decimal(act,j)
            controls.append({'branch':branch,'label':label,'csv_i':j+1,
                't_sec':t[j], 'm_arch_g':m[j], 'm_exact_g':exact[j],
                'mass_rel_error_pct':100*masserr[j],
                'clock_defect_sec':lag[j],
                'gamma_ratio_secant':gstep[j-1],
                'gamma_ratio_decimal':gd,
                'clock_defect_decimal':ld,
                'gamma_ratio_decimal_minus_float':gd-gstep[j-1],
                'clock_defect_decimal_minus_float':ld-lag[j]})
        for thr in [1e-5,1e-4,1e-3,5e-3,1e-2,2e-2]:
            ix=np.flatnonzero(np.abs(masserr)>=thr)
            j=int(ix[0]) if len(ix)>0 else None
            thresholds.append({'branch':branch,'mass_rel_error_threshold':thr,'first_csv_i':j+1 if j is not None else '',
                               't_sec':t[j] if j is not None else '',
                               'm_g':m[j] if j is not None else ''})
        # local slope summary from 1s onward, avoids tiny t increments
        loc=np.flatnonzero(t[1:]>1)
        heads.append({'branch':branch,'n_active':len(t),
            'gamma_step_min_tgt1':float(np.min(gstep[loc])),
            'gamma_step_max_tgt1':float(np.max(gstep[loc])),
            'gamma_step_median_tgt1':float(np.median(gstep[loc])),
            'max_abs_step_ratio_error_tgt1':float(np.max(np.abs(gstep[loc]-1))),
            'min_clock_defect_at_tgt1':float(np.min(lag[t>1])),
            'max_clock_defect_at_tgt1':float(np.max(lag[t>1])),
            'clock_defect_last_minus_penultimate':float(lag[-1]-lag[-2]),
            'clock_defect_penultimate_minus_antepenultimate':float(lag[-2]-lag[-3]),
            'max_abs_step_ratio_decimal_diff_samples':float(max(abs(z['gamma_ratio_decimal_minus_float']) for z in controls if z['branch']==branch))})
    # Exact trajectory equality from different SOURCE SPECTRAL laws ABOVE first table row
    for var in ['exec','sym']:
        p=frames[f'public_{var}'];q=frames[f'paper_{var}']
        for c in ['a','t_sec','T_GeV','m_PBH_g','Xn','n_pi_minus_cm3','n_pi_plus_cm3','n_K_minus_cm3','n_K0L_cm3','n_pbar_cm3','n_nbar_cm3']:
            equal=np.array_equal(p[c].to_numpy(),q[c].to_numpy())
            assert equal,(var,c)
    # Yet MAP changes the archived background/clock despite EXACT map-independent mass law at common t
    by_branch={x['branch']:x for x in lasts}
    exec_d=by_branch['public_exec']['last_mass_cube_time_defect_sec'];sym_d=by_branch['public_sym']['last_mass_cube_time_defect_sec']
    map_lag_difference=exec_d-sym_d
    def byindex(branch,j,which):
        for v in controls:
            if v['branch']==branch and v['csv_i']==j:return v[which]
        raise KeyError((branch,j,which))
    map_lag_difference_pre=byindex('public_exec',1469,'clock_defect_sec')-byindex('public_sym',1469,'clock_defect_sec')
    save={'date':'2026-10-24','cell':'Mech-S7','rotation':'015',
      'source_pin':'d395183674cace6c9906a8911bdeb7234ba4040d',
      'gamma_g3_per_s':GAMMA,'M_initial_g':M_INITIAL,'T_BH_plateau_source':'PDG2024 constant extrapolation above table, original Julia N_rho(T_BH)',
      'source_input_zip_sha256':sha,
      'four_last_active_rows':lasts,'per_branch_secant_summary':heads,
      'map_clock_defect_last_diff_sec':map_lag_difference,
      'map_clock_defect_pre_last_diff_sec':map_lag_difference_pre,
      'source_law_branch_equality_all_active_rows':True,
      'control_disclaimer':'Secant error of saved interpolated output, NOT accepted solver-step error or certified physical X/Yp endpoint error',
      'NO_CANON':True,'NO_EXEC_SIGN':True,'NO_SOURCE_VALID_E2B':True,'NO_PBH_BOUND':True}
    safe_csv(out/'all_source_active_mass_clock_015.csv',rows)
    safe_csv(out/'selected_secants_decimal_controls_015.csv',controls)
    safe_csv(out/'threshold_crossings_015.csv',thresholds)
    safe_csv(out/'secant_branch_summary_015.csv',heads)
    (out/'result_015.json').write_text(json.dumps(save,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    print(json.dumps({'lasts':lasts,'heads':heads,'map_lag_diff_last':map_lag_difference,
                     'map_lag_diff_pre_last':map_lag_difference_pre,
                     'selected':controls[-9:]},indent=2))

if __name__=='__main__': main()