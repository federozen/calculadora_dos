"""Estado confirmado de Copa Argentina 2026 y migración de fotos anteriores."""
from lpf_clubs import canon_club
LPF_RUNTIME_API = 21
ALIVE = ('Banfield', 'Boca Juniors', 'Atlético Tucumán', 'Platense')
ELIMINATED = ('Racing', 'Estudiantes de La Plata', 'Independiente Rivadavia', 'Deportivo Riestra')
UPDATED = '02/10/2026 · cuatro semifinalistas confirmados'
SOURCE = 'Copa Argentina oficial · Boca–Banfield y Atlético Tucumán–Platense'
BOCA_SOURCE = 'https://www.copaargentina.org/es/news/11984_Boca-obtuvo-una-victoria-epica-ante-Racing-y-esta-en-Semifinales.html'
PLATENSE_SOURCE = 'https://www.copaargentina.org/es/news/11988_Platense-hace-historia-vencio-a-Estudiantes-de-La-Plata-y-es-semifinalista-por-primera-vez.html'
SEMIFINALS = (('Boca Juniors','Banfield'), ('Atlético Tucumán','Platense'))


def normalize_alive(values):
    """No reintroduce eliminados; respeta una selección posterior de los vivos."""
    if values is None:
        return list(ALIVE)
    canonical = list(dict.fromkeys(canon_club(v) for v in values))
    return [t for t in ALIVE if t in canonical]


def sync_copa_state(session):
    """Sincroniza lista, editor y ESTADO para que relatos/API usen la misma foto.

    La versión del snapshot se registra por separado: no usa la fecha de una
    descarga para determinar si una foto deportiva es más nueva.
    """
    old_values = session.get('LPF_COPA_ARG_VIVOS')
    text = session.get('lpf_copa_arg_alive_txt')
    revision = session.get('_COPA_CONFIRMED_REVISION')
    if revision != UPDATED:
        # En una primera migración se consideran confirmados todos los semifinalistas.
        values = list(ALIVE)
    else:
        values = normalize_alive(old_values)
        if text is not None:
            values = normalize_alive(str(text).splitlines())
    session['LPF_COPA_ARG_VIVOS'] = values
    session['lpf_copa_arg_alive_txt'] = '\n'.join(values)
    session['LPF_COPA_ARG_UPDATED'] = UPDATED
    session['LPF_COPA_ARG_SOURCE'] = SOURCE
    session['_COPA_CONFIRMED_REVISION'] = UPDATED
    state = session.get('ESTADO')
    if isinstance(state, dict) and state.get('modo') == 'lpf2026':
        session['ESTADO'] = {**state, 'copa_arg_vivos': list(values), 'copa_arg_updated': UPDATED, 'copa_arg_source': SOURCE}
