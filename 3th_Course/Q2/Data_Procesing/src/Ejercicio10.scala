import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{udf, col, avg, when, desc}
import java.util.Properties

/**
 * Ejercicio 10 — Queries propias en PostgreSQL
 *
 * Este es el ejercicio final donde creo MI PROPIA solución analítica
 * usando el conector JDBC a PostgreSQL.
 *
 * PREREQUISITOS (ejecutar en terminal primero):
 *
 *   sudo apt install postgresql
 *   sudo service postgresql start
 *   sudo -u postgres psql
 *
 * Luego dentro de psql:
 *
 *   CREATE TABLE peliculas_datos (
 *     id INT PRIMARY KEY,
 *     titulo VARCHAR(255),
 *     ano INT,
 *     genero VARCHAR(100),
 *     presupuesto DOUBLE PRECISION,
 *     ingresos DOUBLE PRECISION
 *   );
 *
 *   -- Insertar 10 películas de ejemplo
 *   INSERT INTO peliculas_datos VALUES
 *     (1, 'Avatar', 2009, 'Sci-Fi', 237000000, 2923706994),
 *     (2, 'Avatar 2', 2022, 'Sci-Fi', 350000000, 2320250281),
 *     (3, 'Avengers', 2012, 'Accion', 220000000, 1520595760),
 *     (4, 'Avengers IW', 2018, 'Accion', 325000000, 2052415039),
 *     (5, 'Titanic', 1997, 'Drama', 200000000, 2257843092),
 *     (6, 'Inception', 2010, 'Sci-Fi', 160000000, 839292587),
 *     (7, 'The Dark Knight', 2008, 'Accion', 185000000, 1005045668),
 *     (8, 'Interstellar', 2014, 'Sci-Fi', 165000000, 731200000),
 *     (9, 'Jurassic World', 2015, 'Accion', 150000000, 1670516444),
 *     (10, 'Lion King', 2019, 'Animacion', 250000000, 1660888561);
 *   \q
 *
 * Luego ejecutar este script desde spark-shell:
 *   spark-shell --jars ~/Descargas/postgresql-42.7.0.jar
 *   :load Ejercicio10.scala
 *   Ejercicio10.main(Array())
 */

