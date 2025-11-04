# AEC2 - Conslutas en MongoDB

---

## Introducción

Contamos con el archivo `restaurants.json`, que contiene información sobre **3772 restaurantes de Nueva York**. Cada documento incluye detalles como:

- Nombre del restaurante
- Dirección
- Distrito
- Puntuaciones de las reseñas
- Tipo de comida
- Coordenadas geográficas

> Nota: Los nombres de los restaurantes no son únicos, ya que puede haber varios restaurantes de la misma cadena.

La información del archivo `restaurants.json` deberá almacenarse en una colección denominada **restaurants** en MongoDB. Posteriormente, se realizarán consultas y agregaciones para obtener la información solicitada.

---

## Tareas

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

## Instrucciones de Uso

Este proyecto contiene 30 ejercicios de consultas MongoDB trabajando con la base de datos `restaurantesNY`. La práctica cubre desde consultas básicas hasta agregaciones complejas.

El dataset que uso es de restaurantes de Nueva York con información sobre ubicación, tipo de cocina y un historial de calificaciones (grades) que incluye nota, puntuación numérica y fecha. En total son 3772 restaurantes repartidos por los 5 distritos de Nueva York.

## Estructura del Proyecto

```
AEC2/
├── consultas_mongodb.js         # las 3 consultas
├── setup.sh                     # script para importar el JSON a MongoDB
├── export_results.sh            # script para exportar resultados (ejercicios 1, 6, 13)
├── restaurants.json             # Dataset original
└── README.md                    
```

Todo el código de las consultas está en consultas_mongodb.js`, organizado del ejercicio 1 al 30, con mis comentarios explicativos y anotacioness antes de cada query.

## Desarrollo

### Uso:

**Setup rápido:**
```bash
chmod +x setup.sh
./setup.sh
```

Esto crea la base de datos `restaurantesNY`, la colección `restaurants` e importa los 3772 documentos.

### Evolución de las Consultas

He organizado las queries por bloques de dificultad:

**Ejercicios 1-10:**
- Operadores de comparación básicos 
- Proyecciones para seleccionar campos específicos
- `skip()` y `limit()` para paginación
- arrays
- Indexación en arrays con notación de punto 
- Operadores lógicos 
- ordenacion de resultados

**Ejercicios 11-20:**
- Regex case-insensitive
- Combinación de múltiples condiciones 
- Negaciones con `$not` 
- Primeras agregaciones
- `$group` para agrupar y contar documentos
- Agrupaciones por múltiples campos
- `$unwind` para descomponer arrays

**Ejercicios 21-30:**
- Pipeline de agregación con múltiples etapas
- Análisis estadísticos
- Operadores temporales 
- `$filter` para operaciones dentro de arrays sin descomponerlos
- `$cond` para lógica condicional 

## Comandos Útiles que he usado

**Conectarse y cargar:**
```bash
mongosh restaurantesNY
load('consultas_mongodb.js')
```

**Exportar resultados:**
```bash
chmod +x export_results.sh
./export_results.sh
```

Esto genera los JSON de los ejercicios 1, 6 y 13 que requieren exportación.

**Verificar importación:**
```javascript
db.restaurants.countDocuments()  // Debe devolver 3772
db.restaurants.findOne()         // Ver un documento de ejemplo
```


---

## Extras

Esta AEC2 ha sido una buena forma de profundizar en MongoDB más allá de las consultas básicas que habíamos visto. Al principio los ejercicios son bastante directos, pero a partir del 15 cuando empiezan las agregaciones la cosa se complica.

**Lo que más me ha costado:**
- El ejercicio 22 de las probabilidades. Tener que hacer todos los cálculos dentro del pipeline me obligó a entender bien cómo funcionan los operadores condicionales y las divisiones.
- Los ejercicios 29 y 30 con los top 5 por categoría. No hay una función directa para esto, hay que construir el ranking manualmente con $group, $push y $slice. La primera vez que lo intenté me salió mal porque no ordené antes de agrupar.

La práctica está muy bien estructurada con la progresión de dificultad. Te obliga a usar casi todo el repertorio de operadores de MongoDB y a pensar en cómo estructurar pipelines de agregación complejos.


![alt text](image-1.png)