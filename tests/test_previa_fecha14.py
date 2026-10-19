"""Cuentas de fecha 14 y certificaciones, sin red ni Streamlit."""
import sys
import unittest
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'core'))
from lpf_checkpoint import checkpoint_results, cached_results, project_checkpoint
from lpf_data_2026 import LPF_FIXTURE
from lpf_editorial_round import round_start_snapshot, round_objective_alerts
from lpf_conditionals import _apply, _rest_after_round, _season_state, _own_code


class PreviaFecha14Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.played = checkpoint_results() + cached_results()
        cls.zones = project_checkpoint(cls.played)
        done = {(h, a) for h, a, *_ in cls.played}
        cls.pending = [(g['l'], g['v']) for g in LPF_FIXTURE if (g['l'], g['v']) not in done]
        cls.round_games = [(g['l'], g['v']) for g in LPF_FIXTURE if g['f'] == 14]
        cls.rest = {team: sum(team in match for match in cls.pending)
                    for base in cls.zones.values() for team in base}

    def test_fecha14_identificada_aunque_fecha13_no_termino(self):
        self.assertEqual(len(self.round_games), 15)
        self.assertEqual(len({team for game in self.round_games for team in game}), 30)
        snapshot = round_start_snapshot(self.played, LPF_FIXTURE, 14)
        self.assertFalse(snapshot['available'])
        self.assertIn('anteriores', snapshot['reason'])
        self.assertEqual(self.rest['River Plate'], 3)
        from lpf_schedule import current_round
        chosen, matches, delayed = current_round(self.pending, LPF_FIXTURE, forzar=14)
        self.assertEqual(chosen, 14)
        self.assertEqual(len(matches), 15)
        self.assertEqual(len(delayed), 3)

    def test_pueden_asegurar_y_quedar_sin_chances(self):
        for team, expected_state in [('Vélez Sarsfield', 'in'),
                                     ('Rosario Central', 'in'),
                                     ('Racing', 'out')]:
            base = next(base for base in self.zones.values() if team in base)
            rep = round_objective_alerts(base, self.rest, self.pending,
                                         self.round_games, team, 8)
            self.assertTrue(rep['available'], (team, rep.get('reason')))
            self.assertEqual({branch['result'] for branch in rep['branches']}, {'G', 'E', 'P'})
            events = [e for e in rep['events'] if e['state'] == expected_state]
            self.assertTrue(events, team)
            self.assertTrue(all(e.get('proof') for e in events))
            self.assertTrue(all(e['rivals_bound'] <= 7 if expected_state == 'in'
                                else e['rivals_bound'] >= 8 for e in events))

    def test_nueve_canchas_no_ocultan_condiciones_de_copas(self):
        from lpf_data_2026 import TABLA_ANUAL_LPF_2026
        from lpf_parsers import parse_tabla_anual
        from lpf_data_quality import derive_opening_from_results, sum_opening_and_zones
        from lpf_editorial_definition import objective_context
        ref = parse_tabla_anual(TABLA_ANUAL_LPF_2026)[0]
        first = {(g['l'], g['v']) for g in LPF_FIXTURE if g['f'] == 1}
        opening, issues = derive_opening_from_results(
            ref, LPF_FIXTURE,
            [row for row in self.played if row[:2] in first], opening_rounds=16)
        self.assertFalse(issues)
        annual = sum_opening_and_zones(opening, self.zones)
        ctx = objective_context(self.zones, objective='Libertadores',
                                direct_annual=annual, opening_rounds=16,
                                camps=('Belgrano', '', ''))
        answer = round_objective_alerts(ctx['base'], self.rest, self.pending,
                                        self.round_games, 'Lanús', ctx['cutoff'])
        self.assertTrue(answer['available'])
        self.assertTrue(answer['events'])
        self.assertTrue(all(x.get('proof') for x in answer['events']))

    def test_todos_los_caminos_publicados_son_suficientes(self):
        """Probar cada camino: condiciones omitidas pueden terminar como quieran."""
        teams = ['Vélez Sarsfield', 'Rosario Central', 'Racing', 'Banfield']
        for team in teams:
            base = next(base for base in self.zones.values() if team in base)
            rep = round_objective_alerts(base, self.rest, self.pending,
                                         self.round_games, team, 8)
            own = next(game for game in self.round_games if team in game)
            rest = _rest_after_round(base, self.rest, self.round_games)
            others = [game for game in self.round_games if game != own]
            for event in rep.get('events', []):
                conditions = {tuple(item['match']): item['allowed']
                              for item in event['conditions']}
                # Varios desenlaces de las canchas omitidas, no solamente empates.
                for choice in ('L', 'E', 'V'):
                    codes = [next(iter(conditions[g])) if g in conditions else choice
                             for g in others]
                    own_code = _own_code(own, team, event['own_result'])
                    points = _apply(base, [own, *others], [own_code, *codes])
                    self.assertEqual(_season_state(points, rest, team, 8), event['state'],
                                     (team, event, choice))


if __name__ == '__main__':
    unittest.main()
