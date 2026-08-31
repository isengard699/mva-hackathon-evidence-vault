---
tipo: meta
---
# Convenciones

## Nombres de fichero

| Tipo | Patrón | Ejemplo |
|---|---|---|
| Gen | símbolo HGNC | `BUB1B.md` |
| Variante | `GEN c.HGVS` | `BUB1B c.2211dup.md` |
| Fenotipo | `HP-XXXXXXX - Nombre` | `HP-0000252 - Microcefalia.md` |
| Referencia | `PMID-XXXXXXXX` | `PMID-31738183.md` |
| Hipótesis | `HXXX - Enunciado corto` | `H001 - Carga de aneuploidia.md` |
| Bitácora | `AAAA-MM-DD - Asunto` | `2026-08-27 - Apertura.md` |

Sin acentos ni caracteres especiales en los nombres de fichero (portabilidad entre sistemas).
En el contenido, español correcto con todos sus acentos.

## Enlaces

- Enlaza con `[[ ]]` siempre que menciones un gen, fenotipo, hipótesis o referencia que tenga ficha.
- Si no tiene ficha, créala vacía con `verificado: no`. Un enlace roto es un hueco invisible.
- El grafo solo sirve si los enlaces son consistentes.

## Estados

`estado:` en variantes e hipótesis:

- `abierta` / `candidata` — en juego.
- `shortlist` — prioridad alta, en revisión activa.
- `descartada` — fuera, **con motivo obligatorio** en el campo `motivo_descarte`.
- `confirmada` — sostenida por evidencia verificada.

**Nunca borres una ficha descartada.** El registro de por qué algo se cayó vale tanto
como el de por qué algo se mantuvo, y evita que alguien reabra el mismo callejón dentro de un mes.

## Ontologías

No inventes taxonomía. Usa las que ya existen y son el idioma del dominio:

- **HPO** para fenotipo — https://hpo.jax.org
- **ACMG/AMP 2015** para clasificación de variantes — ver [[Criterios ACMG]]
- **Sequence Ontology** para consecuencias moleculares
- **HGVS** para nomenclatura de variantes — https://hgvs-nomenclature.org
- **HGNC** para símbolos de gen

Si tu vault no habla estos idiomas, no le sirve a nadie más que a ti.
