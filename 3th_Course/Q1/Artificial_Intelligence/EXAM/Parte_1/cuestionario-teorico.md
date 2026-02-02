# BLOQUE 1

## Comparación modelo final vs baseline (bloque a bloque)

---

### En este bloque has añadido Dropout respecto al baseline. ¿Qué mejora introduce?

**Respuesta de examen:**

> Este Dropout reduce el riesgo de que el modelo memorice los datos de entrenamiento en esta parte concreta de la red, forzando a que las neuronas no dependan siempre de las mismas activaciones. Esto mejora la generalización frente al baseline, que no tenía este control.
> 

> Dropout:
> 
> 
> Es una técnica que apaga aleatoriamente algunas neuronas durante el entrenamiento para evitar que el modelo se acostumbre a usar siempre las mismas y termine memorizando los datos.
> 

---

### Aquí has añadido una normalización que no estaba en el baseline. ¿Qué cambia?

**Respuesta de examen:**

> Esta capa hace que los valores que produce la red se mantengan dentro de un rango estable. En el baseline estos valores podían variar mucho, haciendo el entrenamiento más inestable. En el modelo final el aprendizaje es más suave y consistente.
> 

> Normalización (Batch Normalization):
> 
> 
> Es una técnica que ajusta los valores internos de la red para que no se disparen ni se hagan demasiado pequeños, facilitando el aprendizaje.
> 

---

### En este bloque hay más convoluciones que en el baseline. ¿Qué aporta eso?

**Respuesta de examen:**

> Añadir más convoluciones permite que el modelo aprenda combinaciones de patrones más complejas antes de reducir el tamaño de la imagen, lo que mejora la capacidad de distinguir detalles visuales.
> 

> Capas convolucionales: Son capas que detectan patrones locales como bordes, texturas y formas dentro de una imagen.
> 

---

### En este bloque aumentas el número de filtros respecto al baseline. ¿Qué mejora eso?

**Respuesta de examen:**

> Aumentar el número de filtros permite al modelo detectar más tipos distintos de patrones en las imágenes. Frente al baseline, el modelo final puede representar mejor la diversidad de formas y texturas de la ropa.
> 

> Filtros en una convolución:
> 
> 
> Son detectores de patrones. Cuantos más filtros, más tipos de patrones puede aprender la red.
> 

---

### Aquí el baseline reducía antes el tamaño de la imagen. ¿Por qué en tu modelo no?

**Respuesta de examen:**

> Porque reducir el tamaño demasiado pronto puede hacer que se pierda información importante. En el modelo final se extraen primero más características y después se reduce el tamaño.
> 

> Reducción de tamaño (pooling):
> 
> 
> Es un proceso que hace la imagen más pequeña quedándose con lo más relevante.
> 

---

### El baseline entrenaba siempre el mismo número de épocas. ¿Qué aporta cambiar eso?

**Respuesta de examen:**

> Permite que el entrenamiento se adapte al comportamiento real del modelo, evitando entrenar de más cuando ya no mejora la validación.
> 

> Época:
> 
> 
> Es una pasada completa del modelo por todos los datos de entrenamiento.
> 

---

# BLOQUE 2

## Preguntas concretas sobre el modelo final

---

### ¿Por qué usas distintos valores de Dropout en distintas partes del modelo?

**Respuesta de examen:**

> Porque no todas las capas tienen el mismo riesgo de sobreajuste. Las capas finales tienen muchos más parámetros y es más fácil que memoricen, por eso ahí el Dropout es más alto.
> 

> Sobreajuste (overfitting):
> 
> 
> Ocurre cuando el modelo aprende demasiado bien los datos de entrenamiento y luego falla al generalizar a datos nuevos.
> 

---

### ¿Qué función cumple el pooling en tu modelo?

**Respuesta de examen:**

> El pooling reduce el tamaño de la representación manteniendo la información más relevante. Esto reduce el número de parámetros y ayuda a controlar el sobreajuste.
> 

> Pooling:
> 
> 
> Es una operación que reduce el tamaño de una imagen o mapa de características quedándose con lo más importante.
> 

---

### ¿Por qué usas una capa densa relativamente grande al final?

**Respuesta de examen:**

> Esta capa combina las características aprendidas por las capas anteriores para tomar la decisión final. Tiene suficiente capacidad para hacerlo, pero está regularizada para evitar que memorice.
> 

> Capa densa:
> 
> 
> Es una capa en la que todas las neuronas están conectadas entre sí y sirven para combinar información ya extraída.
> 

---

### ¿Qué hace exactamente Early Stopping?

**Respuesta de examen:**

> Detiene el entrenamiento cuando el modelo deja de mejorar en validación, evitando que siga ajustándose a los datos de entrenamiento y empeore la generalización.
> 

