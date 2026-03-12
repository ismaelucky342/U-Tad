# Bloque 3 — Mini-pipeline end-to-end (práctica)

Objetivo: construir un mini ETL local (sin Spark) usando las ideas de la unidad: modelado con `case class`, parseo robusto (`Option/Either/Try`), transformaciones sobre colecciones, y (opcional) lectura de fichero y asincronía con `Future`.

---

## Datos de entrada
Trabaja con líneas CSV (muy simple):

Formato: `producto,unidades,precio`

Ejemplo:
```text
A,2,10.0
B,1,15.0
A,3,10.0
C,10,1.25
A,x,10.0
MALFORMADA
```

---

## Ejercicio 1 — Modelo y parseo robusto
Define:
```scala
case class Venta(producto: String, unidades: Int, precio: Double)
```

Implementa:
- `def parseVenta(line: String): Either[String, Venta]`

Reglas:
- `producto`: `trim`, no puede quedar vacío.
- `unidades`: Int > 0.
- `precio`: Double >= 0.
- Si falla algo, devuelve un `Left` con un mensaje útil (y si puedes, incluye el `line`).

---

## Ejercicio 2 — Métricas del pipeline
Dada `ventas: List[Venta]`, calcula:
1. `totalIngresos: Double`
2. `ingresosPorProducto: List[(String, Double)]` ordenado desc
3. `productoTopUnidades: Option[(String, Int)]`

**Definición:**
- ingresos por venta = `unidades * precio`

---

## Ejercicio 3 — Informe final (salida)
Construye una función:
```scala
def renderInforme(
  ventasValidas: List[Venta],
  errores: List[String]
): String = ???
```

El informe debe incluir (formato libre, pero claro):
- número de líneas totales procesadas
- número de ventas válidas
- número de errores
- top 3 productos por ingresos
- total de ingresos

---

## Ejercicio 4 — Pipeline completo desde `List[String]`
Implementa:
```scala
def procesar(lineas: List[String]): (List[Venta], List[String]) = ???
```

Requisitos:
- No lances excepciones.
- No uses mutabilidad (intenta hacerlo todo con transformaciones).

**Pista:** mapea cada línea a `Either`, separa `Right` y `Left`.

---

## Ejercicio 5 (opcional) — Leer desde fichero
Implementa:
- `def leerLineas(path: String): Either[String, List[String]]`

Requisitos:
- Debe cerrar el fichero.
- Si hay error (no existe, permisos), devuelve `Left(mensaje)`.

Luego conecta con `procesar` y genera el informe.

---

## Ejercicio 6 (opcional) — Asincronía con `Future`
Crea:
- `def procesarAsync(lineas: List[String])(using ec: scala.concurrent.ExecutionContext): scala.concurrent.Future[String]`

Objetivo:
- Ejecutar el pipeline en `Future`.
- Devolver el informe (`String`).
- Manejar fallos del `Future` mostrando un mensaje controlado.

---

## Ejercicio 7 (conceptual) — Cómo sería en Spark
Sin escribir Spark real, responde:
- ¿Qué correspondería a `leerLineas` en Spark?
- ¿Qué transformación harías para limpiar/parsear?
- ¿Qué acción “dispararía” la ejecución?

---

### Checklist de bloque
- Pipeline: leer → parsear → limpiar → agregar → reportar.
- Errores no rompen el flujo (se recolectan).
- Salidas ordenadas y fáciles de validar.
