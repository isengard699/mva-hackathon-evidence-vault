---
tipo: meta
---
# Custodia de datos

Las condiciones del hackathon obligan a **borrar todos los datos en los 30 días posteriores
al cierre, desde todos los entornos**, y a notificarlo por email a los organizadores.

Para poder certificar eso hay que saber dónde han estado. Esta ficha es ese registro.
**Manténla al día en el momento en que muevas un fichero, no después.**

## Registro de ubicaciones

| Fecha | Fichero | Entorno | Estado |
|---|---|---|---|
| 2026-08-27 | Challenge_Clinical_Phenotype_1.docx | Equipo local | Activo |
| 2026-08-27 | Challenge_Clinical_Phenotype_1.docx | Sesión de asistente IA en la nube | Activo |
| | | | |

## Reglas de manejo

- **El VCF no sale del equipo local.** No se sube a ningún servicio, ni a un asistente,
  ni a una nube personal, ni a un repositorio, ni aunque sea privado.
- **El `.gitignore` bloquea** `*.vcf`, `*.vcf.gz`, `*.bam`, `*.cram`, `*.fastq*`.
  Es una salvaguarda, no un permiso: la decisión sigue siendo tuya en cada commit.
- **Los datos del paciente no entran en el vault público.** Viven en el vault local paralelo.
- Los resultados derivados (una lista de variantes candidatas, un ranking) **también son
  datos del caso**. No se publican fuera del canal de entrega oficial.

## Al cerrar el hackathon

- [ ] Borrar los ficheros de todos los entornos de la tabla
- [ ] Vaciar cachés de descarga (`~/.cache/huggingface`)
- [ ] Verificar que el repositorio público no contiene nada del caso
- [ ] Enviar el email de confirmación de borrado a los organizadores
- [ ] Anotar aquí la fecha de la notificación
