library(knitr)

# Ruta del archivo de datos
path <- "plataforma_b.csv"

# Carga de datos y visualización
datos_b <- read.csv(path)

# Cálculo de estadísticos muestrales
media_visitas_b <- mean(datos_b$Visitas, na.rm = TRUE)
media_ventas_b <- mean(datos_b$Ventas, na.rm = TRUE)
tasa_conversion_b <- mean(datos_b$Ventas, na.rm = TRUE) / mean(datos_b$Visitas, na.rm = TRUE)

kable(head(datos_b), caption = "Primeras filas de los datos de la Plataforma B")

# Contraste de hipótesis para las visitas
test_visitas <- t.test(datos_b$Visitas, mu = 754, alternative = "greater")
cat("Test de Visitas\n")
print(test_visitas)

# Contraste de hipótesis para las ventas
test_ventas <- t.test(datos_b$Ventas[1:23], mu = 135.72, alternative = "greater")
cat("Test de Ventas\n")
print(test_ventas)

# Contraste de hipótesis para la tasa de conversión
conversion_b <- datos_b$Ventas[1:23] / datos_b$Visitas[1:23]
test_conversion <- t.test(conversion_b, mu = 0.18, alternative = "two.sided")
cat("Test de Tasa de Conversión\n")
print(test_conversion)

# Resultados de las conclusiones
if (test_visitas$p.value < 0.05) {
  cat("Conclusión: La media de visitas diarias en la Plataforma B es significativamente mayor que en la Plataforma A.\n")
} else {
  cat("Conclusión: No se puede concluir que la media de visitas diarias en la Plataforma B sea mayor que en la Plataforma A.\n")
}

if (test_ventas$p.value < 0.05) {
  cat("Conclusión: La media de ventas diarias en la Plataforma B es significativamente mayor que en la Plataforma A.\n")
} else {
  cat("Conclusión: No se puede concluir que la media de ventas diarias en la Plataforma B sea mayor que en la Plataforma A.\n")
}

if (test_conversion$p.value < 0.05) {
  cat("Conclusión: La tasa de conversión en la Plataforma B es significativamente distinta a la de la Plataforma A.\n")
} else {
  cat("Conclusión: No se puede concluir que la tasa de conversión en la Plataforma B sea distinta a la de la Plataforma A.\n")
}

