//====================================================================================================//
//                                                                                                    //
//                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        //
//      AEC4 - PRDT                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       //
//                                                        ██║   ██║█████╗██║   ███████║██║  ██║       //
//      created:        21/04/2026  -  21:45:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       //
//      last change:    25/04/2026  -  00:55:42           ╚██████╔╝      ██║   ██║  ██║██████╔╝       //
//                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        //
//                                                                                                    //
//      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             //
//                                                                                                    //
//      Github:                                           https://github.com/ismaelucky342            //
//                                                                                                    //
//====================================================================================================//

import java.util.Properties
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

println("\n" + "="*80)
println("CONECTOR JDBC A POSTGRESQL - AEC4 PARTE 2")
println("="*80)

// Creo sesion si no existe
val spark = SparkSession.builder()
  .appName("PostgreSQL_JDBC")
  .master("local[*]")
  .getOrCreate()

// --- PASO 1: Configuro propiedades JDBC ---
println("\n[1] Configurando conexion JDBC...")
val props = new Properties()
props.setProperty("user", "postgres")
props.setProperty("driver", "org.postgresql.Driver")
props.setProperty("password", "postgres")
println("OK - Propiedades de conexion listas")

// --- PASO 2: Leo datos desde PostgreSQL ---
println("\n[2] Leyendo datos de PostgreSQL...")
val jdbcDF = spark.read.jdbc(
  "jdbc:postgresql://localhost:5432/postgres",
  "mytable",
  props
)
println("OK - DataFrame creado desde PostgreSQL")
println("\nDatos leidos:")
jdbcDF.show()

// --- PASO 3: Muestro esquema ---
println("\n[3] Esquema del DataFrame JDBC:")
jdbcDF.printSchema()

// --- PASO 4: Creo tabla Spark mapeada a PostgreSQL ---
println("\n[4] Creando tabla Spark con JDBC...")
spark.sql("""
  CREATE TABLE pgtable USING jdbc OPTIONS (
    url 'jdbc:postgresql://localhost:5432/postgres',
    driver 'org.postgresql.Driver',
    user 'postgres',
    password 'postgres',
    dbtable 'mytable'
  )
""")
println("OK - Tabla 'pgtable' creada")

println("\nVerificando contenido:")
spark.sql("SELECT * FROM pgtable").show()

// --- PASO 5: Query 1 - Crear tabla de alta calidad ---
println("\n[5] Query 1 - Crear tabla de modulos de alta calidad...")
val query1 = """
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

spark.sql(query1)
println("OK - Tabla 'high_quality_modules' creada")
println("\nContenido:")
spark.sql("SELECT * FROM high_quality_modules").show(truncate = false)

// --- PASO 6: Query 2 - Analisis detallado ---
println("\n[6] Query 2 - Resumen ejecutivo con multiples metricas...")
val query2 = """
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

println("Ejecutando Query 2...")
spark.sql(query2).show(truncate = false)

// --- PASO 7: Comparacion SQL vs DataFrame API ---
println("\n[7] Mismo resultado con DataFrame API (sin SQL):")
spark.sql("SELECT * FROM pgtable")
  .groupBy()
  .agg(
    count("*").as("Total"),
    round(avg("rating"), 2).as("Rating promedio"),
    max("rating").as("Rating maximo"),
    min("rating").as("Rating minimo")
  )
  .show(truncate = false)

println("\n" + "="*80)
println("Ejercicio JDBC completado")
println("="*80)
