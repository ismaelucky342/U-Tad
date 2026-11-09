# Bitácora de trabajo

Documento interno. No se entrega.

## 8 de noviembre de 2026

### Punto de partida

- El directorio `AEC2` estaba vacío. El enunciado no estaba allí; lo encontré en `~/Descargas/UtadOnline_VICO_Practica_U2.pdf` (15 páginas, autora Isabel X. de San Sebastián Jiménez). Coincide con el megaprompt. Se copia a `_trabajo/enunciado/`.
- El material de la unidad está en `Unit_2/unit_2.md` (115 KB), una carpeta por encima de `AEC2`. Se copia a `_trabajo/enunciado/` para trabajar con él.
- La práctica de U1 del mismo autor está en `Unit_1/AEC1/U1_Practica_Hernandez_Ismael/`. Se usa como referencia de estilo, estructura de la memoria y generación del PDF con WeasyPrint.

### Entorno

- Python del sistema: 3.14.9. No hay `cv2` instalado.
- `uv` disponible. U1 se ejecutó con Python 3.13.15. Se usará esa versión para evitar problemas de ruedas.
- Pango, cairo y fuentes disponibles: WeasyPrint puede generar el PDF.
- No hay LaTeX, pandoc ni wkhtmltopdf. Hay LibreOffice. No hacen falta.
- 12 núcleos, 90 GB libres.
- `pdfinfo`, `pdftotext` y `pdftoppm` disponibles para extraer texto y rasterizar páginas.

### Decisiones

1. **Filtros.** El enunciado dice «diez» y enumera nueve. Se añade `media 5×5` como décimo filtro. Es el homólogo de la mediana 5×5 y permite comparar a igual ventana en la pregunta 2.
2. **Perfiles.** El enunciado dice «cinco casos» y enumera siete. Se calculan los siete.
3. **Mediana truncada.** La lección 14 la define como ordenar la ventana, recortar un porcentaje α por cada lado y tomar la mediana del resto. Con recorte simétrico el resultado es idénticamente la mediana: en 3×3, quitar 1, 2 o 3 valores por lado deja 7, 5 o 3, y la mediana de todos ellos sigue siendo el 5.º de los 9; en 5×5 ocurre lo mismo. El ejemplo de la unidad con α=10 % y α=30 % solo tiene sentido si se promedia lo que queda. Decisión: la rejilla usa la media recortada, con ventana y α elegidos por barrido con semilla auxiliar; se conserva la versión literal como control que demuestra la equivalencia. Se documenta en la memoria. El autor aprobó esta interpretación.
4. **Sal y pimienta.** Las coordenadas se eligen con reemplazo, como en el enunciado. Se medirá la fracción realmente alterada y se guardará en `outputs/ruido_fraccion_real.csv`.
5. **RNG.** El RNG global del enunciado depende del orden de las celdas. Se sustituye por un generador por celda con `SeedSequence([20260101, idx_imagen, idx_condicion])`. Las funciones de ruido reciben el generador. Test: el hash de cada imagen ruidosa es idéntico entre ejecuciones.
6. **CSV adicionales.** La estructura obligatoria lista cuatro CSV. Se mantienen esos cuatro con nombres y columnas exactas y se añaden CSV auxiliares de evidencia. No sustituyen a los obligatorios.
7. **Canny.** El enunciado no fija el operador. Se usa Sobel 3×3 y `L2gradient=True`; los percentiles se calculan sobre la imagen ya suavizada, para que umbral y magnitud estén en la misma escala.
8. **Rotación.** Centro de píxeles `((w-1)/2, (h-1)/2)`, no `(w/2, h/2)`. Se añade el control con medio píxel de desfase.
9. **Tamaño de trabajo.** Lado mayor a 512 px con `INTER_AREA`. Los originales de `data/` no se tocan. El autor lo aprobó.
10. **Nombre de la entrega.** `U2_Practica_Hernandez_Ismael.zip`. El autor lo confirmó.
11. **Imágenes.** El autor prefiere que las busque con licencia. Se propondrán candidatas de Wikimedia Commons con URL, autor y licencia antes de descargarlas.

