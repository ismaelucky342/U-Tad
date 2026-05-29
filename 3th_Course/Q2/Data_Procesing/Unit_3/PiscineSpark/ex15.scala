/*
 * EX15 - EJERCICIO FINAL: Simulación de Sistema Distribuido Completo
 *
 * OBJETIVO:
 * - Integrar TODOS los conceptos vistos
 * - Demostrar cómo Spark funciona en un cluster
 * - Resolver problema real completo
 * - Optimizar performance
 *
 * PROBLEMA: Análisis de datos de una red social
 *
 * Datos:
 * - Usuarios: (id, username, país)
 * - Posts: (post_id, user_id, fecha, likes)
 * - Comentarios: (comment_id, post_id, user_id, fecha)
 *
 * Análisis:
 * 1. Cargar datos (simulate file input)
 * 2. Calcular estadísticas por usuario
 * 3. Encontrar influencers (más likes)
 * 4. Análisis por país
 * 5. Optimizar con particiones y cache
 * 6. Guardar resultados
 *
 * CONCEPTOS:
 * - SparkContext + SparkSession
 * - RDD + transformaciones variadas
 * - Pair RDDs complejos
 * - Particiones y shuffle
 * - Cache / persistencia
 * - DAG y lazy evaluation
 * - Todas las acciones
 *
 */

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.storage.StorageLevel

object EjercicioSpark15 {
  
  case class Usuario(id: Int, username: String, pais: String)
  case class Post(id: Int, userId: Int, fecha: String, likes: Int)
  case class Comentario(id: Int, postId: Int, userId: Int, fecha: String)

  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
      .setAppName("RedSocial_Analytics")
      .setMaster("local[*]")
      .set("spark.default.parallelism", "4")

    val sc = new SparkContext(conf)

    println("=== ANÁLISIS DE RED SOCIAL (EJERCICIO FINAL) ===\n")

    // ============================================================
    // 1. CARGAR DATOS (simular desde archivos)
    // ============================================================
    
    println("1. Cargando datos...\n")

    val usuariosData = sc.parallelize(List(
      (1, "alice", "USA"),
      (2, "bob", "USA"),
      (3, "charlie", "UK"),
      (4, "diana", "Spain"),
      (5, "eve", "Spain"),
      (6, "frank", "USA"),
      (7, "grace", "UK"),
      (8, "henry", "Germany")
    ), numPartitions = 2)

    val postsData = sc.parallelize(List(
      (101, 1, "2024-01-01", 150),
      (102, 2, "2024-01-02", 85),
      (103, 1, "2024-01-03", 320),
      (104, 3, "2024-01-04", 200),
      (105, 4, "2024-01-05", 450),
      (106, 2, "2024-01-06", 120),
      (107, 5, "2024-01-07", 380),
      (108, 1, "2024-01-08", 275),
      (109, 6, "2024-01-09", 95),
      (110, 7, "2024-01-10", 165)
    ), numPartitions = 2)

    val comentariosData = sc.parallelize(List(
      (1001, 101, 2, "2024-01-01"),
      (1002, 101, 3, "2024-01-01"),
      (1003, 102, 1, "2024-01-02"),
      (1004, 103, 4, "2024-01-03"),
      (1005, 103, 5, "2024-01-03"),
      (1006, 105, 1, "2024-01-05"),
      (1007, 105, 2, "2024-01-05"),
      (1008, 105, 6, "2024-01-06"),
      (1009, 107, 3, "2024-01-07"),
      (1010, 107, 4, "2024-01-07")
    ), numPartitions = 2)

    // Convertir a Pair RDD
    val usuarios = usuariosData.map(x => (x._1, (x._2, x._3)))
    val posts = postsData.map(x => (x._2, (x._1, x._3, x._4))) // (userId, (postId, fecha, likes))
    val comentarios = comentariosData.map(x => (x._3, (x._1, x._2))) // (userId, (commentId, postId))

    println(s"   Usuarios cargados: ${usuarios.count()}")
    println(s"   Posts cargados: ${posts.count()}")
    println(s"   Comentarios cargados: ${comentarios.count()}")

    // ============================================================
    // 2. CACHE DE DATOS PARA REUTILIZACIÓN
    // ============================================================
    
    println("\n2. Cacheando datos para reutilización...\n")
    
    usuarios.persist(StorageLevel.MEMORY_ONLY)
    posts.persist(StorageLevel.MEMORY_ONLY)
    comentarios.persist(StorageLevel.MEMORY_ONLY)
    
    println("   Datos cacheados en memoria")

    // ============================================================
    // 3. ESTADÍSTICAS POR USUARIO
    // ============================================================
    
    println("\n3. Estadísticas por usuario:\n")

    // Posts por usuario
    val postsContadoPorUsuario = posts
      .map(x => (x._1, 1))
      .reduceByKey(_ + _)

    // Likes totales por usuario
    val likesTotalesPorUsuario = posts
      .map(x => (x._1, x._2._3))
      .reduceByKey(_ + _)

