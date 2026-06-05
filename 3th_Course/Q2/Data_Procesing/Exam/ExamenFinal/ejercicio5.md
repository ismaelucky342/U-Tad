Ejercicio 5 Sensores de temperatura en un centro de datos. Procesamiento por ventanas. (0,75 puntos)



Tenemos un sistema de monitorización de temperatura en un centro de datos. Varios sensores instalados en diferentes salas envían eventos con una marca de tiempo, el identificador del sensor y la temperatura registrada.



Queremos calcular el rango de temperaturas, es decir, la diferencia entre la temperatura máxima y mínima, utilizando distintos tipos de ventanas de procesamiento.



Los datos recolectados son los siguientes:



EventID, Time, SensorID, Temperature

------------------------------------

0, 10:00.100, S1, 22

1, 10:00.180, S2, 24

2, 10:00.310, S3, 23

3, 10:00.520, S1, 27

4, 10:00.790, S2, 25

5, 10:01.050, S3, 29

6, 10:01.210, S1, 28

7, 10:01.480, S2, 26

8, 10:01.760, S3, 30

9, 10:02.020, S1, 24



Se pide resolver el ejercicio utilizando los siguientes tipos de ventanas:

Ventana temporal de 1 segundo, donde cada ventana empieza con el cambio de segundo. Suponiendo intervalos cerrados por la izquierda y abiertos por la derecha, es decir: [10:00.000, 10:01.000) (0,5 puntos)

Para calcular el rango de temperaturas utilizando una ventana temporal de 1 segundo, agrupamos los eventos en las siguientes ventanas:

Ventana 1: [10:00.000, 10:01.000)

Eventos: 0, 1, 2, 3, 4

Temperaturas: 22, 24, 23, 27, 25  
 Rango: Max(27) - Min(22) = 5

Ventana 2: [10:01.000, 10:02.000)
Eventos: 5, 6, 7, 8, 9

Temperaturas: 29, 28, 26, 30, 24  
 Rango: Max(30) - Min(24) = 6



Ventana por número de eventos de tamaño 5. (0,25 puntos)

Para esta ventana, agrupamos los eventos en bloques de 5

Eventos: 0, 1, 2, 3, 4
Temperaturas: 22, 24, 23, 27, 25  
 Rango: Max(27) - Min(22) = 5

Eventos: 5, 6, 7, 8, 9

Temperaturas: 29, 28, 26, 30, 24  
 Rango: Max(30) - Min(24) = 6


