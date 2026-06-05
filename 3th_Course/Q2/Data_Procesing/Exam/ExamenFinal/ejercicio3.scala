// =================================================================================================== //
//                                                                                                     //
//                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗          //
//     Procesamiento de datos - Examen Final             ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗         //
//                                                       ██║   ██║█████╗██║   ███████║██║  ██║         //
//     created:        05/06/2026  -  9:10:00            ██║   ██║╚════╝██║   ██╔══██║██║  ██║         //
//     last change:    05/06/2026  -  10:56:12           ╚██████╔╝      ██║   ██║  ██║██████╔╝         //
//                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝          //
//                                                                                                     //
//     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com               //
//                                                                                                     // 
//     Github:                                           https://github.com/ismaelucky342              // 
//                                                                                                     // 
// =================================================================================================== // 

/*
 *En este ejercicio se quiere modelar de forma sencilla un producto de una tienda utilizando algunas características propias de Scala: clases, traits, métodos y objetos acompañantes.



Para ello, debes crear un trait llamado Vendible, que represente el comportamiento común que debería tener cualquier elemento que pueda venderse. Este trait deberá definir dos métodos: uno llamado descripcion, que devuelva una descripción textual del producto, y otro llamado precioConIVA, que devuelva el precio del producto aplicando un 21% de IVA sobre su precio original.



A continuación, debes crear una clase llamada Producto, que tendrá como atributos el nombre del producto y su precio. Esta clase deberá extender el trait Vendible e implementar los métodos definidos en él. El método descripcion deberá devolver una cadena de texto que muestre el nombre del producto y su precio original, mientras que el método precioConIVA deberá calcular el precio aplicando un 21% de IVA.



Además, la clase Producto deberá incluir un método llamado aplicarDescuento, que reciba como parámetro un porcentaje de descuento y devuelva el precio del producto después de aplicar dicho descuento.



También deberá incluir un método llamado precioFinal, que reciba como parámetro un porcentaje de descuento. Este método deberá calcular primero el precio del producto con el descuento aplicado y, posteriormente, aplicar el 21% de IVA sobre ese precio ya descontado.



Por último, deberás crear un objeto acompañante llamado Producto. Este objeto tendrá un método crearProducto, que recibirá el nombre y el precio de un producto, y devolverá una nueva instancia de la clase Producto.



Para comprobar el funcionamiento del programa, crea un producto llamado "Teclado" con precio 30.0 utilizando el objeto acompañante. Después, muestra por pantalla su descripción, su precio original con IVA, su precio con un descuento del 10% y su precio final con descuento e IVA.



La salida esperada será similar a la siguiente:



Producto: Teclado | Precio original: 30.0

Precio con IVA: 36.3

Precio con descuento: 27.0

Precio final con descuento e IVA: 32.67



Nota. esta vez debe entregarse un fichero .scala es decir tiene que existir el objeto Main



Trait y objeto acompañante Producto: 0,5 puntos

clase producto 0,5 puntos

object Main para probar 0,5 puntos
 * */


sealed trait Vendible {
  def descripcion: String
  def precioConIVA: Double
}

// Clase producto 
case class Producto(nombre: String, precio: Double) extends Vendible {
  def descripcion: String = s"Producto: $nombre | Precio original: $precio"
  
  def precioConIVA: Double = precio * 1.21
  
  def aplicarDescuento(descuento: Double): Double = precio * (1 - descuento / 100)
  
  def precioFinal(descuento: Double): Double = aplicarDescuento(descuento) * 1.21
}

object Producto {
  def crearProducto(nombre: String, precio: Double): Producto = Producto(nombre, precio)
}

// producto de prueba 

object Main extends App {
  val teclado = Producto.crearProducto("Teclado", 30.0)
  
  println(teclado.descripcion)
  println(f"Precio con IVA: ${teclado.precioConIVA}%.2f")
  println(f"Precio con descuento: ${teclado.aplicarDescuento(10)}%.2f")
  println(f"Precio final con descuento e IVA: ${teclado.precioFinal(10)}%.2f")
}

