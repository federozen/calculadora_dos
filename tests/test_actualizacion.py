"""Pruebas sin red: fecha parcial, parser de la jornada y seguridad de la base."""
import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'core'), str(ROOT / 'scripts')]

from lpf_checkpoint import checkpoint_results, cached_results, project_checkpoint
from lpf_data_2026 import LPF_FIXTURE
from lpf_clubs import canon_club
from lpf_fixture_sources import parse_tyc_clausura_results_html, played_pending_from_records
from actualizar_datos import prepare_update


class SnapshotTest(unittest.TestCase):
    def setUp(self):
        self.source = cached_results()
        self.backup = json.loads((ROOT / 'core/data/lpf_last_valid.json').read_text(encoding='utf-8'))

    def test_13_en_curso_12_finalizados_y_river_tres(self):
        self.assertGreaterEqual(len(self.source), 42)
        pairs = {(l,v) for l,v,_,_ in self.source}
        per_round = {n: sum((g['l'],g['v']) in pairs for g in LPF_FIXTURE if g['f']==n)
                     for n in (11,12,13)}
        self.assertEqual(per_round[11],15)
        self.assertEqual(per_round[12],15)
        self.assertGreaterEqual(per_round[13],12)
        zones=project_checkpoint(checkpoint_results()+self.source)
        self.assertGreaterEqual(zones['B']['River Plate']['pj'],13)
        self.assertGreaterEqual(zones['B']['River Plate']['pts'],20)
        remaining=[(g['f'],g['l'],g['v']) for g in LPF_FIXTURE
                   if 'River Plate' in (g['l'],g['v']) and g['f'] > 10 and (g['l'],g['v']) not in pairs]
        self.assertEqual(remaining,[(14,'River Plate','Racing'),
                                    (15,'Boca Juniors','River Plate'),
                                    (16,'Aldosivi','River Plate')]) if zones['B']['River Plate']['pj']==13 else self.assertLessEqual(len(remaining),3)
        self.assertEqual(project_checkpoint(checkpoint_results()+self.source),self.backup['zones'])

    def test_parser_lee_resultados_en_fixture_actual(self):
        html='''<main><h2>El fixture del Torneo Clausura 2026: cruces y fechas</h2>
        <h4>Fecha 13</h4><ul><li>Belgrano 0-3 River</li>
        <li>Sarmiento – Barracas Central</li><li>Newell's – Central Córdoba</li></ul>
        <h4>Fecha 14</h4><li>River – Racing</li>
        <h2>Resultados del Torneo Clausura 2026</h2><h4>Fecha 12</h4>
        <li>River 1-0 Estudiantes (Río Cuarto)</li></main>'''
        records=parse_tyc_clausura_results_html(html,canon_club=canon_club,official_fixture=LPF_FIXTURE)
        played,_pending=played_pending_from_records(records)
        self.assertEqual(len(played),2)
        self.assertIn(('Belgrano','River Plate',0,3),played)
        self.assertNotIn(('Sarmiento','Barracas Central',0,0),played)

    def test_no_contar_los_tres_partidos_de_esta_noche(self):
        now=datetime(2026,10,19,12,0,tzinfo=timezone.utc)
        updated=prepare_update(self.source, self.source, self.backup, now)
        self.assertGreaterEqual(len(updated['played']),192)
        self.assertGreaterEqual(updated['meta']['fecha_min'],12)
        self.assertGreaterEqual(updated['meta']['fecha_max'],13)

    def test_exigir_cierre_fecha_13_despues_del_19(self):
        now=datetime(2026,10,20,12,0,tzinfo=timezone.utc)
        missing_three={('Deportivo Riestra','Unión'),("Newell's Old Boys",'Central Córdoba'),('Sarmiento','Barracas Central')}
        subset=[row for row in self.source if row[:2] not in missing_three]
        with self.assertRaisesRegex(ValueError,'Fecha 13 cerrada'):
            prepare_update(subset,subset,self.backup,now)

    def test_resultado_contradictorio_no_pisa_base(self):
        original=self.source[0]
        changed=(original[0],original[1],original[2]+1,original[3])
        with self.assertRaisesRegex(ValueError,'contradictorio'):
            prepare_update([changed], self.source, self.backup, datetime(2026,10,19,12,tzinfo=timezone.utc))


if __name__=='__main__':
    unittest.main()
