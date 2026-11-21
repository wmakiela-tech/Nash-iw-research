# PREREG_085 / GAP-005: hadron-yield table generator for the Wu-Xu code (arXiv:2509.05618, repo d395183).
# Reproduces the authors' notebook valid_hadrons_from_BlackHawk.ipynb cells 12-13 (mass grid, BlackHawk_inst call,
# trapezoid in log E over the secondary-energy grid, output format), with the hadronization generator and the
# primary-energy window as arguments. Uses the authors' own tool scripts (read-only include) and a BlackHawk v2.3
# build (tarball SHA256 dd148349...a7 = authors' Artifacts.toml) with the authors' exit-code hack overlaid.
#
# Usage: julia gen_hadron_rows_087.jl <wuxu_src> <blackhawk_dir> <out_file> <hadronization_choice> <Emin_GeV> <Emax_GeV> <E_number> <tag> <m_min_g> <m_max_g> <n_m>
# (PREREG_087 diagnostic variant of gen_hadron_table_085.jl: same BlackHawk call and integration, custom mass grid)
#   hadronization_choice: 0 = PYTHIA (BBN epoch, authors' choice), 1 = HERWIG (BBN epoch)
# Output columns (authors' header and units): m_PBH [GeV], dN/dt for pi+-, K+-, K0L, p, n [GeV].
# Exits nonzero on any BlackHawk failure or non-finite/negative yield.

const SRC = ARGS[1]
const BlackHawk_directory = ARGS[2]
const BlackHawk_results_directory = joinpath(BlackHawk_directory, "results")
const OUT = ARGS[3]
const HCHOICE = parse(Int, ARGS[4])
const EMIN = parse(Float64, ARGS[5])
const EMAX = parse(Float64, ARGS[6])
const ENUM = parse(Int, ARGS[7])
const TAG = ARGS[8]
const MMIN = parse(Float64, ARGS[9]); const MMAX = parse(Float64, ARGS[10]); const NM = parse(Int, ARGS[11])

using DelimitedFiles
using Statistics
include(joinpath(SRC, "tool_script-parameters.jl"))        # defines EU = GeV, NU = NaturalUnit(EU)
include(joinpath(SRC, "tool_script-geomspace.jl"))
include(joinpath(SRC, "tool_script-BlackHawk_extension.jl"))

@assert HCHOICE in (0, 1)
@assert !isfile(OUT) "REFUSE_OVERWRITE $(OUT)"

m_PBH_list = geomspace(MMIN, MMAX, NM) .* NU.g
species = ["pipm", "Kpm", "K0L", "proton", "neutron"]
Y = zeros(Float64, length(m_PBH_list), length(species))

trap(E, f) = begin
    integrand = E .* f
    h = mean(log.(E[begin+1:end]) .- log.(E[begin:end-1]))
    (h / 2) * (2 * sum(integrand) - (first(integrand) + last(integrand)))
end

for (ii, m_PBH) in enumerate(m_PBH_list)
    params = BlackHawkParameters()
    name = "iw087_$(TAG)_$(lpad(ii, 3, '0'))"
    rdir = joinpath(BlackHawk_results_directory, name)
    rm(rdir; force=true, recursive=true)
    set_BlackHawk_name!(params, name)
    set_BlackHawk_mass!(params, m_PBH; NU=NU)
    set_BlackHawk_energy_spectrum!(params, GeV(EMIN), GeV(EMAX), ENUM)
    close_BlackHawk_dark_matter!(params)
    params.hadronization_choice = HCHOICE           # authors: set_BlackHawk_BBN! sets 0
    run_BlackHawk_inst(params)                       # run() throws on nonzero exit (authors' hack: 0 = success)
    _, sec = read_BlackHawk_instantaneous_spectra(rdir)
    for (k, s) in enumerate(species)
        Y[ii, k] = trap(sec["energy"], sec[s])
    end
    rm(rdir; force=true, recursive=true)
end

@assert all(isfinite, Y) && all(Y .>= 0) "NONFINITE_OR_NEGATIVE"
open(OUT, "w+") do io
    write(io, "m_PBH [GeV]\tcharged_pion_dN_over_dt [GeV]\tcharged_kaon_dN_over_dt [GeV]\tkaon_zero_long_dN_over_dt [GeV]\tproton_dN_over_dt [GeV]\tneutron_dN_over_dt [GeV]\n")
    writedlm(io, hcat(EUval.(GeV, m_PBH_list), [EUval.(GeV, Y[:, k] ./ NU.s) for k in 1:length(species)]...))
end
println("IW087_ROWS_DONE $(TAG) rows=$(length(m_PBH_list)) hchoice=$(HCHOICE) E=[$(EMIN),$(EMAX)]x$(ENUM)")
