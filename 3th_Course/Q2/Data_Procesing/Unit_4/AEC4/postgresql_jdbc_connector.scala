// ============================================================================
// ANÁLISIS DE PELÍCULAS CON SPARK - PART 2: Conector JDBC a PostgreSQL
// ============================================================================
// Actividad AEC4: Ejercicio 2 - Conector PostgreSQL
// ============================================================================

// ============================================================================
// COMANDOS DE INSTALACIÓN Y CONFIGURACIÓN (Ejecutados en terminal/VM)
// ============================================================================

/* 
PASO 0: Instalación de PostgreSQL (YA REALIZADO)
$ sudo pacman -S postgresql postgresql-libs
$ sudo -u postgres initdb -D /var/lib/postgres/data
$ sudo systemctl start postgresql

PASO 1: Crear usuario y tabla de prueba
$ sudo -u postgres psql
postgres=# ALTER USER postgres PASSWORD 'postgres';
postgres=# CREATE TABLE mytable(id INT, name VARCHAR, rating INT);
postgres=# INSERT INTO mytable VALUES(1, 'Clase', 9);
postgres=# INSERT INTO mytable VALUES(2, 'Tutorial', 8);
postgres=# INSERT INTO mytable VALUES(3, 'Ejercicio', 10);
postgres=# SELECT * FROM mytable;
postgres=# \q

PASO 2: Descargar driver JDBC de PostgreSQL
$ cd ~/Descargas
$ wget https://jdbc.postgresql.org/download/postgresql-42.7.1.jar

PASO 3: Iniciar Spark Shell con el driver JDBC
$ spark-shell --jars /home/nirmata/Descargas/postgresql-42.7.1.jar

*/

// ============================================================================
// COMENTARIO DE LOS COMANDOS DEL EJERCICIO GUIADO
// ============================================================================

/*
Los comandos ejecutados en la terminal del ejercicio hacen lo siguiente:

1. sudo apt install postgresql
   - Instala PostgreSQL en la máquina virtual (en Arch Linux es: pacman -S postgresql)
   - PostgreSQL es un sistema de gestión de bases de datos relacional de código abierto

2. sudo -u postgres psql
   - Se conecta a PostgreSQL como usuario 'postgres' (superusuario)
   - psql es la interfaz interactiva de línea de comandos de PostgreSQL
   - El flag "-u" especifica qué usuario ejecuta el comando

3. ALTER USER postgres PASSWORD 'postgres';
   - Cambia la contraseña del usuario 'postgres' a 'postgres'
   - ALTER USER es el comando SQL para modificar propiedades de usuarios

4. CREATE TABLE mytable(id INT, name VARCHAR, rating INT);
   - Crea una tabla llamada 'mytable' con 3 columnas:
     * id: tipo INT (entero)
     * name: tipo VARCHAR (cadena de caracteres de longitud variable)
     * rating: tipo INT (entero)

5. INSERT INTO mytable VALUES(1, 'Clase', 9);
   - Inserta un nuevo registro en la tabla con valores: id=1, name='Clase', rating=9
   - Son 3 inserciones seguidas con diferentes datos

6. SELECT * FROM mytable;
   - Consulta todos los registros (*) de la tabla 'mytable'
   - Muestra los 3 registros que fueron insertados

7. \q
   - Comando de psql para salir de la sesión interactiva

8. cp /home/bigdata/.m2/repository/org/postgresql/postgresql/42.3.7/postgresql-42.3.7.jar /home/bigdata/Descargas/
   - Copia el driver JDBC de PostgreSQL desde el repositorio de Maven
   - El driver es necesario para que Spark pueda conectarse a PostgreSQL

9. bin/spark-shell --jars /home/bigdata/Descargas/postgresql-42.3.7.jar
   - Inicia Spark Shell (interfaz interactiva de Spark)
   - El flag --jars añade el driver JDBC en el classpath de Java/Spark
   - Spark necesita el driver para usar JDBC como conector
*/

