---
tipo: panel
---
# Panel de hipótesis

Requiere el plugin **Dataview**.

## Hipótesis en juego, por prioridad

```dataview
TABLE prioridad, estado, verificado, responsable, revisado
FROM "02-Hipotesis"
WHERE tipo = "hipotesis" AND estado != "refutada" AND estado != "aparcada"
SORT prioridad ASC
```

## Hipótesis sin predicción falsable

Estas no deberían existir. Si aparece alguna, o se completa o se aparca.

```dataview
TABLE estado, responsable
FROM "02-Hipotesis"
WHERE tipo = "hipotesis" AND (!prediccion_falsable OR !como_se_refuta)
```

## Refutadas

Se conservan siempre. Saber qué se cayó evita repetir el callejón.

```dataview
TABLE evidencia_en_contra, revisado
FROM "02-Hipotesis"
WHERE estado = "refutada"
SORT revisado DESC
```
