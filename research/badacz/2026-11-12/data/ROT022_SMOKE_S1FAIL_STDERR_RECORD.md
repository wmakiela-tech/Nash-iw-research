---
artifact_id: IW_BADACZ_ROT022_SMOKE_S1FAIL_STDERR_RECORD_20261112
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-12
document_type: RUN_RECORD
claim_ceiling: PROVENANCE_RECORD / DRIVER_INTERFACE_FAILURE / NO_SCIENCE_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# Dosłowne stderr: smoke ROT022 przy pliku punktów właściciela (PREREG_062, S1)

- **Wywołanie.** Sterownik `research/mech-s8/2026-11-12/mech_s8_rot022_C1_C4_calibrated_y2x_native_pilot_UNEXECUTED.jl` (blob `0223f0c5`) z plikiem punktów `research/mech-s8/2026-11-12/mech_s8_rot022_phaseA_smoke_v001.dat` (blob `6d5f3262`). Zmienne: `MECH_ROT022_T1_MEV=0.099688851247`, tolerancja domyślna.
- **Wynik.** Wszystkie cztery warianty (`native`, `p13`, `native_sym`, `p13_sym`) zakończyły się kodem 1 po ~2 s. Ich stderr są identyczne bajt w bajt (SHA-256 `69f5cd7f969a7a79d37844af739adfc4806c3a2cb4dcdd7efc141f91b80cc804`).
- **Przyczyna.** Bramka blobów autorów (linie 53–56) przeszła. Linia 66 parsuje każdą niepustą linię jako `j log10beta`, a plik punktów zawiera 3 linie komentarza `#`.

```text
ERROR: LoadError: ArgumentError: invalid base 10 digit '#' in "#"
Stacktrace:
  [1] tryparse_internal(::Type{Int64}, s::SubString{String}, startpos::Int64, endpos::Int64, base_::Int64, raise::Bool)
    @ Base ./parse.jl:143
  [2] parse(::Type{Int64}, s::SubString{String}; base::Nothing)
    @ Base ./parse.jl:254
  [3] parse
    @ ./parse.jl:253 [inlined]
  [4] #3
    @ ./none:-1 [inlined]
  [5] iterate
    @ ./generator.jl:48 [inlined]
  [6] grow_to!(dest::Vector{Tuple{Int64, Float64}}, itr::Base.Generator{Base.Iterators.Filter{var"#5#6", Vector{String}}, var"#3#4"})
    @ Base ./array.jl:863
  [7] collect(itr::Base.Generator{Base.Iterators.Filter{var"#5#6", Vector{String}}, var"#3#4"})
    @ Base ./array.jl:787
  [8] top-level scope
    @ /home/claude/nash-iw-research/research/mech-s8/2026-11-12/mech_s8_rot022_C1_C4_calibrated_y2x_native_pilot_UNEXECUTED.jl:66
  [9] include(mod::Module, _path::String)
    @ Base ./Base.jl:306
 [10] exec_options(opts::Base.JLOptions)
    @ Base ./client.jl:317
 [11] _start()
    @ Base ./client.jl:550
in expression starting at /home/claude/nash-iw-research/research/mech-s8/2026-11-12/mech_s8_rot022_C1_C4_calibrated_y2x_native_pilot_UNEXECUTED.jl:66
```
