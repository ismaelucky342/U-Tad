# Criterios declarados antes de medir

Escritos el 8 de noviembre de 2026, después del diagnóstico de las imágenes y antes de ejecutar cualquier barrido, rejilla o cálculo de resultados. Este documento fija todos los parámetros que no se eligen a ojo. Si un criterio cambia después de ver resultados, se anota en `_trabajo/BITACORA.md`, se justifica y se vuelve a sellar; no se cambia en silencio.

## 0. Convenciones comunes

### Imágenes y versiones

- Originales: `data/IMG_01.jpg` (follaje, textura fina), `data/IMG_02.jpg` (manzana, regiones uniformes) y `data/IMG_03.jpg` (ruido real ISO 6400). No se modifican.
- El código comprueba al arrancar el SHA-256 de los tres originales contra los valores del manifiesto. Si no coincide, se detiene.
- Versión de trabajo: gris `uint8`, lado mayor 512 con `cv2.INTER_AREA`. Se genera por código desde el original. Para las imágenes no cuadradas, el recorte cuadrado central se hace después, cuando el ejercicio lo pida.
- `IMG_03` no tiene referencia limpia. No se usa como *ground truth*. En el Ejercicio 1 sus columnas `psnr` y `ssim` quedan vacías y se analiza con métricas sin referencia.
- `IMG_02` tiene un 35,07 % de píxeles saturados a 255. Se documenta el efecto del recorte del ruido gaussiano. Si el ranking de filtros cambia al mirar solo la máscara no saturada (`limpia < 250`), se añade el control en `outputs/resultados_denoising_mask.csv`.

### Borde, semillas y reproducibilidad

- Borde en OpenCV: `cv2.BORDER_REFLECT_101`. En implementaciones propias: `np.pad(mode="reflect")`, equivalente. La mediana propia usa `reflect`; `cv2.medianBlur` se usa solo como contraste en el interior, porque no permite elegir el borde.
- Semilla global: `20260101`. Semilla auxiliar para todos los barridos previos: `20260102`.
- Cada celda usa un generador propio: `SeedSequence([semilla, idx_imagen, idx_condicion])`. Las funciones de ruido reciben el generador; no se usa el RNG global. Las imágenes ruidosas deben ser idénticas entre ejecuciones.
- Rutas relativas a la raíz `U2_Practica_Hernandez_Ismael/`. El notebook se ejecuta desde esa carpeta.
- Ninguna celda instala paquetes. Las versiones van en `codigo/requirements.txt`.
- Los CSV y las figuras se generan desde el código. No se editan a mano.
- Los tiempos se miden con `cv2.setNumThreads(1)`, un calentamiento y la mediana de 5 repeticiones. Se cronometra solo la llamada al filtro. Los filtros propios en NumPy no se comparan directamente con los de OpenCV en tiempo; se declara en la memoria.

### Métricas

- PSNR: `skimage.metrics.peak_signal_noise_ratio(referencia, salida, data_range=255)`. Si las imágenes son idénticas, se devuelve `inf` sin aviso.
- SSIM: `skimage.metrics.structural_similarity(referencia, salida, data_range=255, gaussian_weights=True, sigma=1.5, use_sample_covariance=False)`. Se usa la formulación original de Wang. Para el control por máscara, se usa `full=True` y se promedia el mapa SSIM sobre la máscara.
- Redondeo en texto: coma decimal; PSNR 2 decimales, SSIM 3, tiempo 1, F1 3, repetibilidad 3. En CSV: punto decimal y precisión suficiente para reproducir.
- Las comparaciones entre figuras comparten escala en el eje vertical cuando son comparables.

### Salidas obligatorias

