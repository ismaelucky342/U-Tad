# Predicciones antes de medir

Escritas el 8 de noviembre de 2026, después del diagnóstico de las imágenes y antes de ejecutar cualquier barrido o rejilla. No se ha calculado todavía ningún PSNR, SSIM, perfil, F1 ni repetibilidad. Las cifras son rangos y ordenaciones falsables: si los datos las contradicen, se dirá.

Las predicciones se apoyan en la teoría de la unidad y en las propiedades medidas en `_trabajo/diagnostico_originales.csv`: `IMG_01` es textura fina y limpia; `IMG_02` tiene regiones uniformes, bordes fuertes y un 35,07 % de píxeles saturados; `IMG_03` tiene ruido real y no tiene referencia limpia.

## Ejercicio 1. Rejilla de denoising

### Ganadores por condición

| Condición | Ganador esperado en PSNR | Ganador esperado en SSIM | Comentario |
|---|---|---|---|
| Sal y pimienta 5 % | mediana 3×3 o 5×5 | mediana 3×3 | A baja densidad, la ventana pequeña conserva más detalle. |
| Sal y pimienta 10 % | mediana 5×5 | mediana 5×5 o híbrida 3×3 | La mediana 5×5 elimina más impulsos; la híbrida conserva esquinas. |
| Sal y pimienta 30 % | mediana 5×5 | mediana 5×5 | La densidad alta exige ventana grande; la mediana 3×3 deja impulsos. |
| Gaussiano σ=10 | gaussiano σ=1,0 | gaussiano σ=1,0 o bilateral A | Poco ruido: el suavizado suave gana; el bilateral puede empatar en SSIM. |
| Gaussiano σ=20 | gaussiano σ=2,0 o bilateral A | bilateral A o bilateral B | El bilateral debería preservar mejor los bordes; el gaussiano puede ganar en PSNR. |
| Gaussiano σ=40 | gaussiano σ=2,0 | bilateral A o bilateral B | A ruido alto, el gaussiano σ=2,0 suaviza mucho; el bilateral conserva bordes pero puede dejar grano. |

Predicciones concretas:

1. **Mediana frente a media con ruido impulsivo.** La mediana supera a la media en PSNR y SSIM en los tres niveles de sal y pimienta, en las dos imágenes con referencia. La ventaja crece con el porcentaje: espero una diferencia de PSNR de 2–6 dB al 5 %, de 4–10 dB al 10 % y de 8–15 dB al 30 %. Si la ventaja se reduce al 30 %, será porque la mediana 5×5 empieza a borrar detalle y el SSIM lo penaliza.
2. **Mediana con ruido gaussiano.** La mediana pierde frente al gaussiano y al bilateral en PSNR y SSIM. La brecha crece con σ: espero 1–3 dB a σ=10, 3–6 dB a σ=20 y 5–9 dB a σ=40. La mediana 3×3 estará más cerca a σ=10; la mediana 5×5 sobre-suaviza a σ=40 y pierde SSIM en la textura.
3. **Bilateral frente a gaussiano.** El bilateral será entre 10 y 60 veces más lento que un gaussiano de suavizado comparable. En SSIM espero una ventaja del bilateral de 0,00–0,02 en `IMG_01` y de 0,01–0,05 en `IMG_02` (bordes de la manzana). En PSNR el bilateral puede quedar por debajo del gaussiano, sobre todo a σ=40.
4. **Discrepancia PSNR/SSIM.** Espero al menos un caso en el que el filtro con mejor PSNR no sea el de mejor SSIM. Candidato: gaussiano σ=2,0 frente a bilateral en `IMG_01` con σ=20 o 40. El gaussiano reparte el error y gana PSNR; el bilateral conserva la estructura y gana SSIM, o al contrario si el bilateral deja grano.
5. **`IMG_02` y la saturación.** El 35,07 % de píxeles a 255 hará que el ruido gaussiano se recorte en el fondo y que las cifras absolutas de PSNR/SSIM sean más altas que en `IMG_01`. También espero que el ranking en `IMG_02` esté dominado por el fondo blanco y sea menos discriminante que en `IMG_01`. Si el ranking cambia mucho al mirar solo la máscara no saturada, lo diré.
6. **`IMG_03` sin referencia.** No habrá PSNR/SSIM válidos. En el análisis sin referencia espero que la mediana y el bilateral reduzcan el σ del Laplaciano más que el gaussiano, pero que el bilateral conserve mejor el borde de la taza. El gaussiano dejará el grano más suave pero el borde más lavado.
7. **Caso visual frente a métrica.** Candidato: en `IMG_01` con ruido gaussiano, el gaussiano σ=2,0 puede ganar PSNR y verse más borroso que el bilateral; o el bilateral puede ganar SSIM y dejar un grano visible que a simple vista molesta. Si no encuentro un caso claro, lo diré.

