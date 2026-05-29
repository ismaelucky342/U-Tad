/*
 * EX10 - DAG (Directed Acyclic Graph) y Lazy Evaluation
 *
 * OBJETIVO:
 * - Entender que Spark es LAZY: no ejecuta hasta acciones
 * - Visualizar el DAG de transformaciones
 * - Entender cómo Spark optimiza el plan de ejecución
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD con múltiples transformaciones
 *
 * 2. NO añadas acciones (verás que no pasa nada)
 *
 * 3. Añade una acción y verá ejecución
 *
 * 4. Utiliza toDebugString() para ver el DAG
 *
 * 5. Experimenta con:
 *    - Pipeline de transformaciones
 *    - Optimizaciones automáticas (catalyst/tungsten)
 *
 * CONCEPTOS:
 * - Lazy evaluation: transformaciones se quedan pendientes
 * - DAG: grafo de dependencias
 * - Actions: FUERZAN ejecución
 * - toDebugString(): visualizar DAG
 * - Spark puede optimizar pipelines (columnar, etc.)
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark10 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark10").setMaster("local[*]")
    val sc = new SparkContext(conf)

    println("=== LAZY EVALUATION Y DAG ===\n")

    // 1. Crear transformaciones SIN acción
    println("1. Definiendo transformaciones (SIN acciones):\n")
    
    val rdd0 = sc.parallelize(1 to 100)
    println("   Creado: parallelize(1-100)")

    val rdd1 = rdd0.map(x => x * 2)
    println("   Aplicado: map(x => x * 2) - SIN ejecutar")

    val rdd2 = rdd1.filter(_ > 100)
    println("   Aplicado: filter(_ > 100) - SIN ejecutar")

    val rdd3 = rdd2.map(x => (x, x * 10))
    println("   Aplicado: map(x => (x, x * 10)) - SIN ejecutar")

    val rdd4 = rdd3.filter { case (x, _) => x < 500 }
    println("   Aplicado: filter(x < 500) - SIN ejecutar")

    println("\n   ¡NADA HA SIDO EJECUTADO! Spark solo construye el DAG.\n")

    // 2. Ver el DAG
    println("2. Visualizando el DAG con toDebugString():\n")
    println(rdd4.toDebugString)

    // 3. Añadir acción
    println("\n3. Añadiendo acción: collect()")
    println("   Ahora SÍ se ejecuta todo el DAG...\n")

    val resultado = rdd4.collect()
    println(s"   Resultado: ${resultado.mkString(", ")}")

    // 4. Otro ejemplo con más transformaciones
    println("\n4. Ejemplo más complejo:\n")

    val datos = sc.parallelize(1 to 50, 4)
    val complejo = datos
      .map(x => (x % 3, x))
      .filter { case (mod, _) => mod != 0 }
      .groupByKey()
      .map { case (mod, valores) => (mod, valores.sum) }
      .sortBy(_._2, ascending = false)

    println("DAG del pipeline complejo:")
    println(complejo.toDebugString)

    println("\nEjecutando count()...")
    val count = complejo.count()
    println(s"Total de grupos: $count")

    println("\nPrimeros resultados con take(3):")
    complejo.take(3).foreach { case (mod, sum) =>
      println(s"  mod=$mod, sum=$sum")
    }

    println("\n=== REFLEXIÓN ===")
    println("- Todas las transformaciones son LAZY")
    println("- El DAG se construye sin ejecutar nada")
    println("- Solo las ACCIONES ejecutan el DAG")
    println("- Spark optimiza el plan antes de ejecutar")
    println("- toDebugString() muestra el esquema del DAG")

    sc.stop()
  }
}
