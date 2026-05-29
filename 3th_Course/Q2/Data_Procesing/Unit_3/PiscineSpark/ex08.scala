/*
 * EX08 - Cache y Persistencia
 *
 * OBJETIVO:
 * - Entender cache() y persist()
 * - Mejorar performance reutilizando RDDs
 * - Ver la diferencia en múltiples acciones
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD con transformaciones costosas
 *    (simuladas con delays)
 *
 * 2. Realiza MÚLTIPLES acciones sin cache
 *    Mide el tiempo
 *
 * 3. Aplica cache() y repite las acciones
 *    Compara tiempos
 *
 * 4. Explora niveles de persistencia:
 *    - MEMORY_ONLY
 *    - MEMORY_AND_DISK
 *    - DISK_ONLY
 *
 * CONCEPTOS:
 * - cache(): = persist(StorageLevel.MEMORY_ONLY)
 * - persist(): control total sobre dónde guardar
 * - Lazy: NO se guarda hasta primera acción
 * - unpersist(): libera memoria
 * - Reutilizar RDD cached es mucho más rápido
 *
 */

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.storage.StorageLevel

object EjercicioSpark08 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark08").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. RDD con transformaciones "costosas"
    val datos = sc.parallelize(1 to 100000)
    
    val rddTransformado = datos
      .map(x => x * 2)
      .filter(_ > 50000)
      .map(x => x / 2)

    println("=== SIN CACHE ===")
    
    // Primer count (calcula el DAG)
    val t1 = System.currentTimeMillis()
    val c1 = rddTransformado.count()
    val tiempo1 = System.currentTimeMillis() - t1
    println(s"1er count(): ${tempo1}ms, resultado: $c1")

    // Segundo count (recalcula)
    val t2 = System.currentTimeMillis()
    val c2 = rddTransformado.count()
    val tiempo2 = System.currentTimeMillis() - t2
    println(s"2do count(): ${tiempo2}ms, resultado: $c2")

    // Tercer count (recalcula de nuevo)
    val t3 = System.currentTimeMillis()
    val first = rddTransformado.first()
    val tiempo3 = System.currentTimeMillis() - t3
    println(s"first(): ${tiempo3}ms, resultado: $first")

    println("\n=== CON CACHE ===")

    // Aplicar cache
    rddTransformado.cache()

    // Primer count (calcula y cachea)
    val t4 = System.currentTimeMillis()
    val c3 = rddTransformado.count()
    val tiempo4 = System.currentTimeMillis() - t4
    println(s"1er count() con cache: ${tiempo4}ms, resultado: $c3 (CACHEA)")

    // Segundo count (desde cache)
    val t5 = System.currentTimeMillis()
    val c4 = rddTransformado.count()
    val tiempo5 = System.currentTimeMillis() - t5
    println(s"2do count() con cache: ${tiempo5}ms, resultado: $c4 (MÁS RÁPIDO)")

    // Tercer count (desde cache)
    val t6 = System.currentTimeMillis()
    val first2 = rddTransformado.first()
    val tiempo6 = System.currentTimeMillis() - t6
    println(s"first() con cache: ${tiempo6}ms, resultado: $first2 (MÁS RÁPIDO)")

    println("\n=== PERSISTENCIA ===")
    println(s"RDD se cachea en: ${rddTransformado.getStorageLevel}")

    // Liberar cache
    rddTransformado.unpersist()

    sc.stop()
  }
}
