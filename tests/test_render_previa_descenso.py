"""Regresión: la pantalla de previa pasa los seis argumentos del motor conjunto.

No importa la app Streamlit ni ejecuta red. Se prueba la propia función de
presentación aislada para evitar que el motor pase los tests pero falle la UI.
"""
import ast
import logging
import sys
import unittest
from contextlib import nullcontext
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'core'))
from lpf_editorial_round import round_relegation_alerts


class FakeStreamlit:
    def spinner(self, *_args, **_kw):
        return nullcontext()

    def expander(self, *_args, **_kw):
        return nullcontext()

    def columns(self, number):
        return [SimpleNamespace(metric=lambda *a, **k: None) for _ in range(number)]


class RoundRenderRegression(unittest.TestCase):
    def _renderer(self, descent):
        source = (ROOT / 'calculadora_futbol_argentino.py').read_text(encoding='utf-8')
        tree = ast.parse(source)
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                    and n.name == '_render_round_definition_alerts')
        module = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
        zones = {'A': {
            'Barracas Central': {'pts': 15, 'pj': 13, 'gf': 12, 'gc': 14, 'dg': -2},
            'Estudiantes de Río Cuarto': {'pts': 8, 'pj': 13, 'gf': 9, 'gc': 19, 'dg': -10},
        }}
        annual = {
            'Barracas Central': {'pts': 30, 'pj': 29, 'gf': 20, 'gc': 18, 'dg': 2},
            'Estudiantes de Río Cuarto': {'pts': 14, 'pj': 29, 'gf': 15, 'gc': 35, 'dg': -20},
        }
        averages = {'Barracas Central': (46, 45), 'Estudiantes de Río Cuarto': (14, 29)}
        capture = []

        def call_descent(*args):
            capture.append(args)
            return descent(*args)

        namespace = {
            '_lpf_service_snapshot': lambda E: {'zones': zones, 'annual': annual,
                'qualification_inputs': {'champions': {}, 'international_champions': {}}},
            'snapshot_average_totals': lambda _: averages,
            '_lpf_domain_ready': lambda E, domain: (True, []),
            '_editorial_objective_context': lambda z, **kw:
                {'base': annual if kw.get('objective') != 'Playoffs' else zones['A'],
                 'cutoff': 1, 'direct': []},
            'round_objective_alerts': lambda *a: {'available': True, 'events': [], 'branches': []},
            'round_relegation_alerts': call_descent,
            'LPF_APERTURA_PJ': 16,
            'editorialize_text': str,
            'st': FakeStreamlit(),
            'ui_info': lambda *a, **k: None,
            'ui_markdown': lambda *a, **k: None,
            'ui_caption': lambda *a, **k: None,
            'ui_dataframe': lambda *a, **k: None,
            'pd': SimpleNamespace(DataFrame=lambda value: value),
            'lpf_jornada_actual': lambda pending: (14, pending, []),
        }
        exec(compile(module, str(ROOT / 'calculadora_futbol_argentino.py'), 'exec'), namespace)
        return namespace['_render_round_definition_alerts'], zones, averages, capture

    def test_descenso_recibe_promedios_y_partidos_en_orden(self):
        def descent(annual, remaining, pending, averages, games, team):
            self.assertIn(team, annual)
            self.assertEqual(set(averages), set(annual))
            self.assertEqual(pending, games)
            self.assertEqual(remaining[team], 1)
            return {'available':True, 'events':[], 'branches':[]}
        renderer, zones, averages, calls = self._renderer(descent)
        result = renderer({'n_anual':1, 'n_prom':1}, zones=zones,
                          pending=[('Barracas Central','Estudiantes de Río Cuarto')],
                          games=[('Barracas Central','Estudiantes de Río Cuarto')],round_no=14)
        self.assertIn('fecha 14', result.lower())
        self.assertEqual(len(calls), 2)
        self.assertIs(calls[0][3], averages)

    def test_descenso_falla_pero_otras_competiciones_siguen(self):
        def bad_descent(*args):
            raise ValueError('ejemplo: solver no disponible')
        renderer, zones, _, calls = self._renderer(bad_descent)
        with self.assertLogs(level=logging.ERROR):
            result = renderer({'n_anual':1,'n_prom':1}, zones=zones,
                              pending=[('Barracas Central','Estudiantes de Río Cuarto')],
                              games=[('Barracas Central','Estudiantes de Río Cuarto')],round_no=14)
        self.assertIn('Playoffs:', result)
        self.assertIn('Descenso:', result)
        self.assertIn('No se pudo certificar', result)
        self.assertEqual(len(calls), 2)

    def test_motor_descenso_con_seis_argumentos_sinteticos(self):
        annual = {'A':{'pts':9,'pj':14},'B':{'pts':10,'pj':14},'C':{'pts':15,'pj':15}}
        rest={'A':1,'B':1,'C':0}
        averages={'A':(11,20),'B':(12,20),'C':(40,30)}
        game=[('A','B')]
        answer=round_relegation_alerts(annual,rest,game,averages,game,'A')
        self.assertTrue(answer['available'])
        self.assertIn(answer.get('resolved'), ('in','out'))


if __name__ == '__main__':
    unittest.main()