    // Comentarios por usuario
    val comentariosContadoPorUsuario = comentarios
      .map(x => (x._1, 1))
      .reduceByKey(_ + _)

    // Combinar estadísticas
    val estadisticasCompletas = usuarios
      .leftOuterJoin(postsContadoPorUsuario)
      .leftOuterJoin(likesTotalesPorUsuario)
      .leftOuterJoin(comentariosContadoPorUsuario)
      .map { case (userId, (((username, pais), numPosts), numLikes), numComments)) =>
        val posts = numPosts.getOrElse(0)
        val likes = numLikes.getOrElse(0)
        val comments = numComments.getOrElse(0)
        (userId, username, pais, posts, likes, comments)
      }

    println("   Usuario | Posts | Likes | Comentarios")
    estadisticasCompletas.collect().foreach { case (id, user, pais, posts, likes, comments) =>
      println(f"   $user%-8s | $posts%5d | $likes%5d | $comments%3d")
    }

    // ============================================================
    // 4. TOP INFLUENCERS
    // ============================================================
    
    println("\n4. Top Influencers (por likes totales):\n")

    val topInfluencers = estadisticasCompletas
      .sortBy(_._5, ascending = false) // Ordenar por likes
      .take(3)

    topInfluencers.foreach { case (id, user, pais, posts, likes, comments) =>
      println(f"   🌟 $user%-8s | Likes: $likes%4d | Posts: $posts%2d | País: $pais")
    }

    // ============================================================
    // 5. ANÁLISIS POR PAÍS
    // ============================================================
    
    println("\n5. Análisis por país:\n")

    val analisPorPais = usuarios
      .join(posts.groupByKey().map { case (userId, postsSeq) =>
        (userId, postsSeq.toList.map(_._3).sum) // Total likes por usuario
      })
      .map { case (userId, ((username, pais), totalLikes)) =>
        (pais, totalLikes)
      }
      .reduceByKey(_ + _)
      .sortBy(_._2, ascending = false)

    println("   País | Total Likes")
    analisPorPais.collect().foreach { case (pais, likes) =>
      println(f"   $pais%-10s | $likes%6d")
    }

    // ============================================================
    // 6. POSTS POPULARES
    // ============================================================
    
    println("\n6. Top 5 Posts más populares:\n")

    val topPosts = posts
      .map { case (userId, (postId, fecha, likes)) => (postId, userId, fecha, likes) }
      .map(x => (x._1, x)) // Para poder hacer join después
      .map(_._2)
      .top(5)(Ordering.by(_._4)) // Top 5 por likes

    println("   Post ID | Likes | Fecha")
    topPosts.foreach { case (postId, userId, fecha, likes) =>
      println(f"   $postId%7d | $likes%5d | $fecha")
    }

    // ============================================================
    // 7. ESTADÍSTICAS GLOBALES
    // ============================================================
    
    println("\n7. Estadísticas Globales:\n")

    val totalUsuarios = usuarios.count()
    val totalPosts = posts.count()
    val totalComentarios = comentarios.count()
    val totalLikes = posts.map(_._2._3).sum
    val promedioPosts = totalPosts.toDouble / totalUsuarios
    val promedioLikes = totalLikes / totalPosts

    println(f"   Total usuarios: $totalUsuarios")
    println(f"   Total posts: $totalPosts")
    println(f"   Total comentarios: $totalComentarios")
    println(f"   Total likes: ${totalLikes.toInt}")
    println(f"   Promedio posts/usuario: $promedioPosts%.2f")
    println(f"   Promedio likes/post: $promedioLikes%.2f")

    // ============================================================
    // 8. GUARDAR RESULTADOS
    // ============================================================
    
    println("\n8. Guardando resultados...\n")

    val outputPath = "/tmp/spark_red_social"
    
    // Guardar estadísticas
    val statsFormateado = estadisticasCompletas.map { case (id, user, pais, posts, likes, comments) =>
      s"$user,$pais,$posts,$likes,$comments"
    }
    statsFormateado.saveAsTextFile(s"$outputPath/estadisticas")
    
    println(s"   Resultados guardados en: $outputPath/estadisticas")

    // ============================================================
    // 9. INFORMACIÓN DE DAG Y LINEAGE
    // ============================================================
    
    println("\n9. Información de ejecución:\n")
    
    println(f"   Número de particiones (usuarios): ${usuarios.getNumPartitions()}")
    println(f"   Número de particiones (posts): ${posts.getNumPartitions()}")
    println(f"   Almacenamiento en caché: ${usuarios.getStorageLevel}")

    println("\n   DAG (toDebugString) - Primeras líneas:")
    println(estadisticasCompletas.toDebugString.split("\n").take(5).map("      " + _).mkString("\n"))

    // ============================================================
    // 10. LIMPIAR
    // ============================================================
    
    println("\n10. Limpiando...\n")
    
    usuarios.unpersist()
    posts.unpersist()
    comentarios.unpersist()
    
    println("    Caché liberado")
    println("\n=== ANÁLISIS COMPLETADO ===")

    sc.stop()
  }
}
