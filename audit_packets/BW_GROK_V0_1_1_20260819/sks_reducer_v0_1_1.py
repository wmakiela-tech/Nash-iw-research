#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, copy
from pathlib import Path
from collections import defaultdict, deque

FACETS_BY_PLANE={
'S':{'epistemic_status','lifecycle_currentness','prior_art_origin','claim_boundary','research_front_state'},
'P':{'project_lifecycle','adoption_state','authority_state','access_state','transport_state','obligation_state'},
'SPINE':{'integrity_state','custody_state','reproducibility_state','methodological_validity_state'}}

SAFETY_KINDS={'WARRANT_BOUNDARY','NEGATIVE_KNOWLEDGE','UNKNOWN'}

def canonical(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)

def dedupe_and_validate_events(events):
    seen={}; out=[]
    for ev in events:
        eid=ev['event_id']; blob=canonical(ev)
        if eid in seen:
            if seen[eid]!=blob: raise ValueError(f'EVENT_ID_COLLISION_WITH_DIFFERENT_PAYLOAD: {eid}')
            continue
        if not ev.get('issuer_cell_id'):
            raise ValueError(f'ISSUER_CELL_ID_REQUIRED: {eid}')
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
        last[key]=seq
        state[sid]['facets'][facet]={'value':copy.deepcopy(ev['payload']),'event_id':ev['event_id'],'sequence':seq}
    return state

def all_ref_index(dataset):
    idx={}
    for coll,idkey in [('sources','source_id'),('source_anchors','anchor_id'),('records','record_id')]:
        for x in dataset.get(coll,[]): idx[x[idkey]]=x
    return idx

def validate_semantic_guards(dataset):
    idx=all_ref_index(dataset)
    recs={r['record_id']:r for r in dataset.get('records',[])}
    evidence={r['record_id']:r for r in dataset.get('records',[]) if r.get('record_kind')=='EVIDENCE'}
    for ev in dedupe_and_validate_events(dataset.get('events',[])):
        if ev['plane']=='S' and ev['facet']=='epistemic_status' and ev.get('payload',{}).get('value')=='SUPPORTED_CURRENT':
            rec=recs.get(ev['subject_id'],{})
            domain=rec.get('payload',{}).get('domain')
            if domain=='formal_mathematics':
                proof=False
                for ref in ev.get('provenance_refs',[]):
                    er=evidence.get(ref)
                    if er and er.get('payload',{}).get('evidence_type')=='PROOF':
                        proof=True
                if not proof:
                    raise ValueError(f'FORMAL_MATH_SUPPORTED_WITHOUT_PROOF_EVIDENCE: {ev["event_id"]}')
    sources={s['source_id']:s for s in dataset.get('sources',[])}
    for rel in dataset.get('relations',[]):
        if rel.get('relation_type')=='EXACT_PRIOR_ART_ABSORPTION':
            external=[sources.get(a) for a in rel.get('arguments',[]) if a in sources]
            for s in external:
                if s and (not s.get('store_locators') or str(s.get('bibliographic_status','')).upper().startswith('PARTIAL')):
                    raise ValueError(f'EXACT_PRIOR_ART_WITH_UNLOCATED_SOURCE: {rel["relation_id"]}')
    return True

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

def safety_companions(dataset, included_ids):
    companions=[]
    for r in dataset.get('records',[]):
        if r.get('record_kind') not in SAFETY_KINDS: continue
        applies=r.get('payload',{}).get('applies_to',[])
        if any(t in included_ids for t in applies):
            companions.append(r)
    return companions

def terminal_debts(dataset, included_ids):
    return [x for x in dataset.get('completion_debt',[])
            if x.get('closure_relevance')=='TERMINAL_BLOCKER' and x.get('subject_id') in included_ids]

def compile_neighborhood(dataset,roots,max_nodes=8):
    recs={r['record_id']:r for r in dataset.get('records',[])}
    adj=adjacency(dataset); q=deque(roots); visited=set(); units=[]; stubs=[]
    while q and len(visited)<max_nodes:
        node=q.popleft()
        if node in visited or node not in recs: continue
        visited.add(node); units.append(recs[node])
        for edge,nbr in adj.get(node,[]):
            if nbr in visited: continue
            if len(visited)+len(q)<max_nodes: q.append(nbr)
            else: stubs.append({'source_id':node,'via':edge,'target_id':nbr,'expansion_handle':f'EXPAND:{nbr}'})
    safety=safety_companions(dataset,visited)
    safety_ids={r['record_id'] for r in safety}
    combined_ids=visited|safety_ids
    state=derive_current_state(dataset)
    state_subset={}
    for rid in combined_ids:
        if rid in state:
            state_subset[rid]=state[rid]
    debts=terminal_debts(dataset,combined_ids)
    return {
      'closed_world':False,
      'roots':roots,
      'units':units,
      'mandatory_safety_companions':safety,
      'current_state_subset':state_subset,
      'terminal_debts':debts,
      'boundary_stubs':stubs,
      'explicit_omissions':['supporting or distant graph content may be omitted by node budget; active boundaries are not']
    }

def event_set_digest(events):
    blobs=[canonical(e) for e in dedupe_and_validate_events(events)]
    return hashlib.sha256('\n'.join(sorted(blobs)).encode()).hexdigest()

def build_views(dataset):
    validate_semantic_guards(dataset)
    return {'reducer_version':'0.1.1','event_set_digest':event_set_digest(dataset.get('events',[])),'current_state':derive_current_state(dataset)}

if __name__=='__main__':
    here=Path(__file__).resolve().parent
    data=json.loads((here/'sks_seed_slices_v0_1_1.json').read_text(encoding='utf-8'))
    (here/'derived_current_state_v0_1_1.json').write_text(json.dumps(build_views(data),indent=2,ensure_ascii=False),encoding='utf-8')
    (here/'example_epistemic_neighborhood_v0_1_1.json').write_text(
      json.dumps(compile_neighborhood(data,['CLAIM:K12_LEVEL0'],1),indent=2,ensure_ascii=False),encoding='utf-8')
    print('PASS: v0.1.1 derived state and safety-closed neighborhood generated.')
