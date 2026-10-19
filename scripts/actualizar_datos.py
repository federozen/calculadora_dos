"""Sincronización validada del Clausura 2026, apta para GitHub Actions.

Lee marcadores explícitos de TyC, comprueba el fixture y conserva la foto anterior
si hay red caída, marcadores contradictorios o partidos de una fecha ya terminada
sin confirmar. No importa Streamlit ni necesita abrir un navegador.

Ejecutar: python scripts/actualizar_datos.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "core"))
from lpf_checkpoint import CHECKPOINT_ROUND, checkpoint_results, project_checkpoint, save_recent_results
from lpf_clubs import canon_club
from lpf_data_2026 import LPF_FIXTURE
from lpf_fixture_sources import parse_tyc_clausura_results_html, played_pending_from_records
from lpf_http import fetch_html
from lpf_table_backup import build_table_backup, write_table_backup

RESULTS_URL = (
    "https://www.tycsports.com/liga-profesional-de-futbol/"
    "fixture-del-clausura-2026-calendario-de-partidos-y-resultados-id750943.html"
)
DATA = ROOT / "core" / "data"
FECHA_FIN = {
    11: date(2026, 10, 14),
    12: date(2026, 10, 12),
    13: date(2026, 10, 19),
    14: date(2026, 10, 27),
    15: date(2026, 11, 2),
}


def _current_results() -> list[tuple[str, str, int, int]]:
    from lpf_checkpoint import cached_results
    return cached_results()


def _opening_from_backup(backup: dict) -> dict:
    """Apertura cerrado = tabla anual vigente - Clausura en el mismo respaldo."""
    old_zones = {team: row for table in backup["zones"].values() for team, row in table.items()}
    annual = backup["annual"]
    opening = {}
    if set(annual) != set(old_zones):
        raise ValueError("El respaldo anterior no tiene los 30 clubes en anual y zonas")
    for team, annual_row in annual.items():
        row = {key: int(annual_row[key]) - int(old_zones[team][key])
               for key in ("pts", "pj", "gf", "ga", "dg")}
        if row["pj"] != 16 or row["gf"] - row["ga"] != row["dg"]:
            raise ValueError(f"El Apertura no cierra para {team}")
        opening[team] = row
    return opening


def prepare_update(source_results, previous_results, backup, now: datetime) -> dict:
    """Validación completa ANTES de escribir cualquier archivo."""
    fixture = {(g["l"], g["v"]): int(g["f"]) for g in LPF_FIXTURE}
    historic = {(r[0], r[1]): (int(r[2]), int(r[3])) for r in previous_results}
    merged = dict(historic)
    for home, away, hg, ag in source_results:
        pair = (canon_club(home), canon_club(away))
        if pair not in fixture or fixture[pair] <= CHECKPOINT_ROUND:
            continue
        score = (int(hg), int(ag))
        if pair in merged and merged[pair] != score:
            raise ValueError(f"Marcador contradictorio para {pair[0]} - {pair[1]}")
        merged[pair] = score
    if not merged:
        raise ValueError("La fuente no entregó ningún resultado nuevo desde la fecha 10")
    today = now.astimezone(ZoneInfo("America/Argentina/Buenos_Aires")).date()
    for round_no, finished_day in FECHA_FIN.items():
        if today <= finished_day:
            continue  # fechas en disputa no se completan por suposiciones
        missing = [g for g in LPF_FIXTURE if g["f"] == round_no and (g["l"], g["v"]) not in merged]
        if missing:
            raise ValueError(f"Fecha {round_no} cerrada pero faltan {len(missing)} partidos finales en la fuente")
    rows = [(g["l"], g["v"], *merged[(g["l"], g["v"])])
            for g in LPF_FIXTURE if (g["l"], g["v"]) in merged]
    full = checkpoint_results() + rows
    zones = project_checkpoint(full)
    opening = _opening_from_backup(backup)
    annual = {team: {key: int(opening[team][key]) + int(values[key])
                     for key in ("pts", "pj", "gf", "ga", "dg")}
              for base in zones.values() for team, values in base.items()}
    stamp = now.isoformat(timespec="seconds")
    snapshot = build_table_backup(zones, annual, "Resultados TyC verificados + base fija F10", updated_at=stamp)
    round_counts = Counter(fixture[(home, away)] for home, away, _hg, _ag in rows)
    expected_round = max((g["f"] for g in LPF_FIXTURE if (g["l"], g["v"]) in merged), default=10)
    meta = {
        "ok": True, "updated_at": stamp,
        "fecha_min": min(r["pj"] for base in zones.values() for r in base.values()),
        "fecha_max": max(r["pj"] for base in zones.values() for r in base.values()),
        "resultados": len(full), "fuente": "TyC Sports + base fija F10",
        "fuente_resultados": RESULTS_URL,
        "sin_confirmar": 0,
        "avisos": [f"Fecha {expected_round}: {round_counts[expected_round]}/15 resultados confirmados."]
                if round_counts[expected_round] < 15 else [],
    }
    return {"played": full, "zones": zones, "snapshot": snapshot, "meta": meta}


def persist(prepared: dict) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    full = prepared["played"]
    # Las tres salidas sólo se escriben después de validar la coherencia completa.
    # Si GitHub Actions falla, NO hace commit y prevalece la versión anterior.
    save_recent_results(full, DATA / "lpf_since_round11.json", source_urls=(RESULTS_URL,))
    write_table_backup(prepared["snapshot"], DATA / "lpf_last_valid.json")
    txt = "\n".join(f"{home} {hg}-{ag} {away}" for home,away,hg,ag in full) + "\n"
    (DATA / "lpf_resultados.txt").write_text(txt, encoding="utf-8")
    (DATA / "lpf_actualizacion.json").write_text(
        json.dumps(prepared["meta"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    try:
        html, source_url = fetch_html(RESULTS_URL, referer="https://www.tycsports.com/", timeout=25, retries=1)
        records = parse_tyc_clausura_results_html(
            html, canon_club=canon_club, official_fixture=LPF_FIXTURE, source_url=source_url)
        played, _pending = played_pending_from_records(records)
        if not played:
            raise ValueError("El parser no encontró resultados finales de TyC")
        old = json.loads((DATA / "lpf_last_valid.json").read_text(encoding="utf-8"))
        existing = _current_results()
        updated = prepare_update(played, existing, old, datetime.now(timezone.utc))
        known_pairs = {(l, v) for l, v, _hg, _ag in existing}
        new_pairs = {(l, v) for l, v, _hg, _ag in updated["played"]
                     if (l, v) not in known_pairs and (l, v) in
                     {(g["l"], g["v"]) for g in LPF_FIXTURE if g["f"] > CHECKPOINT_ROUND}}
        if not new_pairs:
            print("Sin nuevos partidos finalizados; la base validada no se modifica.")
            return 0
        persist(updated)
        print(json.dumps(updated["meta"], ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f"ACTUALIZACIÓN RECHAZADA, se conserva la base previa: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
