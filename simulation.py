"""Monte Carlo liviano para LPF Lite.

No usa SciPy: sólo NumPy. Simula goles con Poisson a partir de tasas de GF/GC
regularizadas y devuelve chances estimadas, nunca estados exactos.
"""
from __future__ import annotations

from collections import defaultdict

import numpy as np

from .data import ZONE_A, ZONE_B


def _team_rates(zones):
    all_rows = {team: row for base in zones.values() for team, row in base.items()}
    total_gf = sum(int(r["gf"]) for r in all_rows.values())
    total_pj = sum(int(r["pj"]) for r in all_rows.values())
    league = max(0.75, total_gf / max(1, total_pj))
    rates = {}
    prior_games = 4.0
    for team, row in all_rows.items():
        pj = max(0, int(row["pj"]))
        gf = int(row["gf"]); ga = int(row["ga"])
        attack = (gf + prior_games * league) / (pj + prior_games)
        defense = (ga + prior_games * league) / (pj + prior_games)
        rates[team] = (max(0.35, attack), max(0.35, defense))
    return rates, league


def _rank(points, dg, gf, teams):
    return sorted(teams, key=lambda t: (-points[t], -dg[t], -gf[t], t))


def simulate_playoffs(zones, pending, *, n=2500, seed=20260917, focus_team=None, force_next=None):
    """Simula el fixture pendiente y estima clasificación a top 8.

    ``force_next`` puede ser ``G``, ``E`` o ``P`` para fijar el próximo partido del
    equipo foco. El resto del torneo continúa simulado normalmente.
    """
    rng = np.random.default_rng(seed)
    teams = [*ZONE_A, *ZONE_B]
    zone_of = {t: "A" for t in ZONE_A} | {t: "B" for t in ZONE_B}
    current = {team: dict(row) for base in zones.values() for team, row in base.items()}
    rates, league = _team_rates(zones)
    games = sorted(pending, key=lambda g: int(g["f"]))
    next_focus = None
    if focus_team:
        next_focus = next((g for g in games if focus_team in (g["l"], g["v"])), None)

    qualified = defaultdict(int)
    focus_points = defaultdict(lambda: [0, 0])  # total -> [qualified, samples]

    for _ in range(int(n)):
        pts = {t: int(current[t]["pts"]) for t in teams}
        gf = {t: int(current[t]["gf"]) for t in teams}
        ga = {t: int(current[t]["ga"]) for t in teams}
        dg = {t: int(current[t]["dg"]) for t in teams}

        for g in games:
            home, away = g["l"], g["v"]
            fixed = bool(focus_team and next_focus is g and force_next in {"G", "E", "P"})
            if fixed:
                if force_next == "E":
                    gh = ga_ = 1
                else:
                    focus_home = home == focus_team
                    focus_wins = force_next == "G"
                    home_wins = focus_wins if focus_home else not focus_wins
                    gh, ga_ = (1, 0) if home_wins else (0, 1)
            else:
                a_h, d_h = rates[home]
                a_a, d_a = rates[away]
                lam_h = max(0.2, ((a_h * d_a) / league) * 1.08)
                lam_a = max(0.2, ((a_a * d_h) / league) * 0.94)
                gh = int(rng.poisson(lam_h)); ga_ = int(rng.poisson(lam_a))
            gf[home] += gh; ga[home] += ga_; dg[home] += gh - ga_
            gf[away] += ga_; ga[away] += gh; dg[away] += ga_ - gh
            if gh > ga_:
                pts[home] += 3
            elif gh < ga_:
                pts[away] += 3
            else:
                pts[home] += 1; pts[away] += 1

        top = {}
        for zone, zteams in (("A", ZONE_A), ("B", ZONE_B)):
            order = _rank(pts, dg, gf, zteams)
            top[zone] = set(order[:8])
            for team in order[:8]:
                qualified[team] += 1
        if focus_team:
            final_pts = int(pts[focus_team])
            focus_points[final_pts][1] += 1
            if focus_team in top[zone_of[focus_team]]:
                focus_points[final_pts][0] += 1

    chances = {team: 100.0 * qualified[team] / n for team in teams}
    by_points = {
        total: (100.0 * q / samples if samples else 0.0)
        for total, (q, samples) in sorted(focus_points.items())
    }
    target70 = next((total for total, chance in by_points.items() if chance >= 70.0), None)
    return {"chances": chances, "by_points": by_points, "target70": target70, "simulations": int(n)}
