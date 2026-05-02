# AEC4 - Spark SQL: DataFrames, RDDs y Conectores en Scala

En esta actividad voy a mostrar cómo trabajar con Spark en Scala, desde lo básico (crear un DataFrame de una lista) hasta operaciones más avanzadas (conversión entre RDD y DataFrame, consultas SQL, conexiones a PostgreSQL).

Todos los ejemplos se ejecutan en **modo local** en una máquina virtual con Spark ya configurado.

## Estructura del proyecto

```
AEC4/
├── data/
│   └── datos_peliculas.csv       # Dataset con 500+ películas (7 columnas, tipos diversos)
├── src/
│   ├── Ejercicio0.scala          # Descarga de datos con wget (preparación)
│   ├── Ejercicio1.scala          # DataFrame desde una lista de Scala
│   ├── Ejercicio2.scala          # DataFrame con esquema manual (StructType)
│   ├── Ejercicio3.scala          # Lectura de CSV con opciones personalizadas
│   ├── Ejercicio4.scala          # Exploración: esquema, estadísticas, nulos
│   ├── Ejercicio5.scala          # Conversión DataFrame → RDD con transformaciones
│   ├── Ejercicio6.scala          # Consultas SQL vs API de Spark
│   ├── Ejercicio7.scala          # DataFrame → RDD → DataFrame completo
│   ├── Ejercicio8.scala          # Problema analítico con UDF y groupBy avanzado
│   ├── Ejercicio9.scala          # Conexión JDBC a PostgreSQL (setup + básico)
│   ├── Ejercicio10.scala         # Queries propias en PostgreSQL
│   └── setup_postgres.sh          # Script de instalación de PostgreSQL
└── README.md
```

---

## Descripción de los ejercicios

### Ejercicio 0 — Descarga de datos con wget

Aquí explico cómo descargar un dataset desde internet usando `wget`. El archivo que uso es un dataset de películas desde Kaggle (o similar). 

```bash
# Descargar el CSV a la carpeta data/
wget -O data/datos_peliculas.csv https://url-del-dataset.com/peliculas.csv

# Verificar que se descargó correctamente
wc -l data/datos_peliculas.csv
head -5 data/datos_peliculas.csv
```

**Por qué esto importa:** En un proyecto real, los datos vienen de fuentes externas. Necesito saber cómo traerlos a mi máquina antes de procesarlos con Spark.

#### Dataset elegido: Películas
- **Registros:** 500+
- **Columnas:** id, titulo, año, director, genero, presupuesto, ingresos
- **Tipos de datos:** Int, String, Double
- **Por qué:** Es un dataset suficientemente complejo para mostrar transformaciones reales y detectar problemas (valores nulos en presupuesto/ingresos, años inconsistentes, etc.).

---

### Ejercicio 1 — DataFrame desde una lista de Scala

La forma más simple de crear un DataFrame es a partir de datos que ya tengo en memoria. Aquí creo una `Seq` de tuplas y la convierto directamente a DataFrame.

```scala
val empleadosLista = Seq(
  (1, "Ana",    29, "Ventas",    42000.0),
  (2, "Pedro",  34, "Marketing", 39000.0),
  ...
)

val dfEmpleados = empleadosLista.toDF("id", "nombre", "edad", "departamento", "salario")
```

**Lo importante:** Spark infiere los tipos automáticamente. Si tengo Int, String, Double en mis tuplas, el DataFrame lo sabe sin que yo lo indique explícitamente.

---

### Ejercicio 2 — DataFrame con esquema manual

A veces *no* quiero dejar que Spark adivine los tipos. Quiero control total. Por eso defino el esquema explícitamente con `StructType` y `StructField`.

```scala
val esquema = StructType(Array(
  StructField("id",           IntegerType, nullable = false),
  StructField("nombre",       StringType,  nullable = false),
  StructField("edad",         IntegerType, nullable = false),
  StructField("departamento", StringType,  nullable = false),
  StructField("salario",      DoubleType,  nullable = false)
))

val dfConEsquema = spark.createDataFrame(
  spark.sparkContext.parallelize(filas),
  esquema
)
```

**Por qué lo hago:** Así controlo si las columnas permiten valores nulos, los tipos exactos, etc. Es importante cuando integro datos de fuentes heterogéneas.

---

### Ejercicio 3 — Lectura de CSV con configuraciones

