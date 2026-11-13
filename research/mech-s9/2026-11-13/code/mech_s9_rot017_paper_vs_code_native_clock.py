#!/usr/bin/env python3
"""ROT017 Wu-Xu original source native-clock emissivity contrast.
First-two table rows pinned Wu-Xu Git blob 06d0883a27b108692720422294ba2baacd381a64;
v1 mesons original table blob 1cfc5eac427bd71aa984e630ac939188848b3952.
This calculates frozen-background production proxies, not a changed 10D ODE or physical Yp.
"""
import csv, io, zipfile, hashlib, math, json, sys
from pathlib import Path
INPUT_SHA='71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486'
CSV_SHA='45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1'
# Literal FIRST TWO original source table rows. Original GeV values.
TAB=[
[5.609588603804452e32,489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596],
[6.099798045788406e32,442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213]
]
NAMES=['pi_charged','K_charged','K0_long','proton','neutron']
assert len(sys.argv)==3
zpath=Path(sys.argv[1]); zbytes=zpath.read_bytes()
assert hashlib.sha256(zbytes).hexdigest()==INPUT_SHA
with zipfile.ZipFile(io.BytesIO(zbytes)) as z:
 assert z.testzip() is None
 mf=z.read('ARTIFACT_SHA256SUMS').decode().splitlines(); assert len(mf)==16
 for line in mf:
  hexf,name=line.split(maxsplit=1)
  assert hashlib.sha256(z.read(name.split('/')[-1])).hexdigest()==hexf
 raw=z.read('author_native_raw_hadron_history_10000.csv')
 assert hashlib.sha256(raw).hexdigest()==CSV_SHA
 rows=list(csv.DictReader(io.StringIO(raw.decode())))
assert len(rows)==10000
m=[float(r['PBH_mass_g']) for r in rows];t=[float(r['t_seconds']) for r in rows];flags=[int(r['nPBH_zero']) for r in rows]
ev=next(i for i,x in enumerate(flags) if x); assert ev==8544
assert all(x==0 for x in flags[:ev]) and all(x==1 for x in flags[ev:]); assert all(t[i]<t[i+1] for i in range(len(t)-1))
k=next(i for i in range(1,ev) if m[i]<1e9);assert k==8383
# Boundaries in native source mass (code first table M0 ~ 1e9g).
m0=1e9; lam=(m[k-1]-m0)/(m[k-1]-m[k]); tx=t[k-1]+lam*(t[k]-t[k-1]);
ms=[m0]+m[k:ev]; ts=[tx]+t[k:ev]; assert all(0<v<=m0 for v in ms)
assert all(ts[i]<ts[i+1] for i in range(len(ts)-1))
# first two tabulated rates are the original log-log extrapolation formula, not fitted independently.
expn=[math.log(TAB[1][i+1]/TAB[0][i+1])/math.log(TAB[1][0]/TAB[0][0]) for i in range(5)]
# Both models are anchored to the SAME original R0 at M0: Rcode=R0*(M/M0)^p_code; Rpaper=R0*(M/M0)^(-1.3).
# At the measured table edge first node should exactly equal R0 (mass conversion at ~1e9g).
def pchip_integral(t,y):
 h=[t[i+1]-t[i] for i in range(len(t)-1)]
 s=[(y[i+1]-y[i])/h[i] for i in range(len(h))]
 def endpoint(h0,h1,s0,s1):
  q=((2*h0+h1)*s0-h0*s1)/(h0+h1)
  if s0==0 or q*s0<=0: return 0.0
  if s0*s1<0 and abs(q)>3*abs(s0): return 3*s0
  return q
 d=[0.0]*len(y)
 d[0]=endpoint(h[0],h[1],s[0],s[1])
 d[-1]=endpoint(h[-1],h[-2],s[-1],s[-2])
 for i in range(1,len(y)-1):
  v,w=s[i-1],s[i]
  if v*w<=0: d[i]=0.0
  else:
   w1=2*h[i]+h[i-1];w2=h[i]+2*h[i-1]
   d[i]=(w1+w2)/(w1/v+w2/w)
 return math.fsum(dt*((y0+y1)/2+dt*(d0-d1)/12)
   for dt,y0,y1,d0,d1 in zip(h,y[:-1],y[1:],d[:-1],d[1:]))