// ============================================================================
// PARTE 1: LECTURA DESDE POSTGRESQL USANDO JDBC
// ============================================================================

import java.util.Properties
import org.apache.spark.sql.SparkSession

println("\n" + "="*80)
println("CONECTOR JDBC A POSTGRESQL - AEC4 PARTE 2")
println("="*80)

// Crear sesión de Spark (si no está activa)
val spark = SparkSession.builder()
  .appName("PostgreSQL_JDBC_Connector")
  .master("local[*]")
  .getOrCreate()

// Configurar propiedades JDBC
println("\n[PASO 1] Configurando propiedades de conexión JDBC...")
val props = new Properties()
props.setProperty("user", "postgres")
props.setProperty("driver", "org.postgresql.Driver")
props.setProperty("password", "postgres")

println("✓ Propiedades configuradas:")
println(s"  - Usuario: postgres")
println(s"  - Driver: org.postgresql.Driver")
println(s"  - Host: localhost (puerto 5432 por defecto)")

// Leer datos desde PostgreSQL usando JDBC
println("\n[PASO 2] Leyendo datos de PostgreSQL usando JDBC...")
val jdbcDF = spark.read.jdbc(
  "jdbc:postgresql://localhost:5432/postgres",  // URL JDBC: protocolo://host:puerto/database
  "mytable",                                      // La tabla que queremos leer
  props                                           // Propiedades de conexión (usuario, contraseña, driver)
)

println("✓ DataFrame creado desde PostgreSQL")

// Mostrar datos
println("\n[PASO 3] Mostrando datos del DataFrame JDBC...")
println("Contenido de la tabla 'mytable':")
jdbcDF.show()

// Información del esquema
println("\n[PASO 4] Esquema del DataFrame:")
jdbcDF.printSchema()

// Estadísticas básicas
println("\n[PASO 5] Estadísticas básicas:")
println(s"Total de registros: ${jdbcDF.count()}")
jdbcDF.describe().show()

// ============================================================================
// PARTE 2: CREAR TABLA EN SPARK CON CONECTOR JDBC (Usando SQL)
// ============================================================================

println("\n\n" + "="*80)
println("EJERCICIO GUIADO: Crear Tabla Spark con JDBC")
println("="*80)

/*
EXPLICACIÓN DEL COMANDO:

spark.sql("CREATE TABLE pgtable USING jdbc OPTIONS (
  url 'jdbc:postgresql://localhost:5432/postgres', 
  driver 'org.postgresql.Driver', 
  user 'postgres',
  password 'postgres', 
  dbtable 'mytable'
)")

Este comando:
1. CREATE TABLE pgtable - Crea una tabla virtual en Spark llamada 'pgtable'
2. USING jdbc - Especifica que queremos usar JDBC como fuente de datos
3. OPTIONS (...)  - Configura los parámetros de conexión:
   - url: La cadena de conexión JDBC con protocolo, host, puerto y base de datos
   - driver: El driver JDBC a usar (en este caso PostgreSQL)
   - user: Usuario de PostgreSQL
   - password: Contraseña de PostgreSQL
   - dbtable: La tabla de PostgreSQL que queremos mapear

El resultado es que la tabla 'pgtable' en Spark está directamente mapeada a 
la tabla 'mytable' en PostgreSQL. Cualquier lectura desde 'pgtable' lee de 
PostgreSQL en tiempo real.
*/

println("\n[PASO 1] Creando tabla Spark mapeada a PostgreSQL...")
spark.sql("""
  CREATE TABLE pgtable USING jdbc OPTIONS (
    url 'jdbc:postgresql://localhost:5432/postgres',
    driver 'org.postgresql.Driver',
    user 'postgres',
    password 'postgres',
    dbtable 'mytable'
  )
""")

println("✓ Tabla 'pgtable' creada exitosamente")

// Verificar tabla
println("\n[PASO 2] Verificando tabla 'pgtable':")
spark.sql("SELECT * FROM pgtable").show()

