#!/usr/bin/env python3
"""ROT011 independent convergence check of EOS quadrature/grid, host tolerance,
and Radau 7D tolerances for two extreme deposition carriers."""
import json,csv,importlib.util,math
from pathlib import Path
import numpy as np
p=Path(__file__).with_name('reproduce_active_source_micro_thermal_011.py')
spec=importlib.util.spec_from_file_location('host_011',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
base=m.module(Path('/mnt/data/mech_s7_rotation_009/source_7d_clock_baryon_stress_009.py'))
ctx=m.contexts(base,'/mnt/data/mech_s7_rotation_010/mech_s6_public_2x2_raw.zip','/mnt/data/mech_s7_rotation_010/mech_s6_paper_2x2_raw.zip')
rows=[]
for n,quad in [(700,90),(1600,130),(2200,160)]:
    eos=m.eos_table(n=n,quad=quad)
    for chi in (0,1):
        host=m.prepare_host(base,ctx,eos,chi,rtol=5e-11)
        rows.append({'test':'eos_grid','n':n,'quad':quad,'chi':chi,'host_rtol':5e-11,'solver_rtol':None,'Tcut':host['Tcut'],'t_nuc':host['Tnuc_time'],'energy_rel_resid':host['cons_integral_relative'],'Xexec_pub':None,'exec_delta':None,'sym_delta':None})
        print('EOS',n,quad,chi,host['Tcut'],host['Tnuc_time'],flush=True)
# Baseline host quadrature 1600 130, tighter kinetic solver at chi extremes.
eos=m.eos_table()
for chi in (0,1):
    host=m.prepare_host(base,ctx,eos,chi,rtol=5e-11)
    for rtol in (3e-7,3e-8,3e-9):
        measures={}
        for mp in ('exec','sym'):
            cells=[m.evolve(base,ctx,eos,host,mp,law,False,rtol) for law in ('public','paper')]
            measures[mp]=cells[1]['X_nuc']-cells[0]['X_nuc']
            if mp=='exec':public=cells[0]['X_nuc']
        rows.append({'test':'kinetic_rtol','n':1600,'quad':130,'chi':chi,'host_rtol':5e-11,'solver_rtol':rtol,'Tcut':host['Tcut'],'t_nuc':host['Tnuc_time'],'energy_rel_resid':host['cons_integral_relative'],'Xexec_pub':public,'exec_delta':measures['exec'],'sym_delta':measures['sym']})
        print('SOLVER',chi,rtol,measures,flush=True)
with (p.parent/'refinement_controls_011.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(p.parent/'refinement_controls_011.json').write_text(json.dumps(rows,indent=2))