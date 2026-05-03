# AEC4 - Transformaciones en Scala

![image.png](attachment:1b841401-ac06-4cf0-92e6-0c041136b3dc:image.png)

## Introducción

En esta actividad se nos pedía realizar un análisis de un dataset de películas usando Apache Spark. El objetivo principal era demostrar competencias con RDDs y con DataFrames, además de implementar un conector JDBC a PostgreSQL para conectar Spark con una base de datos real.

La actividad tiene dos partes bien diferenciadas. En la primera parte hago un análisis usando RDDs y DataFrames donde cargo los datos como RDD, aplico transformaciones, convierto a DataFrame, hago análisis exploratorio, trabajo con conversiones bidireccionales, y finalmente resuelvo varios problemas usando SQL y funciones personalizadas. En la segunda parte conecto Spark con PostgreSQL a través de JDBC y ejecuto queries directamente desde SQL.

## Selección del Dataset

Para esta práctica me he decantado por un dataset que usé en otro proyecto de películas porque es un dominio interesante para análisis de negocio creo que podemos sacar muchas areas como rentabilidad, géneros populares, presupuestos vs ingresos, etc. El dataset que generé tiene 250 películas con 10 columnas, lo que cumple ampliamente con los requisitos de más de 200 registros y 7 columnas mínimo.

Las columnas que incluí son `id` (INT), `title` (STRING), `release_date` (STRING), `budget` (LONG), `revenue` (LONG), `runtime` (INT), `genre` (STRING), `vote_average` (DOUBLE), `popularity` (DOUBLE), y `cast_size` (INT). El archivo `movies.csv` está en esta misma carpeta (vease el repo de github ya que en la entrega no ha sido subido) y contiene 250 películas con datos realistas que permiten hacer análisis significativos.

## PARTE 1: Análisis con RDD y DataFrame

### Flujo

Para esta parte del trabajo, mi estrategia fue la siguiente, primero cargo el CSV como RDD (la estructura más básica), luego aplico transformaciones para limpiar y parsear los datos, convierto a DataFrame para usar herramientas un poco mas decentes, hago análisis exploratorio, en ambas direcciones (DF→RDD→DF), y finalmente como indicaba el profe resuelvo varios problemas de negocio usando queries SQL y funciones personalizadas (de libre diseño).

### Paso 1: Iniciar Spark Shell y cargar datos

Para comenzar como siempre, abrimos Spark Shell en la terminal:

```bash
spark-shell
```

Una vez dentro, creo sesión con Spark e importo las librerías que voy a necesitar:

```scala
import org.apache.spark.sql.{SparkSession, RDD, Row}
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import scala.io.Source
```

Ahora cargo el archivo CSV como RDD. Lo importante aquí es que un RDD es una colección distribuida de elementos “cruda” - Spark no entiende estructuras, simplemente lee línea a línea:

```scala
val filePath = "/home/nirmata/Documentos/University/U-Tad/3th_Course/Q2/Data_Procesing/Unit_4/AEC4/movies.csv"
val rawRDD = spark.sparkContext.textFile(filePath)
```

Verifico que se cargó correctamente:

```scala
println(s"Número de particiones:${rawRDD.getNumPartitions}")
println(s"Total de líneas:${rawRDD.count()}")
rawRDD.first()
```

El resultado:

![image.png](attachment:be204c6f-ba81-486e-82a1-5e03726ec36a:image.png)

La razón por la que tengo 251 líneas es que el CSV tiene 250 películas más 1 línea de encabezado. Spark automáticamente dividió el RDD en 2 particiones para poder procesarlo en paralelo.

### Paso 2: Transformaciones en RDD - Limpieza y Parsing

Ahora viene la parte considero mas complicada, transformar las líneas de texto en datos estructurados. Un RDD es muy flexible pero muy manual por lo que tenemos que decirle exactamente cómo interpretar cada campo.

Primero identifico y elimino el header:

```scala
val filePath = "/home/nirmata/Documentos/University/U-Tad/3th_Course/Q2/Data_Procesing/Unit_4/AEC4/movies.csv"
val rawRDD = spark.sparkContext.textFile(filePath)
val header = rawRDD.first()
```

Ahora aplico las transformaciones. Esto es lo que me parece que hace a Spark realmente potente ya que con map(), filter() y split() puedo procesar todo en paralelo:

```scala
val dataRDD = rawRDD
  .filter(_ != header)
  .map(line => {
    val fields = line.split(",")
    (
      fields(0).toInt,
      fields(1),
      fields(2),
      fields(3).toLong,
      fields(4).toLong,
      fields(5).toInt,
      fields(6),
      fields(7).toDouble,
      fields(8).toDouble,
      fields(9).toInt
    )
  })
  .cache()
```

Cada línea se divide por comas y se convierte a los tipos correctos. El `.cache()` al final es una optimización que le dice a Spark que guarde este RDD en memoria porque lo voy a usar varias veces.

Verifico que las transformaciones funcionaron:

```scala
println(s"Total registros después de transformar:${dataRDD.count()}")
dataRDD.take(3).foreach(println)
```

Resutlado:

![image.png](attachment:ca4eed95-e297-4a05-be35-535ee25a3da0:image.png)

### Paso 3: Convertir RDD a DataFrame

Para hacer análisis es mucho mejor convertir el RDD a un DataFrame, que es como una tabla SQL estructurada. Spark optimiza automáticamente las queries sobre DataFrames, hace que sea más fácil escribir código, y permite usar SQL directo.

```scala
val dfMovies = dataRDD.toDF(
  "id", "title", "release_date", "budget", "revenue",
  "runtime", "genre", "vote_average", "popularity", "cast_size"
)
.cache()

println("DataFrame creado exitosamente")
```

Con `.toDF()` convierto el RDD en un DataFrame y asigno nombres a las columnas. Nuevamente uso `.cache()` para mantenerlo en memoria.

![image.png](attachment:6038c186-808f-4862-9fde-bb60632d272d:image.png)

### Paso 4: Exploración de Metadatos

Antes de hacer análisis real, necesito entender la estructura de los datos. Primero veo el esquema:

```scala
println("\n=== ESQUEMA QUE TENEMOS ===")
dfMovies.printSchema()
```

Esto me muestra un árbol con el nombre de cada columna, su tipo, y si puede ser nulo:

![image.png](attachment:82368933-b86a-4155-b824-ec16f01677c6:image.png)

Luego miro una muestra de los datos reales:

```scala
println("\n=== MUESTRA DE DATOS (Primeros 5) ===")
dfMovies.show(5, truncate = false)
```

![image.png](attachment:7075a82d-d3b9-4c11-8568-155199d207fd:image.png)

Y obtengo información general:

```scala
println("\n=== INFORMACIÓN GENERAL ===")
println(s"Total de registros:${dfMovies.count()}")
println(s"Total de columnas:${dfMovies.columns.length}")
println(s"Nombres de columnas:${dfMovies.columns.mkString(", ")}")
println(s"Registros únicos:${dfMovies.dropDuplicates().count()}")
```

![image.png](attachment:5ea4921f-cffc-416a-abf8-e06c2af04abb:image.png)

### Paso 5: Análisis Exploratorio

Ahora que tengo los datos, hago un análisis básico para detectar patrones y problemas. Primero veo estadísticas generales:

```scala
println("\n=== ESTADÍSTICAS BÁSICAS ===")
dfMovies.describe("budget", "revenue", "runtime", "vote_average", "popularity", "cast_size").show()
```

![image.png](attachment:33654045-3437-45b0-9541-4554808e7e88:image.png)

Esto me da count, mean, stddev, min, max de cada columna numérica. Es muy útil para saber si hay values raros o si la distribución es normal o está sesgada.

Luego detecto nulos (valores perdidos):

```scala
println("\n=== DETECCIÓN DE NULOS ===")
dfMovies.select(dfMovies.columns.map(c => 
  sum(when(col(c).isNull, 1).otherwise(0)).as(c)
): _*).show()
```

Este query es un poco complejo pero lo que hace es contar cuantos nulos hay en cada columna. Si tengo muchos nulos en una columna, sé que necesito hacer limpieza, pero en este dataset no había ni un solo valor nulo. 

![image.png](attachment:d489541c-cfa1-4778-a517-6a3e42afb719:image.png)

Además de esto, decidí incluir un análisis de cuartiles (percentiles) como hemos hecho en otras asignaturas porque es una técnica más sofisticada que simplemente mide media/desviación. Los cuartiles me permiten basicamente entender cómo están distribuidos los datos en la realidad:

```scala
println("\n=== ANÁLISIS DE CUARTILES ===")

val revenuePercentiles = dfMovies.stat.approxQuantile(
  "revenue", 
  Array(0, 0.25, 0.5, 0.75, 1.0), 
  0.05
)

println(s"Distribución de Ingresos:")
println(s"Mínimo (0%):        ${revenuePercentiles(0).toLong}")
println(s"Q1 (25%):           ${revenuePercentiles(1).toLong}")
println(s"Mediana (50%):      ${revenuePercentiles(2).toLong}")
println(s"Q3 (75%):           ${revenuePercentiles(3).toLong}")
println(s"Máximo (100%):      ${revenuePercentiles(4).toLong}")
```

Los cuartiles me muestran que el 25% de las películas generan menos de X dólares, la mediana es Y, etc. Esto es mucho más informativo que solo la media porque no se distorsiona con valores extremos (outliers).

![image.png](attachment:4a15be3f-5f22-4100-86ec-3dd3027fd42b:image.png)

### Paso 6: Conversión Bidireccional DataFrame ↔︎ RDD

Una parte importante del requisito es demostrar la conversión entre RDD y DataFrame en ambas direcciones. Primero convierto el DataFrame a RDD:

```scala
println("\n=== CONVERSIÓN DATAFRAME → RDD ===")
val rddFromDF = dfMovies.rdd
println(s"Tipo de elementos en RDD:${rddFromDF.first().getClass}")
```

![image.png](attachment:9ccc566d-8fc1-4fe8-a5e4-182a2acd3c1e:image.png)

Ahora que tengo un RDD puedo hacer transformaciones complejas que no son fáciles con DataFrame API. Por ejemplo, filtro películas muy rentables y creo una descripción personalizada:

```scala
val highRevenueRDD = rddFromDF
  .filter(row => row.getAs[Long]("revenue") > 1000000000)
  .map(row => {
    val title = row.getAs[String]("title")
    val revenue = row.getAs[Long]("revenue")
    val rating = row.getAs[Double]("vote_average")
    s"$title - Revenue: ${revenue/1000000}M - Rating: $rating/10"
  })

println(s"Películas con Revenue > $$1B: ${highRevenueRDD.count()}")
println("\nEjemplos:")
highRevenueRDD.take(5).foreach(println)

println("\n=== VUELVO A CONVERTIR A DATAFRAME ===")
val dfHighBudget = rddFromDF
  .filter(row => row.getAs[Long]("budget") > 150000000)
  .toDF()

println(s"Películas con presupuesto > $$150M: ${dfHighBudget.count()}")
dfHighBudget.select("title", "budget", "revenue").show(5, truncate = false)val filePath = "/home/nirmata/Documentos/University/U-Tad/3th_Course/Q2/Data_Procesing/Unit_4/AEC4/movies.csv"
val rawRDD = spark.sparkContext.textFile(filePath)val filePath = "/home/nirmata/Documentos/University/U-Tad/3th_Course/Q2/Data_Procesing/Unit_4/AEC4/movies.csv"
val rawRDD = spark.sparkContext.textFile(filePath)
```

Una vez que hago las transformaciones en RDD, convierto de vuelta a DataFrame para continuar:

```scala
println("\n=== VUELVO A CONVERTIR A DATAFRAME ===")
val dfHighBudget = rddFromDF
  .filter(row => row.getAs[Long]("budget") > 150000000)
  .toDF()

println(s"Películas con presupuesto >$150M:${dfHighBudget.count()}")
dfHighBudget.select("title", "budget", "revenue").show(5, truncate = false)
```

Por qué es importante saber convertir en ambas direcciones: un RDD es más bajo nivel y me da más control para transformaciones raras, pero un DataFrame es mucho más eficiente para análisis SQL. En la práctica real, cambio entre uno y otro según lo que necesito hacer.

![image.png](attachment:b1b992ee-30d4-4a48-ac0e-7ef5100f39c0:image.png)

### Paso 7: Queries Avanzadas y Funciones Personalizadas

Ahora resuelvo varios problemas de negocio. Primero registro el DataFrame como tabla temporal para poder usarla en SQL:

```scala
dfMovies.createOrReplaceTempView("movies")
```

**Query 1: Películas de Acción Premium**

Esta query busca películas que tienen buena calidad (rating alto), presupuesto grande, y son de acción. El negocio quiere saber cuáles son sus “big bets” en acción y si pagó bien:

```scala
println("\n=== QUERY 1: Películas de Acción con Presupuesto > $100M y Rating > 6 ===")
dfMovies
  .filter(col("genre") === "Action" && col("budget") > 100000000 && col("vote_average") > 6.0)
  .select("title", "budget", "revenue", "vote_average")
  .orderBy(desc("revenue"))
  .show(10, truncate = false)
```

La lógica es simple: filter por condicionales múltiples, selecciono columnas relevantes, ordeno por ingresos más altos.

![image.png](attachment:d21c8cd4-52e1-4239-9aa6-0923d98f1811:image.png)

**Query 2: Análisis por Género y Año**

Quiero ver cómo se comportan los diferentes géneros por año. ¿El drama está mejorando? ¿La acción tiene presupuestos más altos? Para esto hago una agrupación múltiple:

```scala
println("\n--- QUERY 2: Análisis por Género y Año ---")
dfMovies
  .withColumn("year", year(col("release_date")))
  .groupBy("genre", "year")
  .agg(
    count("*").as("num_peliculas"),
    avg("revenue").as("ingresos_promedio"),
    max("revenue").as("ingresos_max"),
    min("budget").as("presupuesto_minimo")
  )
  .filter(col("num_peliculas") > 2)
  .orderBy(desc("ingresos_promedio"))
  .show(20, truncate = false)
```

Lo interesante aquí es que extraigo el año de la fecha, luego agrupo por dos columnas (género Y año), calculo múltiples agregaciones, filtro solo años con suficientes películas, y ordeno.

![image.png](attachment:f63f7859-973c-4d62-a2e9-ec6ae9a0d433:image.png)

**Query 3: ROI por Género (usando SQL)**

Aquí uso SQL directo en lugar de DataFrame API. Me parece que SQL es más legible aquí porque tengo operaciones aritméticas complejas (ROI = (Revenue-Budget)/Budget*100):

```scala
println("\n--- QUERY 3: Top Géneros por ROI (SQL) ---")
spark.sql("""
  SELECT
    genre,
    COUNT(*) as num_peliculas,
    ROUND(AVG(revenue - budget) / AVG(budget) * 100, 2) as roi_promedio_percent,
    ROUND(AVG(revenue), 0) as ingresos_promedio,
    ROUND(AVG(vote_average), 2) as calificacion_promedio
  FROM movies
  GROUP BY genre
  ORDER BY roi_promedio_percent DESC
""").show(truncate = false)
```

El ROI es importante porque me dice cuál es el retorno real de la inversión: no es lo mismo un género que gana 500M que uno que gana 500M pero solo invirtió 100M.

![image.png](attachment:f477bd08-d600-4889-ab00-b7daa3962956:image.png)

**Query 4: UDF - Clasificador Personalizado de Rentabilidad**

Aquí defino mi propia función (User Defined Function) que Spark no conoce, y la aplico al DataFrame. Esto es muy útil cuando la lógica es demasiado compleja para expresarla en SQL:

```scala
println("\n=== QUERY 4: Clasificación de Películas por Rentabilidad (UDF Personalizado) ===")

val classifyRentability = udf((budget: Long, revenue: Long) => {
  if (budget == 0) "N/A"
  else {
    val roi = (revenue - budget).toDouble / budget
    if (roi > 5.0) "Extremadamente Rentable (ROI > 500%)"
    else if (roi > 2.0) "Muy Rentable (ROI > 200%)"
    else if (roi > 1.0) "Rentable (ROI > 100%)"
    else if (roi > 0.0) "Moderadamente Rentable"
    else "No Rentable (Pérdidas)"
  }
})

val rentabilityAnalysis = dfMovies
  .withColumn("rentability_class", classifyRentability(col("budget"), col("revenue")))
  .groupBy("rentability_class")
  .agg(
    count("*").as("cantidad"),
    round(avg("revenue"), 0).as("ingresos_promedio")
  )
  .orderBy(desc("cantidad"))

println("Distribución de películas por rentabilidad:")
rentabilityAnalysis.show(truncate = false)
```

La función toma presupuesto e ingresos, calcula ROI, y devuelve una categoría. Luego puedo usar esa nueva columna en operaciones normales como groupBy.

![image.png](attachment:7ea9fe07-2905-4c23-b365-2d975785f677:image.png)

**Query 5: Análisis de Popularidad por Género (UDAF)**

