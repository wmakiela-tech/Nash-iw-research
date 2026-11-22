// IW/NASH REC13 ROT016 read-only exact original CSV vs owner-extracted Wu-Xu scan contours.
// Node.js source-only. No JLD2/raw Wu-Xu scan execution; no paper Figure5 digitization.
// Usage: node rec13_rot016_gap006_source_i1.js Carr.csv Kohri.csv Keith.csv eks1_out.json > out.json
const fs=require("node:fs");
function evalAudit(csvTexts, owner){
const gamma=1/(3*Math.sqrt(3)),corr=-.5*Math.log10(gamma);
const names=["Carr2020gox","Kohri1999ex","Keith2020jww"];
const arrays=csvTexts.map(s=>s.trim().split("\n").map(line=>line.split(",").map(x=>Number(x.trim()))).filter(x=>x.length===2&&x.every(Number.isFinite)&&x.every(v=>v>0)));
function poly(pts,M){let z=Math.log10(M),ret=[];for(let i=1;i<pts.length;i++){let [m0,y0]=pts[i-1],[m1,y1]=pts[i],a=Math.log10(m0),b=Math.log10(m1),v0=Math.log10(y0),v1=Math.log10(y1);if(Math.min(a,b)<=z&&z<=Math.max(a,b)){if(a===b){ret.push(v0,v1);}else ret.push(v0+(z-a)*(v1-v0)/(b-a));}}return ret.length?Math.min(...ret):null;}
let out=[],maxOutputError=0;
for(let row of owner.binding_map){
 let m=row.M_g,v={Carr2020gox:poly(arrays[0],m),Kohri1999ex:poly(arrays[1],m),Keith2020jww:poly(arrays[2],m)};
 if(v.Carr2020gox!==null)v.Carr2020gox+=corr;
 if(v.Keith2020jww!==null)v.Keith2020jww+=corr;
 const e=owner.verdicts_j22_j62[String(row.j)]?.lit_values_all;
 if(e) for(let [n,x] of Object.entries(v))if(x!==null&&e[n]!==null&&e[n]!==undefined)maxOutputError=Math.max(maxOutputError,Math.abs(x-e[n]));
 out.push({j:row.j,m,rowBound:row.wuxu_lb,lit:v,marginCarr:v.Carr2020gox===null?null:v.Carr2020gox-row.wuxu_lb});
}
const overlap=out.filter(x=>x.marginCarr!==null),window=overlap.filter(x=>x.m>=3.2e9&&x.m<=7.4e9);
const y=.251;const Xcode=y/(2+y),Xv3=y/2,Xv1=y/(2*(1+y));
const minMargin=Math.min(...overlap.map(x=>x.marginCarr)),maxMargin=Math.max(...overlap.map(x=>x.marginCarr));
const j22=out.find(x=>x.j===22),j62=out.find(x=>x.j===62);
let sourceD=Object.fromEntries([j22,j62].map(row=>[row.j,{mass_g:row.m,WuXu_owner_scan_beta:row.rowBound,literature_logbeta:row.lit,Carr_minus_WuXu:row.marginCarr,Kohri_minus_WuXu:row.lit.Kohri1999ex-row.rowBound,Keith_minus_WuXu:row.lit.Keith2020jww-row.rowBound}]));
const status= {source_type:"Original owner WuXu vintage CSV polyline + original EKS1 extracted WuXu thresholds. No independent JLD2 scan execution.", gamma,corr_log10beta_prime_to_beta:corr,source_rows:arrays.map(x=>x.length),wx_source_owner_roots:owner.binding_map.length,overlap_Carr_count:overlap.length,Carr_stronger_under_correct_axis:overlap.filter(z=>z.marginCarr<0).length,margin_Carr_minus_Wuxu_min:minMargin,margin_Carr_minus_Wuxu_max:maxMargin,window_3p2_to_7p4_Carr_minus_WuXu_min:Math.min(...window.map(x=>x.marginCarr)),window_3p2_to_7p4_Carr_minus_WuXu_max:Math.max(...window.map(x=>x.marginCarr)),counterfactual_wrong_inverse_gamma_min_margin:minMargin-2*corr,originalEKS1_2cell_values_max_diff:maxOutputError,j22_j62:sourceD,helium_postprocess_mapping:{Y_target:y,Xcode,Xarticle_v1v2:Xv1,Xarticle_v3:Xv3,Xv3_minus_Xcode:Xv3-Xcode,published_v3_Y_if_code_archiveY_is_0p251:2*Xcode,needed_archived_codeY_to_reach_published_v3_Y_0p251:2*Xv3/(1-Xv3),source_code_Y_if_X_is_published_v3_target:2*Xv3/(1-Xv3)},guards:{original_Carr_fails_G0:overlap.every(x=>x.marginCarr>0),wrong_inverse_gamma_still_no_Carr_binding:minMargin>2*corr,source_formula_mismatch_nonzero:Math.abs(Xv3-Xcode)>.01,all_three_curves_nonempty:arrays.every(a=>a.length>40),no_ScanningJLD2_raw_verified:true}};
if(!status.guards.original_Carr_fails_G0||!status.guards.wrong_inverse_gamma_still_no_Carr_binding||maxOutputError>1e-11)throw Error("SCIENCE_FAIL_CLOSED");
return status;
}
if(require.main===module){const v=process.argv.slice(2);if(v.length!==4)throw Error("NEED_FOUR_PINNED_SOURCE_PATHS");console.log(JSON.stringify(evalAudit(v.slice(0,3).map(p=>fs.readFileSync(p,"utf8")),JSON.parse(fs.readFileSync(v[3],"utf8"))),null,2));}
