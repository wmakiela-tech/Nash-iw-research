(* Mech-S8 ROT017 source-pinned all100 Wu-Xu hadron-rate check.
   Original author commit d395183674cace6c9906a8911bdeb7234ba4040d (v2).
   Wolfram Language internet needed; NO native BlackHawk/PYTHIA/Julia run.
   All100 LOO reports only INTRA-TABLE neighbor consistency.
   Anchored k-window power comparison is conditional extrapolation.
 *)
Module[{url,f,data,x,names,logs,ks={2,3,4,5,8,12},measure,summary},
 url="https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/"<>
    "d395183674cace6c9906a8911bdeb7234ba4040d/"<>
    "arXiv-2509.05618/data/out/hadrons_from_PBH.dat";
 f=URLDownload[url];
 If[FileHash[f,"SHA256","HexString"]=!=
    "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df",
    Return[<|"status"->"FAIL_ORIGINAL_SOURCE_SHA"|>]
 ];
 data=N[ToExpression[StringReplace[StringSplit[#],"e"->"*^"]]&/@
    Rest[Import[f,"Lines"]]];
 If[Length[data]=!=100,Return[<|"status"->"FAIL_EXPECTED_100_ROWS"|>]];
 x=Log[data[[All,1]]/First[data][[1]]];
 names={"charged_pion","charged_kaon","K0L","proton_group","neutron_group"};
 logs=Table[Log[data[[All,j]]],{j,2,6}];
 measure[y_]:=Module[{eps,mid,slopes,local,p2},
   eps=Table[Exp[y[[i-1]]+(y[[i+1]]-y[[i-1]])*
       (x[[i]]-x[[i-1]])/(x[[i+1]]-x[[i-1]])-y[[i]]]-1,{i,2,99}];
   mid=Table[Exp[(y[[i-1]]+y[[i+1]])/2-y[[i]]]-1,{i,2,99}];
   local=Function[k,With[{xx=Take[x,k],yy=Take[y,k]},
     -(Total[(xx-Mean[xx])*(yy-Mean[yy])]/Total[(xx-Mean[xx])^2])]];
   slopes=local/@ks;
   p2=First[slopes];
   <|"pair_slope"->p2,"window_slopes"->AssociationThread[ToString/@ks,slopes],
     "loo_max_abs_pct"->100 Max[Abs[eps]],
     "loo_median_abs_pct"->100 Median[Abs[eps]],
     "loo_rms_pct"->100 Sqrt[Mean[eps^2]],
     "loo_peak_row_1based"->Ordering[Abs[eps],-1][[1]]+1,
     "max_geometric_midpoint_diff_percentage_points"->100 Max[Abs[eps-mid]],
     "anchored_at_first_row_ratio_3e8_vs_2pt"->AssociationThread[ToString/@ks,0.3^(-(slopes-p2))],
     "anchored_at_first_row_ratio_1e8_vs_2pt"->AssociationThread[ToString/@ks,0.1^(-(slopes-p2))]|>
 ];
 summary=<|"status"->"PASS_ORIGINAL_WUXU_100_ROWS_WOLFRAM_SOURCE_ONLY",
    "source_sha256"->FileHash[f,"SHA256","HexString"],
    "rows"->Length[data],"interior_loo_per_species"->98,
    "peak_row_mass_g"->data[[86,1]]/data[[1,1]]*10^9,
    "species"->AssociationThread[names,measure/@logs],
    "claim_ceiling"->"LOO_TABLE_SELF_CONSISTENCY_ONLY/NO_TRUE_BLACKHAWK_GREYBODY/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN"|>;
 summary
]
