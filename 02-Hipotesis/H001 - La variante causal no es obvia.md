---
tipo: hipotesis
id: H001
enunciado: "La variante causal no es un hallazgo trivial en los genes MVA conocidos"
estado: refutada
prioridad: 5
verificado: "no"
prediccion_falsable: "Ver cuerpo de la ficha"
como_se_refuta: "Ver cuerpo de la ficha"
genes_implicados: [BUB1B, CEP57, TRIP13]
fenotipos_implicados: []
evidencia_a_favor: []
evidencia_en_contra: ["Leaderboard publico del Track 1: 45 entregas con 100,0 puntos y F-max 1,000"]
responsable: David
revisado: 2026-08-27
---
# H001 — La variante causal no es obvia

## Enunciado

La variante causal **no** es un par bialélico codificante evidente en [[BUB1B]], [[CEP57]]
o [[TRIP13]] que un pipeline clínico estándar habría marcado sin dificultad.

## Razonamiento

El caso ya pasó por secuenciación de genoma completo en contexto clínico. Si el análisis
convencional hubiera cerrado el diagnóstico molecular, **no habría hackathon**.

Convocar a la comunidad con 50.000 $ en premios es, en sí mismo, evidencia de que el
análisis estándar no resolvió el caso. Esa es la señal más informativa que tenemos y
no está en ningún fichero: está en la existencia misma del reto.

## Predicción falsable

Si esta hipótesis es cierta, la respuesta vivirá en alguno de los espacios donde el
pipeline convencional falla:

- Variantes de **splicing** fuera de los dinucleótidos canónicos
- **Intrónicas profundas** con efecto sobre el procesamiento
- **Variantes estructurales** o CNV que un llamador de SNV no reporta
- Un **segundo alelo no llamado**, dejando lo que parece un heterocigoto aislado
- Un **gen de la misma vía** todavía no asociado formalmente a MVA

## Cómo se refuta

Extraer del VCF las regiones de los cinco genes candidatos y comprobar si existe un par
bialélico codificante con clasificación clara de patogenicidad. **Si aparece, esta hipótesis
está muerta** y el problema era más fácil de lo que suponemos.

Es la primera comprobación que hay que hacer, y cuesta minutos.

## Siguiente acción

Descargar el VCF (315 MB) e inspeccionar las regiones de BUB1B (15q15.1), CEP57 (11q21),
TRIP13 (5p15.33), BUB1 (2q13) y BUB3 (10q26.3).

**El resultado es informativo en ambas direcciones**, y por eso es la acción de mayor valor
que hay sobre la mesa.

---

## REFUTADA — 2026-08-28

**Evidencia:** el leaderboard público del Track 1 muestra **45 entregas, todas con 100,0
puntos de rango y F-max 1,000**. Puntuación perfecta en todas. La primera llegó el
2026-08-25 a las 20:13 UTC, **un día después de abrirse la ventana**.

Los nombres de los ficheros entregados identifican la respuesta sin ambigüedad:
`bub1b-compound-het`, `bub1b-pair`, `bub1b-targeted-acmg`, `bub1b-comphet-bcftools`.

**La variante causal es un compound heterocigoto en [[BUB1B]], y es un hallazgo
directo con herramientas estándar.**

## Por qué fallé

El razonamiento fue: *"el caso ya pasó por secuenciación clínica; si el análisis
convencional lo hubiera resuelto, no habría hackathon"*.

El error está en la premisa oculta: que el propósito del hackathon es **encontrar la
variante**. No lo es. El Track 1 es un ejercicio de calibración con clave conocida —
sirve para validar que los participantes saben manejar los datos. El problema abierto
de verdad es el **Track 2**: qué hacer con esa variante, que es donde no hay clave.

**Lección registrada:** un razonamiento elegante sobre las intenciones de los organizadores
no es evidencia. Treinta segundos mirando el leaderboard público lo habrían resuelto antes
de formular la hipótesis. El leaderboard estaba ahí desde el principio.