- `outputs/resultados_denoising.csv`: columnas exactas `imagen,tipo_ruido,nivel,filtro,parametros,psnr,ssim,tiempo_ms`.
- `outputs/perfiles_frecuencia.csv`: columnas `imagen,filtro,parametros,fuente,f_corte,rebotes,ssim_vs_original`.
- `outputs/barrido_canny.csv`: columnas exactas `percentil_alto,fraccion_baja,umbral_alto,umbral_bajo,precision,recall,f1,px_borde`.
- `outputs/repetibilidad.csv`: columnas `imagen,detector,transformacion,valor,repetibilidad,n_orig,n_trans,n_validos,tol,azar`.
- Se permiten CSV auxiliares de evidencia. No sustituyen a los cuatro obligatorios.

## 1. Ejercicio 1. Rejilla de denoising

### Ruido

- Sal y pimienta: `p ∈ {0,05; 0,10; 0,30}`. Se eligen `n = int(p * alto * ancho)` coordenadas con reemplazo; cada una se sustituye por 0 o 255 con probabilidad 1/2. Se mide la fracción realmente alterada respecto a la limpia y se guarda en `outputs/ruido_fraccion_real.csv`.
- Gaussiano: `σ ∈ {10, 20, 40}`. Se suma `rng.normal(0, σ, forma)` a la imagen en `float32`, se recorta a `[0,255]` y se convierte a `uint8`. Se mide el σ empírico del error y la fracción de píxeles recortados; se guardan en el mismo CSV auxiliar.
- Condiciones de la rejilla: las seis anteriores. No hay condición «limpia»: la imagen limpia es la referencia, no una celda.
- El ruido se genera una vez por celda y se usa para los diez filtros de esa condición, de modo que todos los filtros ven exactamente la misma imagen ruidosa.

### Filtros (diez)

| Nº | `filtro` | `parametros` | Implementación |
|---|---|---|---|
| 1 | `media` | `k=3` | `cv2.blur`, borde `REFLECT_101`. |
| 2 | `media` | `k=5` | `cv2.blur`, borde `REFLECT_101`. |
| 3 | `gaussiano` | `sigma=1.0;k=7` | `cv2.GaussianBlur`, borde `REFLECT_101`; `k = 2*ceil(3σ)+1 = 7`. |
| 4 | `gaussiano` | `sigma=2.0;k=13` | `cv2.GaussianBlur`, borde `REFLECT_101`; `k = 13`. |
| 5 | `mediana` | `k=3` | Mediana propia vectorizada con `reflect`; contraste con `cv2.medianBlur` en el interior. |
| 6 | `mediana` | `k=5` | Mediana propia vectorizada con `reflect`; contraste con `cv2.medianBlur` en el interior. |
| 7 | `mediana_hibrida` | `k=3` | Algoritmo de la lección 13: cruz = fila + columna de la ventana (el centro aparece dos veces); diagonales = las dos diagonales concatenadas (el centro aparece dos veces); `m_cruz = mediana(cruz)`, `m_diag = mediana(diagonales)`; salida = `mediana([m_cruz, m_diag, centro])`. Borde `reflect`. |
| 8 | `mediana_truncada` | `k=<elegido>;alpha=<elegido>` | Media recortada: ordenar la ventana, recortar `m = floor(alpha*k²)` valores por cada cola y promediar los que quedan. Si quedan menos de 1, la combinación se descarta en el barrido. Borde `reflect`. |
| 9 | `bilateral_A` | `d=<elegido>;sc=<elegido>;ss=<elegido>` | `cv2.bilateralFilter`, borde `REFLECT_101`; configuración A por SSIM. |
| 10 | `bilateral_B` | `d=<elegido>;sc=<elegido>;ss=<elegido>` | `cv2.bilateralFilter`, borde `REFLECT_101`; configuración B por PSNR. |

- La mediana truncada literal de la lección 14 (recortar y **tomar la mediana** de lo que queda) se implementa como control, no como filtro de la rejilla. Con recorte simétrico coincide con la mediana completa; el control lo demuestra para `k=3,5,7` y todos los `alpha`. La rejilla usa la media recortada porque es la única versión en la que `alpha` tiene efecto.
- Los nombres `bilateral_A` y `bilateral_B` mantienen los diez filtros distinguibles. En la memoria se explican como las dos configuraciones del bilateral.

