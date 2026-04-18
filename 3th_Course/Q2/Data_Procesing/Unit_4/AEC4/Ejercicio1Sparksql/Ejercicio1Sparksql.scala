import org.apache.spark.sql.{Row, SparkSession}
import org.apache.spark.sql.types.{DoubleType, IntegerType, StringType, StructField, StructType}
import org.apache.spark.sql.functions.{avg, col, desc, round}

object Ejercicio1Sparksql {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio1Sparksql")
      .master("local[*]")
      .getOrCreate()

    import spark.implicits._

    // 1) Creación de DataFrame desde una lista de datos en Scala
    val empleadosLista = Seq(
      (1, "Ana", 29, "Ventas", 42000.0),
      (2, "Pedro", 34, "Marketing", 39000.0),
      (3, "Lucía", 27, "IT", 54000.0),
      (4, "Miguel", 41, "Finanzas", 61000.0),
      (5, "Sara", 31, "Ventas", 47000.0)
    )

    val dfDesdeLista = empleadosLista.toDF("id", "nombre", "edad", "departamento", "salario")
    println("=== DataFrame creado desde una lista ===")
    dfDesdeLista.show(false)
    dfDesdeLista.printSchema()

    // 2) Definición manual de un esquema estructurado
    val filas = Seq(
      Row(6, "Raúl", 36, "IT", 57000.0),
      Row(7, "Clara", 28, "Marketing", 43000.0),
      Row(8, "Nuria", 38, "Finanzas", 62000.0)
    )

    val esquema = StructType(Array(
      StructField("id", IntegerType, nullable = false),
      StructField("nombre", StringType, nullable = false),
      StructField("edad", IntegerType, nullable = false),
      StructField("departamento", StringType, nullable = false),
      StructField("salario", DoubleType, nullable = false)
    ))

    val dfConEsquema = spark.createDataFrame(spark.sparkContext.parallelize(filas), esquema)
    println("=== DataFrame creado con esquema manual ===")
    dfConEsquema.show(false)
    dfConEsquema.printSchema()

    // 3) Lectura de datos desde un archivo CSV con configuraciones
    // Ejecutar este script desde la carpeta Ejercicio1Sparksql o pasando la ruta del CSV como argumento.
    val csvPath = if (args.nonEmpty) args(0) else "datos_empleados.csv"
    val dfDesdeCsv = spark.read
      .option("header", "true")
      .option("sep", ";")
      .option("inferSchema", "true")
      .option("mode", "DROPMALFORMED")
      .csv(csvPath)

    println("=== DataFrame leído desde CSV ===")
    dfDesdeCsv.show(false)
    dfDesdeCsv.printSchema()
    println(s"Columnas: ${dfDesdeCsv.columns.mkString(", ")}")
    println(s"Tipos: ${dfDesdeCsv.dtypes.map { case (c, t) => s"$c:$t" }.mkString(", ")}")

    // 4) Exploración inicial de los datos
    println("=== Exploración inicial del DataFrame desde CSV ===")
    dfDesdeCsv.show(10, truncate = false)
    dfDesdeCsv.describe("edad", "salario").show(false)
    println(s"Número total de filas: ${dfDesdeCsv.count()}")

    // 5) Conversión entre DataFrame y RDD
    val rddFromDf = dfDesdeCsv.rdd.map(row => (
      row.getAs[Int]("id"),
      row.getAs[String]("nombre"),
      row.getAs[String]("departamento"),
      row.getAs[Double]("salario")
    ))
    println("=== Conversión de DataFrame a RDD ===")
    rddFromDf.collect().foreach(println)

    // 6) Consultas usando SQL y API de Spark
    dfDesdeCsv.createGlobalTempView("empleados")

    println("=== Consulta SQL: salario medio por departamento ===")
    spark.sql(
      "SELECT departamento, ROUND(AVG(salario), 2) AS salario_medio " +
      "FROM global_temp.empleados GROUP BY departamento ORDER BY salario_medio DESC"
    ).show(false)

    println("=== Consulta SQL: empleados con salario > 45000 ===")
    spark.sql(
      "SELECT nombre, departamento, salario FROM global_temp.empleados " +
      "WHERE salario > 45000 ORDER BY salario DESC"
    ).show(false)

    println("=== Mismas consultas usando API de Spark ===")
    dfDesdeCsv.groupBy("departamento")
      .agg(round(avg("salario"), 2).alias("salario_medio"))
      .orderBy(desc("salario_medio"))
      .show(false)

    dfDesdeCsv.filter(col("salario") > 45000)
      .select("nombre", "departamento", "salario")
      .orderBy(desc("salario"))
      .show(false)

    spark.stop()
  }
}