### Problemas y cómo se resolvieron

- **El enunciado no estaba en el directorio de trabajo.** Estaba en `~/Descargas`. Se copió a `_trabajo/enunciado/`.
- **La mediana truncada literal no trunca.** Se detectó al comparar la definición con la propiedad de la mediana. Se resolvió con media recortada y control literal, aprobado por el autor.
- **El enunciado dice cinco perfiles y enumera siete.** Se calculan los siete y se anota en la memoria.
- **El enunciado dice diez filtros y enumera nueve.** Se añade media 5×5 y se marca.

### Fase 0 cerrada

- Venv creado en `_trabajo/venv` con Python 3.13.15. Versiones instaladas y congeladas en `_trabajo/entorno.txt`.
- `verificar_entorno.py` pasa: OpenCV 5.0.0, SIFT, ORB y FAST disponibles, PSNR infinito en la identidad y SSIM 1,0.
- `pytest` pasa el test de humo.
- Herramientas base creadas: `verificar_entorno.py`, `hoja_contacto.py`, `verificar_cifras.py` y el esqueleto de tests.
- Candidatas de imagen descargadas como miniatura para revisión. Se propone follaje (textura fina), manzana sobre fondo blanco (regiones uniformes) y la muestra de ruido a ISO 6400 (ruido real). Las tres son CC BY-SA 4.0 y se citarán con autor y enlace.

### Pendiente

- Obtener el visto bueno a las tres imágenes y copiar los originales a `data/`.
- Calcular el diagnóstico de las originales y los hashes.
- Escribir predicciones y criterios antes de medir.

### Fase 1 cerrada

- El autor dio el visto bueno a las tres candidatas. Se descargaron los originales a `U2_Practica_Hernandez_Ismael/data/` con los nombres `IMG_01.jpg` (follaje), `IMG_02.jpg` (manzana) e `IMG_03.jpg` (ruido ISO 6400). No se han modificado.
- SHA-256:
  - `IMG_01.jpg`: `348fd88c0e99ab0ee66a5fe01c3d662646354712a4b353dc2c06a24cbc70ba4b`
  - `IMG_02.jpg`: `f739e66c8ab29da3848c5bcf1218fd42ffe13ab0cb5eebdb4cbdb338ad54a00b`
  - `IMG_03.jpg`: `050b7bcabe09732e7aa3141c863d04f8692002cf36977da435c6e39456a6f0ff`
- Fuente, autor y licencia en `_trabajo/manifest_imagenes.json`. Las tres son CC BY-SA 4.0 y se citan con enlace a la ficha de Wikimedia Commons.
- Versión de trabajo: gris `uint8`, lado mayor 512 con `INTER_AREA`. Los originales quedan intactos. Las versiones de trabajo están en `_trabajo/versiones_trabajo/`.
- Diagnóstico en `_trabajo/diagnostico_originales.csv`. Se movió allí desde `outputs/` para que `outputs/` esté vacío antes del sello de la Fase 2; el notebook final lo regenerará en `outputs/` como evidencia adicional.

| Imagen | Rol | Original | Trabajo | Gradiente medio (trabajo) | Densidad de gradiente (trabajo) | σ Laplaciano MAD (trabajo) | Entropía (trabajo) | Píxeles saturados (trabajo) |
|---|---|---|---|---|---|---|---|---|
| `IMG_01.jpg` | textura fina | 6000×4000 | 512×341 | 63,03 | 80,13 % | 0,741 | 7,141 | 0,00 % |
| `IMG_02.jpg` | regiones uniformes | 5184×3456 | 512×341 | 6,53 | 8,68 % | 0,000 | 3,465 | 35,07 % |
| `IMG_03.jpg` | ruido real | 3440×3440 | 512×512 | 18,71 | 73,64 % | 3,459 | 6,782 | 0,00 % |

