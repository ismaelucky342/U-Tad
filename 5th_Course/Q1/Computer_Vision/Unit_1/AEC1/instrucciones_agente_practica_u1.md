# Instrucciones para el agente: Práctica U1 «Del diagnóstico numérico al contrato de preprocesado»

Vas a realizar de principio a fin una práctica universitaria individual de visión por computador (U-tad, Unidad 1). El objetivo es la máxima nota según la rúbrica. Lee todo este documento antes de escribir una sola línea de código.

---

## 0. Principios que mandan sobre todo lo demás

1. **Todo número que aparezca en el informe o en el contrato sale de tu propio código y está en un CSV entregado.** Nunca escribas una cifra "de memoria" ni la redondees a mano. Genera los textos y los pies de figura con f-strings a partir de los DataFrames.
2. **Nunca inventes resultados, dificultades ni experiencias.** Si algo sale mal o la mejora es nula, se dice tal cual. La práctica puntúa igual un resultado negativo bien argumentado que uno espectacular. Lo único que no puntúa es afirmar una mejora que las cifras no respaldan.
3. **Reproducibilidad total**: semilla fijada al principio, rutas relativas, `requirements.txt` con versiones exactas, ningún `pip install` dentro del notebook, ejecución limpia de principio a fin.
4. **Todo el realce se hace sobre luminancia** (canal Y de YCrCb), nunca por canal RGB, salvo la única figura comparativa que pide el enunciado.
5. **El criterio de selección se redacta y se guarda ANTES de calcular el barrido** (ver Ejercicio 2).

---

## 1. Registro y estilo de la documentación (importante)

Todo el texto que escribas (informe, contrato, comentarios del código, celdas markdown, pies de figura, README si lo hubiera) debe leerse como escrito por un estudiante de grado competente, en español de España, y no como texto generado. Reglas concretas:

**Voz y tono**
- Primera persona del singular o plural de modestia, según toque: «he medido», «vemos que», «me ha sorprendido que». Registro académico sobrio pero natural, sin pomposidad.
- Frases de longitud variada. Alterna frases cortas y directas con alguna más larga. Párrafos de distinta extensión; no todos con la misma estructura.
- Opiniones razonadas y matices concretos («esto lo atribuyo a…», «no puedo descartar que…») en lugar de generalidades.
- Decimales con coma en el texto en prosa (0,55; 18,4 %) y con punto en los CSV (como pide el enunciado).

**Expresiones y patrones que debes evitar**
- Muletillas típicas de texto automático: «es importante destacar», «cabe señalar», «en el panorama actual», «en conclusión», «en resumen», «sin lugar a dudas», «fascinante», «crucial», «robusto» como adjetivo comodín, «a lo largo de este documento», «no solo… sino también…» repetido, tríadas retóricas constantes.
- Aperturas y cierres de manual («En este apartado se procederá a…»). Ve al grano.
- Listas con viñetas para todo. En el informe, prosa; usa tablas solo para los datos tabulares que lo pidan.
- Negritas por todas partes, emojis, encabezados con dos puntos y subtítulos grandilocuentes, exceso de guiones largos (—).
- Simetría artificial (tres ventajas, tres inconvenientes, siempre).
- Cualquier mención a ser un asistente, a modelos de lenguaje o a herramientas de IA. Tampoco dejes rastros de agente en nombres de fichero, metadatos del PDF ni comentarios.

**Código**
- Comentarios en español, breves y útiles, solo donde aclaran una decisión («uso Y y no V porque…»). Sin comentar cada línea ni docstrings gigantes. Docstrings de una a tres líneas.
- Nombres de variables y funciones en español, coherentes (`diagnostico`, `diagnostico_color`, `luminancia`, `aplicar_gamma`…). Constantes en mayúsculas al principio.
- Estructura limpia y modular, sin código muerto, sin `print` de depuración sobrantes.

