# Calculadora LPF 2026 · Streamlit (3.8.74)

Calculadora editorial de la Liga Profesional 2026: playoffs por zonas, Tabla Anual,
Libertadores, Sudamericana, descenso (Tabla General + promedios), escenarios, previas
y textos listos para la nota.

## Estructura

```text
.
├── calculadora_futbol_argentino.py   # la app (Streamlit Cloud: Main file)
├── core/                             # motor de cálculo (lpf_*.py)
│   └── data/                         # última foto válida y resultados publicados
├── requirements.txt
├── .streamlit/config.toml
├── scripts/actualizar_datos.py       # actualización automática sin navegador
└── .github/workflows/actualizar-datos.yml
```

## Correrla

```bash
pip install -r requirements.txt
streamlit run calculadora_futbol_argentino.py
```

En Streamlit Cloud: *Main file path* = `calculadora_futbol_argentino.py`. No requiere secrets
(la API key de Claude es opcional y se carga en Datos → Ajustes).

## Navegación

- **Equipo y objetivo** se eligen una sola vez en el panel lateral; todas las páginas los usan.
- **Actualizar a hoy** siempre a mano en el panel lateral, con el estado de los datos.
- Menú superior: **Equipo** (Panel, Puntos por objetivo, Escenarios) · **Competencia**
  (Previa de la fecha, Últimas fechas, Visualizaciones) · **Redacción** (Informe por equipo,
  Cierre por zona, Consultas y chat) · **Datos** (Cargar y actualizar, Auditoría y reglas, Ajustes).

## Datos al día

`.github/workflows/actualizar-datos.yml` corre cada 2 horas (y a mano desde *Actions → Run workflow*).
Ejecuta la misma lógica del botón «Actualizar a hoy» y, si todo cierra, guarda en `core/data/`
los resultados y la foto de tablas. Streamlit Cloud toma el commit y la app abre ya al día.
Si una corrida falla, no toca nada. Si la app abre con datos atrasados respecto del calendario,
intenta actualizar sola una vez por sesión.

## Cuentas de las últimas fechas

- Con **8 partidos o menos** por jugar, playoffs, copas y descenso usan el motor exacto
  (mínimo que asegura y escalera de puntos). Con **4 o menos**, modo definición.
- Cada total que «depende de otros» indica la condición exacta (cuántos rivales pueden llegar
  y cuántos no deben llegar) y dos cierres reales del fixture: uno en que entra y otro en que queda afuera.
- Las probabilidades siguen siendo simulaciones rotuladas como ESTIMADO.
- **Redacción → Cierre por zona**: pieza lista para la nota con cada equipo en orden de tabla,
  sus puntos, lectura de chances, lo que le queda por jugar y los puntos de cada rival entre
  paréntesis. Opcional: mínimo exacto que asegura el pase. Incluye texto para copiar y .md.

## Versión web (Vercel)

La misma app corre en el navegador desde el repositorio de Vercel (stlite + proxy).
El archivo de la app y la carpeta `core/` son idénticos en ambos repositorios.
