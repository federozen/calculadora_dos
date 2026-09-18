from __future__ import annotations

import pandas as pd
import streamlit as st

from lpf_lite import __version__
from lpf_lite.data import APERTURA_CHAMPION, FALLBACK_RESULTS, ZONE_A, ZONE_B
from lpf_lite.engine import (
    annual_table,
    audit,
    average_rows,
    build_zone_tables,
    conservative_secure_total,
    cup_map,
    current_cut,
    next_team_match,
    pending_matches,
    rank_rows,
    recent_form,
    relegation_picture,
    rest_by_team,
    table_df,
    team_position,
)
from lpf_lite.simulation import simulate_playoffs
from lpf_lite.sources import fetch_tyc_results

st.set_page_config(page_title="Calculadora LPF Lite", page_icon="⚽", layout="wide")

st.markdown(
    """
<style>
.block-container {padding-top: 1.4rem; max-width: 1500px;}
[data-testid="stMetricValue"] {font-size: 1.55rem;}
.small-note {color:#6b7280;font-size:.88rem;}
</style>
""",
    unsafe_allow_html=True,
)

@st.cache_data(ttl=600, show_spinner=False)
def load_live():
    return fetch_tyc_results(timeout=20)


def get_data():
    try:
        results, url = load_live()
        return results, "TyC Sports", url, ""
    except Exception as exc:
        return FALLBACK_RESULTS, "Fallback incluido", "", str(exc)


def fmt_match(game):
    return "—" if not game else f"F{game['f']} · {game['l']} vs {game['v']}"


def pct(value):
    return f"{value:.1f}%"

results, source_name, source_url, source_error = get_data()
zones = build_zone_tables(results)
annual = annual_table(zones)
pending = pending_matches(results)
rest = rest_by_team(zones)
quality = audit(results, zones)

st.title("⚽ Calculadora LPF Lite")
st.caption(f"Versión {__version__} · repo rápido · una sola fuente externa de resultados")

if source_error:
    st.warning(
        f"No pude actualizar desde TyC y estoy usando el fallback incluido ({len(results)} resultados). "
        f"Detalle: {source_error}"
    )
elif not quality["ok"]:
    st.warning(f"La fuente entregó {quality['results']} resultados y la tabla reconstruida implica {quality['implied_matches']} partidos.")
else:
    st.success(f"Datos actualizados: {len(results)} resultados · {source_name} · PJ detectados: {quality['pj_values']}")

with st.sidebar:
    st.header("Datos")
    st.write(f"**Fuente:** {source_name}")
    st.write(f"**Resultados:** {len(results)}")
    st.write(f"**Pendientes:** {len(pending)}")
    if source_url:
        st.caption(source_url)
    if st.button("Actualizar ahora", use_container_width=True):
        load_live.clear()
        st.rerun()
    st.divider()
    st.header("Copas 2027")
    all_teams = [r["Equipo"] for r in rank_rows(annual)]
    st.caption(f"Campeón Apertura: {APERTURA_CHAMPION}")
    clausura_champion = st.selectbox("Campeón Clausura", [""] + all_teams, index=0)
    copa_champion = st.selectbox("Campeón Copa Argentina", [""] + all_teams, index=0)
    extra_lib = st.selectbox("Campeón Libertadores argentino", [""] + all_teams, index=0)
    extra_sud = st.selectbox("Campeón Sudamericana argentino", [""] + all_teams, index=0)

main_tabs = st.tabs(["Zonas", "Panel por equipo", "Tabla Anual y Copas", "Descenso", "Auditoría"])

with main_tabs[0]:
    c1, c2 = st.columns(2)
    for col, label in ((c1, "A"), (c2, "B")):
        with col:
            st.subheader(f"Zona {label}")
            df = table_df(zones[label]).copy()
            df["Estado"] = ["Playoffs" if p <= 8 else "" for p in df["Pos"]]
            st.dataframe(df[["Pos", "Equipo", "PTS", "PJ", "GF", "GC", "DG", "Estado"]], hide_index=True, use_container_width=True)
            st.caption(f"Corte actual: {current_cut(zones[label], 8)} puntos")