- **Validación de roles.** `IMG_01` tiene la mayor densidad de gradiente y una textura fina; su σ de ruido es bajo (0,741), así que sirve como imagen limpia de textura. `IMG_02` tiene regiones amplias y uniformes, una densidad de gradiente baja (8,68 %) y bordes fuertes (percentil 95 de 34,41); su σ de ruido es 0,000 porque el fondo es plano. `IMG_03` tiene un σ de ruido 4,7 veces mayor que el follaje y una densidad de gradiente del 73,64 % dominada por el grano; es la imagen de ruido real.
- **Limitación de `IMG_03`.** No tiene referencia limpia. No se usará como *ground truth* en PSNR/SSIM. En la rejilla del Ejercicio 1 sus columnas `psnr` y `ssim` quedarán vacías y se analizará aparte con métricas sin referencia (σ del Laplaciano antes/después, cambio medio absoluto y valoración visual). El resto de la rejilla se apoya en `IMG_01` e `IMG_02`.
- **Matiz de `IMG_02`.** El 35,07 % de los píxeles de trabajo están a 255 (fondo blanco saturado). Al inyectar ruido gaussiano y recortar a 0–255, el ruido del fondo se vuelve unilateral y su varianza efectiva baja; las cifras de PSNR/SSIM de esta imagen estarán infladas en esa zona. Se documenta en la memoria y, si las conclusiones dependen de ello, se repetirá el análisis sobre la máscara no saturada (limpia < 250) como control.
- **Umbral de densidad de gradiente.** El 10 % usado en el diagnóstico es una convención del diagnóstico, no un parámetro del banco de pruebas. Queda declarado en el manifiesto y no se usa para elegir filtros.
- **Siguiente.** Escribir predicciones y criterios y sellarlos antes de medir.

### Fase 2 cerrada

- `_trabajo/predicciones.md` escrito antes de medir. Contiene rangos y ordenaciones para los cuatro ejercicios, incluida la limitación de `IMG_03` y el matiz de saturación de `IMG_02`.
- `_trabajo/criterios_declarados.md` escrito antes de medir. Fija ruido, filtros, barridos de truncada y bilateral, perfil radial, escena sintética, rejilla de Canny, homografías, detectores, tolerancias, línea base de azar y desempates.
- Sello en `_trabajo/orden_declaraciones.log`:
  - Fecha: `2026-11-08T18:26:11+01:00`.
  - `predicciones.md`: `e5e83615b5c59e98c37a4424651908022673b026708a48cc472214853f399b9f`.
  - `criterios_declarados.md`: `2339ea0b8b8f552dc77a6fe5c7b52419062e475085b3f692ed16524addb33da3`.
  - `manifest_imagenes.json`: `f44ad19eed844be4108fb7a587da4b450d26d333527680cf56529d48aa8480af`.
- `outputs/` estaba vacío en el sello. El diagnóstico de imágenes se guardó en `_trabajo/` y no cuenta como resultado de los ejercicios.
- **Siguiente.** Fase 3: núcleo reutilizable, tests y barridos auxiliares.

### Fase 3 cerrada

- Núcleo definitivo en `U2_Practica_Hernandez_Ismael/codigo/banco_pruebas.py`. Se eliminó la copia redundante `_trabajo/nucleo.py` para que solo haya una fuente de verdad.
- Tests: `_trabajo/venv/bin/python -m pytest _herramientas/tests -q` → **11 passed**. Cubren hashes, medianas propia/híbrida/truncada, control literal, rotación 90°, identidad, gamma, PSNR/SSIM, ruido determinista, perfiles, bordes y escena.
- Barridos auxiliares con semilla `20260102` en `outputs/`:
  - `barrido_aux_truncada.csv`: elegido `k=7`, `alpha=0,2` (`m=9` por cola). SSIM medio 0,8244; PSNR medio 30,90.
  - `barrido_aux_bilateral.csv`: A por SSIM `d=9`, `sc=75`, `ss=5` (SSIM 0,8603; PSNR 30,88); B por PSNR distinto `d=7`, `sc=75`, `ss=5` (PSNR 31,02; SSIM 0,8513).
  - `barrido_aux_epsilon.csv`: `epsilon=2,35983e-4`, el menor que anula los rebotes de los tres gaussianos.
  - `barrido_aux_sigma_canny.csv`: `sigma=1,5`; mejor F1 0,9985 con percentil 95 y fracción 0,5 (alto 48, bajo 24; P 0,9970, R 1,0000, 2997 px de borde).