object Ejercicio10 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio10 - Queries propias PostgreSQL")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._

    println("=== Ejercicio 10: Mis queries propias en PostgreSQL ===\"\n")

    val jdbcProperties = new Properties()
    jdbcProperties.setProperty("user",     "postgres")
    jdbcProperties.setProperty("password", "postgres")
    jdbcProperties.setProperty("driver",   "org.postgresql.Driver")

    val jdbcUrl = "jdbc:postgresql://localhost:5432/postgres"
    val dbTable = "peliculas_datos"

    try {
      // Leer datos desde PostgreSQL
      val dfPeliculas = spark.read
        .jdbc(jdbcUrl, dbTable, jdbcProperties)

      println(s"✓ Conectado a PostgreSQL. Total de películas: ${dfPeliculas.count()}\n")

      // ─────────────────────────────────────────────────────────────
      // QUERY 1: Crear una tabla/vista con películas rentables
      // ─────────────────────────────────────────────────────────────
      
      println("=" * 60)
      println("QUERY 1: Crear tabla de películas rentables")
      println("=" * 60)
      println("\n¿Qué pretendo obtener?")
      println("Una tabla con películas que ganaron más del 100% del presupuesto.")
      println("Es decir: (ingresos - presupuesto) / presupuesto > 1.0\n")

      // Crear UDF para calcular ROI
      val calcularROI = udf { (ingresos: Double, presupuesto: Double) =>
        if (presupuesto > 0) (ingresos - presupuesto) / presupuesto else 0.0
      }

      // Crear DataFrame con ROI y rentabilidad
      val dfConROI = dfPeliculas
        .withColumn("roi", calcularROI(col("ingresos"), col("presupuesto")))
        .withColumn("rentable", col("roi") > 1.0)

      // Registrar como tabla temporal para SQL
      dfConROI.createOrReplaceTempView("peliculas_con_roi")

      // Ejecutar query SQL: crear tabla de rentables
      val dfRentables = spark.sql("""
        SELECT 
          titulo,
          ano,
          genero,
          presupuesto,
          ingresos,
          ROUND(roi, 2) as roi
        FROM peliculas_con_roi
        WHERE rentable = true
        ORDER BY roi DESC
      """)

      println("Películas rentables (ROI > 100%):")
      dfRentables.show(truncate = false)

      // Guardar en PostgreSQL para persistencia
      println("\nGuardando tabla 'peliculas_rentables' en PostgreSQL...")
      dfRentables.write
        .mode("overwrite")
        .jdbc(jdbcUrl, "peliculas_rentables", jdbcProperties)
      println("✓ Tabla guardata en PostgreSQL")

      // ─────────────────────────────────────────────────────────────
      // QUERY 2: Consulta analítica de tendencias
      // ─────────────────────────────────────────────────────────────
      
      println("\n" + "=" * 60)
      println("QUERY 2: Análisis de rentabilidad por género y año")
      println("=" * 60)
      println("\n¿Qué pretendo obtener?")
      println("Ver cuál es el género más rentable en cada año,")
      println("incluyendo presupuesto promedio y cantidad de películas.\n")

      val dfAnalisis = spark.sql("""
        SELECT 
          ano,
          genero,
          COUNT(*) as cantidad,
          ROUND(AVG(presupuesto), 0) as presupuesto_promedio,
          ROUND(AVG(roi), 2) as roi_promedio,
          CASE 
            WHEN AVG(roi) > 1.0 THEN '🎯 MUY RENTABLE'
            WHEN AVG(roi) > 0.5 THEN '✓ RENTABLE'
            WHEN AVG(roi) > 0 THEN '△ MODERADO'
            ELSE '✗ PÉRDIDA'
          END as categoria
        FROM peliculas_con_roi
        GROUP BY ano, genero
        ORDER BY ano DESC, roi_promedio DESC
      """)

      println("Análisis de rentabilidad por género y año:")
      dfAnalisis.show(20, truncate = false)

      // ─────────────────────────────────────────────────────────────
      // ANÁLISIS ADICIONAL: Mejor género por década
      // ─────────────────────────────────────────────────────────────
      
      println("\n" + "=" * 60)
      println("ANÁLISIS EXTRA: Mejor género por década")
      println("=" * 60 + "\n")

      val dfDecadas = spark.sql("""
        SELECT 
          CONCAT((ano / 10) * 10, 's') as decada,
          genero,
          ROUND(AVG(roi), 2) as roi_promedio,
          COUNT(*) as peliculas
        FROM peliculas_con_roi
        GROUP BY CONCAT((ano / 10) * 10, 's'), genero
        ORDER BY decada DESC, roi_promedio DESC
      """)

      dfDecadas.show(truncate = false)

      // ─────────────────────────────────────────────────────────────
      // CONCLUSIONES
      // ─────────────────────────────────────────────────────────────
      
      println("\n" + "=" * 60)
      println("CONCLUSIONES")
      println("=" * 60)
      
      val rentablesCount = dfRentables.count()
      val totalPeliculas = dfPeliculas.count()
      val porcentaje = (rentablesCount.toDouble / totalPeliculas) * 100

      println(f"\n1. Rentabilidad general:")
      println(f"   - Total de películas: $totalPeliculas")
      println(f"   - Películas rentables (ROI > 100%): $rentablesCount")
      println(f"   - Porcentaje: ${porcentaje}%.1f%%")

      println(f"\n2. Géneros:")
      println("   - Ver tabla de 'Análisis de rentabilidad por género y año'")
      println("   - Identificar cuál es el género con mejor ROI promedio")

      println(f"\n3. Tendencias históricas:")
      println("   - ¿Mejora o empeora la rentabilidad en años recientes?")
      println("   - ¿Algunos géneros se adaptan mejor que otros?")

    } catch {
      case e: Exception =>
        println(f"✗ Error: ${e.getMessage}")
        println("\nAsegúrate de:")
        println("  1. PostgreSQL está corriendo: sudo service postgresql status")
        println("  2. Tabla 'peliculas_datos' existe en PostgreSQL")
        println("  3. Ejecutaste con: spark-shell --jars postgresql-*.jar")
    }

    spark.stop()
  }
}