with main_tabs[1]:
    zone_choice = st.radio("Zona", ["A", "B"], horizontal=True)
    zone_teams = [r["Equipo"] for r in rank_rows(zones[zone_choice])]
    team = st.selectbox("Equipo", zone_teams)
    row = zones[zone_choice][team]
    pos = team_position(zones[zone_choice], team)
    cutoff = current_cut(zones[zone_choice], 8)
    secure = conservative_secure_total(zones[zone_choice], team, 8)
    next_game = next_team_match(team, pending)
    form = recent_form(team, results, 5)

    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Posición", f"{pos}º")
    m2.metric("Puntos", int(row["pts"]))
    m3.metric("Corte actual", int(cutoff or 0))
    m4.metric("Partidos restantes", int(rest[team]))
    m5.metric("Máximo", int(row["pts"]) + 3 * int(rest[team]))
    st.write(f"**Próximo:** {fmt_match(next_game)}")
    st.write(f"**Forma reciente:** {' · '.join(form) if form else '—'}")
    if secure is None:
        st.info("Referencia segura conservadora: hoy no existe un puntaje alcanzable que garantice top 8 ignorando dependencias entre rivales.")
    else:
        st.info(f"Referencia segura conservadora: **{secure} puntos totales**. Es una garantía deliberadamente exigente, no el mínimo exacto.")

    sims = st.slider("Simulaciones", 800, 5000, 2500, 200)
    sim_key = (team, int(sims), len(results))
    if st.button("Calcular simulación", type="primary"):
        with st.spinner("Simulando el fixture pendiente…"):
            sim = simulate_playoffs(zones, pending, n=sims, focus_team=team)
            forced = {}
            if next_game:
                for code in ("G", "E", "P"):
                    forced[code] = simulate_playoffs(
                        zones, pending, n=max(700, sims // 2), focus_team=team,
                        force_next=code, seed=20260917 + ord(code)
                    )
            st.session_state["lite_sim"] = {"key": sim_key, "main": sim, "forced": forced}

    cached_sim = st.session_state.get("lite_sim") or {}
    if cached_sim.get("key") == sim_key:
        sim = cached_sim["main"]
        st.metric("Chance estimada de Playoffs", pct(sim["chances"][team]))
        if sim["target70"] is not None:
            st.write(f"Primer total que llega al 70% en la simulación: **{sim['target70']} puntos**.")

        if next_game and cached_sim.get("forced"):
            st.subheader("Si en el próximo partido…")
            cols = st.columns(3)
            labels = [("G", "Gana"), ("E", "Empata"), ("P", "Pierde")]
            for col, (code, label) in zip(cols, labels):
                forced = cached_sim["forced"][code]
                col.metric(label, pct(forced["chances"][team]))
            st.caption("Estas tres cifras son ESTIMADAS por Monte Carlo; no son estados matemáticos exactos.")

        if sim["by_points"]:
            chart = pd.DataFrame([{"Puntos finales": p, "Chance de Playoffs": c} for p, c in sim["by_points"].items()]).set_index("Puntos finales")
            st.line_chart(chart)
    else:
        st.caption("La simulación no corre al abrir la app: se ejecuta sólo cuando la pedís, para acelerar el arranque.")

with main_tabs[2]:
    st.subheader("Tabla Anual")
    st.dataframe(table_df(annual), hide_index=True, use_container_width=True)
    cups = cup_map(
        annual,
        clausura_champion=clausura_champion,
        copa_champion=copa_champion,
        extra_lib=extra_lib,
        extra_sud=extra_sud,
    )
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Libertadores 2027 · foto actual")
        lib_df = pd.DataFrame([{"Equipo": team, "Vía": reason} for team, reason in cups["libertadores"]])
        st.dataframe(lib_df, hide_index=True, use_container_width=True)
        for note in cups["notices"]:
            st.caption(note)
    with c2:
        st.subheader("Sudamericana 2027 · foto actual")
        sud_df = pd.DataFrame({"Equipo": cups["sudamericana"]})
        st.dataframe(sud_df, hide_index=True, use_container_width=True)
    st.caption("La foto de Copas usa la Tabla Anual actual y los campeones que cargues en la barra lateral. No proyecta quién ganará torneos pendientes.")

with main_tabs[3]:
    picture = relegation_picture(annual)
    st.subheader("Promedios")
    avg_df = pd.DataFrame(picture["averages"])
    avg_df["Promedio"] = avg_df["Promedio"].map(lambda x: round(float(x), 3))
    st.dataframe(avg_df, hide_index=True, use_container_width=True)
    c1, c2 = st.columns(2)
    with c1:
        st.error("Por promedio hoy: " + ", ".join(picture["average_candidates"]))
    with c2:
        st.error("Por Tabla Anual hoy (excluyendo descenso por promedio): " + ", ".join(picture["annual_candidates"]))
    st.caption("Si hay igualdad en la línea de descenso, se muestran todos los equipos implicados; no se usa DG para resolver un desempate reglamentario.")

with main_tabs[4]:
    st.subheader("Auditoría mínima")
    a1, a2, a3 = st.columns(3)
    a1.metric("Resultados", quality["results"])
    a2.metric("Partidos implícitos", quality["implied_matches"])
    a3.metric("PJ distintos", ", ".join(map(str, quality["pj_values"])))
    if quality["ok"]:
        st.success("Los marcadores reconstruyen exactamente la cantidad de partidos de las tablas calculadas.")
    else:
        st.warning("La cobertura no está completa. La app sigue visible, pero no conviene publicar proyecciones como foto vigente.")
    st.write("**Arquitectura Lite:** TyC → resultados explícitos → tablas reconstruidas → cálculos. No hay ESPN, FutbolArgentino, LPF crawler, API, Opta, reconciliación histórica ni archivos legacy.")
