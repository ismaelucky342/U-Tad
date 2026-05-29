// mismo metodo pero en scala

def calculateAverage(a: Double, b: Double): Double = {
  return (a + b) / 2.0
}

// ejemplo con estilo scala puro 

def calculateAverage(a: Double, b: Double): Double = (a + b) / 2.0

// ¿En que se diferencia el estilo scala puro del estilo scala normal?

// El estilo scala puro se caracteriza por ser más conciso y expresivo,
//evitando el uso de palabras clave innecesarias como "return" y utilizando la inferencia de tipos
// para simplificar la sintaxis. En el ejemplo dado, el estilo scala puro omite la palabra clave "return"
// y el tipo de retorno, ya que Scala puede inferirlo automáticamente. Además, el código es más directo y fácil de leer,
// lo que es una característica común del estilo scala puro.

