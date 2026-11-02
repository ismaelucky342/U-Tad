# Megaprompt para opencode: Práctica U1 "Del diagnóstico numérico al contrato de preprocesado" (U-tad, Visión por Computador)

## 0. Cómo trabajar con este documento

Eres un ingeniero de visión por computador que me ayuda a hacer una práctica universitaria individual. Mi objetivo es la nota máxima según la rúbrica. Léete este documento entero antes de tocar nada.

Orden de trabajo obligatorio:

1. Crea `PLAN.md` en la raíz del proyecto con las fases de abajo convertidas en tareas concretas, cada una con su criterio de "hecho". Enséñamelo y espera mi visto bueno antes de ejecutar.
2. Ejecuta fase a fase. Al terminar cada fase, pasa su puerta de control (las casillas de verificación al final de la fase). Si algo no se cumple, arréglalo antes de seguir.
3. Lleva un `_trabajo/BITACORA.md` interno (no se entrega) con decisiones, problemas encontrados y cómo se resolvieron. Servirá para que yo pueda defender la práctica y para el apartado de análisis.
4. Si te hace falta información mía (nombre, imágenes, preferencias), pídemela en el momento exacto en que la necesites y para. No inventes.

Reglas generales:

- Puedes crear todas las herramientas auxiliares que necesites (comprobadores, generadores de imágenes sintéticas, visualizadores, linters, scripts de empaquetado). Van en `_herramientas/` y `_trabajo/`, fuera de la carpeta de entrega, y no se incluyen en el zip.
- Nunca inventes una cifra. Todo número que aparezca en la memoria sale de un CSV generado por el código. Los números de ejemplo del enunciado (18,4 %, 96, 213, 241...) son ilustrativos, no los copies.
- Un resultado modesto y bien medido, o un resultado negativo bien argumentado, puntúa igual que uno espectacular. Si el preprocesado no mejora algo, se dice.
- Idioma de todo lo que se entrega: español de España. Lee la sección 9 antes de escribir una sola línea de texto.

## 1. Qué pide la práctica (resumen operativo)

Entrega: un único zip `U1_Practica_Apellidos_Nombre.zip` con esta estructura exacta:

```
U1_Practica_Apellidos_Nombre/
├─ memoria/
│  ├─ informe.pdf
│  └─ contrato_preprocesado.md
├─ codigo/
│  ├─ auditoria_fotometrica.ipynb   (o .py)
│  └─ requirements.txt
├─ data/        (las cinco imágenes originales sin retocar)
└─ outputs/
   ├─ resultados_u1.csv
   ├─ robustez_hsv.csv
   └─ figuras .png generadas por el código
```

Ponderación de la rúbrica, para decidir dónde poner el esfuerzo:

- Corrección técnica y completitud: 3 puntos.
- Evidencia cuantitativa y análisis: 4 puntos (el bloque más pesado).
- Calidad de figuras y comunicación: 1,5 puntos.
- Reproducibilidad y estilo de código: 1,5 puntos.

Lo que más puntos separa el "excelente" del "satisfactorio": toda afirmación con cifra propia, criterio de selección declarado ANTES de mirar resultados y aplicado por código, curvas de IoU interpretadas con números, discrepancias con la predicción analizadas, pies de figura completos, escalas coherentes entre paneles comparables, histogramas con ejes rotulados, código modular, semilla fijada, requirements con versiones, rutas relativas y ejecución verificada de principio a fin.

## 2. Decisiones técnicas de partida (fíjalas en la Fase 0 y documéntalas)

Estas decisiones condicionan todas las cifras. Escríbelas en la bitácora y en la memoria.

