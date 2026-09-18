from __future__ import annotations

__version__ = "1.0.1"


# ===== data.py =====
TOTAL_ROUNDS = 16
APERTURA_ROUNDS = 16
APERTURA_CHAMPION = "Belgrano"
TYC_RESULTS_URL = "https://www.tycsports.com/liga-profesional-de-futbol/fixture-del-clausura-2026-calendario-de-partidos-y-resultados-id750943.html"

CLUB_ALIASES = {'Aldosivi': ['aldosivi'],
 'Argentinos Juniors': ['argentinos', 'argentinos jrs', 'aa argentinos juniors'],
 'Atlético Tucumán': ['atl tucuman', 'atletico tucuman', 'tucuman', 'ca tucuman'],
 'Banfield': ['banfield', 'ca banfield'],
 'Barracas Central': ['barracas', 'barracas central'],
 'Belgrano': ['belgrano', 'ca belgrano'],
 'Boca Juniors': ['boca', 'boca jrs', 'boca juniors', 'ca boca juniors'],
 'Central Córdoba': ['central cordoba', 'central cordoba sde', 'ca central cordoba'],
 'Defensa y Justicia': ['defensa', 'defensa y justicia'],
 'Deportivo Riestra': ['riestra', 'deportivo riestra'],
 'Estudiantes de La Plata': ['estudiantes',
                             'estudiantes lp',
                             'estudiantes de la plata',
                             'edlp',
                             'estudiantes (la plata)'],
 'Estudiantes de Río Cuarto': ['estudiantes rc',
                               'estudiantes de rio cuarto',
                               'estudiantes (rc)',
                               'estudiantes rio cuarto',
                               'estudiantes (río cuarto)',
                               'estudiantes (rio cuarto)'],
 'Gimnasia La Plata': ['gimnasia',
                       'gimnasia lp',
                       'gimnasia y esgrima la plata',
                       'gelp',
                       'gimnasia la plata',
                       'gimnasia (la plata)',
                       'gimnasia y esgrima'],
 'Gimnasia de Mendoza': ['gimnasia m',
                         'gimnasia (m)',
                         'gimnasia y esgrima de mendoza',
                         'gimnasia mendoza',
                         'gimnasia mza',
                         'gimnasia (mza)',
                         'gimnasia (mza )',
                         'gimnasia de mza',
                         'gimnasia y esgrima mendoza'],
 'Godoy Cruz': ['godoy cruz', 'godoy'],
 'Huracán': ['huracan', 'ca huracan'],
 'Independiente': ['independiente', 'ca independiente'],
 'Independiente Rivadavia': ['independiente riv',
                             'independiente rivadavia',
                             'ind rivadavia',
                             'sportivo independiente rivadavia'],
 'Instituto': ['instituto', 'instituto atletico central cordoba'],
 'Lanús': ['lanus', 'ca lanus'],
 "Newell's Old Boys": ['newells', 'newell s old boys', 'newells old boys', 'noob'],
 'Platense': ['platense', 'ca platense'],
 'Racing': ['racing', 'racing club'],
 'River Plate': ['river', 'river plate', 'ca river plate'],
 'Rosario Central': ['central', 'rosario central', 'ca rosario central'],
 'San Lorenzo': ['san lorenzo', 'san lorenzo de almagro'],
 'Sarmiento': ['sarmiento', 'sarmiento junin'],
 'Talleres': ['talleres', 'talleres cordoba'],
 'Tigre': ['tigre', 'ca tigre'],
 'Unión': ['union', 'union santa fe'],
 'Vélez Sarsfield': ['velez', 'velez sarsfield', 'ca velez sarsfield']}

ZONE_A = ['Deportivo Riestra',
 'Boca Juniors',
 'Estudiantes de La Plata',
 'Independiente',
 "Newell's Old Boys",
 'Talleres',
 'Vélez Sarsfield',
 'Instituto',
 'Platense',
 'Unión',
 'Lanús',
 'San Lorenzo',
 'Gimnasia de Mendoza',
 'Central Córdoba',
 'Defensa y Justicia']

