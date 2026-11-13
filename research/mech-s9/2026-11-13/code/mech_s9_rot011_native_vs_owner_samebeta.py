#!/usr/bin/env python3
"""Mech-S9 ROT011: source-native GPT L2 vs owner independently executed default-tolerance dense grid.

Usage: python mech_s9_rot011_native_vs_owner_samebeta.py <native_l2_original_action.zip>
              <owner_original_data_yp064_default.csv_or_excerpt.csv> <output.json>

Scientific scope: nonblind retrospective 6 same-beta row checks, not physical validation,
not a new native solve, not retrospective rewriting of EKS1's 8/10 L2 gate.
"""
import csv, hashlib, io, json, sys, zipfile
from decimal import Decimal
from pathlib import Path

def rows(text):
    return list(csv.DictReader(x for x in text.splitlines() if x.strip() and not x.startswith('#')))

zpath, opath, rpath = map(Path, sys.argv[1:4])
with zipfile.ZipFile(zpath) as z:
    bad=z.testzip()
    assert bad is None, ('bad ZIP CRC',bad)
    raw=z.read('independent_L2_raw_calls.csv')
    rr=z.read('independent_L2_roots.csv')
    independent=rows(raw.decode())
owner_bytes=opath.read_bytes()
owner=rows(owner_bytes.decode())
assert len(independent)==57, len(independent)
coarse=[r for r in independent if r['j']=='22' and r['eval_kind']=='coarse']
assert len(coarse)==6, len(coarse)
lookup={round(Decimal(r['log10beta']),6):r for r in owner}
fields=('X_T0','X_T1','Yc_author')
ownerfields=('X_T0','X_T1','Yc_native')
comparisons=[]
for r in coarse:
    key=round(Decimal(r['log10beta']),6)
    assert key in lookup, (key,sorted(lookup))
    o=lookup[key]
    delta={f: str(Decimal(r[f])-Decimal(o[of])) for f,of in zip(fields,ownerfields)}
    comparisons.append({'log10beta':str(key), 'differences':delta,
        'native':{f:r[f] for f in fields}, 'owner':{f:o[of] for f,of in zip(fields,ownerfields)}})
max_delta=max(abs(Decimal(row['differences'][f])) for row in comparisons for f in fields)
result={
    'identity':'IW_MECH_S9_ROT011_NATIVE_L2_OWNER_REVIEW065_DENSE_SAME_BETA_001_20261113',
    'class':'RETROSPECTIVE_SAME_BETA_NONBLIND_NUMERIC_CONTROLS',
    'source_native_original_wuxu_commit':'d395183674cace6c9906a8911bdeb7234ba4040d',
    'native_action_run_id':43310359194,
    'native_action_zip_sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),
    'native_original_csv_sha256':hashlib.sha256(raw).hexdigest(),
    'native_original_roots_sha256':hashlib.sha256(rr).hexdigest(),
    'owner_original_file_git_blob':'38cdbe2091ef84f35b80f1a96f5506db6f47a3ee',
    'owner_reference_input_sha256':hashlib.sha256(owner_bytes).hexdigest(),
    'owner_reference_is_curated_subset':len(owner)!=31,
    'original_owner_source_rows':31,
    'source_native_total_calls':len(independent),
    'compared_common_beta_count':len(comparisons),
    'field_comparisons':len(comparisons)*len(fields),
    'max_absolute_stored_decimal_difference':str(max_delta),
    'same_beta_observation_operator_agreement_pass':max_delta<=Decimal('7e-16'),
    'historic_L2_acceptance':'8_PASS_2_FAIL_UNCHANGED',
    'owner_current_source_disposition':'BADACZ_REVIEW065_SOURCE_OWNER_CORRECTED_J22_V2_SPARSE_QUADRATIC_BIAS',
    'no_physical_PBH_bound':True,
    'no_JCAP_Fig5_original_producer_identity':True,
    'comparison':comparisons,
}
rpath.write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='comparison'},ensure_ascii=False,indent=2))
