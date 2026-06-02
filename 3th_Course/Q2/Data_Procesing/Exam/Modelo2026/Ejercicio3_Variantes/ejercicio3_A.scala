/*
Ejercicio 3_A - Scala Avanzado: CASE CLASSES Y PATTERN MATCHING

Se pide implementar un programa Scala que demuestre el uso de:
1. Case classes para modelar datos
2. Pattern matching para procesarlos
3. Higher-order functions (map, filter, reduce)

Caso: Sistema de gestión de empleados

Requisitos:
- Crear una case class Empleado(nombre: String, departamento: String, salario: Int)
- Procesar una lista de empleados
- Agrupar por departamento
- Calcular salario promedio por departamento
- Mostrar resultados ordenados

Ejemplo de entrada:
List(
  Empleado("Ana", "IT", 3500),
  Empleado("Carlos", "RRHH", 2800),
  Empleado("Laura", "IT", 3200),
  Empleado("Marco", "RRHH", 2900),
  Empleado("Iris", "IT", 3400)
)

Salida esperada:
IT: €3366.67
RRHH: €2850.00
*/

case class Empleado(nombre: String, departamento: String, salario: Int)

val empleados = List(
  Empleado("Ana", "IT", 3500),
  Empleado("Carlos", "RRHH", 2800),
  Empleado("Laura", "IT", 3200),
  Empleado("Marco", "RRHH", 2900),
  Empleado("Iris", "IT", 3400)
)

// Versión 1: Usando groupBy y map
val promediosPorDepto = empleados
  .groupBy(_.departamento)
  .map { case (dept, emps) =>
    val promedio = emps.map(_.salario).sum / emps.length.toDouble
    (dept, promedio)
  }
  .toList
  .sortBy(_._1)

promediosPorDepto.foreach { case (dept, promedio) =>
  println(s"$dept: €${promedio.formatted("%.2f")}")
}

// Versión 2: Usando pattern matching en for-comprehension
val resultados = for {
  (dept, emps) <- empleados.groupBy(_.departamento)
  promedio = emps.map(_.salario).sum / emps.length.toDouble
} yield (dept, promedio)

resultados.toList.sortBy(_._1).foreach { case (dept, promedio) =>
  println(s"$dept: €${promedio.formatted("%.2f")}")
}

// Versión 3: Usando foldLeft (función más avanzada)
case class Estadistica(dept: String, totalSalario: Int, cantidad: Int)

val estadisticas = empleados.foldLeft(Map[String, (Int, Int)]()) { case (acc, emp) =>
  val (totalSalario, cantidad) = acc.getOrElse(emp.departamento, (0, 0))
  acc + (emp.departamento -> (totalSalario + emp.salario, cantidad + 1))
}

estadisticas
  .map { case (dept, (total, cant)) => (dept, total / cant.toDouble) }
  .toList
  .sortBy(_._1)
  .foreach { case (dept, promedio) =>
    println(s"$dept: €${promedio.formatted("%.2f")}")
  }