**Honestidad en el análisis**
- Las discrepancias entre predicción y resultado se analizan con un porqué razonado y comprobable (por ejemplo, mirando el histograma de esa imagen), no con frases vacías.
- Si un resultado es modesto, dilo con naturalidad. Si algo es limitación del método, nómbralo.

---

## 2. Entorno y datos

- Usa Python 3 con: `numpy`, `opencv-python-headless`, `pandas`, `matplotlib`, `jupyter`/`nbconvert` (y la librería que uses para generar el PDF, que puede vivir fuera de `codigo/`). Instálalo todo **fuera** del notebook, anota las versiones reales instaladas (`pip freeze` filtrado a lo usado) y escríbelas fijadas en `codigo/requirements.txt` (`paquete==x.y.z`).
- **Imágenes (5)**: el enunciado exige imágenes propias o de banco libre que cubran: subexpuesta, sobreexpuesta/lavada, iluminación desigual, dominante de color evidente, y una con objeto saturado bien definido sobre fondo distinguible (será la del Ejercicio 4). Pueden coincidir dos casos en una imagen.
  - Pídeselas al usuario si no las tiene en `data/`. Si el entorno no tiene acceso de red a bancos de imágenes, no te inventes imágenes: pregunta. Si el usuario autoriza otra vía, documenta honestamente en el informe su procedencia y licencia.
  - Nómbralas `IMG_01.jpg` … `IMG_05.jpg`. Los originales quedan **intactos** en `data/` y todo parte de ellos.
  - Recomendación para el Ejercicio 4: objeto de color rojo no es necesario; si lo es, implementa las dos ventanas de tono (ver abajo).
- Semilla: `SEMILLA = 42` y `np.random.seed(SEMILLA)` al principio, aunque casi no haya aleatoriedad.
- Rutas con `pathlib.Path`, relativas a la raíz del proyecto; crea `outputs/` si no existe.
- Carga con `cv2.imread` (devuelve BGR). Para `diagnostico_color` convierte a RGB y devuelve la media de R, G y B.

---

## 3. Estructura de entrega (obligatoria, tal cual)

```
U1_Practica_Apellidos_Nombre/
├─ memoria/
│  ├─ informe.pdf
│  └─ contrato_preprocesado.md
├─ codigo/
│  ├─ auditoria_fotometrica.ipynb
│  └─ requirements.txt
├─ data/        (las cinco imágenes originales sin retocar)
└─ outputs/
   ├─ resultados_u1.csv
   ├─ robustez_hsv.csv
   └─ (figuras PNG generadas por el código)
```

Sustituye `Apellidos_Nombre` por los datos reales del usuario (pregúntaselos; no los inventes). El tamaño total debe ser ≤ 200 MB. La memoria va en **PDF**, no en Word.

---

## 4. Ejercicio 1: instrumentación

### Luminancia
Usa el canal **Y de YCrCb** (`cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)[...,0]`). Justifícalo en una o dos frases en el informe: Y es la luminancia perceptual (pondera R, G y B distinto, a diferencia de la media aritmética), y al operar solo sobre Y se conserva la información de croma (Cr, Cb) y no se alteran las relaciones entre canales. V de HSV es `max(R,G,B)` y mezcla información de saturación. Usa Y de forma consistente en todo el trabajo; HSV solo para la segmentación del Ejercicio 4.

### `diagnostico(img)` → dict con exactamente estas claves
- `sat_bajo`: % de píxeles de Y con valor ≤ 2.
- `sat_alto`: % de píxeles de Y con valor ≥ 253.
- `rango_p1_p99`: `np.percentile(Y, 99) - np.percentile(Y, 1)`.
- `entropia`: Shannon en bits del histograma normalizado de 256 niveles. `p = hist/hist.sum()`, descarta `p == 0` antes del logaritmo, `-(p*np.log2(p)).sum()`.
- `desv_tipica`: `np.std(Y)`. Anota en el informe que es desviación poblacional (ddof=0).