ZONE_B = ['River Plate',
 'Barracas Central',
 'Racing',
 'Gimnasia La Plata',
 'Belgrano',
 'Rosario Central',
 'Estudiantes de Río Cuarto',
 'Tigre',
 'Sarmiento',
 'Argentinos Juniors',
 'Huracán',
 'Banfield',
 'Atlético Tucumán',
 'Independiente Rivadavia',
 'Aldosivi']

FIXTURE = [{'f': 1, 'tipo': 'inter', 'zona': None, 'l': 'Defensa y Justicia', 'v': 'Aldosivi'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Boca Juniors'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': 'Independiente'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Talleres'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'Instituto'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': 'Unión'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'San Lorenzo'},
 {'f': 1, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': 'Central Córdoba'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Barracas Central'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Gimnasia La Plata'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'Rosario Central'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Tigre'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'Argentinos Juniors'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Banfield'},
 {'f': 1, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'Independiente Rivadavia'},
 {'f': 2, 'tipo': 'inter', 'zona': None, 'l': 'Central Córdoba', 'v': 'Atlético Tucumán'},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': 'Gimnasia de Mendoza'},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Lanús'},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': 'Platense'},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Vélez Sarsfield'},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': "Newell's Old Boys"},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Estudiantes de La Plata'},
 {'f': 2, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': 'Deportivo Riestra'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Huracán'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'Sarmiento'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'Belgrano'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Racing'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'River Plate'},
 {'f': 2, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Aldosivi'},
 {'f': 3, 'tipo': 'inter', 'zona': None, 'l': 'Deportivo Riestra', 'v': 'Barracas Central'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': 'Defensa y Justicia'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Boca Juniors'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'Independiente'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': 'Talleres'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'Instituto'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': 'Unión'},
 {'f': 3, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'San Lorenzo'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'Gimnasia La Plata'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Rosario Central'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Tigre'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'Argentinos Juniors'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Banfield'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'Independiente Rivadavia'},
 {'f': 3, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Atlético Tucumán'},
 {'f': 4, 'tipo': 'inter', 'zona': None, 'l': 'San Lorenzo', 'v': 'Huracán'},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Central Córdoba'},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': 'Gimnasia de Mendoza'},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Lanús'},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': 'Platense'},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Vélez Sarsfield'},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': "Newell's Old Boys"},
 {'f': 4, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Estudiantes de La Plata'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'Sarmiento'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'Belgrano'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Racing'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'River Plate'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Aldosivi'},
 {'f': 4, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'Barracas Central'},
 {'f': 5, 'tipo': 'inter', 'zona': None, 'l': 'Estudiantes de La Plata', 'v': 'Gimnasia La Plata'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Deportivo Riestra'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'Defensa y Justicia'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': 'Boca Juniors'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'Independiente'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': 'Talleres'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'Instituto'},
 {'f': 5, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': 'Unión'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Rosario Central'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'Tigre'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Argentinos Juniors'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Banfield'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'Independiente Rivadavia'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Atlético Tucumán'},
 {'f': 5, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'Huracán'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'River Plate', 'v': 'Vélez Sarsfield'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Barracas Central', 'v': 'Platense'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Talleres', 'v': 'Rosario Central'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Sarmiento', 'v': 'Estudiantes de La Plata'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Belgrano', 'v': 'Defensa y Justicia'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Lanús', 'v': 'Argentinos Juniors'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Racing', 'v': 'Boca Juniors'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Independiente', 'v': 'Independiente Rivadavia'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Aldosivi', 'v': 'Unión'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Atlético Tucumán', 'v': 'Instituto'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Estudiantes de Río Cuarto', 'v': 'San Lorenzo'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Gimnasia La Plata', 'v': 'Gimnasia de Mendoza'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Tigre', 'v': 'Central Córdoba'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': 'Huracán', 'v': 'Deportivo Riestra'},
 {'f': 6, 'tipo': 'inter', 'zona': None, 'l': "Newell's Old Boys", 'v': 'Banfield'},
 {'f': 7, 'tipo': 'inter', 'zona': None, 'l': 'Unión', 'v': 'Sarmiento'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': 'San Lorenzo'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Central Córdoba'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': 'Gimnasia de Mendoza'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Lanús'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': 'Platense'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Vélez Sarsfield'},
 {'f': 7, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': "Newell's Old Boys"},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'Belgrano'},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Racing'},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'River Plate'},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Aldosivi'},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'Barracas Central'},
 {'f': 7, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Gimnasia La Plata'},
 {'f': 8, 'tipo': 'inter', 'zona': None, 'l': 'Rosario Central', 'v': "Newell's Old Boys"},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'Estudiantes de La Plata'},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': 'Deportivo Riestra'},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'Defensa y Justicia'},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': 'Boca Juniors'},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'Independiente'},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': 'Talleres'},
 {'f': 8, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Instituto'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'Tigre'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Argentinos Juniors'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'Banfield'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Independiente Rivadavia'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Atlético Tucumán'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'Huracán'},
 {'f': 8, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Sarmiento'},
 {'f': 9, 'tipo': 'inter', 'zona': None, 'l': 'Instituto', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Unión'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': 'San Lorenzo'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Central Córdoba'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': 'Gimnasia de Mendoza'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Lanús'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': 'Platense'},
 {'f': 9, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Vélez Sarsfield'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'Belgrano'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Racing'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'River Plate'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Aldosivi'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'Barracas Central'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Gimnasia La Plata'},
 {'f': 9, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'Rosario Central'},
 {'f': 10, 'tipo': 'inter', 'zona': None, 'l': 'Vélez Sarsfield', 'v': 'Tigre'},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': "Newell's Old Boys"},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'Estudiantes de La Plata'},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': 'Deportivo Riestra'},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'Defensa y Justicia'},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': 'Boca Juniors'},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Independiente'},
 {'f': 10, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': 'Talleres'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Argentinos Juniors'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'Banfield'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Independiente Rivadavia'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'Atlético Tucumán'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Huracán'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Sarmiento'},
 {'f': 10, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 11, 'tipo': 'inter', 'zona': None, 'l': 'Talleres', 'v': 'Belgrano'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': 'Instituto'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Unión'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': 'San Lorenzo'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Central Córdoba'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': 'Gimnasia de Mendoza'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Lanús'},
 {'f': 11, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'Platense'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Racing'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'River Plate'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Aldosivi'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'Barracas Central'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Gimnasia La Plata'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'Rosario Central'},
 {'f': 11, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Tigre'},
 {'f': 12, 'tipo': 'inter', 'zona': None, 'l': 'Platense', 'v': 'Argentinos Juniors'},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'Vélez Sarsfield'},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': "Newell's Old Boys"},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'Estudiantes de La Plata'},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': 'Deportivo Riestra'},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Defensa y Justicia'},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': 'Boca Juniors'},
 {'f': 12, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Independiente'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'Banfield'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Independiente Rivadavia'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'Atlético Tucumán'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Huracán'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'Sarmiento'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 12, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Belgrano'},
 {'f': 13, 'tipo': 'inter', 'zona': None, 'l': 'Racing', 'v': 'Independiente'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Talleres'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': 'Instituto'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Unión'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': 'San Lorenzo'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Central Córdoba'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'Gimnasia de Mendoza'},
 {'f': 13, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': 'Lanús'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'River Plate'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Aldosivi'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'Barracas Central'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Gimnasia La Plata'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'Rosario Central'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Tigre'},
 {'f': 13, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'Argentinos Juniors'},
 {'f': 14, 'tipo': 'inter', 'zona': None, 'l': 'Banfield', 'v': 'Lanús'},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'Gimnasia de Mendoza', 'v': 'Platense'},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'Vélez Sarsfield'},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': "Newell's Old Boys"},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Estudiantes de La Plata'},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': 'Deportivo Riestra'},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Defensa y Justicia'},
 {'f': 14, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': 'Boca Juniors'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Independiente Rivadavia'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'Atlético Tucumán'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Huracán'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'Sarmiento'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'Belgrano'},
 {'f': 14, 'tipo': 'zona', 'zona': 'B', 'l': 'River Plate', 'v': 'Racing'},
 {'f': 15, 'tipo': 'inter', 'zona': None, 'l': 'Boca Juniors', 'v': 'River Plate'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': 'Defensa y Justicia', 'v': 'Independiente'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': 'Deportivo Riestra', 'v': 'Talleres'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': 'Estudiantes de La Plata', 'v': 'Instituto'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': "Newell's Old Boys", 'v': 'Unión'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': 'Vélez Sarsfield', 'v': 'San Lorenzo'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': 'Platense', 'v': 'Central Córdoba'},
 {'f': 15, 'tipo': 'zona', 'zona': 'A', 'l': 'Lanús', 'v': 'Gimnasia de Mendoza'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Racing', 'v': 'Aldosivi'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Belgrano', 'v': 'Barracas Central'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Estudiantes de Río Cuarto', 'v': 'Gimnasia La Plata'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Sarmiento', 'v': 'Rosario Central'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Huracán', 'v': 'Tigre'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Atlético Tucumán', 'v': 'Argentinos Juniors'},
 {'f': 15, 'tipo': 'zona', 'zona': 'B', 'l': 'Independiente Rivadavia', 'v': 'Banfield'},
 {'f': 16, 'tipo': 'inter', 'zona': None, 'l': 'Gimnasia de Mendoza', 'v': 'Independiente Rivadavia'},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'Central Córdoba', 'v': 'Lanús'},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'San Lorenzo', 'v': 'Platense'},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'Unión', 'v': 'Vélez Sarsfield'},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'Instituto', 'v': "Newell's Old Boys"},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'Talleres', 'v': 'Estudiantes de La Plata'},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'Independiente', 'v': 'Deportivo Riestra'},
 {'f': 16, 'tipo': 'zona', 'zona': 'A', 'l': 'Boca Juniors', 'v': 'Defensa y Justicia'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Banfield', 'v': 'Atlético Tucumán'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Argentinos Juniors', 'v': 'Huracán'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Tigre', 'v': 'Sarmiento'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Rosario Central', 'v': 'Estudiantes de Río Cuarto'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Gimnasia La Plata', 'v': 'Belgrano'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Barracas Central', 'v': 'Racing'},
 {'f': 16, 'tipo': 'zona', 'zona': 'B', 'l': 'Aldosivi', 'v': 'River Plate'}]

