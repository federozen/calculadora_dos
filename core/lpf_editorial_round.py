"""Informe editorial por fecha, sin red ni interfaz; distingue previa y foto actual."""
from __future__ import annotations
from lpf_checkpoint import CHECKPOINT_ROUND, checkpoint_results, project_checkpoint
from lpf_clubs import canon_club
from lpf_conditionals import _season_state
from lpf_display import editorialize_text
from lpf_schedule import format_datetime
from lpf_standings import liga_tabla_df

LPF_RUNTIME_API = 21


def round_start_snapshot(played, fixture, round_no):
    """Sólo reconstruye una previa cuando todas las fechas anteriores están cerradas."""
    round_no = int(round_no)
    if round_no <= CHECKPOINT_ROUND:
        return {'available': False, 'reason': 'La reconstrucción de previas comienza en la fecha 11.'}
    rounds = {(g['l'], g['v']): int(g['f']) for g in fixture}
    known = {(h, a): (int(gh), int(ga)) for h, a, gh, ga in checkpoint_results()}
    for h, a, gh, ga in played or []:
        pair = (canon_club(h), canon_club(a))
        if pair not in rounds:
            return {'available': False, 'reason': 'Hay resultados fuera del fixture oficial.'}
        score = (int(gh), int(ga))
        if rounds[pair] > CHECKPOINT_ROUND and pair in known and known[pair] != score:
            return {'available': False, 'reason': 'Hay marcadores contradictorios: no se reconstruye una previa.'}
        if min(score) < 0:
            return {'available': False, 'reason': 'Hay un marcador inválido.'}
        if rounds[pair] > CHECKPOINT_ROUND:
            known[pair] = score
    missing = [pair for pair, f in rounds.items() if f < round_no and pair not in known]
    if missing:
        return {'available': False, 'reason': f'Faltan {len(missing)} resultados anteriores a la fecha {round_no}. Usá el informe actualizado; no se inventa una foto previa.'}
    before = [(h, a, *score) for (h, a), score in known.items() if rounds[(h, a)] < round_no]
    zones = project_checkpoint(before, fixture)
    pending = [(g['l'], g['v']) for g in fixture if int(g['f']) >= round_no]
    return {'available': True, 'zones': zones, 'pending': pending, 'played': before}


