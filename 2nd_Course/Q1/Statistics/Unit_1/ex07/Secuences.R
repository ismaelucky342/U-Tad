# Usando el operador :
x <- 1:5  # Secuencia de 1 a 5
print(x)  # [1] 1 2 3 4 5

# Usando la función seq() con incremento predeterminado (por defecto 1)
y <- seq(1, 5)  # Secuencia de 1 a 5
print(y)  # [1] 1 2 3 4 5

# Usando seq() con un incremento especificado
z <- seq(1, 10, by = 2)  # Secuencia de 1 a 10 con incremento de 2
print(z)  # [1] 1 3 5 7 9

# Usando seq() especificando la longitud de la secuencia
w <- seq(1, 5, length.out = 3)  # Secuencia de 3 números entre 1 y 5
print(w)  # [1] 1.0 3.0 5.0
