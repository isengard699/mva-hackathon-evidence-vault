---
tipo: hipotesis
id: H003
enunciado: "El Track 1 no discrimina y el premio se decide integramente en el Track 2"
estado: sostenida
prioridad: 1
verificado: "no"
prediccion_falsable: "Ver cuerpo de la ficha"
como_se_refuta: "Ver cuerpo de la ficha"
genes_implicados: [BUB1B]
fenotipos_implicados: []
evidencia_a_favor: ["45 entregas del Track 1 empatadas en 100,0 puntos y F-max 1,000 a cuatro dias de la apertura"]
evidencia_en_contra: []
responsable: David
revisado: 2026-08-28
---
# H003 — El Track 2 es donde se decide todo

## Enunciado

El Track 1 ha alcanzado saturación: no puede diferenciar entre participantes. Por tanto
la totalidad del reparto de premios se decide en la evaluación cualitativa del Track 2.

## Evidencia

A cuatro días de abrirse la ventana de envío, **45 entregas con puntuación idéntica y
perfecta**: 100,0 puntos de rango y F-max 1,000. No hay margen de mejora ni forma de
destacar. Ver [[H001 - La variante causal no es obvia]].

## Consecuencias operativas

1. **El Track 1 pasa de proyecto a trámite.** Una sesión de trabajo, no un esfuerzo
   sostenido. Se entrega derivando el resultado del VCF, nunca copiándolo del leaderboard:
   el análisis propio es el insumo del informe del Track 2.
2. **Todo el esfuerzo va al Track 2:** informe, repositorio reproducible, vídeo de 3 minutos,
   y caracterización del mecanismo. Ver [[Track 2 - requisitos]].
3. **El campo real es mucho menor de lo que parece.** 45 personas saben producir un CSV.
   Cuántas grabarán un vídeo, escribirán un informe y publicarán un repo reproducible
   sobre reposicionamiento farmacológico es otra cuestión, y el número será bastante menor.

## Predicción falsable

Si es cierta, el número de entregas del Track 2 será **sustancialmente inferior** a 45,
y la dispersión de calidad entre ellas será alta.

## Cómo se refuta

Observando el volumen de entregas del Track 2 conforme se acerque el cierre. Si acabara
habiendo decenas de informes sólidos, la hipótesis de campo reducido cae —aunque la
premisa principal (que el Track 1 no discrimina) seguiría en pie.

## Pregunta abierta

Los nombres de fichero del leaderboard llevan prefijos `model1_` a `model4_`. Se desconoce
si corresponden a intentos permitidos, a modelos de análisis distintos, o a **más de un
probando**. El documento de fenotipo se llama `Challenge_Clinical_Phenotype_1.docx`, y ese
`_1` apunta en la misma dirección. **Conviene aclararlo en el Space antes de diseñar la entrega.**
