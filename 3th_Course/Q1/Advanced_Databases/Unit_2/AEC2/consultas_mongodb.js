// ============================================
// ACTIVIDAD PRÁCTICA: Derivación Logarítmica
// Consultas MongoDB - Restaurantes de Nueva York
// ============================================

// Usar la base de datos
use restaurantsNY;

// ============================================
// 1. Restaurantes con puntuación > 80 y < 100
// ============================================
db.restaurants.find({
  "grades.score": { $gt: 80, $lt: 100 }
}, {
  name: 1,
  cuisine: 1,
  borough: 1,
  "grades.score": 1
});

// Exportar: mongoexport --db=restaurantesNY --collection=restaurants --query='{"grades.score": {$gt: 80, $lt: 100}}' --out=ejercicio1.json

// ============================================
// 2. 5 restaurantes después de omitir los 5 primeros en el Bronx
// ============================================
db.restaurants.find({
  borough: "Bronx"
}).skip(5).limit(5);

// ============================================
// 3. Restaurantes cuyo segundo elemento de coord esté entre 42 y 52
// ============================================
db.restaurants.find({
  "address.coord.1": { $gt: 42, $lt: 52 }
}, {
  _id: 1,
  name: 1,
  address: 1,
  "address.coord": 1
});

// ============================================
// 4. Restaurantes cuya puntuación % 7 = 0
// ============================================
db.restaurants.find({
  "grades.score": { $mod: [7, 0] }
}, {
  _id: 1,
  name: 1,
  grades: 1
});

// ============================================
// 5. No cocina americana, nota 'A', no Brooklyn, orden descendente por cocina
// ============================================
db.restaurants.find({
  cuisine: { $ne: "American" },
  "grades.grade": "A",
  borough: { $ne: "Brooklyn" }
}).sort({ cuisine: -1 });

// ============================================
// 6. Al menos una 'A', sin 'B' ni 'C'
// ============================================
db.restaurants.find({
  "grades.grade": "A",
  "grades.grade": { $nin: ["B", "C"] }
}, {
  name: 1,
  address: 1,
  grades: 1
});

// Exportar: mongoexport --db=restaurantesNY --collection=restaurants --query='{"grades.grade": "A", "grades.grade": {$nin: ["B", "C"]}}' --out=ejercicio6.json

// ============================================
// 7. No americanos ni chinos O nombre empieza por "Wil"
// ============================================
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

// ============================================
// 8. Calificación 'A' y puntuación 11 en fecha específica
// ============================================
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

// ============================================
// 9. Segundo elemento del array con 'A', puntuación 9 y fecha específica
// ============================================
db.restaurants.find({
  "grades.1.grade": "A",
  "grades.1.score": 9,
  "grades.1.date": ISODate("2014-08-11T00:00:00Z")
}, {
  _id: 1,
  name: 1,
  grades: 1
});

// ============================================
// 10. Calificaciones de 2 y 6 en Manhattan o Brooklyn
// ============================================
db.restaurants.find({
  "grades.score": { $all: [2, 6] },
  borough: { $in: ["Manhattan", "Brooklyn"] }
});

// ============================================
// 11. Restaurantes con "coffee" en el nombre (case insensitive)
// ============================================
db.restaurants.find({
  name: /coffee/i
}, {
  name: 1,
  address: 1
});

// ============================================
// 12. Al menos una nota < 5 en Manhattan/Brooklyn, no americana ni china
// ============================================
db.restaurants.find({
  "grades.score": { $lt: 5 },
  borough: { $in: ["Manhattan", "Brooklyn"] },
  cuisine: { $nin: ["American", "Chinese"] }
});

// ============================================
// 13. Todas las notas > 5 en Manhattan o Brooklyn
// ============================================
db.restaurants.find({
  borough: { $in: ["Manhattan", "Brooklyn"] },
  "grades.score": { $not: { $lte: 5 } }
});

// Exportar: mongoexport --db=restaurantesNY --collection=restaurants --query='{"borough": {$in: ["Manhattan", "Brooklyn"]}, "grades.score": {$not: {$lte: 5}}}' --out=ejercicio13.json

// ============================================
// 14. Calificación 'B' o 'C' en una fecha determinada
// ============================================
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

// ============================================
// 15. Puntuación media de cada restaurante
// ============================================
db.restaurants.aggregate([
  {
    $project: {
      name: 1,
      avgScore: { $avg: "$grades.score" }
    }
  }
]);

// ============================================
// 16. Número de restaurantes por distrito
// ============================================
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

// ============================================
// 17. Número de restaurantes por tipo de cocina y distrito
// ============================================
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

// ============================================
// 18. Restaurantes con calificación 'A' por tipo de cocina y distrito
// ============================================
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

// ============================================
// 19. Puntuación más baja por tipo de cocina
// ============================================
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

// ============================================
// 20. Restaurantes cuyo código postal empieza por "10"
// ============================================
db.restaurants.find({
  "address.zipcode": /^10/
}, {
  name: 1,
  address: 1
});

// ============================================
// 21. Restaurantes con puntuación media más alta
// ============================================
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

// ============================================
// 22. Tipo de cocina con mayor probabilidad de recibir calificación 'C'
// ============================================
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

// ============================================
// 23. Restaurante con la fecha de calificación más reciente
// ============================================
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

// ============================================
// 24. Restaurante turco con puntuación media más alta
// ============================================
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

// ============================================
// 25. Número de restaurantes puntuados por mes del año
// ============================================
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

// ============================================
// 26. Distrito con más restaurantes con calificación 'A' y puntuación >= 90
// ============================================
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

// ============================================
// 27. Restaurantes con mayor número de calificaciones 'A'
// ============================================
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

// ============================================
// 28. Restaurantes con puntuación total más alta
// ============================================
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

// ============================================
// 29. Top 5 restaurantes por tipo de cocina con puntuación media más alta
// ============================================
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

// ============================================
// 30. Top 5 restaurantes por distrito con mayor número de calificaciones 'A'
// ============================================
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