> Early Stopping:
> 
> 
> Es una técnica que para el entrenamiento automáticamente cuando seguir entrenando deja de aportar mejoras reales.
> 

---

### ¿Para qué sirve reducir el learning rate durante el entrenamiento?

**Respuesta de examen:**

> Permite que el modelo haga ajustes grandes al principio y ajustes pequeños al final, afinando el aprendizaje cuando ya está cerca de una buena solución.
> 

> Learning rate:
> 
> 
> Es el tamaño de los pasos que da el modelo cuando ajusta sus pesos durante el entrenamiento.
> 

---

### ¿Por qué normalizas los datos de entrada antes de entrenar?

**Respuesta de examen:**

> Para que todas las imágenes tengan valores comparables y el modelo no tenga que aprender a manejar escalas distintas. Esto hace que el entrenamiento sea más estable.
> 

> Normalización de datos:
> 
> 
> Es llevar los valores de entrada a un rango común, normalmente entre 0 y 1.
> 

---

### ¿Por qué usas Adam como optimizador y no otro?

**Respuesta de examen:**

> Porque ajusta automáticamente la velocidad de aprendizaje de cada peso, lo que hace el entrenamiento más estable sin necesidad de mucho ajuste manual.
> 

> Optimizador:
> 
> 
> Es el algoritmo que decide cómo se actualizan los pesos del modelo durante el entrenamiento.
> 

---

### ¿Qué pasaría si quitas la normalización pero mantienes el resto igual?

**Respuesta de examen:**

> El entrenamiento sería más inestable y podría necesitar más ajustes del learning rate o incluso no converger bien.
> 

> Convergencia:
> 
> 
> Es el proceso por el cual el modelo va encontrando una buena solución durante el entrenamiento.
> 

---

### ¿Por qué usas una función Softmax al final?

**Respuesta de examen:**

> Porque transforma las salidas del modelo en probabilidades, permitiendo interpretar el resultado como la clase más probable.
> 

> Softmax:
> 
> 
> Es una función que convierte un conjunto de valores en probabilidades que suman uno.
> 

# BLOQUE 3

---

### ¿Qué harías para reducir el overfitting sin cambiar los datos?

**Respuesta de examen:**

> Aumentaría la regularización, por ejemplo ajustando el Dropout, reduciendo la complejidad del modelo o parando antes el entrenamiento.
> 

> Regularización:
> 
> 
> Son técnicas que limitan la capacidad del modelo para evitar que memorice los datos.
> 

---

### Si el rendimiento es bajo tanto en entrenamiento como en validación, ¿qué indica eso?

**Respuesta de examen:**

> Indica que el modelo no tiene suficiente capacidad para aprender el problema o que el entrenamiento no está bien ajustado.
> 

> Baja capacidad (underfitting):
> 
> 
> Ocurre cuando el modelo es demasiado simple para capturar los patrones del problema.
> 

---

### ¿Cómo decidirías qué mejorar primero: arquitectura o entrenamiento?

**Respuesta de examen:**

> Primero analizaría el comportamiento del entrenamiento. Ajustar cómo aprende el modelo suele ser más efectivo que cambiar la arquitectura sin diagnóstico.
> 

> Curvas de entrenamiento:
> 
> 
> Son gráficas que muestran cómo evoluciona el rendimiento del modelo durante el aprendizaje.
> 

### Si una clase concreta falla mucho más que las demás, ¿qué harías?

**Respuesta de examen:**

> Analizaría los errores de esa clase para ver si el modelo no está capturando bien sus características y ajustaría la arquitectura o la regularización en consecuencia.
> 

> Análisis por clase:
> 
> 
> Es estudiar cómo se comporta el modelo en cada categoría, no solo la media.
> 

---

### Si ves que el modelo aprende muy lento, ¿qué tocarías primero?

**Respuesta de examen:**

> Ajustaría la velocidad de aprendizaje o el tamaño del batch antes de cambiar la arquitectura.
> 

> Tamaño de batch:
> 
> 
> Es el número de ejemplos que el modelo procesa antes de actualizar los pesos.
> 

---

### ¿Cómo justificarías que una mejora es correcta y no casual?

**Respuesta de examen:**

> Repitiendo el entrenamiento y comprobando que el comportamiento es consistente y no depende de una ejecución concreta.
> 

> Variabilidad del entrenamiento:
> 
> 
> Pequeñas diferencias pueden hacer que los resultados cambien entre ejecuciones.
> 

---


**“¿Qué limitación principal tiene tu modelo?”**

**Respuesta de examen:**

> Que el equilibrio entre capacidad y regularización es delicado, y pequeños cambios pueden llevar a sobreajuste o a que el modelo se quede corto.
> 

> Compromiso capacidad–generalización:
> 
> 
> Cuanto más aprende un modelo, más riesgo hay de que memorice.
> 

---