- `outputs/registro_parametros.csv` escrito con los parámetros de E1 y el σ de Canny; el notebook final añadirá los de E3/E4. El registro es parcial, no se presenta como definitivo.

### Fase 4 en curso

- `outputs/resultados_denoising.csv`: **180 filas**, columnas exactas, 60 por imagen y 10 por condición; `assert` superado. En `IMG_03` las columnas `psnr` y `ssim` están vacías.
- Auxiliares:
  - `outputs/ruido_fraccion_real.csv`: 18 filas; fracción realmente alterada, σ empírico y fracción recortada.
  - `outputs/analisis_ruido_real.csv`: 60 filas de `IMG_03`; σ del Laplaciano de entrada/salida con el mismo kernel y estimador del diagnóstico, reducción relativa `(entrada-salida)/entrada`, MAD de cambio y brillo medio de salida.
- El ruido se generó **una vez por celda** y los diez filtros vieron la misma imagen ruidosa. Tiempos: mediana de 5 repeticiones tras calentamiento, solo la llamada al filtro.
- Efecto de la saturación de `IMG_02`: con σ nominal 10/20/40 el σ empírico medido es 7,09/13,43/26,25 y la fracción recortada 39,0/42,4/44,1 %. La sal y pimienta altera de verdad 4,0/7,9/21,3 % porque parte de los impactos cae sobre fondo ya blanco. Se documenta como limitación, no se corrige en la rejilla principal.
- Primeros resultados:
  - PSNR: mediana gana 9 de 12 celdas con referencia; media 2; gaussiano 1.
  - SSIM: mediana gana 6 de 12; gaussiano 4; bilateral A 1; bilateral B 1.
  - Sal y pimienta: mediana 3 o 5 gana PSNR y SSIM en las seis celdas; el bilateral no elimina impulsos (delta SSIM muy negativo).
  - Gaussianos: la mediana truncada tiene el mejor SSIM medio (0,8569) pero menor PSNR medio (29,77); la mediana tiene el mejor PSNR medio (30,51) y peor SSIM (0,7592). El gaussiano σ=2 queda en 0,8451 de SSIM medio.
  - Bilateral: en `IMG_01` σ=10/20 la B supera al gaussiano σ=2 en SSIM y PSNR, pero tarda 8–19× más; en σ=40 pierde. En `IMG_02` la A gana SSIM en σ=10, pero la diferencia es pequeña y el coste 60×. No se elige como filtro global.
- Figuras en `outputs/figuras/`:
  - `e1_heatmap_psnr.png`, `e1_heatmap_ssim.png` (IMG_01 e IMG_02, escala común).
  - `e1_heatmap_rugosidad_IMG_03.png` (sustituto sin referencia de IMG_03; no es PSNR/SSIM).
  - `e1_curvas_psnr.png`, `e1_curvas_ssim.png`, `e1_curvas_rugosidad_IMG_03.png`.
  - `e1_recortes_IMG_01.png`, `e1_recortes_IMG_03.png`.
