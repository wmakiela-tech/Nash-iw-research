import csv,hashlib,json,math,pathlib
BASE=pathlib.Path('/mnt/data')
orig=BASE/'dtc0a_mask_sensitivity_N41_v0_3_1.csv'
calc=json.loads((BASE/'geeky_s12_rot009_helper_native_3d_25_coeff_results.json').read_text())
rows=[]
for row in csv.DictReader(orig.open()):
 a=float(row['alpha']);k=row['interior_k']; coeff=calc['quartics'][k]
 estimate=math.sqrt(sum(v*(a**i) for i,v in enumerate(coeff)))
 target=float(row['K_B_RMS'])
 rows.append({'alpha':a,'mask_k':int(k),'native_reconstructed_K_B_RMS':estimate,'historical_K_B_RMS':target,'relative_error':abs(estimate-target)/target})
out={'artifact_id':'IW_GEEKY_S12_ROT009_NATIVE_HELPER_HISTORICAL_CSV_VALIDATION_001_20261112','historical_csv_sha256':hashlib.sha256(orig.read_bytes()).hexdigest(),'retained_helper_sha256':calc['helper_sha256'],'rows_checked':len(rows),'max_relative_error':max(x['relative_error'] for x in rows),'all_within_1e_minus_11':all(x['relative_error']<1e-11 for x in rows),'rows':rows,'scope':'N41 B, only frozen 15 historical RMS, three alpha values 0,0.05,0.2; not original historical producer'}
(BASE/'geeky_s12_rot009_historical_csv_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'historical_csv_sha256':out['historical_csv_sha256'],'rows':len(rows),'max_rel':out['max_relative_error'],'PASS':out['all_within_1e_minus_11']}))
