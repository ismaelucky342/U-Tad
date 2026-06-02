/*
Ejercicio 5_D - PROBLEMA CONCEPTUAL: MapReduce

IMPORTANTE: Este ejercicio NO requiere código.
Es una evaluación conceptual de los problemas y limitaciones de MapReduce.

---

PREGUNTA 1: ¿Cuál es el cuello de botella principal en MapReduce?

A) La fase MAP siempre es lenta
B) El shuffle (mezcla de datos entre MAP y REDUCE) implica E/S a disco
C) Los REDUCERs no pueden procesar en paralelo
D) El número de mappers es limitado por el tamaño del clúster

RESPUESTA CORRECTA: B
EXPLICACIÓN:
En MapReduce, después de la fase MAP, todos los datos intermedios
deben escribirse a DISCO LOCAL, luego transferirse por red, y finalmente
leerse desde disco en la fase REDUCE. Esta es operación I/O intensiva
que causa latencia alta. En cambio, Spark mantiene datos en memoria.

---

PREGUNTA 2: Tenemos un dataset de 100 GB. Configuramos:
- MapTask size: 64MB → 1562 mappers
- Número de reducers: 10

¿Qué problema ocurriría?

A) Los 1562 mappers ejecutarían en paralelo sin problemas
B) Severe skew: solo 10 reducers reciben salida de 1562 mappers
C) Deadlock entre mappers y reducers
D) El cluster se queda sin memoria

RESPUESTA CORRECTA: B
EXPLICACIÓN:
Tener 1562 mappers productores pero solo 10 reducers consumidores crea:
1. Desbalance: algunos reducers reciben muchos más datos que otros
2. Cuello de botella: 10 reducers no pueden procesar 1562 streams en paralelo
3. Impacto: algunos reducers terminan en minutos, otros tardan horas

La solución sería aumentar reducers, pero el parámetro está "fijo" en configuración.

---

PREGUNTA 3: ¿Cuál es el propósito del "Combiner" en MapReduce?

A) Combinar múltiples datasets de entrada
B) Reducir datos ANTES del shuffle (agregación local en cada mapper)
C) Hacer merge de archivos HDFS fragmentados
D) Combinar output de múltiples jobs secuenciales

RESPUESTA CORRECTA: B
EXPLICACIÓN:
El Combiner es un "mini-reducer" que ejecuta EN CADA MAPPER después
de que termina el MAP local. Su objetivo:
- Reduce volumen de datos a transmitir por red (< I/O)
- Es opcional pero muy recomendado para operaciones agregativas
- Ejemplo: contar palabras, sumar valores, calcular máximos

Nota: El Combiner NO es mandatorio; el REDUCER siempre ejecuta.

---

PREGUNTA 4: Comparada con Spark, ¿por qué MapReduce es más lento
            en la mayoría de casos?

A) Spark tiene hardware mejor
B) MapReduce escribe TODOS los datos intermedios a disco
C) MapReduce no utiliza compilación JIT
D) Spark está optimizado solo para máquinas locales

RESPUESTA CORRECTA: B
EXPLICACIÓN:
Las razones de performance:

MapReduce:
- Escribir a disco después de MAP
- Leer de disco antes de REDUCE
- Serialización completa de todos los datos intermedios
- I/O latency dominante

Spark:
- Mantiene datos en memoria (RDD caché)
- Si debe derrames (spill), es selectivo
- Lazy evaluation optimiza el plan de ejecución
- Pipeline de transformaciones sin intermedios

Ejemplo numérico:
- MapReduce word count: 5 minutos (2 I/O + 1 de computo)
- Spark word count: 30 segundos (1 I/O + 0.5 computo)

---

PREGUNTA 5: ¿En qué caso de uso TODAVÍA hace sentido usar MapReduce
            sobre Spark en 2024?

A) MapReduce es mejor para todos los casos; Spark es más moderno pero lento
B) MapReduce es usado en entornos legacy; Spark es la mejor opción moderna
C) MapReduce es superior para procesamiento batch de datos muy grandes
D) MapReduce y Spark tienen exactamente el mismo performance

RESPUESTA CORRECTA: B
EXPLICACIÓN:
Estado en 2024:

MapReduce:
- Legado: Muchas empresas lo usan en pipelines antiguos que funcionan
- Mantenimiento: Apache Hadoop sigue recibiendo soporte
- Pero: Es considerado obsoleto para nuevos proyectos

Spark:
- Modern: Mejor performance, mejor API, mejor integración
- Recomendado: Para nuevos proyectos, migración es lo común
- Ecosystem: Funciona con Kubernetes, Delta Lake, MLlib, etc.

Excepción muy pequeña:
- Si tienes restricción EXTREMA de RAM (cluster muy pequeño)
- MapReduce podría ser más "robusto" por usar disco
- Pero incluso así, Spark moderno es mejor opción

CONCLUSIÓN: MapReduce es historia. Usa Spark.

---

ANÁLISIS CONCEPTUAL ADICIONAL:

FASES DE MapReduce vs Spark:

MapReduce:
1. INPUT SPLIT: División de datos en bloques
2. MAP: Procesa bloques en paralelo
3. SPILL TO DISK: Escribe output local a disco
4. SORT & SHUFFLE: Ordena y redistribuye por clave
5. TRANSFER OVER NETWORK: Red de datos entre nodos
6. SORT BY KEY: Ordena datos de entrada al reducer
7. REDUCE: Agregación final
8. OUTPUT WRITE: Escribe resultado a HDFS

Spark RDD:
1. PARTITION: Divide en particiones (no necesariamente en disco)
2. LAZY TRANSFORM: Define el plan de ejecución (sin ejecutar)
3. ACTION: Ejecuta solo lo necesario, en memoria
4. SPILL IF NEEDED: Solo si memoria insuficiente

VENTAJAS SPARK:
✓ No escribe intermedia a disco → Más rápido
✓ Lazy evaluation → Optimiza plan de ejecución
✓ In-memory caching → Reutiliza datos entre jobs
✓ API funcional → Más expresivo son escritura verbosa

DESVENTAJAS SPARK:
✗ Requiere más RAM (puede causar OOM)
✗ Menos madurez en manejo de fallos (aunque ha mejorado)
✗ Curva de aprendizaje mayor (conceptos funcionales)

---

CONSEJOS PARA EL EXAMEN:

1. Si preguntan "¿por qué MapReduce es lento?" → Responde "Shuffle + Disk I/O"
2. Si preguntan "¿cuándo usar MapReduce?" → Responde "Legacy/histórico, no nuevos proyectos"
3. Si preguntan "¿qué es Combiner?" → "Mini-reducer local en cada mapper"
4. Si muestran código viejo MapReduce → Reconoce que debería ser Spark
5. Recuerda: Spark = mejor en 99% de casos. MapReduce = 1% casos legacy.

*/

println("""
╔════════════════════════════════════════════════════════════════╗
║  EJERCICIO 5_D: CONCEPTOS DE MapReduce                        ║
╚════════════════════════════════════════════════════════════════╝

RESUMEN DE RESPUESTAS:
├─ P1 - Cuello de botella: B (Shuffle/Disk I/O)
├─ P2 - Desbalance 1562 MAP vs 10 REDUCE: B (Severe skew)
├─ P3 - Propósito Combiner: B (Agregación local pre-shuffle)
├─ P4 - MapReduce vs Spark: B (Escritura disco intermedia)
└─ P5 - Cuándo usar MapReduce 2024: B (Legacy, Spark es mejor)

CONCEPTOS CLAVE:
1. MAP → SHUFFLE → REDUCE (E/S a disco entre fases)
2. Combiner = optimización (pre-agregación en mapper)
3. Reducer count matter (balanced input es crítica)
4. Spark superó MapReduce (in-memory > disk-based)
5. MapReduce es historia en 2024

REGLA PRÁCTICA:
MapReduce performance = I/O time + Network time + Compute time
Spark performance ≈ Compute time (si cabe en memoria)
""")
