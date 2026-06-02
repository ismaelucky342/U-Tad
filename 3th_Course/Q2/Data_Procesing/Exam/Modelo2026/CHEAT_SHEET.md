#  CHEAT SHEET - Referencia Rápida para el Examen

## Scala Básico

```scala
// LECTURA Y ESCRITURA DE ARCHIVOS
import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile("archivo.txt").getLines().toList
val writer = new PrintWriter("salida.txt")
writer.println("texto")
writer.close()

// TRANSFORMACIONES DE COLECCIONES
List(1,2,3).map(_ * 2)           // [2, 4, 6] - transform
List(1,2,3).filter(_ > 1)        // [2, 3] - select
List(1,2,3).fold(0)(_ + _)       // 6 - reduce
List("a","b").flatMap(s => List(s, s.toUpperCase))  // ["a", "A", "b", "B"]

// CASE CLASS Y PATTERN MATCHING
case class Persona(nombre: String, edad: Int)
val p = Persona("Juan", 30)

p match {
  case Persona(n, e) if e > 18 => println(s"$n es adulto")
  case _ => println("otro")
}

// STRING FORMATTING
val valor = 3.14159
valor.formatted("%.2f")  // "3.14"
s"Texto con $variable"
```

## Spark RDD

```scala
val rdd = sc.parallelize(List(1,2,3,4,5))

// TRANSFORMACIONES (lazy)
rdd.map(_ * 2)                    // aplica función
rdd.filter(_ > 2)                 // selecciona
rdd.flatMap(x => List(x, x+1))    // aplanador
rdd.reduceByKey((a,b) => a + b)   // agregación por clave
rdd.groupByKey()                  // agrupa por clave
rdd.sortBy(x => x)                // ordenra

// ACCIONES (ejecutan)
rdd.collect()     // trae todo al driver
rdd.count()       // cuenta elementos
rdd.first()       // primer elemento
rdd.take(3)       // primeros N
rdd.sum()         // suma
rdd.saveAsTextFile("path")
```

## Spark DataFrame + SQL

```scala
// LECTURA
val df = spark.read.format("csv").option("header", "true").load("path")
val df = spark.read.parquet("path")
val df = spark.read.json("path")

// VISTAS
df.createOrReplaceTempView("tabla1")
df.createOrGlobalTempView("tabla2")

// QUERIES
spark.sql("SELECT * FROM tabla1 WHERE edad > 18")

// OPERACIONES
df.select("col1", "col2")
df.where(col("edad") > 18)
df.groupBy("categoria").agg(sum("monto"))
df.join(df2, df.id === df2.id)
df.orderBy(desc("precio"))

// ESCRITURA
df.write.format("csv").mode("overwrite").save("path")
df.write.parquet("path")
df.write.partitionBy("fecha").parquet("path")
```

## Window Functions (SQL)

```sql
-- Ranking
ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)
RANK() OVER (ORDER BY monto DESC)
DENSE_RANK() OVER (ORDER BY monto)

-- Acceso a filas cercanas
LAG(columna) OVER (ORDER BY ...)    -- fila anterior
LEAD(columna) OVER (ORDER BY ...)   -- fila siguiente
FIRST_VALUE(columna) OVER (ORDER BY ...)
LAST_VALUE(columna) OVER (ORDER BY ...)

-- Cuantiles
PERCENT_RANK() OVER (ORDER BY precio)
NTILE(4) OVER (ORDER BY precio)  -- 0-25%, 25-50%, etc

-- Agregaciones con ventana
SUM(monto) OVER (PARTITION BY usuario ORDER BY fecha)
AVG(monto) OVER (PARTITION BY categoria)
COUNT(*) OVER (ORDER BY fecha ROWS BETWEEN 7 PRECEDING AND CURRENT ROW)
```

## Kafka

```bash
# CREAR TOPIC
kafka-topics.sh --create --bootstrap-server localhost:9092 \
  --topic mi_topic --partitions 3 --replication-factor 1

# LISTAR TOPICS
kafka-topics.sh --list --bootstrap-server localhost:9092

# DESCRIBIR TOPIC
kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic mi_topic

# PRODUCTOR
kafka-console-producer.sh --broker-list localhost:9092 --topic mi_topic

# CONSUMIDOR
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mi_topic --from-beginning

# CONSUMIDOR CON CLAVE
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic mi_topic --property "print.key=true" --from-beginning

# BORRAR TOPIC
kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic mi_topic
```