- Caso visual: en `IMG_01` sal 10 %, la mediana 3 (PSNR 34,26; SSIM 0,9679) es también la mejor visual; la truncada 7 (27,14; 0,8247) alisa más pero pierde detalle, así que no hay contradicción métrica/visual. En `IMG_03` no hay PSNR/SSIM: la mediana 3 deja grano, el bilateral A conserva el borde del asa, y el gaussiano σ=2 y la truncada 7 alisan en exceso.
- Pendiente de F4: pasar las tablas de ganadores, mediana/media y bilateral/gaussiano a la memoria y cerrar la redacción del ejercicio. Las funciones `tabla_ganadores_e1`, `tabla_medianas_vs_medias_e1` y `tabla_bilateral_e1` ya están en el código.

### Fase 5 cerrada

- `outputs/perfiles_frecuencia.csv`: **42 filas** (3 imágenes × 7 casos × 2 fuentes), columnas `imagen,caso,parametros,fuente,f_corte,rebotes,ssim_vs_original`; `assert` superado. La fuente `respuesta_filtro` del caso `original` tiene `f_corte` vacío y `rebotes=0`.
- `outputs/parejas_caja_gaussiano.csv`: 9 filas, una por imagen y caja. Se generó además `outputs/parejas_caja_gaussiano_respuesta.csv`, con las mismas columnas, para el emparejamiento por corte de la respuesta.
- El `epsilon` usado es el del registro, `2,35983e-4`. Las respuestas gaussianas dan **0 rebotes**; las cajas dan 17/25/23 rebotes en IMG_01 y 25/44/35 en IMG_03. La respuesta de la caja tiene lóbulos; la gaussiana no.
- **Hallazgo importante:** el corte de la imagen filtrada se degenera. El perfil radial de la imagen cae por debajo de 0,5 ya en el primer anillo (r≈0,83) por el dominio de las bajas frecuencias: `f_corte` = 0,002426 (IMG_01), 0,002139 (IMG_02), 0,001714 (IMG_03) para **todos** los casos. El emparejamiento literal por ese corte elige siempre `gaussiano_0.8` por el desempate de menor σ. No se oculta: se guarda en `parejas_caja_gaussiano.csv`.
- El corte de la **respuesta** sí distingue los filtros: caja 3/5/9 = 0,2130/0,1236/0,0674; gaussianos 0,8/1,6/3,0 = 0,2331/0,1160/0,0614. El emparejamiento por respuesta es caja 3↔gauss 0,8; caja 5↔gauss 1,6; caja 9↔gauss 3,0. Se usa en la figura y en la comparación razonada; el CSV literal queda como comprobación.
- SSIM caja frente a gaussiano emparejado por respuesta:
  - IMG_01: −0,0120 (caja 3 vs 0,8), −0,0010 (caja 5 vs 1,6), −0,0134 (caja 9 vs 3,0).
  - IMG_02: −0,0035, −0,0017, −0,0014.
  - IMG_03: −0,0457, −0,0097, −0,0040.
  La gaussiana gana por poco en casi todos los pares; la caja 5 queda prácticamente empatada y la caja 9 se acerca en IMG_02. La caja 3 pierde más en IMG_03.
- Rebotes del perfil de la imagen: 7/6/5/3 en IMG_01, 2 en IMG_02 y 0 en IMG_03; no son los lóbulos del filtro, sino el contenido de la imagen. La respuesta del filtro es la medida limpia de lóbulos; la memoria lo separa.
- Figuras en `outputs/figuras/`:
  - `e2_perfiles_imagen.png`: 3 paneles, 7 casos, línea 0,5, marcas de corte y escala logarítmica común.
  - `e2_respuesta_filtros.png`: panel completo y zoom de lóbulos.
  - `e2_parejas_caja_gaussiano.png`: parejas por respuesta, con ΔSSIM.
- Comprobación en IMG_02 e IMG_03: el emparejamiento por respuesta no cambia; las diferencias de SSIM se mantienen en signo y orden. El caso más favorable a la caja es el par 5/1,6; el más desfavorable, la caja 3 en IMG_03.

### Fase 6 cerrada