- **Luminancia**: usar el canal Y de YCrCb (OpenCV, uint8) para diagnóstico y para todas las operaciones. Justificación a incluir: separa luminancia de croma, es la conversión vista en la unidad, y permite reconstruir el color sin tocar Cr y Cb. Nunca la media de R, G y B.
- **Dónde se miden las métricas**: siempre sobre el canal Y recalculado a partir de la imagen RGB final (incluida la fila `original`), de modo que todas las filas del CSV sean comparables entre sí. Documentarlo.
- **Convención de gamma**: salida = (entrada/255)^γ · 255, aplicada con una LUT sobre Y. Con γ < 1 aclara y con γ > 1 oscurece. Es coherente con el ejemplo del enunciado (γ=0,45 baja la saturación en negro). Se usa la misma convención en los Ejercicios 2, 4 y 5.
- **Convención de color**: la entrada y salida de `preprocesar(img)` es RGB uint8. Cuidado con que OpenCV lee en BGR; centraliza la lectura en una función que convierta a RGB y no mezcles convenciones.
- **Semilla**: declarada en la primera celda (`SEMILLA = 42`, `np.random.seed`, `random.seed`), aunque casi no haya aleatoriedad.
- **Rutas**: relativas al directorio `codigo/` (por ejemplo `../data`, `../outputs`), con `pathlib`. Nada de rutas absolutas.
- **Sin instalaciones en celdas**: ningún `pip install` dentro del notebook ni del script.

## 3. Fase 0. Reconocimiento y andamiaje

1. Inspecciona el entorno: versión de Python, qué hay instalado (numpy, scipy, opencv, matplotlib, pandas), si hay jupyter/nbconvert, y qué hay para generar PDF (reportlab, weasyprint, pandoc, LaTeX). Crea un entorno virtual en `_trabajo/venv`. Las instalaciones se hacen en la terminal, nunca en las celdas.
2. Pregúntame mi nombre y apellidos para el nombre del zip y de la carpeta raíz.
3. Crea el árbol de carpetas de entrega y el de trabajo.
4. Construye en `_herramientas/` las utilidades base que vayas a reutilizar:
   - generador de imágenes sintéticas de prueba (degradados, patrones de rayas y tableros, objeto de color saturado sobre fondo, versiones subexpuestas y lavadas) para validar el código con resultados conocidos antes de usar mis fotos;
   - función para sacar una "hoja de contacto" PNG que tú mismo puedas abrir y mirar;
   - esqueleto de tests con `assert` para las funciones críticas (ver Fases 2 a 5).
5. Puerta de control: árbol creado, entorno funcionando, decisiones técnicas escritas en la bitácora.

## 4. Fase 1. Imágenes de partida

Necesito cinco imágenes (propias o de banco libre) que cubran, entre todas:

- subexpuesta, con la información apelotonada en la zona oscura;
- sobreexpuesta o lavada, con histograma comprimido;
- iluminación desigual (parte bien expuesta y parte en sombra en el mismo encuadre);
- dominante de color evidente (luz cálida de interior o sombra azulada);
- objeto de color saturado y bien definido sobre fondo distinguible (para el Ejercicio 4).

Una imagen puede cubrir dos casos.

1. Dime con precisión qué imágenes necesitas y con qué características, y espera a que yo te las pase. Para el Ejercicio 4 recomienda un objeto rojo o naranja bien definido si encuentro uno bueno, porque obliga a usar las dos ventanas de tono, que la rúbrica premia. Si no hay uno bueno, vale otro color. Contornos limpios y fondo claramente distinto importan más que el color.
2. Cuando las tengas, calcula sobre ellas un diagnóstico rápido y dime si cada una cumple el papel que se le asigna (por ejemplo, la subexpuesta debería tener un percentil 1 a 99 desplazado hacia valores bajos). Si alguna no encaja, propón qué cambiar.
3. Copia los originales a `data/` con nombres tipo `IMG_01.jpg` ... `IMG_05.jpg`. No los toques. Guarda el SHA-256 de cada uno y haz que el código lo compruebe al arrancar. Anota fuente y licencia de cada imagen en la bitácora (irán a la memoria).
4. Comprueba que el tamaño total del zip final quedará por debajo de 200 MB. Si un original es enorme, avísame en lugar de redimensionarlo por tu cuenta, porque redimensionar ya es retocar.
5. Puerta de control: cinco imágenes validadas, hashes guardados, fuentes anotadas.

## 5. Fase 2. Ejercicio 1: instrumentación, predicciones y criterio (todo ANTES del barrido)

Implementa, en funciones reutilizables:

- `diagnostico(img)` devuelve un diccionario con `sat_bajo` (% de píxeles con Y ≤ 2), `sat_alto` (% con Y ≥ 253), `rango_p1_p99` (percentil 99 menos percentil 1), `entropia` (Shannon, histograma normalizado de 256 niveles, en bits, ignorando bins vacíos) y `desv_tipica`.
- `diagnostico_color(img)` devuelve la media de R, G y B.

Pruebas con resultado conocido (en `_herramientas/`, y las que puedan pasar al código como `assert` ligeros): imagen constante da entropía 0 y desviación 0; degradado uniforme de 0 a 255 da entropía cercana a 8 bits; imagen toda negra da `sat_bajo` = 100; la entropía de un histograma de solo dos niveles equiprobables es 1 bit.

Después, en este orden estricto:

1. Calcula el diagnóstico de las cinco originales y guárdalo en `outputs/diagnostico_originales.csv` (una fila por imagen, una columna por métrica, más las medias RGB).
2. Redacta el diagnóstico verbal de cada imagen (de tres a cinco líneas, con las cifras dentro del texto).
3. Redacta, para cada imagen, la PREDICCIÓN de qué operación funcionará mejor y por qué. Guárdala en `_trabajo/predicciones.md` y calcula su hash.
4. Redacta y fija el CRITERIO DE SELECCIÓN en `_trabajo/criterio_seleccion.md`. Propuesta de partida, que puedes refinar pero hay que fijarla ahora:
   - Por imagen: entre las configuraciones con `sat_bajo` ≤ 1 % y `sat_alto` ≤ 1 %, elegir la de mayor `rango_p1_p99`. Desempate por mayor entropía y, si persiste, por la configuración más sencilla (original, gamma, estiramiento, HE, CLAHE, en ese orden).
   - Si ninguna configuración cumple las restricciones para una imagen, regla de respaldo declarada de antemano (por ejemplo, minimizar el máximo de `sat_bajo` y `sat_alto`).
   - Regla para el LOTE (la que decidirá la función `preprocesar` de la Fase 6), también declarada ahora: por ejemplo, la configuración única que cumple las restricciones en el mayor número de imágenes y, entre ellas, la de mayor rango medio. Define cómo se rompen los empates.
   - Aclara cómo se trata la fila `gamma` con γ=1,0, que coincide con el original.
5. Registra en `_trabajo/orden_declaraciones.log` el hash y la hora de `predicciones.md` y de `criterio_seleccion.md`, y comprueba que son anteriores a la creación de `resultados_u1.csv`. En el código final, el criterio vive como constantes al principio de la sección del Ejercicio 2, antes de la llamada al barrido, y se aplica sobre el CSV por código.
6. Puerta de control: tests pasados, los tres documentos fijados, ningún CSV del barrido existe todavía. No mires resultados del barrido antes de esta puerta.

## 6. Fase 3. Ejercicio 2: barrido sistemático

Rejilla por imagen, con bucles (nada a mano):

- Gamma: γ ∈ {0,45; 0,6; 0,8; 1,0; 1,4; 1,8; 2,2} (7).
- Estiramiento lineal: percentiles de recorte (0,100), (1,99), (2,98), (5,95) (4).
- Ecualización global (HE) (1).
- CLAHE: clipLimit ∈ {1,0; 2,0; 4,0} × tileGrid ∈ {(4,4), (8,8), (16,16)} (9).
- Original (1).

Total: 22 por imagen, 110 filas. Todas las operaciones sobre Y; después se reconstruye el RGB con Cr y Cb originales. Cuidados técnicos: CLAHE y HE necesitan uint8; el estiramiento debe recortar y reescalar a 0-255 con clip explícito; la conversión de ida y vuelta puede mover Y uno o dos niveles, por eso se mide sobre el Y de la imagen final.

El CSV `outputs/resultados_u1.csv`: columnas exactas `imagen,operacion,parametros,sat_bajo,sat_alto,rango_p1_p99,entropia,desv_tipica`, punto decimal, redondeo razonable y fijo. Nombres de operación consistentes (`original`, `gamma`, `estiramiento`, `he`, `clahe`) y parámetros con el formato del enunciado, por ejemplo `g=0.45`, `clip=2.0;tile=8x8`, `p=1-99`. Sin comas dentro de los campos. Generado por el código, 110 filas.