def build_round_article(zones, pending, fixture, round_no, *, mode='before', played=(), schedule=None, cutoff=8):
    """Genera título, bajada, panorama, cruces y bloques de los 30 equipos.

    No convierte distancias al corte en garantías. La previa usa la foto de inicio;
    el informe actualizado identifica los partidos ya terminados de esta fecha.
    """
    schedule = schedule or {}
    round_no = int(round_no)
    pairs = [tuple(p) for p in pending]
    rounds = {(g['l'], g['v']): int(g['f']) for g in fixture}
    games = [p for p, f in rounds.items() if f == round_no]
    scores = {(canon_club(h), canon_club(a)): (int(gh), int(ga)) for h, a, gh, ga in played or []}
    all_rows = {t: row for base in zones.values() for t, row in base.items()}
    remaining = {t: sum(t in p for p in pairs) for t in all_rows}
    tables = {lab: liga_tabla_df(base) for lab, base in zones.items()}
    states = {t: _season_state({n: int(r.get('pts', 0)) for n, r in base.items()}, remaining, t, cutoff)
              for base in zones.values() for t in base}
    qualified = [editorialize_text(t) for t, s in states.items() if s == 'in']
    eliminated = [editorialize_text(t) for t, s in states.items() if s == 'out']
    counts = sorted(set(remaining.values()))
    left_text = (f'{counts[0]} partidos por equipo' if len(counts) == 1 else
                 f'entre {counts[0]} y {counts[-1]} partidos por equipo') if counts else 'sin partidos pendientes'
    if mode == 'before':
        protagonists = 'Boca, River y los otros 28 equipos' if len(all_rows) == 30 and {'Boca Juniors', 'River Plate'} <= set(all_rows) else f'los {len(all_rows)} equipos'
        title = f'Clausura: las cuentas de {protagonists} antes de la fecha {round_no}'
        scope = f'Foto previa al inicio de la fecha {round_no}, con todas las jornadas anteriores cerradas.'
    else:
        title = f'Clausura: las cuentas actuales de los 30 equipos y los cruces de la fecha {round_no}'
        scope = f'Foto actual de los datos cargados: incluye los finales confirmados de la fecha {round_no} y de otras jornadas.'
    finished = sum(p in scores for p in games)
    subtitle = f'Quedan {left_text}. La situación en las dos zonas, los cruces de la fecha y el fixture de cada equipo rumbo a los octavos.'
    intro = f'Clasifican los {cutoff} primeros de cada zona. '
    intro += ('Garantías comprobadas por puntos y techos restantes: ' + ', '.join(qualified) + '. ') if qualified else 'La comprobación por puntos y techos restantes todavía no marca clasificados. '
    intro += ('Sin chances por ese criterio: ' + ', '.join(eliminated) + '. ') if eliminated else 'La comprobación por puntos y techos restantes todavía no marca eliminados. '
    if mode != 'before':
        intro += f'Esta fecha tiene {finished} de {len(games)} partidos con resultado final confirmado. '
    intro += 'Estar entre los ocho hoy no equivale a tener el pase asegurado; la distancia al corte es una referencia actual y puede cambiar.'
    key_matches = []
    for h, a in games:
        finished_note = ' (ya finalizado)' if mode != 'before' and (h, a) in scores else ''
        lab = next((lab for lab, base in zones.items() if h in base and a in base), None)
        if lab is None:
            key_matches.append(f'{editorialize_text(h)}–{editorialize_text(a)}{finished_note}: interzonal, suma en dos zonas distintas.')
            continue
        table = tables[lab]
        order = list(table['Equipo'])
        hp, ap = order.index(h)+1, order.index(a)+1
        if abs(hp-cutoff) <= 2 or abs(ap-cutoff) <= 2 or abs(int(all_rows[h]['pts'])-int(all_rows[a]['pts'])) <= 3:
            key_matches.append(f'{editorialize_text(h)}–{editorialize_text(a)}{finished_note}: {hp}º contra {ap}º en la zona {lab}, con {all_rows[h]["pts"]} y {all_rows[a]["pts"]} puntos en esta foto.')
    blocks = []
    for lab, table in tables.items():
        base = zones[lab]
        cut_team = table.iloc[min(cutoff, len(table))-1]['Equipo']
        cut_pts = int(base[cut_team]['pts'])
        outside_team = table.iloc[cutoff]['Equipo'] if len(table) > cutoff else None
        outside_pts = int(base[outside_team]['pts']) if outside_team else None
        for row in table.to_dict('records'):
            t, pos, pts, pj = row['Equipo'], int(row['Pos']), int(row['PTS']), int(row['PJ'])
            left, state = remaining[t], states[t]
            if state == 'in':
                situation = 'Tiene asegurado el lugar en los octavos aun con desempate adverso.'
            elif state == 'out':
                situation = f'No puede entrar por puntos: hay al menos {cutoff} rivales fuera de su alcance.'
            elif pos <= cutoff and outside_pts is not None:
                gap = pts-outside_pts
                situation = (f'Está dentro de los ocho y le lleva {gap} puntos al {cutoff+1}º, {editorialize_text(outside_team)}.' if gap else
                             f'Está dentro de los ocho, igualado en puntos con {editorialize_text(outside_team)}; hoy los separa el desempate.')
                situation += ' Esa posición todavía no asegura la clasificación.'
            else:
                gap = cut_pts-pts
                situation = (f'Está a {gap} puntos del {cutoff}º, {editorialize_text(cut_team)}.' if gap else
                             f'Iguala en puntos al {cutoff}º, {editorialize_text(cut_team)}, pero hoy queda afuera por el desempate.')
                situation += ' Alcanzar ese puntaje no garantiza entrar: también puede moverse la línea de clasificación.'
            own = next((p for p in games if t in p), None)
            this_round = 'Sin partido identificado en esta fecha.'
            crossing = ''
            if own:
                h, a = own
                rival = a if h == t else h
                venue = 'recibe a' if h == t else 'visita a'
                when = format_datetime(str(schedule.get(own) or ''))
                this_round = f'{venue.capitalize()} {editorialize_text(rival)}' + (f', {when} (hora argentina).' if when else '. Horario no disponible en la programación cargada.')
                if mode != 'before' and own in scores:
                    gh, ga = scores[own]
                    this_round = f'Ya terminó: {editorialize_text(h)} {gh}–{ga} {editorialize_text(a)}.'
                elif rival in base:
                    diff = pts-int(base[rival]['pts'])
                    crossing = (f'Contra su rival de esta fecha, la diferencia de puntos pasa a {diff+3:+d} si gana, '
                                f'{diff:+d} si empata y {diff-3:+d} si pierde. El signo positivo indica ventaja; el negativo, desventaja. '
                                'Esa cuenta no determina por sí sola el puesto ni la clasificación.')
            own_pending = sorted((p for p in pairs if t in p), key=lambda p: rounds.get(p, 99))
            fixture_text = ', '.join(f'F{rounds.get(p, "?")}: {editorialize_text(p[1] if p[0] == t else p[0])} ({"L" if p[0] == t else "V"})' for p in own_pending)
            blocks.append({'zone': lab, 'team': t, 'objective_state': state, 'points': pts, 'position': pos, 'heading': f'{editorialize_text(t)}: {pts} puntos, {pos}º',
                           'situation': situation, 'games_played': pj, 'remaining': left, 'ceiling': pts+3*left,
                           'this_round': this_round, 'crossing': crossing, 'fixture': fixture_text or 'Sin partidos pendientes.'})
    lines = [f'# {title}', subtitle, scope, intro]
    if key_matches:
        lines += ['## Cruces para seguir', *[f'- {s}' for s in key_matches]]
    for lab in tables:
        lines.append(f'## Zona {lab}')
        for b in blocks:
            if b['zone'] != lab:
                continue
            lines += [f'### {b["heading"]}', b['situation'],
                      f'Tiene {b["games_played"]} partidos jugados, {b["remaining"]} por jugar y un techo de {b["ceiling"]} puntos.',
                      f'**Esta fecha:** {b["this_round"]}']
            if b['crossing']: lines.append(b['crossing'])
            lines.append(f'**Lo que le queda:** {b["fixture"]}')
    lines.append('L = local; V = visitante. El techo supone ganar todos los partidos pendientes y no es una proyección. '
                 'Los estados de garantía y eliminación se prueban por puntos y techos restantes; que el criterio no cierre el objetivo no demuestra que exista un cierre favorable del fixture completo.')
    return {'title': title, 'subtitle': subtitle, 'scope': scope, 'intro': intro,
            'key_matches': key_matches, 'teams': blocks, 'text': '\n\n'.join(lines)}