## Ejercicio 2. Perfil radial

1. **Frecuencia de corte.** Espero que disminuya al aumentar el tamaño o σ: caja 9×9 < caja 5×5 < caja 3×3 y gaussiano σ=3,0 < σ=1,6 < σ=0,8. Rangos esperados en ciclos/píxel: caja 3×3, 0,13–0,17; caja 5×5, 0,08–0,10; caja 9×9, 0,04–0,06; gaussiano σ=0,8, 0,14–0,18; σ=1,6, 0,07–0,10; σ=3,0, 0,04–0,06. La caja 9×9 y el gaussiano σ=3,0 deberían quedar cerca.
2. **Rebotes.** Los tres gaussianos tendrán cero rebotes con el ε elegido. Las tres cajas tendrán al menos uno; espero más rebotes en la caja 9×9 que en la 3×3. La respuesta del filtro mostrará los lóbulos con más claridad que el perfil de la imagen filtrada, porque el promedio radial y el contenido de la imagen los suavizan. Si el perfil de la imagen filtrada da cero rebotes en alguna caja, no lo interpretaré como ausencia de lóbulos: miraré la respuesta del filtro.
3. **Emparejamientos.** Espero caja 3×3 con gaussiano σ=0,8, caja 5×5 con σ=1,6 y caja 9×9 con σ=3,0, porque sus cortes caen en la misma zona. Si alguna pareja cambia, será porque el corte medido sobre la imagen se desvía del corte teórico.
4. **SSIM a igual suavizado.** Espero que el gaussiano conserve mejor la imagen que la caja en las tres parejas: el gaussiano no tiene lóbulos laterales y la caja deja *ringing* en los bordes. La diferencia será pequeña en `IMG_01` (0,005–0,02) y mayor en `IMG_02` (0,01–0,05), donde los bordes son fuertes. Si la caja gana en SSIM, será una sorpresa: significaría que su corte más alto o su roll-off más abrupto compensan el *ringing* en esta imagen.

## Ejercicio 3. Canny

1. **σ del suavizado previo.** Espero que el mejor σ esté entre 1,0 y 1,5. Con σ=0 el ruido de σ=15 creará bordes falsos y la precisión caerá; con σ=2,0 los bordes de bajo contraste se perderán y la exhaustividad bajará. El mejor F1 esperado está entre 0,85 y 0,95.
2. **Óptimo frente a regla de la unidad.** Espero que el óptimo esté en percentil alto 85–90 y fracción baja 0,4–0,6. La regla de la unidad (percentil 85, fracción 0,5) perderá entre 0,01 y 0,05 de F1. Si pierde más de 0,10, la regla general será mala para esta escena; si pierde menos de 0,01, será casi óptima.
3. **Curva precisión–exhaustividad.** Al subir el percentil alto, la precisión subirá y la exhaustividad bajará. La fracción baja tendrá un efecto menor, sobre todo cuando el umbral alto ya es selectivo. Espero un codo cerca del percentil 85–90.
4. **Transferencia a las imágenes reales.** Espero que los umbrales absolutos óptimos de la escena sintética **no** transfieran bien: en `IMG_01` producirán demasiados bordes (textura y ruido) y baja precisión; en `IMG_02` detectarán solo los bordes fuertes y perderán los débiles; en `IMG_03` detectarán grano. La regla de percentiles por imagen se adaptará mejor. El número de píxeles de borde con el óptimo absoluto puede ser 2–10 veces el de la regla de la unidad en `IMG_01`. Si la transferencia es buena, será una sorpresa y lo destacaré.
5. **Estabilidad.** Con 10 realizaciones de ruido, espero una desviación típica de F1 menor que 0,02 para las reglas de percentiles. La regla de la unidad y la óptima serán parecidas; la óptima puede sobreajustar la realización principal y ser algo menos estable.

