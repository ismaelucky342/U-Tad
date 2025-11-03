//====================================================================================================#
//                                                                                                    #
//                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
//      AEC2 - ABDS                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
//                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
//      created:        29/10/2025  -  23:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
//      last change:    03/11/2025  -  02:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
//                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
//                                                                                                    #
//      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
//                                                                                                    #
//      Github:                                           https://github.com/ismaelucky342            #
//                                                                                                    #
//====================================================================================================#


// Selecciono la base de datos 
use restaurantsNY;

// Ejercicio 1: busco restaurantes con notas entre 80 y 100
// Uso $gt y $lt para el rango, proyecto solo los campos que necesito
db.restaurants.find({
  "grades.score": { $gt: 80, $lt: 100 }
}, {
  name: 1,
  cuisine: 1,
  borough: 1,
  "grades.score": 1
});

// Para exportar: mongoexport --db=restaurantesNY --collection=restaurants --query='{"grades.score": {$gt: 80, $lt: 100}}' --out=ejercicio1.json

// Ejercicio 2: necesito 5 restaurantes del Bronx pero saltando los 5 primeros
// skip() me permite omitir documentos y limit() restringe el resultado
db.restaurants.find({
  borough: "Bronx"
}).skip(5).limit(5);

// Ejercicio 3: filtro por coordenadas, específicamente la segunda posición del array
// coord.1 hace referencia al índice 1 del array (latitud/longitud)
db.restaurants.find({
  "address.coord.1": { $gt: 42, $lt: 52 }
}, {
  _id: 1,
  name: 1,
  address: 1,
  "address.coord": 1
});

// Ejercicio 4: busco puntuaciones divisibles entre 7
// $mod hace el módulo, [7, 0] significa dividir entre 7 con resto 0
db.restaurants.find({
  "grades.score": { $mod: [7, 0] }
}, {
  _id: 1,
  name: 1,
  grades: 1
});

// Ejercicio 5: query con múltiples condiciones
// No americanos, con al menos una A, que no estén en Brooklyn, ordenados por cocina
db.restaurants.find({
  cuisine: { $ne: "American" },
  "grades.grade": "A",
  borough: { $ne: "Brooklyn" }
}).sort({ cuisine: -1 });

// Ejercicio 6: restaurantes que tienen A pero nunca B ni C
// Aquí hay un truco: busco los que tienen A y excluyo los que tienen B o C
db.restaurants.find({
  "grades.grade": "A",
  "grades.grade": { $nin: ["B", "C"] }
}, {
  name: 1,
  address: 1,
  grades: 1
});

// Exportar: mongoexport --db=restaurantesNY --collection=restaurants --query='{"grades.grade": "A", "grades.grade": {$nin: ["B", "C"]}}' --out=ejercicio6.json

// Ejercicio 7: uso OR lógico
// O no son americanos/chinos O el nombre empieza por "Wil"
db.restaurants.find({
  $or: [
    { cuisine: { $nin: ["American", "Chinese"] } },
    { name: /^Wil/ }
  ]
}, {
  _id: 1,
  name: 1,
  borough: 1,
  cuisine: 1
});

// Ejercicio 8: aquí uso $elemMatch para buscar dentro de un array
// Necesito que un mismo elemento del array cumpla todas las condiciones
db.restaurants.find({
  "grades": {
    $elemMatch: {
      grade: "A",
      score: 11,
      date: ISODate("2014-08-11T00:00:00Z")
    }
  }
}, {
  _id: 1,
  name: 1,
  grades: 1
});

// Ejercicio 9: acceso directo a la segunda posición del array grades
// grades.1 es el segundo elemento (índice 1)
db.restaurants.find({
  "grades.1.grade": "A",
  "grades.1.score": 9,
  "grades.1.date": ISODate("2014-08-11T00:00:00Z")
}, {
  _id: 1,
  name: 1,
  grades: 1
});

// Ejercicio 10: $all verifica que el array contenga todos los valores especificados
// En este caso puntuaciones de 2 Y 6, en Manhattan o Brooklyn
db.restaurants.find({
  "grades.score": { $all: [2, 6] },
  borough: { $in: ["Manhattan", "Brooklyn"] }
});

