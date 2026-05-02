import org.apache.spark.sql.SparkSession
import java.util.Properties

/**
 * Ejercicio 9 — Conexión JDBC a PostgreSQL (setup + básico)
 *
 * Aquí salgo completamente de Spark y trabajo con una base de datos real.
 * JDBC (Java Database Connectivity) es el estándar para conectar Java/Scala
 * a cualquier base de datos.
 *
 * PASOS PREVIOS (en terminal):
 *
 * 1. Instalar PostgreSQL:
 *    sudo apt install postgresql
 *
 * 2. Entrar como usuario postgres:
 *    sudo -u postgres psql
 *
 * 3. Dentro de psql, ejecutar (una línea por una):
 *    ALTER USER postgres PASSWORD 'postgres';
 *    CREATE TABLE peliculas_ranking (
 *      id INT PRIMARY KEY,
 *      titulo VARCHAR(255),
 *      genero VARCHAR(100),
 *      roi DOUBLE PRECISION
 *    );
 *    INSERT INTO peliculas_ranking VALUES 
 *      (1, 'Avatar', 'Sci-Fi', 1134.0),
 *      (2, 'Titanic', 'Drama', 1029.0),
 *      (3, 'Avatar 2', 'Sci-Fi', 562.0);
 *    SELECT * FROM peliculas_ranking;
 *    \q
 *
 * 4. Descargar el driver JDBC de PostgreSQL:
 *    cd ~/Descargas
 *    wget https://jdbc.postgresql.org/download/postgresql-42.7.0.jar
 *
 * 5. Ejecutar con Spark indicando el JAR:
 *    spark-shell --jars ~/Descargas/postgresql-42.7.0.jar
 *
 * Luego ejecuto este script desde la shell.
 */

object Ejercicio9 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio9 - JDBC PostgreSQL")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    println("=== Ejercicio 9: Conexión JDBC a PostgreSQL ===\n")

    // ─────────────────────────────────────────────────────────
    // PASO 1: Configurar propiedades de conexión
    // ─────────────────────────────────────────────────────────
    
    val jdbcProperties = new Properties()
    jdbcProperties.setProperty("user",     "postgres")
    jdbcProperties.setProperty("password", "postgres")
    jdbcProperties.setProperty("driver",   "org.postgresql.Driver")

    val jdbcUrl = "jdbc:postgresql://localhost:5432/postgres"
    val dbTable = "peliculas_ranking"

    println("=== Conectando a PostgreSQL ===")
    println(f"URL:        $jdbcUrl")
    println(f"Usuario:    postgres")
    println(f"Tabla:      $dbTable")
    println()

    try {
      // ─────────────────────────────────────────────────────────
      // PASO 2: Leer datos desde PostgreSQL
      // ─────────────────────────────────────────────────────────
      
      println("Intentando leer desde la tabla 'peliculas_ranking'...")
      
      val jdbcDF = spark.read
        .jdbc(jdbcUrl, dbTable, jdbcProperties)

      println("✓ ¡Conexión exitosa!\n")

      // ─────────────────────────────────────────────────────────
      // PASO 3: Explorar los datos
      // ─────────────────────────────────────────────────────────
      
      println(s"Total de registros en PostgreSQL: ${jdbcDF.count()}")
      println("\nDatos leídos desde PostgreSQL:")
      jdbcDF.show(truncate = false)

      println("\nEsquema del DataFrame JDBC:")
      jdbcDF.printSchema()

      // ─────────────────────────────────────────────────────────
      // PASO 4: Operaciones Spark sobre datos JDBC
      // ─────────────────────────────────────────────────────────
      
      println("\n=== Procesamiento con API de Spark ===")
      jdbcDF.filter(col("roi") > 500.0)
        .select("titulo", "genero", "roi")
        .show(truncate = false)

    } catch {
      case e: Exception =>
        println(f"✗ Error de conexión: ${e.getMessage}")
        println("\nVerifica que:")
        println("  1. PostgreSQL esté instalado y corriendo:")
        println("     sudo service postgresql start")
        println("  2. La tabla 'peliculas_ranking' exista")
        println("  3. El driver PostgreSQL JDBC esté en la ruta correcta")
        println("  4. Ejecutaste spark-shell con: --jars /path/to/postgresql-*.jar")
    }

    spark.stop()
  }
}

// ────────────────────────────────────────────────────────────
// NOTAS SOBRE JDBC:
// ────────────────────────────────────────────────────────────
// 
// JDBC es el protocolo que usan TODOS los sistemas Java/Scala
// para conectarse a bases de datos. Cada BD tiene su propio driver:
//   - PostgreSQL:  org.postgresql.Driver
//   - MySQL:       com.mysql.cj.jdbc.Driver
//   - SQL Server:  com.microsoft.sqlserver.jdbc.SQLServerDriver
//   - Oracle:      oracle.jdbc.driver.OracleDriver
//   - SQLite:      org.sqlite.JDBC
//
// Una vez que el driver está instalado, el código es prácticamente idéntico.
//
// VENTAJAS:
//   ✓ Integración con sistemas reales de BD
//   ✓ Legible y sincronizado
//   ✓ Push-down de filtros: Spark optimiza qué datos traer
//
// DESVENTAJAS:
//   ✗ Requiere configuración externa (BD corriendo)
//   ✗ Dependencia del driver JDBC
//   ✗ Más lento que datos locales para big data
