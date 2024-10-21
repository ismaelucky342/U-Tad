#Muestreo aleatorio simple con reemplazamiento
#En este caso, los elementos pueden ser seleccionados más de una vez. 
#Supongamos que nuevamente tenemos una población de 100 elementos y tomamos una muestra de 10
#pero permitiendo reemplazamiento.

# Muestreo con reemplazamiento
muestra_con_reemplazo <- sample(poblacion, 10, replace = TRUE)
print(muestra_con_reemplazo)

# result: [1] 34 88 21 21 12 45 34 67 12 99
