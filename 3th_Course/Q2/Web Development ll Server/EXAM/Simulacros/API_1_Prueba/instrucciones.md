Ejercicio 1 (10 Puntos)
Se propone desarrollar una API orientada a la gestión de incidencias del departamento de tecnología de una empresa. Se piden las siguientes características:
Dos rutas CRUD: /users y /tickets

Ruta /users: Debe permitir hacer Login a los usuarios existentes, y las siguientes operaciones para administradores (usuarios ya logados): obtener los usuarios existentes tanto de forma total como filtrando por ID, generar nuevos usuarios, actualizar información de estos y eliminarlos.
Ruta /tickets: Debe permitir obtener incidencias, tanto de forma total como por ID, a cualquier persona. Además de crear nuevas incidencias, actualizar las existentes o eliminarlas a los usuarios administradores (usuarios logados).

Información a gestionar en la ruta de usuarios:

Nombre de usuario
Correo electrónico
Nombre completo
Contraseña

Información a gestionar en la ruta de tickets:

Título de la incidencia
Descripción detallada
Prioridad (baja / media / alta / crítica)
Estado (abierta / en progreso / resuelta / cerrada)
Categoría (hardware / software / red / accesos / otro)
Fecha de apertura
Fecha de resolución (puede estar vacía)
Nombre del empleado afectado
Usuario técnico que gestiona el ticket
Solución aplicada (puede estar vacía)

Requisitos técnicos:

El enrutado será realizado mediante Express
Las peticiones a la API tendrán que estar correctamente validadas mediante express-validator
El almacenamiento de datos se realizará mediante Sequelize o Mongoose, a elección del alumno
La gestión de la autenticación será realizada mediante JWT y bcrypt
Se desarrollará una documentación básica de la API haciendo uso de Swagger



[1 Pto] Pregunta 1: Las rutas y sus correspondientes endpoints se han creado y configurado correctamente.
[1,5 Ptos] Pregunta 2: Se ha hecho uso de un ORM y un modelo de base de datos siguiendo las pautas establecidas.
[2 Ptos] Pregunta 3: Se han desarrollado las funcionalidades de los controladores necesarios.
[1 Pto] Pregunta 4: Todos los puntos de entrada de datos han sido validados correctamente.
[1,5 Ptos] Pregunta 5: Se ha desarrollado un sistema de login y creación de usuarios haciendo uso de JWT y bcrypt.
[1 Pto] Pregunta 6: Se ha desarrollado de forma correcta el sistema de permisos de la API.
[1 Pto] Pregunta 7: Se ha implementado una documentación de la API con Swagger.
[1 Pto] Pregunta 8: Se han realizado buenas prácticas de desarrollo y comprobación de errores.

