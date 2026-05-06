# Unidad 1. Introducción a Scala.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Introducción A Scala](#2-introducción-a-scala)
  - [2.1 Introducción](#21-introducción)
  - [2.2 ¿Qué es Scala?](#22-qué-es-scala)
  - [2.3 Comparativa de Scala frente Java](#23-comparativa-de-scala-frente-java)
  - [2.4 Ejemplos prácticos de código Scala frente a Java](#24-ejemplos-prácticos-de-código-scala-frente-a-java)
  - [2.5 Frameworks en Scala](#25-frameworks-en-scala)
  - [2.6 Instalación](#26-instalación)
- [3. Máquina Virtual Del Curso](#3-máquina-virtual-del-curso)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Descarga e importación de la MV](#32-descarga-e-importación-de-la-mv)
- [4. El Lenguaje Scala](#4-el-lenguaje-scala)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Declaración de variables](#42-declaración-de-variables)
  - [4.3 Tipos básicos](#43-tipos-básicos)
  - [4.4 Hello world en Scala](#44-hello-world-en-scala)
  - [4.5 Clases y objetos acompañantes](#45-clases-y-objetos-acompañantes)
  - [4.6 Opciones](#46-opciones)
  - [4.7 Funciones](#47-funciones)
  - [4.8 Case Classes](#48-case-classes)
  - [4.9 Traits](#49-traits)
  - [4.10 Generics](#410-generics)
  - [4.11 Programación funcional](#411-programación-funcional)
  - [4.12 Colecciones con función superior](#412-colecciones-con-función-superior)
  - [4.13 For Comprenhension](#413-for-comprenhension)
  - [4.14 Try-catch](#414-try-catch)
  - [4.15 Otros elementos](#415-otros-elementos)
- [5. Ejemplos](#5-ejemplos)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Ejemplo básico de escala](#52-ejemplo-básico-de-escala)
  - [5.3 Operaciones con collecciones](#53-operaciones-con-collecciones)
  - [5.4 Manejo de errores](#54-manejo-de-errores)
  - [5.5 Tipos genéricos](#55-tipos-genéricos)
  - [5.6 Extractores y Patrones](#56-extractores-y-patrones)
  - [5.7 Ficheros](#57-ficheros)
  - [5.8 Programación asíncrona](#58-programación-asíncrona)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



Esta unidad se centra en establecer una introducción sobre el lenguaje de programación Scala. No busca ser un curso de Scala ni un resumen del mismo. Proporciona una visión general fundamental del lenguaje comparándolo con el ecosistema de Java y deteniéndose en aquellos aspectos más relevantes y diferenciadores del mismo.  Scala es un lenguaje de alto nivel que se ejecuta sobre la JVM (Java Virtual Machine) y combina paradigmas de programación funcional e imperativa.

Entre las características clave abordadas se encuentran su soporte para clases y objetos compañeros, la declaración de variables inmutables y mutables, y la importancia de las opciones (Option) para manejar valores potencialmente nulos. Además, se exploran los conceptos de programación funcional, como funciones de orden superior, transparencia referencial y colecciones funcionales. También se introducen herramientas avanzadas como el pattern matching, traits y generics.

Scala va a ser el lenguaje base que emplearemos en las siguientes unidades con frameworks relacionados con el Big Data.

Los apartados a tratar en esta unidad didáctica serán:



- **Introducción a Scala**  
  ¿Por qué estudiamos primeramente el lenguaje de programación Scala en esta asignatura de Procesamiento de Datos? Porque Scala se ha convertido en una herramienta imprescindible en el mundo del tratamiento de datos. La razón principal es debida a que combina eficiencia, flexibilidad y una integración perfecta con tecnologías clave como Apache Spark.
- **Máquina virtual del curso**  
  Como se ha comentado, durante el curso trabajemos con un entorno el cual os hacemos disponible a través de una máquina virtual. En realidad, tendréis disponibles un par de ellas pero son equivalentes y os comentaré la principal diferencia en los videos posteriores.
- **El lenguaje Scala**  
  El objetivo de este capítulo es introducir los conceptos básicos del lenguaje Scala y su sintaxis, destacando las características que lo hacen ideal para la programación funcional y orientada a objetos.
- **Ejemplos**  
  A continuación, se presentan algunos ejemplos de código en Scala con características particulares. Estos no representan, ni mucho menos, el único tipo de código que se puede explorar o preguntar. Como bien sabéis, la programación se domina practicando, así que tomad estos ejemplos como una base para consolidar vuestro conocimiento en Scala.



#### Objetivos



1. Introducir el lenguaje Scala y su relación con la JVM: Comprender qué es Scala, sus características principales y su interoperabilidad con Java, incluyendo cómo aprovechar librerías y funciones ya existentes en este ecosistema.
2. Explorar los fundamentos de la programación funcional e imperativa en Scala: Entender cómo Scala permite combinar ambos paradigmas, destacando conceptos como inmutabilidad, transparencia referencial y funciones de orden superior.
3. Familiarizarse con características avanzadas del lenguaje: Aprender a usar herramientas como case classes, traits, pattern matching y generics, que hacen de Scala un lenguaje versátil y adaptable a diversos contextos.
4. Manejar estructuras de datos y colecciones funcionales: Dominar el uso de métodos como map, filter, reduce y fold para operar sobre colecciones y trabajar con datos de forma funcional y eficiente.
5. Practicar mediante ejercicios aplicados: Implementar ejercicios que refuercen conceptos clave, como la manipulación de listas, generación automática de datos, y lectura/escritura de archivos, promoviendo un aprendizaje práctico y aplicado.



## 2. Introducción A Scala



### 2.1 Introducción



![image](assets/cm6htzvmr004h3571l3j3z3pc-saat5d41.jpg)



¿Por qué estudiamos primeramente el lenguaje de programación Scala en esta asignatura de Procesamiento de Datos? Porque Scala se ha convertido en una herramienta imprescindible en el mundo del tratamiento de datos. La razón principal es debida a que combina eficiencia, flexibilidad y una integración perfecta con tecnologías clave como Apache Spark.

Si se tuvieran que detallar las razones para aprender el lenguaje Scala en una asignatura como ésta serían las siguientes:



- **Su interconexión con el framework Apache Spark**  
  - Como se ha comentado Apache Spark es una de las herramientas más populares y potentes para el procesamiento de datos a gran escala. Scala es el lenguaje principal con el cual se usa Spark, porque, de hecho, éste fue escrito originalmente en Scala. Por tanto es el lenguaje que proporciona la mejor experiencia de uso y desarrollo.
  - Es cierto que, como se verá más adelante, aunque Spark tiene APIs en Python (PySpark) y Java, con la API de Scala se obtiene:
    - Mejor rendimiento y velocidad de procesamiento.
    - Acceso completo a las características más avanzadas y recientes de Spark.
    - Aprovechamiento al máximo de módulos de Spark como Spark SQL para consultas estructuradas, Spark Streaming para procesado de datos en tiempo real o MLlib para realizar proyectos de aprendizaje automático.
- **Compatibilidad con el ecosistema de Big Data**  
  - Scala no solo es compatible con Spark, sino también con otras herramientas de Big Data como Kafka y Hadoop.
- **Flexibilidad para manejar datos estructurados y no estructurados**  
  - Scala es excelente para trabajar con estructuras de datos como listas, mapas y dataframes, que son fundamentales para el análisis y manipulación de datos.
  - No solo se destaca en el manejo de datos estructurados, como tablas relacionales y dataframes, sino que también es altamente eficiente en el procesamiento de datos no estructurados y semiestructurados, que representan una gran parte de la información generada hoy en día. Estos incluyen datos como textos, imágenes, vídeos, información extraídos de redes sociales, datos de sensores IoT o ficheros de log de servidores entre otros
- **Mejor rendimiento que otros lenguajes populares en Big Data**  
  - Aunque lenguajes como Python son populares para tareas de análisis de datos, Scala es significativamente más rápido porque compila a bytecode que se ejecuta en la JVM. Y como es de suponer esta velocidad es esencial en sistemas distribuidos
- **Preparación para la industria y el futuro profesional**  
  - Scala es un estándar en empresas líderes de tecnología como Twitter, LinkedIn, Netflix y muchas startups enfocadas en datos y machine learning.
  - Dominar Scala y Spark es un plus en el mercado laboral, ya que la demanda de habilidades en Big Data y procesamiento distribuido sigue creciendo.
- **Unifica paradigmas funcionales y orientados a objetos**  
  - Scala permite combinar paradigmas de programación funcional (ideal para manipular datos) y orientada a objetos (útil para modelar sistemas complejos). Esto ofrece a los estudiantes herramientas poderosas para resolver problemas en Big Data de forma flexible y eficaz



Podemos resumir por tanto que aprender Scala no solo es relevante para la asignatura, sino también esencial el trabajo profesional en los campos del  Big Data y del análisis de datos en general.



### 2.2 ¿Qué es Scala?



![image](assets/cm6hufyqz00ag3571nwkea0j3-Imagen2.jpg)



Scala es un lenguaje de programación moderno cuya clasificación como lenguaje se resume en la siguiente tabla:

| Aspecto | Clasificación |
| --- | --- |
| Paradigma | Multiparadigma. Combina los enfoques funcional y orientado a objetos en un solo lenguaje, permitiendo elegir el paradigma que mejor se adapte al problema. Scala es orientado a objetos totalmente , lo que significa que todo en Scala es un objeto, incluso los valores y tipos primitivos como Int o Boolean. Implementa clases, herencia, encapsulación y polimorfismo, además de admitir conceptos como companion objects y traits , que son similares pero más poderosos que las interfaces en Java. Scala soporta programación funcional , un paradigma que prioriza el uso de funciones puras, inmutabilidad y expresiones en lugar de sentencias. Permite también programación imperativa. |
| Tipado | Estáticamente tipado, con inferencia de tipos. Los tipos son verificados en tiempo de compilación, lo que reduce errores en tiempo de ejecución. Sin embargo, Scala tiene un sistema de inferencia de tipos (similar a Python) que permite omitir las declaraciones explícitas de tipos cuando el compilador puede inferirlos. |
| Modelo de Ejecución | Aunque es un lenguaje compilado (genera bytecode para la Java Virtual Machine), Scala también proporciona una consola donde se pueden escribir y probar fragmentos de código de forma inmediata, lo que recuerda a lenguajes interpretados como Python. Al ejecutarse sobre una JVM significa que puede ejecutarse en cualquier máquina que soporte Java, permitiendo también una integración con bibliotecas Java. |
| Nivel | Se trate de un lenguaje de Alto Nivel , al estar su sintaxis más cerca del lenguaje natural que del lenguaje máquina. |
| Interoperabilidad | Altamente interoperable con Java principalmente. Permite utilizar librerías Java directamente dentro del código Scala. |
| Según su Aplicación | Propósito general, con enfoque particular en Big Data. |

La siguiente imagen muestra el modelo de ejecución de Scala basado en la JVM:



![image](assets/cm6j8hhce000z357077s3n5h0-Imagen3.jpg)



Scala no es el único lenguaje, además de Java, que se pude ejecutar en la JVM. En la siguiente tabla se muestra algunos de ellos con sus características y la imagen refleja sus logotipos.

| Lenguaje | Paradigma | Características Clave | Casos de Uso |
| --- | --- | --- | --- |
| Groovy | Dinámico, OO | Sintaxis concisa, scripting, integración Java | Scripting, automatización, desarrollo web |
| Clojure | Funcional, Lisp | Inmutabilidad, concurrencia, minimalista | Big Data, sistemas concurrentes y distribuidos |
| JRuby | Dinámico, OO | Ruby sobre JVM | Desarrollo web con Ruby on Rails, integración Java |
| Jython | Dinámico | Python sobre JVM | Scripting, integración con bibliotecas Java |



![image](assets/cm6j8icl8002c3570szf87xsv-Imagen4.jpg)



### 2.3 Comparativa de Scala frente Java



La utilidad de este apartado reside en facilitaros vuestro aprendizaje de Scala a partir del conocimiento que ya tenéis del lenguaje Java mediante comparativas de diversos aspectos.

Scala y Java, son ambos lenguajes de programación que  se ejecutan sobre la JVM, aunque destacan por enfoques distintos: Mientras Java es un lenguaje orientado a objetos maduro y ampliamente adoptado, Scala combina programación funcional y orientada a objetos con una sintaxis más concisa y capacidades avanzadas como inferencia de tipos, pattern matching y concurrencia mejorada. La siguiente tabla muestra un resumen de la comparativa entre ambos lenguajes:

| Aspecto | Java | Scala |
| --- | --- | --- |
| Paradigma | Orientado a objetos. | Multiparadigma: combina programación funcional y orientada a objetos. |
| Nivel de Tipado / Inferencia de tipos | Estático, pero más rígido; requiere declarar tipos explícitamente. | Estático, con inferencia de tipos (no siempre es necesario declarar los tipos). |
| Sintaxis | Verbosa, requiere más código para realizar tareas simples. | Concisa y expresiva; permite realizar más con menos líneas de código. |
| Tipos Nativos | Utiliza tipos primitivos (int, float, double, etc.) que no son objetos, pero tienen equivalentes en su API de clases (Integer, Double, etc.). Esto genera una separación entre tipos primitivos y tipos de referencia. | No distingue entre tipos primitivos y tipos de referencia en su código. Todos los valores en Scala se comportan como objetos. |
| Inmutabilidad | Las estructuras de datos son mutables por defecto. | Promueve la inmutabilidad por defecto; estructuras inmutables son estándar. |
| Funciones de Orden Superior | No nativas hasta Java 8; introducidas con las interfaces funcionales. | Nativas y soportadas desde el inicio. |
| Compatibilidad con la JVM | Nativo, diseñado para ejecutarse en la JVM. | También se ejecuta en la JVM y puede usar cualquier biblioteca de Java. |
| Sobrecarga de Operadores | No soporta la sobrecarga de operadores. | Sí se permite la soporta sobrecarga de operadores. |
| Funciones Anidadas | No soporta funciones dentro de funciones. | Soporta funciones anidadas, facilitando la organización del código funcional. |
| Funciones como Elementos de Primera Clase | No soportado; las funciones son métodos estáticos o de instancia. | Soportado; las funciones son objetos.  Las funciones son tratadas como valores o entidades independientes, lo que permite: Asignar funciones a variables, pasar funciones como argumentos a otras funciones ydevolver funciones como resultados de otras funciones. |
| Programación Funcional | Introducida parcialmente en Java 8 (lambdas y Streams). | Totalmente soportada desde el inicio; funciones puras, lambdas, currying, etc. |
| Inmutabilidad | Las clases y colecciones son mutables por defecto. | Las clases y colecciones son inmutables por defecto (ejemplo: val lista = List(1, 2, 3)). |
| Case Classes | No soportadas. | Soportadas; permiten crear clases de datos con un mínimo de código y soporte para pattern matching. |
| Pattern Matching | Limitado (usualmente se realiza con if-else o switch). | Soporte nativo y avanzado; permite trabajar con estructuras complejas y case classes. Permite comparar un valor contra una serie de patrones y ejecutar un bloque de código específico según el patrón que coincida. Es similar a un switch o case en lenguajes como Java o C, pero mucho más potente y expresivo. |
| Tail Recursion | No optimizada automáticamente; las recursiones profundas pueden causar desbordamientos de pila. | Soporte completo con optimización de tail recursion, útil para algoritmos funcionales. Tail recursion (o recursión en la cola) es una forma de recursión en la que la última operación que realiza una función es llamar a sí misma, sin realizar ningún cálculo adicional después de esa llamada |
| Null Safety | Usa null, lo que puede causar errores de tiempo de ejecución (NullPointerException). | Introduce Option, Some, y None para manejar valores opcionales de manera segura. |
| Colecciones | APIs estándar (mutables), enriquecidas con Streams desde Java 8. | APIs ricas para colecciones inmutables y operaciones funcionales (map, filter, etc.). |
| Modelo de Concurrencia | Uso de threads y herramientas como ExecutorService o CompletableFuture. | Avanzado; incluye futures, promises y soporte para actores (por ejemplo, con Akka). |
| DSLs (Lenguajes Específicos de Dominio) | Difícil de implementar debido a su sintaxis rígida. | Excelente para DSLs; su flexibilidad permite crear lenguajes para tareas específicas. |
| Compatibilidad con Streams de Java | Total desde Java 8; permite manipular datos con Streams y métodos funcionales. Los Streams en Java son una API introducida en Java 8 que proporciona un modelo funcional para procesar colecciones de datos de manera declarativa y eficiente. Un Stream no es una estructura de datos, sino una secuencia de elementos que se pueden procesar de forma computacional, similar a un flujo continuo de datos. | Total desde Scala 2.12; pero ya incluye APIs nativas más avanzadas (map, flatMap, etc.). |
| Generics | Soportados con algunas limitaciones (erasure en tiempo de ejecución elimina los tipos genéricos). | Soportados con un sistema más rico, incluyendo type bounds (<:, >:, etc.). |
| Macros y Metaprogramación | No soportados nativamente. | Soporte para macros (permiten generar código en tiempo de compilación). |
| Sobrecarga de Métodos | Soportada, pero limitada a métodos normales. | Soportada; además, admite sobrecarga avanzada con valores por defecto en los parámetros. |
| Herencia Múltiple | No soportada directamente (se usa interfaces). | Soportada a través de traits, que combinan características de clases abstractas e interfaces. |
| Compatibilidad con Java | Total, ya que Java es el lenguaje base. | Total; Scala puede llamar a cualquier API de Java y viceversa. |
| Soporte en IDEs | Excelente soporte en IntelliJ IDEA, Eclipse y NetBeans. | Soporte sólido en IntelliJ IDEA y otros IDEs, pero más lento debido a su complejidad. |
| Testing | Herramientas comunes como JUnit y TestNG. | Compatible con JUnit y frameworks específicos como ScalaTest y Specs2. |
| Curva de Aprendizaje | Más fácil para principiantes, especialmente si ya tienen experiencia con lenguajes OOP. | Más empinada, debido a conceptos avanzados como funciones de orden superior y actores. |
| Velocidad de Ejecución | Muy eficiente, gracias a la JVM y la optimización de tipos primitivos. | Similar a Java, pero con una pequeña penalización al usar tipos de datos inmutables. |
| Modularidad | Introducida con Java 9 (module-info.java). | No tiene modularidad nativa; utiliza otras herramientas del ecosistema JVM (como SBT o Maven). |
| Uso en Big Data | Se puede usar con Apache Hadoop, pero no es el lenguaje principal para Apache Spark. | Es el lenguaje nativo de Apache Spark, ampliamente usado en Big Data. |

Debido a algunas de las diferencias mencionadas, y aunque Java y Scala tienen compatibilidad gracias a la JVM, las conversiones no siempre son directas debido a diferencias conceptuales y en las APIs subyacentes. Con las herramientas adecuadas (JavaConverters, StreamConverters), Scala facilita la interoperabilidad con Java, especialmente desde Scala 2.12. Sin embargo, en ciertos casos como varargs y colecciones, es necesario un manejo explícito para una integración fluida.

Algunas de las conversiones no directas son:



#### Tipos nativos



Por ejemplo, al trabajar con arrays de tipos primitivos, podría ser necesario realizar conversiones explícitas. Hay que recordar que Scala no tiene tipos primitivos y todo son objetos. A continuación, se muestra un ejemplo, que maneja un array de enteros:

Código Java



```java
public class JavaArrayExample {
    public static int sumArray(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }
}
```



Código Scala que emplea el anterior Código Java:



```scala
object ScalaExample {
  def main(args: Array[String]): Unit = {
    val scalaArray: Array[Int] = Array(1, 2, 3, 4, 5)

    // Convertimos explícitamente el Array[Int] de Scala a int[] de Java
    val javaArray: Array[Int] = scalaArray.map(_.toInt).toArray

    // Llamamos al método Java
    val result: Int = JavaArrayExample.sumArray(javaArray)

    println(s"La suma del array es: $result")
  }
}
```



En Scala, Array[Int] es un array de enteros manejado como objetos (java.lang.Integer). Por otro lado Java espera un array de tipos primitivos (int[]).  Para convertir, se usa map(_.toInt) para asegurarnos de que cada elemento se transforma explícitamente al tipo primitivo int, y .toArray para asegurar que se almacene en el formato correcto.

**Nota:** En Scala, el guion bajo (_) es un marcador de posición  (placeholder  en terminología técnica) que se utiliza para simplificar funciones anónimas (lambdas). _.toInt es una forma corta de escribir un lambda que convierte cada elemento de la colección a un entero. Se puede escribir de forma equivalente y explícita : map(element => element.toInt). Por tanto, el guion bajo es una forma corta y concisa de referirse al parámetro de una función anónima en Scala.



#### Varargs



O argumentos variables, que permiten pasar un número variable de argumentos a un método, tratándolos internamente como un array.

Aunque Scala puede llamar a métodos con varargs de Java, y viceversa, hay una ligera diferencia en cómo se representan los varargs internamente. Scala traduce los varargs como un Seq (secuencia), mientras que Java los ve como arrays (Array).

Para interoperar con métodos de Java, Scala requiere convertir explícitamente el Seq en un Array usando .toArray.

Adicionalmente los varags se definen de forma diferente en ambos lenguajes. En Java se emplean los tres puntos y en Scala el asterisco:

Java:



```groovy
public void printAll(String... args) {
    for (String arg : args) {
        System.out.println(arg);
    }
}

Scala:

def printAll(args: String*): Unit = {
    args.foreach(println)
}
```



#### Collections



Java tiene su propia API de colecciones en el paquete java.util (como List, Set, Map) y son mutables por defecto. Scala las tiene en el paquete scala.collection y son inmutables por defecto. Si se desea utilizar las collections mutables en Scala hay que usar las del subpaquete scala.collection.mutables

Desde Scala 2.13 están disponibles las clases JavaConverters.asJava y JavaConverters.asScala para convertir entre colecciones Scala y Java.

Ejemplo:



```scala
import scala.jdk.CollectionConverters._

val javaList: java.util.List[Int] = List(1, 2, 3).asJava
val scalaList: List[Int] = javaList.asScala.toList
```



#### Funciones de orden superior



Las funciones de orden superior son funciones que pueden hacer una de las siguientes cosas (o ambas):

- Recibir otras funciones como parámetros.
- Devolver una función como resultado.

Esto permite un estilo de programación funcional en el que las funciones se tratan como elementos de primera clase, lo que significa que se pueden pasar, almacenar y manipular como cualquier otro valor.

Java 8 introdujo las expresiones lambda y las interfaces funcionales, lo que permite tratar las funciones como objetos. Sin embargo, las funciones en Java siempre deben implementarse como instancias de interfaces funcionales (como Runnable o Function).

Scala tiene soporte nativo para funciones de orden superior desde el principio. Desde Scala 2.12, las funciones Scala se convierten automáticamente a interfaces funcionales de Java.



#### Streams



Java los introduce a partir de la versión 8 (API en  java.util.stream), mientras que Scala utiliza su propia API funcional en colecciones (map, filter, reduce, etc.).

Desde Scala 2.12, se pueden convertir colecciones de Scala en streams de Java utilizando JavaConverters. Ejemplo:



```scala
import scala.jdk.StreamConverters._
val scalaList = List(1, 2, 3, 4, 5)
val javaStream = scalaList.toJavaStream
val scalaBack = javaStream.iterator().asScala.toList
```



Respecto a las diferencias sintácticas, la siguiente tabla las resume y muestra cómo Scala simplifica y flexibiliza varias operaciones comunes en comparación con Java.

| Aspecto | Java | Scala |
| --- | --- | --- |
| Punto y coma | Obligatorio al final de las sentencias (;). | Opcional; normalmente no se usa. |
| Nombres de tipos | Tipos en minúsculas (int, double, boolean). | Tipos en mayúsculas (Int, Double, Boolean). |
| Declaración de parámetros y retorno | Los tipos preceden a los nombres de variables (int x). | Los tipos van después de las variables (x: Int). |
| Declaración de métodos | No requiere palabra clave específica. | Los métodos deben ser precedidos por def. |
| Mutabilidad de variables | No distingue explícitamente entre mutables e inmutables. | Usa val (inmutable) y var (mutable). |
| Valor de retorno | Necesita el operador return. | El valor de la última expresión se devuelve implícitamente. |
| Casting | Usa (Type) foo para convertir tipos. | Usa foo.asInstanceOf[type] o funciones como toInt y toDouble. |
| Importación de paquetes | Usa import foo.*. | Usa import foo._. |
| Llamadas a métodos | Los métodos deben llamarse con paréntesis (foo()). | Los paréntesis son opcionales si no hay argumentos (foo). Admite sintaxis infija (thread send signo). |



**Nota:** Recordad que en programación se emplea comúnmente el término foo para representar variables, funciones, métodos, o elementos cuyo nombre específico no es relevante

En resumen, Scala y Java, aunque diferentes, son interoperables: se pueden usar clases y funcionalidades de Java en Scala y viceversa.



### 2.4 Ejemplos prácticos de código Scala frente a Java



Veamos a continuación un par de ejemplos implementados en Java y en Scala para poder comparar la sintaxis. En capítulos posteriores se entra al detalle del lenguaje Scala, es por ello que el objetivo de estos ejemplos más que enseñar a programar en Scala, es hacer notar las diferencias entre ambos lenguajes.



#### Ejemplo 1: Obtener el promedio de dos números:



#### Solución con Java



```groovy
double calculateAverage(double a, double b) {
    return (a + b) / 2.0;
}
```



#### Solución con Scala (traducción literal de Java)



```groovy
def calculateAverage(a: Double, b: Double): Double = {
  return (a + b) / 2.0
}
```



#### Solución con Scala (pero con estilo Scala puro o más idiomático)



```coffeescript
def calculateAverage(a: Double, b: Double): Double = (a + b) / 2.0
```



Es importante señalar en esta versión la eliminación del return, por tener un uso explícito en Scala.La última expresión de una función en Scala se devuelve automáticamente, por lo que el código puede ser más conciso.

Ambos ejemplos destacan cómo Scala permite simplificar las funciones eliminando la mutabilidad, el uso explícito de return y beneficiándose de la inferencia de tipos. Además, estas diferencias reflejan la naturaleza funcional e inmutable de Scala frente a la programación orientada a objetos clásica de Java.



#### Ejemplo 2: Creación de una clase para modelar un rectángulo



#### Solución con Java



```java
public class Rectangle {
    private final double width;
    private final double height;

    // Constructor
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

// Método para calcular el área
    public double area() {
        return width * height;
    }

    // Getters
    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }
}

// Llamada en Java
Rectangle rect = new Rectangle(5.0, 10.0);
System.out.println("Area: " + rect.area());
```



#### Solución con Scala (traducción literal de Java)



```scala
class Rectangle(val width: Double, val height: Double) {
  // Método para calcular el área
  def area(): Double = {
    return width * height
  }
}

// Llamada en Scala (versión traducida)
val rect = new Rectangle(5.0, 10.0)
println(s"Area: ${rect.area()}")
```



#### Solución con Scala (pero con estilo Scala puro o más idiomático):



```scala
class Rectangle(val width: Double, val height: Double) {
  // Método para calcular el área (sin return)
  def area: Double = width * height
}

// Llamada en Scala (versión idiomática)
val rect = new Rectangle(5.0, 10.0)
println(s"Area: ${rect.area}")
```



### 2.5 Frameworks en Scala



Un framework es un conjunto de herramientas, bibliotecas y reglas que facilita el desarrollo de software, proporcionando estructuras de datos y soluciones predefinidas.

Scala, gracias a su naturaleza híbrida de programación funcional y orientada a objetos, ha fomentado el desarrollo de múltiples frameworks que complementan su funcionalidad. Entre los más destacados se encuentran **Akka**, **Play Framework** y **Apache Spark**, cada uno diseñado para resolver necesidades específicas de desarrollo y procesamiento de datos.



![image](assets/cm6jar5jm00r93570z4ucf595-Imagen5.jpg)

- **Akka**  
  Akka es una herramienta para crear aplicaciones que necesitan manejar muchas tareas al mismo tiempo, como sistemas distribuidos o concurrentes. Utiliza el modelo de actores, que permite enviar mensajes entre partes del sistema de forma eficiente y confiable, incluso cuando hay fallos.
- **Play Framework**  
  Play Framework se emplea para crear aplicaciones web y APIs. Es rápido, fácil de usar y permite trabajar de forma reactiva, manejando muchas peticiones al mismo tiempo sin bloquear recursos. Además, facilita el desarrollo gracias a su capacidad de recargar cambios al instante.
- **Apache Spark**  
  Apache Spark es una plataforma para procesar grandes cantidades de datos de forma rápida y eficiente. Está diseñada para el análisis de datos, aprendizaje automático y procesamiento de flujos en tiempo real. En unidades posteriores nos centraremos en este framework.



### 2.6 Instalación



En este curso, utilizaremos una **máquina virtual** preconfigurada para facilitar la experiencia de aprendizaje y asegurar que todos los estudiantes trabajen en un entorno uniforme. Posteriormente, se indicará dónde descargar esta máquina virtual y cómo importarla en tu sistema. Sin embargo, como futuros ingenieros de software, es importante que también sepan instalar Scala de forma local, ya que esta habilidad puede ser útil en situaciones donde sea necesario configurarlo directamente en sus equipos.



#### Instalación local de Scala



> La instalación de Scala en local puede realizarse mediante varios métodos explicados en su página oficial
>
> [Link](https://www.scala-lang.org/download/)



En esta web se detalla cómo instalar Scala utilizando diferentes herramientas y en diferentes Sistemas Operativos, o mediante la descarga directa del paquete comprimido en formato .tar.gz.



#### Uso del simulador web Scastie



Para quienes deseen experimentar con Scala sin necesidad de instalarlo, existe una alternativa muy práctica: Scastie. Se trata es un simulador web accesible desde LINK: [https://scastie.scala-lang.org](https://scastie.scala-lang.org),  donde se puede escribir y ejecutar código Scala directamente en el navegador.

Scastie es especialmente útil para realizar pruebas rápidas o aprender los conceptos básicos del lenguaje al menos al inicio, ya que no requiere ninguna instalación local. Proporciona un entorno completo con soporte para múltiples versiones de Scala, además de incluir bibliotecas adicionales para probar diferentes casos de uso. Sin embargo, se recomienda usarlo como una herramienta complementaria, y se recuerda que en este curso se utilizará la Máquina virtual facilitada como entrono de trabajo.

A modo de pruebe se puede ver en el siguiente video la ejecución de los ejemplos prácticos de Scala vs Java ya visto en apartados anteriores,  en el entorno simulado de Scastie.

A continuación, estaría el video correspondiente al primer ejemplo de cálculo de la media:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%201%20Scastie%201.mp4?v=1)



Por otro lado, el siguiente video muestra la ejecución del segundo ejemplo con la clase rectángulo.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%202%20Scastie%202.mp4?v=1)



## 3. Máquina Virtual Del Curso



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Como se ha comentado, durante el curso trabajemos con un entorno el cual os hacemos disponible a través de una máquina virtual. En realidad, tendréis disponibles un par de ellas pero son equivalentes y os comentaré la principal diferencia en los videos posteriores.



### 3.2 Descarga e importación de la MV



Hay dos carpetas con dos máquinas virtuales, que podrás descargarte en el contenido de la unidad.

En el siguiente video se comenta las características de la primera.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%203%20MV%201.mp4?v=1)



En este otro video se analiza la segunda. Para el curso es suficiente con trabajar con una de ellas aunque el alumno debe conocer las diferencias.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%204%20MV%202.mp4?v=1)



En este otro video se analiza la segunda. Para el curso es suficiente con trabajar con una de ellas aunque el alumno debe conocer las diferencias.



## 4. El Lenguaje Scala



### 4.1 Introducción



![image](assets/cm6jbkknd017f35705vqv8gcg-stock-image.jpg)



Este capítulo no tiene como objetivo ser un manual exhaustivo del lenguaje Scala, sino más bien proporcionar una visión general de sus aspectos más importantes y diferenciadores. Dado que ya habéis adquirido experiencia con varios lenguajes de programación, es importante recordar que la mejor manera de aprender a programar es, precisamente, programando. Por ello, además de los ejercicios propuestos en este capítulo, se recomienda que los alumnos dediquen tiempo adicional a practicar con ejercicios propios. Para profundizar en el aprendizaje, se sugiere inicialmente la documentación propia de scala los tours que ofrece en el enlace: LINK: [https://docs.scala-lang.org/tour/tour-of-scala.html](https://docs.scala-lang.org/tour/tour-of-scala.html). Adicionalmente en la misma web se recomiendan varios libros LINK: [https://docs.scala-lang.org/books.html](https://docs.scala-lang.org/books.html) además de los incluidos en la bibliografía de la asignatura.  Asimismo, se recuerda que las populares cheatsheets son un recurso ampliamente utilizado en el ámbito de la programación, ya que permiten acceder rápidamente a información clave del lenguaje y facilitan la resolución de dudas durante el desarrollo de código.

Por tanto, el objetivo de este capítulo es introducir los conceptos básicos del lenguaje Scala y su sintaxis, destacando las características que lo hacen ideal para la programación funcional y orientada a objetos.



### 4.2 Declaración de variables



Scala permite declarar variables de dos formas principales: val y var.

En el caso de **val**(inmutable), una vez asignado un valor, este no puede ser modificado. Ejemplo:



```ini
val pi = 3.14
pi = 3.15 // Error: reassignment to val
```



La inmutabilidad es un pilar en la programación funcional, ya que reduce errores al evitar estados cambiantes.

Por otra parte, con **var**(mutable): Su valor puede ser reasignado posteriormente. Ejemplo:



```ini
var counter = 0
counter = 1 // Válido
```



Scala permite la inferencia de tipos, donde el compilador deduce automáticamente el tipo de una variable en función del valor que se le asigna. En este caso, Scala deduce que counter es de tipo Int, porque el valor asignado (0) es un entero. Esto simplifica la escritura del código y mejora la legibilidad en muchos casos.

Adicionalmente también se pueden declarar explícitamente los tipos de las variables. Esto significa que el programador especifica el tipo de dato que la variable debe contener. Por ejemplo:



```ini
var mutableVariable: String = "InitialValue"
val inmutableVariable: String = "InmutableValue"
```



### 4.3 Tipos básicos



Scala soporta una variedad de tipos de datos básicos, siendo los principales: enteros, string, boolean y float.

Ejemplos:

- **Enteros (Int):** Representa números enteros.



```kotlin
val age: Int = 25
println(age) // 25
```



- **Cadenas de texto (String):** Representa texto.



```scala
val name: String = "Scala"
println(name) // Scala
```



- **Booleanos (Boolean):** Puede ser true o false.



```ini
val isFunctional: Boolean = true
println(isFunctional) // true
```



- **Números decimales (Float):** Representa números con punto flotante (decimales) con precisión simple. Para valores con mayor precisión, se utiliza el tipo Double.



```bat
val pi: Float = 3.14f // Nota: Es necesario agregar la 'f' al final para indicar que es un Float
println(pi) // 3.14
```



Esto se debe a que, por defecto, los números decimales en Scala se interpretan como **Double**(doble precisión). Sin la f, Scala intentará asignar un valor de tipo **Double al Float,** lo que generará un error de compilación.

Así por tanto:



```ini
val pi: Float = 3.14  // Error: type mismatch; found: Double, required: Float
val pi: Float = 3.14f // Correcto
```



Una alternativa sería:



```bat
val pi: Float = 3.14.toFloat
```



Sin embargo, hay que tener claro que Scala es un lenguaje puramente orientado a objetos. Esto significa que incluso los tipos de datos básicos, como Int, String o Boolean, son instancias de clases. Por ejemplo, el tipo Int es una clase que hereda de AnyVal, una clase base para los tipos de valores. Del mismo modo, String es simplemente una clase de la biblioteca estándar de Java.

La siguiente imagen muestra la jerarquía de tipos en Scala, donde todos los tipos derivan de la clase raíz Any.



![image](assets/cm6jc34zt01q53570u3pcmaph-Imagen8.jpg)



1. **Any:** La superclase de todos los tipos en Scala. Dicho de otro modo, todas las demás clases en Scala son, de forma explícita o implícita, subclases de Any. La clase Any define algunos métodos estándar, como equals, hashCode y toString, los cuales están accesibles por defecto para todos los objetos en Scala.

Para comprobarlo vamos a ver un ejemplo: definicmos una función llamada any que reciba un argumento de tipo Any, lo que significa que puede aceptar un valor de cualquier tipo (números, cadenas, objetos, etc.), ya que Any es la clase raíz en la jerarquía de tipos de Scala. Devuelve un String que es la cadena vacía.  Aprovechamos también para indicar que Scala es  “case sensitive”.



```ini
def any(value: Any): String = ""
```



Podemos llamar a dicha función con diferentes argumentos y no vamos a tener ningún problema porque cualquier clase en el fondo es del tipo Any.



```kotlin
assert(any(5) == "")
assert(any(3.14) == "")
assert(any(false) == "")
assert(any("C") == "")
assert(any("Hola") == "")
```



En Scala, la función assert se utiliza para realizar comprobaciones durante la ejecución del programa. Su propósito es verificar que una condición dada sea verdadera. Si la condición resulta ser falsa, lanza una excepción del tipo java.lang.AssertionError.

El siguiente video muestra la funcionalidad de la función assert:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%205%20Assert.mp4?v=1)



**La clase Any tiene dos subclases principales:**

- **AnyVal:** Para tipos de valor (primitivos). Por tanto, es la clase raíz de todos los tipos de valor en Scala. En Scala, existen nueve clases para representar los tipos primitivos: Byte, Short, Char, Int, Long, Float, Double, Boolean y Unit. Son similares a los tipos primitivos de Java, con la excepción de la clase Unit. La clase Unit es equivalente al tipo Void en Java. No obstante, hay que tener en cuenta que el enfoque de Unit es ligeramente diferente en Scala al enfoque del Void en Java. En Java, el tipo Void se usa para indicar que un método **no devuelve ningún valor útil**. Por ejemplo, un método como:



```java
public void imprimir() {
    System.out.println("Hola");
}
```



Es un método que no devuelve nada. Void no tiene un valor concreto asociado. No existe ninguna "instancia" de Void. Simplemente significa "nada".

Sin embargo, en Scala Unit sí tiene un valor concreto y definido, que es ( ) (un paréntesis vacío). Este valor es la única instancia posible de la clase Unit.

Por ejemplo, un método en Scala que no devuelva nada útil tendría el tipo Unit y siempre retornará ().

Ejemplo:



```kotlin
def imprimir(): Unit = {
  println("Hola")
}
```



Al llamar el método en Scala se obtiene:



```kotlin
imprimir()
// Salida: Hola
// El valor retornado implícitamente es ()
```



La siguiente tabla muestra de forma resumida la comparativa entre el Void de Java y el Unit de Scala:

| Aspecto | Java (Void) | Scala (Unit) |
| --- | --- | --- |
| Definición | Es un tipo abstracto sin instancia. | Es un tipo concreto con una instancia. |
| Instancia | No tiene instancia. | Su única instancia es () . |
| Uso | Indica ausencia de valor. | También indica ausencia de valor, pero siempre retorna () como representación. |
| Comportamiento | No puedes asignar un valor de tipo void . | Puedes asignar () a una variable de tipo Unit . |



Veamos otro ejemplo con otro tipo de variable:



```scala
def myanyValFunc(value: AnyVal): String = ""
val myint: Int = 25
assert(myanyValFunc(myint) == "")
```



La función myanyValFunc toma un parámetro llamado value de tipo AnyVal y devuelve un valor de tipo String, siendo en este caso siempre la cadena vacía. Se declara la variable myint de tipo Int  asignándole el valor 25. Recordemos que en Scala, el tipo Int es una subclase de AnyVal. Por lo tanto, puede pasarse como argumento a la función myanyValFunc. Finalmente, la aserción verifica que la salida sea igual a una cadena vacía. Dado que todas las condiciones son correctas, el programa no genera ninguna salida en consola. Simplemente se ejecuta sin errores. Si se quisiera ver la salida se podría ejecutar:



```bat
println(myanyValFunc(myint)) // Salida: ""
```



- **AnyRef:** Para tipos de referencia (cualquier clase o tipo de objeto, como String). Es similar a la clase Object en Java, y podemos instanciar clases de referencia utilizando la palabra clave new.

A continuación, se muestra un video con un código ejemplo en el cual se emplea Anyref



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%206%20Anyref.mp4?v=1)



Por último, y relacionado con la imagen de jeraquía de clases visto anteriormente comentar que en Scala, Null está en la base de los tipos de referencia (AnyRef) y se utiliza para representar la ausencia de un valor. Se puede asignar el literal null a cualquier tipo de referencia, pero **no** es compatible con los tipos de valor (AnyVal), como es el caso de  Int .

Ejemplo:



```scala
val cadena: String = null // Es válido porque String es un tipo de referencia.
println(cadena)           // Salida: null
val numero: Int = null // ERROR: Type mismatch. Found: Null, required: Int
```



En cambio, Nothing es el tipo más bajo en la jerarquía de Scala y el hijo de todos los tipos, incluido Null. No tiene valor ni puede asignarse a variables, y se usa para indicar casos extremos como errores o listas vacías (List[Nothing]). Representa "nada" en su forma más absoluta.



### 4.4 Hello world en Scala



A continuación, se muestra el código de Scala para implementar el “Hello World”. Se aprovecha el ejemplo para :

- Mostrar la diferencia ente ejecución compilada y desde la consola REPL.
- Comentar los aspectos básicos de entrada y salida.
- Indicar cómo se ponen comentarios en Scala.
- Código extendiendo clase App frente al uso de main.

En el REPL de Scala no necesitas crear un objeto ni un método main porque el REPL actúa como un intérprete interactivo que ejecuta cada línea o fragmento de código directamente en un contexto implícito, mientras que al escribir código en un archivo Scala (modo estático) necesitas estructurarlo siguiendo las reglas de compilación y ejecución de Scala.

La siguiente tabla resume las diferencias entre ambos modos de ejecución:

| Característica | REPL | Archivo .scala |
| --- | --- | --- |
| Ejecución directa | Sí, línea por línea | No, requiere compilación |
| Punto de entrada ( main ) | No es necesario | Obligatorio |
| Objeto necesario | No, el REPL lo genera implícitamente | Sí, debes definirlo explícitamente |
| Compilación | Interna y dinámica | Requiere compilación explícita |
| Uso | Experimentación rápida | Programas estructurados |

Respecto a la salida de datos en Scala, para mostrar mensajes en la consola se puede emplear println, que añade al mensaje un salto de línea a final, o print que no añade dicho salto o printf que permite formatear la salida. Esta última opción se mantiene por compatibilidad con otros lenguajes, pero hay que saber que la forma más correcta y modelar de formatear salida en Scala es mediante la interpolación de cadenas interpolación de cadenas, es decir, formatear cadenas directamente dentro de un string como se muestra en el siguiente ejemplo:



```bat
val nombre = "Carlos"
val year = 2025
val porcentaje = 90.25

// Usando interpolación de cadenas
println(f"Hola, mi nombre es $nombre, estamos en el año $year y aun nos queda mucho para llegar al $porcentaje%.2f%% del temario.")
```



Recordad que para ejecutar este código tenemos dos opciones:



#### Grabar el código en un fichero Scala como muestra la siguiente imagen

1. ![image](assets/cm6jf6agk02ty3570z1gb1dqz-step1-Imagen9.jpg)
   Posteriormente ejecutar scalac (compilador) sobre el fichero que contiene el código. Esto nos genera un archivo HelloWorld.class en el directorio actual. Finalmente ejecutamos el programa con el comando scala.
2. ![image](assets/cm6jf6agk02ty3570z1gb1dqz-step2-Imagen14.jpg)
   Esta forma de ejecutar se conoce como ejecución de un archivo compilado (Modo Estático). En un archivo .scala, estás escribiendo un programa estructurado para ser compilado y ejecutado por la JVM, lo que requiere seguir las reglas específicas de Scala y la JVM (es decir, definir un objeto con un método main).



#### Ejecución interactiva desde la consola REPL (Modo Dinámico)
Scala tiene un REPL (Read-Eval-Print Loop), que es un entorno interactivo donde puedes escribir y ejecutar comandos de Scala en tiempo real, sin necesidad de crear un archivo. En este caso, como se puede ver en la siguiente imagen, basta con ejecutar el comonda scla para entrar a la consola e ir ejecutando las diferentes líneas. Al terminar se ejecuta :q para salir de la consola.

1. ![image](assets/cm6jfcckc02xx3570hx2ngpv6-step1-Imagen15.jpg)
   En el REPL no necesitas main ni un object porque el REPL actúa como intérprete y se encarga de envolver automáticamente tu código en un contexto válido y adicionalmente no es necesario compilar el código ni proporcionar un punto de entrada explícito.

   Por otra parte, el siguiente ejemplo muestra cómo se implementa la entrada estándar en Scala:

   Vamos a realizar el ejemplo creando un fichero con el código como muestra la siguiente imagen:
2. ![image](assets/cm6jfcckc02xx3570hx2ngpv6-step2-Imagen16.jpg)
3. Es importante destacar primeramente la librería importada para poder emplear los métodos de entrada. Seguidamente hay que señalar los distintos métodos empleados para la entrada en función del dato que se va a recibir. Por último, conviene señalar que en Scala tenemos dos formas de realizar comentarios en el código dependiendo si es un comentario de una línea con los símbolos // o si es un comentario de bloque, en cuyo caso se encierra entre los símbolos /* y */.

   A continuación de muestra la ejecución:
4. ![image](assets/cm6jfcckc02xx3570hx2ngpv6-step4-Imagen17.jpg)
   Adicionalmente hay que resaltar que si se ejecutarse en Scastie el código da problemas por la gestión que realiza el propio entorno de la entrada estándar.

   Finalmente se puede hacer un “HolaMundo” en fichero también pero extendiendo la Clase App en vez de emplear la definición del método main como hemos visto. App es un trait (similar a una interfaz en otros lenguajes orientados a objetos, pero con capacidades adicionales, lo comentamos más adelante) predefinido en Scala: El trait App (en el paquete scala.App) proporciona una implementación predeterminada de un método main. Cuando defines un objeto que extiende App, cualquier código que escribas en el cuerpo del objeto se ejecuta automáticamente como parte del método main.

   En las siguientes imágenes vemos tanto el código escrito en el fichero como su compilación y posterior ejecución.
5. ![image](assets/cm6jfcckc02xx3570hx2ngpv6-step5-Imagen18.jpg)
6. ![image](assets/cm6jfcckc02xx3570hx2ngpv6-step6-Imagen19.jpg)



### 4.5 Clases y objetos acompañantes



En este apartado se introduce el concepto de **classes** y **companion objects** en Scala, que es una característica única del lenguaje que permite combinar una clase y un objeto con el mismo nombre para trabajar juntos de manera integrada. Este patrón es útil para encapsular tanto comportamientos relacionados con instancias específicas de una clase como funcionalidad compartida que no depende de ninguna instancia.

Vamos a verlo con un ejemplo:



![image](assets/cm6jfz2ai03753570sefli8zw-Imagen20.jpg)



En este ejemplo, se define una clase MiClase que tiene un constructor, el cual a su vez recibe un parámetro nombre. Dentro de la clase, hay un método privado llamado saludar, que es accesible únicamente desde dentro de la clase. También se define un método público realizarSaludo, que, a su vez, llama a un método del **companion object** llamado saludoPersonalizado. Esto demuestra cómo una clase puede interactuar directamente con su companion object.

El companion object MiClase se define utilizando la palabra clave object. En él se declara un método estático saludoPersonalizado, que imprime un saludo personalizado utilizando el nombre proporcionado. Además, contiene un valor constante PI, que es accesible sin necesidad de crear una instancia de la clase. Este companion object actúa como un lugar centralizado para almacenar lógica o datos que son comunes y no dependen de ninguna instancia específica de la clase.

En el objeto Ejemplo, que contiene el método main, se demuestra cómo utilizar tanto la clase como el companion object. Primero, se crea una instancia de MiClase con el nombre "Juan", y se llama al método realizarSaludo, que internamente utiliza el método saludoPersonalizado del companion object. También se llama directamente al método del companion object saludoPersonalizado con otro nombre, "María". Finalmente, se accede al valor PI definido en el companion object sin necesidad de crear una instancia de MiClase.

Por tanto, el resultado obtenido es:



```ini
Bienvenido, Juan
Bienvenido, María
El valor de PI es: 3.1416
```



En resumen, los companion objects en Scala permiten definir métodos y valores compartidos que no dependen de instancias específicas de la clase, mientras que las clases se utilizan para definir el comportamiento y los datos específicos de las instancias. Este diseño combina lo mejor de los métodos estáticos (al estilo de Java) con una mayor cohesión entre las clases y su funcionalidad compartida.



### 4.6 Opciones



En este apartado nos referimos al uso de la clase Option en Scala, que es una estructura utilizada para representar valores que pueden o no estar presentes. Es una forma segura de manejar valores nulos o ausentes, evitando errores comunes como el NullPointerException. La clase Option tiene dos posibles valores: Some (que contiene un valor) y None (que representa la ausencia de un valor).

Vamos a analizar el siguiente ejemplo:



```ini
scala> var c : Option[MyClass] = None
c: Option[MyClass] = None
scala> c.isDefined
res17: Boolean = false
scala> c = Some(new MyClass)
c: Option[MyClass] = Some(MyClass())
scala> c.isDefined
res18: Boolean = true
```



En este caso, el ejemplo comienza declarando una variable mutable c de tipo Option[MyClass], que inicialmente se asigna como None. Esto significa que, en este momento, c no contiene ningún valor de tipo MyClass.

Luego, se utiliza el método isDefined para verificar si la opción contiene un valor. Como se esperaba, este método devuelve false porque la variable c se inicializó con None.

Posteriormente, se asigna a c una instancia de MyClass encapsulada en Some. Esto indica que ahora c tiene un valor válido de tipo MyClass. Al llamar nuevamente al método isDefined, el resultado es true, ya que la opción ahora contiene un valor.

En resumen, la clase Option en Scala proporciona una forma segura y clara de trabajar con valores que podrían ser opcionalmente válidos o ausentes. Este enfoque fomenta un diseño más robusto y reduce la posibilidad de errores relacionados con referencias nulas.



### 4.7 Funciones



En Scala, las funciones y métodos son elementos fundamentales que permiten encapsular lógica reutilizable. La sintaxis básica para definir una función incluye el uso de la palabra clave def, seguida del nombre de la función, una lista opcional de parámetros, el tipo de retorno y el cuerpo de la función. Por ejemplo y de forma genérica una función en Scala tiene esta estructura:



```javascript
def functionName ([list of parameters]) : [return type] = {
  function body
  [return expr]
}
```



Un ejemplo práctico es la implementación de un método que elimina los primeros n elementos de una lista, como se muestra a continuación:



```scala
override def drop(n: Int): List[A] = {
  var these = this
  var count = n
  while (!these.isEmpty && count > 0) {
    these = these.tail
    count -= 1
  }
  these
}
```



En este caso, se utiliza un bucle while para recorrer los elementos de la lista y eliminar los primeros n elementos, demostrando cómo Scala maneja estructuras de control y mutabilidad local.

Como hemos visto, Scala proporciona métodos para interactuar con la consola de manera eficiente. Métodos como print, println y printf permiten la salida de texto formateado o sin formato. Para llamarlos no hacemos referencia a la clase Console. Podemos incluso, si lo consideramos aunque no es recomendable, redefinir funciones como indica el ejemplo:



```scala
def print(x: Any) = Console.print(x)
def println() = Console.println()
def println(x: Any) = Console.println(x)
def printf(text: String, xs: Any*) = Console.print(text.format(xs: _*))
```



Finalmente, en Scala, las funciones también pueden ser utilizadas como parámetros, una característica que permite un enfoque funcional para resolver problemas. Por ejemplo, en el método foreach:



```scala
final override def foreach[U](f: A => U): Unit = {
  var these = this
  while (!these.isEmpty) {
    f(these.head)
    these = these.tail
  }
}
```



Aquí, f es una función pasada como argumento, que se aplica a cada elemento de una lista. Este enfoque enfatiza la capacidad de Scala para integrar programación funcional con programación orientada a objetos, proporcionando soluciones elegantes y expresivas.

Vamos a ver un ejemplo aplicado del paso de funciones como parámetros, en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%207%20Funciones%20como%20par%C3%A1metros.mp4?v=1)



### 4.8 Case Classes



Las **case classes** en Scala son una característica poderosa y versátil que se utiliza para definir estructuras de datos inmutables y funcionales. Se diferencian de las clases estándar porque añaden varias funcionalidades por defecto, lo que simplifica su uso en escenarios comunes. A continuación, se explica su importancia y cómo se utilizan.

Las case classes son clases especiales que extienden automáticamente la funcionalidad de los objetos estándar en Scala. Algunas de sus características clave incluyen:



- **Clase estándar**  
  Son clases completas con soporte para métodos, herencia y polimorfismo.
- **Parámetros del constructor como valores**  
  Los parámetros del constructor de una case class son inmutables por defecto, ya que se tratan como valores (val).
- **Soporte para pattern matching**  
  Las case classes permiten la deconstrucción directa de sus valores, lo que facilita la escritura de código más expresivo y funcional.
- **Factorías integradas**  
  No es necesario usar new para crear instancias de una case class. Scala incluye automáticamente un método de factoría para simplificar su creación.
- **Serializable**  
  Las case classes son serializables, lo que las hace ideales para usarlas en aplicaciones distribuidas.
- **Método copy**  
  Permiten crear una copia de una instancia con la opción de modificar algunos de sus valores.
- **Extienden Product**  
  Esto les permite funcionar como "tipos productos", lo que significa que pueden ser tratadas como una colección de valores relacionados.



Un ejemplo clásico que demuestra el uso de case classes en el modelado de expresiones matemáticas es el siguiente:



![image](assets/cm6jgq74k03m03570jk7vn70m-Imagen21.jpg)



En este modelo:

- Var representa una variable con un nombre.
- Number representa un número.
- UnOp representa una operación unaria (por ejemplo, la negación -x).
- BinOp representa una operación binaria (como la suma o multiplicación).

Cada una de estas case classes permite instanciar y trabajar con diferentes tipos de expresiones matemáticas de forma estructurada.

Uno de los principales beneficios de las case classes es su integración con el pattern matching. Esta característica permite inspeccionar y deconstruir objetos en tiempo de ejecución, lo que facilita escribir código conciso y claro para el procesamiento de estructuras complejas.

Se muestra a continuación una función que simplifica ciertas expresiones matemáticas usando pattern matching sobre case classes:



![image](assets/cm6jgrmjd03nd3570eu38t2ti-Imagen22.jpg)



Esta función utiliza el pattern matching para identificar patrones comunes en las expresiones y simplificarlas:

1. **Doble negación**: Si una expresión es UnOp("-", UnOp("-", e)), se elimina la doble negación, devolviendo simplemente e.
2. **Sumar cero**: Si una expresión es BinOp("+", e, Number(0)), se simplifica a e, ya que sumar cero no cambia el valor.
3. **Multiplicar por uno**: Si una expresión es BinOp("*", e, Number(1)), se simplifica a e, ya que multiplicar por uno no altera el valor.
4. **Caso por defecto**: Para cualquier otra expresión, se devuelve tal cual.



Ejemplo de uso: Supongamos que queremos simplificar la expresión x + 0. Esto se modela y evalúa de la siguiente manera:



```scala
val expr = BinOp("+", Var("x"), Number(0))
val simplified = simplifyTop(expr)
println(simplified) // Salida: Var("x")
```



En este ejemplo, simplifyTop detecta el patrón BinOp("+", e, Number(0)) y devuelve directamente Var("x"), que es la simplificación.

En resumen: las **case classes** en Scala son una herramienta poderosa que permite modelar datos de manera sencilla, inmutable y expresiva. Su integración con**pattern matching** las convierte en la base perfecta para trabajar con estructuras complejas, como expresiones matemáticas, árboles o datos jerárquicos.



### 4.9 Traits



Los **traits** en Scala son un mecanismo para compartir y reutilizar código entre clases. Son similares a las interfaces en otros lenguajes, pero con la ventaja de que pueden incluir implementaciones concretas de métodos, además de métodos abstractos. Los traits permiten una forma flexible de composición, ya que una clase puede extender múltiples traits.

Pongamos un ejemplo en el que se define un trait llamado Similarity el cual introduce dos métodos relacionados con la comparación de objetos:



```scala
trait Similarity {
  def isSimilar(x: Any): Boolean           // Método abstracto (debe implementarse)
  def isNotSimilar(x: Any): Boolean = !isSimilar(x) // Método con implementación por defecto
}
```



- **isSimilar** es un método abstracto que las clases que extiendan el trait deben implementar.
- **isNotSimilar** tiene una implementación por defecto que invierte el resultado de isSimilar. Esto demuestra que los traits pueden incluir tanto métodos abstractos como concretos.

A continuación, se muestra cómo una clase llamada Point extiende el trait Similarity:



```scala
class Point(xc: Int, yc: Int) extends Similarity {
  var x: Int = xc
  var y: Int = yc
  def isSimilar(obj: Any): Boolean =
    obj.isInstanceOf[Point] && obj.asInstanceOf[Point].x == x
}
```



En este caso la clase Point representa un punto en un plano cartesiano con coordenadas x e y. El método isSimilar verifica si el objeto dado es un punto (Point) y si tiene la misma coordenada x.

Se puede probar este código por ejemplo de la siguiente manera:



```scala
val p1 = new Point(1, 2)
val p2 = new Point(1, 3)
val p3 = new Point(2, 2)

println(p1.isSimilar(p2)) // true: misma coordenada x
println(p1.isSimilar(p3)) // false: diferente coordenada x
```



Veamos otra aplicación: Traits y composición con herencia múltiple. Los traits también permiten componer funcionalidades al ser mezclados con clases. En el segundo ejemplo, se demuestra cómo combinar traits para extender las capacidades de una clase base.



```scala
object StringIteratorTest {
  def main(args: Array[String]) {
    class Iter extends StringIterator(args(0)) with RichIterator
    val iter = new Iter
    iter foreach println
  }
}
```



En este ejemplo: StringIterator es una clase base (no mostrada en el ejemplo, pero asume que recorre los caracteres de una cadena). RichIterator es un trait que extiende las capacidades de iteración (podría añadir métodos adicionales, como foreach). Finalmente, Iter es una clase que extiende StringIterator y combina su funcionalidad con el trait RichIterator.

Los traits son ideales para evitar problemas de herencia múltiple y fomentar la reutilización de código de forma modular y limpia.

Un ejemplo de uso, el cual se recomienda implementarlo a los alumnos, sería: Crear primeramente una instancia de la clase Iter, que combina las funcionalidades de StringIterator y RichIterator. La instancia iter recorre los caracteres de la cadena proporcionada como argumento (args(0)) y los imprime uno por uno. Si ejecutamos el programa con el argumento "Scala", el resultado sería:



```bat
S
c
a
l
a
```



### 4.10 Generics



El concepto de **genéricos** en Scala permite escribir clases, traits o funciones que pueden trabajar con cualquier tipo de datos, proporcionando flexibilidad y reutilización del código mientras se mantiene la seguridad de tipos. En términos simples, los genéricos permiten definir estructuras de datos o funciones que pueden operar sobre tipos arbitrarios, especificados en el momento de su uso. Esto se logra mediante el uso de **parámetros de tipo**, que se representan con un nombre en mayúscula dentro de corchetes ([T], T es el parámetro de tipo).

Veamos un ejemplo que es una implementación sencilla de una clase genérica Stack, que modela una pila (estructura de datos LIFO, Last In, First Out).



```scala
class Stack[T] {
  var elems: List[T] = Nil // Lista que almacena los elementos de la pila

  // Método para agregar un elemento a la pila
  def push(x: T): Unit = { 
    elems = x :: elems // Agrega el elemento al inicio de la lista
  }

  // Método para obtener el elemento en la parte superior de la pila
  def top: T = elems.head

  // Método para eliminar el elemento en la parte superior de la pila
  def pop(): Unit = { 
    elems = elems.tail // Elimina el primer elemento de la lista
  }
}
```



Características del ejemplo:



- **Definición genérica**  
  La clase está parametrizada por un tipo genérico T. Esto significa que puedes crear una pila para cualquier tipo de datos (números, cadenas, objetos, etc.), especificándolo al crear la instancia de la clase.
- **Atributo elems**  
  Es una lista de tipo T que almacena los elementos de la pila. Se inicializa como una lista vacía (Nil).
- **Método push**  
  Agrega un elemento de tipo T a la pila. Internamente, usa el operador :: para insertar el nuevo elemento al inicio de la lista.
- **Método top**  
  Devuelve el elemento superior de la pila (head de la lista). Este método no elimina el elemento, solo lo consulta.
- **Método pop**  
  Elimina el elemento superior de la pila (tail de la lista).



Podemos utilizar esta clase para crear pilas de diferentes tipos. A continuación, un par de ejemplos prácticos, el primero recibiendo enteros y el segundo strings:



```scala
val intStack = new Stack[Int]    // Pila de enteros
intStack.push(1)                // Agrega el número 1
intStack.push(2)                // Agrega el número 2
println(intStack.top)           // Imprime: 2
intStack.pop()                  // Elimina el 2
println(intStack.top)           // Imprime: 1


val stringStack = new Stack[String] // Pila de cadenas
stringStack.push("Scala")
stringStack.push("Generics")
println(stringStack.top)            // Imprime: Generics
stringStack.pop()
println(stringStack.top)            // Imprime: Scala
```



Ventajas de los genéricos en Scala



- **Reutilización del código**  
  La clase Stack es genérica y puede funcionar con cualquier tipo de dato (Int, String, etc.) sin necesidad de escribir una nueva clase para cada tipo.
- **Seguridad de tipos**  
  El compilador garantiza que solo se usen los tipos correctos, evitando errores en tiempo de ejecución.
- **Flexibilidad**  
  Puedes trabajar con cualquier tipo de dato, incluidos tipos definidos por el usuario.



### 4.11 Programación funcional



La programación funcional (FP) es un paradigma que enfatiza la inmutabilidad, el uso de funciones puras y la transparencia referencial, lo que conduce a programas más predecibles y fáciles de razonar. A continuación, se explican los conceptos clave utilizando los ejemplos presentados.

La **transparencia referencial** es un principio fundamental de la programación funcional. Una función es transparente referencialmente si siempre produce el mismo resultado para los mismos argumentos y no tiene efectos secundarios inesperados. Esto significa que puedes reemplazar la llamada a una función con su resultado sin alterar el comportamiento del programa.

Así por ejemplo si tenemos el código:



```haskell
def f(x: Int): Int = x * 2
```



Esta función es transparente referencialmente porque para cualquier valor de entrada, siempre produce el mismo resultado (x * 2) y porque no tiene efectos secundarios (como modificar variables externas o imprimir en consola).

Por otro lado, si consideremos esta otra función:



```scala
def g(x: Int): Int = {
  println("I am multiplying!")
  x * 2
}
```



En este caso, g no es transparente referencialmente porque imprime un mensaje en la consola cada vez que se ejecuta, lo que constituye un efecto secundario. Esto hace que g no sea intercambiable directamente por su resultado, ya que su ejecución no solo depende de sus entradas.

Así si suponemos qque tenemos un método llamado someMethodExpectingInteger que espera un entero como argumento. Podemos observar las diferencias:



```markdown
someMethodExpectingInteger(f(1)) // Equivalente a someMethodExpectingInteger(2)
someMethodExpectingInteger(g(1)) // No equivalente a someMethodExpectingInteger(2), porque imprime algo en la consola
```



La función f(1) puede reemplazarse directamente por su resultado (2), pero g(1) no, porque incluye efectos secundarios que cambian el estado del programa o su salida.

Pongamos otro ejemplo:



```scala
var lastFactor: Option[Int] = None
def f(x: Int): Int = x * 2
def g(x: Int): Int = {
  lastFactor = Some(x) // Modifica una variable externa
  x * 2
}
```



En este caso f sigue siendo transparente referencialmente, ya que no afecta ni depende de ninguna variable externa. Por el contrario g, no es transparente referencialmente porque modifica la variable lastFactor cada vez que se ejecuta. Esto introduce un cambio en el estado global del programa.

Programar funcionalmente empleando conceptos matemáticos aporta las siguientes ventajas:



- **No hay cambios inesperados**  
  Las funciones puras y la inmutabilidad garantizan que los valores no cambien una vez definidos. Esto elimina los errores relacionados con cambios de estado inesperados.
- **Los bugs están confinados**  
  Al trabajar con funciones puras, los errores son más fáciles de rastrear, ya que solo pueden estar en la lógica de la función. No hay interacción con estados externos o efectos secundarios.
- **Concurrencia más sencilla**  
  En un entorno funcional, no es necesario preocuparse por condiciones de carrera o problemas de concurrencia, ya que nada puede cambiar en memoria. Esto simplifica enormemente el diseño de sistemas concurrentes.
- **Sin problemas de paso por valor o referencia**  
  En la programación funcional, no importa cómo se pasa un dato a una función, ya que los valores son inmutables. Esto elimina toda ambigüedad o confusión sobre si un cambio en una función afecta al valor original.
- **Los programas parecen fórmulas matemáticas**  
  El código funcional es limpio, predecible y se asemeja a fórmulas matemáticas. Esto facilita la verificación de la corrección del programa, ya que el razonamiento es más directo.



### 4.12 Colecciones con función superior



Las colecciones con funciones de orden superior en Scala permiten trabajar de manera funcional y declarativa sobre listas y otras estructuras de datos. Estas funciones procesan elementos de una colección usando funciones como parámetros, lo que simplifica tareas comunes como transformación, filtrado, y reducción de datos. A continuación, se explican las principales funciones con ejemplos



#### MAP



La función map se utiliza para transformar cada elemento de una colección aplicando una función. Ejemplo:



```ocaml
val myList = List(1, 2, 3, 4, 5, 6)
myList.map(value => value * 2)
```



Resultado: es una lista con los valores: (2, 4, 6, 8, 10, 12)

Es decir, cada elemento de myList se multiplica por 2 y el resultado es una nueva lista.

De forma genérica podemos decir que recibe una función f que transforma elementos de tipo A en tipo B:  map[B](f: A => B): List[B]



#### FILTER



La función filter selecciona elementos de una colección que cumplen con una condición.

Ejemplo:



```bat
val myList = List(1, 2, 3, 4, 5, 6)
myList.filter(_ > 3)
```



Resultado: es una lista con los valores: (4, 5, 6). Por tanto solo se incluyen los elementos mayores que 3.

De forma genérica podemos decir que recibe una sentencia p que evalúa si un elemento debe incluirse o no: filter(p: A => Boolean): List[A]



#### REDUCE



La función reduce combina los elementos de una colección mediante una operación binaria. Se trata por tanto de una agregación de elementos. Ejemplo:



```ocaml
val myList = List(1, 2, 3, 4, 5, 6)
myList.reduce((a, b) => a + b)
```



Resultado: 21. En este caso suma todos los elementos de la lista.

De forma genérica podemos decir que combina elementos usando la operación op:



```ini
reduce[A1 >: A](op: (A1, A1) => A1): A1
```



#### FOLD



La función fold es similar a reduce, pero comienza con un valor inicial que se usa en las operaciones, por lo que se la conoce también como agregación con valor inicial. Ejemplo alicado sobre la lista anterior:



```bat
myList.fold(0)((acc, cur) => acc + cur)
```



Resultado: 21. La suma comienza desde el valor inicial 0.

De forma genérica podemos decir que usa un acumulador inicial z y combina elementos con la operación op:



```ini
fold[A1 >: A](z: A1)(op: (A1, A1) => A1): A1
```



Se recomienda al alumno realizar la prueba de ver qué efector tendría si e pone valor inicial 1.



#### FOLD LEFT



La función foldLeft procesa elementos de izquierda a derecha y es útil cuando el acumulador tiene un tipo diferente al de los elementos de la colección. Se denomina también agregación específica desde la izquierda. Ejemplo:



```scala
myList.foldLeft(Map.empty[Int, Int])((acc, cur) => acc + (cur -> cur * 2))
```



El elemento inicial es un map vacío, representado por Map.empty[Int, Int]. Este es el valor con el que comienza el acumulador (acc) en el primer paso de la iteración.

Resultado:  5 -> 10, 1 -> 2, 6 -> 12, 2 -> 4, 3 -> 6, 4 -> 8 Crea un mapa donde cada elemento de myList es una clave y su valor es el doble.

De forma genérica: Procesa elementos de izquierda a derecha, empezando con el valor inicial z: foldLeft[B](z: B)(f: (B, A) => B): B



### 4.13 For Comprenhension



El for comprehension en Scala es una forma expresiva y poderosa de trabajar con colecciones y datos que permite realizar iteraciones, filtrados, transformaciones y otras operaciones de manera más declarativa que en lenguajes como Java. Aunque se parece a los bucles for tradicionales, en Scala es más funcional y se basa en métodos como map, flatMap y filter.

En Scala, una expresión for puede ser utilizada para:

- Iterar sobre colecciones.
- Filtrar elementos.
- Transformar resultados con yield.

Ejemplo:

Veamos diferencias semánticas con Java. El código:



```r
for (x <- c1; y <- c2; z <- c3) {
  // Cuerpo del for
}
```



Equivale a usar múltiples llamadas anidadas a métodos de orden superior como foreach:



```bat
c1.foreach(x => c2.foreach(y => c3.foreach(z => {
  // Cuerpo del for
})))
```



Otro caso, si agregamos yield al for, Scala genera un nuevo resultado basado en las transformaciones realizadas:



```r
for (x <- c1; y <- c2; z <- c3) yield {
  // Generar un valor
}
```



Se traduce por tanto en:



```scala
c1.flatMap(x => c2.flatMap(y => c3.map(z => {
  // Generar un valor
})))
```



En resumen, en Scala, los for comprehensions son una forma más declarativa y funcional de iterar, filtrar y transformar datos. A diferencia de los bucles for en lenguajes como Java, un for en Scala no es solo una estructura de control, sino una expresión que se traduce internamente a métodos como map, flatMap y filter. Esto significa que puedes realizar operaciones complejas sobre colecciones de manera más legible y funcional.

Por ejemplo, el código for (x <- c1; y <- c2; z <- c3) { ... } equivale a anidar múltiples llamadas a foreach, recorriendo las colecciones c1, c2 y c3 en cascada. Si se utiliza yield, como en for (x <- c1; y <- c2; z <- c3) yield {...}, el for genera una nueva colección transformada, lo que es equivalente a combinar flatMap y map. Este enfoque hace que los for comprehensions sean una herramienta poderosa para trabajar con datos de forma declarativa y expresiva, facilitando la creación de pipelines funcionales.

Veamos un uso práctico del for-yield. El uso del yield permite que el for genere una nueva colección como resultado, en lugar de solo iterar.

Ejemplo que genera números pares:



```scala
object ComprehensionTest1 extends Application {
  def even(from: Int, to: Int): List[Int] =
    for (i <- List.range(from, to) if i % 2 == 0) yield i
  Console.println(even(0, 20))
}
```



List.range(from, to) genera una lista de números en el rango [from, to). El if i % 2 == 0 filtra los números para incluir solo los pares. El yield genera una nueva lista con los valores seleccionados. Por tanto el resultado sería la lista (0, 2, 4, 6, 8, 10, 12, 14, 16, 18).

Otro ejemplo sería el siguiente que transforma los elementos de una lista.:



```scala
val numeros: List[Int] = List(1, 2, 3, 4, 5)
val duplicados: List[Int] = for {
  numero <- numeros
  duplicado = numero * 2
} yield duplicado
```



La lista numeros contiene números del 1 al 5. Para cada numero, se calcula su duplicado (numero * 2) y se almacena en duplicado. El yield genera una nueva lista con los duplicados. el resultado sería la lista ( 2, 4, 6, 8, 10)

Resumen: El for comprehension en Scala es más que un simple bucle: es una herramienta funcional para trabajar con colecciones de forma declarativa y expresiva. Con el uso de yield, permite filtrar y transformar datos fácilmente, generando nuevas colecciones como resultados.



### 4.14 Try-catch



El manejo de errores en Scala se basa en el uso de estructuras como try-catch-finally para capturar excepciones de manera similar a otros lenguajes como Java, y en estructuras funcionales como Try para manejar errores de manera más declarativa y segura.

La estructura try-catch-finally permite capturar y manejar excepciones de forma tradicional. En el bloque try se escribe el código que podría lanzar una excepción, mientras que en los bloques catch se definen casos específicos para manejar diferentes tipos de errores. Por último, el bloque finally es opcional y se ejecuta siempre, independientemente de si hubo una excepción o no, generalmente para liberar recursos.

Ejemplo:



```kotlin
try {
  // Código que puede lanzar excepciones
} catch {
  case ioe: IOException => println("Ocurrió un error de E/S")
  case e: Exception => println("Ocurrió una excepción genérica")
} finally {
  println("Liberando recursos...")
}
```



Digamos que esta es la estructura clásica de control de excepciones que conocemos hasta ahora.

Veamos a continuación el manejo funcional de errores con Try. El tipo Try en Scala permite manejar errores de manera funcional, encapsulando el resultado de una operación que podría fallar. Existen dos posibles resultados:

- Success: Representa un resultado exitoso.
- Failure: Representa un error, incluyendo información sobre la excepción lanzada.

Ejemplo:



![image](assets/cm6jifl8g04zs3570v3s82xi0-Imagen24.jpg)



Expliquemos el código:

1. Captura de entrada con Try: dividend y divisor son intentos (Try) de leer y convertir a enteros las entradas del usuario.
2. Cálculo seguro: problem combina ambas entradas usando flatMap y map para realizar la división. Si algo falla, problem será un Failure.
3. Manejo del resultado:

- Si problem es un Success, se imprime el resultado de la división.
- Si es un Failure, se informa del error al usuario y se solicita que intente nuevamente mediante una llamada recursiva a divide.

Ventajas del uso de Try con enfoque funcional:

- Evita lanzar excepciones, encapsulando errores en un flujo funcional.
- Permite manejar errores de forma declarativa usando patrones (Success y Failure).

Resumen: El enfoque clásico con try-catch-finally es útil para manejar excepciones de manera inmediata, mientras que el uso de Try ofrece un manejo funcional y expresivo de errores, más alineado con el paradigma funcional de Scala. Usar Try es particularmente útil cuando se quiere evitar interrupciones en el flujo del programa y manejar errores de forma controlada.



### 4.15 Otros elementos



Comenzamos este último apartado con el concepto de implicits en Scala permite introducir valores o comportamientos en un contexto sin tener que pasarlos explícitamente, lo que hace que el código sea más limpio y expresivo. Los parámetros implícitos se utilizan para proporcionar dependencias de manera automática, mejorando la reutilización y la modularidad del código.

Lo mejor para entenderlo es mostrar el siguiente ejemplo y explicarlo:



![image](assets/cm6jiiolb051y3570trwuj5zy-Imagen25.jpg)



El código presentado define una funcionalidad para saludar a una persona en diferentes idiomas utilizando parámetros implícitos. A continuación, explicamos paso a paso cómo funciona:

- Primero, se define una clase Persona para representar a las personas con un atributo nombre.
- Luego, se crea una clase SaludosEnDiferentesIdiomas, que contiene métodos para saludar en inglés y en español. Esta clase encapsula, por tanto, la lógica de cómo se generan los saludos en diferentes idiomas.
- Se crea un objeto SaludosImplicits que contiene una instancia de SaludosEnDiferentesIdiomas marcada como implícita. Esto permite que dicha instancia esté disponible en un contexto donde se requiera un parámetro de tipo SaludosEnDiferentesIdiomas
- La función saludar utiliza un **parámetro implícito** de tipo SaludosEnDiferentesIdiomas. El parámetro saludos no se pasa explícitamente cuando se llama a la función. Scala buscará automáticamente un valor implícito de tipo SaludosEnDiferentesIdiomas en el contexto disponible.
- Finalmente para utilizar la función saludar, primero se importa el valor implícito definido en SaludosImplicits. Después, se puede crear una instancia de Persona y llamar a la función saludar sin pasar manualmente el parámetro implícito. La razón por la que el saludo a "John" se realiza en inglés en el ejemplo es porque la función saludar está programada para llamar específicamente al método saludarEnIngles de la clase SaludosEnDiferentesIdiomas. Es decir, el idioma del saludo no se elige dinámicamente en función del nombre de la persona, sino que está definido explícitamente en el cuerpo de la función.

Ventajas de los implicits:



- **Eliminan la necesidad de pasar parámetros manualmente**  
  El parámetro implícito saludos se resuelve automáticamente, reduciendo el código repetitivo.
- **Facilitan la extensibilidad**  
  Puedes cambiar el comportamiento global de las funciones implícitas simplemente cambiando el valor implícito en el contexto.
- **Modularidad**  
  El uso de implicits permite separar la lógica de las dependencias.



Además del ejemplo de implicits, otros conceptos importantes son:



- **Modos de herencia en Scala**  
  - **Simple:** Una clase hereda de otra.
  - **Múltiple:** Scala lo implementa con mixins utilizando traits.
  - **Abstracta:** Las clases abstractas definen métodos que deben ser implementados en subclases.
- **SBT vs Maven**  
  SBT (Scala Build Tool) es la herramienta más común para gestionar proyectos en Scala, mientras que Maven es más utilizado en proyectos Java. SBT ofrece una integración más fluida con Scala.
- **Rendimiento de colecciones**  
  Las colecciones en Scala están optimizadas para diferentes casos de uso, proporcionando un equilibrio entre rendimiento y funcionalidad. En el siguiente enlace se pueden comprobar los rendimientos de las diferentes colecciones:

  LINK: [https://docs.scala-lang.org/overviews/collections/performance-characteristics.html](https://docs.scala-lang.org/overviews/collections/performance-characteristics.html)



## 5. Ejemplos



### 5.1 Introducción



![image](assets/cm6jisvsu05623570k3pmis82-stock-image.jpg)



A continuación, se presentan algunos ejemplos de código en Scala con características particulares. Estos no representan, ni mucho menos, el único tipo de código que se puede explorar o preguntar. Como bien sabéis, la programación se domina practicando, así que tomad estos ejemplos como una base para consolidar vuestro conocimiento en Scala. Se os anima a profundizar y buscar más ejercicios para realizar y practicar, fortaleciendo así vuestra habilidad en este lenguaje. De la misma forma se recomienda a los alumnos no solo ver los videos de los ejercicios sino una vez comprendido intentarlos por su cuenta nuevamente.



### 5.2 Ejemplo básico de escala



Este código introduce conceptos básicos como definir funciones (sum) y funciones parciales (divide y divide2). Es un buen punto de partida para aprender cómo estructurar un programa Scala y cómo manejar funciones con casos específicos. Implemente las funciones y realice validaciones.



- **Función de suma**  
  Implementa una función llamada sum que reciba dos enteros como parámetros y retorne su suma.
- **Funciones parciales para división**  
  - Define una función parcial llamada divide que divida el número 24 por un divisor recibido como entrada, siempre que este sea distinto de 0. Si el divisor es 0, la función no debe estar definida.
  - Define otra función parcial llamada divide2 que tome como parámetro un dividendo (x) y retorne una función parcial que permita dividir x por un divisor siempre que este sea distinto de 0.



**Hay que gestionar los posibles errores que puedan surgir de la mejor forma conocida.**

El objetivo es entender el uso de funciones, funciones parciales y cómo se manejan los casos no definidos en Scala.

En el siguiente video se puede ver la solución:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%208%20ejemplo%20b%C3%A1sico.mp4?v=1)



### 5.3 Operaciones con collecciones



Esta vez vamos a ejecutar el código en un entorno interactivo como es la consola REPL de Scala. El objetivo de este código es cubrir operaciones fundamentales en listas de Scala, una habilidad esencial para trabajar con colecciones funcionales.

Se pide realizar las siguientes operaciones con listas en Scala:



- **Append**  
  - Agregar un elemento al final de una lista.
  - Agregar un elemento al final de una lista solo si no existe en ella.
- **Prepend**  
  - Agregar un elemento al inicio de una lista.
- **Filter y Map**  
  - Filtrar los números impares de una lista y duplicar su valor.
  - Modificar todos los elementos de una lista, duplicando los impares y dejando los pares sin cambios.
- **FlatMap**  
  - Generar una transformación para cada elemento de una lista y aplanar los resultados.
- **FlatMap con Option**  
  - Manejar cálculos que pueden devolver valores nulos (opcionalidad) y aplanar los resultados en una lista.
- **Pattern Matching con listas**  
  - Sumar todos los elementos de una lista utilizando recursión.
  - Eliminar los primeros n elementos de una lista utilizando patrones.



En el siguiente video se puede ver la solución:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%209%20colecciones.mp4?v=1)



### 5.4 Manejo de errores



Manejo de errores usando Try, Option y Either. Se pide realizar porc onsola los siguientes casos:

- Manejo de excepciones:División con try-catch para capturar errores y manejar divisiones por 0 con un valor alternativo.
- Uso de Try: Implementar manejo de resultados con Try y distinguir entre éxito (Success) y error (Failure) usando Pattern Matching.
- Encapsulación de errores con Option: Usar Option para manejar resultados opcionales, devolviendo Some(resultado) en caso de éxito o None en caso de error.
- Manejo explícito con Either: Representar resultados como éxito (Right) o error (Left) con mensajes descriptivos y flujo de control claro.
- Cálculos con tasas usando Option: Combinar múltiples valores opcionales (Option) para aplicar tasas, proporcionando valores predeterminados en caso de ausencia.

Una posible slución a este enunciado sería el código que se muestra a continuación:



```scala
// Side effects

import scala.util.{Failure, Success, Try}

def divisionWithException(x: Int, y: Int): Int = {
  try {
    x/y
  } catch {
    case e: Exception => 
      println("division entre 0")
      x
  }
}

divisionWithException(9, 0)

def divisionwithTryPM(x: Int, y: Int): Int = {
    Try(x/y) match {
      case Success(resultado) => 
        resultado
      case Failure(error) => 
        println(error)
        x
  }
}

divisionwithTryPM(9, 0)

def divisionwithTry(x: Int, y: Int): Try[Int] = {
  Try(x/y)
}

divisionwithTry(9, 0)

def divisionwithOption(x: Int, y: Int): Option[Int] = {
  Try(x/y) match {
    case Success(resultado) => 
      Some(resultado)
    case _ => 
      None
  }
}

divisionwithOption(9, 0).getOrElse(Int.MaxValue)

def divisionwithEither (x: Int, y: Int) : Either[String, Int] = {
  Try(x/y) match {
    case Success(resultado) => 
      Right(resultado)
    case Failure(throwable) => 
      Left(throwable.getMessage)
  }
}

divisionwithEither(9, 1) match {
  case Left(exception) =>
    println(s"Error: $exception")
  case Right(value) =>
    println(s"Success: $value") 
}

divisionwithEither(9, 0) match {
  case Left(exception) =>
    println(s"Error: $exception")
  case Right(value) =>
    println(s"Success: $value") 
}

// Option

def applyRate(cant: Option[Double], tipo: Option[Double] = Some(1.5)): Option[Double] = {
  (cant, tipo) match {
    case (Some(c), Some(t)) => Option(c*t)
    case (c: Option[Double], Some(t)) => Option(c.getOrElse(100.0)*t)
    case _ => None
  }
}

applyRate(Option(200.0), Option(2.0))
applyRate(Option(200.0))
applyRate(None)
applyRate(None, None)
```



Este código explora diferentes formas de manejar errores y valores opcionales en Scala, utilizando conceptos como excepciones, Try, Option y Either. Cada bloque introduce una estrategia diferente para lidiar con situaciones como divisiones entre cero o valores faltantes.



1. El primer bloque define una función llamada divisionWithException, que usa un bloque try-catch para manejar errores. Si se intenta dividir un número entre cero, la excepción es capturada, se imprime un mensaje y se devuelve el valor del dividendo (x) como resultado. Esto es un enfoque tradicional, pero puede introducir efectos secundarios porque el mensaje se imprime directamente en consola.
2. El segundo bloque introduce divisionwithTryPM, una variación que utiliza el tipo funcional Try para envolver la operación. Dependiendo del resultado, se evalúa si fue un Success o un Failure mediante coincidencia de patrones (match). Si la división es exitosa, se devuelve el resultado; si falla, se imprime el error y se devuelve el valor de x. Este enfoque es más funcional, aunque todavía imprime errores como efecto secundario.
3. El tercer bloque, divisionwithTry, devuelve directamente un objeto Try[Int], lo que permite a quien llama a la función decidir cómo manejar el éxito o el fallo de la operación. Este diseño elimina los efectos secundarios como imprimir en consola y deja el control al consumidor de la función.
4. En el cuarto bloque, divisionwithOption convierte el resultado en un Option[Int]. Si la operación tiene éxito, se devuelve un Some(resultado); de lo contrario, devuelve None. Esto permite manejar errores de manera más declarativa, y el método getOrElse proporciona un valor por defecto cuando no hay un resultado válido.
5. El quinto bloque introduce divisionwithEither, que devuelve un objeto Either con un Left para representar un error (incluyendo el mensaje de error) y un Right para representar el resultado exitoso. Esto es útil para proporcionar información adicional sobre el error y es más expresivo que Option, ya que diferencia claramente entre un resultado válido y un error.
6. Finalmente, el bloque applyRate muestra cómo combinar valores opcionales con Option. Dependiendo de si los valores están presentes (Some) o no (None), realiza cálculos predeterminados o retorna None. Este diseño es útil para trabajar con valores opcionales de forma segura y evitar errores como NullPointerException.



Se han visto, por tanto, en este ejemplo varias formas funcionales y seguras de manejar errores y valores opcionales en Scala, sin necesidad de uso de  excepciones tradicionales.



### 5.5 Tipos genéricos



El objetivo de este ejercicio es enseñar cómo crear clases genéricas, una característica avanzada que permite trabajar con múltiples tipos en un diseño reutilizable.

El código representa una caja genérica (Box) que puede contener cualquier tipo de objeto. La caja permite consultar el contenido con getContent y transformarlo mediante map, creando una nueva caja con el resultado de la transformación.

Crearemos la caja genérica como una clase y posteriormente realizaremos las siguientes pruebas:

- Una caja con el número 10 devuelve 10 al consultar su contenido.
- Una transformación convierte este número en una cadena de "a" repetida 10 veces, dando "aaaaaaaaaa".
- Otra caja con "Scala" devuelve 5 al transformarla en la longitud de su contenido.

Esto muestra cómo manejar tipos genéricos y aplicar funciones de transformación en Scala de forma funcional.

Solución:



```scala
class Box[T](content: T) {
  def getContent: T = content
  
  def map[U](f: T => U): Box[U] = {
    val mappedContent = f(content)
    new Box(mappedContent)
  }
}

val intBox = new Box(10)
println(intBox.getContent) // Imprime: 10

val stringBox = new Box("Scala")
println(stringBox.getContent)

val newStrBox = intBox.map((x: Int) => "a"*x)
println(newStrBox.getContent)

val newIntBox = stringBox.map((s: String) => s.length)
println(newIntBox.getContent)
```



En resumen: El código define una clase genérica Box[T] que encapsula un valor de tipo T. Esta clase permite acceder al contenido mediante el método getContent y transformarlo utilizando el método map, el cual aplica una función f al contenido y devuelve una nueva instancia de Box con el resultado transformado. Por ejemplo, al crear una instancia de Box con el número 10, el método getContent devuelve 10. Luego, aplicando una transformación con map, como repetir la letra "a" diez veces, se obtiene una nueva caja que contiene "aaaaaaaaaa". De manera similar, una instancia de Box con la cadena "Scala" puede ser transformada en su longitud (5) mediante map.



### 5.6 Extractores y Patrones



El objetivo de este ejercicio es practicar el uso de extractores con apply y unapply, clases abstractas y traits.

Los extractores son una característica de Scala que permite descomponer objetos en patrones.

Partamos de este código ejemplo:



```scala
// Extractor

class Alumno(nombre: String, edad: Int)

val alumno1 = Alumno("Juan", 21)

val alumno1 = new Alumno("Juan", 21)

alumno1 match {
  case Alumno(nombre, edad) => println(s"Alumno: $nombre, $edad")
  case _ => println("No es un alumno")
}

object Alumno {
  def apply(nombre: String, edad: Int): Alumno ={
    println("Creando alumno...")
    new Alumno(nombre, edad)
  }
  def unapply(alumno: Alumno): Option[(String, Int)] = Option((alumno.nombre, alumno.edad))
}
```



Este fragmento de código implementa un extractor para la clase Alumno. Los extractores son útiles para usar objetos en estructuras de coincidencia de patrones (match) de manera más legible.

Al comienzo se crea la clase Alumno. Seguidamente  el código muestra dos formas de crear un objeto**en Scala** a partir de la clase Alumno. Sin embargo, hay diferencias importantes entre ambas formas, ya que implican mecanismos distintos:

- Forma 1: **Alumno("Juan", 21)**
  - Aquí se utiliza el **método apply** definido en el **objeto companion** Alumno para crear una instancia de la clase.
  - El objeto Alumno actúa como un "constructor adicional" que encapsula la creación del objeto.
  - Internamente, el apply es responsable de llamar al constructor new Alumno(...).
  - Este enfoque es más idiomático en Scala, ya que reduce la verbosidad y permite una sintaxis más limpia al trabajar con objetos.
  - **Requisitos:** Para que esta forma funcione, debe existir un **companion object** Alumno con un método apply, como este:



```scala
object Alumno {
  def apply(nombre: String, edad: Int): Alumno ={
    println("Creando alumno...")
    new Alumno(nombre, edad)
  }
  def unapply(alumno: Alumno): Option[(String, Int)] = Option((alumno.nombre, alumno.edad))
}
```



- Forma 2: **new Alumno("Juan", 21)**
  - Aquí se utiliza directamente el **constructor de la clase Alumno**.
  - Es más explícito y no depende del objeto companion ni del método apply.
  - Este es el enfoque tradicional en lenguajes como Java, donde siempre se utiliza new para crear objetos.
  - No requiere un companion object, ya que la clase misma proporciona el constructor por defecto.

El método apply permite crear una instancia de la clase Alumno de manera más sencilla, simulando un constructor como en Alumno("Juan", 21).

El método unapply permite descomponer una instancia de Alumno para acceder a sus propiedades (nombre y edad) en un match-case.

Una vez tenemos esa parte clara, podemos añadir las siguientes líneas a nuestro código:



```scala
:paste
class Alumno(val nombre: String, val edad: Int)

lazy val alumno2 = Alumno("Ana", 22)

alumno2 match {
  case Alumno(nombre, edad) => println(s"Alumno: $nombre, $edad")
  case _ => println("No es un alumno")
}

case class Profesor(nombre: String, edad: Int)
val profe1 = Profesor("Miguel", 41)
profe1 match {
  case Profesor(nombre, edad) => println(s"Profesor: $nombre, $edad")
  case _ => println("No es ni alumno ni profesor")
}
```



El :paste asegura que estas definiciones no den error al pegarlas en el REPL, ya que se evalúan como un bloque completo.

Este código tiene dos partes principales:



1. **1.       Uso de la coincidencia de patrones (match) con una clase Alumno y un objeto companion.**

   Clase Alumno define dos propiedades: nombre y edad. Estas se marcan como val, lo que las hace inmutables y accesibles desde fuera de la clase. Aunque no se muestra explícito en este código, para que el patrón Alumno(nombre, edad) funcione, debe haber un companion object asociado a la clase Alumno que implemente el método unapply, tal y como se vio en la primera sección de código. Lazy val significa que la instancia de Alumno no se creará hasta que se utilice por primera vez. Esto puede ser útil para ahorrar recursos si la instancia no siempre es necesaria. Finalmente se hace la coincidencia de patrones con match. El patrón case Alumno(nombre, edad) descompone el objeto alumno2 en sus atributos (nombre y edad) usando el método unapply del companion object. Si el patrón coincide, imprime Alumno: Ana, 22. Si no coincide, imprime No es un alumno.
2. **2.****Uso de la coincidencia de patrones con un case class llamado Profesor.** Es una versión más sencilla y funcional de la clase Alumno, ya que las case classes en Scala generan automáticamente:

   - Un constructor (apply) que permite crear instancias sin necesidad de usar new.
   - Un método unapply, lo que facilita la descomposición en patrones como case Profesor(nombre, edad).
   - Métodos como toString, equals y hashCode, sin necesidad de definirlos manualmente.

   Seguidamente crea un objeto Profesor con los valores "Miguel" y 41. Y para terminar nuevamente crea coincidencia de patrones con match.El patrón case Profesor(nombre, edad) descompone el objeto profe1 en sus atributos nombre y edad. Si el patrón coincide, imprime Profesor: Miguel, 41. Si no coincide, imprime No es ni alumno ni profesor.



A continuación, vamos a emplear otro ejemplo, aunque estemos en el mismo ejercicio, para explicar las clases abstractas partiendo del siguiente ejemplo:



```scala
abstract class SerOrganico

abstract class EntidadDeLaTierra

abstract class Animal(especie: String) extends SerOrganico {
  val esVertebrado: Boolean
  val nombre: String = especie
  def sonido(): String
  def peso(): Int = 0
}

abstract class Mascota {
  val domesticado: Boolean = true
}

class Dog(especie: String, raza: String) extends Animal(especie) with Mascota {
  val esVertebrado = true
  def sonido(): String = "Woof"
  override def peso() = 5
}

trait Mascota {
  val domesticado: Boolean = true
}
```



Este código define una jerarquía de clases y traits que modelan entidades orgánicas, animales y mascotas, destacando el uso de abstracción y herencia en Scala. La clase abstracta SerOrganico actúa como la base para todos los seres vivos, mientras que EntidadDeLaTierra representa una categoría más amplia para cualquier entidad de la Tierra, aunque estas clases no tienen propiedades ni métodos definidos directamente.

1. La clase abstracta Animal introduce atributos y comportamientos comunes a todos los animales, como la propiedad esVertebrado (que indica si el animal tiene columna vertebral) y el método abstracto sonido, que obliga a las clases concretas a definirqué sonido emite el animal. Además, incluye un método peso con un valor por defecto de 0, que puede ser sobrescrito por las subclases si necesitan especificar un peso.
2. La clase Mascota, también abstracta, define un comportamiento específico para animales domésticos mediante la propiedad domesticado, que indica que, por defecto, todos los animales que heredan de esta clase son domesticados.
3. Finalmente, la clase concreta Dog extiende la clase abstracta Animal y el trait Mascota, implementando las propiedades y métodos requeridos. Define que un perro es vertebrado (esVertebrado = true), tiene un sonido característico ("Woof"), y sobrescribe el método peso para indicar que el peso de un perro es 5. En este diseño, el trait Mascota se utiliza como una interfaz que encapsula el comportamiento de domesticación, permitiendo su uso en distintas clases.
4. En resumen, este código ilustra cómo combinar clases abstractas y traits para modelar comportamientos comunes y específicos en un diseño flexible y extensible.



En este punto pueden surgir las preguntas:

- ¿Por qué Animals es abstrcta y no un trait? Animal representa una base jerárquica para todos los animales. Es un concepto que encaja perfectamente en una relación lógica "es un/a" (Dog es un Animal). Además, Animal necesita un constructor con parámetros (especie: String), que no es posible con traits. Por ejemplo, todos los animales deben tener una especie, y esta información se pasa al construir un Dog. Si Animal se definiera como un trait, no podrías pasar la especie directamente al crearlo, lo cual rompe esta lógica.
- ¿Por qué Mascota es un trait? Mascota no representa una jerarquía, sino un comportamiento adicional que puede aplicarse a múltiples clases. El concepto de "ser una mascota" no está limitado a los animales (podría aplicarse a un robot, por ejemplo), y no necesita valores iniciales al momento de la creación, ya que tiene un valor por defecto (domesticado = true). Definir Mascota como una clase abstracta implicaría que todas las mascotas tienen que heredar de ella, lo que podría ser limitante. Al ser un trait, cualquier clase (como Dog, o incluso algo completamente diferente) puede agregar este comportamiento.
- ¿Podrían intercambiarse? Si Mascota fuera una clase abstracta sería más restrictiva, porque las clases como Dog no podrían heredar de otra clase abstracta (Scala no permite herencia múltiple para clases). No tendría sentido lógico obligar a todas las mascotas a heredar de una clase base si simplemente queremos añadir un comportamiento. Por otro lado, si Animal fuera un trait no podrías pasar especie como un parámetro del constructor al crearlo, lo cual es un requisito en este diseño. Perderías claridad en la jerarquía, ya que Dog no "es un" Animal, sino que solo incluiría los comportamientos de Animal.

**Resumen práctico:**

- Se usa clase abstracta (Animal) cuando quieres definir una jerarquía base con constructores o valores iniciales necesarios al momento de instanciar.
- Se usa trait (Mascota) cuando quieres añadir un comportamiento o capacidad adicional que no tiene una relación jerárquica fuerte con las clases que lo implementan.

En este caso, el diseño actual es correcto porque Animal establece una jerarquía base con un constructor, mientras que Mascota se mezcla como un comportamiento adicional

Para finalizar con este ejercicio vamos a analizar el siguiente código cuyo objetivo es conseguir que os familiaricéis con los traits.



```scala
// Traits

trait EntretenimientoConPelota

trait Deporte

trait DeporteDePelota extends EntretenimientoConPelota with Deporte {
  val colorPelota: String = "Blanco"
  def tamanyoPelota(): Int
}

trait DeporteDeEquipo extends Deporte {
  val superficie: String
  def integrantes(): Int = 5
}

class Futbol(profesional: Boolean) extends DeporteDePelota with DeporteDeEquipo {
  def esProfesional(): Boolean = profesional
  def tamanyoPelota(): Int = 70
  override def integrantes(): Int = 11
  val superficie: String = "cesped"
}
```



Este código modela una jerarquía de comportamientos y características relacionadas con deportes utilizando traits en Scala. Los traits representan diferentes aspectos que pueden combinarse para describir deportes específicos.

El trait EntretenimientoConPelota define la idea general de actividades que involucran una pelota. Deporte es un trait más amplio que encapsula lo que caracteriza a un deporte. Sobre estos, DeporteDePelota hereda ambos conceptos y agrega detalles específicos, como el color de la pelota y un método para determinar su tamaño. Por otro lado, DeporteDeEquipo extiende solo Deporte y define propiedades como la superficie donde se juega y el número de integrantes por equipo.

La clase Futbol combina los traits DeporteDePelota y DeporteDeEquipo para definir el deporte del fútbol. Esta clase implementa las propiedades requeridas, especificando que el tamaño de la pelota es 70, que el fútbol se juega en césped, y que un equipo tiene 11 jugadores. Además, introduce un método esProfesional que indica si se trata de un fútbol profesional o no. Este diseño aprovecha los traits para reutilizar comportamientos y combinar características de manera modular y flexible.



### 5.7 Ficheros



Se trata de implementar un programa en Scala que lea un archivo de texto (usaremos por ejemplo un fichero ya disponible en la MV /home/bigdata/microcuento.txt) , realizar diversas operaciones de análisis sobre su contenido y generar un nuevo archivo con las líneas del texto en mayúsculas. Las operaciones solicitadas son:



- **Cálculo de líneas y validación del contenido**  
  - Contar el número total de líneas del archivo.
  - Verificar si todas las líneas tienen más de un cierto número de caracteres.
- **Filtrado y procesamiento**  
  - Seleccionar las líneas que empiezan con una letra específica (por ejemplo, 'U') y calcular su longitud.
  - Tomar las líneas con suficiente variedad de caracteres (líneas cuya cantidad de caracteres distintos sea mayor a 20).
- **Formateo y generación de cadenas**  
  - Convertir todo el archivo en una sola cadena con las líneas separadas por saltos de línea.
  - Obtener la primera línea del archivo, proporcionando un mensaje por defecto si no existe.
  - Combinar las líneas con un rango numérico para crear una representación numerada del contenido.
- **Escritura en un nuevo archivo**  
  - Crear un nuevo archivo donde cada línea del texto original se transforme a mayúsculas.



El programa incluye la lectura y escritura de archivos utilizando las bibliotecas estándar de Scala, asegurando un flujo eficiente y seguro para la manipulación de datos.

A continuación se incluye el código solución, aunque al final también hay disponible un video con la ejecución el cual s recomienda visualizar con detalle.



```scala
// Lectura de ficheros

import scala.io.Source

val filenameIntput = "/home/bigdata/microcuento.txt"

val lines = Source.fromFile(filenameIntput).getLines()
lines.size
lines.size

val lines = Source.fromFile(filenameIntput).getLines.toList
lines.size
lines.size

lines.forall(_.size > 50)
lines.forall(_.size > 100)

lines.exists(_.contains("llaves"))
lines.exists(_.contains("datos"))

lines.collect { case line if line.startsWith("U") => line.size }

lines.takeWhile(_.distinct.size > 20)

lines.mkString(System.lineSeparator())

lines.headOption.getOrElse("No hay primera linea")

Range.inclusive(1,10).zip(lines).mkString(System.lineSeparator())


// Escritura de ficheros

import java.io.PrintWriter

val filenameOutput = "/home/bigdata/microcuento_uppercase.txt"
val printWriter = new PrintWriter(filenameOutput)

lines.foreach(line => printWriter.println(line.toUpperCase))

printWriter.close()
```



A continuación se muestra la ejecución del código en video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652182_1/scormcontent/assets/Video%2010%20fichero.mp4?v=1)



### 5.8 Programación asíncrona



La programación concurrente es un paradigma esencial en la informática moderna, utilizado para manejar múltiples tareas de forma simultánea, maximizando el rendimiento y optimizando los recursos del sistema. En el ecosistema de Scala, las herramientas más utilizadas para implementar concurrencia incluyen **Futuros** y **Promesas**, dos conceptos fundamentales que permiten modelar y gestionar operaciones asincrónicas de manera eficiente. Un **futuro** es un valor que se calcula de forma asincrónica, y una **promesa** es una herramienta para asignar manualmente ese valor. Vamos a revisar implementado en un código, que es como mejor se entiende y tras mostrarlo se explicará en detalle:



```scala
// Futuros

import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

def calcularResultado(): Future[Int] = Future {
  Thread.sleep(5000)
  33
}

val resultadoFuture: Future[Int] = calcularResultado()

resultadoFuture.foreach { resultado =>
  println(s"El resultado del futuro es: $resultado")
}

// Promesas

import scala.concurrent.Promise
import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

val promesaResultado = Promise[Int]()

val futuroResultado: Future[Int] = promesaResultado.future

futuroResultado.foreach { resultado =>
  println(s"El resultado del futuro de la promesa es: $resultado")
}

promesaResultado.success(99)
```



1. En la parte de futuros:

   - Primero se realizan los imports. Se importa la clase Future y el contexto de ejecución global, necesario para manejar los subprocesos en los que se ejecutará el código concurrente.
   - Seguidamente se define un Futuro. Aquí se define una función calcularResultado, que devuelve un Future[Int]. El cuerpo del futuro contiene una operación simulada (un retardo de 5 segundos con Thread.sleep(5000)) seguida de la devolución del valor 33.
   - Se ejecuta el futuro. Se asigna el resultado del futuro a la variable resultadoFuture, activando la ejecución asincróna.
   - Ejecución del callback. Cuando el futuro completa su ejecución, se ejecuta el callback proporcionado a foreach, que imprime el resultado (33). Esto demuestra cómo manejar la salida de operaciones asincrónicas. El callback de un futuro es una función que se ejecuta automáticamente cuando el futuro completa su operación asincrónica, ya sea con éxito o con error. Este callback recibe el resultado del futuro y permite procesarlo sin bloquear el flujo del programa. Esto asegura que el programa sigue funcionando mientras el futuro se completa, y el callback se encarga de manejar el resultado cuando esté listo.
2. En la parte de promesas:

   - En la importación de librerías, además de los Futuros, se importa Promise, una herramienta que permite crear futuros controlados manualmente.
   - Creación de una promesa. Se crea una instancia de Promise[Int], un contenedor para un valor que será completado en el futuro.
   - Vinculación con un futuro: Cada promesa tiene un futuro asociado (promesaResultado.future), que se completará cuando la promesa sea resuelta.
   - Resolución de la promesa: Se completa la promesa con éxito (success(99)), lo que activa el futuro asociado. El valor 99 es propagado al callback, que lo imprime.
3. Por tanto la salida esperada tras ejecutar este programa será:

   - Después de 5 segundos, el primer bloque (futuro) imprimirá: El resultado del futuro es: 33
   - Inmediatamente después de completar la promesa, el segundo bloque imprimirá: El resultado del futuro de la promesa es: 99



Nota: Si al ejecutar no conseguimos ver nda por consola, es conveniente añadir al final del código una  espera : Thread.sleep(6000). Esto es necesario para que el programa principal no termine antes de que el Future asociado a la promesa sea procesado.

La siguiente tabla resume la compartiva entre futuro y promesa:

| Aspecto | Future | Promise |
| --- | --- | --- |
| Inicio del cálculo | Automático al crear el Future . | Manual: el valor del Future depende de completar la promesa. |
| Propósito | Representa una tarea asincrónica que ya está en ejecución. | Permite completar un Future de forma controlada. |
| Ejemplo | Un cálculo pesado o una solicitud HTTP. | Un evento que depende de factores externos (como un resultado manual o una señal). |



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



Tras haber leído el contenido de esta unidad y haber visualizado los vídeos, el alumno debería ser capaz de enfrentarse a problemas prácticos en lenguaje Scala. No obstante, se recomienda que practique con ejercicios adicionales. En la actividad práctica el alumno tendrá ocasión de enfrentarse a tres ejercicios adicionales. Es muy importante poner el foco en las diferencias del lenguaje Scala así como en sus particularidades remarcadas en esta unidad. Se recomienda conseguir una chestsheet del lenguaje que ayude a alumno a realizar códigos de forma eficiente y con un enfoque funcional.

Si al llegar a este punto:

- Sientes confianza y soltura para explicar las particularidades del lenguaje Scala
- Entiendes la jerarquía de clases del lenguaje
- Comprendes los ejercicios propuestos y te sientes capaz de explicar el código y aplicarlo a nuevos enunciados

Se podría decir que has superado las expectativas de esta primera unidad y posees la base que se requiere para enfrentarte con éxito a las siguientes unidades.
