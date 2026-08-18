#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, copy
from pathlib import Path
from collections import defaultdict, deque
FACETS_BY_PLANE={
'S':{'epistemic_status','lifecycle_currentness','prior_art_origin','claim_boundary','research_front_state'},
'P':{'project_lifecycle','adoption_state','authority_state','access_state','transport_state','obligation_state'},
'SPINE':{'integrity_state','custody_state','reproducibility_state'}}
def canonical(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def dedupe_and_validate_events(events):
 seen={}; out=[]
 for ev in events:
  eid=ev['event_id']; blob=canonical(ev)
  if eid in seen:
   if seen[eid]!=blob: raise ValueError(f'EVENT_ID_COLLISION_WITH_DIFFERENT_PAYLOAD: {eid}')
   continue
  seen[eid]=blob; out.append(ev)
 return out
def derive_current_state(dataset):
 records={r['record_id']:r for r in dataset.get('records',[])}
 events=dedupe_and_validate_events(dataset.get('events',[]))
 events.sort(key=lambda e:(e['subject_id'],e['facet'],e['sequence'],e['event_id']))
 state={rid:{'plane':r['plane'],'facets':{}} for rid,r in records.items()}; last={}
 for ev in events:
  sid,plane,facet,seq=ev['subject_id'],ev['plane'],ev['facet'],ev['sequence']
  if sid not in records: raise ValueError(f'EVENT_SUBJECT_MISSING: {sid}')
  if records[sid]['plane']!=plane: raise ValueError(f'EVENT_PLANE_MISMATCH: {ev["event_id"]}')
  if facet not in FACETS_BY_PLANE.get(plane,set()): raise ValueError(f'FACET_NOT_ALLOWED_FOR_PLANE: {plane}:{facet}')
  key=(sid,facet)
  if key in last and seq<=last[key]: raise ValueError(f'NON_MONOTONIC_OR_AMBIGUOUS_SEQUENCE: {ev["event_id"]}')
  last[key]=seq; state[sid]['facets'][facet]={'value':copy.deepcopy(ev['payload']),'event_id':ev['event_id'],'sequence':seq}
 return state
def adjacency(dataset):
 adj=defaultdict(list)
 for rel in dataset.get('relations',[]):
  args=rel.get('arguments',[])
  for a in args:
   for b in args:
    if a!=b: adj[a].append((rel['relation_id'],b))
 for br in dataset.get('bridges',[]):
  a,b=br['from_id'],br['to_id']; adj[a].append((br['bridge_id'],b)); adj[b].append((br['bridge_id'],a))
 return adj
def compile_neighborhood(dataset,roots,max_nodes=8):
 recs={r['record_id']:r for r in dataset.get('records',[])}; adj=adjacency(dataset); q=deque(roots); visited=set(); units=[]; stubs=[]
 while q and len(visited)<max_nodes:
  node=q.popleft()
  if node in visited or node not in recs: continue
  visited.add(node); units.append(recs[node])
  for edge,nbr in adj.get(node,[]):
   if nbr in visited: continue
   if len(visited)+len(q)<max_nodes: q.append(nbr)
   else: stubs.append({'source_id':node,'via':edge,'target_id':nbr,'expansion_handle':f'EXPAND:{nbr}'})
 return {'closed_world':False,'roots':roots,'units':units,'boundary_stubs':stubs,'explicit_omissions':['distant graph content omitted by node budget']}
def event_set_digest(events):
 blobs=[canonical(e) for e in dedupe_and_validate_events(events)]
 return hashlib.sha256('\n'.join(sorted(blobs)).encode()).hexdigest()
def build_views(dataset): return {'reducer_version':'0.1.0','event_set_digest':event_set_digest(dataset.get('events',[])),'current_state':derive_current_state(dataset)}
if __name__=='__main__':
 here=Path(__file__).resolve().parent; data=json.loads((here/'sks_seed_slices_v0_1.json').read_text(encoding='utf-8'))
 (here/'derived_current_state_v0_1.json').write_text(json.dumps(build_views(data),indent=2,ensure_ascii=False),encoding='utf-8')
 (here/'example_epistemic_neighborhood_v0_1.json').write_text(json.dumps(compile_neighborhood(data,['CLAIM:DIMR2_KCF'],5),indent=2,ensure_ascii=False),encoding='utf-8')
 print('PASS: derived current state and example open-world neighborhood generated.')