OPENING = {'Aldosivi': {'dg': -13, 'ga': 19, 'gf': 6, 'pj': 16, 'pts': 8},
 'Argentinos Juniors': {'dg': 4, 'ga': 13, 'gf': 17, 'pj': 16, 'pts': 29},
 'Atlético Tucumán': {'dg': -5, 'ga': 20, 'gf': 15, 'pj': 16, 'pts': 14},
 'Banfield': {'dg': -2, 'ga': 19, 'gf': 17, 'pj': 16, 'pts': 18},
 'Barracas Central': {'dg': 0, 'ga': 15, 'gf': 15, 'pj': 16, 'pts': 21},
 'Belgrano': {'dg': 4, 'ga': 13, 'gf': 17, 'pj': 16, 'pts': 26},
 'Boca Juniors': {'dg': 13, 'ga': 9, 'gf': 22, 'pj': 16, 'pts': 30},
 'Central Córdoba': {'dg': -10, 'ga': 21, 'gf': 11, 'pj': 16, 'pts': 16},
 'Defensa y Justicia': {'dg': -3, 'ga': 21, 'gf': 18, 'pj': 16, 'pts': 19},
 'Deportivo Riestra': {'dg': -7, 'ga': 12, 'gf': 5, 'pj': 16, 'pts': 11},
 'Estudiantes de La Plata': {'dg': 12, 'ga': 7, 'gf': 19, 'pj': 16, 'pts': 31},
 'Estudiantes de Río Cuarto': {'dg': -19, 'ga': 24, 'gf': 5, 'pj': 16, 'pts': 5},
 'Gimnasia La Plata': {'dg': 0, 'ga': 19, 'gf': 19, 'pj': 16, 'pts': 26},
 'Gimnasia de Mendoza': {'dg': -8, 'ga': 22, 'gf': 14, 'pj': 16, 'pts': 19},
 'Huracán': {'dg': 4, 'ga': 13, 'gf': 17, 'pj': 16, 'pts': 22},
 'Independiente': {'dg': 4, 'ga': 20, 'gf': 24, 'pj': 16, 'pts': 24},
 'Independiente Rivadavia': {'dg': 14, 'ga': 15, 'gf': 29, 'pj': 16, 'pts': 34},
 'Instituto': {'dg': 0, 'ga': 17, 'gf': 17, 'pj': 16, 'pts': 21},
 'Lanús': {'dg': 3, 'ga': 15, 'gf': 18, 'pj': 16, 'pts': 24},
 "Newell's Old Boys": {'dg': -12, 'ga': 27, 'gf': 15, 'pj': 16, 'pts': 15},
 'Platense': {'dg': -5, 'ga': 15, 'gf': 10, 'pj': 16, 'pts': 16},
 'Racing': {'dg': 2, 'ga': 15, 'gf': 17, 'pj': 16, 'pts': 21},
 'River Plate': {'dg': 10, 'ga': 12, 'gf': 22, 'pj': 16, 'pts': 29},
 'Rosario Central': {'dg': 4, 'ga': 16, 'gf': 20, 'pj': 16, 'pts': 28},
 'San Lorenzo': {'dg': 0, 'ga': 14, 'gf': 14, 'pj': 16, 'pts': 22},
 'Sarmiento': {'dg': -7, 'ga': 20, 'gf': 13, 'pj': 16, 'pts': 19},
 'Talleres': {'dg': 4, 'ga': 13, 'gf': 17, 'pj': 16, 'pts': 26},
 'Tigre': {'dg': 3, 'ga': 15, 'gf': 18, 'pj': 16, 'pts': 20},
 'Unión': {'dg': 4, 'ga': 20, 'gf': 24, 'pj': 16, 'pts': 21},
 'Vélez Sarsfield': {'dg': 6, 'ga': 12, 'gf': 18, 'pj': 16, 'pts': 28}}

