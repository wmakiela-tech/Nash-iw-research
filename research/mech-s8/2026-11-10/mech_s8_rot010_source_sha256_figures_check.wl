(* IW_MECH_S8 ROT010, preserved 2026-11-10.
   Public original arXiv v2/v3 source custody and author-pinned GitHub plot.
   Reproduces ONLY source-byte SHA-256, TeX token and PDF byte identity checks.
   No BBN, Julia, BlackHawk, or historic Figure 5 execution.
   Requires Wolfram Language with internet-enabled URLDownload and ExtractArchive.
   Never substitute Hash[Import[path,"Byte"],...] for FileHash[path,...]. *)

Module[{v2, v3, arch, root, tex, fig, pdfs, source, figures, raw, record, expected, result, ok},
  source = <||>; figures = <||>;
  Do[
    arch = URLDownload["https://arxiv.org/src/2509.05618" <> v];
    root = CreateDirectory[];
    ExtractArchive[arch, root];
    tex = FileNameJoin[{root, "main.tex"}];
    fig = FileNameJoin[{root, "fig", "Y_P.pdf"}];
    pdfs = FileNames["*.pdf", FileNameJoin[{root, "fig"}]];
    source[v] = <|
      "archive_size" -> FileByteCount[arch],
      "archive_sha256" -> FileHash[arch, "SHA256", "HexString"],
      "tex_size" -> FileByteCount[tex],
      "tex_sha256" -> FileHash[tex, "SHA256", "HexString"],
      "fig5_size" -> FileByteCount[fig],
      "fig5_sha256" -> FileHash[fig, "SHA256", "HexString"],
      "tex_prints_plus_mass_bilinear" -> StringContainsQ[Import[tex, "Text"],
        "{}+\\left(g_{V}^{2}-g_{A}^{2}\\right)m_{n}m_{p}"],
      "tex_prints_GF2_over16" -> StringContainsQ[Import[tex, "Text"],
        "\\frac{1}{2^{4}}\\cdot G_{F}^{2}"]
    |>;
    figures[v] = Association@Table[
      FileNameTake[p] -> FileHash[p, "SHA256", "HexString"], {p, pdfs}],
    {v, {"v2", "v3"}}
  ];
  raw = URLDownload[
    "https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/" <>
    "d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/plots/Y_P.pdf"];
  record = <|"source_versions" -> source,
    "figure_names" -> Sort[Keys[figures["v2"]]],
    "figure_count" -> Length[Keys[figures["v2"]]],
    "seven_figure_files_identical" -> (figures["v2"] === figures["v3"]),
    "github_fig5_bytes" -> FileByteCount[raw],
    "github_fig5_sha256" -> FileHash[raw, "SHA256", "HexString"],
    "arxiv_vs_author_git_fig5_bytes_identical" ->
      (source["v3"]["fig5_sha256"] === FileHash[raw, "SHA256", "HexString"])|>;
  expected = <|
    "v2_archive" -> "9994c81d520fbaff551e91bed88b8631b6a0bb029c28c72ee1650747716054aa",
    "v3_archive" -> "60627ec16d199b8dc1a81d82341d916d6f281e9e913d2f71506b5e7dbdbcb7e6",
    "v2_tex" -> "1eae342f580c70519ba858c13900b0f3c89a9e35b241f15fbc48b870e85e21b3",
    "v3_tex" -> "2d5db9ce9e08718fa1f26d25f15e56b32b94f9d14b3e40a834915df8b2bccd70",
    "arxiv_fig5" -> "453c2842636a2e4ca3b36cb6ee22b854fac943f0069f85debf2ec988b96f7fa9",
    "github_fig5" -> "95f5249c880ef8411361f9cb1d06300c3042996f5a6c78b72f55b72ca74169b4"|>;
  ok = And[
    source["v2"]["archive_sha256"] === expected["v2_archive"],
    source["v3"]["archive_sha256"] === expected["v3_archive"],
    source["v2"]["tex_sha256"] === expected["v2_tex"],
    source["v3"]["tex_sha256"] === expected["v3_tex"],
    source["v2"]["fig5_sha256"] === expected["arxiv_fig5"],
    source["v3"]["fig5_sha256"] === expected["arxiv_fig5"],
    record["github_fig5_sha256"] === expected["github_fig5"],
    record["figure_count"] === 7,
    record["seven_figure_files_identical"],
    ! record["arxiv_vs_author_git_fig5_bytes_identical"],
    source["v3"]["tex_prints_plus_mass_bilinear"],
    source["v3"]["tex_prints_GF2_over16"]
  ];
  result = <|"verification" -> If[ok, "PASS", "FAIL"],
     "claims" -> "SOURCE_BYTES_ONLY/FIG5_HISTORICAL_PRODUCER_OPEN/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN",
     "observations" -> record|>;
  Export["mech_s8_rot010_verified_source_result.json", result, "RawJSON"];
  Print[result["verification"]];
  result
]
