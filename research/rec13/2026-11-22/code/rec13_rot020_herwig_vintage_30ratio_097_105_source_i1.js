// REC13 ROT020. Independent author code: replay original 097 BH aggregates vs 105 / 097 MC observations. NO native original BlackHawk table file independent raw read; NOT novel physics.
// node rec13_rot020_herwig_vintage_30ratio_i1.js analysis097.json H71_f1.json H72_f1.json H73_f1.json analysis105.json
const fs=require('node:fs');
function auditHistoric(raw, mc, owner105) {
 const names=["H71_f1","H72_f1","H73_f1"];
 const species={pipm:"211",Kpm:"321",K0L:"130",proton:"2212",neutron:"2112"};
 const byArm={},bySpecies={};let n=0;
 const data={};
 for(let j=0;j<3;j++){
  const arm=names[j],entries=[];
  for(const e of mc[j].energies){
   const key=Number(e.E.toPrecision(6)).toString(), bh=raw.bh[key];
   if(!bh)throw Error("Missing pinned historic owner aggregate "+key);
   const by={};
   for (const [name,pdg] of Object.entries(species)){
    const log=Math.log10(bh[name]/e[pdg]);
    if(!Number.isFinite(log))throw Error("bad input");
    by[name]={log,zMC:log/((e["se_"+pdg]/e[pdg])/Math.LN10),seLog:(e["se_"+pdg]/e[pdg])/Math.LN10};
    if(j===0&&owner105.ratios[key]&&Math.abs(log-owner105.ratios[key][name])>2e-15)throw Error("105 internal mismatch");
    n++;
   }
   entries.push({E:Number(key),by,rc:e.rc_read===0&&e.rc_run===0,events:e.events,eventBalance:e.max_abs_event_Eresidual});
  }
  let vals=entries.flatMap(e=>Object.values(e.by).map(x=>x.log));
  byArm[arm]={n:vals.length, rmsDex:Math.sqrt(vals.reduce((s,x)=>s+x*x,0)/vals.length),maxAbsDex:Math.max(...vals.map(Math.abs)),meanAbsDex:vals.reduce((s,x)=>s+Math.abs(x),0)/vals.length,countWithin0p01Dex:vals.filter(x=>Math.abs(x)<.01).length,countWithin0p04Dex:vals.filter(x=>Math.abs(x)<.04).length, maxAbsZmc:Math.max(...entries.flatMap(e=>Object.values(e.by).map(x=>Math.abs(x.zMC)))),minEvents:Math.min(...entries.map(x=>x.events)),maxEnergyResidual:Math.max(...entries.map(x=>x.eventBalance)),allRcPass:entries.every(x=>x.rc)};
  data[arm]=entries;
 }
 for(const name of Object.keys(species)){
   bySpecies[name]=Object.fromEntries(names.map(arm=>{
      const d=data[arm].map(x=>x.by[name].log);
      return [arm,{maxAbs:Math.max(...d.map(Math.abs)),rms:Math.sqrt(d.reduce((s,x)=>s+x*x,0)/d.length)}]
   }));
 }
 const h71=byArm.H71_f1,h72=byArm.H72_f1,h73=byArm.H73_f1;
 const res={
  original_sources:"Three pinned Badacz original complete MC JSONs (H71 2026-11-22 owner 105, H72/H73 2026-11-22 owner 097) and owner's 2019 BH historic table 30 owner-extracted aggregates in analysis097; native archive not independently hashed.",
  exact_ratio_check_against_105:true,
  rowsCompared_per_arm:30,
  arms:byArm,bySpecies,
  sourceComparisonRatios:{rms_H72_div_H71:h72.rmsDex/h71.rmsDex,rms_H73_div_H71:h73.rmsDex/h71.rmsDex},
  negative:{historical_original_binary_version_not_identified:true,ratio_agreement_not_an_independent_original_BH_table_rehash:true,old_BH_extracted_counts_are_owner_aggregate_not_new_source:true,one_quark_six_energies_not_ten_channels_hypothesis:true,MC_standard_errors_ignore_historic_100k_event_table_uncertainty:true,no_proven_nonzero_downstream_physics_impact:true},
  allPass:h71.n===30&&h71.maxAbsDex<.01&&h71.allRcPass&&h71.minEvents===10000
 };
 if(!res.allPass)throw Error("GATE FAIL");
 return res
}
if(require.main===module){const v=process.argv.slice(2);if(v.length!==5)throw Error('5 pinned input paths required');const a=v.map(x=>JSON.parse(fs.readFileSync(x,'utf8')));console.log(JSON.stringify(auditHistoric(a[0],a.slice(1,4),a[4]),null,2));}
