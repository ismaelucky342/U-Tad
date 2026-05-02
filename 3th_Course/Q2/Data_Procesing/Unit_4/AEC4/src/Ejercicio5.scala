import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.col

/**
 * Ejercicio 5 — DataFrame → RDD (bajando a nivel bajo)
 *
 * Hasta ahora trabajé con DataFrames (nivel alto, SQL-ish).
 * Aquí bajo a RDD: la abstracción más primitiva de Spark.
 *
 * ¿Cuándo necesito RDD?
 *   - Operaciones funcionales complejas (map, filter muy específicos)
 *   - Acceso a particiones individuales
 *   - Performance en transformaciones simples
 *
 * Pero cuidado: RDD es más bajo nivel, menos optimizado.
 * 90% del tiempo useré DataFrame. El 10% restante, aquí estoy.
 */
object Ejercicio5 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio5 - DataFrame a RDD")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    val csvPath = if (args.nonEmpty) args(0) else "data/datos_peliculas.csv"

    // Primero cargo el DataFrame
    val df = spark.read
      .option("header",      "true")
      .option("sep",         ";")
      .option("inferSchema", "true")
      .option("mode",        "DROPMALFORMED")
      .csv(csvPath)

    println("=== Conversión: DataFrame → RDD ===\n")

    // Convierto a RDD y extraigo solo los campos que me interesan
    val rddPeliculas = df.rdd.map(row => (
      row.getAs[Int]("id"),
      row.getAs[String]("titulo"),
      row.getAs[String]("genero"),
      row.getAs[Double]("presupuesto"),
      row.getAs[Double]("ingresos")
    ))

    println("RDD con información de películas (primeras 5):")
    rddPeliculas.take(5).foreach { case (id, titulo, genero, presupuesto, ingresos) =>
      println(f"  [$id] $titulo%-40s | $genero%-10s | Presupuesto: $$$presupuesto%.0f")
    }

    // Aplicar una transformación en el RDD
    println("\n=== Transformación: Filtrar películas con presupuesto > 100M ===")
    
    val rddFiltrado = rddPeliculas.filter { case (_, _, _, presupuesto, _) =>
      presupuesto > 100000000.0
    }

    println(f"Películas con presupuesto > $100M: ${rddFiltrado.count()}")

    // Otra transformación: calcular ganancia
    println("\n=== Transformación: Calcular ganancia (ingresos - presupuesto) ===")
    
    val rddGanancia = rddPeliculas.map { case (id, titulo, genero, presupuesto, ingresos) =>
      val ganancia = ingresos - presupuesto
      (titulo, genero, ganancia)
    }

    println("Top 5 películas por ganancia:")
    rddGanancia
      .takeOrdered(5)(Ordering[Double].reverse.on(_._3))
      .foreach { case (titulo, genero, ganancia) =>
        println(f"  $titulo%-40s | $genero%-10s | Ganancia: $$$ganancia%.0f")
      }

    println(f"\n✓ Información del RDD:")
    println(f"  - Número de particiones: ${rddPeliculas.getNumPartitions}")
    println(f"  - Total de registros: ${rddPeliculas.count()}")

    spark.stop()
  }
}