### Barrido de la mediana truncada

- Rejilla: `k ∈ {3,5,7}`, `alpha ∈ {0,1; 0,2; 0,3; 0,4}`. Doce combinaciones.
- Datos: las tres imágenes de trabajo, ruido gaussiano con σ ∈ {10,20,40}, semilla auxiliar `20260102`. Cada celda usa su propio generador.
- Métrica: SSIM frente a la limpia.
- Criterio: se elige la combinación con mayor SSIM medio sobre las 3 imágenes × 3 niveles. Desempate: mayor PSNR medio; luego menor `k`; luego menor `alpha`.
- Se elige una sola pareja `(k, alpha)` para todas las imágenes y condiciones.
- El resultado se guarda en `outputs/barrido_aux_truncada.csv` con columnas `k,alpha,m,ssim_medio,psnr_medio`.

### Barrido del bilateral

- Rejilla: `d ∈ {5,7,9,11}`, `sigmaColor ∈ {25,50,75,100}`, `sigmaSpace ∈ {5,10,20}`. 48 combinaciones.
- Datos: las tres imágenes de trabajo, ruido gaussiano σ=20, semilla auxiliar `20260102`.
- Configuración A: la de mayor SSIM medio. Configuración B: la de mayor PSNR medio. Si coinciden, B es la siguiente mejor distinta por PSNR.
- Una sola pareja A y una sola pareja B para las tres imágenes y todas las condiciones.
- Resultado en `outputs/barrido_aux_bilateral.csv` con columnas `d,sigma_color,sigma_space,psnr_medio,ssim_medio,configuracion`.

### Rejilla principal

- 3 imágenes × 6 condiciones × 10 filtros = 180 filas.
- Orden: imagen (`IMG_01`, `IMG_02`, `IMG_03`), tipo de ruido (`sal_pimienta`, `gaussiano`), nivel ascendente, filtro en el orden de la tabla.
- `nivel` es texto: `0.05`, `0.10`, `0.30` para sal y pimienta; `10`, `20`, `40` para gaussiano.
- `psnr` y `ssim`: frente a la imagen limpia de trabajo. Para `IMG_03` quedan vacíos porque no hay referencia limpia.
- `tiempo_ms`: mediana de 5 repeticiones, con calentamiento, solo la llamada al filtro.
- `assert`: 180 filas; 60 por imagen; 10 por condición; las seis condiciones y los diez filtros presentes en cada imagen.
- Para `IMG_03` se genera aparte `outputs/analisis_ruido_real.csv` con `imagen,tipo_ruido,nivel,filtro,parametros,sigma_laplaciano_entrada,sigma_laplaciano_salida,reduccion_sigma,mad_cambio,brillo_medio`. El σ del Laplaciano usa el mismo kernel y estimador que el diagnóstico (`median(|L|)/(0.6745*6)`). No se presenta como calidad de denoising, sino como reducción de rugosidad y cambio respecto a la entrada.

### Análisis

- Ganadores por imagen y condición: máximo PSNR y máximo SSIM por separado. Empate: menor tiempo.
- Mediana frente a media: se comparan `mediana k=3` con `media k=3` y `mediana k=5` con `media k=5` en las seis condiciones. Se reporta la diferencia de PSNR y de SSIM.
- Bilateral frente a gaussiano comparable: `bilateral_A` y `bilateral_B` frente a `gaussiano sigma=2.0;k=13` y, si el corte lo justifica, frente a `gaussiano sigma=1.0;k=7`. Se reporta la razón de tiempos y la diferencia de SSIM.
- Discrepancia PSNR/SSIM: se busca una condición en la que el ganador de PSNR no sea el de SSIM y se explica qué mide cada métrica.
- Caso visual frente a métrica: se eligen recortes de `IMG_01` y `IMG_03` con el ganador de PSNR y el candidato visual; se documenta la comparación. Si no hay caso, se dice.
- La memoria usa `IMG_01` e `IMG_02` para las cifras de PSNR/SSIM y `IMG_03` para el análisis sin referencia.