## Ejercicio 4. Repetibilidad

1. **FAST y escala.** FAST no es invariante a escala. A escala 1,0 la repetibilidad será 1,0 (identidad). A 0,5 espero 0,3–0,6 y a 2,0 espero 0,4–0,7. La curva no será plana: caerá en los extremos. Si a 0,5 y 2,0 se mantiene por encima de 0,8, refutaré la afirmación de que FAST básico no es invariante a escala en estas imágenes.
2. **Rotación.** La curva tendrá estructura. Espero 0° y 90° altos (0,9–1,0), 45° el mínimo (0,4–0,7) y los ángulos intermedios entre ambos. La recuperación a 90° se debe a que la rejilla de píxeles vuelve a alinearse; el control con medio píxel de desfase bajará (0,7–0,9). Si la curva es plana, el test del anillo sería más invariante de lo que sugiere la teoría.
3. **Iluminación.** Espero que gamma 0,8 y 1,3 conserven mejor la repetibilidad que 0,6 y 1,7. FAST, que compara diferencias de intensidad con un umbral fijo, será más sensible al cambio de contraste que SIFT. ORB quedará entre ambos. Si SIFT no es el más estable, lo diré.
4. **Multiescala.** ORB y SIFT tendrán curvas de escala más planas que FAST. En 0,5 y 2,0 espero que SIFT y ORB superen a FAST en 0,2–0,4 de repetibilidad; SIFT puede ser el más estable y ORB quedar cerca. A escala 1,0 los tres darán 1,0. Esta diferencia será la demostración empírica de por qué existen los detectores multiescala.
5. **Línea base de azar.** Con unos 1000 keypoints, `tol=3` y un recorte de 341×341, la probabilidad de acertar por azar estará entre 0,1 y 0,3. No es despreciable: una repetibilidad de 0,4 puede estar cerca del azar. En `IMG_02`, con menos keypoints, la línea base será menor y una repetibilidad alta será más significativa. Compararé siempre con la línea base.
6. **Dependencia de la imagen.** Espero que `IMG_01` tenga más keypoints y una repetibilidad a 45° menor que `IMG_02`, porque su textura fina cambia más con la rotación. `IMG_03` tendrá keypoints espurios por el ruido y una repetibilidad más baja. Si la manzana, con menos puntos, da una repetibilidad más baja por falta de puntos, será un matiz interesante.

## Posibles sorpresas que estaría dispuesto a reconocer

- Que la regla de Canny de la unidad sea casi óptima (pérdida < 0,01) y que los umbrales absolutos transferidos sean el problema, no la regla.
- Que la caja conserve mejor el SSIM que el gaussiano a igual corte.
- Que el bilateral no compense su coste en ninguna imagen.
- Que la repetibilidad a 90° no sea 1,0 por el muestreo del warp.
- Que la mediana híbrida no supere a la mediana estándar en las esquinas de estas imágenes.

Si ninguna se cumple, revisaré los datos y buscaré la sorpresa en los detalles, no la inventaré.