Después:

1. Aplica el criterio de la Fase 2 sobre el CSV por código, sin tocarlo, y genera `outputs/ganadoras_por_imagen.csv` y la tabla resumen.
2. Compara cada ganadora con la predicción. Analiza las discrepancias con cifras y con una hipótesis razonada de por qué ocurren (son lo más valioso para el apartado de análisis).
3. Aplica la regla de lote y guarda el resultado en `outputs/ganadora_lote.csv`.
4. Figura de comparación RGB por canal frente a luminancia: un ÚNICO ejemplo (elige la imagen donde se vea mejor el desplazamiento de color). Calcula una cifra que lo respalde, por ejemplo la variación de las medias R, G y B o de la relación entre canales antes y después por cada vía, y guárdala en un CSV.
5. Figuras `barrido_imgNN.png` (una por imagen): original y ganadora con sus histogramas de luminancia, ejes rotulados, mismos límites de eje en paneles comparables.
6. Puerta de control: 110 filas, columnas exactas, tablas y figuras generadas, discrepancias analizadas con cifras.

## 7. Fase 4. Ejercicio 3: mosaico de Bayer y demosaico

1. Usa `simular_bayer` tal cual está en el enunciado. Si la imagen tiene dimensiones impares, recórtala a dimensiones pares de forma documentada, sin interpolar.
2. Fracción de píxeles por canal: cuenta sobre el array (no asumas), y verifica que sale 25 % R, 50 % G y 25 % B. Relaciónalo con el motivo de que el verde tenga más posiciones (la visión humana es más sensible al verde y el verde aporta la mayor parte de la luminancia). Guarda la cuenta en `outputs/bayer_fracciones.csv`.
3. Demosaico bilineal PROPIO, sin la función de demosaico de OpenCV. Implementación recomendada: convolución con los núcleos clásicos (verde: [[0,1,0],[1,4,1],[0,1,0]]/4; rojo y azul: [[1,2,1],[2,4,2],[1,2,1]]/4) sobre los canales dispersos, con borde reflejado. Pruebas: una imagen constante debe reconstruirse con error cero en el interior; un píxel medido debe conservar exactamente su valor. Si quieres, compara luego con `cv2.cvtColor(..., COLOR_BAYER_*)` como referencia secundaria y rotúlalo así.
4. Errores, en `outputs/error_demosaico.csv`:
   - error absoluto medio por canal entre original y reconstruida;
   - mapa de error en falso color (suma de diferencias absolutas de los tres canales), con barra de color rotulada;
   - error absoluto medio en píxeles de borde frente al resto. Define el borde con Canny (umbrales fijados y anotados) o con umbral sobre el gradiente, y anota qué porcentaje de píxeles es borde. Compara las dos cifras con su cociente.
5. Para qué imagen: una con bordes marcados y texturas finas, de las cinco. Un recorte ampliado del original, el mosaico y la reconstrucción hace la figura muy legible. Anota una limitación honesta: las imágenes JPEG ya vienen demosaicadas y comprimidas, así que la simulación mide el error de nuestro interpolador respecto a una imagen que ya es una interpolación.
6. Puerta de control: tests de demosaico pasados, tres tipos de error calculados, cifra de bordes frente a resto comentable.

## 8. Fase 5. Ejercicio 4: robustez de la segmentación HSV, y Fase 6: contrato

### Fase 5

