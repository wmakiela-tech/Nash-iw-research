import json,time,sys
from pathlib import Path
from mpmath import iv
from verify_m13_rot33_interval import tensor_polys,quartic
iv.dps=45
ch=sys.argv[1];chidx='ABC'.index(ch);t=time.monotonic();pol=tensor_polys(41)[chidx];print('pol',round(time.monotonic()-t,2),flush=True)
cache={};data={}
for k in range(2,7):
 v=quartic(pol,41,k,cache);data[str(k)]=[[str(x.a),str(x.b)] for x in v];print(ch,k,round(time.monotonic()-t,2),flush=True)
out=Path(__file__).resolve().parent/('direct_'+ch+'.json');out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n');print('WROTE',out,flush=True)