## 2. Ejercicio 2. Perfil radial

### Imágenes y filtros

- Imagen principal: `IMG_01` (textura). Se repiten los cálculos en `IMG_02` e `IMG_03` como evidencia; las conclusiones se apoyan en la principal y se comprueba si se repiten.
- Recorte cuadrado central de la imagen de trabajo: lado = `min(alto, ancho)`.
- Filtros y casos (siete):
  - `original` (sin filtro), `parametros=ninguno`.
  - `caja_3`, `caja_5`, `caja_9`: `cv2.blur` con `k=3,5,9`, borde `REFLECT_101`.
  - `gaussiano_0.8`, `gaussiano_1.6`, `gaussiano_3.0`: `cv2.GaussianBlur` con `σ=0,8; 1,6; 3,0` y `k=2*ceil(3σ)+1 = 7; 11; 19`, borde `REFLECT_101`.
- Los siete casos son los del enunciado: original + tres cajas + tres gaussianos.

### Espectro y perfil

- Imagen en `float32`, gris, recortada al cuadrado central.
- Ventana de Hann 2D: `np.outer(np.hanning(lado), np.hanning(lado))`. Se aplica antes de la FFT para reducir la fuga espectral.
- Espectro: `np.fft.fftshift(np.fft.fft2(imagen_ventaneada))`; magnitud `np.abs`.
- Perfil radial: el del enunciado, con centro `(lado//2, lado//2)`, promediando por anillos enteros. Se normaliza por el valor en frecuencia cero. Frecuencia en ciclos/píxel = radio / lado.
- Se calcula el perfil de la imagen filtrada para los siete casos.
- Se calcula además el perfil de la respuesta del filtro para los seis filtros (no para el original): respuesta al impulso en una imagen del mismo lado con un delta en el centro, filtrada con el mismo borde, FFT y perfil radial. El original se representa como respuesta identidad plana; su corte no está definido y queda vacío en el CSV.
- El CSV `outputs/perfiles_frecuencia.csv` tiene 3 imágenes × 7 casos × 2 fuentes = 42 filas. `fuente` vale `imagen_filtrada` o `respuesta_filtro`. Para el caso `original` con `fuente=respuesta_filtro`, `f_corte` queda vacío y `rebotes=0` (la identidad es plana); para `original` con `fuente=imagen_filtrada` se mide su corte como referencia. Los seis filtros tienen corte y rebotes en las dos fuentes. `ssim_vs_original` solo se rellena en `imagen_filtrada`.
- `assert`: 42 filas; 7 casos y 2 fuentes por imagen.

### Frecuencia de corte

- Se busca el primer radio en el que el perfil normalizado cae por debajo de 0,5.
- Se interpola linealmente entre el último punto ≥ 0,5 y el primero < 0,5: `f_corte = r0 + (0,5 - p0) * (r1 - r0) / (p1 - p0)`, en ciclos/píxel.
- Si no hay cruce, `f_corte` queda vacío y se informa. No se espera en las cajas ni en los gaussianos.

### Rebotes

- Se considera el perfil a partir del primer índice en el que baja de 0,5.
- Se cuentan los máximos locales con prominencia mayor o igual que `epsilon`, usando `scipy.signal.find_peaks(..., prominence=epsilon)`.
- `epsilon` se elige por barrido sobre las tres respuestas gaussianas (`σ=0,8; 1,6; 3,0`) de la imagen principal: `np.logspace(-6, -1, 60)`. Se toma el menor `epsilon` que da cero rebotes en las tres. Si ninguno lo consigue, se amplía el rango y se declara. El valor elegido se usa para todos los perfiles.
- El barrido se guarda en `outputs/barrido_aux_epsilon.csv` con `epsilon,rebotes_gaussiano_0.8,rebotes_gaussiano_1.6,rebotes_gaussiano_3.0`.
- Se reportan los rebotes del perfil de la imagen y de la respuesta del filtro. Si difieren, se explica que el promedio radial y el contenido de la imagen suavizan los lóbulos.