Asegúrate de que Y sea `uint8` y de trabajar con el histograma de 256 niveles con `np.bincount` o `np.histogram(range=(0,256))`.

### `diagnostico_color(img)` → media de R, G, B.

### Entregables del ejercicio (van en el informe)
1. **Tabla** con el diagnóstico de las cinco originales (fila por imagen, columna por métrica, más las medias RGB).
2. **Un párrafo por imagen (3 a 5 líneas)** traduciendo las cifras a diagnóstico verbal, citando los números concretos de la tabla (no solo «tiene poco contraste»).
3. **Una predicción por imagen** de qué operación funcionará mejor y por qué, con razonamiento ligado a las métricas (p. ej. «sat_bajo del X %, rango estrecho, espero que gamma<1 libere sombras sin quemar luces»). Escríbela **antes** de lanzar el barrido y guárdala en una celda markdown y en el informe tal cual. No la retoques después aunque falle.
4. Figura: rejilla 5×2 con cada imagen y su histograma de luminancia (ejes rotulados: «Nivel de luminancia (0–255)», «Nº de píxeles»), con pie completo.

---

## 5. Ejercicio 2: barrido sistemático

### 5.1 Criterio de selección: declararlo antes de mirar nada
Antes de ejecutar el barrido, escribe en una celda markdown (y guárdalo también en un pequeño fichero de texto en `outputs/` para dejar constancia) algo equivalente a:

- **Criterio por imagen**: entre las configuraciones procesadas que cumplan `sat_bajo ≤ 1 %` y `sat_alto ≤ 1 %`, elegir la de mayor `rango_p1_p99`; desempate por mayor `entropia`.
- **Caso en que ninguna cumpla** (por ejemplo, una imagen con mucha saturación de partida): elegir la que minimice `max(sat_bajo, sat_alto)`, y desempatar por mayor rango.
- **La referencia «original» no compite**, pero se compara con la ganadora para ver si mejora de verdad. Si ninguna mejora al original, se dice.
- **Regla para el lote** (la usará el Ejercicio 5): la configuración que cumple las restricciones en más imágenes; desempate por mayor rango medio entre las cinco.

Declara este criterio una vez y aplícalo igual a las cinco imágenes. No lo modifiques tras ver resultados.

### 5.2 Barrido (22 configuraciones × 5 imágenes = 110 filas)
Todo con bucles, sin repetir código a mano.

| Operación | Parámetros | Nº |
|---|---|---|
| gamma | γ ∈ {0.45, 0.6, 0.8, 1.0, 1.4, 1.8, 2.2} | 7 |
| estiramiento lineal | percentiles ∈ {(0,100),(1,99),(2,98),(5,95)} | 4 |
| HE global | sin parámetros | 1 |
| CLAHE | clipLimit ∈ {1.0,2.0,4.0} × tileGrid ∈ {(4,4),(8,8),(16,16)} | 9 |
| original | – | 1 |

Detalles de implementación (sobre Y, luego reconstruir color):
- **Gamma**: `Y' = 255 * (Y/255) ** gamma` (con γ<1 aclara, como en el ejemplo del enunciado, donde γ=0,55 reduce los píxeles pegados a 0). Usa LUT de 256 valores y redondea a uint8.
- **Estiramiento**: `lo, hi = percentiles de Y`; `Y' = clip((Y-lo)/(hi-lo),0,1)*255`. Protege contra `hi == lo`. Con (0,100) equivale a min-max.
- **HE**: `cv2.equalizeHist(Y)`.
- **CLAHE**: `cv2.createCLAHE(clipLimit, tileGridSize).apply(Y)`.
- **Reconstrucción**: sustituye Y por Y', mantén Cr y Cb, convierte con `YCrCb2BGR`.
- **Métricas de cada fila**: calcula las cinco métricas sobre la luminancia **de la imagen resultante** (reconvierte la imagen final a YCrCb y toma Y), de forma idéntica para todas las filas, incluida la original. Documenta que se mide sobre la imagen final tras el viaje de ida y vuelta de color.

