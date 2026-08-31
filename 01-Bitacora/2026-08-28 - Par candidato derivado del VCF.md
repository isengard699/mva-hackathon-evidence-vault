---
tipo: bitacora
fecha: 2026-08-28
autor: David
hipotesis_tocadas: [H001, H002]
---
# 2026-08-28 — Par candidato derivado del VCF

## Qué se hizo

Cadena completa de análisis, reproducible y con toda la parametrización explícita:

1. **Descarga selectiva.** Solo VCF (315 MB) e índice. Los 84,7 GB de FASTQ no se tocan.
2. **Extracción por región.** Cinco genes candidatos (BUB1B, CEP57, TRIP13, BUB1, BUB3),
   coordenadas GRCh38 consultadas a Ensembl **en tiempo de ejecución** y registradas.
   Padding de ±10 kb. Descartados homocigotos de referencia y posiciones sin llamada.
   Resultado: **265 variantes**.
3. **Anotación con Ensembl VEP.** Consecuencia molecular, HGVS, frecuencia poblacional,
   predictores in silico.
4. **Priorización.** ALTA = consecuencia de impacto real **y** frecuencia < 1 %.

## Resultado

**Exactamente 2 variantes de prioridad ALTA, ambas en BUB1B, ambas heterocigotas, ambas PASS:**
un alelo truncante y un alelo missense ausente de población.

Reparto final: ALTA 2 · REVISAR 3 · media 5 · **baja 255**.

Los 255 descartados por frecuencia son el trabajo real del filtro: un polimorfismo presente
en un porcentaje apreciable de la población no puede causar una enfermedad de menos de
50 casos en el mundo.

## Qué cambió de estado

| Ficha | Antes | Después |
|---|---|---|
| [[H002 - La respuesta es un par compound-het]] | sostenida por leaderboard | **sostenida por análisis propio** |
| [[H001 - La variante causal no es obvia]] | refutada | sigue refutada, ahora con datos propios |

## Incidencias registradas

- **1 variante multialélica** y **2 rechazadas por VEP** (las tres en BUB3) quedan marcadas
  como `REVISAR`. **No se descartan: se declaran sin evaluar.** Un fallo técnico que
  desaparece de la vista es cómo se pierde un hallazgo.
- La primera versión del anotador abortaba el lote entero por una sola variante mala, y
  además ocultaba las de prioridad baja: un resultado nulo y un fallo silencioso se veían
  igual. Corregido en la v3.
- Nombre de fichero con una notación HGVS `c.` **inventada** por Claude. Detectado y
  corregido antes de propagarse. Tercer error del mismo tipo en dos días: rellenar un hueco
  con algo plausible en lugar de dejarlo marcado.

## Qué falta

- Cerrar la ficha del missense: ClinVar, dominio funcional, predictores, evidencia funcional.
- Anotar a mano las tres variantes de BUB3 pendientes.
- Confirmar el formato exacto de columnas en la pestaña de entrega del Track 1.
- Caracterizar el mecanismo para el Track 2. [[PMID-31738183]] es el punto de partida.
