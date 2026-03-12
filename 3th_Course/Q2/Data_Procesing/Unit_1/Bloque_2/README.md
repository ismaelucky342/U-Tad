# Bloque 2 — Colecciones, agregaciones y manejo de errores (práctica)

Objetivo: practicar transformaciones típicas de pipelines: `map/filter/groupBy/fold`, `pattern matching`, `Either` y `Try`.

---

## Ejercicio 1 — Agregación por clave (`groupBy`)
Usa el modelo:
```scala
case class Venta(producto: String, unidades: Int, precio: Double)
```

Dada una lista `ventas`, calcula:
1. `unidadesPorProducto: Map[String, Int]`
2. `ingresosPorProducto: Map[String, Double]`

**Regla:** ingresos = `unidades * precio`.

---

## Ejercicio 2 — Top-K (ranking)
Con `unidadesPorProducto`, obtén el top 3 de productos por unidades.

**Salida sugerida:** `List(("A", 12), ("B", 8), ("C", 5))`

**Pista:** convierte el `Map` a lista y ordena por el valor descendente.

---

## Ejercicio 3 — `foldLeft` para totales
Sin usar `.sum` directamente, calcula:
- total de unidades
- total de ingresos

**Pista:** `ventas.foldLeft(0)((acc, v) => acc + v.unidades)` y similar para `Double`.

---

## Ejercicio 4 — Pattern matching: clasificador
Implementa:
```scala
def etiqueta(v: Venta): String = ???
```

Reglas (ejemplo):
- Si `unidades >= 10` → `"mayorista"`
- Si `producto == "A"` → `"producto_A"`
- Si `precio >= 1000` → `"premium"`
- En otro caso → `"general"`

**Nota:** decide un orden razonable de reglas y justifícalo con tests.

---

## Ejercicio 5 — Parseo con `Either` (errores con mensaje)
Implementa:
- `def parsePositivo(s: String): Either[String, Int]`

Reglas:
- Si no es entero: `Left("No es un entero")`
- Si es entero pero `<= 0`: `Left("Debe ser > 0")`
- Si es válido: `Right(n)`

Luego crea:
- `def parseVentaE(line: String): Either[String, Venta]`

Reglas:
- Si no tiene 3 campos → `Left("Formato inválido")`
- Usa `parsePositivo` para unidades
- Para precio, crea `parseDoubleE` que devuelva `Either[String, Double]`

**Objetivo final:**
- Procesar una lista de líneas y obtener:
  - lista de ventas válidas
  - lista de errores (mensajes)

---

## Ejercicio 6 — `Try` vs `Option`
Implementa dos versiones:
- `def parseIntOpt(s: String): Option[Int]`
- `def parseIntTry(s: String): scala.util.Try[Int]`

Comparación:
- ¿Cómo extraes un valor por defecto en cada caso?
- ¿Cómo transformarías el error a un mensaje con `Try`?

---

## Ejercicio 7 — Composición con for-comprehension (`Either`)
Implementa:
- `def dividirE(a: String, b: String): Either[String, Double]`

Reglas:
- Si `a` o `b` no son dobles → `Left("No es número")`
- Si `b == 0` → `Left("División por 0")`
- Si ok → `Right(a/b)`

**Pista:** usa `for ... yield ...` sobre `Either`.

---

### Checklist de bloque
- Sabes elegir entre `Option` / `Either` / `Try`.
- Haces agregaciones con `groupBy` y `foldLeft`.
- Usas pattern matching sin `if` en cascada.
