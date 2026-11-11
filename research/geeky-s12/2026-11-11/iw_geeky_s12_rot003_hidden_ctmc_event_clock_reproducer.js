#!/usr/bin/env node
"use strict";
// Public source-local exact integer-scaled finite-CTMC checker.
// Base q=1/n, p=1-q, s=1, lambda=1/2; generator multiplied by 4n.
// This is a mathematical model, NOT physical rate/thermal instrumentation.
function reproduce() {
  const cases=[];
  function check(ok,desc){if(!ok)throw Error("ROT003 FAIL: "+desc);}
  for(const n of [2,4,16,1000,1000000]){
    // Every rate below is multiplied by 4*n (integer arithmetic).
    const N=6;
    const q=Array.from({length:N},()=>Array(N).fill(0));
    const idx=(x,i)=>3*x+((i+3)%3);
    const cw=4*(n-1), ccw=4, cross=n;
    for(let x=0;x<2;x++)for(let i=0;i<3;i++){
      const a=idx(x,i);
      q[a][idx(x,i+1)]+=cw;
      q[a][idx(x,i-1)]+=ccw;
      q[a][idx(1-x,i)]+=cross;
      q[a][idx(1-x,i+(x===0?1:-1))]+=cross;
      q[a][a]=-(cw+ccw+2*cross);
    }
    check(q.every((row,i)=>row.reduce((v,w)=>v+w,0)===0),"row sums");
    check(q.every((row)=>row.every(Number.isSafeInteger)),"integer coefficients");
    for(let j=0;j<N;j++)check(q.reduce((s,row)=>s+row[j],0)===0,"uniform stationary");
    check(q.every((row,i)=>row[i]===-6*n),"identical microscopic exit clocks");
    for(let x=0;x<2;x++)for(let i=0;i<3;i++){
      const a=idx(x,i);
      check(q[a].reduce((s,v,j)=>s+(Math.floor(j/3)===(1-x)?v:0),0)===2*n,"strong lumpability");
      check(q[a][idx(1-x,i+(x===0?1:-1))]===n,"genuinely cross-linked flip");
    }
    const edges=[];
    for(let x=0;x<2;x++)for(let i=0;i<3;i++){
      const a=idx(x,i),b=idx(x,i+1);
      // (a,b) is one directed orientation per distinct unordered hidden edge.
      edges.push({type:"hidden",a,b,fwd:q[a][b],rev:q[b][a]});
    }
    for(let i=0;i<3;i++){
      edges.push({type:"visible_same",a:idx(0,i),b:idx(1,i),fwd:n,rev:n});
      edges.push({type:"visible_shift",a:idx(0,i),b:idx(1,i+1),fwd:n,rev:n});
    }
    check(edges.length===12,"12 undirected edges");
    check(edges.filter(e=>e.type==="hidden").every(e=>e.fwd+e.rev===4*n),"exact fixed hidden edge traffic");
    check(edges.filter(e=>e.type!=="hidden").every(e=>e.fwd+e.rev===2*n),"exact fixed cross traffic");
    const sumStationaryTraffic=edges.reduce((t,e)=>t+(e.fwd+e.rev)/(24*n),0);
    check(Math.abs(sumStationaryTraffic-1.5)<1e-12,"total traffic fixed");
    const sigma=(n-2)/n*Math.log(n-1);
    const edgeSigma=edges.reduce((t,e)=>t+(e.fwd-e.rev)/(24*n)*Math.log(e.fwd/e.rev),0);
    check(Math.abs(sigma-edgeSigma)<1e-12,"edge entropy decomposition");
    cases.push({reverse_fraction:"1/"+n,hidden_forward_rate:(n-1)/n,hidden_reverse_rate:1/n,
      macro_flip_rate:0.5,hidden_event_rate:1,total_micro_event_rate:1.5,
      microstationary:"1/6 per state",every_hidden_undirected_edge_traffic:"1/6",
      every_cross_undirected_edge_traffic:"1/12",total_traffic:sumStationaryTraffic,
      ep_rate:sigma,ep_rate_from_edges:edgeSigma,checks:"PASS"});
  }
  check(cases[0].ep_rate===0,"equilibrium endpoint");
  check(cases.at(-1).ep_rate>10,"unbounded direction");
  return {
    artifact_id:"IW_GEEKY_S12_ROT003_INTERACTING_HIDDEN_CTMC_EVENT_CLOCK_EP_NONIDENTIFIABILITY_001_20261111",
    source_scope:"ABSTRACT_EXACT_6_STATE_CTMC_ONLY",model:"two visible x, three hidden i; fixed clock s=1 lambda=1/2; hidden clockwise p, counterclockwise q, p+q=1; visible flips couple hidden index via same and shifted edges",
    observation_law:"For any initial microstate, macro flip epochs are Poisson(1/2), hidden (unlabelled) epochs Poisson(1), independent; full visible X path and all microscopic event timestamps independent of p/q",
    microscopic_traffic:"all six hidden edge traffic=1/6, all six cross edge traffic=1/12, total 3/2, stationary micro law uniform",
    entropy_production:"(p-q)*log(p/q) = (n-2)/n*log(n-1) as q=1/n; range [0,infinity) at fixed observable law and fixed undirected micro traffic",
    cases,verdict:"PASS_EXACT_INTEGER_SCALED_GENERATOR_AND_ANALYTIC_EP_CHECK"
  };
}
console.log(JSON.stringify(reproduce(),null,2));
