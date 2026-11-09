# Plan de la práctica U2

Práctica individual: «Medir el filtrado y la repetibilidad de los detectores».
Entrega: `U2_Practica_Hernandez_Ismael.zip`. Autor: Ismael Hernández.
Semilla global: `20260101`. Semilla auxiliar para barridos previos: `20260102`.

## Reglas de trabajo

- Ningún parámetro se elige a ojo. Cada umbral, sigma, tamaño de kernel y porcentaje sale de un barrido con un criterio escrito antes de mirar los resultados.
- Todo número que aparezca en la memoria o en `hallazgos.md` sale de un CSV generado por el código. Los valores del enunciado son ejemplos y no se copian.
- Un resultado negativo bien medido cuenta igual que uno espectacular. Si una afirmación de la unidad no se confirma, se dice.
- Los originales de `data/` no se tocan. El código comprueba su SHA-256 al arrancar.
- Las figuras y los CSV se generan desde el código. Nada se edita a mano.
- El texto entregable va en español de España, en primera persona y con cifras en la misma frase o en la siguiente.

## Decisiones de partida

| Tema | Decisión | Motivo |
|---|---|---|
| Entorno | `uv` con Python 3.13.15 y venv en `_trabajo/venv` | Es la versión con la que se ejecutó U1 y evita sorpresas de ruedas en 3.14 |
| Dependencias | `numpy==2.5.4`, `opencv-python-headless==5.0.0.93`, `scipy==1.18.1`, `scikit-image==0.26.0`, `pandas==3.1.1`, `matplotlib==3.11.2`, `ipykernel==7.4.0`, `ipython==9.17.1` | Versiones fijadas y probadas en la máquina; SIFT se comprueba con una llamada real |
| Imágenes de trabajo | Gris uint8 por código; lado mayor a 512 px con `INTER_AREA` | 180 celdas y medianas propias; los originales quedan intactos |
| Borde | `BORDER_REFLECT_101` en OpenCV y `np.pad(mode="reflect")` en las implementaciones propias | Mismo modo en todos los filtros; `reflect` de NumPy equivale a `REFLECT_101` |
| Ruido | Un generador por celda con `SeedSequence([20260101, idx_imagen, idx_condicion])`; las funciones reciben el generador | El RNG global del enunciado depende del orden de las celdas; así el ruido es idéntico entre ejecuciones |
| Sal y pimienta | Coordenadas con reemplazo, como el enunciado; se mide la fracción realmente alterada | Dos impactos pueden caer en el mismo píxel y un píxel puede quedar igual |
| PSNR | `data_range=255`, siempre frente a la limpia | Convención declarada |
| SSIM | `gaussian_weights=True`, `sigma=1.5`, `use_sample_covariance=False`, `data_range=255` | Formulación original de Wang |
| Tiempo | Calentamiento de 1 ejecución y mediana de 5 repeticiones, `cv2.setNumThreads(1)` | Comparable entre filtros de OpenCV; los propios en NumPy no se comparan con OpenCV |
| Gamma | `(entrada/255)^gamma · 255` con LUT redondeada a uint8 | Misma convención que U1 |
| Rutas | Relativas a la raíz del proyecto; el notebook se ejecuta desde `U2_Practica_Hernandez_Ismael/` | Reproducibilidad |
| Decimales | Punto en CSV; coma en texto y pies; PSNR 2, SSIM 3, tiempo 1 | Coherencia de formato |
| Figuras | PNG a 160 dpi, ejes rotulados con unidades, barra de color en mapas, escalas compartidas y pie con parámetros y cifra | Rúbrica de comunicación |

### Filtros de la rejilla