1. Define los rangos HSV (tono, saturación mínima, valor acotado) sobre la imagen del objeto. Si el objeto es rojo: dos ventanas de tono combinadas con OR lógico, recordando que en OpenCV el tono va de 0 a 179. Ajusta con ayuda de una figura de superposición de máscara que puedas inspeccionar visualmente. Puedes usar una operación morfológica ligera si procede, pero entonces forma parte de los parámetros congelados.
2. Congela rangos y morfología en `_trabajo/rangos_hsv.json` y en constantes del código. Guarda la máscara de referencia en `outputs/mascara_referencia.png`. A partir de aquí no se tocan.
3. Perturbación: γ ∈ {0,5; 0,7; 1,0; 1,4; 2,0} sobre Y, con la convención de la sección 2. Para cada una, aplica los rangos congelados y calcula IoU con la referencia, usando la función `iou` del enunciado.
4. Intervención: para cada γ, perturba, después normaliza la luminancia con la mejor configuración del Ejercicio 2 para ESTA imagen (la ganadora por imagen), y después HSV, rangos y IoU. La referencia sigue siendo la máscara original. Documenta que con γ=1,0 la IoU con normalización puede ser menor que 1, porque la normalización también cambia la imagen, y no lo escondas.
5. `outputs/robustez_hsv.csv`: diez filas (cinco γ por dos condiciones), con columnas como `gamma,condicion,iou`. Una gráfica con ambas curvas, ejes rotulados.
6. Cuantifica: IoU media antes y después, IoU en el peor caso, y en qué γ mejora o empeora y cuánto. Si la mejora solo aparece en un extremo o no aparece, dilo y propón una explicación basada en lo observado (por ejemplo, qué ocurre con la saturación y el valor al aplicar el realce, o que la ecualización mueve píxeles fuera de la ventana de valor).
7. Si la configuración ganadora del lote difiere de la ganadora de esta imagen, calcula también la curva con la del lote en `outputs/robustez_hsv_lote.csv` (archivo adicional, el principal sigue teniendo diez filas) para que el contrato pueda citar cifras coherentes.
8. Puerta de control: diez filas exactas, máscara guardada, rangos congelados y no modificados, cifras de mejora (o su ausencia) calculadas.

### Fase 6: contrato de preprocesado

1. Función única `preprocesar(img)` sin parámetros libres, con los valores fijados dentro, que reproduce exactamente la fila del CSV elegida por la regla de lote. Test: aplicar `preprocesar` a cada imagen debe dar métricas idénticas a las de esa fila del CSV.
2. `memoria/contrato_preprocesado.md`, una página como máximo (unas 350 a 450 palabras), con los cinco apartados exactos:
   1. qué hace, en dos o tres frases y sin jerga;
   2. qué parámetros lleva fijados y de qué fila de `resultados_u1.csv` sale cada uno;
   3. qué mejora aporta, con las cifras de IoU antes y después del Ejercicio 4;
   4. en qué condiciones deja de funcionar (obligatorio, nada de "en ninguna"). Apóyate en lo que hayas observado: imágenes ya saturadas, ruido amplificado por CLAHE, escenas con contenido uniforme, cambios de dominante, el rojo y la costura del tono, etc. Si lo has medido, pon la cifra;
   5. qué métricas vigilar en producción y con qué umbral concreto (por ejemplo `sat_bajo` > X % o `rango_p1_p99` < Y niveles, con X e Y justificados con las cifras de tus imágenes).
3. Puerta de control: test de coincidencia pasado y contrato dentro de la página.

## 9. Lenguaje y estilo: la parte crítica

Todo texto entregable (informe, contrato, comentarios de código, nombres de figuras, títulos de gráficas) tiene que leerse como lo escribiría un estudiante de grado competente y serio, no como texto generado. Reglas:

**Voz**
- Primera persona del singular o impersonal sencillo, como en un informe real ("he medido", "me ha sorprendido que", "no esperaba"). Es una práctica individual.
- Registro formal pero natural, sin jerga innecesaria ni coloquialismos. Español de España, coma decimal en el texto y en los pies (punto decimal solo en los CSV).
- Frases de longitud variada. Alguna corta. Ningún párrafo debe sonar plantilla.

**Contenido**
- Cada afirmación lleva su cifra en la misma frase o en la siguiente. No hay adjetivos sin número ("mejora notable", "gran contraste") salvo que se acompañen de la cifra.
- Cuenta lo que ha pasado de verdad: lo que no salió como esperaba, el error que cometió y arregló, la predicción fallida y la hipótesis de por qué. Esto además es lo que puntúa.
- Matices honestos donde corresponda ("con cinco imágenes no puedo asegurar que esto se generalice"), pero sin muletillas defensivas en cada párrafo.
- Ni resúmenes finales que repiten lo ya dicho ni introducciones que anuncian lo que viene. Entrar directo.

