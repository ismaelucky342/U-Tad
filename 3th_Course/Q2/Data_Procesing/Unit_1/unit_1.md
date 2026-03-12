
# Unidad 1 — Scala para Procesamiento de Datos (resumen tipo temario)

## Introducción y objetivos

### Introducción
Esta unidad introduce Scala como lenguaje base para trabajar con pipelines de datos: transformar colecciones, modelar información de forma segura, manejar errores sin romper el flujo y preparar el terreno para frameworks del ecosistema (p. ej. Spark).

### Objetivos
- Entender qué es Scala y por qué es común en procesamiento de datos.
- Comparar el enfoque de Scala frente a Java (sintaxis, modelo de tipos, expresividad).
- Escribir código idiomático: inmutabilidad, funciones, case classes, pattern matching.
- Usar colecciones y funciones de orden superior para transformar datos.
- Manejar errores con `try/catch` y con enfoques más funcionales (`Option`, `Try`).
- Conocer frameworks habituales y una instalación típica (local o máquina virtual).

---

## Introducción

### ¿Qué es Scala?
Scala es un lenguaje que corre sobre la JVM y combina **programación orientada a objetos** y **programación funcional**.

Ideas clave:
- Todo es un objeto (incluso funciones).
- Se favorece la **inmutabilidad** (`val` en lugar de `var`).
- Tipado estático con inferencia: el compilador deduce tipos en muchos casos.
- Facilita escribir transformaciones de datos de forma compacta y segura.

### Comparativa de Scala frente Java
- **Verboso vs expresivo**: Scala suele necesitar menos “ceremonia”.
- **Inmutabilidad por defecto**: Scala empuja a `val`; en Java es más común mutar.
- **Null-safety**: Scala usa `Option` para evitar `null` en APIs idiomáticas.
- **Pattern matching**: Scala trae matching potente (muy útil al parsear datos).
- **Funciones de orden superior**: `map/filter/groupBy` son el pan de cada día.
- **Interoperabilidad**: puedes usar librerías Java desde Scala sin problema.

### Ejemplos prácticos de código Scala frente a Java

#### 1) Transformación de datos: filtrar y mapear

Scala:
```scala
val nums = List(1, 2, 3, 4, 5)
val paresCuadrado = nums.filter(_ % 2 == 0).map(n => n * n)
// Resultado: List(4, 16)
```

Java (estilo Streams):
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> paresCuadrado = nums.stream()
		.filter(n -> n % 2 == 0)
		.map(n -> n * n)
		.collect(Collectors.toList());
```

#### 2) Evitar `null`: `Option` vs null-checks

Scala:
```scala
def findUserName(id: Int): Option[String] = if (id == 1) Some("Ana") else None

val saludo = findUserName(2)
	.map(n => s"Hola, $n")
	.getOrElse("Hola, invitado")
```

Java (aprox. con Optional):
```java
Optional<String> findUserName(int id) {
		return id == 1 ? Optional.of("Ana") : Optional.empty();
}

String saludo = findUserName(2)
		.map(n -> "Hola, " + n)
		.orElse("Hola, invitado");
```

### Frameworks en Scala
En procesamiento de datos y back-end es habitual encontrar:
- **Apache Spark (Scala)**: procesamiento distribuido (ETL, batch/streaming).
- **Akka / Pekko**: concurrencia por actores.
- **Play Framework**: web/APIs.
- **Cats / ZIO**: librerías de programación funcional (tipos, efectos, etc.).

Nota rápida sobre Spark:
- La API más usada hoy es **DataFrame/Dataset** (optimizada por Catalyst).
- El patrón típico es: leer → seleccionar/limpiar → transformar → agregar → escribir.

### Instalación
Una instalación típica (fuera de MV) suele incluir:
- JDK (misma familia que use el curso/proyecto).
- Scala.
- sbt (herramienta de build).
- IDE (IntelliJ IDEA con plugin Scala o VS Code con Metals).

Si el curso usa MV, el objetivo es tener un entorno reproducible: misma versión de JDK/Scala/sbt y librerías.

---

## Introducción

### Descarga e importación de la MV
Checklist (genérico):
- Descargar la imagen (OVA/VMX) desde la plataforma del curso.
- Importar en VirtualBox/VMware.
- Verificar:
	- red (NAT/Bridge según instrucciones),
	- carpetas compartidas (si aplica),
	- memoria/CPU asignadas.
- Dentro de la MV, comprobar que existen herramientas:
	- `java -version`
	- `scala -version`
	- `sbt sbtVersion`

---

## Introducción

### Declaración de variables
- `val`: inmutable (preferida).
- `var`: mutable (usar cuando sea necesario).

```scala
val limite = 10
var contador = 0
contador += 1
```

### Tipos básicos
Tipos frecuentes: `Int`, `Long`, `Double`, `Boolean`, `Char`, `String`.

```scala
val edad: Int = 21
val ratio: Double = 0.75
val activo: Boolean = true
```

### Hello world en Scala
```scala
@main def hello(): Unit =
	println("Hello, Scala")