- Escena sintética y referencia desde las primitivas, sin Canny en la referencia. Ruido gaussiano σ=15 con la semilla principal `[20260101, 3, 0]`.
- σ de suavizado elegido en el barrido auxiliar: **1,5**, el de mayor mejor F1 (0,9985), dentro de la predicción 1,0–1,5.
- `outputs/barrido_canny.csv`: **24 filas**, columnas exactas, orden por percentil y fracción ascendentes. Las 24 parejas están presentes.
- Resultado principal:
  - Óptimo de la rejilla: percentil 95, fracción 0,6 → alto 48, bajo 28; P 0,99966, R 0,996875, F1 0,998268, 2978 px.
  - Regla de la unidad: percentil 85, fracción 0,5 → alto 20, bajo 10; P 0,05405, R 1,0000, F1 0,10255, 55 561 px.
  - Pérdida absoluta 0,8957; relativa 0,8973. La regla de la unidad **falla** en esta escena: el umbral alto 20 deja pasar el grano. La predicción decía que si perdía más de 0,10 sería mala; se cumple con creces.
  - El óptimo está en el borde superior de la rejilla declarada (p95, f0,6). Con p95/f0,5 el F1 es 0,99793; con p95/f0,3, 0,98965. La diferencia entre las filas p95 es pequeña; lo que domina es subir el percentil a 95. No se amplía la rejilla porque estaba sellada; se declara el borde.
- Estabilidad (10 realizaciones):
  - Óptimo: P 0,997798 ± 0,001901; R 0,998250 ± 0,003389; F1 0,998020 ± 0,001874; 2992,7 ± 15,9 px.
  - Unidad: P 0,053284 ± 0,000414; R 0,999844 ± 0,000266; F1 0,101176 ± 0,000746; 56 423 ± 481 px.
  - La desviación de F1 es menor que 0,02 en ambas, como se predijo; pero la unidad es estable en un valor malo.
- Curva precisión–exhaustividad: la principal (f=0,5) y la secundaria (f=0,6) muestran un salto brusco al pasar de p90 a p95; el codo está en p95. La precisión sube de 0,079 a 0,999 y la exhaustividad apenas baja de 1,0 a 0,9969. La fracción baja tiene poco efecto cuando p95 ya es selectivo.
- Transferencia (`outputs/transferencia_canny.csv`), fracción de píxeles de borde:
  - IMG_01: óptimo sintético 48/28 → 12,20 %; unidad sintética 20/10 → 15,06 %; percentil óptimo local 125/75 → 5,05 %; percentil unidad local 84/42 → 9,56 %.
  - IMG_02: 0,81 %; 1,34 %; 0,44 %; 0,82 %.
  - IMG_03: 0,46 %; 0,83 %; 0,81 %; 11,29 %.
  - Los umbrales absolutos no transfieren: en IMG_01 sobre-detectan textura; en IMG_02 detectan de más respecto al percentil local; en IMG_03 el óptimo absoluto se queda corto y la unidad absoluta sobre-detecta. El percentil local se adapta mejor; el peor caso es la unidad local en IMG_03 (8/4), que convierte el grano en bordes. La predicción de que el óptimo absoluto daría 2–10× la unidad no se cumple en dirección: la unidad absoluta tiene umbrales más bajos y da más bordes.
- Figuras en `outputs/figuras/`:
  - `e3_escena.png` (limpia, referencia en rojo, ruidosa, suavizada).
  - `e3_barrido_f1.png` (24 celdas, óptimo y unidad marcados).
  - `e3_curvas_pr.png` (principal y secundaria).
  - `e3_estabilidad.png` (barras con desviación).
  - `e3_transferencia_IMG_01.png`, `..._IMG_02.png`, `..._IMG_03.png` (cuatro reglas por imagen).
- El registro incluye `canny_p_optimo=95`, `canny_f_optimo=0,6`, umbrales 48/28 y 20/10 y las pérdidas.

### Fase 7 cerrada

