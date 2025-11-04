//====================================================================================================#
//                                                                                                    #
//                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
//      AEC2 - ABDS                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
//                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
//      created:        23/10/2025  -  23:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
//      last change:    04/11/2025  -  18:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
//                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
//                                                                                                    #
//      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
//                                                                                                    #
//      Github:                                           https://github.com/ismaelucky342            #
//                                                                                                    #
//====================================================================================================#

// Documento hecho de forma voluntaria para ampliar

// 1. Contar el total de librerías en la colección
// Uso countDocuments() sin filtros para obtener el total
print("1. Total de librerías:");
print(db.bookstores.countDocuments());

// 2. Librerías abiertas desde 2018 hacia ahora
// Filtro: year_opened >= 2018, ordeno de más reciente a más antiguo
// Proyecto solo nombre y año (sin _id para que quede más limpio)
print("\n2. Librerías desde 2018 (más nuevas primero):");
db.bookstores.find(
  { year_opened: { $gte: 2018 } },
  { name: 1, year_opened: 1, _id: 0 }
).sort({ year_opened: -1 }).forEach(printjson);

// 3. Busco librerías que tengan francés en su array de idiomas
// El operador directo sobre array busca si "fr" está dentro
print("\n3. Librerías con francés:");
db.bookstores.find(
  { languages: "fr" },
  { name: 1, borough: 1, _id: 0 }
).forEach(printjson);

// 4. Filtro por capacidad Y superficie a la vez, ordeno por capacidad
// Limito a 10 resultados como pide el enunciado
print("\n4. Librerías grandes (capacity>=80 y area>=200), top 10:");
db.bookstores.find(
  { 
    capacity: { $gte: 80 },
    area_sqm: { $gte: 200 }
  },
  { name: 1, capacity: 1, area_sqm: 1, _id: 0 }
).sort({ capacity: -1 }).limit(10).forEach(printjson);

// 5. Librerías que tienen el campo chain (pertenecen a una cadena)
// $exists: true verifica que exista el campo
print("\n5. Librerías de cadena:");
db.bookstores.find(
  { chain: { $exists: true } },
  { name: 1, "chain.name": 1, "chain.branch_id": 1, _id: 0 }
).forEach(printjson);

// 6. Filtro por distrito Chamberí Y que tengan inglés
// Doble condición: borough = "Chamberí" AND "en" en languages
print("\n6. Chamberí con inglés:");
db.bookstores.find(
  { 
    borough: "Chamberí",
    languages: "en"
  },
  { name: 1, languages: 1, _id: 0 }
).forEach(printjson);

// 7. Busco librerías que tengan AMBAS categorías: academic Y art
// $all se asegura de que estén las dos en el array
print("\n7. Librerías academic + art:");
db.bookstores.find(
  { 
    categories: { $all: ["academic", "art"] }
  },
  { name: 1, borough: 1, neighborhood: 1, _id: 0 }
).forEach(printjson);

// 8. Librerías económicas (precio $) pero con buena valoración
// Combino price_level = "$" con rating.avg >= 4.5
print("\n8. Baratas pero buenas ($ y rating>=4.5):");
db.bookstores.find(
  { 
    price_level: "$",
    "rating.avg": { $gte: 4.5 }
  },
  { name: 1, neighborhood: 1, "rating.avg": 1, _id: 0 }
).forEach(printjson);

// 9. Librerías que tienen eventos programados
// events debe existir Y no ser array vacío
print("\n9. Con eventos programados:");
db.bookstores.find(
  { 
    events: { $exists: true, $ne: [] }
  },
  { name: 1, borough: 1, _id: 0 }
).forEach(printjson);

// 10. En Salamanca, las que tienen workshops
// Busco dentro del array events alguno con type = "workshop"
print("\n10. Salamanca con workshops:");
db.bookstores.find(
  { 
    borough: "Salamanca",
    "events.type": "workshop"
  },
  { name: 1, _id: 0 }
).forEach(printjson);

print("\n--- AGREGACIONES ---\n");

// Antes de empezar con las agregaciones, creo un índice sobre las fechas
// Esto mejora el rendimiento cuando filtro por eventos
print("Creando índice en events.date...");
print(db.bookstores.createIndex({ "events.date": 1 }));