### 5.3 Fichero `outputs/resultados_u1.csv`
- Columnas exactas y en este orden: `imagen,operacion,parametros,sat_bajo,sat_alto,rango_p1_p99,entropia,desv_tipica`.
- Formato de valores como en el ejemplo del enunciado: `operacion` ∈ {`original`,`gamma`,`estiramiento`,`he`,`clahe`}; `parametros`: `-`, `g=0.45`, `p=1-99`, `-` (HE), `clip=2.0;tile=8x8`; sat con 2 decimales, rango entero, entropía con 2 decimales, desv. típica con 1 decimal. Separador `,`, decimal `.`.
- Exactamente **110 filas** más cabecera. Verifícalo por código (assert).

### 5.4 Selección por código y comparación
- Aplica el criterio con pandas (filtros + `idxmax`), nunca a ojo.
- **Tabla resumen** en el informe: imagen, configuración ganadora, métricas antes y después.
- **Comparación con las predicciones del Ejercicio 1**: acierto/discrepancia. Analiza cada discrepancia con una explicación concreta apoyada en cifras (histograma, saturaciones, tipo de iluminación). Los fallos de predicción son lo más valioso de analizar.

### 5.5 Figuras del Ejercicio 2
- Una figura por imagen (`barrido_img01.png` … `barrido_img05.png`): original vs. ganadora, con sus histogramas, **mismos ejes y escalas** en paneles comparables.
- **Una única figura comparativa luminancia vs. RGB por canal**: aplica la misma operación (p. ej. HE) sobre Y y sobre cada canal RGB por separado en una imagen con dominante de color. Cuantifica el desplazamiento de color con `diagnostico_color` (medias RGB antes y después de cada vía) y cítalo en el pie. Nombre sugerido: `comparacion_luminancia_vs_rgb.png`.
- Pies de figura según el protocolo: **operación + parámetros exactos + qué cambió en las cifras**, generados desde el CSV. Ejemplo del tipo: «CLAHE con clipLimit=2,0 y tiles de 8×8 sobre el canal Y. El rango entre percentiles pasa de X a Y niveles y la saturación en negro cae del A % al B %.»

---

## 6. Ejercicio 3: mosaico de Bayer y demosaico

- Elige **una** de las imágenes (preferiblemente con detalle y bordes claros), recórtala a dimensiones pares si hace falta, y explica en el informe por qué la elegiste. Usa la imagen RGB original (no la procesada).
- **Paso 1**: usa `simular_bayer(rgb)` tal como está en el enunciado (RGGB). Ojo: la imagen debe estar en **RGB**, no BGR, o los canales quedarán cambiados.
  - Responde en el informe: fracción de cada canal en el mosaico. Debe salir R = 25 %, G = 50 %, B = 25 %; compruébalo **contando sobre el array** (máscaras booleanas por posición, no sumando a mano) y relaciónalo con la mayor sensibilidad del ojo al verde y con por qué el sensor le da más posiciones.
- **Paso 2**: demosaico bilineal **propio**, sin `cv2.cvtColor` con códigos Bayer. Forma limpia y clara: construir tres máscaras de posiciones medidas (R, G, B), y para cada canal convolucionar el mosaico enmascarado con un kernel y normalizar:
  - G: kernel `[[0,1,0],[1,4,1],[0,1,0]]/4`.
  - R y B: kernel `[[1,2,1],[2,4,2],[1,2,1]]/4`.
  - Trabaja en float y respeta los píxeles medidos (el kernel ya los conserva si se aplica sobre el canal enmascarado). Usa borde reflejado (`cv2.BORDER_REFLECT`). Redondea y recorta a uint8 al final.
  - Comprobación interna: en las posiciones medidas, el valor reconstruido de ese canal debe ser exactamente el original.
  - Opcional como término de comparación: el demosaico de OpenCV. Cuidado con la nomenclatura: para un patrón RGGB OpenCV usa los códigos `COLOR_BayerBG2*` (su nombre se refiere al orden en otra convención). Verifícalo empíricamente (el error debe ser pequeño); si dudas, no lo incluyas.
