## Ejercicio 1 - **Scala simple** *(1,5ptos)*

Vamos a crear un ejemplo sencillo en Scala para demostrar que **el alumno sabe ejecutar un código Scala tanto en Ejecución interactiva desde la consola REPL (Modo Dinámico) como en ejecución de un archivo .scala compilado (Modo Estático).**

Escribe un programa en Scala que **lea un archivo de texto llamado frasescelebres.txt, convierta cada línea a minúsculas, invierta el orden de los caracteres de cada línea y guarde el resultado en un nuevo archivo llamado output.txt para la opción 1 que se comenta abajo y output2.txt para la opción 2.La ruta y nombre de los ficheros de entrada y salida tienen que ser variables de tipo val.**

**Pista: usa las funciones toLowerCase para convertir a minúsculas y reverse para invertir el orden de los caracteres en cada línea.**

Se pide:

1. Líneas de código y pantallazo de la ejecución del código en la consola REPL (Modo Dinámico). También el fichero salida output1.txt
2. Fichero .scala y pantallazo de la ejecución en modo compilado (Modo Estático). También el fichero salida output2.txt

[Icono de archivo] **frasescelebres.txt**

Ejemplo de salida esperada en ambos casos:

*nonnel nhoj - .senalp sorto odneicah odapuco satse sartneim asap euq ol se adiv alihdnag amtaham - .onimac le se zap al ,zap al arap onimac yah onseletotsira -.neib le recah ne etsisnoc dadicilef aredadrev alsboj evets - .secah euq ol rama se ojabart narg nu recah ed odom ocinu le*

### Resolución:

Vale, este ejercicio es un clásico para romper el hielo con **Scala**. No te asustes por los nombres raros ("REPL", "Modo Estático"), en realidad te están pidiendo hacer un "sándwich" de datos: abrir un archivo, transformar el texto y guardarlo en otro.

Aquí tienes la explicación desglosada para que entiendas cada paso.

---

### 1. Entendiendo la lógica (El "Algoritmo")

El ejercicio te pide tres transformaciones por cada línea del archivo `frasescelebres.txt`:

1. **Leer** la línea.
2. **Pasar a minúsculas**: usando `.toLowerCase`.
3. **Invertir el orden**: usando `.reverse`.
4. **Escribir** el resultado en un archivo nuevo.

---

### 2. El Código (Modo Estático / Archivo .scala)

Para el **punto 2** de tu examen (el modo compilado), necesitas crear un objeto contenedor. Así quedaría el código limpio:

```scala
import scala.io.Source
import java.io.PrintWriter

object ProcesarFrases {
  def main(args: Array[String]): Unit = {
    // Definimos las rutas como variables de tipo val (como pide el enunciado)
    val ficheroEntrada = "frasescelebres.txt"
    val ficheroSalida = "output2.txt"

    // 1. Abrimos el archivo de entrada
    val origen = Source.fromFile(ficheroEntrada)
    
    // 2. Preparamos el archivo de salida
    val destino = new PrintWriter(ficheroSalida)

    try {
      // 3. Procesamos línea a línea
      for (linea <- origen.getLines()) {
        val lineaProcesada = linea.toLowerCase.reverse
        destino.println(lineaProcesada)
      }
    } finally {
      // 4. Cerramos siempre los archivos para no dejar procesos colgados
      origen.close()
      destino.close()
    }
    
    println("Proceso finalizado con éxito.")
  }
}
```

Explicación de los comandos:

- **`Source.fromFile`**: Es la herramienta de Scala para "leer" archivos.
- **`PrintWriter`**: Es la herramienta más sencilla de Java (que Scala usa) para "escribir" texto en un archivo.
- **`val`**: Se usa para variables inmutables (que no cambian), tal como exige el profe.
- **`.getLines()`**: Nos permite recorrer el archivo frase por frase en lugar de cargarlo todo de golpe (muy eficiente).

---

### 3. Resolución para el Modo REPL (Modo Dinámico)