### SSIM y emparejamiento

- `ssim_vs_original`: SSIM entre la imagen filtrada y la original limpia (sin ruido), con la configuración común.
- Para cada caja (`caja_3`, `caja_5`, `caja_9`) se elige el gaussiano (`0.8`, `1.6`, `3.0`) con menor `|f_corte_caja - f_corte_gaussiano|` usando los perfiles de `imagen_filtrada` de la imagen principal. Empate: menor σ.
- Se compara el SSIM de la caja y del gaussiano emparejados. La pregunta se responde con la diferencia de SSIM, no con impresiones.
- La tabla de parejas se guarda en `outputs/parejas_caja_gaussiano.csv` con `imagen,caja,parametros_caja,gaussiano,parametros_gaussiano,f_corte_caja,f_corte_gaussiano,delta_f,ssim_caja,ssim_gaussiano,delta_ssim`.
- Se repite el emparejamiento en `IMG_02` e `IMG_03` como comprobación; si cambia, se dice.

### Figuras

- Perfiles normalizados de los siete casos, con línea horizontal en 0,5 y marcas de corte; misma escala vertical.
- Perfiles de respuesta de los seis filtros, en panel aparte, con zoom en la zona de lóbulos.
- Comparación caja/gaussiano emparejados: curvas y SSIM en el pie.
- Ejes rotulados: frecuencia en ciclos/píxel y magnitud normalizada.

## 3. Ejercicio 3. Canny

### Escena sintética y referencia

- Imagen de 512×512, gris `uint8`, fondo 128. Primitivas rellenas, sin solaparse, dibujadas con `LINE_8`:

| Forma | Geometría | Intensidad | Contraste con el fondo |
|---|---|---|---|
| Rectángulo A | `(50,50)`–`(190,170)` | 210 | +82 |
| Rectángulo B | `(300,60)`–`(470,150)` | 50 | −78 |
| Rectángulo de bajo contraste C | `(220,240)`–`(290,300)` | 150 | +22 |
| Círculo D | centro `(130,350)`, radio 65 | 230 | +102 |
| Círculo E | centro `(380,340)`, radio 50 | 70 | −58 |
| Segmento F | `(40,470)`–`(240,430)`, grosor 3 | 240 | +112 |
| Segmento G | `(280,480)`–`(480,440)`, grosor 3 | 20 | −108 |

- La imagen limpia se pinta a partir de las máscaras de las primitivas prototipo.
- La referencia de bordes es la unión de los bordes internos de cada máscara: `borde = mask & ~cv2.erode(mask, np.ones((3,3), np.uint8))`. Es un borde de 1 píxel, generado por código desde las primitivas, no con Canny.
- El ruido se añade solo a la imagen, no a la referencia: gaussiano σ=15, recorte a `[0,255]`, `uint8`.
- Semilla principal: `SeedSequence([20260101, 3, 0])`. Semilla auxiliar del barrido de σ: `SeedSequence([20260102, 3, 0])`. Estabilidad: `SeedSequence([20260101, 3, 200+rep])`, `rep=0..9`.

### Suavizado previo

- Rejilla: `σ_suavizado ∈ {0,0; 0,5; 1,0; 1,5; 2,0}`. Para σ>0, `cv2.GaussianBlur` con `k=2*ceil(3σ)+1` y borde `REFLECT_101`; para σ=0, sin suavizado.
- Para cada σ se ejecutan las 24 combinaciones de umbrales con la semilla auxiliar y se calcula el mejor F1.
- Criterio: se elige el σ con mayor mejor F1. Desempate: menor σ. Se usa un solo σ para la rejilla principal.
- El barrido se guarda en `outputs/barrido_aux_sigma_canny.csv` con `sigma,mejor_f1,percentil_alto,fraccion_baja`.

### Gradiente y umbrales

