/*
 * EX12 - Pair RDD: operaciones complejas
 *
 * OBJETIVO:
 * - Dominar operaciones en Pair RDD
 * - Join, union, intersection
 * - Operaciones distribuidas avanzadas
 *
 * ENUNCIADO:
 *
 * 1. Crea Pair RDD con datos de estudiantes:
 *    (ID_estudiante, nombre)
 *
 * 2. Crea Pair RDD con calificaciones:
 *    (ID_estudiante, nota)
 *
 * 3. Realiza:
 *    - join(): combinar por clave
 *    - leftOuterJoin(): incluir NOs coincidentes
 *    - reduceByKey(): agregar calificaciones
 *    - keys() / values(): extraer claves/valores
 *
 * 4. Calcula estadísticas:
 *    - Nota máxima por estudiante
 *    - Promedio general
 *
 * CONCEPTOS:
 * - join(): combina RDDs por clave
 * - leftOuterJoin(): preserva claves izquierda
 * - rightOuterJoin(): preserva claves derecha
 * - fullOuterJoin(): todas las claves
 * - keys() / values(): extraer componentes
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark12 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark12").setMaster("local[*]")
    val sc = new SparkContext(conf)

    println("=== PAIR RDD: OPERACIONES COMPLEJAS ===\n")

    // 1. RDD de estudiantes: (ID, nombre)
    val estudiantes = sc.parallelize(List(
      (1, "Ana"),
      (2, "Luis"),
      (3, "Marta"),
      (4, "Carlos"),
      (5, "Lucia")
    ))

    // 2. RDD de calificaciones: (ID, nota)
    val calificaciones = sc.parallelize(List(
      (1, 7.5),
      (2, 4.0),
      (3, 8.2),
      (1, 6.5),
      (4, 6.8),
      (3, 7.8),
      (5, 9.1),
      (2, 5.0)
    ))

    // 3. join(): combinar estudian y calificaciones
    println("1. join() - Combinar estudiantes con calificaciones:")
    val joined = estudiantes.join(calificaciones)
    joined.collect().foreach { case (id, (nombre, nota)) =>
      println(s"   ID=$id: $nombre -> $nota")
    }

    // 4. keys() y values()
    println("\n2. keys() y values():")
    println(s"   IDs únicos: ${estudiantes.keys.collect().mkString(", ")}")
    println(s"   Notas: ${calificaciones.values.collect().mkString(", ")}")

    // 5. leftOuterJoin()
    println("\n3. leftOuterJoin() - Todos los estudiantes (aunque no tengan notas):")
    
    // Primero añadir un estudiante sin calificaciones
    val estudiantesConExtra = estudiantes.union(
      sc.parallelize(List((6, "Pedro")))
    )
    
    val leftJoined = estudiantesConExtra.leftOuterJoin(calificaciones)
    leftJoined.collect().foreach { case (id, (nombre, notaOpt)) =>
      val nota = notaOpt match {
        case Some(n) => n.toString
        case None => "SIN CALIFICACIÓN"
      }
      println(s"   ID=$id: $nombre -> $nota")
    }

    // 6. rightOuterJoin()
    println("\n4. rightOuterJoin() - Todas las calificaciones (incluso si no está en estudiantes):")
    val rightJoined = estudiantes.rightOuterJoin(
      calificaciones.union(sc.parallelize(List((99, 10.0))))
    )
    rightJoined.collect().foreach { case (id, (nombreOpt, nota)) =>
      val nombre = nombreOpt match {
        case Some(n) => n
        case None => "DESCONOCIDO"
      }
      println(s"   ID=$id: $nombre -> $nota")
    }

    // 7. reduceByKey() en calificaciones
    println("\n5. reduceByKey() - Suma de notas por estudiante:")
    val sumaPorEstudiante = calificaciones.reduceByKey(_ + _)
    
    sumaPorEstudiante.join(estudiantes).collect().foreach { case (id, (suma, nombre)) =>
      println(s"   $nombre (ID=$id): suma=$suma")
    }

    // 8. Estadísticas con join
    println("\n6. Estadísticas avanzadas:")
    
    // Contar notas por estudiante
    val countPorEstudiante = calificaciones.map(x => (x._1, 1)).reduceByKey(_ + _)
    
    // Unir suma y conteo
    val estadisticas = sumaPorEstudiante.join(countPorEstudiante)
      .map { case (id, (suma, count)) => (id, suma / count) }
      .join(estudiantes)
    
    estadisticas.collect().foreach { case (id, (promedio, nombre)) =>
      println(s"   $nombre: promedio = $promedio")
    }

    // 9. Operaciones de conjunto
    println("\n7. Operaciones de conjunto:")
    
    val ids1 = sc.parallelize(List(1, 2, 3, 4))
    val ids2 = sc.parallelize(List(3, 4, 5, 6))
    
    println(s"   union: ${ids1.union(ids2).distinct().collect().mkString(", ")}")
    println(s"   intersection: ${ids1.intersection(ids2).collect().mkString(", ")}")

    sc.stop()
  }
}
