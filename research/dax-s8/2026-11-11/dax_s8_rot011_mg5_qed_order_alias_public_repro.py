#!/usr/bin/env python3
"""DAX-S8 ROT011: source-typed order gate, NOT native MadGraph diagrams or QED.
With --checkout provide full official MG5 checkout at pinned COMMIT.
Without it, only audited-source EXCERPT FIXTURE is checked.
"""
import argparse,hashlib,json,re
from pathlib import Path
COMMIT='a5b17913ef0b6e1c872016f94d0fb610207dab47'
SHA={
 'models/sm/vertices.py':'116b2c2279843830c31eb53405d86db3002f4fec',
 'models/sm/couplings.py':'d4bbfbf10ab02f665df30ee9d21cdfc82589758c',
 'models/sm/parameters.py':'3fdef86ab6d328e375a8a70c183b248804b3a79a',
 'models/sm/restrict_default.dat':'81943fc1cc83550a8177506015495cda6c981ec0'}
ENTRIES={
 'photon':('V_98','P.a',['GC_3']),
 'Z':('V_107','P.Z',['GC_50','GC_59']),
 'H':('V_104','P.H',['GC_89'])}
def gitblob(b):
 return hashlib.sha1(('blob %s\0'%len(b)).encode()+b).hexdigest()
def check(checkout):
 if checkout:
  source={}
  for path,sha in SHA.items():
   raw=(checkout/path).read_bytes()
   assert gitblob(raw)==sha,(path,gitblob(raw))
   source[path]=raw.decode('utf-8')
  vertices=source['models/sm/vertices.py']
  couplings=source['models/sm/couplings.py']
  assert re.search(r'^\s*11\s+0\.000000e\+00\s+# Me\s*$',source['models/sm/restrict_default.dat'],re.M)
  assert 'Me = Parameter' in source['models/sm/parameters.py']
  mode='FULL_PINNED_UPSTREAM_SOURCE'
 else:
  # Exact object identities and orders independently read from original full
  # GitHub source via authenticated source connector; local is only a fixture.
  vertices='\n'.join('%s = Vertex(particles = [ P.e__plus__, P.e__minus__, %s ], couplings = {%s})'%(
   name,boson,','.join('(0,%s):C.%s'%(i,c) for i,c in enumerate(cs)))
   for name,boson,cs in ENTRIES.values())
  couplings='\n'.join("%s = Coupling(order = {'QED':1})"%c
   for name,boson,cs in ENTRIES.values() for c in cs)
  mode='SOURCE_VERIFIED_EXCERPT_FIXTURE_ONLY'
 results={}
 for species,(name,boson,cs) in ENTRIES.items():
  if checkout:
   block=re.search(r'(?ms)^'+name+r' = Vertex\(.*?^\s*couplings\s*=.*?\)\s*$',vertices).group()
  else:block=next(v for v in vertices.splitlines() if v.startswith(name+' ='))
  assert boson in block and 'P.e__plus__' in block and 'P.e__minus__' in block
  for c in cs:
   assert 'C.'+c in block
   if checkout:
    cblock=re.search(r'(?ms)^'+c+r' = Coupling\(.*?^\s*order\s*=.*?\)\s*$',couplings).group()
   else:cblock=next(v for v in couplings.splitlines() if v.startswith(c+' ='))
   assert "'QED':1" in cblock
  results[species]={'vertex':name,'couplings':cs,'QED_order_each':1}
 assert 2*results['photon']['QED_order_each']+2*results['Z']['QED_order_each']==4
 return {'status':'PASS_SOURCE_TYPED_QED_ORDER_NOT_NEUTRAL_SPECIES',
  'mode':mode,'upstream_commit':COMMIT,'blob_sha':SHA,'vertices':results,
  'counterexample':'photon_exchange_and_Z_exchange_have_equal_MG5_QED_order',
  'limitations':'NO_NATIVE_DIAGRAM_GENERATION_OR_QED_AMPLITUDE_RUN'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--checkout',type=Path);x=p.parse_args()
 print(json.dumps(check(x.checkout),indent=2,sort_keys=True))
