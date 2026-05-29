/*
 * EX13 - Combinación de transformaciones complejas
 *
 * OBJETIVO:
 * - Resolver problema real con múltiples transformaciones
 * - Combinar map, filter, flatMap, reduceByKey, groupByKey
 * - Optimizar pipelines
 *
 * ENUNCIADO:
 *
 * PROBLEMA: Análisis de logs de ventas
 *
 * Datos:
 * "2024-01-01,USA,100,Electronics"
 * "2024-01-01,EUR,50,Books"
 * "2024-01-02,USA,200,Electronics"
 * ...
 *
 * Tareas:
 * 1. Parsear los logs
 * 2. Filtrar solo Electronics
 * 3. Convertir monedas (EUR->USD: 1.2x)
 * 4. Agrupar por país
 * 5. Calcular: total ventas, promedio, máximo
 * 6. Ordenar por total descendente
 *
 * CONCEPTOS:
 * - Pipeline complejo
 * - Parsing y transformación
 * - Múltiples agregaciones
 * - Optimización de operaciones
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark13 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark13").setMaster("local[*]")
    val sc = new SparkContext(conf)

    println("=== ANÁLISIS COMPLEJO DE DATOS ===\n")

    // Datos de ejemplo (en producción vendrían de archivos)
    val logsVentas = sc.parallelize(List(
      "2024-01-01,USA,100,Electronics",
      "2024-01-01,EUR,50,Books",
      "2024-01-01,USA,200,Electronics",
      "2024-01-02,USA,150,Electronics",
      "2024-01-02,EUR,80,Electronics",
      "2024-01-02,GBP,120,Electronics",
      "2024-01-03,USA,300,Clothing",
      "2024-01-03,EUR,100,Electronics",
      "2024-01-03,USA,250,Electronics",
      "2024-01-04,GBP,200,Electronics",
      "2024-01-04,EUR,90,Electronics"
    ))

    println("Datos originales:")
    logsVentas.take(3).foreach(println)

    // 1. Parsear logs: convertir a (fecha, país, monto, categoría)
    val infoVentas = logsVentas.map { linea =>
      val partes = linea.split(",")
      (partes(0), partes(1), partes(2).toDouble, partes(3))
    }

    println("\n1. Datos parseados:")
    infoVentas.take(2).foreach { case (fecha, pais, monto, cat) =>
      println(s"   ($fecha, $pais, $monto, $cat)")
    }

    // 2. Filtrar solo Electronics
    val electronics = infoVentas.filter(_._4 == "Electronics")
    println(s"\n2. Solo Electronics: ${electronics.count()} registros")

    // 3. Convertir monedas a USD
    val conversionTasas = Map("USA" -> 1.0, "EUR" -> 1.2, "GBP" -> 1.35)
    val montosUSD = electronics.map { case (fecha, pais, monto, cat) =>
      val tasa = conversionTasas.getOrElse(pais, 1.0)
      (pais, monto * tasa)
    }

    println("\n3. Montos convertidos a USD:")
    montosUSD.take(3).foreach { case (pais, monto) =>
      println(s"   $pais: $monto USD")
    }

    // 4. Agrupar por país: calcular estadísticas
    val estadisticasPais = montosUSD
      .map(x => (x._1, x._2, 1)) // (país, monto, count)
      .reduceByKey { case ((k1, v1, c1), (k2, v2, c2)) =>
        (k1, v1 + v2, c1 + c2) // Suma y conteo
      }
      .map { case (pais, (totalMonto, count)) =>
        (pais, totalMonto, count, totalMonto / count)
      }

    println("\n4. Estadísticas por país:")
    estadisticasPais.collect().foreach { case (pais, total, count, promedio) =>
      println(s"   $pais: Total=$total USD, Transacciones=$count, Promedio=$promedio USD")
    }

    // Alternativa más clara con groupByKey + map
    println("\n4B. Alternativa con groupByKey:")
    val estadisticasPais2 = montosUSD
      .groupByKey()
      .map { case (pais, montos) =>
        val listaMontos = montos.toList
        val total = listaMontos.sum
        val promedio = total / listaMontos.length
        val maximo = listaMontos.max
        (pais, total, promedio, maximo, listaMontos.length)
      }

    estadisticasPais2.collect().foreach { case (pais, total, prom, max, count) =>
      println(s"   $pais: Total=$total, Promedio=$prom, Máximo=$max, Vendimias=$count")
    }

    // 5. Ordenar por total descendente
    println("\n5. Top países por ventas Electronics:")
    val topPaises = estadisticasPais2.sortBy(_._2, ascending = false)
    topPaises.take(3).foreach { case (pais, total, _, _, _) =>
      println(s"   $pais: ${total} USD")
    }

    // 6. Análisis adicional: registros por fecha
    println("\n6. Ventas por fecha:")
    val ventasPorFecha = electronics
      .map(x => (x._1, x._3)) // (fecha, monto original)
      .reduceByKey(_ + _)
    
    ventasPorFecha.collect().foreach { case (fecha, total) =>
      println(s"   $fecha: $total (Electronics)")
    }

    // 7. Resumen final
    println("\n7. RESUMEN FINAL:")
    val totalVentas = montosUSD.map(_._2).sum
    val numTransacciones = montosUSD.count()
    val promedioTransaccion = totalVentas / numTransacciones
    
    println(s"   Total ventas (Electronics): ${totalVentas} USD")
    println(s"   Número de transacciones: ${numTransacciones}")
    println(s"   Promedio por transacción: ${promedioTransaccion} USD")
    println(s"   Países: ${estadisticasPais2.map(_._1).collect().mkString(", ")}")

    sc.stop()
  }
}