- Gradiente: Sobel 3×3 en `float64`, `gx` y `gy`; magnitud `np.hypot(gx, gy)` sobre la imagen suavizada.
- Percentiles sobre las magnitudes **no nulas** (se excluyen los píxeles con magnitud exactamente 0).
- Percentil alto `p ∈ {70,75,80,85,90,95}`. `umbral_alto = int(round(percentil(magnitud, p)))`, mínimo 1.
- Fracción baja `f ∈ {0,3; 0,4; 0,5; 0,6}`. `umbral_bajo = max(1, int(umbral_alto * f))`, truncado a entero.
- Canny: `cv2.Canny(imagen_suavizada_uint8, umbral_bajo, umbral_alto, apertureSize=3, L2gradient=True)`.
- 24 combinaciones. Se registran las 24, no solo la mejor.

### Puntuación

- Tolerancia espacial: 2 px.
- `dist_ref = cv2.distanceTransform(1 - referencia, cv2.DIST_L2, 5)`: distancia de cada píxel al borde de referencia más cercano.
- `precision = (deteccion & (dist_ref <= 2)).sum() / deteccion.sum()`, o 0 si no hay detección.
- `dist_det = cv2.distanceTransform(1 - deteccion, cv2.DIST_L2, 5)`.
- `recall = (referencia & (dist_det <= 2)).sum() / referencia.sum()`.
- `f1 = 2*precision*recall / (precision + recall)`, o 0 si la suma es 0.
- `px_borde = int(deteccion.sum())`.
- CSV `outputs/barrido_canny.csv`: exactamente `percentil_alto,fraccion_baja,umbral_alto,umbral_bajo,precision,recall,f1,px_borde`; 24 filas; orden por percentil y fracción ascendentes.
- `assert`: 24 filas; las 24 parejas `(p,f)` presentes.

### Óptimo, regla de la unidad y pérdida

- Óptimo: fila con mayor F1. Desempate: mayor precisión; luego mayor percentil; luego menor fracción.
- Regla de la unidad: percentil 85 y fracción 0,5. Es una fila de la rejilla.
- Pérdida absoluta: `F1_opt - F1_unidad`. Pérdida relativa: `(F1_opt - F1_unidad) / F1_opt`.
- Se reportan también los umbrales absolutos de ambas reglas.

### Curva precisión–exhaustividad

- Curva principal: percentil alto variable con fracción baja fija en 0,5 (la de la unidad), para comparar directamente con la regla.
- Curva secundaria: percentil alto variable con la fracción óptima. Ambas salen de las 24 filas.
- Se explica la dirección de cada magnitud y el codo.

### Estabilidad

- 10 realizaciones de ruido con σ=15 y las semillas de estabilidad.
- Para cada realización se repiten el suavizado con el σ elegido y el cálculo de percentiles sobre esa realización; se aplican la regla óptima `(p_opt, f_opt)` y la regla de la unidad `(85, 0,5)`.
- Se reportan media y desviación típica de precisión, exhaustividad y F1 para cada regla.
- CSV `outputs/estabilidad_canny.csv` con `realizacion,regla,precision,recall,f1,umbral_alto,umbral_bajo,px_borde`.

### Transferencia a las imágenes reales

- Se aplica el mismo σ de suavizado a las tres imágenes de trabajo.
- Cuatro reglas por imagen:
  1. `optimo_sintetico`: umbrales absolutos de la fila óptima sintética.
  2. `unidad_sintetica`: umbrales absolutos de la regla de la unidad sintética.
  3. `percentil_optimo_local`: `p_opt` y `f_opt` calculados sobre las magnitudes no nulas de esa imagen.
  4. `percentil_unidad_local`: percentil 85 y fracción 0,5 sobre esa imagen.
- Se registran `umbral_alto`, `umbral_bajo`, `px_borde` y `frac_borde = px_borde / (alto*ancho)` en `outputs/transferencia_canny.csv` con `imagen,regla,umbral_alto,umbral_bajo,px_borde,frac_borde`.
- Se generan montajes de las cuatro reglas por imagen. La conclusión es descriptiva: no hay referencia en las imágenes reales. Se compara el número de bordes, la densidad y la presencia de grano o de bordes débiles.
- La pregunta 4 se responde con la comparación de los umbrales y de `frac_borde`, no con una puntuación inventada.