def build_editorial_piece(article, kind, team, *, previous=None):
    """Formatos breves que reutilizan hechos calculados y no agregan pronósticos."""
    selected = next((b for b in article['teams'] if b['team'] == team), None)
    if selected is None:
        raise ValueError('Equipo fuera de la foto')
    cards = []
    if kind == 'Tarjeta del equipo':
        title = f'{editorialize_text(team)}: las cuentas en 30 segundos'
        cards = [
            {'title': selected['heading'], 'body': selected['situation']},
            {'title': 'Esta fecha', 'body': selected['this_round']},
            {'title': 'Lo que le queda', 'body': selected['fixture']},
            {'title': 'Su máximo posible', 'body': f"{selected['remaining']} partidos por jugar; techo de {selected['ceiling']} puntos. Supone ganar todo y no es una proyección."},
        ]
    elif kind == 'Duelos de la fecha':
        title = 'Los cruces que mueven la pelea'
        cards = [{'title': 'Cruce de la fecha', 'body': s} for s in article['key_matches']]
        if not cards:
            cards = [{'title': 'Sin cruces destacados', 'body': 'No hay un cruce directo identificado por cercanía al corte o por diferencia de hasta tres puntos en esta foto.'}]
    elif kind == 'Radiografía de la zona':
        title = f"Zona {selected['zone']}: quién está adentro y quién viene detrás"
        cards = [{'title': b['heading'], 'body': b['situation']} for b in article['teams'] if b['zone'] == selected['zone']]
    elif kind == 'Semáforo de playoffs':
        title = 'Playoffs: asegurados, eliminados y pelea abierta'
        labels = {'in': 'ASEGURA', 'out': 'ELIMINADO', 'pelea': 'ABIERTO'}
        cards = [{'title': f"{editorialize_text(b['team'])} · {labels[b['objective_state']]}",
                  'body': b['situation'], 'state': b['objective_state']} for b in article['teams']]
    elif kind == 'Antes y después de la fecha':
        if previous is None:
            raise ValueError('No hay una foto previa completa para comparar')
        before = next(b for b in previous['teams'] if b['team'] == team)
        title = f'{editorialize_text(team)}: qué cambió desde el inicio de la fecha'
        cards = [
            {'title': 'Antes', 'body': f"{before['points']} puntos, {before['position']}º; {before['remaining']} partidos por jugar."},
            {'title': 'Ahora', 'body': f"{selected['points']} puntos, {selected['position']}º; {selected['remaining']} partidos por jugar."},
            {'title': 'La diferencia', 'body': f"Tiene {selected['points']-before['points']:+d} puntos respecto de esa foto. La posición también puede cambiar por resultados de otras canchas."},
            {'title': 'Qué sigue', 'body': selected['fixture']},
        ]
    else:
        raise ValueError('Formato desconocido')
    note = ('Foto de los datos cargados. El semáforo de garantía usa puntos y techos restantes; estar dentro hoy no equivale a asegurar. '
            'Un objetivo abierto no demuestra por sí solo un cierre favorable del fixture completo. Las piezas no incluyen probabilidades.')
    text = '\n\n'.join([f'# {title}', article['scope'], *[f"## {c['title']}\n\n{c['body']}" for c in cards], note])
    return {'title': title, 'scope': article['scope'], 'cards': cards, 'note': note, 'text': text}


