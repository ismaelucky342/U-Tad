# Spark Learning Path - Ejercicios Completos

## Descripción General
Esta serie de 14 ejercicios cubre de forma progresiva todos los conceptos fundamentales de Apache Spark, desde lo básico hasta problemas complejos de análisis distribuido.

---

## Ejercicios

### **EX00** - Primer RDD Básico
- Conceptos: `parallelize()`, `map()`, `collect()`, `count()`
- Acciones vs Transformaciones

### **EX01** - Transformaciones Encadenadas
- Conceptos: `map()`, `filter()` juntos
- Lazy evaluation
- Cadenas de transformaciones

### **EX02** - map, filter y zipWithIndex
- Conceptos: `map()`, `filter()`, `zipWithIndex()`
- Transformaciones con índices
- Lazy evaluation

### **EX03** - flatMap vs map
- Conceptos: `flatMap()` vs `map()`
- Flatten implícito
- Parsing de datos

### **EX04** - Pair RDD y reduceByKey ⭐
- Conceptos: **Pair RDD**, `reduceByKey()`, word count
- Primera vez con clave-valor
- `sortBy()`, `first()`, `take()`

### **EX05** - groupByKey vs reduceByKey
- Conceptos: `groupByKey()`, diferencia con `reduceByKey()`
- Cuando usar cada uno (performance)
- Estadísticas agregadas

### **EX06** - Acciones: collect, count, take, first
- Conceptos: **Acciones en Spark** (fuerzan DAG)
- `count()`, `take()`, `first()`, `collect()`
- Costo de cada acción

### **EX07** - saveAsTextFile
- Conceptos: **Guardar a disco**, `textFile()`, lectura
- Output en múltiples particiones
- I/O distribuido

### **EX08** - Cache y Persistencia ⭐
- Conceptos: **Cache**, `persist()`, `StorageLevel`
- Performance con reutilización
- `unpersist()` liberación

### **EX09** - Particiones
- Conceptos: **Particiones distribuidas**, `getNumPartitions()`
- `repartition()` vs `coalesce()`
- `glom()`, `mapPartitions()`
- Performance por # particiones

### **EX10** - DAG y Lazy Evaluation ⭐
- Conceptos: **DAG (Directed Acyclic Graph)**
- `toDebugString()` visualización
- Lazy evaluation real
- Cuándo se ejecuta

### **EX11** - SparkSession vs SparkContext
- Conceptos: **SparkSession** (v2.0+)
- DataFrames vs RDDs
- SQL queries nativas
- Catalyst optimizer

### **EX12** - Pair RDD Complejas
- Conceptos: `join()`, `leftOuterJoin()`, `rightOuterJoin()`
- `keys()`, `values()`
- Operaciones de conjunto

### **EX13** - Transformaciones Complejas (Análisis Real)
- Conceptos: **Problema real**: Análisis de logs de ventas
- Pipeline de múltiples transformaciones
- Conversión de tipos, parsing
- Agregaciones múltiples
- Estadísticas complejas

### **EX14** - Inmutabilidad de RDDs ⭐
- Conceptos: **RDDs inmutables**
- Lineage tracking
- Fault tolerance aprovechamiento
- Comparación mutable vs inmutable
- Optimizaciones que permite

### **EX15** - Ejercicio Final: Red Social Completa ⭐⭐⭐
- **Integra TODOS los conceptos**:
  - SparkContext + SparkSession
  - RDDs complejos
  - Pair RDDs variados
  - Cache/persistencia
  - Particiones controladas
  - Lazy evaluation + DAG
  - Múltiples acciones
  - Transformaciones complejas
  - saveAsTextFile
  
- **Problema**: Análisis completo de red social
  - Usuarios, Posts, Comentarios
  - Estadísticas por usuario
  - Detectar influencers
  - Análisis por país
  - Posts populares
  - Estadísticas globales

---

## Conceptos Cubiertos

| Concepto | Ejercicios | Complejidad |
|----------|-----------|------------|
| **RDD** | 00-15 | ⭐ |
| **Transformaciones** | 00-15 | ⭐ |
| **Acciones** | 00, 01, 06, 15 | ⭐ |
| **Lazy Evaluation** | 01, 02, 10, 14 | ⭐⭐ |
| **DAG** | 10, 14, 15 | ⭐⭐ |
| **Particiones** | 09, 15 | ⭐⭐ |
| **SparkContext** | 00-15 | ⭐ |
| **SparkSession** | 11, 15 | ⭐⭐ |
| **Driver** | 15 (implicit) | ⭐⭐ |
| **Executors** | 15 (implicit) | ⭐⭐ |
| **Cluster Manager** | 15 (config) | ⭐⭐ |
| **Cache/Persistencia** | 08, 15 | ⭐⭐ |
| **Pair RDD** | 04, 05, 12, 13, 15 | ⭐⭐ |
| **map** | 00-15 | ⭐ |
| **filter** | 00-15 | ⭐ |
| **flatMap** | 03, 13 | ⭐⭐ |
| **reduceByKey** | 04, 13, 15 | ⭐⭐ |
| **groupByKey** | 05, 13, 15 | ⭐⭐ |
| **collect** | 06, 15 | ⭐ |
| **count** | 06, 15 | ⭐ |
| **take** | 06, 15 | ⭐ |
| **saveAsTextFile** | 07, 15 | ⭐⭐ |
| **parallelize** | 00-15 | ⭐ |
| **Inmutabilidad** | 14, 15 | ⭐⭐ |
| **Ejecución Distribuida** | 09, 15 | ⭐⭐⭐ |

---

## Cómo Usar

### Compilar
```bash
scalac -cp /path/to/spark/jars/* exNN.scala
```

### Ejecutar con spark-submit
```bash
spark-submit --class EjercicioSparkNN exNN.jar
```

### Ejecutar localmente (dev)
```bash
spark-shell
```

Luego copiar/pegar el código del ejercicio.

---

## Progresión de Dificultad

```
EX00 ──► EX01 ──► EX02 ──► EX03 ──► EX04
         ┌────────────────────────────┘
         │
      EX05 ──► EX06 ──► EX07 ──► EX08 ──► EX09
         │                                  │
         └──────────────────────────────────┘
                        │
                    EX10 ──► EX11 ──► EX12 ──► EX13
                        │                        │
                        └────────┬───────────────┘
                                 │
                            EX14 ─┴─ EX15 (FINAL)
```

---

## Objetivos Alcanzados

✅ Entender RDD como abstracción fundamental  
✅ Dominar transformaciones: map, filter, flatMap, reducByKey, groupByKey  
✅ Diferenciar entre transformaciones (lazy) y acciones  
✅ Comprender DAG y lazy evaluation  
✅ Controlar particiones para performance  
✅ Usar cache/persistencia eficientemente  
✅ Trabajar con Pair RDDs complejos  
✅ Entender falta de tolerancia (lineage)  
✅ Aprovechar inmutabilidad para paralelismo sin bugs  
✅ Resolver problemas reales con Spark  

---

## Tips de Performance

1. **Evita collect() con RDDs grandes** → Usar take(), count()
2. **Cache antes de múltiples acciones** → Reutiliza cálculos
3. **reduceByKey > groupByKey** → Menor shuffle
4. **Particiones correctas** → Menos overhead, mejor paralelismo
5. **Lazy evaluation** → Inspecciona DAG con toDebugString()
6. **Inmutabilidad = Paralelismo seguro** → Sin locks/sincronización