## 4. Ejercicio 4. Repetibilidad

### Imágenes y transformaciones

- Recorte cuadrado central de la imagen de trabajo: `lado = min(alto, ancho)`; `y0=(alto-lado)//2`, `x0=(ancho-lado)//2`. `IMG_01` e `IMG_02`: 341×341; `IMG_03`: 512×512.
- Centro de píxeles: `cx=(lado-1)/2`, `cy=(lado-1)/2`.
- Homografía de rotación: `H = T_inv @ R(θ) @ T`, con `T` traslación del centro al origen, `R(θ)` la rotación 2D en coordenadas homogéneas y `T_inv` la traslación inversa. El signo de la rotación se elige para que `θ=+90°` coincida con `np.rot90(imagen, k=1)`; el test lo comprueba.
- Homografía de escala: `H = T_inv @ S(s) @ T`, con `S = diag(s, s, 1)`. Para `s=1,0`, `H=I`.
- Iluminación: `H=I`; se aplica una LUT gamma `((i/255)**γ)*255`, redondeada y recortada a `uint8`, a la imagen transformada.
- Warp: `cv2.warpPerspective(imagen, H, (lado, lado), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)`.
- Control de medio píxel: la misma rotación de 90° con `cx=lado/2`, `cy=lado/2`. Se compara con el centro de píxeles.
- Valores:
  - Rotación: `0, 10, 20, 30, 45, 60, 90` grados.
  - Escala: `0,5; 0,7; 0,85; 1,0; 1,25; 1,5; 2,0`.
  - Iluminación: `γ ∈ {0,6; 0,8; 1,0; 1,3; 1,7}`.

### Detectores

- FAST: `cv2.FastFeatureDetector_create(threshold=25, nonmaxSuppression=True)`.
- ORB: `cv2.ORB_create(nfeatures=5000, scaleFactor=1.2, nlevels=8, edgeThreshold=31, firstLevel=0, WTA_K=2, scoreType=cv2.ORB_HARRIS_SCORE, patchSize=31, fastThreshold=20)`. `nfeatures` alto para que el límite no domine la comparación.
- SIFT: `cv2.SIFT_create()` con los valores por defecto.
- Se usa `.detect(imagen, None)`. Los detectores son deterministas; no se añade ruido en este ejercicio.

### Función de repetibilidad

- Se sigue la lógica del enunciado, generalizada para recibir el detector y una LUT opcional:
  - Detectar keypoints en la original y en la transformada.
  - Proyectar los de la original con `H`.
  - Conservar solo los proyectados dentro de `[0, ancho) × [0, alto)`.
  - Contar como acierto si hay un keypoint transformado a distancia euclídea ≤ `tol`.
  - `repetibilidad = aciertos / n_validos`; si no hay keypoints o no hay válidos, 0.
- `tol=3,0` en la rejilla principal.
- Se devuelven `repetibilidad`, `n_orig`, `n_trans`, `n_validos`.
- Línea base de azar por densidad: `azar = 1 - (1 - π*tol²/(lado²))**n_trans`, acotada a `[0,1]`; si `n_trans=0`, 0. Se calcula por fila y se representa como línea discontinua. Es una aproximación de puntos uniformes; se declara su límite.

### Rejilla principal

- 3 imágenes × 3 detectores × 19 transformaciones = 171 filas.
- Orden: imagen, detector (`FAST`, `ORB`, `SIFT`), transformación (`rotacion`, `escala`, `iluminacion`), valor ascendente.
- CSV `outputs/repetibilidad.csv` con `imagen,detector,transformacion,valor,repetibilidad,n_orig,n_trans,n_validos,tol,azar`.
- `assert`: 171 filas; 57 por imagen; 19 por detector; todas las transformaciones y valores presentes.
- Figuras: repetibilidad frente a rotación, escala e iluminación. Tres paneles (uno por imagen) o una figura por transformación con las tres imágenes; en la escala se comparan FAST, ORB y SIFT. Eje y de 0 a 1, compartido, línea de azar discontinua, leyenda y unidades.

