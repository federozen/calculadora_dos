# Calculadora LPF Clean 4.0.0

Versión limpia de la Calculadora del Fútbol Argentino basada en la rama funcional 3.8.70.

## Qué conserva

Esta edición **no es una Lite recortada**. Conserva el mismo `app.py` y el mismo motor de cálculo que la 3.8.70 que funcionó en producción, incluyendo:

- actualización y auditoría de tablas/resultados;
- TyC Sports como fuente de resultados alternativa, LPF oficial y fallbacks existentes;
- Zona A, Zona B y Tabla Anual;
- Playoffs;
- Libertadores y Sudamericana;
- descenso/promedios;
- Panel por equipo;
- Últimas fechas;
- G/E/P;
- puestos posibles;
- matrices y doble entrada;
- escenarios exactos y condicionales;
- pisos, referencia conservadora y garantía exacta cuando corresponde;
- simulaciones/chances;
- gráficos, termómetros, heatmaps, árboles y visualizaciones editoriales;
- narrativa editorial y auditoría de calidad.

## Qué se eliminó

Sólo material que no hace falta para ejecutar la app en Streamlit: tests, históricos, backups `.bak/.pre`, patches, API/FastAPI, Opta de desarrollo, Mundial, fixtures sintéticos, documentación duplicada y archivos de release.

## Estructura

```text
.
├── app.py                 # UI completa de Streamlit
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
└── core/                  # motor LPF completo
    ├── lpf_*.py
    ├── competition_html_adapters.py
    └── data/
        └── lpf_last_valid.json
```

La raíz queda deliberadamente corta. `app.py` agrega `core/` al `sys.path`, por lo que no hay que configurar `PYTHONPATH` ni instalar el proyecto como paquete.

## Streamlit Cloud

1. Subir **todo el contenido** de este directorio al nuevo repositorio.
2. Main file path: `app.py`.
3. No requiere secrets para iniciar.

## Contratos preservados

- Runtime API: 21
- Public Service: v1
- DataProvider: v2
- Snapshot: schema 3

La única versión pública distinta es `4.0.0-clean`, para diferenciar esta rama del repo histórico 3.8.70.
