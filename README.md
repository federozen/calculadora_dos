# Calculadora LPF Lite

Versión liviana y separada de la calculadora grande. Está pensada para un GitHub nuevo y un deploy rápido en Streamlit.

## Qué conserva

- actualización de resultados del Clausura 2026 desde TyC Sports;
- tablas Zona A y Zona B reconstruidas desde marcadores explícitos;
- Tabla Anual = Apertura fijo + Clausura vivo;
- panel por equipo con corte actual, máximo, forma y próximo partido;
- chances estimadas de Playoffs y escenario G/E/P por Monte Carlo;
- foto actual de Libertadores/Sudamericana con campeones configurables;
- promedios y descenso;
- auditoría mínima de cobertura.

## Qué se eliminó a propósito

No incluye API/FastAPI, Opta, Mundial, ESPN, FutbolArgentino.com, crawler LPF, MILP/SciPy, matplotlib, reconciliación histórica, tests masivos, backups, patches ni documentación de versiones anteriores.

La **referencia segura conservadora** no reemplaza la garantía exacta del proyecto completo. Las chances y G/E/P de esta edición son **estimadas por Monte Carlo**.

## Ejecutar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy en Streamlit Community Cloud

Elegir `app.py` como archivo principal. No requiere variables de entorno ni secrets.

## Fuente

Los resultados se leen de la página pública de fixture/resultados de TyC Sports y se validan contra el fixture canónico 2026 incluido en `lpf_lite/data.py`. Si la fuente no responde, se usa un fallback parcial incluido y la interfaz lo advierte explícitamente.