### Tests obligatorios

- Rotación de 90°: la imagen transformada con la homografía de centro de píxeles debe coincidir con `np.rot90(imagen, k=1)`. Se acepta una diferencia máxima de 1 nivel por redondeo del warp; si es mayor, el test falla y se corrige la homografía. La repetibilidad con la homografía y con `np.rot90` debe coincidir.
- Identidad: escala 1,0, gamma 1,0 y rotación 0° deben dar imagen idéntica y repetibilidad 1,0.
- Control de medio píxel: a 90°, la repetibilidad con `cx=lado/2` debe ser distinta de la del centro de píxeles; se reporta la diferencia.
- Los tests se ejecutan con `pytest` y se guardan en `_herramientas/tests/`.

### Sensibilidad (auxiliar)

- Umbral de FAST: `{10,25,50}` en el barrido de escala, tres imágenes. El principal es 25.
- Pirámide de ORB: `nlevels ∈ {1,4,8}` en el barrido de escala, tres imágenes. El principal es 8.
- Tolerancia: `tol ∈ {1,2,3,5}` en los barridos de rotación y escala con FAST, tres imágenes. La principal es 3,0.
- CSV `outputs/repetibilidad_sensibilidad.csv` con `imagen,detector,barrido,parametro,valor,repetibilidad,n_orig,n_trans,n_validos,tol,azar`.
- Control de medio píxel en `outputs/repetibilidad_control_medio_pixel.csv` con `imagen,detector,transformacion,valor,centro,repetibilidad,n_orig,n_trans,n_validos,tol`.
- Las curvas de sensibilidad se presentan como evidencia, no sustituyen a la rejilla principal.

## 5. Selección de parámetros y registro

- Ningún parámetro se elige mirando el resultado final. Los barridos auxiliares usan la semilla `20260102`; la rejilla principal usa `20260101`.
- Los parámetros elegidos se escriben en `outputs/registro_parametros.csv` con `parametro,valor,criterio,barrido`:
  - tamaño de trabajo, borde, semillas, configuración PSNR/SSIM;
  - `k` y `alpha` de la mediana truncada;
  - `d`, `sigmaColor` y `sigmaSpace` de bilateral A y B;
  - `σ_suavizado` de Canny;
  - `p_opt`, `f_opt`, `p_unidad=85`, `f_unidad=0.5` de Canny;
  - parámetros de FAST, ORB y SIFT;
  - `tol` de repetibilidad y fórmula de la línea base.
- Los desempates están declarados en cada sección.
- Si un barrido no produce ningún valor válido (por ejemplo, ningún ε da cero rebotes), se amplía el rango, se declara y se vuelve a sellar antes de continuar.

## 6. Qué no se hace

- No se elige ningún parámetro a ojo.
- No se editan los CSV a mano.
- No se instalan paquetes dentro del notebook.
- No se usa `IMG_03` como *ground truth*.
- No se cambian las imágenes de partida.
- No se repite una celda con otra semilla para obtener una cifra más favorable.
- No se ocultan los resultados negativos. Si una afirmación de la unidad no se confirma, se dice con la cifra.
- Si se detecta un error de implementación después de medir, se corrige, se anota en la bitácora, se vuelve a ejecutar y se vuelve a sellar; no se parchea el CSV.

## 7. Sello

Este documento y `_trabajo/predicciones.md` se sellan con SHA-256 y hora en `_trabajo/orden_declaraciones.log` antes de generar cualquier CSV de resultados en `outputs/`. La carpeta `outputs/` está vacía en el momento del sello. El diagnóstico de las imágenes se guardó en `_trabajo/` y no cuenta como resultado de los ejercicios.
