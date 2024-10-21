# Crear un vector de tipos de vivienda (caracteres)
tipo_vivienda <- c("piso", "casa", "adosado", "piso", "casa", "adosado", "piso", "casa", "adosado", "piso")

# Convertir el vector en un factor
factor_vivienda <- factor(tipo_vivienda)

# Imprimir el factor
print(factor_vivienda)

# Ver los niveles del factor
levels(factor_vivienda)
