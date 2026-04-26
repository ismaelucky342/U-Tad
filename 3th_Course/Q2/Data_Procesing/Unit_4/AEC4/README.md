# EjercicioSparkSQL

Ejercicio práctico de Apache Spark para explorar la creación, transformación y consulta de DataFrames y RDDs en un entorno distribuido. Todos los ejemplos están escritos en Scala y se ejecutan en modo local.

---

## Estructura del proyecto

```
EjercicioSparkSQL/
├── data/
│   └── datos_empleados.csv       # Datos de empleados (delimitado por ;)
├── src/
│   ├── Ejercicio1.scala          # DataFrame desde una lista de Scala
│   ├── Ejercicio2.scala          # DataFrame con esquema manual (StructType)
│   ├── Ejercicio3.scala          # Lectura de CSV con opciones de configuración
│   ├── Ejercicio4.scala          # Exploración inicial del DataFrame
│   ├── Ejercicio5.scala          # Conversión DataFrame → RDD
│   └── Ejercicio6.scala          # Consultas con SQL y con la API de Spark
└── README.md
```

---

## Descripción de los ejercicios

### Ejercicio 1 — DataFrame desde una lista de Scala

Se parte de una `Seq` de tuplas con datos de empleados y se convierte en un DataFrame usando `toDF()` con nombres de columna explícitos. Spark infiere automáticamente los tipos de datos de cada columna a partir de los valores de la secuencia.

**Métodos principales:** `toDF()`, `show()`, `printSchema()`

---

### Ejercicio 2 — DataFrame con esquema manual

En lugar de dejar que Spark infiera los tipos, se define el esquema de forma explícita mediante `StructType` y `StructField`, especificando el nombre, el tipo (`IntegerType`, `StringType`, `DoubleType`) y la nullabilidad de cada columna. El DataFrame se crea a partir de un `RDD[Row]` y el esquema definido.

**Métodos principales:** `StructType`, `StructField`, `spark.createDataFrame()`, `parallelize()`

---

### Ejercicio 3 — Lectura de CSV con configuraciones

Se lee un archivo CSV usando `spark.read` con las siguientes opciones:

| Opción | Valor | Descripción |
|---|---|---|
| `header` | `true` | La primera fila contiene los nombres de columna |
| `sep` | `;` | El delimitador de campo es punto y coma |
| `inferSchema` | `true` | Spark deduce los tipos automáticamente |
| `mode` | `DROPMALFORMED` | Descarta filas con formato incorrecto |

La ruta del CSV puede pasarse como argumento al ejecutar el programa, o usa la ruta por defecto `data/datos_empleados.csv`.

**Métodos principales:** `spark.read`, `columns`, `dtypes`

---

### Ejercicio 4 — Exploración inicial de los datos

Una vez cargado el DataFrame se aplican los métodos de inspección más habituales para conocer su contenido, estructura y estadísticas básicas.

| Método | Descripción |
|---|---|
| `show(n)` | Muestra las primeras n filas |
| `printSchema()` | Imprime el árbol de tipos del esquema |
| `columns` | Array con los nombres de todas las columnas |
| `dtypes` | Array de pares (nombre, tipo) por columna |
| `count()` | Número total de filas en el DataFrame |
| `describe(cols*)` | Estadísticas descriptivas: count, mean, stddev, min, max |

---

### Ejercicio 5 — Conversión DataFrame → RDD

Un DataFrame se convierte en un `RDD[Row]` mediante `.rdd` y, a continuación, se aplica `.map()` para extraer los campos de cada fila y transformarlos en tuplas tipadas. Este flujo es útil cuando se necesita acceder a la API de bajo nivel de Spark para operaciones funcionales sobre particiones.

**Métodos principales:** `.rdd`, `.map()`, `row.getAs[T]()`, `.collect()`, `getNumPartitions`

---

### Ejercicio 6 — Consultas con SQL y con la API de Spark

Se registra el DataFrame como una vista global temporal con `createGlobalTempView()`, accesible desde cualquier SparkSession del mismo contexto bajo el prefijo `global_temp.`. Se realizan dos consultas de dos formas equivalentes:

**Consulta 1 — Salario medio por departamento (descendente)**

```sql
SELECT   departamento,
         ROUND(AVG(salario), 2) AS salario_medio
FROM     global_temp.empleados
GROUP BY departamento
ORDER BY salario_medio DESC
```

Equivalente con la API de Spark:
```scala
df.groupBy("departamento")
  .agg(round(avg("salario"), 2).alias("salario_medio"))
  .orderBy(desc("salario_medio"))
```

**Consulta 2 — Empleados con salario superior a 45 000 (descendente)**

```sql
SELECT nombre, departamento, salario
FROM   global_temp.empleados
WHERE  salario > 45000
ORDER BY salario DESC
```

Equivalente con la API de Spark:
```scala
df.filter(col("salario") > 45000)
  .select("nombre", "departamento", "salario")
  .orderBy(desc("salario"))
```

**Métodos principales:** `createGlobalTempView()`, `spark.sql()`, `groupBy()`, `agg()`, `filter()`, `select()`, `orderBy()`

---

## Datos de ejemplo

El archivo `data/datos_empleados.csv` contiene registros adicionales en formato CSV con separador `;`:

```
id;nombre;edad;departamento;salario
9;Elena;32;Ventas;46000.0
10;Diego;45;Finanzas;65000.0
11;Marta;26;IT;52000.0
12;Alberto;29;Marketing;41000.0
13;Lorena;35;Ventas;48000.0
```

---

## Ejecución

Cada objeto puede ejecutarse de forma independiente desde un entorno con Spark configurado. Para los ejercicios 3–6 se puede pasar la ruta del CSV como primer argumento:

```bash
spark-submit --class Ejercicio3 target/ejercicio-sparksql.jar data/datos_empleados.csv
```

Si no se proporciona argumento, todos los scripts buscan el CSV en `data/datos_empleados.csv` relativo al directorio de trabajo.