1. `media`, `k=3`.
2. `media`, `k=5` (añadida para completar los diez; homóloga de la mediana 5×5).
3. `gaussiano`, `sigma=1.0`, núcleo `2*ceil(3σ)+1 = 7`.
4. `gaussiano`, `sigma=2.0`, núcleo `13`.
5. `mediana`, `k=3` (implementación propia vectorizada con `reflect`; contraste con `cv2.medianBlur` en el interior).
6. `mediana`, `k=5` (implementación propia vectorizada con `reflect`; contraste con `cv2.medianBlur` en el interior).
7. `mediana_hibrida`, `k=3`, según la lección 13: mediana de la cruz, mediana de las diagonales y mediana de `[cruz, diagonal, centro]`, con el centro incluido en ambos jurados.
8. `mediana_truncada`: media recortada con ventana `k` y porcentaje `alpha` elegidos por barrido; control literal de la lección 14.
9. `bilateral`, configuración A elegida por barrido.
10. `bilateral`, configuración B elegida por barrido.

### Definiciones fijadas

- **Mediana truncada.** La lección 14 dice: ordenar la ventana, recortar un porcentaje `alpha` de los valores más bajos y otro `alpha` de los más altos, y tomar la mediana de lo que queda. Con recorte simétrico esa operación es idénticamente la mediana y `alpha` no tendría efecto. Para que el truncamiento haga algo, la rejilla usa la media de los valores que quedan (media recortada) y se conserva la versión literal como control que demuestra la equivalencia. Ventana y `alpha` salen de un barrido con semilla auxiliar: `k ∈ {3,5,7}`, `alpha ∈ {0,1; 0,2; 0,3; 0,4}`; criterio: máximo SSIM medio en las tres imágenes y las tres condiciones gaussianas, con desempate por PSNR medio, luego menor `k` y luego menor `alpha`. El control literal usa el mismo `k` y `alpha` y demuestra que coincide con la mediana completa.
- **Bilateral.** Barrido previo de `d`, `sigmaColor` y `sigmaSpace` con semilla auxiliar sobre ruido gaussiano σ=20. Configuración A: la de mayor SSIM medio. Configuración B: la de mayor PSNR medio. Si coinciden, se toma la siguiente mejor distinta. Una sola pareja para las tres imágenes.
- **Perfil radial.** Perfil del enunciado sobre el espectro de la imagen filtrada en float32, con ventana Hann y recorte cuadrado central. Además, perfil de la respuesta en frecuencia del propio filtro (respuesta al impulso con relleno de ceros). Frecuencia en ciclos por píxel = radio / lado. Corte por interpolación lineal del cruce de 0,5. Rebote: máximo local con prominencia mayor o igual que `epsilon`; `epsilon` se elige por barrido como el menor que da cero rebotes en todos los gaussianos.
- **Canny.** Percentiles sobre las magnitudes de Sobel 3×3 no nulas de la imagen ya suavizada, con `L2gradient=True` en `cv2.Canny`. Umbral bajo = fracción del alto, truncado a entero. Tolerancia de 2 px con transformada de distancia. Si no se detecta ningún píxel, precisión 0. El σ del suavizado previo sale de un barrido con criterio declarado.
- **Repetibilidad.** Lógica del enunciado, generalizada para recibir detector, homografía y una LUT fotométrica opcional aplicada solo a la imagen transformada. Se conserva el recorte de puntos proyectados fuera del encuadre. Rotaciones alrededor del centro de píxeles `((w-1)/2, (h-1)/2)`, imágenes cuadradas por recorte central, `INTER_LINEAR` y `BORDER_CONSTANT`. Test obligatorio: 90° igual a `np.rot90`; escala 1,0 y gamma 1,0 igual a 1,0. Línea base de azar por densidad.

## Incoherencias y matices del enunciado

