Ejemplo 1: Obtener todos los usuarios de una ciudad específica

Enunciado:
Listar todos los usuarios que viven en "Madrid".

db.usuarios.find({ciudad: "Madrid"})



Ejemplo 2: Obtener usuarios mayores de cierta edad

Enunciado:
Listar todos los usuarios mayores de 25 años.

db.usuarios.find({age: {$gt: 25}})



Ejemplo 3: Buscar usuarios por interés

Enunciado:
Obtener todos los usuarios que tengan "programación" entre sus intereses.

db.usuarios.find({intereses: "programación})



Ejemplo 4: Obtener usuarios activos

Enunciado:
Listar todos los usuarios cuyo campo activo sea true.

db.usuarios.find({activo: true})



Ejemplo 5: Proyección de campos

Enunciado:
Obtener solo el nombre y la ciudad de los usuarios activos, sin mostrar el _id.

db.usuarios.find(
    {activo:true},
    {nombre: 1, ciudad: 1, _id: 0}
)



Ejemplo 6: Buscar usuarios en varias ciudades

Enunciado:
Listar todos los usuarios que vivan en "Madrid" o "Barcelona".

db.usuarios.find({ciudad: {$in["Madrid", "Barcelona"]}})



Ejemplo 7: Buscar usuarios por múltiples condiciones

Enunciado:
Obtener usuarios que tengan más de 25 años y que sean activos.

db.usuarios.find(
    {active: true},
    edad: {$gt: 25}
)




Ejemplo 8: Buscar por patrón en texto

Enunciado:
Obtener usuarios cuyo nombre empiece por "Ism" (insensible a mayúsculas/minúsculas).

db.usuarios.find({nombre: {$regrex: "^ism", $options: 1}})




Ejemplo 9: Combinar $or

Enunciado:
Listar usuarios que sean menores de 20 años o que tengan "fútbol" entre sus intereses.

db.usuarios.find({
    $or: [
        {edad: { $lt: 20}}, 
        {intereses: "futbol"}
    ]
})


Ejemplo 10: Contar usuarios por ciudad (agregación simple)

Enunciado:
Contar cuántos usuarios hay en cada ciudad.

db.usuarios.aggregate([
    {$group: {_id: "$ciudad", totalUsuarios: { $sum: 1}}}
])



Ejemplo 11: Insertar documentos

Enunciado:
Agregar un nuevo usuario a la colección.

db.usuarios.insertOne({
    nombre:carla
    age:14
    ciudad: "valencia"
    intereses ["lectura", "programación"]
    activo: true
})




Ejemplo 12: Actualizar un campo

Enunciado:
Actualizar la ciudad de “Luis” a “Sevilla”.

db.usuarios.updateOne(
    {nombre: "Luis"}, 
    {$set: { ciudad: "Sevilla"}}
)




Ejemplo 13: Incrementar un valor

Enunciado:
Aumentar la edad de todos los usuarios activos en 1 año.

db.usuarios.updateMany(
    { activo: true},
    { $inc: { edad: 1}}
)



Ejemplo 14: Borrar documentos

Enunciado:
Eliminar todos los usuarios que no estén activos.

db.usuarios.deleteMany({
    activo:false
})

"usariamos deleteOne si solo quisieramos borrar uno"




Ejemplo 15: Ordenar y limitar resultados

Enunciado:
Obtener los 3 usuarios más jóvenes.

db.usuarios.find() <- no lo abrimos lo devolvemos en el cursos con .metodo
    .sort({edad: 1}) <- usamos 1 ascendente o -1 descendente
    .limit(3)