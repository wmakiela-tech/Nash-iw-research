#!/usr/bin/env python3
"""DAX-S7 R61: source-typed, falsifiable PBH-injection continuity audit.

USAGE (requires historical rotation 59 CSV in the same directory):
  python IW_DAX_S7_ROTATION_61_PBH_INJECTION_CONTINUITY_20261026.py
  python IW_DAX_S7_ROTATION_61_PBH_INJECTION_CONTINUITY_20261026.py --selftest
  python IW_DAX_S7_ROTATION_61_PBH_INJECTION_CONTINUITY_20261026.py --source-dir /path/to/arXiv-2509.05618/data --background

First stage performs a real, runnable independent Fermi-Dirac EOS computation
using 13 source-table snapshots from rotation 59 and compares them with the
existing R60 table. All relevant input Git blob hashes are verified. For
--background provide the three ORIGINAL input files, with their expected Git
blob SHAs. In that mode reconstruct full radiation/PBH background with two
conditional closures: 'code' and 'paper-entropy baseline + same PBH injection'.
The second closure is a falsification tool, NOT a physical two-temperature
Hawking deposition solution. NO original Julia solver is invoked.

DO NOT claim a physical bound, publication correction, or a real PBH discovery.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parent
DATE='2026-10-26'
TNUC=0.07818527068831995
QNEUT=939.5654205-938.27208816
PI=math.pi
INPUT_59='IW_DAX_S7_ROTATION_59_PAPER_CODE_NEUTRINO_ENTROPY_COMPARISON_20261026.csv'
INPUT_60='IW_DAX_S7_ROTATION_60_FERMI_EOS_CONTINUITY_20261026.csv'
SOURCES={
 'ext/N_around_m_e.csv':'93f2494f026c5d0587ea40fe08bb938dd9d01fa8',
 'ext/N_s_from_PDG2024.csv':'33aceb876fc36cb2486d36c690e6401d85d76b46',
 'ext/N_rho_OVER_N_s_from_PDG2024.csv':'28b0c13563d7b3bdeaee191a3a981197345d05b8',
}
INPUT_BLOBS={
 INPUT_59:'a1934e09b02d797a7b759510da99b10e1facfa97',
 INPUT_60:'37e9220244840d7a2d122db38115ab6d54a60419',
}


def git_blob(raw:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def verify(path,expected):
    got=git_blob(path.read_bytes())
    if got!=expected: raise AssertionError(f'Git blob SHA mismatch: {path}: {got} != {expected}')


def electron_eos(T):
    """Independent ideal electron+positron energy and pressure from Fermi integrals."""
    y=0.51099895/T
    def n(x):
        E=math.hypot(x,y)
        return 0. if E>700 else 1/(math.exp(E)+1)
    I_rho=quad(lambda x:x*x*math.hypot(x,y)*n(x),0,100,epsabs=3e-13,epsrel=3e-13)[0]
    I_p=quad(lambda x:x**4/math.hypot(x,y)*n(x),0,100,epsabs=3e-13,epsrel=3e-13)[0]
    gr=60/PI**4*I_rho
    gp=20/PI**4*I_p
    gs=45/PI**4*(I_rho+I_p/3)
    return gr,gp,gs


def thermodynamic_sample(entry):
    T=float(entry['T_MeV'])
    gr=float(entry['g_rho']);gs=float(entry['g_s'])
    r=float(entry['r']);s=float(entry['s'])
    eg,ep,es=electron_eos(T)
    q4=(gr-2-eg)/5.25
    q3=(gs-2-es)/5.25
    assert q4>0 and q3>0
    qE=q4**.25
    qS=q3**(1/3)
    gp=(2+5.25*qE**4)/3+ep
    Ccode=-4+r/(3+s)
    Cpaper=-3*(4+r)/(3+s)
    Ceos=-3*(1+gp/gr)
    residue=Ccode-Ceos
    return {
        'T_MeV':T,'g_rho':gr,'g_s':gs,'r':r,'s':s,
        'Tnu_over_Tgamma_from_energy':qE,'Tnu_over_Tgamma_from_entropy':qS,
        'C_code':Ccode,'C_paper':Cpaper,'C_EOS':Ceos,
        'R_E_at_equal_injection':residue,
        'R_E_paper':Cpaper-Ceos,
        'I_threshold_source':-Ccode,
        'I_threshold_EOS':-Ceos,
        'I_threshold_paper':-Cpaper,
        'false_reheating_window_width':max(0,(-Ceos)-(-Ccode)),
        'local_window_relative_to_EOS':max(0,(Ccode-Ceos)/(-Ceos)),
    }


def write_csv(path,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)


def fixed_temperature_injection_cases(base):
    """All dimensions: I = (-Mdot*nPBH)/(H*rho); C=dlnrho/dlna.
    If a fraction f of the nominal source actually heats the tracked bath,
    R = Ccode - CEOS + (1-f)I. This is a bookkeeping experiment only.
    """
    levels=[0.,.01,.1,.5,1.,2.,3.5,3.75,3.8,3.85,3.87,3.9,3.93,3.95,3.965,4.,4.25,5.]
    Ccode,Ceos,r=base['C_code'],base['C_EOS'],base['r']
    rows=[]
    for I in levels:
        srcd=(Ccode+I)/(4+r)
        eosd=(Ceos+I)/(4+r)
        for f in (0.,.5,1.):
            residual=Ccode-Ceos+(1-f)*I
            rows.append({'T_MeV':TNUC,'I_PBH_total':I,'fraction_received_by_tracked_EOS':f,
            'C_source_plus_I':Ccode+I,'C_EOS_plus_fI':Ceos+f*I,
            'energy_residual_over_Hrho':residual,
            'dlnT_dlna_source_nominal':srcd,
            'dlnT_dlna_EOS_all_heated':eosd,
            'source_heating':srcd>0,'EOS_all_heated_heating':eosd>0,
            'opposite_temperature_sign_equal_injection':(srcd*eosd<0)})
    return rows


def lninterp(table,T,j=1):
    keys=table[:,0]
    ix=int(np.searchsorted(keys,T,side='right'))-1
    if ix<0:return float(table[0,j]),0.
    if ix>=len(keys)-1:return float(table[-1,j]),0.
    s=(table[ix+1,j]-table[ix,j])/math.log(keys[ix+1]/keys[ix])
    return float(table[ix,j]+s*math.log(T/keys[ix])),float(s)


class SourceThermo:
    def __init__(self,folder):
        for p,expected in SOURCES.items():verify(folder/p,expected)
        self.low=np.loadtxt(folder/'ext/N_around_m_e.csv',delimiter=',')
        self.high=np.loadtxt(folder/'ext/N_s_from_PDG2024.csv',delimiter=',')
        self.ratio=np.loadtxt(folder/'ext/N_rho_OVER_N_s_from_PDG2024.csv',delimiter=',')
        self.G=float(self.high[-1,1]*self.ratio[-1,1])
        self.Nbh=27*self.G/(4*30720*PI)
        grid=np.geomspace(.01,1.e6,1000)
        self.logT=np.log(grid)
        self.logrho=np.log(np.array([self.g(float(T))[0]*T**4 for T in grid]))
        assert np.all(np.diff(self.logrho)>0)

    def g(self,T):
        if T<=10:
            a,da=lninterp(self.low,T,1)
            b,db=lninterp(self.low,T,2)
            return a,da/a,db/b
        b,db=lninterp(self.high,T,1)
        c,dc=lninterp(self.ratio,T,1)
        return b*c,db/b+dc/c,db/b

    def T_of_L(self,L):
        k=max(0,min(len(self.logrho)-2,int(np.searchsorted(self.logrho,L,side='right'))-1))
        f=(L-self.logrho[k])/(self.logrho[k+1]-self.logrho[k])
        return math.exp(self.logT[k]+f*(self.logT[k+1]-self.logT[k]))


class Background:
    def __init__(self,table,mass,beta,closure):
        self.tb=table;self.mass=mass;self.beta=beta;self.closure=closure
        self.tf=mass/2.176434e-5*5.391247e-44/(1/(3*math.sqrt(3)))
        self.tau=(mass/2.176434e-5)**3*5.391247e-44/(3*table.Nbh)
        self.Tf=math.sqrt(1/(2*self.tf*.20658852676118475*math.sqrt(table.G)))
        self.Lf=math.log(table.G)+4*math.log(self.Tf)

    def properties(self,L,A,y):
        T=self.tb.T_of_L(L)
        gr,r,s=self.tb.g(T)
        B=self.beta*math.exp(self.Lf-L-3*A)
        H=.20658852676118475*math.exp(L/2)*math.sqrt(1+B*y)
        C=(-4+r/(3+s)) if self.closure=='code' else (-3*(4+r)/(3+s))
        return T,H,B,C

    @staticmethod
    def RK4(x,h,L,A,fn):
        p=fn(x,L,A)
        q=fn(x+h/2,L+h*p[0]/2,A+h*p[1]/2)
        r=fn(x+h/2,L+h*q[0]/2,A+h*q[1]/2)
        s=fn(x+h,L+h*r[0],A+h*r[1])
        return (L+h*(p[0]+2*q[0]+2*r[0]+s[0])/6,
                A+h*(p[1]+2*q[1]+2*r[1]+s[1])/6)

    def run(self,nx=5500,ny=8500,npost=1800,post_duration=.15,late_horizon_s=12.):
        L,A=self.Lf,0.
        prevT=self.Tf;prevTime=self.tf
        crossings=[]
        def record(nL,nA,t,stage):
            nonlocal L,A,prevT,prevTime
            temp=self.tb.T_of_L(nL)
            if (prevT-TNUC)*(temp-TNUC)<0:
                w=(TNUC-prevT)/(temp-prevT)
                crossings.append({'time_s':prevTime+w*(t-prevTime),'stage':stage,
                                  'direction':'heating' if temp>prevT else 'cooling'})
            prevT=temp;prevTime=t;L=nL;A=nA
        xmax=math.log((self.tf+.875*self.tau)/self.tf)
        hx=xmax/nx
        for i in range(nx):
            x=i*hx
            def f(z,l,a):
                t=self.tf*math.exp(z)
                y=max(1e-15,1-(t-self.tf)/self.tau)**(1/3)
                _,H,B,C=self.properties(l,a,y)
                return t*(H*C+B/(3*self.tau*y*y)),t*H
            pair=self.RK4(x,hx,L,A,f)
            record(*pair,self.tf*math.exp(x+hx),'before-evap')
        hy=-.5/ny
        for i in range(ny):
            y=.5+i*hy;yn=y+hy
            def f(y,l,a):
                _,H,B,C=self.properties(l,a,y)
                return -3*self.tau*y*y*H*C-B,-3*self.tau*y*y*H
            pair=self.RK4(y,hy,L,A,f)
            record(*pair,self.tf+self.tau*(1-yn**3),'evap')
        T_evap=self.tb.T_of_L(L)
        dt=post_duration/npost
        for i in range(npost):
            tt=self.tau+i*dt
            def f(t,l,a):
                _,H,B,C=self.properties(l,a,0.)
                return H*C,H
            pair=self.RK4(tt,dt,L,A,f)
            record(*pair,self.tau+(i+1)*dt,'after-evap')
            if len(crossings)>=3:break
        # Long-tail guard: for lighter masses the FIRST crossing can occur
        # multiple seconds after evaporation, well beyond the .15 s branch window.
        if not crossings:
            passed=post_duration
            while passed < late_horizon_s and not crossings:
                dt2=.02
                tt=self.tau+passed
                def f(t,l,a):
                    _,H,B,C=self.properties(l,a,0.)
                    return H*C,H
                pair=self.RK4(tt,dt2,L,A,f)
                record(*pair,tt+dt2,'after-evap-longtail')
                passed+=dt2
        return {'mass_g':self.mass,'beta':self.beta,'closure':self.closure,
                'nx':nx,'ny':ny,'t_evap_s':self.tau,'T_evap_MeV':T_evap,
                'n_crossings':len(crossings),'crossings':crossings}


def selftest():
    assert git_blob(b'test')=='30d74d258442c7c65512eafab474568dd706c430'
    assert abs(electron_eos(1.e6)[0]-3.5)<1e-11
    assert abs(electron_eos(.014)[0])<1e-10
    row={'T_MeV':TNUC,'g_rho':3.722254946361439,'g_s':4.242172521488243,
         'r':.44011773575892355,'s':.3590581309288281}
    a=thermodynamic_sample(row)
    assert abs(a['R_E_at_equal_injection']-.09638112)<2e-5
    assert abs(a['I_threshold_source']-3.86897585019)<2e-5
    for I in (0.,1.,3.9,4.1):
        assert abs((a['C_code']+I)-(a['C_EOS']+I)-a['R_E_at_equal_injection'])<1e-12
    print('SELFTEST PASS: Fermi EOS, source residual, exact injection cancellation')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input59',type=Path,default=ROOT/INPUT_59)
    parser.add_argument('--input60',type=Path,default=ROOT/INPUT_60)
    parser.add_argument('--output-dir',type=Path,default=ROOT)
    parser.add_argument('--selftest',action='store_true')
    parser.add_argument('--background',action='store_true')
    parser.add_argument('--source-dir',type=Path)
    parser.add_argument('--nx',type=int,default=5500)
    parser.add_argument('--ny',type=int,default=8500)
    opts=parser.parse_args()
    if opts.selftest:selftest()
    for name,path in ((INPUT_59,opts.input59),(INPUT_60,opts.input60)):
        verify(path,INPUT_BLOBS[name])
    with opts.input59.open(encoding='utf-8') as f:
        inputrows=list(csv.DictReader(f))
    with opts.input60.open(encoding='utf-8') as f:
        refrows=list(csv.DictReader(f))
    assert len(inputrows)==len(refrows)==13
    table=[thermodynamic_sample(e) for e in inputrows]
    for row,ref in zip(table,refrows):
        assert abs(row['T_MeV']-float(ref['T_MeV']))<1e-10
        assert abs(row['C_EOS']-float(ref['C_physical_EOS_dlnrho_dln_a']))<1e-11
        assert abs(row['R_E_at_equal_injection']-float(ref['energy_residual_source_over_Hrho']))<1e-11
    nuc=min(table,key=lambda item:abs(item['T_MeV']-TNUC))
    assert abs(nuc['T_MeV']-TNUC)<1e-10
    inj=fixed_temperature_injection_cases(nuc)
    # source and physical closures have opposite temperature signs for some I
    assert any(row['opposite_temperature_sign_equal_injection'] for row in inj)
    for row in inj:
        expected=nuc['R_E_at_equal_injection']+(1-row['fraction_received_by_tracked_EOS'])*row['I_PBH_total']
        assert abs(row['energy_residual_over_Hrho']-expected)<1e-12
    opts.output_dir.mkdir(parents=True,exist_ok=True)
    write_csv(opts.output_dir/'IW_DAX_S7_ROTATION_61_COOLING_HEATING_THRESHOLDS_20261026.csv',table)
    write_csv(opts.output_dir/'IW_DAX_S7_ROTATION_61_PBH_INJECTION_SWEEP_20261026.csv',inj)
    bg_results=[]
    if opts.background:
        if not opts.source_dir:raise ValueError('provide --source-dir containing the three original files')
        tables=SourceThermo(opts.source_dir)
        for mass in (9.6725e9,9.580552280e9):
            for mode in ('code','paper'):
                bg_results.append(Background(tables,mass,1e-17,mode).run(nx=opts.nx,ny=opts.ny))
        bgpath=opts.output_dir/'IW_DAX_S7_ROTATION_61_OPTIONAL_BACKGROUND_20261026.json'
        bgpath.write_text(json.dumps(bg_results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    branch_filename='IW_DAX_S7_ROTATION_61_SOURCE_TABLE_BRANCH_RETUNING_20261026.csv'
    branch_path=opts.output_dir/branch_filename
    if branch_path.is_file():
        with branch_path.open(encoding='utf-8') as stream:branch_rows=list(csv.DictReader(stream))
        assert len(branch_rows)==9
        assert sorted(set(int(z['number_of_T_nuc_crossings_in_checked_window']) for z in branch_rows))==[1,3]
    else: branch_rows=[]
    manifest={
      'rotation':'IW_DAX_S7_R61','date':DATE,
      'verdict':'PBH_INJECTION_CANCELLATION_EXACT_FOR_EQUAL_BOOKKEEPING / HEATING_THRESHOLD_DISAGREEMENT / NO_PHYSICAL_UPGRADE / NO_EXEC / NO_CANON',
      'provenance':{'source_main_scan_blob':'b368ba55d5a493f7bc185909730f7fe5691f10d6',
       'species_code_blob':'0437c032bdc4bafca6cb634c0db4cd2c46fb7efc',
       'original_source_table_blobs':SOURCES,'historic_verified_inputs':INPUT_BLOBS},
      'method':'13 source-table thermodynamic checkpoints; fully rerun electron Fermi-Dirac energy and pressure integrals; analytic identity; optional separate full source-table background port',
      'numbers':{'T_nuc_MeV':TNUC,'C_source':nuc['C_code'],'C_EOS':nuc['C_EOS'],
       'C_paper':nuc['C_paper'],'R_E_at_equal_injection':nuc['R_E_at_equal_injection'],
       'I_threshold_source':nuc['I_threshold_source'],'I_threshold_EOS':nuc['I_threshold_EOS'],
       'false_reheating_window_width':nuc['false_reheating_window_width'],
       'I_3p9_source_temperature_slope':next(x for x in inj if x['I_PBH_total']==3.9 and x['fraction_received_by_tracked_EOS']==1)['dlnT_dlna_source_nominal'],
       'I_3p9_EOS_temperature_slope':next(x for x in inj if x['I_PBH_total']==3.9 and x['fraction_received_by_tracked_EOS']==1)['dlnT_dlna_EOS_all_heated']},
      'background_optional_results':bg_results,
      'full_source_connector_background':{'matrix_filename':branch_filename,
       'rows':len(branch_rows),'method':'independent connector-side JavaScript port of the three source table CSVs, not locally re-executed Python --background',
       'converged_crossing_counts':{'code_M96725e5':3,'paper_M96725e5':1,'paper_M9580552280':3}},
      'limitations':['No complete Julia Wu-Xu execution','Not a physical two-sector neutrino/EM Hawking deposition model','f parameter is a diagnostic, not a measured branching fraction','No PBH exclusion or publication correction claim','Paper-entropy background with the same PBH source is a conditional stress test, not a complete physical model']}
    out=opts.output_dir/'IW_DAX_S7_ROTATION_61_SOURCE_TYPED_MANIFEST_20261026.json'
    out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'PASS':True,'T_nuc':nuc,'opposite_sign_cases':sum(r['opposite_temperature_sign_equal_injection'] and r['fraction_received_by_tracked_EOS']==1 for r in inj),'optional_background':bg_results},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
