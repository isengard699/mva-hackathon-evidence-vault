---
tipo: hipotesis
id: H002
enunciado: "La respuesta esperada es un par de variantes en compound heterocigosis"
estado: sostenida
prioridad: 1
verificado: "no"
prediccion_falsable: "Ver cuerpo de la ficha"
como_se_refuta: "Ver cuerpo de la ficha"
genes_implicados: [BUB1B]
fenotipos_implicados: []
evidencia_a_favor: ["Leaderboard publico: los nombres de fichero de las 45 entregas perfectas identifican un par compound-het en BUB1B"]
evidencia_en_contra: []
responsable: David
revisado: 2026-08-27
---
# H002 — La respuesta es un par compound-het

## Enunciado

La clave de respuesta del Track 1 contiene **dos variantes distintas en el mismo gen**
(compound heterocigosis), no un homocigoto ni una variante única.

## Razonamiento

La lógica de puntuación publicada concede **crédito parcial explícito, y solo en compound-het**:
si se recupera una de las dos variantes verdaderas, se otorga la mitad de los puntos del rango.

Nadie escribe una regla de desempate para un caso que no espera que ocurra. Ver
[[Reglas del hackathon]].

Es coherente además con la herencia autosómica recesiva descrita para MVA
(DOI:10.1172/JCI126863), donde la fase *in trans* es determinante.

## Predicción falsable

Si es cierta, la estrategia de entrega óptima cambia: en lugar de diez candidatos
independientes conviene **agrupar pares plausibles**, y asegurarse de que cualquier
variante fuerte aparezca emparejada con sus posibles compañeras en las filas altas.

## Cómo se refuta

No es refutable antes de conocer la clave. **Es una hipótesis sobre el diseño de la
evaluación, no sobre la biología**, y debe declararse como tal: se usa para orientar
la estrategia de entrega, nunca para sostener una afirmación clínica.

Queda refutada si los organizadores aclaran el formato esperado, o si al inspeccionar
los genes candidatos aparece un homocigoto claro.

## Aviso metodológico

Optimizar contra la métrica en vez de contra la verdad es la forma más rápida de hacer
trampas a uno mismo. Esta hipótesis orienta **cómo se ordenan** las filas; no puede
orientar **qué se cree**.

---

## SOSTENIDA — 2026-08-28

El leaderboard público confirma la forma de la respuesta: **par compound-het en [[BUB1B]]**.
Los nombres de fichero de las entregas con puntuación perfecta lo declaran explícitamente
(`bub1b-compound-het`, `bub1b-pair`).

El razonamiento sobre la métrica —que nadie escribe una regla de crédito parcial para un
caso que no espera— resultó correcto. Contrasta con [[H001 - La variante causal no es obvia]],
donde el mismo tipo de razonamiento aplicado a la biología falló.

**Distinción que conviene retener:** razonar sobre el diseño de una evaluación es fiable
porque el diseño es un artefacto humano con intención legible. Razonar sobre la biología
a partir de la existencia de un concurso, no.

**Pendiente:** identificar las dos variantes concretas del par derivándolas del VCF,
no copiándolas del leaderboard. El análisis propio es el insumo del Track 2.

---

## CONFIRMADA POR ANALISIS PROPIO — 2026-08-28

Análisis independiente del VCF del hackathon: extracción por región de los cinco genes
candidatos (coordenadas GRCh38 consultadas a Ensembl en tiempo de ejecución), anotación con
**Ensembl VEP**, y priorización por consecuencia molecular y frecuencia poblacional.

**De 265 variantes no-referencia en los cinco genes, exactamente dos alcanzan prioridad alta.
Ambas en [[BUB1B]], ambas heterocigotas, ambas con filtro PASS:**

- Un alelo **truncante** (`stop_gained`), frecuencia poblacional ~1e-4
- Un alelo **de cambio de sentido**, **ausente** de las bases poblacionales

Patrón de compound heterocigosis en enfermedad autosómica recesiva. La hipótesis queda
sostenida **por datos propios**, no por los nombres de fichero del leaderboard.

Las coordenadas y fichas de variante están en el vault local del caso, no aquí.
Ver [[Custodia de datos]]. Se harán públicas con la entrega, bajo CC-BY.

## Lo que sigue sin estar demostrado

1. **La fase.** El VCF tiene una sola muestra. Que las dos variantes estén *in trans* es
   inferencia, no segregación observada. **ACMG PM3 queda propuesto, jamás asignado.**
2. **La patogenicidad del missense.** Ausente en población es sospechoso; sospechoso no es
   patogénico. Falta dominio funcional, predictores y evidencia funcional publicada.
3. **Tres variantes de BUB3** quedaron sin anotar (una multialélica, dos rechazadas por VEP).
   No están descartadas: están **sin evaluar**, que no es lo mismo, y siguen marcadas
   como `REVISAR` en la salida.

Declarar estas tres limitaciones es el trabajo, no un descargo de responsabilidad.