El **punto 1** te pide hacerlo en la consola interactiva. En el REPL no necesitas envolver todo en un `object` ni en un `def main`. Simplemente vas escribiendo línea a línea:

1. Escribe `scala` en tu terminal para entrar.
2. Pega este bloque:

```scala
import scala.io.Source
import java.io.PrintWriter

val in = "frasescelebres.txt"
val out = "output1.txt"

val lineas = Source.fromFile(in).getLines().toList
val procesadas = lineas.map(l => l.toLowerCase.reverse)

val writer = new PrintWriter(out)
procesadas.foreach(writer.println)
writer.close()
```

*(Aquí he usado `.map` porque en el REPL suele ser más rápido y limpio para demostrar que sabes usar programación funcional).*

---

### 4. Diferencias que te van a preguntar

- **Modo Dinámico (REPL):** Es como una conversación. Escribes código, pulsas Enter y se ejecuta al momento. Ideal para probar trozos de código rápidos.
- **Modo Estático (Compilado):** Creas un archivo `.scala`, lo compilas (con `scalac`) y generas un ejecutable. Es como se construyen las aplicaciones reales.

## Ejercicio 2 **- Colecciones con función superior** *(1pto)*

Dado el siguiente RDD en Spark:
`val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))`
Cada elemento es una cadena que representa una lista de números separados por comas.

Aplica transformaciones (utilizando **funciones superiores** sobre colecciones (por ejemplo, map, flatMap, fold, etc.) para procesar el RDD, y una acción para obtener el siguiente resultado: **"Suma total: 45"**

Implementa **dos versiones diferentes** que obtengan dicho resultado:

- **A)** En la **primera versión**, utiliza exclusivamente las funciones **map()** y **sum()** para calcular la suma total. *(0,5ptos)*
- **B)** En la **segunda versión**, realiza la suma utilizando exclusivamente las funciones **flatMap()**, **map()** y **fold()**. *(0,5ptos)*

**Se pide entregar el código bien pegado como respuesta o en un fichero .txt. También hay que incluir pantallazo de ambas ejecuciones.**

---

Este segundo ejercicio se mete de lleno en **Apache Spark**, que es la herramienta estrella para procesar grandes volúmenes de datos. Aquí el "truco" está en entender cómo transformar los datos de texto a números.

Tienes un RDD que contiene esto: `["1,2,3", "4,5", "6,7,8,9"]`.

Fíjate que son **Strings** (cadenas de texto) con comas. Para sumar los números, primero hay que "limpiar" y "separar".

Aquí tienes las dos versiones que pide el profe explicadas para que no se te olvide:

---

### Versión A: Usando `map()` y `sum()`

Esta versión es más directa. La idea es: por cada String, lo convierto en una lista de números y sumo esa lista.

```scala
val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

// 1. Convertimos cada String en la suma de sus números
val sumasParciales = data.map(cadena => {
  // split(",") separa por la coma: "1,2,3" -> ["1", "2", "3"]
  // toInt convierte el texto a número: "1" -> 1
  cadena.split(",").map(_.toInt).sum
})

// 2. Sumamos los resultados de todas las filas
val totalA = sumasParciales.sum()

println(s"Suma total: $totalA")
```

**¿Qué está pasando aquí?**

- Dentro del `map`, cada "línea" se convierte en un número (la suma de esa línea).
- Al final, el RDD resultante es algo como `[6, 9, 30]`. Al hacer `.sum()`, obtenemos el 45.

---

### Versión B: Usando `flatMap()`, `map()` y `fold()`

Esta es la versión más "profesional" en Big Data. En lugar de sumar línea por línea, vamos a poner **todos los números en una sola lista gigante** (aplanar) y luego sumarlos todos juntos.

