# Auditoría de la práctica ML1 (U1–U2)

## Veredicto

La práctica está terminada y se puede entregar. No veo fallos graves de contenido ni de ejecución. El notebook tiene 110 celdas, 34 de código ejecutadas en orden (1–34), sin errores ni salidas de error, y 10 figuras. El ZIP contiene el notebook y el CSV, y ambos coinciden byte a byte con los archivos actuales.

En tono, encaja con la memoria de Computer Vision: primera persona, decisiones explicadas, límites reconocidos y ninguna pose de “texto generado”. Es más extenso que la media, pero la extensión está justificada por la limpieza y el análisis.

## Lo que está bien

- **Ajuste al enunciado**: EDA, limpieza, inyección controlada de errores, auditoría, estadística descriptiva, visualizaciones y conclusiones. No se limita a describir: justifica decisiones y mide el coste de la imputación.
- **Trazabilidad**: cada error inyectado queda registrado; la detección se hace sin mirar el registro y la auditoría se hace al final. Es exactamente el orden que pide el ejercicio.
- **Coherencia numérica**: los conteos cuadran (93 cambios, 51 nulos, 8 duplicados, 13 imposibles, 10 categorías inválidas). Las diferencias entre el original y el limpio se explican por imputación y recorte, no se ocultan.
- **Honestidad**: reconoce que `cp=4` es contraintuitivo, que `restecg=1` tiene 4 casos, que la moda imputa mal `cp`/`thal`/`ca`, que hay data leakage si se imputa antes de partir y que `ca` puede tener fuga temporal. Eso es lo que más valor tiene en el texto.
- **Figuras**: 10 figuras con ejes rotulados, escalas y colores consistentes; histogramas con media/mediana, boxplots, countplots, scatterplots, pairplot y heatmap.
- **Reproducibilidad**: semilla 42, generador local para la inyección, rutas locales con fallback a UCI y ejecución completa en orden.

## Tono y estilo

Sí se adapta al resto. Usa primera persona de forma natural («he preferido», «me sorprende», «no me fío», «lo dejo anotado») y alterna pasado y presente según toca. No hay un cambio brusco a tono impersonal ni a lista de resultados sin interpretación.

Lo que más se repite es el arranque «Ahora...» / «Voy a...». No es un problema, pero si se quiere afinar, se pueden variar unas cuantas transiciones. También hay algún pasaje muy explicativo para un lector que ya conoce pandas; no molesta, pero se podría recortar si se busca un texto más directo.

## Puntos débiles o mejorables

1. **Dependencias no declaradas.** El notebook importa `seaborn`, que a su vez usa `scipy`, pero no hay `requirements.txt` en el ZIP. En un entorno sin seaborn, el *Restart & Run All* falla. Añadiría un `requirements.txt` con versiones fijadas y lo incluiría en el ZIP. Es la mejora más importante.
2. **ZIP y anexo no coinciden.** El anexo dice que se crea una carpeta `APAU_U1U2_Act1_IsmaelHernandez/` y se comprime; el ZIP actual tiene el notebook y el CSV en la raíz. Funciona igual, pero el texto y el paquete deberían decir lo mismo. O se reempaqueta con carpeta, o se corrige el anexo.
3. **`random_state=42` prometido pero no usado.** La introducción dice que se usa `random_state=42` cuando la función lo permite, pero el notebook no entrena modelos y no hay ninguna llamada con ese argumento. No es un error técnico; sobra la frase o habría que matizarla.
4. **Conteos antes/después de imputar.** En 1.5 se dan 206/97 hombres/mujeres y `cp=4` con 144 casos; tras imputar aparecen 207/96 y 152. Está explicado en 3.1, pero conviene etiquetar el primer bloque como «antes de imputar» para que no parezca una contradicción.
5. **El CSV no es el original puro.** El texto dice «el CSV es el archivo original de UCI con cabecera»; en realidad es el original más una cabecera. Es una precisión menor, pero mejor decir «el original con cabecera añadida».
6. **Repetición de cifras.** Algunas conclusiones repiten números ya vistos; es correcto, pero se podría resumir. No afecta a la entrega.

## Comprobaciones hechas

- 34 celdas de código con `execution_count` 1–34, todas con salida y sin errores.
- 10 figuras embebidas.
- ZIP con 2 archivos; hashes idénticos a los archivos actuales.
- 303 filas y 14 columnas en el CSV; carga local correcta.
- No hay celdas vacías ni `TODO` reales.
- No he podido re-ejecutar el notebook desde cero en este entorno porque falta `seaborn`; el notebook ya trae la ejecución completa.

## Recomendación

No tocaría el análisis. Haría tres cosas antes de entregar: añadir `requirements.txt`, decidir si el ZIP lleva carpeta o no y corregir esa frase del anexo, y quitar o matizar lo de `random_state`. Con eso queda cerrado.