- **Paso 3**: métricas.
  1. Error absoluto medio por canal (R, G, B).
  2. Mapa de error: suma de |original − reconstruida| sobre los tres canales, en falso color con barra de color rotulada (`error_demosaico.png`).
  3. MAE separado en **bordes** y **resto**: máscara de bordes con Canny sobre la luminancia de la original, con umbrales fijos y documentados (p. ej. 100 y 200) y, si quieres, una pequeña dilatación (documenta cuál). Reporta ambas cifras y el cociente bordes/resto. Interpreta: esa diferencia es lo que sostiene que el demosaico falla en los bordes.
  - Guarda estas cifras en un CSV propio (por ejemplo `outputs/demosaico_metricas.csv`) para poder citarlas y que cualquier cifra del informe esté en un CSV entregado.
- Pie de figura completo (operación, parámetros, cifra).

---

## 7. Ejercicio 4: robustez de una segmentación HSV

Usa la imagen del objeto saturado.

1. **Máscara de referencia**. Convierte a HSV con OpenCV (H en 0–179, S y V en 0–255). Define rangos de tono, saturación mínima y valor, ajústalos **ahora** hasta que la máscara convenza, y **congélalos** como constantes con comentario. Guarda la máscara en `outputs/mascara_referencia.png`. A partir de aquí no se tocan.
   - Si el objeto es **rojo**: dos ventanas de tono (una cerca de 0 y otra cerca de 179) combinadas con `cv2.bitwise_or` / `np.logical_or`. Documenta esa decisión en el informe.
2. **Perturbación**: γ ∈ {0.5, 0.7, 1.0, 1.4, 2.0}, aplicado **sobre la luminancia Y** (misma función que en el Ejercicio 2), reconstruyendo color. γ = 1.0 es el control.
3. **Degradación**: para cada γ, convierte a HSV, aplica **exactamente los mismos rangos**, calcula IoU con la referencia con la función `iou` del enunciado. Sin normalización: el control (γ=1.0) debe dar IoU = 1.0; comprúebalo con un assert.
4. **Intervención**: antes de pasar a HSV, aplica a la imagen perturbada la **mejor configuración del Ejercicio 2 para esta imagen** (la ganadora por el criterio declarado) y vuelve a calcular la IoU con la **misma máscara de referencia** (la de la imagen original sin procesar). Ojo: con γ=1.0 y normalización la IoU puede ser menor que 1, porque la normalización cambia la imagen; es un resultado legítimo y hay que contarlo.
5. **`outputs/robustez_hsv.csv`**: exactamente **10 filas** (5 γ × {sin, con normalización}). Columnas sugeridas: `gamma,condicion,iou` (con `condicion` ∈ {`sin_normalizacion`,`con_normalizacion`}). Se puede añadir alguna columna extra (píxeles de la máscara), pero manteniendo 10 filas.
6. **Gráfica**: ambas curvas IoU vs γ en la misma figura, ejes rotulados, rango del eje y fijo (p. ej. 0–1.05), con leyenda y pie completo.
7. **Interpretación cuantificada**: IoU media sobre los cinco γ antes y después, IoU en el peor caso antes y después, diferencia absoluta. Concluye con honestidad: ¿ha servido de algo? ¿En qué extremo mejora y en cuál no? Da una hipótesis razonada de por qué (por ejemplo, que la normalización empuje valores de V o S fuera de los rangos congelados, o que ayude solo cuando la perturbación comprime el histograma). **No afirmes mejora si las cifras no la muestran.**
   - Si en el Ejercicio 5 la configuración elegida para el lote difiere de la usada aquí (la ganadora de esta imagen), evalúa también la del lote y guarda ese resultado en un CSV aparte (`outputs/robustez_hsv_contrato.csv`), sin tocar el de 10 filas.

