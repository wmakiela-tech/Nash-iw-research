// REC13 ROT015: original Badacz 097 published JSON source-only independent I1.
// Direct original BlackHawk v2.3 huge raw hadron table unavailable to this audit;
// BH per-primary values are taken from owner preserved analysis097.json, NOT independently rehashed.
// run: node rot015_source_i1.js analysis097.json H72_f1.json H73_f1.json H73_f2.json > source_i1.json
const fs=require("node:fs");
function audit(raw,mc){
 const names=["H72_f1","H73_f1","H73_f2"],sp={pipm:"211",Kpm:"321",K0L:"130",proton:"2212",neutron:"2112"},key=e=>Number(e.toPrecision(6)).toString();
 let cells=0,maxreplay=0,arms=[],nOK=0,rcOK=0,meanOK=0,evtOK=0,pi=[],all=[],losses=[],two=[];
 for(let k=0;k<3;k++){
  const arr=mc[k].energies, label=names[k];let M={arm:label,version:mc[k].version,sqrts_factor:mc[k].sqrt_s_factor,events_total:0,max_abs_log_ratio:{},max_eventwise_energy_error:0};
  for(let t=0;t<arr.length;t++){
   const e=arr[t],v=raw.bh[key(e.E)], ref=raw.ratios[label][key(e.E)];
   if(!v||!ref)throw Error("MISSING_ORIGINAL_SOURCE_BH");
   if(e.events===2000)nOK++;if(e.rc_read===0&&e.rc_run===0)rcOK++;if(Math.abs(e.Efinal_over_sqrts-1)<.001)meanOK++;if(e.max_abs_event_Eresidual<.001)evtOK++;
   M.events_total+=e.events;M.max_eventwise_energy_error=Math.max(M.max_eventwise_energy_error,e.max_abs_event_Eresidual);
   for(const [s,p] of Object.entries(sp)){
    const z=Math.log10(v[s]/e[p]);maxreplay=Math.max(maxreplay,Math.abs(z-ref[s]));cells++;
    M.max_abs_log_ratio[s]=Math.max(M.max_abs_log_ratio[s]||0,Math.abs(z));
   }
  }
  arms.push(M);
 }
 for(let t=0;t<mc[1].energies.length;t++){
  let e1=mc[1].energies[t],e2=mc[2].energies[t],lab=key(e1.E),b=raw.bh[lab].pipm;
  let l1=Math.log10(b/e1["211"]),l2=Math.log10(b/e2["211"]);
  let s1=e1.se_211/(e1["211"]*Math.LN10),s2=e2.se_211/(e2["211"]*Math.LN10);
  pi.push({E:lab,L1:l1,L2:l2,MC_sigma1:s1,MC_sigma2:s2,abs_margin:Math.abs(l2)-Math.abs(l1),separate_three_standard_error_robust:Math.abs(l1)+3*s1<Math.abs(l2)-3*s2});
  for(const s of Object.keys(sp)){const a1=Math.abs(raw.ratios.H73_f1[lab][s]),a2=Math.abs(raw.ratios.H73_f2[lab][s]);if(a1>a2)losses.push({E:lab,species:s,abs_L_f1:a1,abs_L_f2:a2})}
  const K=raw.ratios.H73_f1[lab].Kpm,Z=raw.ratios.H73_f1[lab].K0L;
  two.push({E:+lab,x:Math.log10(+lab/25),K,Z,mean:(K+Z)/2});
 }
 two.sort((a,b)=>a.E-b.E);
 const avg=x=>x.reduce((a,b)=>a+b,0)/x.length,mx=avg(two.map(z=>z.x)),my=avg(two.map(z=>z.mean)),sxy=two.reduce((s,z)=>s+(z.x-mx)*(z.mean-my),0),sxx=two.reduce((s,z)=>s+(z.x-mx)**2,0),slope=sxy/sxx,intercept=my-slope*mx;
 let residuals=two.map(z=>({E:z.E,K:z.K-(intercept+slope*z.x),K0L:z.Z-(intercept+slope*z.x)}));
 let max_resid=Math.max(...residuals.flatMap(z=>[Math.abs(z.K),Math.abs(z.K0L)])),loocv=[];
 for(let k=0;k<two.length;k++){
  let v=two.filter((_,i)=>i!==k),a=avg(v.map(z=>z.x)),b=avg(v.map(z=>z.mean)),s=v.reduce((o,z)=>o+(z.x-a)*(z.mean-b),0)/v.reduce((o,z)=>o+(z.x-a)**2,0),p=b-s*a+s*two[k].x;
  loocv.push({E:two[k].E,errK:two[k].K-p,errK0L:two[k].Z-p});
 }
 const Kvalues=two.flatMap(z=>[z.K,z.Z]),costConstant=(Math.max(...Kvalues)-Math.min(...Kvalues))/2;
 let endpoints=Object.entries(raw.endpoint).map(([E,z])=>({E:+E,max_nonzero_pi_node:z.max_nonzero_pi_node,E_half:z.E_half,endpoint_to_half:z.max_nonzero_pi_node/z.E_half,above_half:z.max_nonzero_pi_node>z.E_half,within_one_log_bin:z.max_nonzero_pi_node/z.E_half <=Math.exp(Math.log(1e11)/99)})).sort((a,b)=>a.E-b.E);
 const cvmax=Math.max(...loocv.flatMap(z=>[Math.abs(z.errK),Math.abs(z.errK0L)]));
 return {verification:{ratios_replayed:cells,ratio_max_error:maxreplay,energy_runs:18,exact_2000_event_runs:nOK,all_rc0_runs:rcOK,all_mean_energy_runs:meanOK,all_eventwise_energy_runs:evtOK},arms,pi:{rows:pi,all_six_three_MC_SE_inequality:pi.every(x=>x.separate_three_standard_error_robust),minimum_raw_abs_margin:Math.min(...pi.map(x=>x.abs_margin)),H73_f1_species_wins:30-losses.length,H73_f2_species_wins:losses.length,H73_f2_winner_details:losses},kaon_nuisance:{two_parameter_q:"q(E)=10^intercept*(E/25GeV)^slope",intercept,slope,q_at25:10**intercept,q_at100000:10**(intercept+slope*Math.log10(100000/25)),max_in_sample_dex:max_resid,strict_prereg_0p04_in_sample_fit:max_resid<.04,constant_best_minimax_residual_dex:costConstant,max_LOOCV_dex:cvmax,LOOCV_pred_not_certified:cvmax>.04,kaon_residuals:residuals,leave_one_energy_out:loocv},histogram:{bin_spacing_ln:Math.log(1e11)/99,bin_factor:Math.exp(Math.log(1e11)/99),four_of_six_above_Eprime_over2:endpoints.filter(z=>z.above_half).length,endpoints}};
}
if(require.main===module){
 const [a,...f]=process.argv.slice(2);if(!a||f.length!==3)throw Error("NEED_4_SOURCE_FILES");
 const data=JSON.parse(fs.readFileSync(a,"utf8"));const mc=f.map(x=>JSON.parse(fs.readFileSync(x,"utf8")));
 process.stdout.write(JSON.stringify(audit(data,mc),null,2)+"\n");
}
