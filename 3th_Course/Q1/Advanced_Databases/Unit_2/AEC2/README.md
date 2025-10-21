# Actividad Práctica: Derivación Logarítmica

## Información General

- **Centro adscrito:** [Indicar centro]
- **Organización de la actividad práctica:** Derivación Logarítmica
- **Tipo de tarea:** Individual
- **Entregables:** `INSD_ABDS_U2_Apellido1_Apellido2_Nombre.zip`

---

## Descripción de la Actividad

Tras finalizar el grado en Ingeniería del Software, queremos dedicarnos a nuestra pasión: la hostelería. Nuestro objetivo es abrir el nuevo restaurante de moda en Nueva York, pero primero aplicaremos los conocimientos de bases de datos adquiridos durante el grado para analizar el entorno: tipos de comida, competidores, puntuaciones, etc.

Para ello contamos con el archivo `restaurants.json`, que contiene información sobre **3772 restaurantes de Nueva York**. Cada documento incluye detalles como:

- Nombre del restaurante
- Dirección
- Distrito
- Puntuaciones de las reseñas
- Tipo de comida
- Coordenadas geográficas

> Nota: Los nombres de los restaurantes no son únicos, ya que puede haber varios restaurantes de la misma cadena.

La información del archivo `restaurants.json` deberá almacenarse en una colección denominada **restaurants** en MongoDB. Posteriormente, se realizarán consultas y agregaciones para obtener la información solicitada.

---

## Tareas a Realizar

1. Encontrar los restaurantes con puntuación superior a 80 pero inferior a 100. Exportar el resultado a un archivo JSON.  
2. Mostrar los 5 restaurantes siguientes después de omitir los 5 primeros en el distrito del Bronx.  
3. Mostrar Id, nombre, dirección y ubicación de restaurantes cuyo segundo elemento del array `coord` esté entre 42 y 52.  
4. Seleccionar Id, nombre y calificaciones de los restaurantes cuya puntuación dividida entre 7 dé resto 0.  
5. Encontrar restaurantes que **no preparan cocina americana** y tienen nota 'A', excluyendo Brooklyn, ordenados descendientemente por tipo de cocina.  
6. Mostrar nombre, dirección y notas de restaurantes con al menos una calificación 'A', sin calificaciones 'B' ni 'C'. Exportar a JSON.  
7. Mostrar Id, nombre, distrito y tipo de cocina de restaurantes que **no sean americanos ni chinos** o cuyo nombre empiece por "Wil".  
8. Mostrar Id, nombre y calificaciones de restaurantes que obtuvieron calificación 'A' y puntuación 11 en la fecha ISO "2014-08-11T00:00:00Z".  
9. Mostrar Id, nombre y calificaciones de restaurantes cuyo segundo elemento del array de calificaciones tenga 'A' y puntuación 9 en la fecha ISO "2014-08-11T00:00:00Z".  
10. Encontrar restaurantes con calificaciones de 2 y 6, ubicados en Manhattan o Brooklyn.  
11. Mostrar nombre y dirección de restaurantes que incluyan la palabra "coffee" (mayúsculas/minúsculas indiferente).  
12. Encontrar restaurantes con al menos una nota inferior a 5 en Manhattan o Brooklyn, cuya cocina no sea americana ni china.  
13. Encontrar restaurantes con todas las notas superiores a 5 en Manhattan o Brooklyn. Exportar a JSON.  
14. Mostrar nombre y dirección de restaurantes que recibieron calificación 'B' o 'C' en una fecha determinada.  
15. Mostrar la **puntuación media** de cada restaurante.  
16. Mostrar el **número de restaurantes por distrito**.  
17. Mostrar el **número de restaurantes por tipo de cocina y distrito**.  
18. Mostrar el número de restaurantes que han obtenido la calificación 'A' por tipo de cocina y distrito.  
19. Mostrar la puntuación más baja por tipo de cocina.  
20. Mostrar el nombre y la dirección de los restaurantes cuyo código postal empieza por "10".  
21. Mostrar los restaurantes con la puntuación media más alta.  
22. Encontrar el tipo de cocina con mayor probabilidad de recibir una calificación 'C'.  
23. Encontrar el restaurante con la fecha de calificación más reciente.  
24. Encontrar el restaurante de cocina turca ('Turkish') con la puntuación media más alta.  
25. Mostrar el número de restaurantes que han sido puntuados en cada mes del año.  
26. Encontrar el distrito con más restaurantes que tienen calificación 'A' y puntuación igual o superior a 90.  
27. Mostrar los restaurantes con el mayor número de calificaciones 'A'.  
28. Mostrar los restaurantes que han obtenido la puntuación total más alta.  
29. Mostrar los 5 restaurantes con la puntuación media más alta para cada tipo de cocina, junto con sus puntuaciones medias.  
30. Mostrar los 5 restaurantes de cada distrito con el mayor número de calificaciones 'A'.

---

## Entregable

- Comprimir todos los archivos y consultas MongoDB en un ZIP con el formato:  
  `INSD_ABDS_U2_Apellido1_Apellido2_Nombre.zip`

---

## Instrucciones de Uso

### 1. Importar Datos

```bash
# Dar permisos de ejecución al script
chmod +x setup.sh

# Ejecutar el script de importación
./setup.sh
```

### 2. Ejecutar Consultas

```bash
# Abrir MongoDB shell
mongosh restaurantesNY

# Cargar el archivo de consultas
load('consultas_mongodb.js')
```

### 3. Exportar Resultados

```bash
# Dar permisos de ejecución
chmod +x export_results.sh

# Ejecutar exportación
./export_results.sh
```

### Estructura de Archivos

```
AEC2/
├── README.md                    # Este archivo
├── consultas_mongodb.js         # Todas las consultas numeradas
├── setup.sh                     # Script de importación
├── export_results.sh            # Script de exportación
├── restaurants.json             # Datos originales (proporcionado)
├── ejercicio1_resultados.json   # Resultado ejercicio 1
├── ejercicio6_resultados.json   # Resultado ejercicio 6
└── ejercicio13_resultados.json  # Resultado ejercicio 13
```

### Notas Técnicas

- **Base de datos**: `restaurantesNY`
- **Colección**: `restaurants`
- **Total de documentos**: 3772 restaurantes
- **Índices creados**: borough, cuisine, grades.grade, address.zipcode

### Consultas Destacadas

- **Ejercicios 15-30**: Utilizan agregaciones avanzadas
- **Ejercicios con $elemMatch**: 8, 9, 14, 26
- **Ejercicios con $unwind**: 19, 22, 23, 25
- **Ejercicios con regex**: 11, 20
- **Ejercicios con exportación**: 1, 6, 13
