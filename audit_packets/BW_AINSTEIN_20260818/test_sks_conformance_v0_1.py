#!/usr/bin/env python3
import json,copy
from pathlib import Path
from sks_reducer_v0_1 import derive_current_state,dedupe_and_validate_events,compile_neighborhood
HERE=Path(__file__).resolve().parent; D=json.loads((HERE/'sks_seed_slices_v0_1.json').read_text(encoding='utf-8'))
def ok(n,c):
 if not c: raise AssertionError(n)
 print('PASS',n)
d=copy.deepcopy(D); d['events'].append(copy.deepcopy(d['events'][0])); ok('duplicate_same_event_is_noop',len(dedupe_and_validate_events(d['events']))==len(D['events']))
d=copy.deepcopy(D); bad=copy.deepcopy(d['events'][0]); bad['payload']={'value':'CORRUPTED'}; d['events'].append(bad)
try: dedupe_and_validate_events(d['events']); raise AssertionError('collision_not_detected')
except ValueError as e: ok('duplicate_event_id_payload_collision_detected','EVENT_ID_COLLISION' in str(e))
state=derive_current_state(D)
ok('S_science_does_not_enact_P_adoption','adoption_state' not in state['POBJ:NRHO_RESEARCH_LINE']['facets'])
ok('P_presence_does_not_upgrade_S','epistemic_status' not in state['SOBJ:NRHO_QUOTIENT_PROBLEM']['facets'])
dim2=state['CLAIM:DIMR2_KCF']['facets']; ok('prior_art_separate_from_lifecycle','prior_art_origin' in dim2 and 'lifecycle_currentness' in dim2)
enp=compile_neighborhood(D,['CLAIM:DIMR2_KCF'],1); ok('neighborhood_is_open_world',enp['closed_world'] is False); ok('boundary_stub_on_truncation',len(enp['boundary_stubs'])>=1)
print('ALL CORE CONFORMANCE TESTS PASS')
