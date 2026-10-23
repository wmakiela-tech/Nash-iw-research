#!/usr/bin/env python3
"""IW/NASH DAX-S7 rotation 49 -- independent Wu-Xu background-equation port.

This script is NOT the original Julia executor. It reconstructs the autonomous
(t, rho_SM, M_PBH) background subsystem of the public main-scan.jl and its
source interpolation tables. Hadrons and neutron abundance do not backreact on
that subsystem in the source code.

Usage:
  python IW_DAX_S7_ROTATION_49_SOURCE_BACKGROUND_TRIPLE_CROSSING_20261024.py --data-dir /path/to/arXiv-2509.05618/data/ext
  python IW_DAX_S7_ROTATION_49_SOURCE_BACKGROUND_TRIPLE_CROSSING_20261024.py --selftest

Source version should be pinned to file blobs in accompanying report.
No claims about full source Julia integration, physical Yp or PBH bounds.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
import urllib.request
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

T_NUC = 0.07818527068831995  # MeV; Wu-Xu source
MP_G = 2.176434e-5  # conventional Planck mass, g
TPL_S = 5.391247e-44  # Planck time, seconds
GAMMA = 1 / (3 * math.sqrt(3))
# CODATA-based H(T)=HCOEFF sqrt(g_rho) T_MeV^2 / second.
HCOEFF = 0.20658852676118475
T_FLOOR = 0.01  # MeV; inverse-interpolator grid starts here
T_CEILING = 1e6  # MeV; inverse-interpolator grid ends here
LOG_T_NUC = math.log(T_NUC)
SOURCE_FILES = {
    'N_around_m_e.csv': '93f2494f026c5d0587ea40fe08bb938dd9d01fa8',
    'N_s_from_PDG2024.csv': '33aceb876fc36cb2486d36c690e6401d85d76b46',
    'N_rho_OVER_N_s_from_PDG2024.csv': '28b0c13563d7b3bdeaee191a3a981197345d05b8',
}
SOURCE_BASE_URL = ('https://raw.githubusercontent.com/Fenyutanchan/'
                   'Primordial-Black-Hole/master/arXiv-2509.05618/data/ext/')


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def fetch_source(dest: Path) -> None:
    """Explicit opt-in download; exact expected Git blob hashes are required."""
    dest.mkdir(parents=True, exist_ok=True)
    for name, expected in SOURCE_FILES.items():
        path = dest / name
        if path.exists() and git_blob_sha(path.read_bytes()) == expected:
            print('SOURCE OK', name, expected)
            continue
        with urllib.request.urlopen(SOURCE_BASE_URL + name, timeout=30) as response:
            raw = response.read()
        observed = git_blob_sha(raw)
        if observed != expected:
            raise RuntimeError(f'Source drift for {name}: expected {expected}, observed {observed}')
        path.write_bytes(raw)
        print('SOURCE VERIFIED', name, observed)


def log_interp(nodes: np.ndarray, x: float, extrap: str) -> tuple[float, float]:
    """Piecewise linear log-T interpolation, value and d(value)/dlnT."""
    ax, vals = nodes[:, 0], nodes[:, 1]
    j = int(np.searchsorted(ax, x, side='right')) - 1
    if j < 0:
        if extrap == 'constant':
            return float(vals[0]), 0.0
        j = 0
    if j >= len(ax) - 1:
        if extrap == 'constant':
            return float(vals[-1]), 0.0
        j = len(ax) - 2
    d = float((vals[j + 1] - vals[j]) / (ax[j + 1] - ax[j]))
    return float(vals[j] + d * (x - ax[j])), d


class WuXuThermodynamics:
    def __init__(self, data_dir: Path):
        raw = np.loadtxt(data_dir / 'N_around_m_e.csv', delimiter=',')
        sns = np.loadtxt(data_dir / 'N_s_from_PDG2024.csv', delimiter=',')
        rat = np.loadtxt(data_dir / 'N_rho_OVER_N_s_from_PDG2024.csv', delimiter=',')
        self.low_rho = np.column_stack((np.log(raw[:, 0]), raw[:, 1]))
        self.low_s = np.column_stack((np.log(raw[:, 0]), raw[:, 2]))
        self.high_s = np.column_stack((np.log(sns[:, 0]), sns[:, 1]))
        self.high_ratio = np.column_stack((np.log(rat[:, 0]), rat[:, 1]))
        self.g_top = float(sns[-1, 1] * rat[-1, 1])
        self.n_bh = (27 / 4) * self.g_top / (30720 * math.pi)
        grid_T = np.geomspace(T_FLOOR, T_CEILING, 1000)
        grid_rho = np.array([self.g_rho(float(T)) * T**4 for T in grid_T])
        # Log10 interpolation is equivalent to natural log interpolation.
        self.inverse_grid = np.column_stack((np.log(grid_rho), np.log(grid_T)))
        assert np.all(np.diff(self.inverse_grid[:, 0]) > 0)

    def g_rho(self, T: float) -> float:
        return self.thermo(T)[0]

    def thermo(self, T: float) -> tuple[float, float, float]:
        """Return g_rho, dln(g_rho)/dlnT and dln(g_s)/dlnT."""
        x = math.log(T)
        if T <= 10:
            g, dg = log_interp(self.low_rho, x, 'constant')
            s, ds = log_interp(self.low_s, x, 'constant')
            return g, dg / g, ds / s
        s, ds = log_interp(self.high_s, x, 'constant')
        q, dq = log_interp(self.high_ratio, x, 'constant')
        return s * q, ds / s + dq / q, ds / s

    def T_from_lnrho(self, L: float) -> float:
        # rho unit here is g_rho*T_MeV^4, constant pi²/30 cancels.
        logT, _ = log_interp(self.inverse_grid, L, 'linear')
        return math.exp(logT)


class SourceBackground:
    def __init__(self, tables: WuXuThermodynamics, mass_g: float, beta: float):
        self.th = tables
        self.mass_g = mass_g
        self.beta = beta
        self.tf = mass_g / MP_G * TPL_S / GAMMA
        self.tau = (mass_g / MP_G)**3 * TPL_S / (3 * tables.n_bh)
        self.Tf = math.sqrt(1 / (2 * self.tf * HCOEFF * math.sqrt(tables.g_top)))
        self.Lf = math.log(tables.g_top) + 4 * math.log(self.Tf)
        self.t_evap = self.tf + self.tau
        self.log_a_end = math.log(10 * (tables.g_top / tables.g_rho(T_NUC))**(1 / 3) * self.Tf / T_NUC)

    def state(self, L: float, A: float, y: float):
        T = self.th.T_from_lnrho(L)
        g, r, s = self.th.thermo(T)
        B = self.beta * math.exp(self.Lf - L - 3*A)
        H = HCOEFF * math.exp(L / 2) * math.sqrt(1 + B*y)
        C0 = -4 + r / (3+s)
        return T, B, H, C0

    def run(self, rtol=1e-9, atol=1e-11, max_step_x=0.015,
            max_step_y=0.0004, max_step_post=0.005,
            cutoff_T=0.065):
        """Integrate log time -> remaining mass ratio -> log time.

        Cutting off at y=0 is an analytically tractable mass-law extension of
        source cutoff at max(Mf exp(-20), m_Pl). The difference is negligible
        in physical t at scanned masses, but not a byte-identical Julia run.
        """
        calls = []
        def event(_, q):
            return math.log(self.th.T_from_lnrho(float(q[0]))) - LOG_T_NUC
        event.terminal = False
        event.direction = 0
        # Step 1: x = ln(t/t_f), until M/Mf=1/2.
        x_end = math.log(self.t_evap/self.tf - self.tau/(8*self.tf))
        def before(x, q):
            L, A = q
            t = self.tf * math.exp(x)
            y = max(1e-40, 1 - (t - self.tf) / self.tau)**(1/3)
            _, B, H, C = self.state(L, A, y)
            return [t*(H*C + B/(3*self.tau*y*y)), t*H]
        pre = solve_ivp(before, (0, x_end), [self.Lf, 0.],
                        events=event, rtol=rtol, atol=atol, max_step=max_step_x)
        if not pre.success:
            raise RuntimeError('pre phase: '+pre.message)
        calls += [(self.tf*math.exp(float(x)), 'pre') for x in pre.t_events[0]]
        # Step 2: y=M/M_f decreasing from 1/2 to 0.
        def evaporating(y, q):
            L, A = q
            _, B, H, C = self.state(L, A, y)
            return [-3*self.tau*y*y*H*C-B, -3*self.tau*y*y*H]
        ev = solve_ivp(evaporating, (.5, 0.), pre.y[:, -1], events=event,
                       rtol=rtol, atol=atol, max_step=max_step_y)
        if not ev.success:
            raise RuntimeError('evap phase: '+ev.message)
        calls += [(self.tf+self.tau*(1-float(y)**3), 'evap') for y in ev.t_events[0]]
        L_end, A_end = ev.y[:, -1]
        T_end = self.th.T_from_lnrho(float(L_end))
        # Step 3: PBH vanish, x=ln(t/t_evap).
        def after(x, q):
            L, A = q
            t = self.t_evap*math.exp(x)
            _, _, H, C = self.state(L, A, 0.)
            return [t*H*C, t*H]
        post = solve_ivp(after, (0, math.log(400/self.t_evap)), ev.y[:, -1],
                         events=event, rtol=rtol, atol=atol, max_step=max_step_post)
        if not post.success:
            raise RuntimeError('post phase: '+post.message)
        calls += [(self.t_evap*math.exp(float(x)), 'post') for x in post.t_events[0]]
        times = [t for t, stage in sorted(calls)]
        gap = times[-1] - times[0] if len(times)>1 else None
        H_Tn = HCOEFF * math.sqrt(self.th.g_rho(T_NUC)) * T_NUC**2
        deta_grid = self.log_a_end / 9999
        approx_gap_eta = gap * H_Tn if gap is not None else None
        return {
            'mass_g':self.mass_g,'beta':self.beta,'t_f_s':self.tf,
            'tau_evap_s':self.tau,'source_Tf_MeV':self.Tf,
            'T_at_evap_MeV':T_end,'crossings_s':times,
            'crossing_phases':[p for _,p in sorted(calls)],
            'crossing_count':len(times),'span_s':gap,
            'source_log_a_end':self.log_a_end,
            'source_grid_delta_log_a':deta_grid,
            'estimated_delta_log_a_spanning_crossings':approx_gap_eta,
            'sampling_step_over_branch_width':
                deta_grid/approx_gap_eta if approx_gap_eta else None,
            'source_tables':'WuXu from CSV','full_julia_run':False,
            'solver_success':bool(pre.success and ev.success and post.success),
            'solver_nfev':int(pre.nfev+ev.nfev+post.nfev),
        }


def selftest():
    # Self-contained constant-g test of the temperature/radiation ODE; no PBH.
    class Flat:
        g_top = 10.75
        n_bh = (27/4)*g_top/(30720*math.pi)
        def g_rho(self, T): return self.g_top
        def T_from_lnrho(self, L): return math.exp((L-math.log(self.g_top))/4)
        def thermo(self, T): return self.g_top,0.,0.
    b = SourceBackground(Flat(), 1e10, 0.)
    result = b.run(max_step_x=.08, max_step_y=.008, max_step_post=.008)
    tref = 1/(2*HCOEFF*math.sqrt(b.th.g_top)*T_NUC**2)
    assert len(result['crossings_s']) == 1
    assert abs(result['crossings_s'][0]/tref-1)<1e-6, result
    print('PASS: analytic radiation-only T(t)=T_f sqrt(t_f/t)',result['crossings_s'][0],tref)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir',type=Path)
    ap.add_argument('--fetch-source',action='store_true',
                    help='Download only three Git-blob-verified input CSV tables')
    ap.add_argument('--selftest',action='store_true')
    ap.add_argument('--mass',type=float,default=9.6725e9)
    ap.add_argument('--beta',type=float,default=1e-17)
    ap.add_argument('--rtol',type=float,default=1e-9)
    ap.add_argument('--output',type=Path)
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    if args.data_dir is None and not args.fetch_source:
        ap.error('--data-dir required unless --selftest or --fetch-source')
    if args.data_dir is None:
        args.data_dir = Path(__file__).resolve().parent / 'dax_s7_wuxu_source_tables'
    if args.fetch_source:
        fetch_source(args.data_dir)
    d = SourceBackground(WuXuThermodynamics(args.data_dir),args.mass,args.beta).run(rtol=args.rtol)
    data = json.dumps(d,indent=2,ensure_ascii=False)
    if args.output:
        args.output.write_text(data+'\n',encoding='utf-8')
    print(data)

if __name__=='__main__': main()
