# Crear un vector
v <- c(10, 20, 30, 40, 50)

# Acceder al segundo elemento
print(v[2])  # [1] 20

# Acceder a múltiples elementos (por ejemplo, el primero y el cuarto)
print(v[c(1, 4)])  # [1] 10 40

# Excluir un elemento específico (por ejemplo, excluir el tercer elemento)
print(v[-3])  # [1] 10 20 40 50

# Usar un vector lógico para la indexación (acceder a elementos mayores que 25)
print(v[v > 25])  # [1] 30 40 50
