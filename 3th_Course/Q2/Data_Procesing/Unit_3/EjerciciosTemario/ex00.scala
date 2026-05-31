//Práctica Spark Shell

//Ir al directorio:
//cd /home/bigdata/spark-3.3.3-bin-hadoop3/

//Consultar ayuda:
//bin/spark-shell --help

//Iniciar Spark:
//bin/spark-shell --master local[*] --name SparkBasico --deploy-mode client --driver-memory 1G --executor-memory 1G --conf spark.sql.shuffle.partitions=50

//Parámetros:
//local[*]=todos los núcleos
//name=nombre aplicación
//client=driver local
//driver-memory=memoria driver
//executor-memory=memoria executor
//shuffle.partitions=50 particiones shuffle

//Abrir Spark UI:
//http://10.0.2.15:4040

//Revisar Jobs, Stages y Storage.

//Identificar 3 transformaciones y 3 acciones útiles.

// paso 1: crear un RDD a partir de una colección local

val rdd = sc.parallelize(List(1, 2, 3, 4, 5))

// paso 2: aplicar una transformación (map)

val rddMult = rdd.map(x => x * 2)

// paso 3: obtener resultado con una acción (collect)

val resultado = rddMult.collect()

// paso 4: imprimir resultado

println(s"Resultado: ${resultado.mkString(", ")}")

// BONUS: contar elementos con count()
println(s"Cantidad de elementos en el RDD final: ${rddMult.count()}")

// Cerrar SparkContext (en modo interactivo no es necesario, pero en aplicación sí)
// sc.stop()