UDAF es como un UDF pero para agregaciones. En este caso uso SQL con funciones de agregación avanzadas como PERCENTILE_APPROX:

```scala
println("\n=== QUERY 5: Análisis de Popularidad por Género (UDAF) ===")
spark.sql("""
  SELECT
    genre,
    ROUND(AVG(popularity), 2) as popularidad_promedio,
    MAX(popularity) as popularidad_maxima,
    MIN(popularity) as popularidad_minima,
    PERCENTILE_APPROX(popularity, 0.5) as mediana_popularidad,
    COUNT(DISTINCT title) as num_peliculas
  FROM movies
  GROUP BY genre
  ORDER BY popularidad_promedio DESC
""").show(truncate = false)
```

Esto me muestra distribuciones completas de popularidad por género, incluyendo la mediana.

![image.png](attachment:e16e384d-e20a-4dbd-adb7-2ee92823892f:image.png)

## PARTE 2: Conector JDBC a PostgreSQL

En la segunda parte de la práctica trabajo con un conector JDBC para leer datos desde una base de datos PostgreSQL real. Este es un paso importante porque en el mundo real, especialmente en empresas grandes, los datos no están en archivos CSV sino en bases de datos relacionales. Spark integra con cualquier BD mediante JDBC (Java Database Connectivity), que es un estándar de Java.

### Verificación de PostgreSQL

Lo primero que hago es verificar que PostgreSQL está corriendo en mi máquina. Esto lo compruebo desde otra terminal:

```bash
sudo systemctl status postgresql
```

y verifico que puedo conectarme y que la tabla que voy a usar existe:

```bash
sudo -u postgres psql -c "SELECT * FROM mytable;"
```

Lo cual me devuelve que el servicio esta activo y la tabla la tenemos preparada:

![image.png](attachment:8916c142-2dd5-437e-8c54-e394bcf66db9:image.png)

### Iniciar Spark con el Driver JDBC

Aquí es importante debo abrir una NUEVA sesión de Spark que incluya el JDBC driver para PostgreSQL. El driver que descargué (`postgresql-42.7.1.jar`) tiene el código necesario para que Spark hable con PostgreSQL.

```bash
spark-shell --jars ~/Descargas/postgresql-42.7.1.jar
```

El flag `--jars` le dice a Spark que incluya ese archivo JAR en el classpath.

### Configurar conexión JDBC

Una vez dentro de Spark Shell, importo la clase Properties que uso para las credenciales:

```scala
import java.util.Properties
```

Ahora configuro las propiedades de conexión:

```scala
val props = new Properties()
props.setProperty("user", "postgres")
props.setProperty("driver", "org.postgresql.Driver")
props.setProperty("password", "postgres")

println("Propiedades JDBC configuradas")
```

Estos Properties contienen:
- `user`: El usuario de PostgreSQL (postgres)
- `driver`: El driver JDBC a usar (el de PostgreSQL)
- `password`: La contraseña (en mi servidor de prueba es “postgres”)

![image.png](attachment:17981e34-a3e1-4f5b-a2af-0c3911b2f898:image.png)

### Leer datos desde PostgreSQL con Spark

Aquí es donde ocurre la magia: creo un DataFrame leyendo directamente desde PostgreSQL:

```scala
println("\n=== LEYENDO DATOS DESDE POSTGRESQL ===")

val jdbcDF = spark.read.jdbc(
  "jdbc:postgresql://localhost:5432/postgres",
  "mytable",
  props
)

println("DataFrame creado desde PostgreSQL")
println("\nContenido:")
jdbcDF.show()
```

Lo que hace:
- `spark.read.jdbc()` es el método que usa Spark para conectar a cualquier BD relacional
- La URL JDBC especifica el servidor (localhost), en el puerto (5432), BD (postgres)
- `"mytable"` es el nombre de la tabla que quiero leer
- `props` contiene las credenciales

El resultado:

![image.png](attachment:d8e79314-2bdb-4e0b-84f4-f237722923aa:image.png)

### Crear tabla Spark mapeada a PostgreSQL

Además de solo leer datos puntuales, puedo crear una tabla en Spark que está mapeada directamente a PostgreSQL. Esto significa que cada vez que hago una query sobre esa tabla, Spark automáticamente se conecta a PostgreSQL y ejecuta la query allá:

