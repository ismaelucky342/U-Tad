/*
 * EX09 - Particiones
 *
 * OBJETIVO:
 * - Entender cómo Spark divide datos en particiones
 * - Controlar número de particiones
 * - Entender impacto en performance
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD con parallelize y especifica particiones
 *
 * 2. Explora:
 *    - getNumPartitions(): número de particiones
 *    - mapPartitions(): operar sobre cada partición
 *    - glom(): ver contenido de particiones
 *
 * 3. Utiliza repartition() y coalesce()
 *    - repartition(n): crear n particiones (shuffle)
 *    - coalesce(n): reducir particiones sin shuffle
 *
 * 4. Mide performance diferente número de particiones
 *
 * CONCEPTOS:
 * - Particiones: datos distribuidos entre executors
 * - Más particiones: más paralelismo pero más overhead
 * - Menos particiones: menos overhead pero menos paralelismo
 * - repartition vs coalesce: repartition hace shuffle
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark09 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark09").setMaster("local[*]")
    val sc = new SparkContext(conf)

    println("=== PARTICIONES ===\n")

    // 1. Crear RDD con particiones definidas
    val datos1 = sc.parallelize(1 to 100, numPartitions = 4)
    println(s"RDD parallelize(1-100, 4 particiones): ${datos1.getNumPartitions()} particiones")

    val datos2 = sc.parallelize(1 to 100, numPartitions = 8)
    println(s"RDD parallelize(1-100, 8 particiones): ${datos2.getNumPartitions()} particiones")

    // 2. glom(): ver contenido de particiones
    println("\nContenido de particiones (datos1 con 4 particiones):")
    datos1.glom().collect().zipWithIndex.foreach { case (partition, idx) =>
      println(s"  Partición $idx: ${partition.toList}")
    }

    // 3. repartition vs coalesce
    println("\n=== REPARTITION vs COALESCE ===")

    val reparticionado = datos1.repartition(6)
    println(s"Después de repartition(6): ${reparticionado.getNumPartitions()} particiones")

    val coalescido = reparticionado.coalesce(2)
    println(s"Después de coalesce(2): ${coalescido.getNumPartitions()} particiones")

    // 4. mapPartitions: operación por partición
    println("\n=== MAPPARTITIONS ===")

    val mapPartResult = datos1.mapPartitions { partition =>
      val sum = partition.sum
      val count = partition.length
      Iterator(s"Suma: $sum, Elementos: $count")
    }

    println("Estadísticas por partición:")
    mapPartResult.collect().foreach(println)

    // 5. Performance testing
    println("\n=== IMPACTO EN PERFORMANCE ===")

    def medirPerformance(numParts: Int): Long = {
      val datos = sc.parallelize(1 to 1000000, numParts)
      val result = datos
        .map(x => x * 2)
        .filter(_ > 1000000)
        .count()
      System.currentTimeMillis()
    }

    for (particiones <- List(1, 4, 8, 16)) {
      val t1 = System.currentTimeMillis()
      val datos = sc.parallelize(1 to 1000000, particiones)
      datos.map(x => x * 2).filter(_ > 1000000).count()
      val t2 = System.currentTimeMillis()
      println(s"Con $particiones particiones: ${t2 - t1}ms")
    }

    sc.stop()
  }
}
