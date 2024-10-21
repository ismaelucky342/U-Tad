# Generamos una población de ejemplo
set.seed(123)
poblacion <- data.frame(
  id = 1:100,
  grupo = rep(letters[1:5], each = 20), # 5 conglomerados (A, B, C, D, E)
  variable_1 = rnorm(100, mean = 50, sd = 10),  # Datos de una variable
  estrato = rep(1:2, each = 50)  # Dos estratos (1 y 2)
)

# Ver los primeros datos
head(poblacion)

### 1. Muestreo por Conglomerados ###
# Dividimos la población en conglomerados y seleccionamos algunos conglomerados al azar
conglomerados <- unique(poblacion$grupo)
conglomerados_seleccionados <- sample(conglomerados, size = 2)  # Seleccionamos 2 conglomerados al azar
muestra_conglomerados <- subset(poblacion, grupo %in% conglomerados_seleccionados)

cat("Muestra por conglomerados:\n")
print(muestra_conglomerados)

### 2. Muestreo de Conveniencia ###
# Seleccionamos los primeros 10 individuos que estén disponibles
muestra_conveniencia <- poblacion[1:10, ]

cat("\nMuestra de conveniencia:\n")
print(muestra_conveniencia)

### 3. Muestreo Sistemático ###
# Seleccionamos cada k-ésimo individuo de la población
k <- 10  # Vamos a tomar 1 individuo cada 10
indices <- seq(1, nrow(poblacion), by = k)
muestra_sistematica <- poblacion[indices, ]

cat("\nMuestra sistemática:\n")
print(muestra_sistematica)

### 4. Muestreo Estratificado ###
# Dividimos la población en estratos y tomamos una muestra de cada uno
muestra_estratificada <- do.call(rbind, lapply(split(poblacion, poblacion$estrato), function(estrato) {
  sample_estrato <- estrato[sample(1:nrow(estrato), size = 5), ]  # Seleccionamos 5 individuos de cada estrato
  return(sample_estrato)
}))

cat("\nMuestra estratificada:\n")
print(muestra_estratificada)
