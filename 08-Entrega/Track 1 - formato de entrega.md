---
tipo: meta
verificado: "parcial"
fuente: "evaluation.py del Space oficial SageBio/rare-disease-real-kid-mva-hackathon-2026"
revisado: 2026-08-27
---
# Track 1 — formato de entrega

## Restricciones duras

- **Máximo 10 filas por probando.**
- **EPCR** (probabilidad estimada de causalidad) en el intervalo **(0, 1]**. Cero no vale.
- Filas **ordenadas descendentemente por EPCR**.

## Estrategia derivada de la puntuación

Los puntos caen por escalones: **100 / 50 / 25 / 10 / 0**. La diferencia entre acertar
en primera posición y en segunda es de 50 puntos; entre la quinta y la sexta, de 15.

Consecuencias:

1. **La fila 1 vale tanto como las filas 2 y 3 juntas.** Merece la pena defenderla.
2. **Las filas 6 a 10 son casi gratis** (10 puntos frente a 0). No dejes filas vacías:
   una apuesta improbable en la fila 9 no te cuesta nada en la métrica de rango.
3. **Pero sí te cuesta en F-max**, que penaliza los falsos positivos por encima del umbral.
   Baja el EPCR de las apuestas especulativas para que queden fuera del óptimo de F.

Ese es el equilibrio real del track: **rango premia cubrir, F-max premia acertar.**
Los EPCR bajos en las filas de cola te dan lo uno sin arruinar lo otro.

## Registro de entregas

| Fecha | Filas | EPCR fila 1 | Hipótesis que la sostiene | Resultado |
|---|---|---|---|---|
| | | | | |

**Cada entrega se registra aquí con la hipótesis que la justifica.** Una fila sin hipótesis
detrás es una corazonada disfrazada de predicción.