def exposure(rate):
 vals=[rate(x) for x in ms]
 delta=[ts[i+1]-ts[i] for i in range(len(ts)-1)]
 left=math.fsum(vals[i]*d for i,d in enumerate(delta))
 right=math.fsum(vals[i+1]*d for i,d in enumerate(delta))
 trapezoid=(left+right)/2
 return {'left':left,'right':right,'trapezoid':trapezoid,
         'pchip':pchip_integral(ts,vals)}
result={'status':'POSTHOC_AUTHOR_PAPER_RATE_EXPONENT_VS_CODE_EXTRAPOLATION_FROZEN_NATIVE_MASS_CLOCK',
'author_git_commit':'d395183674cace6c9906a8911bdeb7234ba4040d',
'original_v1_table_blob':'1cfc5eac427bd71aa984e630ac939188848b3952',
'original_v2_table_blob':'06d0883a27b108692720422294ba2baacd381a64',
'original_first_two_table_rows_GeV':TAB,
'original_native_run':43436800793,'original_native_artifact':14045176436,'original_native_zip_sha256':INPUT_SHA,
'new_Julia_calls':0,'native_samples':10000,'PBH_last_active_index_one_based':ev,
'node_bracket_one_based':[k,k+1], 'node_linear_interpolated_time_s':tx,
'last_active_mass_g':m[ev-1],'last_active_time_s':t[ev-1],
'extrapolated_time_samples_including_interpolated_node':len(ms),
'channel_results':[],
'exclusion_note':'No integration over PBH cutoff; no physical hadronization uncertainty; paper prescription is an authors-stated analytic extension, not independent generator data.',
'ceilings':['NO_CAUSAL_DELTA_X','NO_NATIVE_10D_INTERVENTION','NO_PHYSICAL_PBH_BOUND','NO_NOVELTY','NO_CANON','NO_EXEC_SIGN']}
for i,name in enumerate(NAMES):
 p=expn[i];r0=TAB[0][i+1]
 c=exposure(lambda mass:r0*(mass/m0)**p)
 a=exposure(lambda mass:r0*(mass/m0)**(-1.3))
 ratios={method:a[method]/c[method] for method in c}
 rr_last=(m[ev-1]/m0)**(-1.3-p)
 rr_half=(0.5)**(-1.3-p)
 result['channel_results'].append({'channel':name,'p_code':p,'p_paper':-1.3,
 'rate_ratio_at_last_saved_active_mass':rr_last,'rate_ratio_at_0p5e9g':rr_half,
 'source_native_time_integral_code_proxy':c,'source_native_time_integral_paper_proxy':a,
 'time_integrated_paper_to_code_ratio':ratios,'time_integrated_delta_percent_trapezoid':100*(ratios['trapezoid']-1),
 'time_integrated_delta_percent_pchip':100*(ratios['pchip']-1)})
assert all(1.18<x['rate_ratio_at_last_saved_active_mass']<1.25 for x in result['channel_results'])
assert all(1.0<x['time_integrated_paper_to_code_ratio']['trapezoid']<1.25 for x in result['channel_results'])
assert all(abs(x['time_integrated_delta_percent_trapezoid']-x['time_integrated_delta_percent_pchip'])<0.09 for x in result['channel_results'])
Path(sys.argv[2]).write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
print(json.dumps({'node_t':tx,'last_t':t[ev-1], 'ratios':[(v['channel'],v['p_code'],v['rate_ratio_at_last_saved_active_mass'],v['time_integrated_delta_percent_trapezoid']) for v in result['channel_results']]},indent=2))
