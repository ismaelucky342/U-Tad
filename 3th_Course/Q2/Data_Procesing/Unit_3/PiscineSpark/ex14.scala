/*
 * EX14 - Inmutabilidad de RDDs
 *
 * OBJETIVO:
 * - Entender que RDDs son inmutables
 * - Cómo Spark usa inmutabilidad para recuperación
 * - Lineage: tracking de transformaciones
 * - Ventajas en entornos distribuidos
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD
 *
 * 2. Aplica transformaciones y demuestra
 *    que el original NO cambia
 *
 * 3. Examina el lineage (toDebugString)
 *
 * 4. Simula fallos y recuperación
 *
 * 5. Compara con código mutable
 *
 * CONCEPTOS:
 * - Inmutabilidad: RDD no cambia, se crean nuevos
 * - Ventajas: sin race conditions, recuperación automática
 * - Lineage: Spark registra todas las transformaciones
 * - Recuperación: puede recalcular datos perdidos
 * - Performance: permite optimizaciones
 *
 */

import org.apache.spark.{SparkConf, SparkContext}
import scala.collection.mutable.ArrayBuffer

object EjercicioSpark14 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark14").setMaster("local[*]")
    val sc = new SparkContext(conf)

    println("=== INMUTABILIDAD DE RDDs ===\n")

    // 1. Crear RDD original
    val rddOriginal = sc.parallelize(1 to 10)
    println(s"RDD original: ${rddOriginal.collect().mkString(", ")}")

    // 2. Aplicar transformaciones
    println("\n2. Aplicar transformaciones:\n")

    val rdd2 = rddOriginal.map(_ * 2)
    println(s"   Después map(*2): ${rdd2.collect().mkString(", ")}")

    // IMPORTANTE: rddOriginal NO ha cambiado
    println(s"   RDD original aún: ${rddOriginal.collect().mkString(", ")}")

    val rdd3 = rdd2.filter(_ > 10)
    println(f"\n   Después filter(>10): ${rdd3.collect().mkString(", ")}")
    println(f"   RDD original aún: ${rddOriginal.collect().mkString(", ")}")

    // 3. Examinar lineage
    println("\n3. LINEAGE (toDebugString):")
    println("\nLineage de rdd3:")
    println(rdd3.toDebugString)

    // Comparar con mutable
    println("\n4. COMPARACIÓN: Mutable vs Inmutable\n")

    println("   Código mutable en Scala:")
    val listaMutable = ArrayBuffer(1, 2, 3, 4, 5)
    println(f"      Original: $listaMutable")
    listaMutable.map(_ * 2) // En Scala, esto NO modifica la lista
    println(f"      Después map(*2): $listaMutable")
    listaMutable.foreach(_ * 2)
    println(f"      Después foreach(*2): $listaMutable")

    println("\n   En cambio, RDD es SIEMPRE inmutable:")
    val rddInmutable = sc.parallelize(1 to 5)
    println(f"      Original: ${rddInmutable.collect().mkString(", ")}")
    val rddTransformado = rddInmutable.map(_ * 2)
    println(f"      Después transformación: ${rddInmutable.collect().mkString(", ")} (NO cambió)")
    println(f"      Nuevo RDD: ${rddTransformado.collect().mkString(", ")}")

    // 5. Ventajas de inmutabilidad
    println("\n5. VENTAJAS:\n")

    println("   a) Sin race conditions:")
    println("      - Múltiples threads/procesos pueden usar el mismo RDD")
    println("      - No hay competencia por recursos")

    val rddShared = sc.parallelize(1 to 100)
    
    // Múltiples transformaciones del mismo RDD sin conflicto
    val pares = rddShared.filter(_ % 2 == 0)
    val impares = rddShared.filter(_ % 2 == 1)
    val mayores50 = rddShared.filter(_ > 50)

    println(s"      Pares: ${pares.take(3).mkString(", ")}...")
    println(s"      Impares: ${impares.take(3).mkString(", ")}...")
    println(s"      >50: ${mayores50.take(3).mkString(", ")}...")

    println("\n   b) Recuperación automática (Fault Tolerance):")
    println("      - Si un executor falla, Spark recalcula dados")
    println("      - El lineage permite reconstruir desde el inicio")

    println("\n   c) Optimizaciones:")
    println("      - No hay locks/sincronización")
    println("      - Parallelismo real sin sincronización")
    println("      - Catalyst puede optimizar sabiendo que no hay side effects")

    // 6. Cadena de transformaciones
    println("\n6. Cadena de transformaciones (sin mutar original):\n")

    val base = sc.parallelize(1 to 20)
    println(f"   Base: ${base.take(5).mkString(", ")}...")

    val paso1 = base.map(x => x * 2)
    println(f"   x2: ${paso1.take(5).mkString(", ")}...")

    val paso2 = paso1.filter(_ > 20)
    println(f"   >20: ${paso2.take(5).mkString(", ")}...")

    val paso3 = paso2.map(x => (x, x % 3))
    println(f"   (x, x%3): ${paso3.take(3).mkString(", ")}...")

    // El original no ha cambiado
    println(f"\n   Base original aún: ${base.take(5).mkString(", ")}...")

    // 7. Lineage completo
    println("\n7. Lineage completo:")
    println(paso3.toDebugString)

    println("\n=== REFLEXIÓN ===")
    println("- RDDs son SIEMPRE inmutables")
    println("- Cada transformación crea un nuevo RDD")
    println("- Spark registra lineage completo (DAG)")
    println("- Permite recuperación ante fallos")
    println("- Facilita paralelismo sin bugs de concurrencia")
    println("- Permite optimizaciones de Catalyst")

    sc.stop()
  }
}
