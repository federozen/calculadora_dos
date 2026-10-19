# Calculadora LPF 2026 · Streamlit Cloud (3.8.90)

Calculadora editorial de la Liga Profesional: playoffs por zonas, Tabla Anual, Libertadores, Sudamericana, descenso (Tabla General + promedios), escenarios, previas y textos listos para publicar.

## Corrección 3.8.90: TypeError en Previa de la fecha

Se corrigió la llamada de la pantalla «Previa de la fecha» a
`round_relegation_alerts(annual, remaining, pending, averages, games, team)`.
La versión anterior omitía `averages`, por lo que Streamlit Cloud lanzaba un
`TypeError` antes de terminar de mostrar las definiciones.

El fallo individual de la comprobación de descenso ahora deja ese objetivo
como **sin certificación** (con detalle en logs) y no impide consultar los
escenarios de playoffs y cupos internacionales. Esto no convierte ningún
resultado de descenso en una predicción ni reemplaza el solver exacto.

Se añadieron tres pruebas de integración del render de previa, incluida
la propagación de los seis argumentos y la recuperación ante errores.
Las 12 pruebas automáticas locales pasan.

## Nuevo en 3.8.89: previa completa y condiciones de la fecha 14

En **Redacción → Previa de la fecha**, el nuevo bloque «Qué puede definirse» aparece
antes de las fichas individuales. Por defecto propone la fecha 14 cuando quedan
hasta tres partidos de una fecha 13 casi terminada. Las definiciones se calculan
con los últimos finales **realmente confirmados** y no suponen que los tres partidos
faltantes terminaron de determinada manera.

- **Playoffs:** muestra equipos que pueden asegurar el ingreso y equipos que pueden
  quedar sin chances. Para cada vía identifica qué necesita el equipo (ganar,
  empatar o perder) y las condiciones de los otros encuentros.
- **Libertadores / al menos Sudamericana:** comprueba exclusivamente lo que se
  puede definir por **Tabla Anual**, descontando plazas directas ya confirmadas.
  No confunde quedar afuera de un cupo de Anual con perder la clasificación
  por campeonatos pendientes.
- **Descenso:** conecta Tabla Anual y promedios, incluida la reasignación. Sólo
  publica definiciones certificadas; puede haber combinaciones no enumeradas.
- **Matriz de los 30 clubes:** una fila por equipo con escenarios G/E/P para los
  cuatro objetivos. En cada alerta se explica el porqué de la garantía usando
  puntos, máximos matemáticos y rivales que todavía pueden alcanzarlo, o la
  certificación conjunta de las dos vías de descenso.
- **Todas las alternativas:** expandí cada equipo para consultar los otros
  caminos suficientes comprobados. La pieza completa exportada también los
  incorpora. No son porcentajes ni pronósticos.

**Árbol y condiciones:** ahora también permite elegir expresamente la **fecha 14**
como alcance del radar de un equipo, aun si hay hasta tres partidos de la 13
pendientes. Los condicionales detallados y los cálculos a demanda de otras canchas
respetan la misma fecha elegida.

**Foto provisional:** si falta algún resultado anterior a la fecha elegida, se
muestra una advertencia visible y el motor deja esos partidos libres en todas
las ramas. Si la fecha 13 ya está cerrada en la base, recupera la foto exacta
previa a la 14. Nunca inventa marcadores para completar una jornada.

**Límite explícito:** las condiciones publicadas son suficientes (aseguran lo
que indican), pero no necesariamente agotan todas las combinaciones que puede
resolver el fixture completo. La matriz no transforma una rama abierta en una
clasificación demostrada. La actualización de resultados sigue dependiendo de
la automatización de GitHub y de que la fuente publique marcadores válidos.

## Corrección del 19/10/2026: Fecha 13

