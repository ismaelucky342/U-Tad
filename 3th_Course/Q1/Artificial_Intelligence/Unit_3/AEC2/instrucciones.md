``
Centro adscrito a
```
# UNIDAD 3

# ACTIVIDAD PRÁCTICA

# CLASIFICACIÓN DE PERROS Y

# GATOS CON CNN Y TRANSFER

# LEARNING


## ÍNDICE

- ORGANIZACIÓN DE LA ACTIVIDAD PRÁCTICA
- DESCRIPCIÓN DE LA ACTIVIDAD PRÁCTICA
   - Participación en la Competición de Kaggle
   - Documentación de las iteraciones
- RÚBRICA DE CORRECCIÓN
- CÓMO REALIZAR LA ENTREGA


## ORGANIZACIÓN DE LA ACTIVIDAD PRÁCTICA

### Clasificación de Perros y Gatos con CNN y Transfer Learning

### Tipo de tarea Individual

### Entregables Un archivo INSD_INAR_U 3 _Nombre_Apellido1_Apellido2.zip

### que contenga:

### - CyD_Nombre_Apellido1_Apellido2.ipynb

### - CyD_Nombre_Apellido1_Apellido2.pdf

## DESCRIPCIÓN DE LA ACTIVIDAD PRÁCTICA

**Importante: Si se utilizan argumentos o código no basados en el material proporcionado en la asignatura,**

**se deberá indicar obligatoriamente las referencias bibliográficas (libros, páginas web, videos) utilizadas.**

**En caso contrario, la calificación de la actividad será de 0 puntos.**

El objetivo de esta actividad es aplicar los conocimientos de redes neuronales convolucionales (CNN) y

transfer learning para resolver un problema de clasificación de imágenes. Participarás en la competición de

Kaggle **[U-Tad] Dogs vs. Cats 2025** , entrenando y optimizando modelos, y documentando el proceso

experimental hasta el resultado final.

### Participación en la Competición de Kaggle

**Para unirte a la competición utiliza este enlace utilizando una cuenta de Kaggle verificada.**

El objetivo es obtener el mejor accuracy score posible en la competición. Deberás registrarte, realizar

múltiples envíos (submissions) y experimentar para mejorar tu resultado. Se recomienda utilizar el notebook

**[U-Tad] Competition starter: CNN** como punto de partida.

La competición finaliza el **14 de noviembre de 2025 a las 12:45**. Tendrás hasta el 23 de noviembre a las 23:

para la entrega del resto de elementos del proyecto en Blackboard.

En el documento **Kaggle_competition_guide.pdf** tienes más información relativa al funcionamiento de las

competiciones en Kaggle.

### Documentación de las iteraciones

Para evaluar tu proceso de trabajo, deberás documentar cada experimento significativo que realices en un

documento PDF. Este documento debe seguir una estructura clara, detallando los cambios introducidos en

cada iteración y los resultados obtenidos.


Se recomienda utilizar la siguiente plantilla para cada iteración (se requiere un mínimo de 4 iteraciones

documentadas para poder aspirar a la máxima calificación):

**PLANTILLA DE ITERACIÓN**

**Iteración #** : [Ej: 1]

**Fecha** : [Ej: 31 /10/2025]

**Descripción del Cambio** : [Ej: "He añadido un nuevo bloque convolucional (una capa Conv2D con 128 filtros

y su correspondiente capa MaxPooling2D) para hacer la red más profunda. Adicionalmente, he

incrementado el número de épocas de entrenamiento de 12 a 20."]

**Hipótesis/Justificación** : [Ej: "Mi hipótesis es que un modelo con mayor profundidad puede aprender a

identificar características más complejas y abstractas de las imágenes, lo que debería mejorar la precisión.

El aumento de épocas es necesario para asegurar que esta red, ahora más grande, tenga tiempo suficiente

para entrenar y que sus pesos converjan correctamente."]

**Resultado Obtenido** :

- **Validation Accuracy** : [Ej: "0.85 -> 0.88"]
- **Kaggle Public Score** : [Ej: "0.86 -> 0.89"]

**Conclusiones y Próximos Pasos** : [Ej: "El modelo ha mejorado, lo que confirma que una mayor profundidad

fue beneficiosa para este problema. Sin embargo, el tiempo de entrenamiento ha aumentado

considerablemente. Dado que seguir añadiendo capas manualmente puede llevar a rendimientos

decrecientes y a un coste computacional muy alto, el siguiente paso lógico es probar _transfer learning_ con

una arquitectura ya optimizada para ver si se puede superar este resultado de forma más eficiente."]

**Referencias** : [Ej: https://keras.io/guides/transfer_learning/]

### Notebook Final

Este notebook debe contener el código de tu mejor modelo. El código debe estar limpio, bien estructurado

y comentado.

Además del código de entrenamiento, el notebook debe incluir una sección final de análisis y conclusiones

con los siguientes elementos:

- **Análisis de Métricas Finales** : Muestra y comenta la accuracy y loss final obtenidas en el conjunto de
    validación (o en el supplementary_data).
- **Curvas de Aprendizaje** : Genera y comenta los gráficos de loss y accuracy de entrenamiento y
    validación. ¿Hay signos de overfitting o underfitting?
- **Reflexión Final** : Explica brevemente por qué crees que este modelo fue el que mejor funcionó,
    haciendo referencia a tus experimentos documentados en iteraciones.pdf


## RÚBRICA DE CORRECCIÓN

### Criterios Excelente Satisfactorio No satisfactorio Insuficiente

### Leaderboard

### Privado

### ( 3 puntos)

```
2 .5 – 3 .0 puntos
```
```
El score de accuracy
final se encuentra en el
top 25% (primer cuartil,
Q1) del leaderboard
final privado.
Demuestra un
rendimiento
excepcional.
```
```
1. 5 – 2 .4 puntos
```
```
El score de accuracy
final se encuentra
por encima de la
mediana (segundo
cuartil, Q 2 ) del
leaderboard privado
o supera
notablemente el
baseline (0.569).
Muestra un
rendimiento sólido.
```
0. 5 – 1. 4 puntos

```
El score de accuracy
final apenas supera
el baseline inicial
(0.569) o se
encuentra por
debajo de la
mediana. El
rendimiento es
básico.
```
```
0 .0 - 0. 4 puntos
```
```
No se realizan
entregas a la
competición o el
score de accuracy es
igual o inferior al
baseline.
```
### Documentación

### de Iteraciones

### ( 3 puntos)

```
2 .5 – 3 .0 puntos
```
```
Documenta 4 o más
iteraciones. Cada una
presenta una hipótesis
clara, cambios bien
justificados y
conclusiones profundas
que guían lógicamente
los siguientes pasos del
proceso.
```
```
1. 5 – 2 .4 puntos
```
```
Documenta al menos
3 iteraciones. Las
descripciones son
correctas, pero las
hipótesis o
conclusiones carecen
de profundidad o no
siempre están bien
justificadas.
```
0. 5 – 1. 4 puntos

```
Documenta menos
de 3 iteraciones o las
descripciones son
superficiales, sin
hipótesis claras o
análisis de
resultados. El
documento es un
mero listado de
acciones.
```
```
0 .0 - 0. 4 puntos
```
```
No se entrega el
documento, no sigue
la plantilla o no
refleja un proceso de
experimentación
real.
```
### Análisis en

### Notebook Final

### ( 4 puntos)

```
3. 5 – 4 .0 puntos
```
```
El análisis es
exhaustivo. Interpreta
correctamente las
métricas finales y las
curvas de aprendizaje,
identificando
claramente
overfitting/underfitting.
La reflexión final
conecta de forma
excelente el modelo
con el proceso
iterativo.
```
```
2 .0 – 3. 4 puntos
```
```
El análisis es
correcto e incluye los
elementos
solicitados. Sin
embargo, la
interpretación de las
curvas o la reflexión
final es superficial o
la conexión con las
iteraciones es débil.
```
```
1. 0 – 1. 9 puntos
```
```
El notebook incluye
solo parcialmente los
elementos de
análisis. Las
interpretaciones son
erróneas o están
ausentes. El código
no está limpio o bien
comentado.
```
```
0 – 0.9 puntos
```
```
No se incluye
ninguna sección de
análisis o el
notebook es una
copia directa del
código de inicio sin
modificaciones
sustanciales.
```
## CÓMO REALIZAR LA ENTREGA

Deberás entregar un archivo INSD_INAR_U 3 _Nombre_Apellido1_Apellido2.zip que contenga:

1. El fichero CyD_Nombre_Apellido1_Apellido2.pdf con la documentación de tus iteraciones.
2. El notebook CyD_Nombre_Apellido1_Apellido2.ipynb con tu mejor modelo.