// 11. Agrupo por distrito y cuento cuántas hay en cada uno
// Simple: $group por borough, $sum: 1 para contar
print("\n11. Librerías por distrito:");
db.bookstores.aggregate([
  { $group: { _id: "$borough", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]).forEach(printjson);

// 12. Calculo la media de valoración en cada distrito
// $avg sobre rating.avg, ordeno de mejor a peor
print("\n12. Rating medio por distrito:");
db.bookstores.aggregate([
  { $group: { _id: "$borough", avg_rating: { $avg: "$rating.avg" } } },
  { $sort: { avg_rating: -1 } }
]).forEach(printjson);

// 13. Top 5 barrios mejor valorados, pero solo los que tengan 3+ librerías
// Agrupo, cuento, filtro con $match y me quedo con el top 5
print("\n13. Top 5 barrios (min 3 librerías):");
db.bookstores.aggregate([
  {
    $group: {
      _id: "$neighborhood",
      avg_rating: { $avg: "$rating.avg" },
      count: { $sum: 1 }
    }
  },
  { $match: { count: { $gte: 3 } } },
  { $sort: { avg_rating: -1 } },
  { $limit: 5 }
]).forEach(printjson);

// 14. Cuento cuántas librerías hay de cada categoría
// Como categories es array, uso $unwind para "desplegar" cada valor
print("\n14. Count por categoría:");
db.bookstores.aggregate([
  { $unwind: "$categories" },
  { $group: { _id: "$categories", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]).forEach(printjson);

// 15. Media de superficie y capacidad por cada categoría
// Mismo truco: unwind para separar las categorías y luego agrupar
print("\n15. Superficie y aforo medio por categoría:");
db.bookstores.aggregate([
  { $unwind: "$categories" },
  {
    $group: {
      _id: "$categories",
      avg_area: { $avg: "$area_sqm" },
      avg_capacity: { $avg: "$capacity" }
    }
  },
  { $sort: { avg_area: -1 } }
]).forEach(printjson);

// 16. Densidad = personas por metro cuadrado (capacity/area_sqm)
// Primero calculo density con $addFields, luego agrupo y promedío
print("\n16. Densidad media por distrito:");
db.bookstores.aggregate([
  { $addFields: { density: { $divide: ["$capacity", "$area_sqm"] } } },
  { $group: { _id: "$borough", avg_density: { $avg: "$density" } } },
  { $sort: { avg_density: -1 } }
]).forEach(printjson);

// 17. Eventos por mes durante 2025
// Despliego events, filtro por año, extraigo el mes con $month
print("\n17. Eventos por mes en 2025:");
db.bookstores.aggregate([
  { $unwind: "$events" },
  {
    $match: {
      "events.date": {
        $gte: ISODate("2025-01-01T00:00:00Z"),
        $lt: ISODate("2026-01-01T00:00:00Z")
      }
    }
  },
  { $group: { _id: { $month: "$events.date" }, count: { $sum: 1 } } },
  { $sort: { _id: 1 } },
  { $project: { _id: 0, month: "$_id", count: 1 } }
]).forEach(printjson);

// 18. Porcentaje de librerías con inglés en cada distrito
// Uso $cond para contar las que tienen "en" y calculo el porcentaje
print("\n18. % de librerías con inglés por distrito:");
db.bookstores.aggregate([
  {
    $group: {
      _id: "$borough",
      total: { $sum: 1 },
      with_english: {
        $sum: { $cond: [{ $in: ["en", "$languages"] }, 1, 0] }
      }
    }
  },
  {
    $project: {
      _id: 1,
      total: 1,
      with_english: 1,
      proportion: { $multiply: [{ $divide: ["$with_english", "$total"] }, 100] }
    }
  },
  { $sort: { proportion: -1 } }
]).forEach(printjson);

// 19. Las 5 librerías mejor valoradas
// Simplemente ordeno por rating.avg descendente y limito a 5
print("\n19. Top 5 librerías mejor valoradas:");
db.bookstores.aggregate([
  { $sort: { "rating.avg": -1 } },
  { $limit: 5 },
  { $project: { _id: 0, name: 1, borough: 1, rating: "$rating.avg" } }
]).forEach(printjson);

// 20. Total de asistencia esperada por tipo de evento en Q2 2025
// Rango: marzo a junio 2025, despliego eventos y sumo expected_attendance
print("\n20. Asistencia total por tipo (Mar-Jun 2025):");
db.bookstores.aggregate([
  { $unwind: "$events" },
  {
    $match: {
      "events.date": {
        $gte: ISODate("2025-03-01T00:00:00Z"),
        $lte: ISODate("2025-06-30T23:59:59Z")
      }
    }
  },
  {
    $group: {
      _id: "$events.type",
      total_attendance: { $sum: "$events.expected_attendance" }
    }
  },
  { $sort: { total_attendance: -1 } }
]).forEach(printjson);

print("\n✓ Consultas completadas\n");
