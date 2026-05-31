// Ejercicio aplicando funciones de orden superior, case classes y opciones

// estilo imperativo 

def processDataImperativo(data: List[Int]): List[Int] = {
  var result = List[Int]()
  for (elem <- data) {
    if (elem > 0) {
      result = result :+ (elem * 2)
    }
  }
  return result
}

// estilo funcional (scala puro)

def processDataFuncional(data: List[Int]): List[Int] = {
  data.filter(_ > 0).map(_ * 2)
}

// filter y map son funciones de orden superior que permiten procesar la lista de manera más concisa y expresiva, evitando la necesidad de mutar variables y utilizando la programación funcional para transformar los datos.