1. **«Diez filtros» con nueve en la lista.** La tabla enumera media 3×3, gaussiano σ=1,0 y 2,0, mediana 3×3 y 5×5, híbrida, truncada y bilateral ×2. Son nueve. Se añade media 5×5 y se marca en `parametros` y en la memoria.
2. **«Cinco casos» con siete perfiles.** El Ejercicio 2 dice cinco y enumera original, caja 3×3, 5×5, 9×9 y gaussiano σ=0,8; 1,6; 3,0. Se calculan los siete.
3. **Mediana truncada.** El enunciado no la define; la lección 14 sí, pero su definición literal coincide con la mediana. Se resuelve como media recortada con control literal, documentado.
4. **CSV adicionales.** La estructura obligatoria lista cuatro CSV. Se mantienen esos cuatro con nombres y columnas exactas y se añaden CSV auxiliares de evidencia (`ruido_fraccion_real.csv`, `registro_parametros.csv`, `barrido_aux_*.csv`, etc.). No sustituyen a los obligatorios.
5. **Canny sin operador fijado.** El enunciado no fija `L2gradient` ni el operador. Se declara Sobel 3×3 y `L2gradient=True`, y los percentiles se calculan sobre la imagen suavizada para que umbral y magnitud estén en la misma escala.
6. **Centro de rotación.** El enunciado dice «centro de la imagen». Se usa el centro de píxeles y se añade el control con medio píxel de desfase.

## Fases

### Fase 0. Reconocimiento y andamiaje

- [x] Inspeccionar el entorno y localizar el enunciado y el material de la unidad.
- [x] Crear `PLAN.md`, `_trabajo/BITACORA.md` y los árboles de entrega y trabajo.
- [x] Crear el venv con Python 3.13.15 e instalar las versiones fijadas.
- [x] Comprobar `cv2.SIFT_create`, `cv2.ORB_create`, `cv2.FastFeatureDetector_create` y `skimage.metrics` con llamadas reales.
- [x] Copiar el enunciado a `_trabajo/enunciado/` y crear las herramientas base.

**Hecho cuando:** el venv funciona, los cuatro detectores y métricas responden, las decisiones y las incoherencias están en la bitácora y las herramientas base existen.

### Fase 1. Imágenes de partida

- [x] Proponer tres candidatas con licencia (textura fina, regiones uniformes con bordes, ruido real) y obtener el visto bueno.
- [x] Copiar los originales a `data/` sin tocarlos, con SHA-256 y fuente.
- [x] Calcular tamaño, densidad de gradiente y MAD del Laplaciano; validar el papel de cada una.
- [x] Declarar la versión de trabajo y la limitación de la imagen con ruido real.

**Hecho cuando:** hay tres imágenes validadas, hashes y fuentes anotadas, versión de trabajo declarada y la limitación de la referencia con ruido real escrita.

### Fase 2. Predicciones y criterios

- [x] Escribir `_trabajo/predicciones.md` con cifras o rangos antes de medir.
- [x] Escribir `_trabajo/criterios_declarados.md` con todos los criterios que fijan parámetros.
- [x] Sellar ambos con SHA-256 y hora en `_trabajo/orden_declaraciones.log`.

**Hecho cuando:** los dos ficheros existen, su hash y hora son anteriores a cualquier CSV de `outputs/` y no falta ningún criterio.

### Fase 3. Núcleo reutilizable y tests

- [x] Implementar ruido, métricas, filtros, medianas propias vectorizadas, tiempos, perfil radial, puntuación de bordes y repetibilidad generalizada.
- [x] Escribir tests con casos de resultado conocido.
- [x] Ejecutar los barridos auxiliares (truncada, bilateral, σ de Canny, ε de rebote) con la semilla auxiliar.
- [x] Crear `outputs/registro_parametros.csv` (parcial; el notebook final añade los parámetros de E3/E4).

**Hecho cuando:** todos los tests pasan (mediana propia = `cv2.medianBlur`, híbrida y truncada = implementación ingenua, 90° = `np.rot90`, identidad = 1,0, PSNR/SSIM conocidos) y los barridos auxiliares están en CSV.

### Fase 4. Ejercicio 1

- [x] Generar la rejilla de 180 filas (3 imágenes × 6 condiciones × 10 filtros). En `IMG_03` no hay referencia limpia: sus columnas PSNR y SSIM quedan vacías y se analiza aparte con métricas sin referencia.
- [x] Escribir `outputs/resultados_denoising.csv` con las columnas exactas y un `assert` de 180 filas.
- [x] Generar las tablas de ganadores, mediana frente a media y bilateral frente a gaussiano.
- [x] Generar mapas de calor, curvas y montajes de recorte.
- [x] Analizar la imagen con ruido real por separado, sin usarla como *ground truth*.