## Common SQL Patterns

```sql
-- AGREGACIÓN BÁSICA
SELECT categoria, COUNT(*) as cantidad, SUM(monto) as total
FROM ventas
GROUP BY categoria

-- FILTRAR DESPUÉS DE AGREGAR
SELECT categoria, SUM(monto) as total
FROM ventas
GROUP BY categoria
HAVING SUM(monto) > 1000

-- RANKING
SELECT *, RANK() OVER (ORDER BY monto DESC) as posicion
FROM ventas

-- PERCENTILES
SELECT usuario, gasto, 
       PERCENT_RANK() OVER (ORDER BY gasto) as percentil
FROM usuarios

-- PROMEDIOS MÓVILES
SELECT fecha, monto,
       AVG(monto) OVER (ORDER BY fecha ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as media_7d
FROM ventas

-- TOP N POR GRUPO
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY categoria ORDER BY precio DESC) as rank
  FROM productos
)
SELECT * FROM ranked WHERE rank <= 3
```

## File Handling en Scala

```scala
// LECTURA COMPLETA
val contenido = scala.io.Source.fromFile("archivo.txt").mkString

// LECTURA LÍNEA POR LÍNEA
val lineas = scala.io.Source.fromFile("archivo.txt").getLines().toList

// ESCRITURA
val writer = new java.io.PrintWriter("archivo.txt")
writer.println("línea 1")
writer.println(s"valor: ${variable}")
writer.close()

// WRITERS SEGUROS (se cierran automáticamente)
val writer = new java.io.PrintWriter("archivo.txt")
try {
  writer.println("contenido")
} finally {
  writer.close()
}
```

## Debugging Tips

```scala
// IMPRIMIR DURANTE SPARK
df.show()           // primeras 20 filas
df.show(100)        // primeras 100
df.printSchema()    // esquema

// CONTAR
df.count()

// COLUMNAS
df.columns          // names
df.select().columns // selected columns

// FILTRADO SIMPLE
df.filter(col("edad") > 18).show()

// PEEK - función para ver datos en la tubería
df.map { x => println(x); x }
```

## Formatos de Archivo

| Formato | Ventajas | Desventajas |
|---------|----------|------------|
| CSV     | Legible, portable | Lento, serialización ineficiente |
| JSON    | Flexible, sem ilegible | Lento, sin compresión nativa |
| Parquet | Rápido, columnar, comprimido | Menos legible |
| Avro    | Serialización eficiente | Menos común en analytics |

## Optimizaciones Spark

```scala
// BROADCAST (tabla pequeña)
val smallDF = ... // < 100MB
val broadcasted = spark.broadcast(smallDF.collect())

// REPARTICIÓN
df.repartition(200)  // más particiones
df.coalesce(10)      // menos particiones

// CACHING
df.cache()           // en memoria
df.persist()         // más control
df.unpersist()       // liberar

// SQL HINTS
SELECT /*+ BROADCAST(pequeño) */ * FROM grande
JOIN pequeño ON ...
```

## Errores Comunes

| Problema | Causa | Solución |
|----------|------|----------|
| "Column not found" | Nombre diferente | Chequea `df.columns` |
| "OutOfMemory" | Dataset muy grande | Usa `coalesce()`, particiona |
| "File not found" | Path incorrecto | Check `hdfs dfs -ls /ruta` |
| "NullPointerException" | Null sin manejo | Usa `.na.fill()` o `.filter(x.isNotNull)` |
| "Type mismatch" | Tipo incorrecto | Cast con `.cast("IntegerType")` |

---

## Template Rápido para Ejercicio 1

```scala
// MODO INTERACTIVO (copy-paste)
import scala.io.Source
import java.io.PrintWriter

val ficheroEntrada = "entrada.txt"
val ficheroSalida1 = "output1.txt"

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(campo1, campo2) = linea.split(",")
  // TRANSFORMAR AQUÍ
  (campo1, resultado)
}.filter { case (_, valor) => valor > UMBRAL }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (a, b) =>
  writer1.println(s"$a,$b")
}
writer1.close()

// MODO COMPILADO: rodea con object, encapsula en main()
```

---

**Usa este sheet como referencia durante el examen cuando no recuerdes la sintaxis exacta.**