Cuando leo datos de un archivo CSV, necesito decirle a Spark cómo interpretarlo. Aquí especifico el delimitador, si la primera fila es header, y que deduzca tipos automáticamente.

```scala
val dfCsv = spark.read
  .option("header",      "true")      // Primera fila = nombres de columna
  .option("sep",         ";")         // Delimitador es punto y coma
  .option("inferSchema", "true")      // Deduce tipos de datos
  .option("mode",        "DROPMALFORMED") // Descarta filas rotas
  .csv("data/datos_peliculas.csv")
```

**En la práctica:** Si no indico `sep`, Spark asume coma y falla. Si no indico `header=true`, los nombres de columna serán `_1`, `_2`, etc. Pequeños detalles que rompen todo.

---

### Ejercicio 4 — Exploración: esquema, estadísticas, valores nulos

Una vez que tengo el DataFrame cargado, ¿qué hago? Lo primero es **mirarlo**. Necesito saber qué contiene, cuántas filas, qué tipos, y si hay datos faltantes (nulos).

```scala
df.show(10, truncate = false)        // Primeras 10 filas
df.printSchema()                      // Árbol de tipos
df.columns                            // Nombres de columnas
df.count()                            // Número total

df.describe("presupuesto", "ingresos").show()  // Estadísticas (min, max, media, etc.)

// Detección de nulos
df.select(df.columns.map(c => count(when(col(c).isNull, 1)).alias(c)): _*).show()
```

**Lo que veo:** Con `describe()` sé el rango de datos. Con la detección de nulos veo si hay películas sin presupuesto o ingresos registrados.

---

### Ejercicio 5 — Conversión DataFrame → RDD con transformaciones

Un DataFrame es "alto nivel" y fácil de usar. Un RDD es "bajo nivel" pero muy flexible. A veces necesito trabajar con RDD para aplicar transformaciones rápidas o acceder a particiones.

```scala
val rddEmpleados = df.rdd.map(row => (
  row.getAs[Int]("id"),
  row.getAs[String]("nombre"),
  row.getAs[String]("departamento"),
  row.getAs[Double]("salario")
))

// Una transformación: filtrar por salario
val filtrado = rddEmpleados.filter { case (_, _, _, salario) => salario > 45000 }
```

**Por qué:** Spark puede optimizar mejor un RDD con transformaciones simples que un DataFrame en ciertos casos. Y el RDD me da acceso directo a `.collect()` y otras operaciones "raw".

---

### Ejercicio 6 — Consultas SQL vs API de Spark

Aquí muestro que **puedo hacer lo mismo de dos formas**: con SQL (para los que vienen de bases de datos) o con la API de DataFrames (más funcional).

**Con SQL:**
```scala
df.createGlobalTempView("empleados")
spark.sql("SELECT departamento, ROUND(AVG(salario), 2) FROM global_temp.empleados GROUP BY departamento ORDER BY AVG(salario) DESC").show()
```

**Con API de Spark:**
```scala
df.groupBy("departamento")
  .agg(round(avg("salario"), 2).alias("salario_medio"))
  .orderBy(desc("salario_medio"))
  .show()
```

**La realidad:** Spark convierte ambas al mismo código interno. Yo puedo usar la que le entienda mejor.

---

### Ejercicio 7 — DataFrame → RDD → DataFrame completo

Aquí hago el flujo completo: tomo un DataFrame, lo convierto a RDD, hago transformaciones ahí, y vuelvo a convertir a DataFrame. 

```scala
// 1. Convertir a RDD
val rdd = df.rdd

// 2. Transformación: normalizar salarios (aplicar descuento del 10%)
val rddTransformado = rdd.map { row =>
  val nuevoSalario = row.getAs[Double]("salario") * 0.9
  (row.getAs[Int]("id"), row.getAs[String]("nombre"), nuevoSalario)
}

// 3. Volver a DataFrame
val dfResultado = rddTransformado.toDF("id", "nombre", "salario_reducido")
```

**Por qué lo hago:** Muestra la relación bidireccional entre RDD y DataFrame. A veces necesito bajar a RDD para operaciones muy específicas.

---

### Ejercicio 8 — Problema analítico con UDF y groupBy avanzado

Aquí planteo un problema real: **¿Cuáles son las películas más rentables por género, y cuáles tienen ROI alto en años recientes?**

