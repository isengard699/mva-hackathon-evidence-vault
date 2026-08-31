---
tipo: meta
verificado: "parcial"
fuente: "tabs/about.py y tabs/faq.py del Space oficial SageBio/rare-disease-real-kid-mva-hackathon-2026"
revisado: 2026-08-28
---
# Track 2 — rúbrica y estrategia

## La rúbrica

Un panel independiente puntúa cada entrega sobre cuatro criterios:

| Criterio | Peso |
|---|---|
| Rigor científico | **35 %** |
| Impacto potencial | 25 % |
| Innovación | **25 %** |
| Escalabilidad | **15 %** |

## La lectura estratégica

El objetivo declarado del hackathon (`tabs/about.py`) es que las entregas se publiquen bajo
CC-BY 4.0 **"para que los métodos desarrollados para este caso puedan reutilizarse para
otros individuos sin diagnóstico"**.

Eso significa que **el 75 % del peso no mide la calidad del fármaco propuesto**, sino
el rigor del razonamiento, su originalidad y si el método generaliza. El candidato
farmacológico es el vehículo del informe, no el informe.

## Cómo responde este vault a cada criterio

| Criterio | Qué lo sostiene |
|---|---|
| **Rigor (35 %)** | [[Regla de evidencia]]: identificador verificable o la ficha no puntúa. Campo "qué NO demuestra" obligatorio en cada referencia. `validar.py` bloquea el commit si algo se declara verificado sin fuente |
| **Impacto (25 %)** | Depende del candidato propuesto. Es donde menos ventaja estructural tenemos y donde hay que apoyarse en literatura primaria |
| **Innovación (25 %)** | El instrumento en sí: un registro de evidencia auditable con validación automática, que **conserva las hipótesis refutadas con la evidencia que las mató** |
| **Escalabilidad (15 %)** | El vault público es agnóstico al caso por construcción: los datos del paciente viven separados. Clonarlo y aplicarlo a otro probando no exige tocar nada. Ver [[Custodia de datos]] |

## La trampa a evitar

Escribir el informe **hacia** la rúbrica en lugar de hacia la verdad.

Un panel experto detecta a la primera un texto construido para marcar casillas. La
trazabilidad solo puntúa si es real: si las fichas están verificadas de verdad, si la
incertidumbre declarada es la que hay, y si las hipótesis refutadas se refutaron por
evidencia y no por conveniencia narrativa.

**El único camino a ese 35 % es que el rigor sea cierto.** No hay atajo, y menos ante
gente que revisa artículos para vivir.

## Datos operativos

- Track 1: **hasta 6 entregas** por participante; solo cuenta la mejor puntuación.
- Track 2: **una sola entrega**, sin reenvíos. Un miembro designado por equipo.
- Un único probando confirmado (`tabs/about.py` habla de un niño).
- Los prefijos `model1`-`model4` de los ficheros del leaderboard **no están documentados**
  en el FAQ. Probablemente ranuras de entrega. Pendiente de aclarar.
