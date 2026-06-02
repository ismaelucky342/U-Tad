/*===============================================================================
EJERCICIO 6 (2 puntos) - SPARK SQL Y HDFS: ETL COMPLETO
===============================================================================

DATOS DE ENTRADA:
1. users.csv: user_id, nombre, país
2. transacciones.json: transaccion_id, user_id, producto, cantidad, precio
3. productos.parquet: producto_id, categoria, stock

TAREA:
Implementa un pipeline Spark SQL que:

1. Cargue los 3 datasets (CSV, JSON, Parquet)
2. Realice un JOIN:
   - transacciones con users (para obtener país)
   - resultado con productos (para obtener categoría)
3. Cree una vista SQL "venta_completa" con columnas:
   user_id, nombre, país, producto, categoria, cantidad, precio, monto_total

4. Ejecute análisis SQL:
   a) Total de ventas por país (GROUP BY país, ORDER BY total DESC)
   b) Producto más vendido por categoría
   c) Cliente (user_id) que más gastó en total

5. Guarde el resultado enriquecido en Parquet con particiones por país

EJEMPLO DE SALIDA SQL:
Query 1 - Ventas por país:
| país       | total_vendas |
| USA        | 15000.00     |
| España     | 8500.00      |
| Alemania   | 7200.00      |

Query 2 - Producto más vendido por categoría:
| categoría   | producto      | cantidad |
| Electrónica | Laptop        | 45       |
| Ropa        | Camiseta      | 120      |

Query 3 - Cliente top:
| user_id | nombre    | gasto_total |
| 42      | Juan López| 3500.00     |

PISTAS:
- Usa SparkSession.read.csv/json/parquet/option()
- SQL JOIN: SELECT a.*, b.* FROM tabla_a JOIN tabla_b ON a.id = b.id
- GROUP BY y ORDER BY para agregaciones
- write.mode("overwrite").parquet(path) para guardar
*/

// 1. Cargar datasetsc
val spark = SparkSession.builder.appName("ETL Completo").getOrCreate()
import spark.implicits._

val usersDF = spark.read.option("header", "true").csv("users.csv")
val transaccionesDF = spark.read.json("transacciones.json")
val productosDF = spark.read.parquet("productos.parquet")

// 2. Realizar JOINs
val transaccionesConUsuarios = transaccionesDF.join(usersDF, "user_id")
val ventaCompletaDF = transaccionesConUsuarios.join(productosDF, transaccionesConUsuarios("producto") === productosDF("producto_id"))
  .select("user_id", "nombre", "país", "producto", "categoria", "cantidad", "precio")
  .withColumn("monto_total", $"cantidad" * $"precio")

// 3. Crear vista SQL
ventaCompletaDF.createOrReplaceTempView("venta_completa")

// 4. Análisis SQL
// a) Total de ventas por país
val ventasPorPais = spark.sql("""
  SELECT país, SUM(monto_total) AS total_vendas
    FROM venta_completa
    GROUP BY país
    ORDER BY total_vendas DESC
""")

// b) Producto más vendido por categoría
val productoMasVendido = spark.sql("""
  SELECT categoria, producto, SUM(cantidad) AS cantidad
    FROM venta_completa
    GROUP BY categoria, producto
    ORDER BY cantidad DESC
""").dropDuplicates("categoria")        

// c) Cliente que más gastó en total
val clienteTop = spark.sql("""
  SELECT user_id, nombre, SUM(monto_total) AS gasto_total
    FROM venta_completa
    GROUP BY user_id, nombre
    ORDER BY gasto_total DESC
    LIMIT 1
""")

// 5. Guardar resultado enriquecido en Parquet con particiones por país
ventaCompletaDF.write.mode("overwrite").partitionBy("país").parquet("venta_completa.parquet")       

