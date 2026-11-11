(* Mech-S8 ROT018 original Wu-Xu 100-row 5-species rolling masked-source audit.
   Uses ORIG author git v2 d395183, raw file SHA256 exact check.
   Source Git blob 06d0883a27b108692720422294ba2baacd381a64.
   This is an empirical leave-known-data-out test, NOT a physical low-mass validation.
   Requires Wolfram Language with URLDownload, internet connection. *)
Module[{url, file, rows, data, xx, yy, hs = {1,3,6,12,28},
  labels={"pi_aggregate","Kpm_aggregate","K0L","p_aggregate","n_aggregate"},
  step, check, stats, result, dataSHA},
  url="https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/"<>
     "d395183674cace6c9906a8911bdeb7234ba4040d/"<>
     "arXiv-2509.05618/data/out/hadrons_from_PBH.dat";
  file=URLDownload[url];
  dataSHA=FileHash[file,"SHA256","HexString"];
  If[dataSHA=!= "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df",
    Return[<|"status"->"SOURCE_SHA256_FAIL","observed_sha256"->dataSHA|>]];
  rows=Rest[Import[file,"Lines"]];
  data=N[ToExpression[StringReplace[StringSplit[#],"e"->"*^"]]&/@rows];
  If[Dimensions[data]=!={100,6},Return[<|"status"->"SOURCE_DIMENSIONS_FAIL"|>]];
  xx=Log[data[[All,1]]];
  yy=Table[Log[data[[All,col]]],{col,2,6}];
  step[y_,h_]:=Table[
    Exp[y[[i]]+(y[[i+1]]-y[[i]])*(xx[[i-h]]-xx[[i]])/
      (xx[[i+1]]-xx[[i]])-y[[i-h]]]-1,
    {i,h+1,99}];
  stats[y_,h_]:=Module[{e=step[y,h]},
    <|"count"->Length[e],
      "median_abs_pct"->100 Median[Abs[e]],
      "max_abs_pct"->100 Max[Abs[e]],
      "first_anchor_signed_pct"->100 First[e],
      "max_target_row_1based"->First[Ordering[Abs[e],-1]]|>];
  result=<|"status"->"PASS_ORIGINAL_AUTHOR_FULL100_HORIZON_K2",
    "sha256_raw_source"->dataSHA,
    "source_rows"->Length[data],
    "mass_ratio_for_28_steps"->Exp[28 Mean[Differences[xx]]],
    "metric"->AssociationThread[labels,
      Table[AssociationThread[ToString/@hs,
        stats[yy[[i]],#]&/@hs],{i,1,5}]],
    "ceiling"->"ORIGINAL_TABLE_POSTHOC_BACKTEST_ONLY / NO_LOW_MASS_PHYSICAL_BOUND / NO_CANON / NO_EXEC_SIGN"|>;
  Print[result["status"]]; result
]
