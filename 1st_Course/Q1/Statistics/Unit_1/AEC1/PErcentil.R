# Datos de ejemplo
x <- c(2, 4, 4, 5, 5, 5, 6, 7, 8, 9)

# Calcular el tercer cuartil (Q3)
Q3 <- quantile(x, 0.75)

# Crear un diagrama de caja y bigotes
boxplot(x, main = "Diagrama de Caja y Bigotes", col = "lightblue", border = "darkblue")

# Agregar una línea horizontal en Q3
abline(h = Q3, col = "red", lwd = 2, lty = 2)  # Línea roja discontinua en Q3