**Fórmulas y muletillas a evitar** (hazlo con un linter en `_herramientas/`, ver Fase 8)
- "Es importante destacar / señalar / tener en cuenta", "cabe destacar", "cabe mencionar", "en este sentido", "en conclusión", "en definitiva", "a modo de resumen", "en el panorama actual", "juega un papel clave/fundamental/crucial", "un enfoque robusto/holístico", "permite sentar las bases", "sin lugar a dudas", "por último pero no menos importante", "delve", "navegar", "ámbito", "paradigma", "sinergia", "potenciar".
- Construcciones "no solo X, sino también Y" repetidas, listas de tres elementos por inercia, antítesis simétricas, enumeraciones "En primer lugar, en segundo lugar...".
- Guiones largos (—) como recurso estilístico: cero o casi cero. Negritas decorativas en medio de párrafos, emojis, títulos con dos puntos tipo "Idea clave:", viñetas para lo que cabe en una frase.
- Cierres tipo "este análisis demuestra la importancia de...". Sustituir por la cifra y su lectura.
- Simetría artificial entre secciones (todas con la misma estructura de párrafos).

**Código**
- Comentarios breves, en español, solo donde el porqué no es obvio ("el rojo cae en la costura del tono, hacen falta dos ventanas"). Sin comentar cada línea ni explicar lo que hace el código evidente. Sin emojis ni banners decorativos en los prints.
- Nombres coherentes con el enunciado y en español (`diagnostico`, `sat_bajo`, `simular_bayer`, `iou`).
- Docstrings cortas y útiles, sin plantillas tipo "Args / Returns" en todas las funciones.
- Sin restos de depuración ni código muerto.

**Texto que sale de las cifras**
- Escribe los pies de figura con f-strings desde los DataFrames del código, para que cifra y figura nunca discrepen. Formato de pie: operación aplicada, parámetros exactos, canal sobre el que se aplicó y qué cambió en las cifras ("CLAHE con clipLimit=2,0 y tiles de 8×8 sobre el canal Y. El rango entre percentiles pasa de X a Y niveles y la saturación en negro cae de A % a B %"). Con otras palabras y con tus números.
- Para el cuerpo de la memoria, primero redacta con marcadores `{{clave}}` que se rellenan desde los CSV y verifica que ninguna cifra queda a mano.

**Autotest de voz**: antes de dar un texto por bueno, léelo como si fueras el profesor que corrige sesenta memorias. Si un párrafo se podría pegar en cualquier otra práctica cambiando los números, reescríbelo con detalles propios de estas imágenes.

## 10. Fase 7. Memoria en PDF (`memoria/informe.pdf`)

Estructura sugerida (títulos sobrios, nada de portadas recargadas):

1. Material y decisiones de partida (imágenes con fuente y licencia, luminancia elegida y por qué, convención de gamma, semilla).
2. Ejercicio 1: tabla de diagnóstico, párrafo por imagen, predicciones.
3. Ejercicio 2: criterio de selección (copiado tal cual se fijó, indicando que se declaró antes de ejecutar el barrido), tabla de ganadoras, comparación con predicciones, discrepancias, figura RGB frente a luminancia.
4. Ejercicio 3: fracciones, método, errores, bordes frente a resto, limitaciones.
5. Ejercicio 4: rangos congelados (y la decisión de las dos ventanas si aplica), curvas, cuantificación de la mejora o su ausencia.
6. Ejercicio 5: referencia al contrato (puede incluirse su contenido).
7. Limitaciones y qué haría con más datos (breve y concreto).

Reglas: PDF, no Word. Todas las figuras con pie completo, ejes rotulados, escalas coherentes entre paneles comparables, etiquetas legibles. Una tabla resumen donde convenga, pero sin saturar. Genera el PDF con la herramienta que haya disponible (reportlab, weasyprint, pandoc...) desde un script en `_herramientas/`. Rasteriza luego las páginas a PNG y mira cada una para detectar desbordes, figuras cortadas, tablas rotas y texto ilegible.

