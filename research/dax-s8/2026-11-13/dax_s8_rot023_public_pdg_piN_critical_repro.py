#!/usr/bin/env python3
"""DAX-S8 ROT023 reproducibility: original-source PDG/COMPAS pion-nucleon
first hadronic encounter versus R68 vacuum charged-pion decay.
Input: four original .dat files and source_rot020_results_exact.json
from verified full ROT023 package, all beside this program.
This deliberately DOES NOT extrapolate piN σ to 718GeV, does not infer
free BBN nucleon fraction or pion loss/escape. Python stdlib only.
"""
from pathlib import Path
import hashlib,json,math,re
root=Path(__file__).resolve().parent
pins={
 'pimp_total.dat':'fa5bc4b5a1efbc80b0f258b7e16a97f8795b803143ca60ca93fd398a187576b3',
 'pipp_total.dat':'439a76fe69ecfc13ac624ae7e0c77be31b1915620b2433140a654b16d2e4031a',
 'pimp_elastic.dat':'5f9af000adc836c11a905adb9e43b41537ed77282ff37963ae6f6bce0bf3406f',
 'pipp_elastic.dat':'e068a871cc329be780ce1023ad9a98419c94b31222f6e3f7b9d509daef69cd11'
}
def parse(name):
 raw=(root/name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==pins[name]
 rows=[]
 for line in raw.decode('ascii').splitlines():
  a=line.split()
  if len(a)<10:continue
  try:rec=dict(i=int(a[0]),p=float(a[1]),sig=float(a[4]),reference=' '.join(a[9:]))
  except ValueError:continue
  rows.append(rec)
 assert all(row['i']==i+1 for i,row in enumerate(rows))
 return rows
datasets={k:parse(k) for k in pins}
assert [len(datasets[k]) for k in pins]==[605,428,277,129]
# The pipp_total original HEADER says 412 but has 428 source rows.
def datum(dataset,p,ref):
 matches=[x for x in datasets[dataset] if x['p']==p and ref in x['reference']]
 assert len(matches)==1
 return matches[0]['sig']
plus340=datum('pipp_total.dat',340.,'CARROLL 79')
minus340=datum('pimp_total.dat',340.,'CARROLL 79')
minus640=datum('pimp_total.dat',640.,'DERSCH 99')
total360=datum('pimp_total.dat',360.,'FIRESTONE 76')
elastic360=datum('pimp_elastic.dat',360.,'FIRESTONE 76')
assert [plus340,minus340,minus640,total360,elastic360]==[24.62,25.08,27.1,25.25,3.61]
prior=json.loads((root/'source_rot020_results_exact.json').read_text())
mpi=float(prior['constants']['mpi_MeV'])
T=float(prior['constants']['T_MeV'])
ctau_m=float(prior['constants']['pi_c_tau_m'])
Epi=float(prior['pion_pair_Q_mean_MeV'])/2
gamma=Epi/mpi
beta=math.sqrt(1-1/gamma**2)
hbarc_cm=1.973269804e-11
zeta3=1.20205690315959428539973816151145
n_gamma=2*zeta3/math.pi**2*(T/hbarc_cm)**3
eta=6.12e-10
n_b=eta*n_gamma
Ldec_m=ctau_m*gamma*beta
sigma_crit_mb=1/(n_b*Ldec_m*100*1e-27)
assert abs(sigma_crit_mb/26.849366723122218-1)<1e-13
def model(sigma_mb,free_fraction=1):
 ratio=sigma_mb*free_fraction/sigma_crit_mb
 return {'sigma_assumed_mb':sigma_mb,'free_fraction_assumed':free_fraction,
 'mfp_piN_km':(1/(n_b*sigma_mb*free_fraction*1e-27))/1e5,
 'P_decay_before_first_piN':1/(1+ratio)}
result={
 'status':'PASS_ORIGINAL_PDG_COMPAS_SOURCE_TYPED_R68_HADRON_FIRST_EVENT_CRITICAL_GATE',
 'p_pi_R68_GeV':math.sqrt(Epi**2-mpi**2)/1000,
 'source_rows':{k:len(v) for k,v in datasets.items()},
 'pi_charge_mean_DIRECT_340GeVc_mb':(plus340+minus340)/2,
 'pi_minus_N_INFERRED_640GeVc_mb':minus640,
 'pi_minus_p_DIRECT_360GeVc_nonelastic_mb':total360-elastic360,
 'n_baryon_number_per_cm3':n_b,'vacuum_pion_decay_length_km':Ldec_m/1000,
 'critical_total_sigma_mb_only_if_all_baryon_number_free':sigma_crit_mb,
 'modeled_scenarios':[model(24.85),model(25),model(27.1),model(25,.5)],
 'limitations':'Direct sigma(piN) at exact R68 718GeV is NOT read; 640 entry NUCLEAR INFERRED, not directly measured; f_free is unknown and bound nuclei separate; first encounter != pion disappearance; no pion cascade, neutrino flux or BBN result.'
}
print(json.dumps(result,indent=2,sort_keys=True))
