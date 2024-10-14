# Instalar paquete ggplot2
install.packages("ggplot2")

# Cargar data.frame diamonds del paquete ggplot2
library(ggplot2)
data("diamonds")

# Obtener una muestra aleatoria
library(dplyr)
sample_data <- sample_n(diamonds, 100)
