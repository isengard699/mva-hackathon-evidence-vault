---
tipo: panel
---
# Deuda de evidencia

El inventario de todo lo que este vault afirma **sin haberlo comprobado**.

Si esta lista está vacía, el vault es sólido. Si está llena, al menos es honesto.
Lo peligroso es un vault que no tenga esta página.

## Todo lo no verificado

```dataview
TABLE tipo, fuente, revisado
FROM "03-Genes" OR "04-Variantes" OR "05-Fenotipo" OR "06-Evidencia" OR "07-Mecanismo" OR "02-Hipotesis"
WHERE verificado = "no"
SORT tipo ASC, file.name ASC
```

## Referencias citadas pero no leídas

Una referencia listada no es una referencia leída.

```dataview
TABLE titulo, acceso, revisado
FROM "06-Evidencia"
WHERE acceso = "no accedido" OR acceso = "solo abstract"
```

## Verificación parcial

```dataview
TABLE tipo, fuente, revisado
FROM "03-Genes" OR "04-Variantes" OR "06-Evidencia"
WHERE verificado = "parcial"
```
