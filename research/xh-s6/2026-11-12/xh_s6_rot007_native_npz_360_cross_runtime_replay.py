#!/usr/bin/env python3
"""XH-S6 ROT007: original NPZ/NumPy cross-runtime control for ROT006.

Pinned author Git repository/weights and pinned prior V8 outcome CSV source.
No author PsychRNN original Python replay, training, monkey data or source noise.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np

AUTHOR_COMMIT = '7889a81e298c01532a313e02971c11dbc9db8eb0'
ORIGINAL = {'MTbroadsharp_m10.npz': 'c5e701740f8ab1d19ca07415c0de2d6e7f88c37f',
            'DLPFCcombined_m4.npz': '47142e3dee920a759406136449f0b12f9ce752ee'}
REF_CSV = {'motion_dots': '88bd42f4ce793c823faf5bc8e804b466ce643624',
           'reward_ring': 'f8a4e12e7fd706112bbe273bd437675ec55ebc3a'}

def git_blob(raw:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()

def pin_bytes(path:Path, sha:str)->bytes:
    contents=path.read_bytes()
    got=git_blob(contents)
    if got!=sha: raise RuntimeError(f'SOURCE_IDENTITY_FAIL {path}: {got} expected {sha}')
    return contents

def model(path:Path, name:str)->dict:
    pin_bytes(path, ORIGINAL[name])
    with np.load(path,allow_pickle=False) as src:
        w={k:np.asarray(src[k],dtype=np.float64) for k in ['init_state','W_in','W_rec','W_out','b_rec','b_out']}
    assert w['init_state'].shape==(1,150)
    assert w['W_in'].shape==(150,75)
    assert w['W_rec'].shape==(150,150)
    assert np.all(w['W_in'][:,-1]==0)
    return w

def source_step(w,h,u,mt_linear):
    # Original author BasicSimulator_linOut (MT) / BasicSimulator (dlPFC).
    h2=.9*h+.1*(w['W_rec']@np.maximum(h,0)+w['W_in']@u+w['b_rec'])
    y=w['W_out']@(h2 if mt_linear else np.maximum(h2,0))+w['b_out']
    return h2,y

def trial(mt,dp,shown,good,ring,dots):
    hm=mt['init_state'][0].copy();hd=dp['init_state'][0].copy()
    cx=2*math.cos(math.radians(good));cy=2*math.sin(math.radians(good))
    motion=-.3+np.exp(.18*np.cos(np.deg2rad(np.arange(0,360,5)-shown)))
    for t in range(0,1200,10):
        u=np.zeros(75)
        if t>=ring: u[:2]=[cx,cy]
        if t>=dots: u[2:74]=motion
        hm,ym=source_step(mt,hm,u,True)
        d=np.zeros(75)
        if t>ring: d[:2]=[cx,cy]
        d[2:74]=ym[2:74]
        hd,yd=source_step(dp,hd,d,False)
    order=np.argsort(yd)
    return 5*int(order[-1]),float(yd[order[-1]]-yd[order[-2]])

def load_expected(path,axis):
    contents=pin_bytes(path,REF_CSV[axis])
    lines=[ln for ln in contents.decode('utf8').splitlines() if not ln.startswith('#')]
    data=list(csv.DictReader(lines))
    if len(data)!=180: raise RuntimeError('EXPECTED_ROW_COUNT_FAIL')
    return data

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--weights-dir',type=Path,required=True)
    a.add_argument('--dots-csv',type=Path,required=True)
    a.add_argument('--ring-csv',type=Path,required=True)
    a.add_argument('--output-dir',type=Path,required=True)
    args=a.parse_args()
    t0=time.monotonic()
    mt=model(args.weights_dir/'MTbroadsharp_m10.npz','MTbroadsharp_m10.npz')
    dp=model(args.weights_dir/'DLPFCcombined_m4.npz','DLPFCcombined_m4.npz')
    input_rows=[('motion_dots',load_expected(args.dots_csv,'motion_dots')),
                ('reward_ring',load_expected(args.ring_csv,'reward_ring'))]
    args.output_dir.mkdir(parents=True,exist_ok=True)
    records=[];failures=[];max_error=0.0
    for axis,rows in input_rows:
        for row in rows:
            good=int(row['reward_center_deg']);shown=int(row['shown_deg'])
            ring=int(row['ring_ms']);dots=int(row['dots_ms'])
            expected_choice=int(row['trained_winner_deg'])
            expected_margin=float(row['trained_top2_margin'])
            choice,margin=trial(mt,dp,shown,good,ring,dots)
            error=abs(margin-expected_margin)
            max_error=max(max_error,error)
            success=(choice==expected_choice and error<=2e-5)
            if not success: failures.append({'axis':axis,'good':good,'shown':shown,'ring':ring,'dots':dots,
                      'expected_choice':expected_choice,'got_choice':choice,
                      'expected_margin':expected_margin,'got_margin':margin,'absolute_error':error})
            records.append([axis,good,shown,ring,dots,expected_choice,choice,expected_margin,margin,error,int(success)])
    with (args.output_dir/'xh_s6_rot007_native_python_360_detailed.csv').open('w',encoding='utf8',newline='') as f:
        w=csv.writer(f);w.writerow(['axis','good','shown','ring','dots','expected_choice','choice','expected_margin','margin','abs_error','pass']);w.writerows(records)
    result={'artifact_id':'IW_XH_S6_ROT007_ORIGINAL_NPZ_PYTHON_360_CROSS_RUNTIME_REPLAY_001_20261112',
        'author_commit':AUTHOR_COMMIT,'author_git_blobs':ORIGINAL,'prior_reference_csv_blobs':REF_CSV,
        'source_numpy':np.__version__,'compared':len(records),'passed':len(records)-len(failures),
        'failed':len(failures),'max_margin_abs_error':max_error,'elapsed_s':time.monotonic()-t0,
        'scope':'Python NumPy independent implementation of author source mathematical recurrence, original author frozen NPZ; no noise; no original PsychRNN module runtime; no experimental data',
        'full_python_cross_runtime_weight_replay':'PASS' if not failures and len(records)==360 else 'FAIL',
        'failures':failures[:30],'no_canon':True,'no_exec_sign':True,'no_novelty':True}
    (args.output_dir/'xh_s6_rot007_native_python_360_summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(result,indent=2,sort_keys=True),flush=True)
    if result['full_python_cross_runtime_weight_replay']!='PASS':sys.exit(2)
if __name__=='__main__':main()