```scala
val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

// 1. flatMap "rompe" las filas y pone todos los elementos juntos
// Pasa de ["1,2,3", "4,5"] a ["1", "2", "3", "4", "5"]
val todosLosStrings = data.flatMap(cadena => cadena.split(","))

// 2. Convertimos cada String suelto a entero
val todosLosNumeros = todosLosStrings.map(numero => numero.toInt)

// 3. Usamos fold para sumar. 
// El 0 es el valor inicial, y (acc, n) => acc + n es la regla de suma
val totalB = todosLosNumeros.fold(0)((acumulado, numero) => acumulado + numero)

println(s"Suma total: $totalB")
```

---

### Conceptos clave para el examen (Te los pueden preguntar):

1. **`map` vs `flatMap`**:
    - `map` devuelve un elemento por cada elemento de entrada (relación 1 a 1).
    - `flatMap` puede devolver varios elementos por cada uno de entrada (relación 1 a muchos), y al final los "aplana" todos en una sola lista.
2. **`fold(0)(...)`**: Es una acción que combina todos los elementos del RDD usando una función (en este caso la suma). El `0` es el valor de partida. Se usa mucho en Spark porque permite procesar datos en paralelo de forma segura.
3. **Transformación vs Acción**:
    - `map` y `flatMap` son **transformaciones** (no hacen nada hasta que pides un resultado).
    - `sum()` y `fold()` son **acciones** (aquí es donde Spark realmente se pone a trabajar y te da el número final).


## Pregunta 3 - Scala Avanzado (1,5 puntos)

Este ejercicio se compone de dos apartados que hacen uso de características especiales disponibles en Scala. Por simplificación se puede ejecutar por consola o compilado como prefiera el alumno.

### **Apartado A) Ejercicio Pattern matching junto con trait** *(0.75ptos)*

**Enunciado:** Dada una jerarquía de animales usando sealed trait, usa pattern matching para detectar si un animal es un **Gato de raza "persa"** e imprimir su nombre.

**Pasos:**

- Se declara un *sealed trait* (trait sellado) Animal, que actúa como supertipo común para una jerarquía cerrada de clases. La sentencia en concreto a usar es **sealed trait Animal**
- Se declaran las clases Perro y Gato extienden este trait e incorporan dos campos (nombre y raza).
- Se crea una instancia de Gato con nombre "Misu" y raza "persa", asignada a una variable de tipo Animal. La llamaremos **a**.
- Se instancia un Perro con nombre "Micki" y raza "bulldog", también asignado al tipo base Animal. La llamaremos **b**.
- Se aplica pattern matching primeramente sobre **a** para comprobar si es un Gato de raza "persa" y luego sobre **b**.

---

### **Apartado B) Cálculo del área de un círculo - versión clásica vs. funcional** *(0.75ptos)*

Recordamos que el área de un círculo es PI * radio ^2

Define una clase Circulo que contenga un atributo radio y permite calcular el área de dicho círculo.

**Parte B1 (0.25ptos) Versión clásica (orientada a objetos, sin lógica funcional):**
Implementa la clase Circulo de forma que incluya un método area() que calcule y devuelva el área del círculo. El cálculo debe estar dentro del objeto instanciado, sin usar programación funcional ni objetos compañeros.

**Parte B2 (0.5ptos) Versión funcional y con objeto compañero/acompañante**
Crea ahora un objeto llamado CalculadoraCirculo que actúe como companion object funcional (aunque no se llame igual que la clase). Este objeto debe contener una función pura que reciba una instancia de Circulo y devuelva su área. El cálculo no debe estar dentro de la clase. Pista: Recuerda que si te defines la clase como "case class" no hace falta el método apply.

**Probar ambas versiones con un círculo de radio 3**

**Se pide entregar el código bien pegado como respuesta o en un fichero .txt. También hay que incluir pantallazo de ambas ejecuciones**


---

## Apartado A) Pattern Matching y Jerarquías con `sealed trait`

El objetivo de este ejercicio es demostrar cómo Scala maneja la seguridad de tipos mediante "jerarquías cerradas".

### 1. Definición de la estructura