// Ejercicio 11: búsqueda con regex, case insensitive
// /coffee/i busca "coffee" sin importar mayúsculas/minúsculas
db.restaurants.find({
  name: /coffee/i
}, {
  name: 1,
  address: 1
});

// Ejercicio 12: combinación de condiciones
// Al menos una nota menor que 5, en ciertos distritos, excluyendo tipos de cocina
db.restaurants.find({
  "grades.score": { $lt: 5 },
  borough: { $in: ["Manhattan", "Brooklyn"] },
  cuisine: { $nin: ["American", "Chinese"] }
});

// Ejercicio 13: aquí el truco está en negar la condición
// Quiero todos los que NO tengan ninguna nota <= 5
db.restaurants.find({
  borough: { $in: ["Manhattan", "Brooklyn"] },
  "grades.score": { $not: { $lte: 5 } }
});

// Exportar: mongoexport --db=restaurantesNY --collection=restaurants --query='{"borough": {$in: ["Manhattan", "Brooklyn"]}, "grades.score": {$not: {$lte: 5}}}' --out=ejercicio13.json

// Ejercicio 14: de nuevo $elemMatch para múltiples condiciones en un mismo elemento
db.restaurants.find({
  "grades": {
    $elemMatch: {
      grade: { $in: ["B", "C"] },
      date: ISODate("2014-08-11T00:00:00Z")
    }
  }
}, {
  name: 1,
  address: 1
});

// Ejercicio 15: mi primera agregación
// $avg calcula la media de todas las puntuaciones del array grades
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      avgScore: { $avg: "$grades.score" }
    }
  }
]);

// Ejercicio 16: agrupación simple
// Cuento cuántos restaurantes hay por distrito
db.restaurants.aggregate([
  {
    $group: {
      _id: "$borough",
      count: { $sum: 1 }
    }
  },
  {
    $sort: { count: -1 }
  }
]);

// Ejercicio 17: agrupación por dos campos
// Agrupo por tipo de cocina Y distrito para ver la distribución
db.restaurants.aggregate([
  {
    $group: {
      _id: {
        cuisine: "$cuisine",
        borough: "$borough"
      },
      count: { $sum: 1 }
    }
  },
  {
    $sort: { "_id.cuisine": 1, "_id.borough": 1 }
  }
]);

// Ejercicio 18: filtro antes de agrupar
// Primero selecciono los que tienen A, luego agrupo
db.restaurants.aggregate([
  {
    $match: {
      "grades.grade": "A"
    }
  },
  {
    $group: {
      _id: {
        cuisine: "$cuisine",
        borough: "$borough"
      },
      count: { $sum: 1 }
    }
  },
  {
    $sort: { count: -1 }
  }
]);

// Ejercicio 19: $unwind es clave aquí
// Descompongo el array grades para poder trabajar con cada elemento individualmente
db.restaurants.aggregate([
  {
    $unwind: "$grades"
  },
  {
    $group: {
      _id: "$cuisine",
      minScore: { $min: "$grades.score" }
    }
  },
  {
    $sort: { minScore: 1 }
  }
]);

// Ejercicio 20: regex para códigos postales
// ^ indica inicio de cadena, busco los que empiezan por "10"
db.restaurants.find({
  "address.zipcode": /^10/
}, {
  name: 1,
  address: 1
});

// Ejercicio 21: ranking de mejores puntuaciones medias
// Calculo la media y ordeno descendente para ver los top
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      avgScore: { $avg: "$grades.score" }
    }
  },
  {
    $sort: { avgScore: -1 }
  },
  {
    $limit: 10
  }
]);

// Ejercicio 22: análisis de probabilidad
// Para cada tipo de cocina calculo qué % de sus notas son C
db.restaurants.aggregate([
  {
    $unwind: "$grades"
  },
  {
    $group: {
      _id: "$cuisine",
      totalGrades: { $sum: 1 },
      gradeC: {
        $sum: {
          $cond: [{ $eq: ["$grades.grade", "C"] }, 1, 0]
        }
      }
    }
  },
  {
    $project: {
      cuisine: "$_id",
      totalGrades: 1,
      gradeC: 1,
      probability: {
        $multiply: [
          { $divide: ["$gradeC", "$totalGrades"] },
          100
        ]
      }
    }
  },
  {
    $sort: { probability: -1 }
  },
  {
    $limit: 1
  }
]);

