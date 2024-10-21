# Operaciones aritméticas
a <- c(1, 2, 3)
b <- c(4, 5, 6)
suma <- a + b  # Suma elemento a elemento
print(suma)  # [1] 5 7 9

multiplicacion <- a * b  # Multiplicación elemento a elemento
print(multiplicacion)  # [1] 4 10 18

# Comparaciones elemento a elemento
comparacion <- a > b
print(comparacion)  # [1] FALSE FALSE FALSE

# Reciclado de vectores (vector más corto se repite)
c <- c(1, 2)
resultado <- a + c  # [1] 1+1 2+2 3+1
print(resultado)  # [1] 2 4 4
