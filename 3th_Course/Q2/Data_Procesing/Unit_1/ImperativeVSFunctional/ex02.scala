// Ejemplo un poco mas avanzado de programacion funcional en scala vs imperativa con transformaciones

// estilo imperativo

def transformListImperativo(lst: List[Int]): List[Int] = {
  var result = List[Int]()
  for (elem <- lst) {
    if (elem % 2 == 0) {
      result = result :+ (elem * 2)
    }
  }
  return result
}

// estilo funcional (scala puro)

def transformListFuncional(lst: List[Int]): List[Int] = {
  lst.filter(_ % 2 == 0).map(_ * 2)
}

// En el estilo funcional, se utilizan funciones de orden superior como filter y map para transformar la lista de manera más concisa y expresiva.
