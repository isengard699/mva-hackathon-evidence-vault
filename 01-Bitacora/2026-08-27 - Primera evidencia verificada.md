---
tipo: bitacora
fecha: 2026-08-27
autor: David
hipotesis_tocadas: []
---
# 2026-08-27 — Primera evidencia verificada

## Qué se hizo

Contrastada la referencia [[PMID-31738183]] en la página del artículo en JCI
(DOI:10.1172/JCI126863). Metadatos completos, abstract literal, diseño y muestra.

El texto completo **no** se ha leído: PMC6934189 es de acceso abierto pero exige captcha.
La ficha queda como `acceso: solo abstract` y `verificado: parcial`.

## Qué cambió de estado

| Ficha | Antes | Después | Motivo |
|---|---|---|---|
| [[PMID-31738183]] | no verificada | **parcial** | Metadatos y abstract contrastados en fuente |
| [[BUB1B]] | no verificada | **parcial** | Asociación gen-MVA y herencia bialélica con fuente |
| [[CEP57]] | no verificada | **parcial** | Ídem |
| [[TRIP13]] | no verificada | **parcial** | Ídem |

Deuda de evidencia: **de 7 a 3**.

## Qué se aprendió

**El abstract sostiene, literalmente, tres cosas que el vault afirmaba sin fuente:**
la asociación de MVA con BUBR1/CEP57/TRIP13, la herencia bialélica, y el espectro clínico
(cánceres, defectos congénitos, patología progeroide).

**Y un hallazgo que cambia cómo hay que leer este artículo:** es un estudio en **modelo murino**,
no una cohorte de pacientes. El título habla de heterogeneidad fenotípica por efectos alélicos,
pero medida en ratón. Cualquier hipótesis de correlación genotipo-fenotipo que se apoye
en esta referencia arrastra esa limitación y debe declararla.

**Alerta abierta:** existe una **errata publicada** (PMID:33136097) sin revisar. Hasta
comprobar qué corrige, todo dato numérico del artículo original queda en cuarentena.

## Qué falta

- Leer el texto completo y la errata.
- Verificar identificadores (Ensembl, RefSeq, OMIM) de los tres genes.
- ~~Confirmar microcefalia~~ - ficha borrada: era una suposicion de Claude, no aparece en el fenotipo real del caso.
- Rellenar [[Punto de control del huso mitotico]] contra una revisión con PMID.
- Formular la primera hipótesis real (las fichas de demostración ya están borradas).

---

## Añadido — identificadores de gen verificados

Contrastados contra la **API REST de HGNC** (rest.genenames.org), autoridad para símbolos
e identificadores de gen:

| Gen | HGNC | Locus | Ensembl | RefSeq | OMIM gen |
|---|---|---|---|---|---|
| [[BUB1B]] | HGNC:1149 | 15q15.1 | ENSG00000156970 | NM_001211 | 602860 |
| [[CEP57]] | HGNC:30794 | 11q21 | ENSG00000166037 | NM_014679 | 607951 |
| [[TRIP13]] | HGNC:12307 | 5p15.33 | ENSG00000071539 | NM_004237 | 604507 |

**Fenotipos OMIM localizados:** MVA1 257300, MVA2 614114, MVA3 617598.
La correspondencia subtipo-gen **NO está confirmada en primaria**: omim.org bloquea el acceso
automatizado y las entradas se localizaron por título en buscador. Queda como pendiente
en cada ficha de gen: hay que abrir OMIM a mano.

Borradas las dos fichas de demostración (ejemplo sintético de variante y H001).

---

## Añadido — bases del hackathon leídas, y reestructuración

Leídos el README del dataset, `tabs/rules.py`, `evaluation.py` y `tabs/submit_track2.py`
del Space oficial. Resumen operativo en [[Reglas del hackathon]].

**Cambios estructurales:**

- **Separación público / local.** El documento de fenotipo está marcado *"Confidential ·
  Do not redistribute"*. El vault público no contiene ni un solo dato del paciente;
  el caso vive en un vault local paralelo. Ver [[Custodia de datos]].
- **Borrada la ficha de microcefalia.** Era una suposición de Claude, no un dato: no aparece
  en el fenotipo real. Primer caso registrado de una ficha eliminada por falta de respaldo,
  que es exactamente para lo que sirve este sistema.
- Añadidas [[H001 - La variante causal no es obvia]] y
  [[H002 - La respuesta es un par compound-het]]: las dos primeras hipótesis reales.
- Añadida la carpeta `08-Entrega` con formatos y estrategia de puntuación.

**El dato que más cambia el plan:** el dataset son 85 GB, pero **el VCF pesa 315 MB**.
El resto son FASTQ crudos, necesarios solo para re-alinear desde cero. Los datos listos
para análisis caben en cualquier portátil.
