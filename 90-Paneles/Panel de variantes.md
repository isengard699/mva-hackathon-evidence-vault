---
tipo: panel
---
# Panel de variantes

Requiere el plugin **Dataview**.

## Shortlist verificada

Solo entran variantes con `verificado` distinto de `no`.
**Este es el punto donde la regla de evidencia deja de ser un discurso y se vuelve un filtro.**

```dataview
TABLE gen, hgvs_c, acmg_clase_propuesta, af_gnomad, cadd_phred, prioridad
FROM "04-Variantes"
WHERE tipo = "variante" AND estado = "shortlist" AND verificado != "no"
SORT prioridad ASC
```

## Candidatas pendientes de verificación

```dataview
TABLE gen, hgvs_c, fuente, revisado
FROM "04-Variantes"
WHERE tipo = "variante" AND verificado = "no" AND estado != "descartada"
SORT revisado ASC
```

## Descartadas y por qué

```dataview
TABLE gen, hgvs_c, motivo_descarte, revisado
FROM "04-Variantes"
WHERE estado = "descartada"
SORT revisado DESC
```

## Sin fase determinada

MVA se asocia a herencia recesiva con variantes bialélicas, así que la fase
(*in trans* vs *in cis*) es determinante para el criterio ACMG **PM3**.

```dataview
TABLE gen, hgvs_c, genotipo
FROM "04-Variantes"
WHERE tipo = "variante" AND fase = "desconocida" AND estado != "descartada"
```