```

### Clases y objetos acompañantes
- Clase: define estado/comportamiento.
- Objeto acompañante (`object`): “singleton” con utilidades/constructores.

```scala
class User(val id: Int, val name: String)

object User:
	def anonymous(): User = new User(0, "anonymous")
```

### Opciones
`Option[A]` modela “puede no existir”: `Some(a)` o `None`.

```scala
def parseInt(s: String): Option[Int] =
	try Some(s.toInt) catch case _: NumberFormatException => None
```

### Funciones
- Sintaxis compacta.
- Se pueden pasar como parámetros.

```scala
def inc(x: Int): Int = x + 1
val doble: Int => Int = x => x * 2
```

### Case Classes
Útiles para modelar datos: inmutables, `equals/hashCode` automáticos, `copy`, pattern matching.

```scala
case class Venta(producto: String, unidades: Int, precio: Double)
```

### Traits
Similares a interfaces + implementación.

```scala
trait Logger:
	def info(msg: String): Unit
```

### Generics
Permiten reutilizar código con tipos parametrizados.

```scala
def headOption[A](xs: List[A]): Option[A] = xs.headOption
```

### Programación funcional
Principios prácticos en esta unidad:
- Evitar mutación cuando no aporta.
- Construir resultados mediante transformaciones (`map`, `flatMap`, `fold`).
- Funciones puras: mismo input → mismo output (cuando sea posible).

### Colecciones con función superior
Operaciones típicas en pipelines:
- `map`: transformar.
- `filter`: seleccionar.
- `groupBy`: agrupar.
- `reduce/fold`: agregar.

```scala
val ventas = List(
	Venta("A", 2, 10.0),
	Venta("B", 1, 15.0),
	Venta("A", 1, 10.0)
)

val ingresosPorProducto = ventas
	.groupBy(_.producto)
	.view
	.mapValues(vs => vs.map(v => v.unidades * v.precio).sum)
	.toMap
// Map("A" -> 30.0, "B" -> 15.0)
```

### For Comprehension
Azúcar sintáctico para combinar `map/flatMap/filter`, muy útil con `Option`, `Either`, colecciones.

```scala
val totalOpt: Option[Double] =
	for
		a <- Some(10.0)
		b <- Some(2.0)
	yield a / b
```

### Try-catch
Manejo clásico de excepciones.

```scala
def safeDivide(a: Double, b: Double): Double =
	try a / b
	catch case _: ArithmeticException => Double.NaN
```

> En enfoque funcional se suele preferir `Try` o `Either` para no lanzar.

### Otros elementos
- Interpolación de strings: `s"...$x"`.
- Pattern matching.
- `Either` para errores con información.
- `Future` para asincronía (con cuidado de hilos y errores).

---

## Introducción

### Ejemplo básico de Scala (mini-pipeline de datos)
Ejemplo: parsear líneas tipo CSV (simple), filtrar inválidas y calcular métricas.

Supongamos líneas: `producto,unidades,precio`.

```scala
case class Venta(producto: String, unidades: Int, precio: Double)

def parseVenta(line: String): Option[Venta] =
	line.split(",") match
		case Array(p, u, pr) =>
			val unidadesOpt = try Some(u.toInt) catch case _: NumberFormatException => None
			val precioOpt = try Some(pr.toDouble) catch case _: NumberFormatException => None
			for
				unidades <- unidadesOpt
				precio <- precioOpt
			yield Venta(p.trim, unidades, precio)
		case _ => None

val lineas = List(
	"A,2,10.0",
	"B,1,15.0",
	"A,x,10.0" // inválida
)