Al usar `sealed`, le decimos al compilador que todas las clases que extienden `Animal` deben estar en este mismo archivo. Esto permite que el compilador nos avise si olvidamos algún caso en el `match`.

```scala
// El trait "sellado" define la base común
sealed trait Animal[cite: 1]

// Las case classes son ideales para modelar datos y usar en pattern matching
// Ya incluyen automáticamente campos inmutables (val) y métodos como copy o equals
case class Perro(nombre: String, raza: String) extends Animal[cite: 1]
case class Gato(nombre: String, raza: String) extends Animal[cite: 1]

```

### 2. Lógica de detección (Pattern Matching)

El `pattern matching` funciona como un `switch` superpotente que puede "mirar" dentro de los objetos.

```scala
// Creamos las instancias solicitadas
val a: Animal = Gato("Misu", "persa")[cite: 1]
val b: Animal = Perro("Micki", "bulldog")[cite: 1]

// Función para procesar y detectar el patrón específico
def procesarAnimal(animal: Animal): Unit = {
  animal match {
    // Aquí buscamos específicamente un Gato donde el segundo campo sea "persa"
    case Gato(n, "persa") => 
      println(s"¡Detectado! Es un Gato de raza persa. Su nombre es: $n")[cite: 1]
    
    // Si es un Gato pero no persa
    case Gato(n, r) => 
      println(s"Es un gato llamado $n, pero es de raza $r.")
      
    // Si es cualquier otro animal (en este caso Perro)
    case _ => 
      println("No es un gato persa.")[cite: 1]
  }
}

// Ejecución
procesarAnimal(a) // Imprimirá el nombre Misu
procesarAnimal(b) // Indicará que no cumple el patrón

```

---

## Apartado B) Cálculo del área: Clásica vs. Funcional

Este ejercicio compara el estilo tradicional de **Programación Orientada a Objetos (POO)** frente al estilo **Funcional con Objetos Compañeros**.

### Parte B1: Versión Clásica (POO)

En este modelo, los datos (el radio) y el comportamiento (el método `area()`) viven juntos en el mismo objeto.

```scala
class Circulo(val radio: Double) {[cite: 1]
  // El método pertenece a la instancia (this)
  def area(): Double = {[cite: 1]
    // Usamos la constante PI y la función pow de la librería matemática
    scala.math.Pi * scala.math.pow(this.radio, 2)[cite: 1]
  }
}

// Para usarlo, instanciamos con 'new'
val circuloOO = new Circulo(3.0)[cite: 1]
println(s"Resultado OO: ${circuloOO.area()}")[cite: 1]

```

### Parte B2: Versión Funcional (Companion Object)

Aquí separamos los datos de la lógica. La `case class` solo guarda los datos, y un objeto externo realiza el cálculo mediante una **función pura** (una función que no cambia el estado, solo recibe algo y devuelve un resultado).

```scala
// 1. Definimos solo los datos (inmutables por defecto en case class)
case class CirculoFuncional(radio: Double)[cite: 1]

// 2. Definimos la lógica en un objeto "compañero" (Calculadora)
object CalculadoraCirculo {[cite: 1]
  // Esta es una función pura: depende solo de sus parámetros de entrada
  def calcularArea(c: CirculoFuncional): Double = {[cite: 1]
    scala.math.Pi * scala.math.pow(c.radio, 2)[cite: 1]
  }
}

// Para usarlo, no necesitamos 'new' gracias a la case class
val miCirculoFunc = CirculoFuncional(3.0)[cite: 1]
// Llamamos a la lógica pasando el objeto como parámetro
val resultado = CalculadoraCirculo.calcularArea(miCirculoFunc)[cite: 1]

println(s"Resultado Funcional: $resultado")[cite: 1]

```

---

### Resumen de diferencias clave:

* **En B1 (Clásico):** El objeto "sabe" calcular su propia área.


* **En B2 (Funcional):** El objeto es un simple contenedor de datos y existe una "herramienta" externa (`CalculadoraCirculo`) que sabe cómo procesar esos datos.