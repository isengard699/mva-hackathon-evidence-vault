---
tipo: meta
verificado: "parcial"
fuente: "Space oficial SageBio/rare-disease-real-kid-mva-hackathon-2026 (tabs/rules.py, evaluation.py, tabs/submit_track2.py) y README del dataset"
revisado: 2026-08-27
---
# Reglas del hackathon

Resumen operativo. **La fuente es el Space oficial**; ante cualquier duda, manda el Space.

## Calendario

Ventana de envío: **24 agosto – 24 octubre 2026**.
Evaluación del Track 2: panel experto, ~2-3 meses tras el cierre.

## Los dos tracks

| | Track 1 | Track 2 |
|---|---|---|
| Objetivo | Predecir la variante causal | Proponer fármacos reposicionados |
| Entrega | Tabla, máx **10 filas** por probando, columna **EPCR** en (0,1], ordenada descendente | Informe PDF/MD + repo GitHub reproducible + vídeo de 3 min |
| Evaluación | Automática contra clave validada clínicamente | Cualitativa, panel experto |
| Límite | — | **Una sola entrega por participante** |

## Puntuación del Track 1

**Métrica 1 — puntos por rango:**

| Rango de la respuesta correcta | Puntos |
|---|---|
| 1 | 100 |
| 2-3 | 50 |
| 4-5 | 25 |
| 6-10 | 10 |
| 11+ | 0 |

Acierto completo del par causal: puntos íntegros de ese rango.
**Acierto parcial (solo en compound-het):** si se recupera una de las dos variantes
verdaderas, **la mitad** de los puntos de ese rango.

**Métrica 2 — F-max:** se barren todos los umbrales de EPCR presentes en la entrega;
en cada uno se calculan precisión y exhaustividad y se computa F. Se reporta el máximo.

> **Lectura estratégica:** que exista crédito parcial *"solo en compound-het"* es una pista
> sobre la forma esperada de la respuesta. Ver [[H002 - La respuesta es un par compound-het]].

## Requisitos del Track 2

El informe debe **caracterizar el mecanismo** de la variante: pérdida o ganancia de función,
vía alterada y consecuencias biológicas aguas abajo, para justificar el reposicionamiento.
Los organizadores facilitan una plantilla de métodos en Excel.

## Premios

| Puesto | Metálico | Créditos Claude |
|---|---|---|
| 1º | 12.000 $ | 12.000 $ |
| 2º | 7.000 $ | 7.000 $ |
| 3º | 4.000 $ | 4.000 $ |
| **Innovación** | 2.000 $ | 2.000 $ |

## Reglas duras

- **Mayor de 18 años.** Cada miembro del equipo se registra individualmente.
- **Prohibido recompartir o redistribuir los datos.** A nadie.
- **Borrado obligatorio en los 30 días posteriores al cierre, desde TODOS los entornos**,
  con notificación por email a los organizadores. Ver [[Custodia de datos]].
- **Prohibido intentar re-identificar o recontactar** al paciente, su familia o
  la MVA Society.
- Las entregas se publican bajo **CC-BY 4.0** y tu nombre se hace público.
- Las entregas pueden ser **re-ejecutadas** por los organizadores: el repo tiene que
  ser reproducible de verdad, no de boquilla.