val ventas = lineas.flatMap(parseVenta)
val totalIngresos = ventas.map(v => v.unidades * v.precio).sum
```

### Ejemplo equivalente con Spark (DataFrame/Dataset)
Mismo objetivo, pero pensado para volúmenes grandes y ejecución distribuida.

```scala
import org.apache.spark.sql.{SparkSession, functions => F}

val spark = SparkSession.builder()
	.appName("unit-1")
	.master("local[*]")
	.getOrCreate()

// CSV con cabecera: producto,unidades,precio
val df = spark.read
	.option("header", "true")
	.option("inferSchema", "true")
	.csv("data/ventas.csv")

// Limpieza + métrica: ingresos = unidades * precio
val limpio = df
	.select(
		F.trim(F.col("producto")).as("producto"),
		F.col("unidades").cast("int").as("unidades"),
		F.col("precio").cast("double").as("precio")
	)
	.filter(F.col("producto").isNotNull && F.col("unidades").isNotNull && F.col("precio").isNotNull)

val ingresosPorProducto = limpio
	.withColumn("ingresos", F.col("unidades") * F.col("precio"))
	.groupBy("producto")
	.agg(F.sum("ingresos").as("ingresos_total"))
	.orderBy(F.desc("ingresos_total"))

ingresosPorProducto.show(false)
```

Idea clave: en Spark las transformaciones son *lazy* (se ejecutan al hacer una acción como `show`, `count`, `write`, etc.).

### Operaciones con colecciones
Patrones típicos:
- Normalizar: `map(_.trim.toLowerCase)`
- Deduplicar: `distinct`
- Ventanas y top-k: `sortBy(...).take(k)`

```scala
val topProductos = ventas
	.groupBy(_.producto)
	.view
	.mapValues(_.map(_.unidades).sum)
	.toList
	.sortBy { case (_, unidades) => -unidades }
	.take(3)
```

### Manejo de errores
Tres enfoques habituales:
- `try/catch` cuando interactúas con APIs que lanzan.
- `Option` si solo te importa “hay/no hay”.
- `Either[String, A]` si quieres mensaje/causa.

```scala
def parsePositivo(s: String): Either[String, Int] =
	try
		val n = s.toInt
		if n > 0 then Right(n) else Left("Debe ser > 0")
	catch case _: NumberFormatException => Left("No es un entero")
```

### Tipos genéricos
Ejemplo: función de agregación reutilizable.

```scala
def countBy[A, K](xs: List[A])(key: A => K): Map[K, Int] =
	xs.groupBy(key).view.mapValues(_.size).toMap

val conteoPorProducto = countBy(ventas)(_.producto)
```

### Extractores y patrones (pattern matching)
Muy útil para parsear y clasificar entradas.

```scala
def etiqueta(v: Venta): String = v match
	case Venta(_, unidades, _) if unidades >= 10 => "mayorista"
	case Venta("A", _, _) => "producto_A"
	case _ => "general"
```

### Ficheros
Lectura simple (para prácticas pequeñas). Para grandes volúmenes, normalmente usarías herramientas distribuidas (p. ej. Spark).

```scala
import scala.io.Source

def leerLineas(path: String): List[String] =
	val src = Source.fromFile(path)
	try src.getLines().toList
	finally src.close()
```

### Programación asíncrona
Con `Future` puedes ejecutar tareas sin bloquear. Idea: lanzar el cálculo y manejar éxito/fracaso.

```scala
import scala.concurrent.{Future, ExecutionContext}
import scala.util.{Success, Failure}

given ExecutionContext = ExecutionContext.global

def calcularTotalAsync(ventas: List[Venta]): Future[Double] = Future:
	ventas.map(v => v.unidades * v.precio).sum

calcularTotalAsync(ventas).onComplete {
	case Success(total) => println(s"Total: $total")
	case Failure(e)     => println(s"Error: ${e.getMessage}")
}
```

---

## Conclusiones de la unidad
- Scala permite expresar transformaciones de datos de forma compacta y legible.
- `val`, `Option`, `case class` y las operaciones sobre colecciones reducen errores comunes (mutación, `null`, parseos frágiles).
- Pattern matching y for-comprehensions facilitan parsear y encadenar pasos.
- Los conceptos de esta unidad son base directa para frameworks de datos como Spark.

