# Datos de ejemplo
metodologia <- factor(c("Scrum", "Kanban", "Waterfall", "Scrum", "Kanban"))
tiempo_dias <- c(30, 45, 60, 35, 50)
satisfaccion_cliente <- factor(c(8, 7, 9, 10, 6), ordered = TRUE, levels = 1:10)

# Crear un dataframe para representar los datos
datos_proyectos <- data.frame(
  metodologia,
  tiempo_dias,
  satisfaccion_cliente
)

# Ver los datos
print(datos_proyectos)
