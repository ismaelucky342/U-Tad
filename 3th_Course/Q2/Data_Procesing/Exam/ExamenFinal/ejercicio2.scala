// =================================================================================================== //
//                                                                                                     //
//                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗          //
//     Procesamiento de datos - Examen Final             ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗         //
//                                                       ██║   ██║█████╗██║   ███████║██║  ██║         //
//     created:        05/06/2026  -  9:10:00            ██║   ██║╚════╝██║   ██╔══██║██║  ██║         //
//     last change:    05/06/2026  -  10:55:32           ╚██████╔╝      ██║   ██║  ██║██████╔╝         //
//                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝          //
//                                                                                                     //
//     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com               //
//                                                                                                     // 
//     Github:                                           https://github.com/ismaelucky342              // 
//                                                                                                     // 
// =================================================================================================== // 

/*
 *  Dado el siguiente RDD en Spark:



val data = sc.parallelize(List("1,2,3,4", "5,6", "7,8,9,10"))
Cada elemento es una cadena que representa una lista de números separados por comas.
Aplica transformaciones utilizando funciones superiores sobre colecciones, como map, flatMap, filter, count, fold, etc., y una acción para obtener el siguiente resultado:
Cantidad de pares: 5
Es decir se bus que el código sea capaz de contar el numero de elementos pares que hay
Implementa dos versiones diferentes que obtengan dicho resultado:


A) En la primera versión, utiliza map(), filter() y sum() para contar los números pares, transformando cada número par en un 1. 0,5 puntos

B) En la segunda versión, utiliza flatMap(), filter(), map() y fold() para contar los números pares. 0,5 puntos
 *
 * */

// Version A 

val data = sc.parallelize(List("1,2,3,4", "5,6", "7,8,9,10"))

val numeros = data.map(linea => linea.split(",").map(_.toInt)) 

val cantidadPares = numeros.map(arr => arr.count(_ % 2 == 0)).sum()

println(s"Cantidad de pares: $cantidadPares")

// Version B 
//
val data = sc.parallelize(List("1,2,3,4", "5,6", "7,8,9,10"))

val numeros = data.flatMap(linea => linea.split(",").map(_.toInt))

val cantidadPares = numeros.filter(_ % 2 == 0).map(_ => 1).fold(0)(_ + _)

println(s"Cantidad de pares: $cantidadPares")