// Ejercicio 23: busco la evaluación más reciente
// Descompongo grades y ordeno por fecha descendente
db.restaurants.aggregate([
  {
    $unwind: "$grades"
  },
  {
    $sort: { "grades.date": -1 }
  },
  {
    $limit: 1
  }
]);

// Ejercicio 24: filtro específico + agregación
// Solo restaurantes turcos, luego busco el de mayor puntuación media
db.restaurants.aggregate([
  {
    $match: {
      cuisine: "Turkish"
    }
  },
  {
    $project: {
      name: 1,
      address: 1,
      avgScore: { $avg: "$grades.score" }
    }
  },
  {
    $sort: { avgScore: -1 }
  },
  {
    $limit: 1
  }
]);

// Ejercicio 25: extracción temporal
// $month saca el mes de una fecha, agrupo por eso para ver distribución mensual
db.restaurants.aggregate([
  {
    $unwind: "$grades"
  },
  {
    $group: {
      _id: { $month: "$grades.date" },
      count: { $sum: 1 }
    }
  },
  {
    $sort: { _id: 1 }
  },
  {
    $project: {
      month: "$_id",
      count: 1,
      _id: 0
    }
  }
]);

// Ejercicio 26: filtro complejo + agrupación
// Busco los que tienen A con nota >= 90, luego cuento por distrito
db.restaurants.aggregate([
  {
    $match: {
      "grades": {
        $elemMatch: {
          grade: "A",
          score: { $gte: 90 }
        }
      }
    }
  },
  {
    $group: {
      _id: "$borough",
      count: { $sum: 1 }
    }
  },
  {
    $sort: { count: -1 }
  },
  {
    $limit: 1
  }
]);

// Ejercicio 27: uso $filter para contar dentro de un array
// Cuento cuántas A tiene cada restaurante sin descomponer el array
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      borough: 1,
      gradeACount: {
        $size: {
          $filter: {
            input: "$grades",
            as: "grade",
            cond: { $eq: ["$$grade.grade", "A"] }
          }
        }
      }
    }
  },
  {
    $sort: { gradeACount: -1 }
  },
  {
    $limit: 10
  }
]);

// Ejercicio 28: suma total de puntuaciones
// En lugar de media, sumo todas las puntuaciones del array
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      cuisine: 1,
      borough: 1,
      totalScore: { $sum: "$grades.score" }
    }
  },
  {
    $sort: { totalScore: -1 }
  },
  {
    $limit: 10
  }
]);

// Ejercicio 29: ranking por categoría
// Para cada tipo de cocina, saco el top 5 de restaurantes por puntuación media
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      cuisine: 1,
      avgScore: { $avg: "$grades.score" }
    }
  },
  {
    $sort: { cuisine: 1, avgScore: -1 }
  },
  {
    $group: {
      _id: "$cuisine",
      restaurants: {
        $push: {
          name: "$name",
          avgScore: "$avgScore"
        }
      }
    }
  },
  {
    $project: {
      cuisine: "$_id",
      top5: { $slice: ["$restaurants", 5] }
    }
  },
  {
    $sort: { cuisine: 1 }
  }
]);

// Ejercicio 30: similar al 29 pero con número de A's por distrito
// Para cada distrito, top 5 restaurantes con más calificaciones A
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      borough: 1,
      gradeACount: {
        $size: {
          $filter: {
            input: "$grades",
            as: "grade",
            cond: { $eq: ["$$grade.grade", "A"] }
          }
        }
      }
    }
  },
  {
    $sort: { borough: 1, gradeACount: -1 }
  },
  {
    $group: {
      _id: "$borough",
      restaurants: {
        $push: {
          name: "$name",
          gradeACount: "$gradeACount"
        }
      }
    }
  },
  {
    $project: {
      borough: "$_id",
      top5: { $slice: ["$restaurants", 5] }
    }
  },
  {
    $sort: { borough: 1 }
  }
]);
