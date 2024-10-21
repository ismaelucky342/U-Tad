# Especificar los niveles en un orden personalizado
factor_vivienda_custom <- factor(tipo_vivienda, levels = c("casa", "piso", "adosado"))

# Imprimir el factor con los niveles personalizados
print(factor_vivienda_custom)

# Ver los niveles del factor
levels(factor_vivienda_custom)