Voy a:
1. Crear un **UDF** para calcular ROI = (ingresos - presupuesto) / presupuesto
2. **Agrupar por género Y año**
3. Una query con **condicional** (año > 2018)
4. Una query con **SQL**, otra con **API**

```scala
// UDF para calcular ROI
val calcularROI = udf { (ingresos: Double, presupuesto: Double) =>
  if (presupuesto > 0) ((ingresos - presupuesto) / presupuesto) else 0.0
}

df.withColumn("roi", calcularROI(col("ingresos"), col("presupuesto")))
  .filter(col("año") > 2018)
  .groupBy("genero", "año")
  .agg(
    avg("roi").alias("roi_medio"),
    count("*").alias("cantidad_peliculas")
  )
  .orderBy(desc("roi_medio"))
  .show()
```

**Qué veo:** Las combinaciones género+año con mejor ROI, cuántas películas hay de cada, etc.

---

### Ejercicio 9 — Conexión JDBC a PostgreSQL (setup + básico)

Aquí salgo de Spark y conecto a una base de datos real: PostgreSQL. Primero hago el setup en la máquina virtual.

#### Setup PostgreSQL:

```bash
# Instalar PostgreSQL
sudo apt install postgresql

# Acceder como superusuario
sudo -u postgres psql

# Dentro de postgres:
ALTER USER postgres PASSWORD 'postgres';
CREATE TABLE peliculas_ranking (
    id INT,
    titulo VARCHAR,
    genero VARCHAR,
    roi DOUBLE PRECISION
);
INSERT INTO peliculas_ranking VALUES(1, 'Avatar', 'Sci-Fi', 185.5);
SELECT * FROM peliculas_ranking;
\q
```

#### Conexión desde Spark (Scala):

```scala
import java.util.Properties

val props = new Properties()
props.setProperty("user", "postgres")
props.setProperty("driver", "org.postgresql.Driver")
props.setProperty("password", "postgres")

val jdbcDF = spark.read.jdbc(
  "jdbc:postgresql://localhost:5432/postgres",
  "peliculas_ranking",
  props
)

jdbcDF.show()
```

**Qué pasa:** Spark lee directamente de PostgreSQL usando JDBC. El DataFrame que obtengo es como cualquier otro: puedo filtrarlo, agrupar, etc.

---

### Ejercicio 10 — Queries propias en PostgreSQL

Aquí creo dos queries personalizadas usando el conector JDBC:

**Query 1 — Crear una tabla/vista desde datos de Spark:**
```scala
spark.sql("""
  CREATE TABLE top_peliculas USING jdbc 
  OPTIONS (
    url 'jdbc:postgresql://localhost:5432/postgres',
    driver 'org.postgresql.Driver',
    user 'postgres',
    password 'postgres',
    dbtable 'peliculas_ranking'
  )
""")
```

**Query 2 — Consulta analítica:**
```scala
spark.sql("""
  SELECT genero, AVG(roi) AS roi_promedio, COUNT(*) AS count
  FROM top_peliculas
  WHERE roi > 50
  GROUP BY genero
  ORDER BY roi_promedio DESC
""").show()
```

**Explicación:** La primera query crea una tabla virtual en Spark que mapea a PostgreSQL. La segunda hace un análisis: promedio de ROI por género, solo películas rentables (ROI > 50).

---

## Cómo ejecutar los ejercicios

Cada uno se ejecuta desde `spark-shell` o compilando y haciendo `spark-submit`.

### Opción 1: Desde spark-shell

```bash
spark-shell

scala> :load src/Ejercicio1.scala
scala> Ejercicio1.main(Array())
```

### Opción 2: Compilar y ejecutar

```bash
# Compilar uno de los ejercicios
scalac -cp /path/to/spark/jars/* src/Ejercicio3.scala

# Ejecutar con Spark
spark-submit --class Ejercicio3 target/ejercicio.jar data/datos_peliculas.csv
```

---

## Notas finales

- **Los datos:** He elegido un dataset de películas porque es realista, tiene tipos diversos, y permite hacer preguntas interesantes.
- **RDD vs DataFrame:** Casi siempre voy a querer DataFrames. Los RDDs son más rápidos en casos muy específicos.
- **SQL vs API:** Prefiero la API de Spark porque es más funcional, pero SQL es más familiar para quién viene de SQL tradicional.
- **PostgreSQL:** La conexión JDBC es simple pero poderosa. Así puedo sincronizar datos entre Spark y bases de datos reales.
