# Vault de Evidencia MVA

Esqueleto de vault de [Obsidian](https://obsidian.md) para trabajar de forma **auditable** sobre
*Mosaic Variegated Aneuploidy* (MVA) en el marco del hackathon
**Rare Disease, Real Kid: The MVA Hackathon 2026** (SageBio + Hugging Face).

> **Qué es esto:** una capa de trazabilidad, no un pipeline bioinformático.
> No sustituye a Exomiser, LIRICAL, VEP ni a ninguna herramienta de filtrado.
> Se coloca *encima* de ellas para responder a la única pregunta que ninguna contesta:
> **¿por qué este candidato está en el puesto 3 y no en el 30, y quién lo decidió, cuándo y con qué evidencia?**

## El problema que resuelve

Un pipeline te devuelve un ranking. Un ranking no es una explicación.
Cuando un jurado, un clínico o tu yo de dentro de tres semanas pregunta *por qué*,
la respuesta suele estar repartida entre un notebook, tres pestañas del navegador y la memoria de alguien.

Este vault convierte ese razonamiento en objetos consultables: hipótesis, evidencia, descartes y bitácora.

## La analogía que lo explica

Es un **HAZOP aplicado a genómica**. La estructura es la misma:

| HAZOP industrial | Aquí |
|---|---|
| Desviación | Hipótesis |
| Causa | Mecanismo propuesto |
| Consecuencia | Predicción falsable |
| Salvaguarda | Evidencia que la sostiene |
| Acción | Siguiente paso, con responsable y fecha |

Si has hecho un HAZOP, ya sabes usar esto.

## Las capas, y dónde encaja el vault

| Capa | Qué es | Dónde vive | ¿En el vault? |
|---|---|---|---|
| 0. Crudo | VCF / BAM, ~85 GB | Disco | **No.** Solo ruta + hash |
| 1. Filtrado | Scripts deterministas | Repo versionado | No |
| 2. Anotación | VEP, gnomAD, ClinVar, OMIM | Tablas | No |
| 3. Fichas | Genes, variantes candidatas | Vault | **Sí** |
| 4. Evidencia | Papers, mecanismo, fenotipo | Vault | **Sí** |
| 5. Razonamiento | Hipótesis, descartes, bitácora | Vault | **Sí** |

**Nunca metas variantes crudas aquí.** Un WGS son millones de variantes; Obsidian se ahoga
por encima de unas 20.000 notas. Este vault es para las decenas de candidatos que sobreviven al filtrado.

## La regla que lo hace útil

**Toda afirmación biomédica lleva identificador verificable o no entra.**
PMID, DOI, ClinVar VCV, dbSNP rs, HPO, OMIM, Ensembl. Sin excepciones.
Ver [[Regla de evidencia]].

Esto no es burocracia: es el único mecanismo que impide que un LLM rellene el vault
de prosa plausible sin respaldo. Una ficha bonita e inventada es **peor** que una ficha vacía,
porque parece rigurosa.

## Cómo empezar

1. Abre esta carpeta como vault en Obsidian.
2. Instala el plugin **Dataview** (los paneles de `90-Paneles/` no funcionan sin él).
3. Lee [[Convenciones]] y [[Regla de evidencia]]. Son cinco minutos.
4. Duplica una plantilla (`_plantilla-*.md`) para crear tu primera ficha.
5. Abre [[Deuda de evidencia]] para ver qué falta por verificar.

## El validador

```bash
pip install pyyaml
python3 validar.py              # informe
python3 validar.py --estricto   # la deuda de evidencia también falla
```

Convierte la [[Regla de evidencia]] de norma escrita en norma **ejecutable**. Comprueba:

- YAML válido — un frontmatter roto hace que Dataview ignore la ficha **en silencio**.
- Campos obligatorios según el tipo de ficha.
- Que ninguna ficha se declare `verificado: "si"` sin un identificador verificable en `fuente`.
- Que ninguna variante entre en la shortlist sin verificar.
- Que ninguna variante se descarte sin dejar el motivo.
- Que ninguna hipótesis activa carezca de predicción falsable y de forma de refutarla.
- Que ninguna referencia se declare leída sin PMID ni DOI.
- Enlaces internos rotos y nombres de fichero no portables.

Distingue **errores** (estructura rota, hay que arreglarlo) de **avisos** (deuda de evidencia declarada,
que es sana mientras se vea).

### Git

```bash
git init
git config core.hooksPath .githooks   # el validador corre antes de cada commit
git add . && git commit -m "Apertura del vault"
```

El `.gitignore` bloquea VCF, BAM, CRAM y FASTQ. **Los datos crudos no entran nunca en el repo**:
aquí vive el razonamiento, no el genoma.

## Sobre las fichas ya incluidas

Las fichas de **BUB1B**, **CEP57** y **TRIP13** están deliberadamente **incompletas**,
con los campos no verificados marcados como tales.

Es intencionado. Podría haberlas rellenado con texto plausible en treinta segundos,
y eso habría sido exactamente el fallo que este vault existe para evitar.
Un hueco marcado es información; un hueco tapado con prosa, no.

El ejemplo de `04-Variantes/` es **sintético y está etiquetado como tal**. No corresponde
a ningún paciente ni a ninguna variante publicada.

## Aviso

Material de apoyo metodológico. **No es consejo médico, ni diagnóstico, ni atención clínica.**
El hackathon tampoco lo es. Los datos genómicos del caso pertenecen a una familia que los
compartió con la comunidad investigadora; trátalos con el respeto que eso merece.

## Licencia

CC0 / dominio público. Cópialo, destrózalo, mejóralo. Si lo mejoras, publícalo.
