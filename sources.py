"""Fuente de resultados para LPF Lite.

La versión Lite usa una sola fuente externa para el Clausura: el fixture vivo de
TyC Sports. La tabla se reconstruye localmente a partir de los marcadores; no se
importan standings de terceros ni se mezclan reglas con datos.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Iterable

import requests
from bs4 import BeautifulSoup

from .data import CLUB_ALIASES, FIXTURE, TYC_RESULTS_URL


def _fold(value: object) -> str:
    text = str(value or "").strip().lower().replace("’", "'")
    text = "".join(ch for ch in unicodedata.normalize("NFD", text) if unicodedata.category(ch) != "Mn")
    text = text.replace(".", " ").replace("'", "")
    return re.sub(r"\s+", " ", text).strip()


def _compact(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "", _fold(value))


_LOOKUP: dict[str, str] = {}
for canonical, aliases in CLUB_ALIASES.items():
    _LOOKUP[_fold(canonical)] = canonical
    for alias in aliases:
        _LOOKUP[_fold(alias)] = canonical

# Variantes visibles que aparecen en TyC y no siempre coinciden con los alias
# editoriales del proyecto completo.
_EXTRA = {
    "ind rivadavia mza": "Independiente Rivadavia",
    "ind rivadavia": "Independiente Rivadavia",
    "independiente rivadavia mza": "Independiente Rivadavia",
    "gimnasia mza": "Gimnasia de Mendoza",
    "gimnasia m": "Gimnasia de Mendoza",
    "estudiantes rio cuarto": "Estudiantes de Río Cuarto",
    "estudiantes rc": "Estudiantes de Río Cuarto",
    "newells": "Newell's Old Boys",
    "central cordoba": "Central Córdoba",
    "boca": "Boca Juniors",
    "river": "River Plate",
    "argentinos": "Argentinos Juniors",
    "velez": "Vélez Sarsfield",
    "riestra": "Deportivo Riestra",
    "defensa": "Defensa y Justicia",
    "central": "Rosario Central",
    "gimnasia": "Gimnasia La Plata",
    "estudiantes": "Estudiantes de La Plata",
}
_LOOKUP.update({_fold(k): v for k, v in _EXTRA.items()})


def canon_team(value: object) -> str | None:
    raw = re.sub(r"^\s*\d+[.)-]?\s*", "", str(value or ""))
    raw = re.sub(r"\s+", " ", raw).strip()
    if not raw:
        return None
    direct = _LOOKUP.get(_fold(raw))
    if direct:
        return direct
    compact = _compact(raw)
    scores: list[tuple[int, str]] = []
    for alias, team in _LOOKUP.items():
        needle = _compact(alias)
        if len(needle) >= 4 and needle in compact:
            scores.append((len(needle), team))
    scores.sort(reverse=True)
    if not scores:
        return None
    if len(scores) == 1 or scores[0][0] > scores[1][0]:
        return scores[0][1]
    return None


_FIXTURE_INDEX = {(row["l"], row["v"]): int(row["f"]) for row in FIXTURE}
_EXPECTED = {team for pair in _FIXTURE_INDEX for team in pair}


def _round_from_text(value: object) -> int | None:
    text = _fold(value)
    match = re.search(r"\bfecha\s+(?:n[°ºo]?\s*)?(\d{1,2})\b", text)
    return int(match.group(1)) if match else None


def _score_line(text: str) -> tuple[str, str, int, int] | None:
    line = re.sub(r"\s+", " ", str(text or "")).strip()
    if not line:
        return None
    patterns = (
        re.compile(r"^(?P<home>.+?)\s+(?P<hg>\d+)\s*[–—-]\s*(?P<ag>\d+)\s+(?P<away>.+?)(?:\s*\([^)]*\))?$"),
        re.compile(r"^(?P<home>.+?)\s+(?P<hg>\d+)\s*[–—-]\s*(?P<away>.+?)\s+(?P<ag>\d+)(?:\s*[,;(].*)?$"),
    )
    for pattern in patterns:
        m = pattern.match(line)
        if not m:
            continue
        home = canon_team(m.group("home"))
        away = canon_team(m.group("away"))
        if home in _EXPECTED and away in _EXPECTED and home != away and (home, away) in _FIXTURE_INDEX:
            return home, away, int(m.group("hg")), int(m.group("ag"))
    return None


def parse_tyc_results(html: str) -> list[tuple[int, str, str, int, int]]:
    """Devuelve ``(fecha, local, visitante, gl, gv)`` validados contra el fixture."""
    soup = BeautifulSoup(html or "", "html.parser")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    root = soup.find("article") or soup.find("main") or soup
    in_results = False
    current_round: int | None = None
    out: list[tuple[int, str, str, int, int]] = []
    seen: set[tuple[str, str]] = set()

    # TyC estructura el artículo en títulos, párrafos y listas. El parser evita
    # depender de clases CSS: sólo necesita el encabezado de resultados, Fecha N y
    # un marcador explícito que exista en el fixture canónico.
    for tag in root.find_all(["h1", "h2", "h3", "h4", "h5", "p", "li", "td"]):
        text = re.sub(r"\s+", " ", tag.get_text(" ", strip=True)).strip()
        if not text:
            continue
        folded = _fold(text)
        if "resultados del torneo clausura 2026" in folded:
            in_results = True
            current_round = None
            continue
        if not in_results:
            continue
        if folded in {"te puede interesar", "tambien te puede interesar"}:
            break
        marker = _round_from_text(text)
        if marker is not None:
            current_round = marker
            continue
        if current_round is None or not 1 <= current_round <= 16:
            continue
        parsed = _score_line(text)
        if not parsed:
            continue
        home, away, gh, ga = parsed
        if _FIXTURE_INDEX.get((home, away)) != current_round:
            continue
        key = (home, away)
        if key in seen:
            continue
        seen.add(key)
        out.append((current_round, home, away, gh, ga))
    return sorted(out, key=lambda r: (r[0], r[1], r[2]))


def fetch_tyc_results(timeout: int = 20) -> tuple[list[tuple[int, str, str, int, int]], str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; LPF-Lite/1.0; +https://github.com/)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "es-AR,es;q=0.9",
        "Referer": "https://www.tycsports.com/liga-profesional-de-futbol/",
        "Cache-Control": "no-cache",
    }
    response = requests.get(TYC_RESULTS_URL, headers=headers, timeout=timeout, allow_redirects=True)
    response.raise_for_status()
    results = parse_tyc_results(response.text)
    if len(results) < 135:
        raise RuntimeError(
            f"TyC respondió, pero sólo pude identificar {len(results)} resultados; "
            "la foto vigente requiere al menos 135 (Fechas 1-9)."
        )
    return results, str(response.url)


def played_pairs(results: Iterable[tuple[int, str, str, int, int]]) -> set[tuple[str, str]]:
    return {(home, away) for _round, home, away, _gh, _ga in results}