// ============================================================================
// PARTE 3: QUERIES SQL PERSONALIZADAS - EJERCICIO PROPIO
// ============================================================================

println("\n\n" + "="*80)
println("QUERIES SQL PERSONALIZADAS - EJERCICIO PROPIO")
println("="*80)

/*
EJERCICIO PERSONALIZADO: Análisis de Datos de Formación

PROBLEMA: 
Una startup de educación online necesita analizar sus datos de cursos y 
calificaciones de estudiantes. Tenemos una tabla con información de módulos 
de formación (id, name=nombre del módulo, rating=calificación promedio).

ANÁLISIS A REALIZAR:
1. Identificar módulos de alta calidad (rating >= 8)
2. Calcular estadísticas de desempeño
3. Crear vistas para seguimiento
*/

// ============================================================================
// QUERY 1: Crear Vista - Módulos de Alta Calidad
// ============================================================================

println("\n[QUERY 1] CREACIÓN DE TABLA/VISTA: Módulos de Alta Calidad (Rating >= 8.0)")
println("-" * 80)

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

println("QuerySQL:")
println(query1)
println("\nEjecución:")
spark.sql(query1)

println("\n✓ Tabla 'high_quality_modules' creada")
println("\nContenido de la tabla:")
spark.sql("SELECT * FROM high_quality_modules").show(truncate = false)

println("\nEXPLICACIÓN:")
println("""
Esta query ejecuta los siguientes pasos:
1. CREATE TABLE high_quality_modules - Crea una nueva tabla con los resultados
2. SELECT ... FROM pgtable - Lee de la tabla mapeada de PostgreSQL
3. WHERE rating >= 8.0 - Filtra solo módulos con calificación >= 8
4. CASE WHEN ... - Clasifica los módulos en categorías de calidad
5. ORDER BY rating DESC - Ordena de mayor a menor rating

Esta tabla se guarda en el metastore de Spark y puede ser consultada 
posteriormente sin necesidad de conectarse a PostgreSQL nuevamente.

PROPÓSITO: Permitir a la startup identificar rápidamente sus módulos de 
mayor calidad para promoción y uso como referencia.
""")

// ============================================================================
// QUERY 2: Análisis Detallado - Estadísticas Complejas
// ============================================================================

println("\n\n[QUERY 2] CONSULTA ANALÍTICA: Análisis Detallado de Módulos")
println("-" * 80)

val query2 = """
  SELECT 
    'Total de módulos' as Metrica,
    COUNT(*) as Valor
  FROM pgtable
  UNION ALL
  SELECT 
    'Módulos de alta calidad (>=8)',
    COUNT(*)
  FROM pgtable
  WHERE rating >= 8.0
  UNION ALL
  SELECT 
    'Rating promedio global',
    ROUND(AVG(rating), 2)
  FROM pgtable
  UNION ALL
  SELECT 
    'Rating máximo',
    MAX(rating)
  FROM pgtable
  UNION ALL
  SELECT 
    'Rating mínimo',
    MIN(rating)
  FROM pgtable
  ORDER BY Metrica
"""

println("Query SQL:")
println(query2)
println("\nEjecución:")
val resultAnalysis = spark.sql(query2)
resultAnalysis.show(truncate = false)

println("\nEXPLICACIÓN:")
println("""
Esta query es una consulta analítica que combina múltiples agregaciones:

1. COUNT(*) - Cuenta total de módulos
2. COUNT(*) con WHERE - Módulos con rating >= 8
3. AVG(rating) - Promedio de calificación
4. MAX(rating) - Calificación máxima
5. MIN(rating) - Calificación mínima

Técnicas utilizadas:
- UNION ALL: Combina múltiples SELECT en una sola consulta
- Funciones de agregación: COUNT, AVG, MAX, MIN
- WHERE: Filtrado condicional
- ROUND: Redondeo de decimales
- ORDER BY: Ordenamiento alfabético de resultados

PROPÓSITO: Obtener un resumen ejecutivo de la calidad general del portafolio 
de módulos en una sola consulta. Esto es mucho más eficiente que ejecutar 
5 consultas separadas.

RESULTADOS ESPERADOS:
- Métrica "Módulos de alta calidad": Mostrará cuántos módulos tienen rating >= 8
  Esto permite a la startup ver qué porcentaje de su catálogo es de calidad excelente
- Métrica "Rating promedio global": Indica la calidad promedio general
  Un promedio alto (>8) indica que la mayoría de módulos son de buena calidad
""")