```scala
spark.sql("""
  CREATE TABLE pgtable USING jdbc OPTIONS (
    url 'jdbc:postgresql://localhost:5432/postgres',
    driver 'org.postgresql.Driver',
    user 'postgres',
    password 'postgres',
    dbtable 'mytable'
  )
""")

println("Tabla 'pgtable' creada exitosamente")
```

Ahora que tengo esta tabla definida, puedo usarla como una tabla normal de Spark:

```scala
spark.sql("SELECT * FROM pgtable").show()
```

![image.png](attachment:836b09ac-b869-4487-acd8-384139268d83:image.png)

### Queries SQL complejas con JDBC

Una vez que tengo la tabla mapeada, puedo hacer queries SQL complejas. Por ejemplo, quiero identificar módulos de alta calidad (rating >= 8) y clasificarlos:

```scala
val createTableQuery = """
  CREATE TABLE IF NOT EXISTS high_quality_modules AS
  SELECT
    id,
    name,
    rating,
    CASE
      WHEN rating >= 9.0 THEN 'Excelente'
      WHEN rating >= 8.0 THEN 'Muy Bueno'
      ELSE 'Bueno'
    END as quality_category
  FROM pgtable
  WHERE rating >= 8.0
  ORDER BY rating DESC
"""

spark.sql(createTableQuery)
println("Tabla de alta calidad creada")

spark.sql("SELECT id, name, rating, CASE WHEN rating >= 9.0 THEN 'Excelente' WHEN rating >= 8.0 THEN 'Muy Bueno' ELSE 'Bueno' END as quality_category FROM pgtable WHERE rating >= 8.0 ORDER BY rating DESC").show(truncate = false)
```

Lo interesante aquí es la sentencia CASE WHEN: esto me permite hacer clasificaciones condicionales (si rating >= 9 entonces “Excelente”, si >= 8 entonces “Muy Bueno”, etc.).

![image.png](attachment:606d0b8f-dcbd-432a-8239-c9890fcc272e:image.png)

### Análisis Detallado con Agregaciones

Para un resumen ejecutivo más completo, hago una query con múltiples agregaciones usando UNION ALL:

```scala
val summaryQuery = """
  SELECT
    'Total de módulos' as Metrica,
    CAST(COUNT(*) as STRING) as Valor
  FROM pgtable
  UNION ALL
  SELECT
    'Módulos de alta calidad (>=8)',
    CAST(COUNT(*) as STRING)
  FROM pgtable
  WHERE rating >= 8.0
  UNION ALL
  SELECT
    'Módulos de baja calidad (<8)',
    CAST(COUNT(*) as STRING)
  FROM pgtable
  WHERE rating < 8.0
  UNION ALL
  SELECT
    'Rating promedio',
    CAST(ROUND(AVG(rating), 2) as STRING)
  FROM pgtable
  UNION ALL
  SELECT
    'Rating máximo',
    CAST(MAX(rating) as STRING)
  FROM pgtable
  UNION ALL
  SELECT
    'Rating mínimo',
    CAST(MIN(rating) as STRING)
  FROM pgtable
"""

spark.sql(summaryQuery).show(truncate = false)
```

Este patrón con UNION ALL me permite combinar múltiples SELECT en una sola tabla. Cada SELECT calcula una métrica diferente, y todas se presentan juntas. Es mucho mejor que ejecutar 6 queries separadas porque:
1. Una sola conexión a la BD
2. Más eficiente
3. El resultado es más fácil de leer

![image.png](attachment:743705db-0fbe-462f-baa0-615e63e3d9a2:image.png)

## RDD vs DataFrame

Un RDD es la abstracción más baja. Es una colección distribuida de objetos que puedo manipular de forma muy flexible. Lo bueno de los RDDs es que tengo control total: puedo hacer transformaciones arbitrarias, trabajar con datos semiestructurados, y resolver problemas complejos. Lo malo es que tengo que escribir mucho código y Spark no puede optimizar automáticamente las operaciones.

En contraste, los DataFrames son tablas estructuradas donde cada columna tiene un tipo. Spark entiende mejor que es un DataFrame (porque ve la estructura), por lo que puede optimizar automáticamente las operaciones. Las queries en DataFrame también se traducen a SQL internamente, lo que las hace más rápidas. El tradeoff es que tengo menos flexibilidad: solo puedo hacer operaciones que Spark soporta.