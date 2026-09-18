"""Motor compacto de LPF Lite: standings, Anual, Copas y descenso."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

import pandas as pd

from .data import APERTURA_CHAMPION, FIXTURE, OPENING, PREVIOUS_AVERAGES, TOTAL_ROUNDS, ZONE_A, ZONE_B

STAT_KEYS = ("pts", "pj", "gf", "ga", "dg")


def _blank() -> dict[str, int]:
    return {"pts": 0, "pj": 0, "gf": 0, "ga": 0, "dg": 0}


def build_zone_tables(results):
    teams = list(ZONE_A) + list(ZONE_B)
    stats = {team: _blank() for team in teams}
    for _round, home, away, gh, ga in results:
        if home not in stats or away not in stats:
            continue
        h, a = stats[home], stats[away]
        h["pj"] += 1; a["pj"] += 1
        h["gf"] += int(gh); h["ga"] += int(ga)
        a["gf"] += int(ga); a["ga"] += int(gh)
        if gh > ga:
            h["pts"] += 3
        elif gh < ga:
            a["pts"] += 3
        else:
            h["pts"] += 1; a["pts"] += 1
    for row in stats.values():
        row["dg"] = row["gf"] - row["ga"]
    return {"A": {t: stats[t] for t in ZONE_A}, "B": {t: stats[t] for t in ZONE_B}}


def annual_table(zones):
    out = {}
    for base in zones.values():
        for team, row in base.items():
            opening = OPENING[team]
            out[team] = {key: int(opening[key]) + int(row[key]) for key in STAT_KEYS}
    return out


def rank_rows(base: dict[str, dict]) -> list[dict]:
    ordered = sorted(base.items(), key=lambda item: (-int(item[1]["pts"]), -int(item[1]["dg"]), -int(item[1]["gf"]), item[0]))
    return [
        {"Pos": i, "Equipo": team, "PTS": int(row["pts"]), "PJ": int(row["pj"]), "GF": int(row["gf"]), "GC": int(row["ga"]), "DG": int(row["dg"])}
        for i, (team, row) in enumerate(ordered, 1)
    ]


def table_df(base):
    return pd.DataFrame(rank_rows(base))


def pending_matches(results):
    played = {(home, away) for _round, home, away, _gh, _ga in results}
    return [dict(row) for row in FIXTURE if (row["l"], row["v"]) not in played]


def rest_by_team(zones):
    return {team: max(0, TOTAL_ROUNDS - int(row["pj"])) for base in zones.values() for team, row in base.items()}


def current_cut(zone_base, rank=8):
    rows = rank_rows(zone_base)
    if len(rows) < rank:
        return None
    return rows[rank - 1]["PTS"]


def team_position(base, team):
    for row in rank_rows(base):
        if row["Equipo"] == team:
            return int(row["Pos"])
    return None


def conservative_secure_total(zone_base, team, rank=8):
    """Puntaje seguro conservador: supera el rank-ésimo máximo rival posible."""
    own = zone_base[team]
    own_max = int(own["pts"]) + 3 * max(0, TOTAL_ROUNDS - int(own["pj"]))
    rival_maxima = []
    for rival, row in zone_base.items():
        if rival == team:
            continue
        rival_maxima.append(int(row["pts"]) + 3 * max(0, TOTAL_ROUNDS - int(row["pj"])))
    rival_maxima.sort(reverse=True)
    if len(rival_maxima) < rank:
        return int(own["pts"])
    target = rival_maxima[rank - 1] + 1
    return target if target <= own_max else None


def next_team_match(team, pending):
    games = [g for g in pending if team in (g["l"], g["v"])]
    return min(games, key=lambda g: int(g["f"])) if games else None


def recent_form(team, results, n=5):
    seq = []
    for _round, home, away, gh, ga in sorted(results, key=lambda r: r[0], reverse=True):
        if team not in (home, away):
            continue
        gf, gc = (gh, ga) if team == home else (ga, gh)
        seq.append("G" if gf > gc else "E" if gf == gc else "P")
        if len(seq) >= n:
            break
    return list(reversed(seq))


def fixed_libertadores(annual, clausura_champion="", copa_champion="", extra_lib="", extra_sud="", copa_heir=""):
    order = [row["Equipo"] for row in rank_rows(annual)]
    fixed: list[tuple[str, str]] = []
    notices = []

    def add(team, reason):
        if team and team in order and all(existing != team for existing, _ in fixed):
            fixed.append((team, reason)); return True
        return False

    add(extra_lib, "Campeón Libertadores 2026")
    add(extra_sud, "Campeón Sudamericana 2026")
    base_slots = 6
    for team, reason in ((APERTURA_CHAMPION, "Campeón Apertura"), (clausura_champion, "Campeón Clausura")):
        if team:
            if not add(team, reason):
                notices.append(f"{team} ya tenía plaza; el cupo corre por Tabla Anual.")
            base_slots -= 1
        else:
            base_slots -= 1
    if copa_champion:
        if not add(copa_champion, "Campeón Copa Argentina"):
            if copa_heir:
                add(copa_heir, "Hereda plaza de Copa Argentina")
            notices.append("El campeón de Copa Argentina ya tenía plaza; su plaza no pasa automáticamente a la Tabla Anual.")
        base_slots -= 1
    else:
        base_slots -= 1
        notices.append("Copa Argentina todavía sin campeón definido.")

    table_slots = max(0, base_slots)
    taken = {team for team, _ in fixed}
    reduced = [team for team in order if team not in taken]
    for team in reduced[:table_slots]:
        fixed.append((team, "Tabla Anual"))
    return {"libertadores": fixed, "table_slots": table_slots, "reduced": reduced, "notices": notices}


def cup_map(annual, **kwargs):
    alloc = fixed_libertadores(annual, **kwargs)
    lib_teams = [team for team, _ in alloc["libertadores"]]
    order = [row["Equipo"] for row in rank_rows(annual)]
    sud = [team for team in order if team not in lib_teams][:6]
    return alloc | {"sudamericana": sud}


def average_rows(annual):
    rows = []
    for team, row in annual.items():
        pp, pj_prev = PREVIOUS_AVERAGES.get(team, (0, 0))
        pts = int(pp) + int(row["pts"])
        pj = int(pj_prev) + int(row["pj"])
        avg = pts / pj if pj else 0.0
        rows.append({"Equipo": team, "Promedio": avg, "Pts": pts, "PJ": pj})
    return sorted(rows, key=lambda r: (-r["Promedio"], -r["Pts"], r["Equipo"]))


def relegation_picture(annual):
    averages = average_rows(annual)
    min_avg = min(Fraction(int(r["Pts"]), int(r["PJ"])) if r["PJ"] else Fraction(0, 1) for r in averages)
    avg_bottom = [r["Equipo"] for r in averages if (Fraction(int(r["Pts"]), int(r["PJ"])) if r["PJ"] else Fraction(0, 1)) == min_avg]
    # El descenso por Anual excluye al/los candidatos que desciendan por promedio.
    annual_sorted = sorted(((team, int(row["pts"])) for team, row in annual.items()), key=lambda x: (x[1], x[0]))
    annual_candidates = []
    for team, pts in annual_sorted:
        if team in avg_bottom:
            continue
        if not annual_candidates:
            min_pts = pts
        if pts == min_pts:
            annual_candidates.append(team)
        else:
            break
    return {"average_candidates": avg_bottom, "annual_candidates": annual_candidates, "averages": averages}


def audit(results, zones):
    result_count = len(results)
    implied = sum(int(row["pj"]) for base in zones.values() for row in base.values()) // 2
    pjs = sorted({int(row["pj"]) for base in zones.values() for row in base.values()})
    return {
        "results": result_count,
        "implied_matches": implied,
        "uniform_pj": pjs[0] if len(pjs) == 1 else None,
        "pj_values": pjs,
        "ok": result_count == implied and result_count > 0,
    }