---

## 8. Ejercicio 5: contrato de preprocesado

- **Función `preprocesar(img)`**: una sola función, sin parámetros libres, con los valores fijados dentro (constantes con comentario que indique de qué fila del CSV salen). Aplica la configuración elegida con la regla del lote declarada en el Ejercicio 2, siempre sobre luminancia. Debe devolver imagen `uint8` del mismo tamaño y manejar entrada BGR (documenta la convención). Colócala en una celda propia del notebook, bien visible.
- **`memoria/contrato_preprocesado.md`**: **una página como máximo** (apunta a unas 350–450 palabras) con estos cinco apartados numerados:
  1. Qué hace la función, en dos o tres frases y sin jerga.
  2. Parámetros fijados y fila del CSV de la que sale cada uno (referencia exacta: imagen, operación y parámetros).
  3. Mejora aportada con las cifras del Ejercicio 4: IoU antes y después (media y peor caso). Si no mejora, dilo y explica.
  4. **En qué condiciones deja de funcionar** (obligatorio, nunca «en ninguna»): condiciones concretas y razonadas con evidencia propia (por ejemplo, imágenes con saturación previa >X %, escenas casi uniformes donde el estiramiento amplifica ruido, dominantes de color extremas, iluminación mixta que CLAHE trata distinto por zonas, dependencia de que el objeto conserve su tono bajo los rangos congelados).
  5. Qué medir para detectar que ha dejado de funcionar en producción: una o dos métricas del Ejercicio 1 y un **umbral numérico** justificado con los datos (por ejemplo, alarma si `sat_bajo` > X % o `rango_p1_p99` < Y tras el preprocesado, donde X e Y salen del CSV).
- Todas las cifras del contrato deben existir en alguno de los CSV entregados.

---

## 9. Informe PDF (`memoria/informe.pdf`)

Estructura sugerida, en este orden, con prosa natural y sin relleno:
1. Portada breve (título de la práctica, nombre y apellidos del usuario, asignatura/curso si los proporciona).
2. Material de partida: breve descripción de las cinco imágenes y su procedencia/licencia; rejilla imágenes + histogramas.
3. Ejercicio 1: elección de luminancia y justificación, tabla, párrafos, predicciones.
4. Ejercicio 2: criterio declarado (antes del barrido), descripción del barrido, tabla resumen de ganadoras, discrepancias con predicciones, figuras por imagen, figura luminancia vs. RGB.
5. Ejercicio 3: fracciones de canal, demosaico, error por canal, mapa de error, bordes vs. resto.
6. Ejercicio 4: rangos HSV congelados (con la decisión de las dos ventanas si aplica), curvas, interpretación cuantificada.
7. Ejercicio 5: remite al contrato y resume la decisión final.
8. Limitaciones: honestas y concretas (tamaño del lote de 5 imágenes, un único objeto, gamma como única perturbación, etc.).

Requisitos de calidad:
- **Toda figura**: ejes rotulados, escalas coherentes entre paneles comparables (mismos límites en histogramas y curvas), títulos legibles y **pie completo** (operación, parámetros exactos, cifra del cambio) generado desde los datos. Ningún pie que solo nombre la operación.
- Figuras guardadas como PNG con nombres autoexplicativos en `outputs/`, regeneradas en la ejecución final.
- Tablas legibles; cifras con el mismo formato que en los CSV (con coma decimal en prosa).
- Para generar el PDF puedes componer el informe en HTML/Markdown y convertirlo (WeasyPrint, ReportLab o similar) con un script auxiliar; el script auxiliar no hace falta entregarlo, pero el informe debe generarse a partir de los CSV y figuras reales. Revisa visualmente cada página renderizada (convierte a imagen y mírala) antes de dar por buena la maqueta: sin texto cortado, sin figuras desbordadas, sin páginas vacías.
- Metadatos del PDF: autor = nombre del usuario; sin referencias a herramientas.