- Homografías con centro de píxeles. Tests: **12 passed**; el warp de 90° coincide con `np.rot90`; identidad (escala 1,0 y gamma 1,0) da repetibilidad 1,0; el control de medio píxel cambia la imagen y se reporta. Añadido test de que la repetibilidad a 90° con la homografía coincide con la de `np.rot90`.
- `outputs/repetibilidad.csv`: **171 filas** (3 imágenes × 3 detectores × 19 transformaciones), 57 por imagen, 19 por detector; columnas exactas. `outputs/repetibilidad_sensibilidad.csv`: 294 filas; se añadió `valor_transformacion` al final para poder dibujar las curvas (las columnas exigidas siguen presentes). `outputs/repetibilidad_control_medio_pixel.csv`: 18 filas.
- Línea base de azar por densidad, calculada por fila; en IMG_01/ORB llega a 0,634, así que las tasas altas de ORB no se pueden leer sin ella. En IMG_03 el azar es casi 0, pero solo hay 4 keypoints FAST, 35 ORB y 29 SIFT: las curvas son gruesas y no permiten conclusiones finas.
- Pregunta 1 (FAST y escala): **se refuta la invariancia**. FAST 0,5/1,0/2,0 → IMG_01 0,925/1,000/0,340; IMG_02 0,642/1,000/0,481; IMG_03 0,750/1,000/0,000. La caída al ampliar es grande; a 0,5 aguanta mejor de lo que predecía (0,3–0,6), sobre todo en IMG_01; la predicción falló en ese punto. La escala 2,0 de IMG_03 no tiene keypoints transformados (0 válidos), no es una tasa 0 comparable.
- Pregunta 2 (rotación): **no es plana**. FAST 0/45/90° → IMG_01 1,000/0,808/1,000; IMG_02 1,000/0,415/1,000; IMG_03 1,000/0,500/1,000. ORB → 1,000/0,906/0,998; 1,000/0,728/0,974; 1,000/0,943/1,000. SIFT → 1,000/0,830/0,943; 1,000/0,800/0,933; 1,000/0,429/0,931. Hay valle en ángulos intermedios y pico en 90°: el anillo de 16 píxeles de FAST tiene simetría de 90° y la rejilla vuelve a alinearse; a 45° la interpolación y el anillo no caen sobre los mismos píxeles. El pico no es perfecto en SIFT/ORB por la detección en la imagen girada.
- Pregunta 3 (multiescala): escala 0,5/1,0/2,0 → ORB IMG_01 0,994/1,000/0,418; IMG_02 0,866/1,000/0,505; IMG_03 0,971/1,000/0,000 (sin keypoints a 2,0). SIFT → 0,595/1,000/0,748; 0,533/1,000/0,844; 0,310/1,000/1,000 (a 2,0 solo 1 keypoint válido; no es evidencia de invariancia). FAST → 0,925/1,000/0,340; 0,642/1,000/0,481; 0,750/1,000/0,000. ORB gana a FAST al reducir; SIFT conserva mejor la ampliación en IMG_01/02; la diferencia es la demostración empírica del espacio de escalas. En IMG_03 las muestras son demasiado pequeñas.
- Sensibilidad FAST (umbral 10/25/50, escala): IMG_01 0,831/0,743/0,607; IMG_02 0,745/0,565/0,633; IMG_03 0,236/0,476/0,286. El 25 principal no es el mejor en dos imágenes; no se cambia porque estaba declarado. Umbral 10 sube en IMG_01/02; 50 baja.
- Sensibilidad ORB (nlevels 1/4/8, escala): IMG_01 0,717/0,802/0,819; IMG_02 0,576/0,711/0,748; IMG_03 0,482/0,558/0,555. La pirámide ayuda; 4 y 8 casi empatan; 1 es peor.
- Sensibilidad tol (1/2/3/5): rotación IMG_01 0,719/0,819/0,871/0,939; IMG_02 0,531/0,566/0,596/0,625; IMG_03 0,429/0,536/0,571/0,607. Escala: 0,466/0,653/0,743/0,828; 0,432/0,530/0,565/0,638; 0,405/0,476/0,476/0,476. Es monótona; tol=5 infla la tasa. Se mantiene 3,0.
- Control de medio píxel (90°): ORB IMG_01 0,998/0,981; IMG_02 0,974/0,955; IMG_03 1,000/0,971. SIFT 0,943/0,941; 0,933/0,911; 0,931/0,931. FAST 1,000/1,000 en las tres por la tolerancia y el número de keypoints. El warp de medio píxel sí es distinto del de `np.rot90`; el test lo comprueba.
- Figuras: `e4_rotacion.png`, `e4_escala.png`, `e4_iluminacion.png` (tres paneles, azar discontinuo), `e4_sens_fast.png`, `e4_sens_orb.png`, `e4_sens_tol.png`, `e4_medio_pixel.png`.
- Registro actualizado con `fast_threshold`, `orb_nfeatures`, `orb_nlevels`, `sift_configuracion`, `tol_repetibilidad` y `azar_formula`.


