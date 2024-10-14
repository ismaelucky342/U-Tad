#Muestreo aleatorio simple sin reemplazamiento
#Imaginemos que tenemos una población de 100 elementos (numerados del 1 al 100) y queremos tomar una muestra de 10 elementos.

# Muestreo sin reemplazamiento
poblacion <- 1:100
muestra_sin_reemplazo <- sample(poblacion, 10)
print(muestra_sin_reemplazo)


# result: [1] 50 34 67 2 89 23 11 76 41 92