Se incorporaron los 42 resultados finales de las fechas 11 a 13 (15 + 15 + 12), verificados contra el fixture publicado por TyC Sports. La fecha 13 termina el lunes 19 de octubre: **a las 9 h de Argentina todavía quedan tres partidos** (Newell's–Central Córdoba, Sarmiento–Barracas Central y Deportivo Riestra–Unión). No se anticiparon sus marcadores.

River ya disputó 13 partidos y le restan **tres**, contra Racing (F14), Boca (F15) y Aldosivi (F16). La última foto precargada contabiliza 192 resultados entre F1 y F13. Los archivos en `core/data/` se sincronizaron entre sí.

## Qué estaba pasando

- El respaldo (`core/data/`) tenía fecha 4 de octubre y sólo siete finales de la F11.
- El parser de TyC leía la sección histórica de resultados, pero no los marcadores de la fecha más reciente que el sitio publica arriba, bajo el *fixture*.
- El código omitía consultar TyC si las notas de LPF coincidían con una tabla de posiciones vieja. Ahora también consulta el fixture vivo para encontrar finales recientes.
- El ZIP original traía el script `scripts/actualizar_datos.py` pero **no el workflow programado** que describe el README. Se agregó en `.github/workflows/actualizar-datos.yml`.
- El indicador de calendario trataba la fecha 13 como finalizada desde el domingo 18; ahora reconoce que se disputa hasta el lunes 19.

## Instalación en Streamlit Community Cloud (recomendada)

Esta aplicación ya está diseñada para **Streamlit Cloud + GitHub**. No hace falta levantar servidores, ejecutar cron en Streamlit ni abrir la app para que GitHub consulte resultados.

1. **Descomprimí el ZIP** y subí el contenido completo a la **misma rama del repositorio de GitHub que usa tu app**. Hay que conservar la carpeta oculta `.github/workflows/`, el archivo `calculadora_futbol_argentino.py`, `core/`, `scripts/`, `tests/` y `requirements.txt`. No subas el ZIP como un único archivo ni reemplaces solamente el `.py` principal.
2. Confirmá que en **Streamlit Community Cloud → Settings** la app apunta al archivo principal `calculadora_futbol_argentino.py` y a esa rama. Streamlit Cloud toma los commits de GitHub sin volver a crear la app. Si seguís viendo archivos viejos, desde **Manage app → Reboot app** podés forzar el reinicio.
3. En el repositorio de **GitHub → Actions**, abrí **Actualizar resultados Clausura 2026** y pulsá **Run workflow** sobre la rama que usa Streamlit Cloud. Controlá que termine en verde. Si el `git push` falla por permisos, revisá **Settings → Actions → General → Workflow permissions** y habilitá acceso de lectura/escritura cuando la política de tu organización lo permita. Las ramas protegidas pueden requerir otra configuración.
4. A partir de ahí, GitHub comprueba marcadores aproximadamente **cada 30 minutos** (el horario de GitHub puede retrasarse). **Si hay nuevos resultados finales verificados, guarda y publica automáticamente los cambios en `core/data/`.** Streamlit Cloud recoge ese commit. Sin nuevos finales, no modifica la base.
5. **Dentro de Streamlit**, la app abre con la última base confirmada. Si esa foto tiene más de dos horas o el calendario muestra fechas ya cerradas incompletas, intenta consultar fuentes en vivo al usarla, y vuelve a revisarlas **cada diez minutos con la sesión abierta**. El botón «Actualizar a hoy» fuerza una nueva consulta en ese momento. La actualización en la sesión no reemplaza el almacenamiento persistente de GitHub.

**Cómo comprobarlo:** en la barra lateral verás por separado «Base guardada en GitHub» y «Última consulta en vivo en esta sesión». Tras un nuevo resultado, el contador de partidos jugados y los pendientes deben cambiar. La versión de la app debe figurar como **3.8.90**.

**Si la automatización falla:** la app conserva los 192 resultados verificados hasta el 18/10/2026 (con la fecha 13 todavía incompleta). No inventa partidos terminados. Un error de red o una fuente incompleta debe aparecer como advertencia y debe revisarse en los logs de GitHub Actions o Streamlit Cloud.

- No hace falta ejecutar `streamlit run` en tu computadora para publicar cambios.
- Streamlit Cloud no ejecuta procesos programados mientras la app está dormida; por eso la persistencia y el chequeo sin usuarios dependen de GitHub Actions.
- El `GITHUB_TOKEN` de Actions es un token propio del workflow. **No copies tokens ni claves al código ni a los Secrets de Streamlit** para este flujo.

El script de GitHub ejecuta `python scripts/actualizar_datos.py`, sin depender de Streamlit ni de un navegador. Lee los marcadores desde TyC y comprueba que cada partido existe en el fixture, que no contradice un resultado ya confirmado y que una fecha que terminó tenga sus 15 marcadores. Si falla la red, el parser o la validación, sale con error y **no publica una nueva base incompleta**. Sólo escribe un nuevo commit cuando hay resultados nuevos.

Para correr las pruebas sin red: `python -m unittest discover -s tests -v`.

## Estructura

```text
calculadora_futbol_argentino.py   App Streamlit
core/                             Motor, proveedores y parsers
core/data/                        Resultados y tablas verificados
scripts/actualizar_datos.py       Sincronizador de GitHub Actions
.github/workflows/actualizar-datos.yml
requirements.txt
tests/
```

Fuente del fixture y marcadores: [TyC Sports – Fixture del Clausura 2026](https://www.tycsports.com/liga-profesional-de-futbol/fixture-del-clausura-2026-calendario-de-partidos-y-resultados-id750943.html). La actualización futura depende de que las fuentes continúen publicando datos legibles y de que el workflow funcione en tu repositorio. No está verificada hasta que lo ejecutes en GitHub.
