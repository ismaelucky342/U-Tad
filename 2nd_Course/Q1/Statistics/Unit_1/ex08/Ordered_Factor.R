# Crear un vector de calificaciones (orden cualitativo)
calificaciones <- c("medio", "alto", "bajo", "medio", "alto", "bajo")

# Convertir el vector en un factor ordenado
factor_calificaciones <- factor(calificaciones, 
                                levels = c("bajo", "medio", "alto"), 
                                ordered = TRUE)

# Imprimir el factor ordenado
print(factor_calificaciones)

# Comparar elementos del factor
print(factor_calificaciones[1] < factor_calificaciones[2])  # TRUE
