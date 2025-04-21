# Función para calcular el valor absoluto
valor_absoluto <- function(x) {
    return(abs(x))
}

# Función para calcular la raíz cuadrada
raiz_cuadrada <- function(x) {
    return(sqrt(x))
}

# Ejemplos de uso
x <- -9
y <- 16

cat("El valor absoluto de", x, "es:", valor_absoluto(x), "\n")
cat("La raíz cuadrada de", y, "es:", raiz_cuadrada(y), "\n")