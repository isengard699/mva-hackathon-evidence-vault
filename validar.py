#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador del Vault de Evidencia MVA.

Hace cumplir por máquina lo que 00-Meta/Regla de evidencia.md pide por escrito.

    python3 validar.py              # valida el vault
    python3 validar.py --estricto   # los avisos también fallan

Códigos de salida:  0 = limpio (o solo avisos)   1 = errores estructurales
Requiere: pip install pyyaml
"""
import argparse
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("Falta PyYAML.  Instálalo con:  pip install pyyaml")

ROOT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- constantes

# Identificadores que cuentan como fuente verificable (Regla de evidencia)
ID_VERIFICABLE = re.compile(
    r"(PMID:\s*\d+"
    r"|doi\.org/10\.|DOI:\s*10\.|10\.\d{4,}/"
    r"|VCV\d+"
    r"|\brs\d+"
    r"|HP:\d{7}"
    r"|OMIM:\s*\d+"
    r"|ENS[GTP]\d+"
    r"|N[MPR]_\d+"
    r"|gnomAD\s*v)",
    re.IGNORECASE,
)

# Texto que delata que un campo fuente NO es una fuente
NO_ES_FUENTE = re.compile(
    r"(sin verificar|pendiente|ninguna|desconocid|por determinar|ejemplo|inventad|tbd|n/?a)",
    re.IGNORECASE,
)

VERIFICADO_VALIDO = {"si", "sí", "no", "parcial"}

# Tipos cuyas afirmaciones son biomédicas y por tanto exigen fuente
TIPOS_CON_FUENTE = {"gen", "variante", "fenotipo", "referencia", "mecanismo"}

CAMPOS_REQUERIDOS = {
    "gen":       ["simbolo_hgnc", "verificado"],
    "variante":  ["gen", "hgvs_c", "estado", "verificado"],
    "hipotesis": ["id", "estado", "verificado"],
    "fenotipo":  ["hpo_id", "verificado"],
    "referencia": ["verificado", "acceso"],
    "mecanismo": ["verificado"],
    "bitacora":  ["fecha"],
}

ESTADOS_VARIANTE = {"candidata", "shortlist", "descartada", "confirmada"}
ESTADOS_HIPOTESIS = {"abierta", "en-revision", "sostenida", "refutada", "aparcada"}

errores, avisos = [], []


def err(f, msg):
    errores.append(f"{f}: {msg}")


def avi(f, msg):
    avisos.append(f"{f}: {msg}")


def sin_bloques_codigo(texto):
    """Quita los bloques ``` para que los placeholders de los prompts no cuenten."""
    return re.sub(r"```.*?```", "", texto, flags=re.DOTALL)


def vacio(v):
    return v is None or (isinstance(v, str) and not v.strip()) or v == []


# ---------------------------------------------------------------- recorrido

notas = sorted(p for p in ROOT.rglob("*.md") if ".obsidian" not in p.parts)
stems = {p.stem for p in notas}
frontmatters = {}

for p in notas:
    rel = p.relative_to(ROOT).as_posix()
    texto = p.read_text(encoding="utf-8")
    es_plantilla = p.name.startswith("_plantilla")

    # --- nombre de fichero portable
    if re.search(r"[áéíóúñÁÉÍÓÚÑüçÜÇ]", p.name):
        avi(rel, "el nombre de fichero lleva acentos (ver Convenciones)")

    # --- frontmatter
    if not texto.startswith("---"):
        if not es_plantilla and p.name != "README.md":
            err(rel, "sin frontmatter YAML")
        continue

    partes = texto.split("---", 2)
    if len(partes) < 3:
        err(rel, "frontmatter mal cerrado")
        continue

    try:
        fm = yaml.safe_load(partes[1]) or {}
    except Exception as e:
        err(rel, f"YAML inválido -> Dataview lo ignorará en silencio ({e})")
        continue

    if not isinstance(fm, dict):
        err(rel, "el frontmatter no es un mapa de clave/valor")
        continue

    # YAML convierte 'no' en False y 'yes'/'true' en True (el "Norway problem").
    # Si eso llega a Dataview, la consulta  WHERE verificado = "no"  no coincide
    # con nada y la deuda de evidencia desaparece del panel en silencio.
    # Aquí lo normalizamos, y avisamos para que se entrecomille en origen.
    if isinstance(fm.get("verificado"), bool):
        avi(rel, "verificado sin comillas: YAML lo lee como booleano y Dataview deja de encontrarlo. "
                 'Escribe verificado: "no"')
        fm["verificado"] = "no" if fm["verificado"] is False else "si"

    frontmatters[rel] = fm
    tipo = fm.get("tipo")

    if es_plantilla or tipo in (None, "meta", "panel"):
        continue

    # --- campos requeridos
    for campo in CAMPOS_REQUERIDOS.get(tipo, []):
        if campo not in fm:
            err(rel, f"falta el campo obligatorio '{campo}' para tipo={tipo}")

    # --- verificado con valor legal
    ver = str(fm.get("verificado", "")).strip().lower()
    if ver and ver not in VERIFICADO_VALIDO:
        err(rel, f"verificado='{ver}' no es válido (si | no | parcial)")

    # --- regla de evidencia: si dice estar verificado, que lo demuestre
    if tipo in TIPOS_CON_FUENTE and ver in {"si", "sí", "parcial"}:
        fuente = str(fm.get("fuente", "") or "")
        if vacio(fuente):
            err(rel, f"verificado='{ver}' pero el campo 'fuente' está vacío")
        elif NO_ES_FUENTE.search(fuente) and not ID_VERIFICABLE.search(fuente):
            err(rel, f"verificado='{ver}' con una fuente que no es una fuente: '{fuente[:60]}'")
        elif not ID_VERIFICABLE.search(fuente):
            err(rel, f"verificado='{ver}' pero 'fuente' no contiene ningún identificador verificable")

    if tipo in TIPOS_CON_FUENTE and ver == "no":
        avi(rel, "deuda de evidencia: sin verificar")

    # --- variantes
    if tipo == "variante":
        estado = str(fm.get("estado", "")).strip()
        if estado and estado not in ESTADOS_VARIANTE:
            err(rel, f"estado='{estado}' no válido {sorted(ESTADOS_VARIANTE)}")
        if estado == "descartada" and vacio(fm.get("motivo_descarte")):
            err(rel, "descartada sin 'motivo_descarte' (nunca se descarta sin dejar el motivo)")
        if estado == "shortlist" and ver == "no":
            err(rel, "en shortlist sin verificar: no puede entrar en el panel de decisión")
        if str(fm.get("fase", "")).strip() == "desconocida" and estado in {"shortlist", "confirmada"}:
            avi(rel, "fase desconocida en una variante priorizada (crítico para ACMG PM3 en herencia recesiva)")

    # --- hipótesis
    if tipo == "hipotesis":
        estado = str(fm.get("estado", "")).strip()
        if estado and estado not in ESTADOS_HIPOTESIS:
            err(rel, f"estado='{estado}' no válido {sorted(ESTADOS_HIPOTESIS)}")
        if estado not in {"aparcada", "refutada"}:
            for campo in ("prediccion_falsable", "como_se_refuta"):
                if vacio(fm.get(campo)):
                    err(rel, f"hipótesis activa sin '{campo}': eso es una corazonada, no una hipótesis")

    # --- referencias
    if tipo == "referencia":
        acceso = str(fm.get("acceso", "")).strip().lower()
        if acceso == "texto completo" and vacio(fm.get("pmid")) and vacio(fm.get("doi")):
            err(rel, "declara texto completo leído pero no tiene ni PMID ni DOI")
        if ver in {"si", "sí"} and acceso == "no accedido":
            err(rel, "marcada como verificada pero nadie ha accedido al artículo")

    # --- fenotipo
    if tipo == "fenotipo":
        hpo = str(fm.get("hpo_id", "") or "")
        if hpo and not re.fullmatch(r"HP:\d{7}", hpo.strip()):
            err(rel, f"hpo_id='{hpo}' no tiene el formato HP:0000000")

# --- enlaces internos (fuera de bloques de código)
for p in notas:
    rel = p.relative_to(ROOT).as_posix()
    cuerpo = sin_bloques_codigo(p.read_text(encoding="utf-8"))
    for link in re.findall(r"\[\[([^\]|#]+)", cuerpo):
        link = link.strip()
        if link and link not in stems:
            err(rel, f"enlace roto: [[{link}]]")

# ---------------------------------------------------------------- informe

total = len(frontmatters)
verificadas = sum(
    1 for fm in frontmatters.values()
    if str(fm.get("verificado", "")).lower() in {"si", "sí"}
)
parciales = sum(1 for fm in frontmatters.values() if str(fm.get("verificado", "")).lower() == "parcial")
biomedicas = sum(1 for fm in frontmatters.values() if fm.get("tipo") in TIPOS_CON_FUENTE)

print("=" * 62)
print("  VALIDADOR DEL VAULT DE EVIDENCIA MVA")
print("=" * 62)
print(f"  Notas analizadas ......... {len(notas)}")
print(f"  Fichas biomédicas ........ {biomedicas}")
print(f"  Verificadas .............. {verificadas}")
print(f"  Parciales ................ {parciales}")
print(f"  ERRORES .................. {len(errores)}")
print(f"  Avisos (deuda) ........... {len(avisos)}")
print("=" * 62)

if errores:
    print("\nERRORES — hay que arreglarlos:\n")
    for e in errores:
        print(f"  [X] {e}")

if avisos:
    print("\nAVISOS — deuda de evidencia, no bloquean:\n")
    for a in avisos:
        print(f"  [!] {a}")

if not errores and not avisos:
    print("\nVault limpio. Sospechoso, pero limpio.")
elif not errores:
    print(f"\nSin errores estructurales. {len(avisos)} huecos declarados: eso es honestidad, no fallo.")

args = argparse.ArgumentParser(add_help=False)
args.add_argument("--estricto", action="store_true")
opts, _ = args.parse_known_args()

sys.exit(1 if errores or (opts.estricto and avisos) else 0)
