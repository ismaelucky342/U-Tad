# Fijar la semilla para replicar resultados
# Supongamos que queremos asegurarnos de que siempre obtengamos la misma muestra.
# Usamos la función set.seed() para fijar la semilla.

# Fijar la semilla
set.seed(2024)
muestra_con_semilla <- sample(poblacion, 10)
print(muestra_con_semilla)

# result: [1] 82 7 66 28 51 93 34 13 44 10
