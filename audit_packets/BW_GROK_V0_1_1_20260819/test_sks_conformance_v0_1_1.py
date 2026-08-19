#!/usr/bin/env python3
import json,copy
from pathlib import Path
from sks_reducer_v0_1_1 import derive_current_state,dedupe_and_validate_events,compile_neighborhood,validate_semantic_guards
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'sks_seed_slices_v0_1_1.json').read_text(encoding='utf-8'))
F=json.loads((HERE/'sks_conformance_fixtures_v0_1_1.json').read_text(encoding='utf-8'))

def ok(n,c):
    if not c: raise AssertionError(n)
    print('PASS',n)

x=copy.deepcopy(D); x['events'].append(copy.deepcopy(x['events'][0]))
ok('duplicate_same_event_is_noop',len(dedupe_and_validate_events(x['events']))==len(D['events']))

x=copy.deepcopy(D); bad=copy.deepcopy(x['events'][0]); bad['payload']={'value':'CORRUPTED'}; x['events'].append(bad)
try:
    dedupe_and_validate_events(x['events']); raise AssertionError('collision_not_detected')
except ValueError as e: ok('duplicate_event_id_payload_collision_detected','EVENT_ID_COLLISION' in str(e))

def fixture_dataset(fid):
    fx=next(z for z in F['fixtures'] if z['fixture_id']==fid)
    return {'records':fx.get('records',[]),'events':fx.get('events',[]),'relations':fx.get('relations',[]),'bridges':fx.get('bridges',[]),'sources':[],'source_anchors':[],'completion_debt':[]}

fx=fixture_dataset('FIX:P_ADOPTION_MUST_NOT_UPGRADE_S')
st=derive_current_state(fx)
ok('P_adoption_does_not_upgrade_S','epistemic_status' not in st['CLAIM:FIX_SCI']['facets'])
ok('P_closure_does_not_close_S','lifecycle_currentness' not in st['CLAIM:FIX_SCI']['facets'])

fx=fixture_dataset('FIX:S_SUPPORT_MUST_NOT_ENACT_P')
st=derive_current_state(fx)
ok('S_support_does_not_enact_P_adoption','adoption_state' not in st['POBJ:FIX_PROJECT2']['facets'])
ok('S_support_does_not_enact_P_authority','authority_state' not in st['POBJ:FIX_PROJECT2']['facets'])

st=derive_current_state(D); dim2=st['CLAIM:DIMR2_KCF']['facets']
ok('prior_art_separate_from_lifecycle','prior_art_origin' in dim2 and 'lifecycle_currentness' in dim2)
ok('dim2_closure_is_pending_source_verification',dim2['lifecycle_currentness']['value']['value']=='CLOSED_PENDING_SOURCE_VERIFICATION')

enp=compile_neighborhood(D,['CLAIM:DIMR2_KCF'],1)
ok('neighborhood_is_open_world',enp['closed_world'] is False)
ok('boundary_stub_on_truncation',len(enp['boundary_stubs'])>=1)

enp=compile_neighborhood(D,['CLAIM:K12_LEVEL0'],1)
sk={r['record_kind'] for r in enp['mandatory_safety_companions']}
ids={r['record_id'] for r in enp['mandatory_safety_companions']}
ok('K12_warrant_boundary_not_truncated','WARRANT_BOUNDARY' in sk and 'BOUNDARY:K12_FORBIDDEN_UPGRADES' in ids)
ok('K12_unknown_not_truncated','UNKNOWN:K12_ATTRIBUTION' in ids)

x=copy.deepcopy(D)
rel=next(r for r in x['relations'] if r['relation_id']=='REL:NRHO_DIM2_ABSORBED')
rel['relation_type']='EXACT_PRIOR_ART_ABSORPTION'
try:
    validate_semantic_guards(x); raise AssertionError('unlocated exact prior art not blocked')
except ValueError as e: ok('exact_prior_art_unlocated_source_blocked','EXACT_PRIOR_ART_WITH_UNLOCATED_SOURCE' in str(e))

x=copy.deepcopy(D)
ev=next(e for e in x['events'] if e['subject_id']=='CLAIM:NRHO_GENERAL_QUOTIENT' and e['facet']=='epistemic_status')
ev['event_type']='QUALIFIED'; ev['payload']={'value':'SUPPORTED_CURRENT'}
try:
    validate_semantic_guards(x); raise AssertionError('formal math proof guard failed')
except ValueError as e: ok('formal_math_supported_without_proof_blocked','FORMAL_MATH_SUPPORTED_WITHOUT_PROOF_EVIDENCE' in str(e))

x=copy.deepcopy(D); x['events'][0].pop('issuer_cell_id',None)
try:
    dedupe_and_validate_events(x['events']); raise AssertionError('issuer guard failed')
except ValueError as e: ok('issuer_cell_required','ISSUER_CELL_ID_REQUIRED' in str(e))

fx=fixture_dataset('FIX:SUPERSESSION_HISTORY_PRESERVED')
st=derive_current_state(fx)
ok('supersession_current_state_sequence_2',st['CLAIM:FIX_SUPER']['facets']['epistemic_status']['sequence']==2)
ok('supersession_raw_history_preserved',len(fx['events'])==2)

ok('patched_seed_semantic_guards',validate_semantic_guards(D) is True)

print('ALL v0.1.1 CORE CONFORMANCE TESTS PASS')
