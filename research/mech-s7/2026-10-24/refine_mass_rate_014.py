#!/usr/bin/env python3
"""Independent stringent relative tolerance check of ROT014 rate perturbation cells."""
from pathlib import Path
import importlib.util, time, json, csv
here=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('bridge_014_refine',str(here/'edge_bridge_013.py'))
b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
base=b.base=b.module(b.BASE,'base_014_refine')
mod=b.host_wrapper_setup(b.module(b.SCRIPT,'micro_014_refine'))
raw=base.load(b.PUB,b.PAP)
ctx0=mod.contexts(base,b.PUB,b.PAP)
eos=mod.eos_table()
G0=base.GAMMA;dt0=base.DT_EDGE
rows=[]; t=time.time()
for scale in (0.99,1.,1.01):
 base.GAMMA=G0*scale;base.DT_EDGE=base.M_EDGE**3/base.GAMMA
 for mp in ('exec','sym'):
  br=b.run_bridge(base,mod,raw,eos,.5,mp,False,rtol=3e-9)
  ctx=b.shifted_ctx(ctx0,br,mp)
  host=mod.prepare_host(base,ctx,eos,.5,rtol=2e-10)
  xpub=mod.evolve(base,ctx,eos,host,mp,'public',rtol=3e-9)['X_nuc']
  xpap=mod.evolve(base,ctx,eos,host,mp,'paper',rtol=3e-9)['X_nuc']
  rows.append({'gamma_ratio':scale,'map':mp,'deltaX_rtol3e9':xpap-xpub,'X_public_rtol3e9':xpub})
  print('TIGHT',scale,mp,'dX',xpap-xpub,'sec',round(time.time()-t,1),flush=True)
base.GAMMA=G0;base.DT_EDGE=dt0
prior=json.loads((here/'mass_clock_rate_014.json').read_text())['results']
for row in rows:
 r=next(x for x in prior if x['gamma_ratio']==row['gamma_ratio'] and x['map']==row['map'] and x['clock_variant']=='last-row-absolute')
 row['deltaX_rtol3e8']=r['deltaX'];row['absolute_contrast_gap']=abs(row['deltaX_rtol3e9']-r['deltaX'])
with (here/'mass_rate_refinement_014.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print('DONE',max(x['absolute_contrast_gap'] for x in rows))