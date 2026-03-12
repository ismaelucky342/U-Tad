# Bloque 1 — Fundamentos de Scala (práctica)

Objetivo: afianzar sintaxis básica, `val/var`, funciones, `case class`, `Option` y un primer contacto con transformaciones simples.

Recomendación: crea un pequeño proyecto `sbt` o usa un fichero `Main.scala` y ejecuta con `scala`/IDE.

---

## Ejercicio 1 — Variables y tipos
1. Declara:
   - un `val` `nombre` (String)
   - un `val` `anioNacimiento` (Int)
   - un `var` `visitasPerfil` (Int) inicializado a 0
2. Incrementa `visitasPerfil` 3 veces.
3. Calcula `edadAprox` como `2026 - anioNacimiento`.

**Salida esperada (formato libre):**
- Una línea que muestre nombre, edad aproximada y visitas.

---

## Ejercicio 2 — Funciones puras
Implementa:
- `def inc(x: Int): Int`
- `def doble(x: Int): Int`
- `def clamp(x: Int, min: Int, max: Int): Int` (si `x` está fuera del rango, lo lleva al límite)

**Pruebas rápidas:**
- `inc(4) == 5`
- `doble(7) == 14`
- `clamp(5, 0, 10) == 5`
- `clamp(-2, 0, 10) == 0`
- `clamp(99, 0, 10) == 10`

---

## Ejercicio 3 — `case class` para modelar datos
Crea:
```scala
case class Venta(producto: String, unidades: Int, precio: Double)
```

1. Crea una lista de 4 ventas.
2. Implementa una función:
   - `def ingresos(v: Venta): Double = v.unidades * v.precio`
3. Imprime cada venta junto con su ingreso.

**Extra:** usa `copy` para modificar las unidades de una venta y recalcular.

---

## Ejercicio 4 — `Option` (null-safety)
Implementa:
- `def parseInt(s: String): Option[Int]`
- `def parseDouble(s: String): Option[Double]`

**Requisitos:**
- Si no se puede parsear, devuelve `None` (sin lanzar).

**Pruebas rápidas:**
- `parseInt("10") == Some(10)`
- `parseInt("x") == None`
- `parseDouble("1.5") == Some(1.5)`

---

## Ejercicio 5 — For-comprehension con `Option`
Implementa:
- `def dividir(a: String, b: String): Option[Double]`

**Reglas:**
- Parsea `a` y `b` como `Double` usando tus funciones.
- Si alguno falla, devuelve `None`.
- Si `b == 0`, devuelve `None`.
- Si todo va bien, devuelve `Some(a/b)`.

**Pruebas rápidas:**
- `dividir("10", "2") == Some(5.0)`
- `dividir("10", "0") == None`
- `dividir("x", "2") == None`

---

## Ejercicio 6 — Transformaciones mínimas con colecciones
Dada una lista:
```scala
val nombres = List("  Ana ", "", "Pepe", "  maria", "MARIA ")
```
1. Normaliza: `trim` + pasar a minúsculas.
2. Elimina vacíos.
3. Deduplica.
4. Ordena alfabéticamente.

**Resultado esperado:** `List("ana", "maria", "pepe")`

---

## Ejercicio 7 — Mini-parseo de CSV (simple)
Dadas líneas tipo `producto,unidades,precio`:
```scala
val lineas = List(
  "A,2,10.0",
  "B,1,15.0",
  "A,x,10.0",
  "MALFORMADA"
)
```

Implementa:
- `def parseVenta(line: String): Option[Venta]`

**Reglas:**
- Si no hay 3 campos, `None`.
- Si unidades o precio no parsean, `None`.
- `producto` debe ir `trim`.

Luego:
- Obtén `ventas: List[Venta]` usando `flatMap(parseVenta)`.
- Calcula `totalIngresos`.

**Salida esperada:**
- `ventas` debe contener solo las líneas válidas.

---

### Checklist de bloque
- Usas `val` por defecto.
- Evitas `null` usando `Option`.
- Transformas listas con `map/filter/flatMap`.