### Fase 8 cerrada

- `memoria/hallazgos.md` contiene exactamente cinco afirmaciones, cada una con `Fuente:` y `Límite:`. La introducción está en primera persona y las fuentes usan índices pandas.
- `verificar_cifras.py --estricto` lee los 20 CSV y no deja ninguna cifra sin respaldo.

### Fase 9 cerrada

- `memoria/informe.pdf`: 26 páginas, WeasyPrint 70.0. Reescrito en primera persona y con tabla de créditos de imágenes al estilo de la AEC1 de la Unidad 1. Se corrigió la tabla A1 para que no parta filas, se unificaron las fuentes de los hallazgos a índices pandas, se ajustó el pie de la figura 12 y se añadió el cierre de la entrega.
- El PDF está en primera persona en el texto narrativo; la tabla de créditos y la nota final citan la AEC1 de la Unidad 1 como referencia de tono y formato. Las tablas y los pies conservan el estilo técnico.
- Revisión visual: sin filas partidas ni figuras cortadas; la última página incluye A.2–A.4 y el cierre. Queda la confirmación final del autor al abrir el PDF.

### Fase 10 cerrada

- `codigo/banco_pruebas.ipynb`: 16 celdas (7 markdown y 9 de código), ejecutado con el kernel limpio; salidas `E1 (180, 8)`, `E2 (42, 7)`, `E3 (24, 8)`, estabilidad `(20, 8)`, transferencia `(12, 6)` y `E4 (171, 10)`.
- `codigo/banco_pruebas.py` incluye `ejecutar_todo()` y funciona tanto desde la raíz de la entrega como desde `codigo/`.
- Prueba en limpio en `/tmp/opencode/aec2_nb`: todos los CSV comparables coinciden salvo `tiempo_ms`; los CSV auxiliares de barridos se conservan como entradas declaradas.
- `_trabajo/venv/bin/python -m pytest _herramientas/tests -q`: **12 passed**.
- `U2_Practica_Hernandez_Ismael.zip`: 53 archivos, 35 MB, sin `__pycache__`; `unzip -t` sin errores. Estructura `memoria/`, `codigo/`, `data/` y `outputs/`.


### Documentación en Markdown

- `memoria/informe.md` es la fuente editable y en primera persona; `_herramientas/generar_md.py` la reconstruye desde el HTML. No se ha vuelto a generar el PDF por indicación del autor.
- Se corrigieron en el MD las citas a `_herramientas/tests` y a los comandos internos: ahora los tests y el verificador se describen como internos y A.3 solo usa `python codigo/banco_pruebas.py`.
- `_trabajo/auditoria_rubrica_u2.md` cruza la rúbrica U2 con la entrega y revisa los problemas heredados de la AEC1.
- El PDF existente conserva la redacción en primera persona y las figuras, pero no los últimos pies de figura del MD. Si se entrega PDF, hay que regenerarlo y comprobar las imágenes.
