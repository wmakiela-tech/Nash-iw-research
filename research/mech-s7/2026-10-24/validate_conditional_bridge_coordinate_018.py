#!/usr/bin/env python3
"""Execute an independent change-of-variable test on Mech-S7 ROT013 PREEDGE
conditional bridge (10 components T, ln a, ln rhoNu, Xn, 6 species).
Two solves use the same source-pinned rate interpolation and physics; only the
integration variable differs: u=M/Marchive versus z=3 ln(M/Marchive), exactly
an affine shift of global ln remaining lifetime. NOT the native Julia 10D.
"""
from pathlib import Path
import importlib.util,math,csv,json
import numpy as np
from scipy.integrate import solve_ivp as scipy_solve
DIR=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('bridge018',DIR/'edge_bridge_013.py')
e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
e.base=e.module(e.BASE,'base018')
original=e.module(e.SCRIPT,'origmod018')
mod=e.host_wrapper_setup(original)
raw=e.base.load(e.PUB,e.PAP)
eos=mod.eos_table()

# Single numerical integration coordinate reparameterization; no patch to physics RHS.
def logtau_solver(fun,tspan,y0,method,rtol,atol,max_step,**kw):
    u0,uf=tspan
    z0,zf=3*math.log(u0),3*math.log(uf)
    def rhs(z,y):
        u=math.exp(z/3)
        return fun(u,y)*(u/3)
    sol=scipy_solve(rhs,(z0,zf),y0,method=method,rtol=rtol,atol=atol,max_step=0.01,**kw)
    return sol

rows=[]
for mp in ('exec','sym'):
    native=e.run_bridge(e.base,mod,raw,eos,.5,mp,False,rtol=3e-9)
    prev=e.solve_ivp
    try:
        e.solve_ivp=logtau_solver
        phase=e.run_bridge(e.base,mod,raw,eos,.5,mp,False,rtol=3e-9)
    finally:
        e.solve_ivp=prev
    for variable in ('Tedge','lnaedge','rnu_edge','Xedge','nedge'):
        a=native[variable];b=phase[variable];err=abs(a-b)
        rows.append({'map':mp,'quantity':variable,'mass_u':a,'logtau_z':b,
                     'absolute_difference':err,'relative_difference':err/max(abs(a),abs(b),1e-90),
                     'original_steps':native['steps'],'phase_steps':phase['steps']})
    for i,(a,b) in enumerate(zip(native['nedge_pop_cm3'],phase['nedge_pop_cm3'])):
        rows.append({'map':mp,'quantity':f'n_pop_{e.base.SPECIES[i]}','mass_u':a,'logtau_z':b,
                     'absolute_difference':abs(a-b),
                     'relative_difference':abs(a-b)/max(abs(a),abs(b),1e-90),
                     'original_steps':native['steps'],'phase_steps':phase['steps']})
    print(mp,'Xedge',native['Xedge'],phase['Xedge'],'Tedge',native['Tedge'],phase['Tedge'],
          'orig steps',native['steps'],'new steps',phase['steps'],flush=True)
max_relative=max(row['relative_difference'] for row in rows)
print('max_relative',max_relative,'max_abs_X',max(x['absolute_difference'] for x in rows if x['quantity']=='Xedge'))
if max_relative>6e-6:
    print('WARNING tight numerical coordinate comparison not met',flush=True)
with (DIR/'conditional_bridge_mass_vs_logtau_018.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
(DIR/'conditional_bridge_mass_vs_logtau_018.json').write_text(json.dumps({'cells':rows,'max_relative':max_relative,'rtol':3e-9,'model':'ROT013 source-native tabulated PREEDGE conditional 10-component, NOT original Julia 10D'},indent=2))
assert max_relative<6e-6
print('PASS mass-vs-logtau direct 10-component conditional bridge')