def piece_html(piece):
    """HTML autónomo, sin imágenes, scripts ni fuentes externas."""
    from html import escape
    palette = {'in': '#15803d', 'out': '#b91c1c', 'pelea': '#b45309'}
    cards = ''.join(f'<article class="card" style="border-top-color:{palette.get(c.get("state"), "#2563eb")}">'
                    f'<h2>{escape(c["title"])}</h2><p>{escape(c["body"])}</p></article>' for c in piece['cards'])
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{escape(piece["title"])}</title><style>'
            'body{margin:0;background:#f1f5f9;color:#0f172a;font:17px/1.55 system-ui,sans-serif;padding:20px}'
            'main{max-width:1000px;margin:auto}h1{font-size:clamp(24px,4vw,36px);line-height:1.2}'
            '.scope,footer{color:#475569;font-size:14px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px}'
            '.card{background:#fff;border-radius:12px;border-top:5px solid;padding:20px;box-shadow:0 2px 8px #0f172a12}'
            '.card h2{font-size:20px;margin:0 0 10px}.card p{margin:0}footer{margin-top:20px}'
            '</style></head><body><main>' + f'<h1>{escape(piece["title"])}</h1><p class="scope">{escape(piece["scope"])}</p>'
            f'<section class="grid">{cards}</section><footer>{escape(piece["note"])}</footer></main></body></html>')