PREVIOUS_AVERAGES = {'Aldosivi': (33, 32),
 'Argentinos Juniors': (113, 73),
 'Atlético Tucumán': (84, 73),
 'Banfield': (76, 73),
 'Barracas Central': (98, 73),
 'Belgrano': (86, 73),
 'Boca Juniors': (129, 73),
 'Central Córdoba': (84, 73),
 'Defensa y Justicia': (96, 73),
 'Deportivo Riestra': (100, 73),
 'Estudiantes de La Plata': (105, 73),
 'Estudiantes de Río Cuarto': (0, 0),
 'Gimnasia La Plata': (86, 73),
 'Gimnasia de Mendoza': (0, 0),
 'Huracán': (109, 73),
 'Independiente': (110, 73),
 'Independiente Rivadavia': (89, 73),
 'Instituto': (87, 73),
 'Lanús': (109, 73),
 "Newell's Old Boys": (82, 73),
 'Platense': (92, 73),
 'Racing': (123, 73),
 'River Plate': (123, 73),
 'Rosario Central': (113, 73),
 'San Lorenzo': (96, 73),
 'Sarmiento': (70, 73),
 'Talleres': (106, 73),
 'Tigre': (88, 73),
 'Unión': (99, 73),
 'Vélez Sarsfield': (116, 73)}


