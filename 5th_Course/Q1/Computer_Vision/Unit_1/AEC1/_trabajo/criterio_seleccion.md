# Criterio de selección (fijado antes de ejecutar el barrido)

Fecha de fijación: 26 de octubre de 2026, antes de generar `outputs/resultados_u1.csv`.

## Por imagen

Entre las configuraciones procesadas que cumplan a la vez `sat_bajo <= 1,00 %` y
`sat_alto <= 1,00 %`, se elige la de mayor `rango_p1_p99`. Si hay empate, gana la de
mayor `entropia`; si el empate persiste, la configuración más sencilla según el orden
`gamma`, `estiramiento`, `he`, `clahe` y, dentro de cada operación, el orden en que
aparecen sus parámetros en el barrido.

La fila `original` no compite. Se conserva como línea base y se compara con la ganadora
para decidir si el procesado mejora de verdad. Si ninguna configuración procesada mejora
a la original, se dirá con las cifras delante.

Si ninguna configuración procesada cumple las dos restricciones para una imagen, se elige
la que minimice `max(sat_bajo, sat_alto)`. El desempate es mayor `rango_p1_p99`, después
mayor `entropia` y, por último, el orden de sencillez anterior. Esta regla se aplica tal
cual, sin retocarla después de ver los resultados.

## Para el lote

La configuración única del contrato será la que cumpla las dos restricciones en más
imágenes de las cinco. El desempate es el mayor rango medio de `rango_p1_p99` entre las
cinco imágenes, después la mayor entropía media y, por último, el orden de sencillez.
La fila `original` tampoco compite en el lote: el contrato debe describir un procesado
aplicable, no la ausencia de procesado.

## Tratamiento de gamma = 1,0

`gamma` con `g=1.0` es una operación procesada a efectos del barrido, pero su efecto es
prácticamente el de la original salvo el redondeo de la ida y vuelta de color. Puede
ganar por el criterio si sus métricas son las mejores; si eso ocurre, se comentará que
la ganancia procede del redondeo y no de un realce real.
