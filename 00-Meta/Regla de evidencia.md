---
tipo: meta
---
# Regla de evidencia

## Regla única

> **Toda afirmación biomédica lleva un identificador verificable, o no entra en el vault.**

Identificadores aceptados:

| Tipo | Formato | Ejemplo |
|---|---|---|
| Publicación | `PMID:` o `DOI:` | `PMID:31738183` |
| Variante clínica | `VCV` de ClinVar | `VCV000012345` |
| Polimorfismo | `rs` de dbSNP | `rs104894093` |
| Fenotipo | `HP:` de HPO | `HP:0000252` |
| Enfermedad / gen | `OMIM:` | `OMIM:257300` |
| Gen / transcrito | Ensembl o RefSeq | `ENSG00000156970`, `NM_001211.6` |
| Frecuencia | gnomAD + versión | `gnomAD v4.1` |

## Estados de una afirmación

Cada ficha lleva `verificado:` en el frontmatter:

- `si` — comprobado contra la fuente primaria por una persona.
- `parcial` — algunos campos comprobados, otros no. Detállalo en la propia ficha.
- `no` — todavía nadie lo ha comprobado. **Excluida de todos los paneles de decisión.**

## Qué NO cuenta como fuente

- La salida de un LLM. Nunca. Ni la mía.
- Otra ficha de este vault (eso es un enlace, no una fuente).
- Un resumen de un paper. La fuente es el paper.
- "Es sabido que...". Si es sabido, tiene PMID.

## El fallo que esto previene

Un agente puede rellenar cuarenta fichas en diez minutos con prosa impecable
y tres citas inventadas. Nadie lo detecta a simple vista, porque el formato es correcto.

Por eso el campo `fuente:` es obligatorio y por eso los paneles filtran por `verificado`.
Una ficha sin fuente **existe** —para que se vea el hueco— pero **no puntúa**.

Ver [[Deuda de evidencia]] para el inventario de huecos abiertos.