FALLBACK_RESULTS = [(1, 'Belgrano', 'Rosario Central', 2, 1),
 (1, 'Sarmiento', 'Argentinos Juniors', 2, 3),
 (1, 'Defensa y Justicia', 'Aldosivi', 1, 1),
 (1, 'Gimnasia de Mendoza', 'Central Córdoba', 1, 0),
 (1, 'Racing', 'Gimnasia La Plata', 2, 1),
 (1, 'Vélez Sarsfield', 'Instituto', 1, 0),
 (1, 'Huracán', 'Banfield', 1, 0),
 (1, 'Platense', 'Unión', 2, 2),
 (1, 'Estudiantes de Río Cuarto', 'Tigre', 1, 0),
 (1, "Newell's Old Boys", 'Talleres', 1, 0),
 (1, 'River Plate', 'Barracas Central', 0, 1),
 (1, 'Lanús', 'San Lorenzo', 1, 0),
 (1, 'Atlético Tucumán', 'Independiente Rivadavia', 0, 0),
 (1, 'Estudiantes de La Plata', 'Independiente', 0, 2),
 (1, 'Deportivo Riestra', 'Boca Juniors', 3, 0),
 (2, 'Banfield', 'Sarmiento', 3, 2),
 (2, 'San Lorenzo', 'Gimnasia de Mendoza', 1, 0),
 (2, 'Rosario Central', 'Racing', 0, 0),
 (2, 'Argentinos Juniors', 'Estudiantes de Río Cuarto', 3, 0),
 (2, 'Barracas Central', 'Aldosivi', 1, 0),
 (2, 'Defensa y Justicia', 'Deportivo Riestra', 2, 1),
 (2, 'Gimnasia La Plata', 'River Plate', 1, 0),
 (2, 'Instituto', 'Platense', 2, 1),
 (2, 'Independiente Rivadavia', 'Huracán', 2, 1),
 (2, 'Talleres', 'Vélez Sarsfield', 1, 3),
 (2, 'Independiente', "Newell's Old Boys", 1, 0),
 (2, 'Central Córdoba', 'Atlético Tucumán', 0, 2),
 (3, 'Gimnasia de Mendoza', 'Unión', 2, 0),
 (3, 'Estudiantes de Río Cuarto', 'Banfield', 0, 0),
 (3, 'Belgrano', 'Argentinos Juniors', 0, 1),
 (3, 'Estudiantes de La Plata', 'Defensa y Justicia', 3, 0),
 (3, 'Racing', 'Tigre', 1, 3),
 (3, 'Deportivo Riestra', 'Barracas Central', 0, 1),
 (3, 'Aldosivi', 'Gimnasia La Plata', 1, 2),
 (3, "Newell's Old Boys", 'Boca Juniors', 2, 2),
 (3, 'River Plate', 'Rosario Central', 0, 1),
 (3, 'Lanús', 'Instituto', 0, 1),
 (3, 'Sarmiento', 'Independiente Rivadavia', 2, 1),
 (3, 'Platense', 'Talleres', 0, 4),
 (3, 'Vélez Sarsfield', 'Independiente', 1, 0),
 (3, 'Huracán', 'Atlético Tucumán', 0, 0),
 (3, 'Central Córdoba', 'San Lorenzo', 1, 0),
 (2, 'Boca Juniors', 'Estudiantes de La Plata', 1, 0),
 (2, 'Tigre', 'Belgrano', 0, 0),
 (2, 'Unión', 'Lanús', 2, 1),
 (4, 'Rosario Central', 'Aldosivi', 2, 1),
 (4, 'Independiente Rivadavia', 'Estudiantes de Río Cuarto', 2, 1),
 (4, 'Deportivo Riestra', 'Estudiantes de La Plata', 2, 0),
 (4, 'Atlético Tucumán', 'Sarmiento', 1, 2)]


# ===== sources.py =====
import re
import unicodedata
from typing import Iterable

import requests
from bs4 import BeautifulSoup



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


# ===== engine.py =====
from collections import defaultdict
from fractions import Fraction

import pandas as pd


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


# ===== simulation.py =====
from collections import defaultdict

import numpy as np



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


# ===== Streamlit UI =====
import pandas as pd
import streamlit as st


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