## 11. Fase 8. Código final, auditoría y empaquetado

1. Código: desarrolla como `.py` con celdas `# %%` y convierte a `codigo/auditoria_fotometrica.ipynb` (jupytext o similar). Ejecútalo con el kernel reiniciado (nbconvert con ejecución) para que las salidas queden embebidas. Estructura modular: funciones de utilidad arriba, secciones por ejercicio, una sección final que escribe CSV y figuras. Sin instalaciones, con semilla, con rutas relativas, con la comprobación de hashes de las originales.
2. `codigo/requirements.txt` con versiones fijadas (`paquete==x.y.z`) de lo que usa el código de verdad (numpy, opencv-python-headless, matplotlib, pandas, scipy, etc.) y, si el notebook lo necesita para ejecutarse, ipykernel.
3. Prueba de reproducibilidad en limpio: copia el proyecto a un directorio temporal, borra `outputs/`, crea un entorno nuevo con solo `requirements.txt`, ejecuta de principio a fin y comprueba que se regeneran todos los CSV y figuras. Compara los hashes de los CSV con los de la ejecución anterior: deben coincidir.
4. Verificador de cifras (`_herramientas/verificar_cifras.py`): extrae todos los números de `informe.pdf` (o de su fuente) y de `contrato_preprocesado.md` y comprueba que cada uno aparece en algún CSV de `outputs/`, con tolerancia por redondeo. Los CSV adicionales (diagnóstico, ganadoras, bayer, errores) están permitidos y son la forma de que todas las cifras de la memoria estén respaldadas. Lo que no aparezca, se explica o se quita.
5. Verificador de pies: cada figura de la memoria tiene un pie con operación, parámetros y cifra de cambio.
6. Linter de estilo (`_herramientas/lint_voz.py`): busca en memoria, contrato y código las expresiones de la sección 9, cuenta guiones largos, negritas dentro de párrafos, emojis y frases largas. Corrige lo que salte, reescribiendo de verdad la frase, no sustituyendo palabras.
7. Revisión según rúbrica: comprobación punto por punto de los criterios "Excelente" de las cuatro filas y de la lista de comprobación del enunciado. Escribe en la bitácora qué punto cumple cada cosa.
8. Empaquetado: script que construye `U1_Practica_Apellidos_Nombre.zip` con exactamente la estructura de la sección 1, sin `_herramientas/`, `_trabajo/`, entornos virtuales ni cachés. Verifica nombre del zip, estructura, tamaño menor de 200 MB y que `data/` contiene solo las cinco originales con hashes intactos.
9. Informe final para mí: qué se ha hecho, dónde está cada cosa, las decisiones que he de conocer para defender la práctica, cualquier limitación o duda abierta y los puntos donde conviene que yo personalice o relea el texto (con una frase mía no se nota el sello de nadie más).

## 12. Trampas conocidas (revísalas todas)

- Aplicar CLAHE, HE o estiramiento por canal RGB: penalizado. Todo sobre Y.
- Usar la media de R, G y B como luminancia: penalizado.
- Declarar el criterio de selección después de ver resultados, o aplicarlo a ojo: pierdes los puntos más pesados.
- Olvidar la fila `original`, tener 109 o 111 filas, columnas con nombre distinto al del enunciado.
- Demosaico con la función de OpenCV como solución principal: penalizado.
- Rojo en HSV con una sola ventana de tono.
- Retocar los rangos HSV después de congelarlos.
- Afirmar una mejora que las cifras no respaldan.
- Pies de figura que solo nombran la operación.
- Cifras en la memoria que no están en ningún CSV.
- Rutas absolutas, `pip install` en celdas, requirements sin versiones, semilla ausente.
- Memoria en Word en lugar de PDF; zip con nombre distinto.
- Texto con aire de plantilla o de asistente (sección 9).

## 13. Condiciones de parada

Detente y pregúntame si: faltan imágenes adecuadas; una decisión técnica cambia las cifras de forma sustancial y hay dos opciones razonables; los resultados contradicen alguna parte del plan; o cualquier requisito del enunciado te parece ambiguo y la interpretación afecta a la nota.