// ============================================================================
// ANÁLISIS COMPARATIVO: DataFrame API vs SQL
// ============================================================================

println("\n\n[ANÁLISIS ADICIONAL] Comparación: SQL vs DataFrame API")
println("-" * 80)

println("\n--- Mismo resultado usando DataFrame API (no SQL) ---")
import org.apache.spark.sql.functions._

val dfAnalysis = spark.sql("SELECT * FROM pgtable")
  .groupBy()
  .agg(
    count("*").as("Total de módulos"),
    sum(when(col("rating") >= 8.0, 1).otherwise(0)).as("Módulos de alta calidad (>=8)"),
    round(avg("rating"), 2).as("Rating promedio global"),
    max("rating").as("Rating máximo"),
    min("rating").as("Rating mínimo")
  )

dfAnalysis.show(truncate = false)

println("""
COMPARACIÓN:
- SQL es más legible y declarativa (qué quiero, no cómo obtenerlo)
- DataFrame API es más programática y flexible
- Ambas generan el mismo plan de ejecución optimizado por Spark SQL
- Para análisis complejos, a menudo combinamos ambas (SQL + DataFrame API)
""")

// ============================================================================
// RESUMEN FINAL Y EXPLICACIÓN DE CONCEPTOS CLAVE
// ============================================================================

println("\n\n" + "="*80)
println("RESUMEN Y CONCEPTOS CLAVE")
println("="*80)

println("""
╔════════════════════════════════════════════════════════════════════════════╗
║                        CONECTOR JDBC EN SPARK                             ║
╚════════════════════════════════════════════════════════════════════════════╝

¿QUÉ ES JDBC?
JDBC = Java Database Connectivity
Es una API estándar de Java que permite conectar aplicaciones Java con 
bases de datos relacionales. Spark usa JDBC para leer/escribir en PostgreSQL.

¿POR QUÉ USAMOS JDBC?
- Abstracción uniforme: Un mismo código puede conectar a diferentes BD
- Seguridad: Las credenciales se pasan de forma estructurada
- Compatibilidad: La mayoría de BD relacional tiene driver JDBC

¿CÓMO FUNCIONA EN SPARK?
1. Spark divide la tabla en particiones (para paralelismo)
2. Cada partition worker ejecuta la consulta de forma independiente
3. Los datos se traen en paralelo (más rápido que serial)
4. Se reúnen en un único DataFrame en Spark

VENTAJAS DE USAR SPARK + JDBC:
✓ Procesar datos de PostgreSQL con la potencia de Spark
✓ Combinar datos de múltiples fuentes (PostgreSQL, Parquet, CSV, etc.)
✓ Realizar análisis distribuidos a gran escala
✓ Mantener los datos en PostgreSQL (sin duplicar)

LIMITACIONES:
✗ Más lento que leer datos locales (hay latencia de red)
✗ Requiere que PostgreSQL esté disponible y accesible
✗ Las transformaciones complejas se hacen mejor en Spark, no en BD

CASO DE USO IDEAL:
Cuando tienes datos en PostgreSQL y quieres:
- Combinarlos con datos de archivos (CSV, Parquet)
- Realizar análisis complejos que PostgreSQL no puede hacer eficientemente
- Reducir carga del servidor BD (push-down del filtrado a Spark)
""")

println("\n" + "="*80)
println("✓ Ejercicio JDBC completado exitosamente")
println("="*80)

// Limpiar (opcional)
// spark.stop()