**Hecho cuando:** hay 180 filas con columnas exactas, las cinco preguntas tienen cifra y las figuras tienen barra de color y escalas compartidas.

### Fase 5. Ejercicio 2

- [x] Calcular los siete perfiles en las tres imágenes, con las dos fuentes.
- [x] Obtener corte y rebotes, y barrer `epsilon`.
- [x] Emparejar cada caja con el gaussiano de corte más parecido y calcular SSIM.
- [x] Generar las figuras de perfiles.

**Hecho cuando:** hay siete perfiles, los gaussianos dan cero rebotes, las cajas dan rebotes mayores que cero o se explica lo contrario y están `perfiles_frecuencia.csv` y las curvas.

### Fase 6. Ejercicio 3

- [x] Generar la escena sintética de 512×512 y su referencia desde las primitivas.
- [x] Barrer el σ del suavizado previo y ejecutar la rejilla de 24 combinaciones.
- [x] Calcular el óptimo, la regla de la unidad y la pérdida.
- [x] Dibujar la curva precisión-exhaustividad y el mapa de F1.
- [x] Medir la estabilidad con 10 realizaciones de ruido.
- [x] Transferir a las tres imágenes reales por percentiles y por umbrales absolutos.

**Hecho cuando:** hay 24 filas con columnas exactas, la pérdida está cuantificada, la estabilidad medida y la transferencia descrita con cifras.

### Fase 7. Ejercicio 4

- [x] Construir las homografías y pasar los tests de 90°, identidad y escala 1,0.
- [x] Ejecutar los tres barridos con FAST, ORB y SIFT sobre las tres imágenes.
- [x] Calcular la línea base de azar.
- [x] Barrer el umbral FAST, `tol` y la pirámide de ORB.
- [x] Responder las tres preguntas con cifras y figuras.

**Hecho cuando:** los tests son exactos, están las tres curvas frente a escala con azar y las preguntas 1 a 3 tienen cifra.

### Fase 8. Hallazgos

- [x] Escribir `memoria/hallazgos.md` con exactamente cinco afirmaciones, cada una con `Fuente:` y `Límite:`.
- [x] Incluir una sorpresa real o declarar su ausencia.
- [x] Verificar cada cifra con un script contra el CSV y la fila citados.

**Hecho cuando:** hay cinco afirmaciones exactas, todas verificadas y con límite de validez.

### Fase 9. Memoria

- [x] Generar `memoria/informe.pdf` con WeasyPrint desde los CSV.
- [x] Rasterizar las páginas y revisar desbordes, figuras cortadas y tablas rotas.
- [x] Pasar el linter de voz (revisión manual de primera persona).
- [x] Revisión visual del PDF hecha; queda la confirmación final del autor.

**Hecho cuando:** el PDF existe, cada pregunta está localizable por número, las figuras cumplen los requisitos y no hay desbordes.

### Fase 10. Cierre

- [x] Convertir `banco_pruebas.py` en `banco_pruebas.ipynb` y ejecutarlo con el kernel limpio.
- [x] Escribir `codigo/requirements.txt` con versiones fijadas y comprobar SIFT.
- [x] Ejecutar la prueba en limpio en un directorio temporal y comparar los CSV salvo `tiempo_ms`.
- [x] Verificar rejillas, cifras, figuras y voz; revisar la rúbrica punto por punto.
- [x] Empaquetar el zip y comprobar nombre, estructura, tamaño y hashes.

**Hecho cuando:** la ejecución limpia regenera todo, los verificadores pasan y el zip tiene la estructura exacta.

## Paradas previstas

- Faltan imágenes adecuadas.
- La definición de mediana truncada no encaja con el material de clase (resuelto: media recortada con control literal).
- La revisión visual de figuras: el autor revisa los montajes; el código comprueba ejes, barras, escalas y desbordes.
- Si 512 px cambia alguna conclusión, se repite un subconjunto a 768 px y se declara.