---

## 10. Código: `codigo/auditoria_fotometrica.ipynb`

- Un notebook ordenado por secciones (markdown breve + código), funciones reutilizables (luminancia, aplicar_gamma, estirar, ecualizar, clahe, diagnostico, diagnostico_color, simular_bayer, demosaico_bilineal, iou, segmentar_hsv, preprocesar).
- Primera celda de código: imports, `SEMILLA`, rutas relativas, creación de `outputs/`. Nada de `!pip install`, ni `%pip`, ni rutas absolutas.
- Ejecútalo con el kernel limpio y de principio a fin (`jupyter nbconvert --to notebook --execute --inplace`), de modo que el notebook entregado lleve las salidas de esa ejecución y los CSV y figuras de `outputs/` sean de esa misma pasada. Borra antes `outputs/*` para comprobar que se regenera todo.
- Si usas rutas, que funcionen tanto lanzando desde `codigo/` como desde la raíz (resuelve la raíz de forma robusta, p. ej. buscando la carpeta `data/`).

---

## 11. Verificación final (obligatoria antes de dar nada por terminado)

Escribe y ejecuta un script de comprobación (no hace falta entregarlo) que verifique:

1. `resultados_u1.csv`: 110 filas, columnas exactas y en orden, 22 configuraciones por imagen, ninguna fila duplicada, sin NaN.
2. `robustez_hsv.csv`: 10 filas; IoU del control sin normalización = 1.0.
3. Todos los números citados en `informe.pdf` (extrae el texto) y en `contrato_preprocesado.md` aparecen en alguno de los CSV (respetando el redondeo y la coma decimal en prosa). Corrige lo que no coincida.
4. Ningún pie de figura sin parámetros ni cifras.
5. `requirements.txt` con `==` en todas las líneas y sin `pip install` en el notebook (`grep`).
6. Sin rutas absolutas en el código (`grep` de `/home`, `/mnt`, `C:\`, `~`).
7. Semilla fijada en la primera celda.
8. Reejecución limpia del notebook sin errores; figuras con fecha de modificación posterior al inicio de esa ejecución.
9. Las imágenes de `data/` no han sido modificadas (compara hash antes y después).
10. `contrato_preprocesado.md` cabe en una página y tiene los cinco apartados, con el apartado 4 sustantivo.
11. Zip con el nombre `U1_Practica_Apellidos_Nombre.zip`, estructura interna exacta, tamaño ≤ 200 MB, memoria en PDF.
12. Lectura final de todo el texto buscando las expresiones de la sección 1 que hay que evitar, y comprobando que el registro es consistente de principio a fin.

---

## 12. Mapa a la rúbrica (para no dejar puntos en la mesa)

- **Corrección técnica (3)**: 5 métricas correctas; las 22 configuraciones × 5 imágenes; Bayer y demosaico bilineal propios; HSV con dos ventanas si el objeto es rojo; todo sobre luminancia.
- **Evidencia y análisis (4)**: cada afirmación con su cifra; criterio declarado antes y aplicado por código; curvas de IoU interpretadas cuantificando la mejora o su ausencia; discrepancias con la predicción analizadas.
- **Figuras y comunicación (1,5)**: escalas coherentes, ejes rotulados, pies completos; PDF.
- **Reproducibilidad y estilo (1,5)**: modular, rutas relativas, semilla, requirements con versiones, ejecución verificada.

## 13. Qué entregar al usuario al terminar

El zip final y un mensaje corto con: qué datos personales hay que revisar (nombre en portada y en el zip), de dónde salió cada imagen, un resumen de 3 o 4 líneas con los resultados principales (ganadoras, IoU antes/después, cociente bordes/resto) y cualquier limitación real que hayas encontrado.
