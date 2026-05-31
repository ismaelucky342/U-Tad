// Otro ejemplo de función pura, esta vez con recursión

// modo imperativo 

def factorialImperativo(n: Int): Int = {
  var result = 1
  for (i <- 1 to n) {
    result *= i
  }
  return result
}

// modo funcional (scala puro)

def factorialFuncional(n: Int): Int = {
  if (n == 0) 1
  else n * factorialFuncional(n - 1)
}


