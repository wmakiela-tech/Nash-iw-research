#!/usr/bin/env python3
"""Standalone deterministic replay: copies dependency closure into temp folder,
runs independent k=5 7D ODE check and compares reference numeric outputs."""
from pathlib import Path
import tempfile,subprocess,shutil,json,sys
P=Path(__file__).resolve().parent
inputs=[
 'reproduce_high_order_moment_gate_024.py','reproduce_joint_c2_ratio_020.py',
 'reproduce_two_moment_kernel_023.py','edge_bridge_013.py',
 'active_micro_bridge_013.py','active_source_antispectral_012.py',
 'mech_s7_rotation_009/source_7d_clock_baryon_stress_009.py',
 'mech_s7_rotation_010/reproduce_mech_s7_thermal_eos_event_010.py',
 'mech_s6_public_2x2_raw.zip','mech_s6_paper_2x2_raw.zip',
 'mass_sensitivity_kernel_021.csv'
]
with tempfile.TemporaryDirectory(prefix='mech_s7_rot024_') as tmp:
 root=Path(tmp)
 for rel in inputs:
  (root/rel).parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(P/rel,root/rel)
 dest=root/'out'
 env=dict(__import__('os').environ,OPENBLAS_NUM_THREADS='1')
 proc=subprocess.run([sys.executable,str(root/'reproduce_high_order_moment_gate_024.py'),
   '--maps','exec','--degrees','5','--rtol','3e-9','--epsilon','.04','--out',str(dest)],
   cwd=root,env=env,capture_output=True,text=True,timeout=120)
 if proc.returncode:raise RuntimeError(proc.stdout+proc.stderr)
 fresh=json.loads((dest/'high_order_moment_results_024.json').read_text())['rows']
 prior=json.loads((P/'high_order_moment_results_024.json').read_text())['rows']
 delta=[]
 for a in fresh:
  b=next(x for x in prior if x['map']==a['map'] and x['moment_degree']==a['moment_degree'] and x['epsilon']==a['epsilon'])
  delta.append(abs(a['Xnuc']-b['Xnuc']))
 report={'clean_replay':'PASS' if max(delta)<1e-12 else 'FAIL','selected_degree':5,'map':'exec',
  'n_ode_cases':len(fresh),'max_abs_replayed_Xnuc_difference':max(delta),
  'clean_isolated_input_files':len(inputs)}
 (P/'clean_replay_024.json').write_text(json.dumps(report,indent=2))
 print(json.dumps(report,indent=2))